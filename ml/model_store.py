"""Persist / load trained pipelines and their metadata.

Artifacts live under ``ml/models/``:

    ml/models/{model_id}.joblib        fitted sklearn Pipeline
    ml/models/{model_id}.meta.json     training metadata + dev metrics
    ml/models/selected_model.json      id of the dev-best model (train-time choice)
    ml/models/evaluation_report.json   holdout evaluation (written by evaluate.py)

``model_id`` is a short identifier (``[A-Za-z0-9._-]+``) — e.g.
``match_result_logistic-v1.0.0`` — so files are safe on any filesystem and the
id round-trips cleanly through the ML contract's ``model_id`` field.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import joblib

MODELS_DIR = Path(__file__).resolve().parent / "models"
SELECTED_FILE = "selected_model.json"
EVALUATION_FILE = "evaluation_report.json"

_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")


def _id_path(model_id: str, ext: str) -> Path:
    if not _ID_PATTERN.match(model_id):
        raise ValueError(f"invalid model_id {model_id!r} (allowed: {_ID_PATTERN.pattern})")
    return MODELS_DIR / f"{model_id}.{ext}"


def save_model(model_id: str, pipeline, meta: dict) -> Path:
    """Serialize a fitted pipeline together with its metadata."""
    path = _id_path(model_id, "joblib")
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, path, compress=3)
    save_meta(model_id, meta)
    return path


def load_model(model_id: str):
    """Load a fitted pipeline (must have been trained for this feature_version)."""
    path = _id_path(model_id, "joblib")
    if not path.exists():
        raise FileNotFoundError(
            f"no model '{model_id}' at {path} — run `python3 ml/train.py` first"
        )
    return joblib.load(path)


def save_meta(model_id: str, meta: dict) -> Path:
    path = _id_path(model_id, "meta.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def load_meta(model_id: str) -> dict:
    path = _id_path(model_id, "meta.json")
    if not path.exists():
        raise FileNotFoundError(f"no metadata for model '{model_id}' at {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def list_models() -> list[str]:
    """Every stored model id (sorted by modification time, newest last)."""
    if not MODELS_DIR.is_dir():
        return []
    return sorted(
        p.stem for p in MODELS_DIR.glob("*.joblib")
        if (MODELS_DIR / f"{p.stem}.meta.json").exists()
    )


def save_selected(info: dict) -> Path:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    path = MODELS_DIR / SELECTED_FILE
    path.write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8")
    return path


def load_selected() -> dict:
    path = MODELS_DIR / SELECTED_FILE
    if not path.exists():
        raise FileNotFoundError(
            f"no {SELECTED_FILE} at {path} — run `python3 ml/train.py` first"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def evaluation_report_path() -> Path:
    return MODELS_DIR / EVALUATION_FILE
