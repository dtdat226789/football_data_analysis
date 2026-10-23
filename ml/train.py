"""Train match-result classifiers on the feature dataset.

Usage:  python3 ml/train.py

Pipeline:

  1. Load ``ml/datasets/match_result_dataset.json`` + ``split_manifest.json``.
  2. Temporal dev split for model selection: train on the first N-1 train
     seasons, validate on the last train season (2024-2025). The holdout
     season (2025-2026) is never touched here.
  3. Train two candidate pipelines:
        LogisticRegression (class_weight balanced, scaled)
        HistGradientBoostingClassifier   (sklearn built-in; no extra deps)
  4. Select the better by dev log-loss, retrain it on the full train window
     and serialize pipeline + metadata to ``ml/models/``. Both fully-trained
     candidates are kept so evaluate.py can compare them on the holdout.
  5. Record the dev-best in ``ml/models/selected_model.json``.

Exit code is 1 when the dataset is missing, a split is empty, or any step fails.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import HistGradientBoostingClassifier

from ml.contract import FEATURE_VERSION
from ml.model_store import save_model, save_selected
from ml import model_store
from ml.scoring import LABELS, majority_proba, metrics_report, split_rows, to_xy
from ml.features.build_features import FEATURE_COLUMNS
from ml.validation import DEFAULT_HOLDOUT_SEASONS, DEFAULT_TRAIN_SEASONS

ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "ml" / "datasets" / "match_result_dataset.json"
MANIFEST_PATH = ROOT / "ml" / "datasets" / "split_manifest.json"

SEED = 42
DEV_SEASON = "2024-2025"  # last train season, used only for model selection
IMPUTE_VALUE = 0.0        # rest-day NULLs -> 0, matching the documented NULL policy

MODEL_BUILDERS = {
    "logistic": lambda: Pipeline(
        [
            ("imputer", SimpleImputer(strategy="constant", fill_value=IMPUTE_VALUE)),
            ("scaler", StandardScaler()),
            (
                "clf",
                LogisticRegression(
                    class_weight="balanced",
                    max_iter=2000,
                    solver="lbfgs",
                    random_state=SEED,
                ),
            ),
        ]
    ),
    "hist_gb": lambda: Pipeline(
        [
            ("imputer", SimpleImputer(strategy="constant", fill_value=IMPUTE_VALUE)),
            ("clf", HistGradientBoostingClassifier(random_state=SEED, max_iter=200)),
        ]
    ),
}


def model_id(name: str) -> str:
    """Persistent, filesystem-safe identifier for a trained classifier."""
    return f"match_result_{name}-v{FEATURE_VERSION}"


def load_dataset(dataset_path: Path | None = None, manifest_path: Path | None = None) -> tuple[list[dict], list[str], list[str]]:
    """Rows + train/holdout season lists from the materialized artifacts.

    Defaults resolve the module globals at *call* time (not import time) so
    tests can redirect the artifacts by monkeypatching ``train.DATASET_PATH``.
    """
    dataset_path = dataset_path if dataset_path is not None else DATASET_PATH
    manifest_path = manifest_path if manifest_path is not None else MANIFEST_PATH
    if not dataset_path.exists():
        raise FileNotFoundError(f"dataset not found at {dataset_path} — run `python3 ml/build_dataset.py` first")
    rows = json.loads(dataset_path.read_text(encoding="utf-8"))
    if not rows:
        raise ValueError(f"dataset {dataset_path} is empty")
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    train_seasons = list(manifest.get("train_seasons") or DEFAULT_TRAIN_SEASONS)
    holdout_seasons = list(manifest.get("holdout_seasons") or DEFAULT_HOLDOUT_SEASONS)
    return rows, train_seasons, holdout_seasons


def split_rows_for_dev(rows: list[dict], train_seasons: list[str], dev_season: str = DEV_SEASON) -> tuple[list[dict], list[dict]]:
    """Dev window: train on all train seasons before ``dev_season``, validate on it."""
    if dev_season not in train_seasons:
        raise ValueError(f"dev season '{dev_season}' not among train seasons {train_seasons}")
    dev_train_seasons = [s for s in train_seasons if s != dev_season]
    dev_train, dev_val = split_rows(rows, dev_train_seasons, [dev_season])
    return dev_train, dev_val


def train_candidates(
    X: np.ndarray, y: np.ndarray, X_val: np.ndarray, y_val: np.ndarray
) -> dict[str, dict]:
    """Fit every candidate on the dev window and score it on the dev validation set."""
    results: dict[str, dict] = {}
    for name, builder in MODEL_BUILDERS.items():
        pipeline = builder()
        pipeline.fit(X, y)
        report = metrics_report(y_val, pipeline.predict_proba(X_val))
        results[name] = {
            "model_id": model_id(name),
            "classifier": pipeline.named_steps["clf"].__class__.__name__,
            "dev_log_loss": report["log_loss"],
            "dev_accuracy": report["accuracy"],
            "dev_macro_f1": report["macro_f1"],
            "dev_brier": report["brier"],
            "dev_ece": report["ece"],
        }
    return results


def main(argv: list[str] | None = None) -> int:
    rows, train_seasons, holdout_seasons = load_dataset()
    train_rows, holdout_rows = split_rows(rows, train_seasons, holdout_seasons)
    dev_train, dev_val = split_rows_for_dev(rows, train_seasons)
    if not dev_train or not dev_val:
        print(f"ERROR: dev split empty (train={len(dev_train)}, val={len(dev_val)}); dataset seasons: "
              f"{sorted({r['season'] for r in rows})}")
        return 1

    X, y = to_xy(dev_train, FEATURE_COLUMNS)
    X_val, y_val = to_xy(dev_val, FEATURE_COLUMNS)

    print(f"dev train: {len(X)} rows ({[s for s in train_seasons if s != DEV_SEASON]})")
    print(f"dev val  : {len(X_val)} rows ([{DEV_SEASON}])")
    print(f"holdout  : {len(train_rows) - len(X)} rows already set aside for 2025-2026")
    print()

    dev_results = train_candidates(X, y, X_val, y_val)

    header = f"{'model':<10} {'dev log_loss':>12} {'accuracy':>9} {'macro_f1':>9} {'brier':>8} {'ece':>7}"
    print(header)
    print("-" * len(header))
    for name, res in dev_results.items():
        print(
            f"{name:<10} {res['dev_log_loss']:>12.4f} {res['dev_accuracy']:>9.4f} "
            f"{res['dev_macro_f1']:>9.4f} {res['dev_brier']:>8.4f} {res['dev_ece']:>7.4f}"
        )

    majority = majority_proba(y)
    base_report = metrics_report(y_val, np.repeat(majority[None, :], len(y_val), axis=0))
    print(f"{'majority':<10} {base_report['log_loss']:>12.4f} {base_report['accuracy']:>9.4f} "
          f"{base_report['macro_f1']:>9.4f} {base_report['brier']:>8.4f} {base_report['ece']:>7.4f}")

    best_name = min(dev_results, key=lambda n: dev_results[n]["dev_log_loss"])
    print(f"\nselected by dev log-loss: {best_name} ({dev_results[best_name]['model_id']})")

    X_full, y_full = to_xy(train_rows, FEATURE_COLUMNS)
    for name, res in dev_results.items():
        pipeline = MODEL_BUILDERS[name]()
        pipeline.fit(X_full, y_full)
        save_model(
            res["model_id"],
            pipeline,
            {
                "model_id": res["model_id"],
                "feature_version": FEATURE_VERSION,
                "classifier": pipeline.named_steps["clf"].__class__.__name__,
                "columns": list(FEATURE_COLUMNS),
                "labels": list(LABELS),
                "imputation": {"strategy": "constant", "fill_value": IMPUTE_VALUE},
                "selected": name == best_name,
                "seed": SEED,
                "train_seasons": list(train_seasons),
                "holdout_seasons": list(holdout_seasons),
                "n_train_rows": int(len(X_full)),
                "n_holdout_rows": int(len(holdout_rows)),
                "dev_split": {"train_seasons": [s for s in train_seasons if s != DEV_SEASON], "val_season": DEV_SEASON},
                "dev_metrics": dev_results[name],
                "trained_at": datetime.now(timezone.utc).isoformat(),
            },
        )
        print(f"saved {res['model_id']} -> {model_store.MODELS_DIR}")
    save_selected(
        {
            "model_id": dev_results[best_name]["model_id"],
            "selected_by": "dev_log_loss",
            "dev_season": DEV_SEASON,
            "dev_log_loss": dev_results[best_name]["dev_log_loss"],
            "feature_version": FEATURE_VERSION,
        }
    )
    print(f"selected -> {model_store.MODELS_DIR / 'selected_model.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
