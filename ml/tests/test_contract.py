"""Tests for the ML prediction contract (ml/contract).

DB-free, network-free. Verifies:

  - MatchFeatures field parity with the feature-layer registries
  - per-column types / nullability following the validation contract
  - ranges mirroring the validation checks
  - every PredictionResponse invariant
  - JSON Schema exports on disk stay in sync with the models and validate rows
"""
from __future__ import annotations

import json
from typing import Optional

import jsonschema
import pytest
from pydantic import ValidationError

from ml.contract import (
    CONFIDENCE_TOLERANCE,
    FEATURE_VERSION,
    SCHEMAS_DIR,
    MatchFeatures,
    MatchOutcome,
    PredictionRequest,
    PredictionResponse,
    REST_COLUMNS,
    export_schemas,
)
from ml.features.build_features import CONTEXT_COLUMNS, FEATURE_COLUMNS


def _default_feature(col: str):
    if col in REST_COLUMNS:
        return 7
    if col.endswith("_win_rate"):
        return 0.5
    if col.endswith("_position_before_match"):
        return 1
    return 0


def build_row():
    """A valid match row covering exactly CONTEXT_COLUMNS + FEATURE_COLUMNS."""
    row = {}
    for col in CONTEXT_COLUMNS:
        if col in ("league", "season", "match_date"):
            row[col] = {"league": "premier", "season": "2020-2021", "match_date": "2021-01-01"}[col]
        elif col in ("home_team", "away_team"):
            row[col] = "T1"
        else:
            row[col] = 1
    for col in FEATURE_COLUMNS:
        row[col] = _default_feature(col)
    return row


def build_response(**overrides):
    base = {
        "probabilities": {"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.2},
        "predicted_match_result": "DRAW",
        "confidence": 0.3,
    }
    base.update(overrides)
    return base


# ---------------------------------------------------------------------------
# MatchFeatures: field parity with the registries
# ---------------------------------------------------------------------------

def test_match_features_exactly_context_plus_feature_columns():
    expected = list(CONTEXT_COLUMNS) + list(FEATURE_COLUMNS)
    got = list(MatchFeatures.model_fields)
    missing = sorted(set(expected) - set(got))
    extra = sorted(set(got) - set(expected))
    assert missing == [], f"contract missing columns: {missing}"
    assert extra == [], f"contract has unexpected columns: {extra}"
    assert got == expected, "contract column order differs from the registries"
    assert len(got) == len(CONTEXT_COLUMNS) + len(FEATURE_COLUMNS)


def test_context_columns_typed_per_registry():
    assert MatchFeatures.model_fields["api_id"].annotation is int
    assert MatchFeatures.model_fields["game_index"].annotation is int
    assert MatchFeatures.model_fields["league"].annotation is str
    assert MatchFeatures.model_fields["match_date"].annotation is str
    assert MatchFeatures.model_fields["home_team_games_before"].annotation is int


def test_rest_columns_nullable_ints():
    for col in sorted(REST_COLUMNS):
        assert MatchFeatures.model_fields[col].annotation == Optional[int], col


# ---------------------------------------------------------------------------
# MatchFeatures: validation of rows
# ---------------------------------------------------------------------------

def test_valid_row_validates():
    mf = MatchFeatures.model_validate(build_row())
    assert mf.api_id == 1
    assert mf.home_team_home_win_rate == 0.5


def test_rest_nulls_accepted_only_in_rest_group():
    row = build_row()
    row["home_rest_days"] = None
    row["rest_days_difference"] = None
    MatchFeatures.model_validate(row)  # must not raise


def test_null_outside_rest_group_rejected():
    row = build_row()
    row["home_team_points_last_5"] = None
    with pytest.raises(ValidationError):
        MatchFeatures.model_validate(row)


def test_out_of_range_win_rate_rejected():
    row = build_row()
    row["home_team_home_win_rate"] = 1.5
    with pytest.raises(ValidationError):
        MatchFeatures.model_validate(row)

    row = build_row()
    row["away_team_away_win_rate"] = -0.1
    with pytest.raises(ValidationError):
        MatchFeatures.model_validate(row)


def test_negative_position_rejected():
    row = build_row()
    row["away_position_before_match"] = 0
    with pytest.raises(ValidationError):
        MatchFeatures.model_validate(row)


# ---------------------------------------------------------------------------
# PredictionRequest
# ---------------------------------------------------------------------------

def test_prediction_request_nested_validation():
    req = PredictionRequest(features=build_row())
    assert isinstance(req.features, MatchFeatures)
    assert req.model_id is None

    req = PredictionRequest(features=build_row(), model_id="xgb-v1")
    assert req.model_id == "xgb-v1"


def test_prediction_request_rejects_bad_features():
    bad = build_row()
    bad["home_team_id"] = "not-an-int"
    with pytest.raises(ValidationError):
        PredictionRequest(features=bad)


# ---------------------------------------------------------------------------
# PredictionResponse invariants
# ---------------------------------------------------------------------------

def test_valid_prediction_response():
    res = PredictionResponse(**build_response())
    assert res.model_id is None
    assert res.feature_version == FEATURE_VERSION
    assert res.generated_at is not None


def test_probabilities_keys_exact():
    payload = build_response(probabilities={"HOME_WIN": 1.0, "AWAY_WIN": 0.0})
    with pytest.raises(ValidationError):
        PredictionResponse(**payload)

    payload = build_response(probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.2, "EXTRA": 0.0})
    with pytest.raises(ValidationError):
        PredictionResponse(**payload)


def test_probabilities_must_sum_to_one():
    payload = build_response(probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.1})
    with pytest.raises(ValidationError, match="sum to 1"):
        PredictionResponse(**payload)


def test_probabilities_out_of_range_rejected():
    payload = build_response(probabilities={"HOME_WIN": 1.4, "DRAW": -0.2, "AWAY_WIN": -0.2})
    with pytest.raises(ValidationError, match="must be in"):
        PredictionResponse(**payload)


def test_confidence_range():
    payload = build_response(confidence=1.5)
    with pytest.raises(ValidationError, match="must be in"):
        PredictionResponse(**payload)


def test_confidence_equals_predicted_probability():
    payload = build_response(predicted_match_result="DRAW", confidence=0.5)
    with pytest.raises(ValidationError, match="confidence"):
        PredictionResponse(**payload)


def test_confidence_tolerance_respected():
    payload = build_response(
        probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.2},
        predicted_match_result="DRAW",
        confidence=0.3 + CONFIDENCE_TOLERANCE / 2,
    )
    PredictionResponse(**payload)  # within tolerance -> ok


def test_match_outcome_validates():
    out = MatchOutcome(match_result="HOME_WIN", home_score=2, away_score=0)
    assert out.match_result.value == "HOME_WIN"
    with pytest.raises(ValidationError):
        MatchOutcome(match_result="TIE", home_score=0, away_score=0)
    with pytest.raises(ValidationError):
        MatchOutcome(match_result="DRAW", home_score=-1, away_score=-1)


# ---------------------------------------------------------------------------
# JSON Schema exports
# ---------------------------------------------------------------------------

def test_committed_schemas_in_sync(tmp_path):
    """Regenerate the schemas and require the committed files to match exactly."""
    export_schemas(tmp_path)
    for name in ("features.schema.json", "request.schema.json", "response.schema.json"):
        committed = (SCHEMAS_DIR / name).read_text(encoding="utf-8")
        regenerated = (tmp_path / name).read_text(encoding="utf-8")
        assert committed == regenerated, f"{name} is stale — run `python3 -m ml.contract`"


def test_export_schemas_writes_all_files(tmp_path):
    out = export_schemas(tmp_path)
    assert out == tmp_path
    for name in ("features.schema.json", "request.schema.json", "response.schema.json"):
        assert (out / name).is_file()


def test_exported_features_schema_matches_models(tmp_path):
    export_schemas(tmp_path)
    current = MatchFeatures.model_json_schema()
    exported = json.loads((tmp_path / "features.schema.json").read_text(encoding="utf-8"))
    assert exported == current


def test_features_schema_validates_good_and_bad_rows():
    schema = json.loads((SCHEMAS_DIR / "features.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=build_row(), schema=schema)

    bad = build_row()
    bad["home_team_home_win_rate"] = 1.7
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(instance=bad, schema=schema)


def test_response_schema_validates_payload():
    schema = json.loads((SCHEMAS_DIR / "response.schema.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=PredictionResponse(**build_response()).model_dump(mode="json"), schema=schema)