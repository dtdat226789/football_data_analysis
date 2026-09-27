"""Tests for ml/backfill_predictions.py.

Guards the two properties that matter for the match-detail page:
  * the artifact is keyed by api_id and carries the model metadata, and
  * training seasons are marked in_sample so the UI can badge them honestly.
"""
from __future__ import annotations

import json

import pytest

from ml import backfill_predictions as bp
from ml.predict import PredictionResponse


class _FakeResult:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return iter(self._data)


def _row(api_id: int, season: str):
    return {"api_id": api_id, "season": season, "match_result": "DRAW"}


@pytest.fixture(autouse=True)
def _stub_score(monkeypatch):
    def fake_score(rows, model_id=None, **kwargs):
        return [
            PredictionResponse(
                probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.2},
                predicted_match_result="HOME_WIN",
                confidence=0.5,
                model_id="m-1",
                feature_version="1.1.0",
            )
            for _ in rows
        ]

    monkeypatch.setattr(bp, "score_rows", fake_score)
    return fake_score


def test_payload_keys_by_api_id_as_string():
    # JSON object keys are strings; the API looks up str(api_id).
    rows = [_row(1, "2024-2025"), _row(2, "2025-2026")]
    payload = bp.build_payload(rows, "m-1", ["2025-2026"])
    assert set(payload["matches"]) == {"1", "2"}


def test_in_sample_marks_training_seasons_only():
    rows = [_row(1, "2024-2025"), _row(2, "2025-2026"), _row(3, "2023-2024")]
    payload = bp.build_payload(rows, "m-1", ["2025-2026"])
    assert payload["matches"]["1"]["in_sample"] is True
    assert payload["matches"]["2"]["in_sample"] is False
    assert payload["matches"]["3"]["in_sample"] is True
    assert payload["holdout_seasons"] == ["2025-2026"]


def test_payload_carries_model_and_honesty_metadata():
    payload = bp.build_payload([_row(1, "2025-2026")], "m-1", ["2025-2026"])
    assert payload["model_id"] == "m-1"
    assert payload["feature_version"] == "1.1.0"
    assert payload["n_matches"] == 1
    assert "in-sample" in payload["in_sample_warning"]


def test_actual_result_is_recorded_alongside_the_prediction():
    payload = bp.build_payload([_row(1, "2025-2026")], "m-1", ["2025-2026"])
    entry = payload["matches"]["1"]
    assert entry["actual_match_result"] == "DRAW"
    assert entry["predicted_match_result"] == "HOME_WIN"


def test_length_mismatch_refuses_to_write(monkeypatch):
    # A silent zip() truncation would leave some matches with no prediction.
    monkeypatch.setattr(bp, "score_rows", lambda rows, *a, **k: [])
    with pytest.raises(ValueError, match="refusing to write"):
        bp.build_payload([_row(1, "2024-2025")], "m-1", [])


def test_load_dataset_reads_json(tmp_path):
    p = tmp_path / "d.json"
    p.write_text(json.dumps([_row(7, "2025-2026")]))
    assert bp.load_dataset(p)[0]["api_id"] == 7


def test_load_dataset_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError, match="build_dataset"):
        bp.load_dataset(tmp_path / "nope.json")


def test_main_writes_artifact(tmp_path, monkeypatch):
    out = tmp_path / "preds.json"
    rows = [_row(1, "2024-2025"), _row(2, "2025-2026")]
    monkeypatch.setattr(bp, "load_dataset", lambda *a, **k: rows)
    monkeypatch.setattr(bp, "resolve_model_id", lambda mid=None: "m-1")

    meta = tmp_path / "meta.json"
    meta.write_text(json.dumps({"holdout_seasons": ["2025-2026"]}))
    monkeypatch.setattr(bp.model_store, "_id_path", lambda *a, **k: meta)

    assert bp.main(["--out", str(out)]) == 0
    payload = json.loads(out.read_text())
    assert payload["n_matches"] == 2
    assert payload["matches"]["2"]["in_sample"] is False


def test_main_reports_missing_model_metadata(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(bp, "resolve_model_id", lambda mid=None: "m-1")
    monkeypatch.setattr(
        bp.model_store, "_id_path", lambda *a, **k: tmp_path / "absent.json"
    )
    assert bp.main(["--out", str(tmp_path / "x.json")]) == 1
    assert "no metadata" in capsys.readouterr().out
