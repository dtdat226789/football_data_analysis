"""Tests for the match insights endpoint (routers/matches.py).

The pre-match grouping and the JSON-artifact fallbacks are pure and always run.
The DB-backed route runs when PostgreSQL is reachable, otherwise skipped.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.common as common  # noqa: E402
from apps.routers import matches  # noqa: E402
from apps.main import app  # noqa: E402
from ml.features.build_features import FEATURE_COLUMNS  # noqa: E402


# Context columns that exist in the dataset but are deliberately not model
# features (workload is display-only; the model does not consume it).
_CONTEXT_ONLY_COLUMNS = {"home_team_games_before", "away_team_games_before"}


# ── column-name contract ────────────────────────────────────────────────────
def test_pre_match_group_keys_are_real_dataset_columns():
    # Regression: the group keys were written as abbreviations (home_wins_last_5)
    # instead of the real column names (home_team_wins_last_5). Nothing raised;
    # form and venue groups just silently rendered empty. Pin every key to a
    # real column so a rename cannot pass unnoticed again.
    used = [col for fields in matches._PRE_MATCH_GROUPS.values() for col, _ in fields]
    assert used, "no pre-match columns declared"
    known = set(FEATURE_COLUMNS) | _CONTEXT_ONLY_COLUMNS
    unknown = sorted(set(used) - known)
    assert unknown == [], f"not real dataset columns: {unknown}"


def test_dataset_row_satisfies_every_group_key():
    # The stronger end of the contract: if a real dataset is present, every key
    # must actually resolve in it, so an empty panel cannot ship.
    dataset = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
    if not dataset.exists():
        pytest.skip("dataset not built")
    rows = [r for r in json.loads(dataset.read_text()) if r.get("game_index", 0) > 20]
    if not rows:
        pytest.skip("no mid-season rows")
    panel = matches.build_pre_match(rows[0])
    assert isinstance(panel, dict) and panel, "build_pre_match returned nothing"
    for group, fields in matches._PRE_MATCH_GROUPS.items():
        missing = [
            col for col, _ in fields if col not in rows[0] or rows[0][col] is None
        ]
        assert not missing, f"{group} empty for a mid-season row: {missing}"


def test_every_group_has_a_display_label():
    assert set(matches._PRE_MATCH_GROUPS) == set(matches.PRE_MATCH_GROUP_LABELS)


def test_pre_match_never_exposes_the_result():
    # A feature panel that leaked the outcome would be a data-integrity bug.
    forbidden = {"home_score", "away_score", "match_result"}
    used = {col for fields in matches._PRE_MATCH_GROUPS.values() for col, _ in fields}
    assert used & forbidden == set()


# ── build_pre_match ─────────────────────────────────────────────────────────
def _dataset_row():
    return {
        "api_id": 1,
        "season": "2024-2025",
        "game_index": 20,
        "home_team": "Arsenal",
        "away_team": "Chelsea",
        "home_team_id": 1,
        "away_team_id": 2,
        "home_team_points_last_5": 10,
        "away_team_points_last_5": 7,
        "home_team_wins_last_5": 3,
        "away_team_wins_last_5": 2,
        "home_team_goals_scored_last_5": 8,
        "away_team_goals_scored_last_5": 5,
        "home_team_goals_conceded_last_5": 2,
        "away_team_goals_conceded_last_5": 4,
        "home_team_home_win_rate": 0.7,
        "home_team_home_goals_avg": 2.1,
        "home_team_home_conceded_avg": 0.9,
        "away_team_away_win_rate": 0.5,
        "away_team_away_goals_avg": 1.4,
        "away_team_away_conceded_avg": 1.2,
        "home_position_before_match": 2,
        "away_position_before_match": 5,
        "position_difference": -3,
        "home_points_before_match": 40,
        "away_points_before_match": 33,
        "points_difference": 7,
        "home_rest_days": 4,
        "away_rest_days": 7,
        "rest_days_difference": -3,
        "home_team_games_before": 19,
        "away_team_games_before": 19,
    }


def test_build_pre_match_populates_every_group():
    out = matches.build_pre_match(_dataset_row())
    assert set(out["groups"]) == set(matches._PRE_MATCH_GROUPS)
    assert out["groups"]["form_last_5"]["home_team_wins_last_5"]["value"] == 3
    assert out["groups"]["form_last_5"]["home_team_wins_last_5"]["label"] == "Home wins (last 5)"


def test_build_pre_match_omits_null_columns():
    row = _dataset_row()
    row["home_rest_days"] = None  # season opener
    out = matches.build_pre_match(row)
    assert "home_rest_days" not in out["groups"]["rest"]
    assert "away_rest_days" in out["groups"]["rest"]


def test_build_pre_match_handles_absent_row():
    assert matches.build_pre_match(None) is None


# ── JSON artifact loading ───────────────────────────────────────────────────
def test_load_json_index_missing_file_is_empty(tmp_path):
    assert matches._load_json_index(tmp_path / "nope.json", "matches") == {}


def test_load_json_index_corrupt_file_is_empty(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not json")
    assert matches._load_json_index(bad, "matches") == {}


def test_load_json_index_ignores_wrong_shape(tmp_path):
    p = tmp_path / "p.json"
    p.write_text(json.dumps({"matches": ["not", "a", "dict"]}))
    assert matches._load_json_index(p, "matches") == {}


def test_artifact_is_parsed_once_and_shared_by_index_and_meta(tmp_path, monkeypatch):
    """A match detail must cost one read of the predictions file, not one per section.

    Both the stored prediction and the model header used to be produced by
    separate read_bytes()+json.loads() calls on the same ~0.8 MB file, on every
    request, while the larger dataset was memoized.
    """
    p = tmp_path / "preds.json"
    p.write_text(
        json.dumps(
            {
                "model_id": "m-1",
                "feature_version": "1.1.0",
                "holdout_seasons": ["2025-2026"],
                "in_sample_warning": "w",
                "matches": {"7": {"raw": {}, "calibrated": {}}},
            }
        )
    )
    monkeypatch.setattr(matches, "PREDICTIONS_JSON", p)
    expected_index = {"7": {"raw": {}, "calibrated": {}}}
    expected_meta = {
        "model_id": "m-1",
        "feature_version": "1.1.0",
        "holdout_seasons": ["2025-2026"],
        "in_sample_warning": "w",
    }

    reads: list[Path] = []
    original = Path.read_bytes

    def counting_read_bytes(self: Path):
        reads.append(self)
        return original(self)

    monkeypatch.setattr(Path, "read_bytes", counting_read_bytes)
    matches.clear_artifact_cache()
    try:
        # Same two calls the endpoint makes, three times over.
        for _ in range(3):
            assert matches._load_json_index(matches.PREDICTIONS_JSON, "matches") == expected_index
            assert matches._predictions_meta() == expected_meta
    finally:
        monkeypatch.undo()
        matches.clear_artifact_cache()

    assert len(reads) == 1


def test_dataset_index_survives_a_top_level_dict(tmp_path, monkeypatch):
    """The dataset is a list; a dict artifact must not crash the index build."""
    p = tmp_path / "dataset.json"
    p.write_text(json.dumps({"matches": [{"api_id": 7}]}))
    monkeypatch.setattr(matches, "DATASET_JSON", p)
    matches.clear_artifact_cache()
    try:
        assert matches._dataset_index() == {}
    finally:
        monkeypatch.undo()
        matches.clear_artifact_cache()


def test_predictions_meta_is_none_when_the_artifact_is_absent(tmp_path, monkeypatch):
    monkeypatch.setattr(matches, "PREDICTIONS_JSON", tmp_path / "gone.json")
    matches.clear_artifact_cache()
    try:
        assert matches._predictions_meta() is None
    finally:
        monkeypatch.undo()
        matches.clear_artifact_cache()


def test_clear_artifact_cache_forces_a_reread(tmp_path):
    p = tmp_path / "p.json"
    p.write_text(json.dumps({"matches": {"1": {"v": 1}}}))
    matches.clear_artifact_cache()
    try:
        assert matches._load_json_index(p, "matches") == {"1": {"v": 1}}
        p.write_text(json.dumps({"matches": {"1": {"v": 2}}}))
        assert matches._load_json_index(p, "matches") == {"1": {"v": 1}}, "should be cached"
        matches.clear_artifact_cache()
        assert matches._load_json_index(p, "matches") == {"1": {"v": 2}}
    finally:
        matches.clear_artifact_cache()


# ── endpoint ────────────────────────────────────────────────────────────────
def _live_client() -> TestClient:
    try:
        from db_common import get_conn

        conn = get_conn()
    except Exception as exc:  # pragma: no cover - environment dependent
        pytest.skip(f"PostgreSQL unavailable: {exc}")
    conn.close()
    return TestClient(app)


def test_insights_returns_all_three_sections():
    client = _live_client()
    dataset = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
    if not dataset.exists():
        pytest.skip("dataset not built")
    rows = json.loads(dataset.read_text())
    api_id = next(r["api_id"] for r in rows if r.get("season") and r.get("game_index", 0) > 5)

    body = client.get(f"/api/v1/matches/{api_id}/insights").json()
    assert body["api_id"] == api_id
    assert body["pre_match"]["groups"], "expected a populated pre-match panel"
    assert body["head_to_head"]["matches"] is not None
    assert "limit" in body["head_to_head"]
    if body["model"] is not None:
        assert set(body["model"]["probabilities"]) <= {"HOME_WIN", "DRAW", "AWAY_WIN"}
        assert body["model"]["in_sample"] in (True, False)


def test_insights_404s_for_unknown_match():
    client = _live_client()
    assert client.get("/api/v1/matches/999999999/insights").status_code == 404


def test_insights_excludes_the_match_itself_and_later_meetings():
    # A head-to-head list that includes this fixture, or a future one, leaks
    # information the page is supposed to present as "prior".
    client = _live_client()
    dataset = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
    if not dataset.exists():
        pytest.skip("dataset not built")
    rows = json.loads(dataset.read_text())
    api_id = rows[0]["api_id"]
    body = client.get(f"/api/v1/matches/{api_id}/insights").json()
    prior = body["head_to_head"]["matches"]
    assert api_id not in [m["api_id"] for m in prior]
    if prior:
        latest = max(m["match_date"] for m in prior)
        assert body["match"]["match_date"] > latest


def test_h2h_summary_counts_all_meetings_not_just_the_page():
    # The table is capped by ?limit; the summary must still cover every prior
    # meeting, and must admit that the table is partial.
    client = _live_client()
    dataset = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
    if not dataset.exists():
        pytest.skip("dataset not built")
    api_id = json.loads(dataset.read_text())[0]["api_id"]

    body = client.get(f"/api/v1/matches/{api_id}/insights?limit=1").json()
    h2h = body["head_to_head"]
    summary = h2h["summary"]
    if summary is None:
        assert h2h["matches"] == []
        return
    assert len(h2h["matches"]) <= 1
    assert summary["played"] >= len(h2h["matches"])
    assert (
        summary["home_team_wins"] + summary["draws"] + summary["away_team_wins"]
        == summary["played"]
    )
    assert h2h["truncated"] is (summary["played"] > len(h2h["matches"]))


def test_insights_limit_is_clamped():
    client = _live_client()
    dataset = common.ROOT_DIR / "ml" / "datasets" / "match_result_dataset.json"
    if not dataset.exists():
        pytest.skip("dataset not built")
    api_id = json.loads(dataset.read_text())[0]["api_id"]
    body = client.get(f"/api/v1/matches/{api_id}/insights?limit=9999").json()
    assert body["head_to_head"]["limit"] <= 25
