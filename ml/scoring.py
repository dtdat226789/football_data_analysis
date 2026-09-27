"""Metric, baseline and dataset helpers shared by train.py / evaluate.py.

This module is the single source of truth for how model quality is measured,
so train and evaluate cannot drift apart. It is deliberately small and pure:

  * ``encode_labels`` maps the string ``match_result`` labels to the integer
    codes used by the numpy/scikit-learn helpers;
  * ``log_loss`` / ``brier`` / ``ece`` score a probability matrix;
  * ``metrics_report`` bundles every useful number into one JSON-able dict;
  * ``majority_proba`` / ``always_home_proba`` give trivial baselines every
    model must beat;
  * ``split_rows`` / ``to_xy`` / ``to_feature_matrix`` turn the materialized
    feature rows into train/val/holdout matrices, encoding the NULL rest days
    as NaN so an in-pipeline imputer can fill them exactly like training.

The canonical label order is ``["HOME_WIN", "DRAW", "AWAY_WIN"]``. Scikit-learn
orders ``predict_proba`` columns alphabetically; callers must zip ``model.classes_``
with the probabilities (see ``ml/predict.py``) rather than assume an order.
"""
from __future__ import annotations

from typing import Sequence

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    log_loss as sklearn_log_loss,
    precision_recall_fscore_support,
)

# Canonical label order; matches ml.features.build_features.MATCH_RESULTS keys.
LABELS = ["HOME_WIN", "DRAW", "AWAY_WIN"]

_LABEL_INDEX = {label: i for i, label in enumerate(LABELS)}


def encode_labels(labels: Sequence[str]) -> np.ndarray:
    """Map the string result labels to integer codes in LABELS order."""
    return np.array([_LABEL_INDEX[label] for label in labels], dtype=int)


def _as_matrix(y_true: Sequence[int] | np.ndarray, y_score: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    yt = np.asarray(y_true, dtype=int)
    ys = np.asarray(y_score, dtype=float)
    if ys.ndim != 2 or ys.shape[1] != len(LABELS):
        raise ValueError(f"y_score must be a (n, {len(LABELS)}) probability matrix, got shape {ys.shape}")
    if len(yt) != ys.shape[0]:
        raise ValueError(f"y_true ({len(yt)}) and y_score ({ys.shape[0]}) length mismatch")
    return yt, ys


def accuracy(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
    return float(accuracy_score(np.asarray(y_true), np.asarray(y_pred)))


def macro_f1(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
    return float(f1_score(np.asarray(y_true), np.asarray(y_pred), average="macro", zero_division=0))


def log_loss(y_true: Sequence[int], y_score: np.ndarray) -> float:
    yt, ys = _as_matrix(y_true, y_score)
    return float(sklearn_log_loss(yt, ys, labels=list(range(len(LABELS)))))


def brier(y_true: Sequence[int], y_score: np.ndarray) -> float:
    """Multiclass Brier score: mean over samples of the squared 0-1 loss per class."""
    yt, ys = _as_matrix(y_true, y_score)
    onehot = np.zeros_like(ys)
    onehot[np.arange(len(yt)), yt] = 1.0
    return float(np.mean(np.sum((onehot - ys) ** 2, axis=1)))


def ece(y_true: Sequence[int], y_score: np.ndarray, n_bins: int = 10) -> float:
    """Expected calibration error on the predicted (argmax) class confidence."""
    yt, ys = _as_matrix(y_true, y_score)
    conf = ys.max(axis=1)
    pred = ys.argmax(axis=1)
    correct = (pred == yt).astype(float)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_idx = np.clip(np.digitize(conf, edges, right=True) - 1, 0, n_bins - 1)
    out = 0.0
    n_samples = float(len(conf))
    for b in range(n_bins):
        mask = bin_idx == b
        n = int(mask.sum())
        if n == 0:
            continue
        out += (n / n_samples) * abs(float(correct[mask].mean()) - float(conf[mask].mean()))
    return float(out)


def confusion_matrix(y_true: Sequence[int], y_pred: Sequence[int]) -> dict:
    """Confusion matrix labelled by LABELS: rows actual, columns predicted."""
    yt = np.asarray(y_true, dtype=int)
    yp = np.asarray(y_pred, dtype=int)
    k = len(LABELS)
    mat = np.zeros((k, k), dtype=int)
    for a, p in zip(yt, yp):
        mat[a, p] += 1
    return {"labels": list(LABELS), "matrix": mat.tolist()}


def per_class_metrics(y_true: Sequence[int], y_pred: Sequence[int]) -> dict:
    """Precision/recall/F1/support for every label."""
    yt = np.asarray(y_true, dtype=int)
    yp = np.asarray(y_pred, dtype=int)
    precision, recall, f1, support = precision_recall_fscore_support(
        yt, yp, labels=list(range(len(LABELS))), average=None, zero_division=0
    )
    return {
        label: {
            "precision": float(p),
            "recall": float(r),
            "f1": float(f),
            "support": int(s),
        }
        for label, p, r, f, s in zip(LABELS, precision, recall, f1, support)
    }


def metrics_report(y_true: Sequence[int], y_score: np.ndarray) -> dict:
    """The standard quality report for a probability matrix vs. actuals."""
    yt, ys = _as_matrix(y_true, y_score)
    y_pred = ys.argmax(axis=1).tolist()
    return {
        "accuracy": accuracy(yt, y_pred),
        "macro_f1": macro_f1(yt, y_pred),
        "log_loss": log_loss(yt, ys),
        "brier": brier(yt, ys),
        "ece": ece(yt, ys),
        "per_class": per_class_metrics(yt, y_pred),
        "confusion_matrix": confusion_matrix(yt, y_pred),
        "degenerate_label_set": len(np.unique(yt)) == 1,
        "n": int(len(yt)),
    }


# ---------------------------------------------------------------------------
# Baselines: every real model must beat these trivial references.
# ---------------------------------------------------------------------------

def majority_proba(y_train: Sequence[int]) -> np.ndarray:
    """Constant probabilities equal to the training-set class frequencies."""
    yt = np.asarray(y_train, dtype=int)
    counts = np.array([float(np.sum(yt == i)) for i in range(len(LABELS))])
    total = counts.sum()
    return (counts / total) if total else np.ones(len(LABELS)) / len(LABELS)


def always_home_proba() -> np.ndarray:
    """Constant 100% HOME_WIN — captures that home advantage dominates."""
    p = np.zeros(len(LABELS))
    p[_LABEL_INDEX["HOME_WIN"]] = 1.0
    return p


def baseline_report(y_true: Sequence[int], proba: np.ndarray) -> dict:
    """Score the trivial baselines against the same actuals for comparison."""
    yt, _ = _as_matrix(y_true, np.repeat(proba[None, :], len(y_true), axis=0))
    report = metrics_report(yt, np.repeat(proba[None, :], len(yt), axis=0))
    report["description"] = "constant class frequencies" if not _is_home(proba) else "always predict HOME_WIN"
    return report


def _is_home(proba: np.ndarray) -> bool:
    return bool(np.argmax(proba) == _LABEL_INDEX["HOME_WIN"]) and proba[_LABEL_INDEX["HOME_WIN"]] == 1.0


# ---------------------------------------------------------------------------
# Row helpers (materialized dataset -> numpy matrices)
# ---------------------------------------------------------------------------

def split_rows(rows: list[dict], train_seasons: Sequence[str], holdout_seasons: Sequence[str]) -> tuple[list[dict], list[dict]]:
    """Split feature rows by season (never by row)."""
    train_set, holdout_set = set(train_seasons), set(holdout_seasons)
    overlap = train_set & holdout_set
    if overlap:
        raise ValueError(f"season assigned to both train and holdout: {sorted(overlap)}")
    return (
        [r for r in rows if r["season"] in train_set],
        [r for r in rows if r["season"] in holdout_set],
    )


def to_xy(rows: list[dict], feature_cols: Sequence[str], label_col: str = "match_result") -> tuple[np.ndarray, np.ndarray]:
    """Feature matrix + encoded labels for labelled dataset rows."""
    X = to_feature_matrix(rows, feature_cols)
    y = encode_labels([r[label_col] for r in rows])
    return X, y


def to_feature_matrix(rows: list[dict], feature_cols: Sequence[str]) -> np.ndarray:
    """Float feature matrix; NULL rest days become NaN (imputed in-pipeline)."""
    if not rows:
        return np.empty((0, len(feature_cols)), dtype=float)
    cols = list(feature_cols)
    out = np.empty((len(rows), len(cols)), dtype=float)
    for row_idx, row in enumerate(rows):
        for col_idx, col in enumerate(cols):
            value = row[col]
            out[row_idx, col_idx] = float("nan") if value is None else float(value)
    return out