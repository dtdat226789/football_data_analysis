"""DB-free tests for ml/train.py, ml/model_store.py and their wiring.

Uses a tiny synthetic dataset so the *full* train main() (dev split, model
selection, serialization) can be exercised end-to-end in a temp dir.
"""
from __future__ import annotations

import json

import numpy as np
import pytest

from ml.features.build_features import FEATURE_COLUMNS
from ml.contract import FEATURE_VERSION
from ml import model_store
from ml import train

from ml.train import (
    MODEL_BUILDERS,
    load_dataset,
    model_id,
    split_rows_for_dev,
    train_candidates,
)


def make_rows(n_per_season: int = 24, seed: int = 7) -> list[dict]:
    """Synthetic feature rows with a learnable home-strength signal."""
    rng = np.random.default_rng(seed)
    rows = []
    for season in ["2020-2021", "2023-2024", "2024-2025"]:
        for i in range(n_per_season):
            home_strength = float(rng.normal(0.0, 1.0))
            away_strength = float(rng.normal(0.0, 1.0))
            logit = home_strength - away_strength
            p = [1 / (1 + np.exp(-logit)), 0.33, 1 / (1 + np.exp(logit))]
            p = np.array(p) / sum(p)
            label = ["HOME_WIN", "DRAW", "AWAY_WIN"][int(rng.choice(3, p=p))]
            row = {"season": season, "match_result": label}
            for col in FEATURE_COLUMNS:
                row[col] = None if col.endswith("rest_days") else 0.0
            row["points_difference"] = 2.0 * np.sign(home_strength - away_strength)
            row["position_difference"] = -3.0 * np.sign(home_strength - away_strength)
            row["home_team_home_win_rate"] = max(0.0, min(1.0, 0.5 + 0.2 * home_strength))
            row["away_team_away_win_rate"] = max(0.0, min(1.0, 0.5 - 0.2 * away_strength))
            if i > 0:  # season openers (i == 0) keep NULL rest, like the real policy
                row["home_rest_days"] = 5
                row["away_rest_days"] = 5
                row["rest_days_difference"] = 0
            rows.append(row)
    # holdout season with a handful of rows
    for i in range(10):
        row = {"season": "2025-2026", "match_result": ["HOME_WIN", "DRAW", "AWAY_WIN"][i % 3]}
        for col in FEATURE_COLUMNS:
            row[col] = None if col.endswith("rest_days") else 0.0
        if i > 0:
            row["home_rest_days"] = 5
            row["away_rest_days"] = 5
            row["rest_days_difference"] = 0
        rows.append(row)
    return rows


@pytest.fixture()
def tiny_dataset(tmp_path):
    manifest = {
        "train_seasons": ["2020-2021", "2023-2024", "2024-2025"],
        "holdout_seasons": ["2025-2026"],
    }
    ds = tmp_path / "match_result_dataset.json"
    mf = tmp_path / "split_manifest.json"
    ds.write_text(json.dumps(make_rows()))
    mf.write_text(json.dumps(manifest))
    return ds, mf


# ---------------------------------------------------------------------------
# load_dataset
# ---------------------------------------------------------------------------

def test_load_dataset_reads_manifest_over_defaults(tiny_dataset):
    ds, mf = tiny_dataset
    rows, train_seasons, holdout_seasons = load_dataset(ds, mf)
    assert len(rows) == 82
    assert train_seasons == ["2020-2021", "2023-2024", "2024-2025"]
    assert holdout_seasons == ["2025-2026"]


def test_load_dataset_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_dataset(tmp_path / "nope.json", tmp_path / "nope.json")


def test_load_dataset_empty_raises(tmp_path):
    empty = tmp_path / "empty.json"
    empty.write_text("[]")
    with pytest.raises(ValueError, match="empty"):
        load_dataset(empty, tmp_path / "missing.json")


# ---------------------------------------------------------------------------
# dev split
# ---------------------------------------------------------------------------

def test_split_rows_for_dev_excludes_dev_season_from_train():
    rows = [{"season": s, "i": i} for i, s in enumerate(
        ["2020-2021"] * 5 + ["2023-2024"] * 5 + ["2024-2025"] * 5)]
    dev_train, dev_val = split_rows_for_dev(rows, ["2020-2021", "2023-2024", "2024-2025"])
    assert len(dev_train) == 10
    assert len(dev_val) == 5
    assert all(r["season"] == "2024-2025" for r in dev_val)


def test_split_rows_for_dev_requires_dev_season():
    with pytest.raises(ValueError, match="not among"):
        split_rows_for_dev([], ["2020-2021", "2023-2024"])


# ---------------------------------------------------------------------------
# pipelines + candidate training
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name", list(MODEL_BUILDERS))
def test_pipeline_fits_imputes_and_returns_probabilities(name):
    rows = make_rows(24)
    seasons = ["2020-2021", "2023-2024", "2024-2025"]
    tr, va = split_rows_for_dev(rows, seasons)
    from ml.scoring import to_xy
    X, y = to_xy(tr, FEATURE_COLUMNS)
    X_val, y_val = to_xy(va, FEATURE_COLUMNS)
    pipeline = MODEL_BUILDERS[name]()
    pipeline.fit(X, y)
    proba = pipeline.predict_proba(X_val)
    assert proba.shape == (len(va), 3)
    np.testing.assert_allclose(proba.sum(axis=1), 1.0, atol=1e-6)


def test_train_candidates_reports_dev_metrics_and_model_ids():
    rows = make_rows(24)
    tr, va = split_rows_for_dev(rows, ["2020-2021", "2023-2024", "2024-2025"])
    from ml.scoring import to_xy
    X, y = to_xy(tr, FEATURE_COLUMNS)
    X_val, y_val = to_xy(va, FEATURE_COLUMNS)
    results = train_candidates(X, y, X_val, y_val)
    assert set(results) == set(MODEL_BUILDERS)
    assert results["logistic"]["model_id"].startswith("match_result_logistic-")
    assert 0.0 <= results["logistic"]["dev_log_loss"] <= 1.5


def test_model_id_contains_feature_version():
    assert model_id("hist_gb").endswith(f"-v{FEATURE_VERSION}")


# ---------------------------------------------------------------------------
# end-to-end train main() against a temp dataset + temp models dir
# ---------------------------------------------------------------------------

def test_train_main_end_to_end(tiny_dataset, tmp_path, monkeypatch):
    ds, mf = tiny_dataset
    monkeypatch.setattr(train, "DATASET_PATH", ds)
    monkeypatch.setattr(train, "MANIFEST_PATH", mf)
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path / "models")

    assert train.main([]) == 0

    selected = json.loads((tmp_path / "models" / "selected_model.json").read_text())
    assert selected["model_id"] in {
        f"match_result_logistic-v{FEATURE_VERSION}",
        f"match_result_hist_gb-v{FEATURE_VERSION}",
    }
    artifact = tmp_path / "models" / f"{selected['model_id']}.joblib"
    assert artifact.exists()
    meta = json.loads((tmp_path / "models" / f"{selected['model_id']}.meta.json").read_text())
    assert meta["model_id"] == selected["model_id"]
    assert set(meta["columns"]) == set(FEATURE_COLUMNS)
    assert meta["n_train_rows"] == 72
    assert meta["n_holdout_rows"] == 10


# ---------------------------------------------------------------------------
# model_store
# ---------------------------------------------------------------------------

def test_model_store_round_trip(monkeypatch, tmp_path):
    from sklearn.linear_model import LogisticRegression
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path)
    pipeline = LogisticRegression(max_iter=200)
    pipeline.fit([[0.0, 1.0], [1.0, 0.0]], ["HOME_WIN", "AWAY_WIN"])
    model_store.save_model("m-test", pipeline, {"model_id": "m-test", "columns": ["a", "b"]})
    loaded = model_store.load_model("m-test")
    assert loaded.predict([[1.0, 0.0]])[0] == "AWAY_WIN"
    assert model_store.load_meta("m-test")["columns"] == ["a", "b"]
    assert "m-test" in model_store.list_models()


def test_model_store_rejects_unsafe_ids(monkeypatch, tmp_path):
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path)
    for bad in ("../escape", "a/b", "x y"):
        with pytest.raises(ValueError):
            model_store.save_model(bad, object(), {})


def test_model_store_missing_model_raises(monkeypatch, tmp_path):
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path)
    with pytest.raises(FileNotFoundError, match="train.py"):
        model_store.load_model("does-not-exist")


def test_selected_round_trip(monkeypatch, tmp_path):
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path)
    with pytest.raises(FileNotFoundError, match="train.py"):
        model_store.load_selected()
    model_store.save_selected({"model_id": "m-x"})
    assert model_store.load_selected() == {"model_id": "m-x"}
