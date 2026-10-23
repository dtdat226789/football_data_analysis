"""Predict match results from pre-match features.

Usage:
    python3 ml/predict.py --features <rows.json>            score contract rows
    python3 ml/predict.py --league premier                  score upcoming fixtures
    python3 ml/predict.py --league premier --out preds.json
    python3 ml/predict.py --model-id match_result_logistic-v1.0.0 --features rows.json

Two mutually-exclusive input modes:

Mode A ``--features``
    The file holds one ``MatchFeatures`` row, a JSON array of them, or an
    object with a ``matches``/``rows`` array. Rows must carry the full
    context + features block the ML contract requires (api_id, season, ...);
    every row is validated with ``MatchFeatures`` before scoring.

Mode B ``--league <api_key>``
    Reads ``data/raw/fixtures/{league}.json`` (the fetch_fixtures.py dump of
    *scheduled* matches), resolves teams through ``team_aliases``, builds the
    same leakage-safe pre-match features by
    ``build_features.build_fixture_rows`` (which never applies the fixtures'
    results), and scores them. Fixtures whose teams are unknown in the identity
    bridge are reported as skipped rather than silently dropped.

Output is a JSON envelope ``{"mode", "model_id", "feature_version", "count",
"predictions": [...]}``. Each element in ``predictions`` carries the fixture
context plus a validated ``PredictionResponse``.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np

from ml import model_store
from ml.contract import FEATURE_VERSION, PredictionResponse, MatchFeatures
from ml.features.build_features import FEATURE_COLUMNS, build_fixture_rows
from ml.scoring import LABELS, to_feature_matrix

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = ROOT / "data" / "raw" / "fixtures"


def probability_map(row_proba: np.ndarray, classes: list[str]) -> dict[str, float]:
    """zip the model's label order to {label: probability}."""
    probs = {label: float(p) for label, p in zip(classes, row_proba)}
    total = sum(probs.values()) or 1.0
    return {label: p / total for label, p in probs.items()}


def _class_facing_labels(classes) -> list[str]:
    """Map the classifier's ``classes_`` to the canonical string labels.

    Training feeds integer-encoded codes (see ``ml/scoring.to_xy``), so a
    reloaded pipeline's ``classes_`` are ``[0, 1, 2]`` — the *positions* in
    ``LABELS``. External models fitted directly on strings keep their labels.
    """
    first = classes[0] if len(classes) else None
    if isinstance(first, (int, np.integer)):
        return [LABELS[int(c)] for c in classes]
    return list(classes)


def score_rows(rows: list[dict], model_id: str) -> list[PredictionResponse]:
    """Score pre-match feature rows with a stored model."""
    if not rows:
        return []
    pipeline = model_store.load_model(model_id)
    X = to_feature_matrix(rows, FEATURE_COLUMNS)
    proba = pipeline.predict_proba(X)
    classes = _class_facing_labels(pipeline.classes_)
    responses = []
    for row_proba in proba:
        probabilities = probability_map(row_proba, classes)
        predicted = max(probabilities, key=probabilities.get)
        responses.append(
            PredictionResponse(
                probabilities=probabilities,
                predicted_match_result=predicted,
                confidence=probabilities[predicted],
                model_id=model_id,
                feature_version=FEATURE_VERSION,
            )
        )
    return responses


# ---------------------------------------------------------------------------
# Mode A: score feature rows from a file
# ---------------------------------------------------------------------------

def load_feature_rows(path: Path) -> list[dict]:
    """Read a features file into a list of contract-validated row dicts."""
    if not path.exists():
        raise FileNotFoundError(f"features file not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        for key in ("matches", "rows", "features", "predictions"):
            if key in payload and isinstance(payload[key], list):
                payload = payload[key]
                break
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        raise ValueError(f"unrecognized features payload in {path} (expected a row, a list, or {{matches/rows: [...]}})")
    return [MatchFeatures.model_validate(row).model_dump() for row in payload]


# ---------------------------------------------------------------------------
# Mode B: build features for upcoming fixtures and score them
# ---------------------------------------------------------------------------

def load_fixtures(league: str) -> list[dict]:
    """Scheduled fixtures for a league from the fetch_fixtures.py dump."""
    path = FIXTURES_DIR / f"{league}.json"
    if not path.exists():
        raise FileNotFoundError(
            f"no fixtures dump at {path} — run `python backend/scripts/fetch_fixtures.py --league {league}`"
        )
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("matches") or []


def predict_fixtures(league: str, model_id: str) -> dict:
    """Build + score features for a league's scheduled fixtures."""
    fixtures = load_fixtures(league)
    if not fixtures:
        return {
            "mode": "league",
            "league": league,
            "model_id": model_id,
            "feature_version": FEATURE_VERSION,
            "count": 0,
            "predictions": [],
            "skipped": [],
        }

    from ml import db

    conn = db.get_conn()
    try:
        rows, skipped = build_fixture_rows(conn, fixtures, league)
    finally:
        conn.close()

    responses = score_rows(rows, model_id)
    predictions = []
    for row, response in zip(rows, responses):
        predictions.append(
            {
                "league": league,
                "home_team": row.get("home_team"),
                "away_team": row.get("away_team"),
                "match_date": row.get("match_date"),
                "prediction": response.model_dump(mode="json"),
            }
        )
    return {
        "mode": "league",
        "league": league,
        "model_id": model_id,
        "feature_version": FEATURE_VERSION,
        "count": len(predictions),
        "predictions": predictions,
        "skipped": skipped,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="ml.predict",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--features", metavar="JSON", help="features file to score (Mode A)")
    group.add_argument("--league", metavar="API_KEY", help="league slug for scheduled fixtures (Mode B)")
    parser.add_argument("--model-id", default=None, help="stored model to use (default: dev-best from train.py)")
    parser.add_argument("--out", metavar="JSON", default=None, help="write the envelope to this file (default: stdout)")
    return parser.parse_args(argv)


def resolve_model_id(model_id: str | None) -> str:
    if model_id is not None:
        return model_id
    return model_store.load_selected()["model_id"]


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        model_id = resolve_model_id(args.model_id)
        if args.features is not None:
            rows = load_feature_rows(Path(args.features))
            responses = score_rows(rows, model_id)
            payload = _envelope("features", None, model_id, rows, responses)
        else:
            payload = predict_fixtures(args.league, model_id)
    except (FileNotFoundError, ValueError, LookupError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {len(payload['predictions'])} prediction(s) to {args.out}")
    else:
        sys.stdout.write(text)
    return 0


def _envelope(mode: str, league: str | None, model_id: str, rows: list[dict], responses: list) -> dict:
    predictions = []
    for row, response in zip(rows, responses):
        predictions.append(
            {
                "league": row.get("league"),
                "season": row.get("season"),
                "api_id": row.get("api_id"),
                "home_team": row.get("home_team"),
                "away_team": row.get("away_team"),
                "match_date": row.get("match_date"),
                "prediction": response.model_dump(mode="json"),
            }
        )
    return {
        "mode": mode,
        "league": league,
        "model_id": model_id,
        "feature_version": FEATURE_VERSION,
        "count": len(predictions),
        "predictions": predictions,
    }


if __name__ == "__main__":
    sys.exit(main())
