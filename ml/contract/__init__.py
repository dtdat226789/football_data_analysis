"""ML prediction contract — schemas + invariants for the match-result model.

Single source of truth for the shapes the classifier will exchange:

* ``MatchFeatures``   one pre-match feature row (context + features only)
* ``MatchOutcome``    the observed result of the same fixture
* ``PredictionRequest``  a fixture to score with an optional model_id
* ``PredictionResponse`` the scored probabilities + invariants

Field definitions are **derived** from the feature-layer registries in
``ml.features.build_features`` (never hand-duplicated), so the contract cannot
silently drift from the pipeline. Feature columns are typed as follows:

* all numeric features are ``float`` except the rest group, which is
  ``int | None`` (NULL only before a season opener — the existing validation
  contract, see ``ml/validation.py``);
* context identifiers are ``int`` / ``str`` according to their meaning.

JSON Schema exports live in ``ml/contract/schemas/`` and are regenerated with::

    python3 -m ml.contract
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, create_model, model_validator

from ml.features.build_features import CONTEXT_COLUMNS, FEATURE_COLUMNS

# Explicit version of the feature set/semantics. Bump whenever a feature is
# added, renamed, or its meaning changes (this also bumps every PredictionResponse).
FEATURE_VERSION = "1.0.0"

# Prediction invariants: probabilities and confidence live in [0, 1]; the
# probabilities sum to 1 within this tolerance and confidence equals the
# predicted probability within this tolerance.
PROB_MIN = 0.0
PROB_MAX = 1.0
PROB_SUM_TOLERANCE = 1e-3
CONFIDENCE_TOLERANCE = 1e-3

# Rest days are the only features legitimately absent before a season opener.
REST_COLUMNS = frozenset({"home_rest_days", "away_rest_days", "rest_days_difference"})


class MatchResult(str, Enum):
    """Label of a match result (matches the dataset's ``match_result``)."""
    HOME_WIN = "HOME_WIN"
    DRAW = "DRAW"
    AWAY_WIN = "AWAY_WIN"


MATCH_RESULT_LABELS = {mr.value for mr in MatchResult}

# ---------------------------------------------------------------------------
# MatchFeatures — derived from the feature-layer registries
# ---------------------------------------------------------------------------

# Per-column Python annotations for the fixed context block.
_CONTEXT_TYPES: dict[str, type] = {
    "api_id": int,
    "league": str,
    "season": str,
    "game_index": int,
    "home_team_id": int,
    "home_team": str,
    "away_team_id": int,
    "away_team": str,
    "match_date": str,
    "home_team_games_before": int,
    "away_team_games_before": int,
}

if set(_CONTEXT_TYPES) != set(CONTEXT_COLUMNS):
    raise AssertionError(
        "contract context type map drifted from CONTEXT_COLUMNS: "
        f"missing={sorted(set(CONTEXT_COLUMNS) - set(_CONTEXT_TYPES))} "
        f"extra={sorted(set(_CONTEXT_TYPES) - set(CONTEXT_COLUMNS))}"
    )


def _feature_annotation(column: str) -> type:
    return Optional[int] if column in REST_COLUMNS else float


def _feature_bounds(column: str) -> dict:
    """Bounds mirroring the range checks of ml/validation.py, derived by name."""
    if column.endswith("_win_rate"):
        return {"ge": PROB_MIN, "le": PROB_MAX}
    if column.endswith(("_goals_avg", "_conceded_avg")):
        return {"ge": 0.0}
    if column.endswith("_position_before_match"):
        return {"ge": 1}
    return {}


_fields: dict[str, tuple] = {}
for _col in CONTEXT_COLUMNS:
    _fields[_col] = (_CONTEXT_TYPES[_col], Field())
for _col in FEATURE_COLUMNS:
    _fields[_col] = (_feature_annotation(_col), Field(**_feature_bounds(_col)))

MatchFeatures = create_model("MatchFeatures", **{k: v for k, v in _fields.items()})
"""One pre-match feature row: exactly ``CONTEXT_COLUMNS + FEATURE_COLUMNS``."""


class MatchOutcome(BaseModel):
    """The observed result of a match (the prediction target)."""
    match_result: MatchResult
    home_score: int = Field(ge=0)
    away_score: int = Field(ge=0)


class PredictionRequest(BaseModel):
    """Score one fixture carrying pre-match features (and, optionally, a model)."""
    features: MatchFeatures
    model_id: Optional[str] = None


class PredictionResponse(BaseModel):
    """The model's prediction for a single fixture, with consistency invariants.

    Invariants enforced on construction:

    * ``probabilities`` holds exactly the keys ``HOME_WIN``, ``DRAW``,
      ``AWAY_WIN``, each in ``[0, 1]``;
    * probabilities sum to 1 (within ``PROB_SUM_TOLERANCE``);
    * ``confidence`` is in ``[0, 1]`` and equals the probability of the
      predicted result (within ``CONFIDENCE_TOLERANCE``).
    """
    probabilities: dict[str, float]
    predicted_match_result: MatchResult
    confidence: float
    model_id: Optional[str] = None
    feature_version: str = FEATURE_VERSION
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="after")
    def _check_probabilities_and_confidence(self) -> "PredictionResponse":
        got = set(self.probabilities)
        if got != MATCH_RESULT_LABELS:
            missing = sorted(MATCH_RESULT_LABELS - got)
            extra = sorted(got - MATCH_RESULT_LABELS)
            raise ValueError(
                "probabilities must hold exactly HOME_WIN/DRAW/AWAY_WIN"
                + (f"; missing {missing}" if missing else "")
                + (f"; unexpected {extra}" if extra else "")
            )
        if not all(PROB_MIN <= p <= PROB_MAX for p in self.probabilities.values()):
            raise ValueError(f"all probabilities must be in [{PROB_MIN}, {PROB_MAX}]")
        total = sum(self.probabilities.values())
        if abs(total - 1.0) > PROB_SUM_TOLERANCE:
            raise ValueError(f"probabilities must sum to 1 within {PROB_SUM_TOLERANCE} (got {total:.6f})")
        if not PROB_MIN <= self.confidence <= PROB_MAX:
            raise ValueError(f"confidence must be in [{PROB_MIN}, {PROB_MAX}]")
        expected = self.probabilities[self.predicted_match_result.value]
        if abs(self.confidence - expected) > CONFIDENCE_TOLERANCE:
            raise ValueError(
                f"confidence must equal the probability of the predicted result "
                f"(expected {expected:.6f}, got {self.confidence:.6f})"
            )
        return self


# ---------------------------------------------------------------------------
# JSON Schema export
# ---------------------------------------------------------------------------

SCHEMAS_DIR = Path(__file__).resolve().parent / "schemas"

_SCHEMA_FILES = {
    "features.schema.json": MatchFeatures,
    "request.schema.json": PredictionRequest,
    "response.schema.json": PredictionResponse,
}


def export_schemas(out_dir: Optional[Path | str] = None) -> Path:
    """Write the JSON Schema for every contract model to ``out_dir``.

    Defaults to ``ml/contract/schemas/``. Regenerate with ``python3 -m ml.contract``.
    """
    out = Path(out_dir) if out_dir is not None else SCHEMAS_DIR
    out.mkdir(parents=True, exist_ok=True)
    for name, model in _SCHEMA_FILES.items():
        (out / name).write_text(json.dumps(model.model_json_schema(), indent=2) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    _path = export_schemas()
    print(f"wrote ML contract schemas to {_path}")