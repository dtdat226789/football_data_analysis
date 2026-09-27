"""Score every materialized match and persist the probabilities to JSON.

Why a separate artifact instead of the API loading the model:

* ``ml/models/`` is gitignored, so a checkout may have no model at all. The API
  must degrade to "no prediction" rather than fail.
* The API already serves pre-computed ML output from JSON (see
  ``routers/fixtures.py``, which reads ``data/raw/fixtures/*.json``). Serving a
  JSON artifact keeps that boundary: the API never imports sklearn.

Honesty note: these are *in-sample* predictions for every training season. The
model memorised those matches, so their confidence is optimistic and must not
be read as out-of-sample skill. Only the holdout seasons are genuinely unseen.
Each entry therefore carries ``in_sample``, and the UI badges it.

Usage:
    python3 -m ml.backfill_predictions
    python3 -m ml.backfill_predictions --model-id match_result_logistic-v1.1.0
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from ml import model_store
from ml.predict import resolve_model_id, score_rows

ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT / "ml" / "datasets"
DATASET_JSON = DATASETS_DIR / "match_result_dataset.json"
PREDICTIONS_JSON = DATASETS_DIR / "match_predictions.json"


def build_payload(rows: list[dict], model_id: str, holdout_seasons: list[str]) -> dict:
    predictions = score_rows(rows, model_id)
    if len(predictions) != len(rows):
        raise ValueError(
            f"scored {len(predictions)} rows for {len(rows)} inputs; refusing to write"
        )

    holdout = set(holdout_seasons)
    matches: dict[str, dict] = {}
    for row, pred in zip(rows, predictions, strict=True):
        season = row.get("season")
        matches[str(row["api_id"])] = {
            "season": season,
            "probabilities": pred.probabilities,
            "predicted_match_result": pred.predicted_match_result,
            "confidence": pred.confidence,
            "actual_match_result": row.get("match_result"),
            "in_sample": season not in holdout,
        }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model_id": model_id,
        "feature_version": predictions[0].feature_version if predictions else None,
        "holdout_seasons": sorted(holdout),
        "in_sample_warning": (
            "Training-season rows are in-sample: the model was fitted on them, "
            "so their confidence is optimistic. Only holdout_seasons are "
            "out-of-sample."
        ),
        "n_matches": len(matches),
        "matches": matches,
    }


def load_dataset(path: Path = DATASET_JSON) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(
            f"dataset not found: {path}. Run 'python3 ml/build_dataset.py' first."
        )
    return json.loads(path.read_text())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-id", default=None, help="default: the selected model")
    parser.add_argument("--dataset", type=Path, default=DATASET_JSON)
    parser.add_argument("--out", type=Path, default=PREDICTIONS_JSON)
    args = parser.parse_args(argv)

    model_id = resolve_model_id(args.model_id)
    meta_path = model_store._id_path(model_id, "meta.json")
    if not meta_path.exists():
        print(f"error: no metadata for {model_id}; run 'python3 -m ml.train' first")
        return 1
    meta = json.loads(meta_path.read_text())

    rows = load_dataset(args.dataset)
    if not rows:
        print("error: dataset is empty")
        return 1

    payload = build_payload(rows, model_id, meta.get("holdout_seasons") or [])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2) + "\n")

    n_in = sum(1 for m in payload["matches"].values() if m["in_sample"])
    print(f"model    : {model_id} (feature_version {payload['feature_version']})")
    print(f"scored   : {payload['n_matches']} matches -> {args.out}")
    print(f"  in-sample (optimistic): {n_in}")
    print(f"  out-of-sample (holdout): {payload['n_matches'] - n_in}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
