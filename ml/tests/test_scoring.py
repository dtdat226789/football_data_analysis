"""DB-free tests for ml/scoring.py (metrics, baselines, matrix helpers).

Hand-built tiny matrices keep every expected value computable by hand.
"""
from __future__ import annotations

import json

import numpy as np
import pytest

from ml.scoring import (
    LABELS,
    always_home_proba,
    brier,
    confusion_matrix,
    ece,
    encode_labels,
    log_loss,
    macro_f1,
    majority_proba,
    metrics_report,
    per_class_metrics,
    split_rows,
    to_feature_matrix,
    to_xy,
)


def test_encode_labels_maps_to_canonical_order():
    y = encode_labels(["AWAY_WIN", "HOME_WIN", "DRAW", "HOME_WIN"])
    np.testing.assert_array_equal(y, [2, 0, 1, 0])


def test_encode_labels_rejects_unknown():
    with pytest.raises(KeyError):
        encode_labels(["TIE"])


def test_log_loss_perfect_is_zero():
    y_true = [0, 1, 2]
    y_score = np.eye(3)
    assert log_loss(y_true, y_score) == pytest.approx(0.0, abs=1e-6)


def test_brier_perfect_is_zero():
    y_true = [0, 1, 2]
    y_score = np.eye(3)
    assert brier(y_true, y_score) == pytest.approx(0.0, abs=1e-12)


def test_brier_worst_case_is_two():
    # Always certain and always wrong: per sample sum of (onehot-p)^2 = 1+1 = 2.
    y_true = [0, 1, 2]
    wrong = np.roll(np.eye(3), 1, axis=1)
    assert brier(y_true, wrong) == pytest.approx(2.0)


def test_macro_f1_binary_toy():
    y_true = [0, 0, 1]          # HOME_WIN, HOME_WIN, DRAW
    y_pred = [0, 1, 1]
    # Over the two *observed* classes only (sklearn macro behaviour):
    #   HOME_WIN: P=1, R=1/2 -> F1=2/3 ; DRAW: P=1/2, R=1 -> F1=2/3
    assert macro_f1(y_true, y_pred) == pytest.approx(2 / 3)


def test_ece_perfect_is_zero():
    y_score = np.eye(3)
    assert ece([0, 1, 2], y_score) == pytest.approx(0.0)


def test_ece_captures_overconfidence():
    # Always predicts super-confidently but is only 1/3 correct; all six rows
    # land in the same top bin, so ECE = bin_weight * |acc - conf| = 1 * |1/6 - 0.99|.
    y_true = [0, 1, 2, 1, 2, 2]
    y_score = np.array([[0.99, 0.005, 0.005]] * 6)
    assert ece(y_true, y_score, n_bins=10) == pytest.approx(abs(1 / 6 - 0.99), rel=1e-9)


def test_confusion_matrix_labels_and_counts():
    y_true = [0, 0, 1]
    y_pred = [1, 0, 1]
    out = confusion_matrix(y_true, y_pred)
    assert out["labels"] == LABELS
    np.testing.assert_array_equal(np.array(out["matrix"]), [[1, 1, 0], [0, 1, 0], [0, 0, 0]])


def test_per_class_metrics_reports_every_label():
    y_true = [0, 0, 1]
    y_pred = [0, 1, 1]
    out = per_class_metrics(y_true, y_pred)
    assert set(out) == set(LABELS)
    assert out["HOME_WIN"]["precision"] == pytest.approx(1.0)
    assert out["DRAW"]["recall"] == pytest.approx(1.0)
    assert out["AWAY_WIN"]["support"] == 0


def test_metrics_report_shape():
    y_true = [0, 1, 2, 0]
    y_score = np.array([[0.5, 0.3, 0.2], [0.2, 0.6, 0.2], [0.1, 0.2, 0.7], [0.4, 0.3, 0.3]])
    report = metrics_report(y_true, y_score)
    assert report["n"] == 4
    assert report["accuracy"] == 1.0
    # every predicted argmax matches its actual: diagonal confusion matrix
    mat = report["confusion_matrix"]["matrix"]
    assert mat[0] == [2, 0, 0]
    assert mat[1] == [0, 1, 0]
    assert mat[2] == [0, 0, 1]


# ---------------------------------------------------------------------------
# baselines
# ---------------------------------------------------------------------------

def test_majority_proba_are_train_frequencies():
    proba = majority_proba(np.array([0, 0, 0, 1, 2, 2]))
    np.testing.assert_allclose(proba, [0.5, 1 / 6, 1 / 3])


def test_always_home_proba_is_pure_home():
    p = always_home_proba()
    assert p.tolist() == [1.0, 0.0, 0.0]


# ---------------------------------------------------------------------------
# row helpers
# ---------------------------------------------------------------------------

def test_split_rows_by_season_never_by_row():
    rows = [
        {"season": "2020-2021", "x": 1},
        {"season": "2024-2025", "x": 2},
        {"season": "2025-2026", "x": 3},
    ]
    train, holdout = split_rows(rows, ["2020-2021", "2024-2025"], ["2025-2026"])
    assert [r["x"] for r in train] == [1, 2]
    assert [r["x"] for r in holdout] == [3]


def test_split_rows_rejects_overlap():
    rows = [{"season": "2020-2021", "x": 1}]
    with pytest.raises(ValueError, match="both train and holdout"):
        split_rows(rows, ["2020-2021"], ["2020-2021"])


def test_to_feature_matrix_encodes_null_as_nan():
    rows = [{"a": 1, "b": None, "c": 0.5}, {"a": 2, "b": 7, "c": 0.0}]
    X = to_feature_matrix(rows, ["a", "b", "c"])
    assert np.isnan(X[0, 1])
    assert X[1, 1] == 7.0
    assert X.shape == (2, 3)


def test_to_xy_empty_rows():
    X, y = to_xy([], ["a", "b"])
    assert X.shape == (0, 2)
    assert y.shape == (0,)


def test_to_feature_matrix_rejects_missing_key():
    with pytest.raises(KeyError):
        to_feature_matrix([{"a": 1}], ["a", "b"])


# ---------------------------------------------------------------------------
# JSON-ability of reports (they feed model_meta.json / evaluation_report.json)
# ---------------------------------------------------------------------------

def test_metrics_report_is_json_serializable():
    y_true = [0, 1, 2, 2, 1, 0, 0, 1]
    y_score = np.random.default_rng(0).dirichlet(alpha=[1.0, 1.0, 1.0], size=8)
    json.dumps(metrics_report(y_true, y_score))  # must not raise