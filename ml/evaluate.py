"""Evaluate a trained model on the holdout season.

Usage:  python3 ml/evaluate.py
        python3 ml/evaluate.py --model-id match_result_logistic-v1.0.0

The holdout season (2025-2026) is never seen during training; this script scores
it exactly once. Defaults to the dev-best model recorded by train.py
(``ml/models/selected_model.json``). Writes a JSON report to
``ml/models/evaluation_report.json`` and prints a compact summary.

Again: selecting a model or tuning on this report would leak holdout
information — treat it as a one-time final measurement.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np

from ml import model_store
from ml.contract import FEATURE_VERSION
from ml.features.build_features import FEATURE_COLUMNS
from ml.scoring import (
    always_home_proba,
    majority_proba,
    metrics_report,
    split_rows,
    to_xy,
)
from ml.train import load_dataset
from ml.model_store import evaluation_report_path, load_model, load_meta


def run_evaluation(model_id: str) -> dict:
    """Score the holdout season with a stored model and return the report."""
    rows, train_seasons, holdout_seasons = load_dataset()
    train_rows, holdout_rows = split_rows(rows, train_seasons, holdout_seasons)
    if not holdout_rows:
        raise ValueError(
            f"no rows in holdout seasons {holdout_seasons}; dataset seasons are "
            f"{sorted({r['season'] for r in rows})}"
        )

    X, y = to_xy(holdout_rows, FEATURE_COLUMNS)
    pipeline = load_model(model_id)
    y_score = pipeline.predict_proba(X)
    report = metrics_report(y, y_score)

    majority = majority_proba(to_xy(train_rows, FEATURE_COLUMNS)[1])

    def constant_proba(proba: np.ndarray) -> np.ndarray:
        return np.repeat(proba[None, :], len(y), axis=0)

    def baseline_numbers(proba: np.ndarray) -> dict:
        r = metrics_report(y, constant_proba(proba))
        return {"log_loss": r["log_loss"], "accuracy": r["accuracy"]}

    baselines = {
        "majority_class": baseline_numbers(majority),
        "always_home": baseline_numbers(always_home_proba()),
    }

    meta = load_meta(model_id)
    return {
        "model_id": model_id,
        "feature_version": FEATURE_VERSION,
        "classifier": meta.get("classifier"),
        "holdout_seasons": holdout_seasons,
        "n_holdout_rows": int(len(holdout_rows)),
        "train_seasons": train_seasons,
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "metrics": report,
        "baselines": baselines,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model-id",
        default=None,
        help="model id to evaluate (default: the dev-best model recorded by train.py)",
    )
    args = parser.parse_args(argv)

    model_id = args.model_id
    if model_id is None:
        model_id = model_store.load_selected()["model_id"]
    try:
        report = run_evaluation(model_id)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        return 1
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    evaluation_report_path().write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )

    m = report["metrics"]
    print(f"model        : {report['model_id']} ({report['classifier']})")
    print(f"holdout      : {report['holdout_seasons']} · {report['n_holdout_rows']} rows")
    print(f"accuracy     : {m['accuracy']:.4f}")
    print(f"macro_f1     : {m['macro_f1']:.4f}")
    print(f"log_loss     : {m['log_loss']:.4f}")
    print(f"brier        : {m['brier']:.4f}")
    print(f"ece          : {m['ece']:.4f}")
    for label, pc in m["per_class"].items():
        print(f"  {label:<10} precision={pc['precision']:.3f} recall={pc['recall']:.3f} f1={pc['f1']:.3f} (n={pc['support']})")
    print("baselines    : " + ", ".join(
        f"{name} acc={b['accuracy']:.4f} logloss={b['log_loss']:.4f}" for name, b in report["baselines"].items()
    ))
    print(f"report       : {evaluation_report_path()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())