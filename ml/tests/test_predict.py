"""DB-free tests for ml/predict.py and ml/features/fixtures.py.

The key property verified here: a scheduled fixture scored only from the prior
matches it can observe is *identical* to the feature row the dataset pipeline
builds for that exact match — i.e. predict produces the same view of the match
that training saw.
"""
from __future__ import annotations

import json
from datetime import date, time

import numpy as np
import pytest

from ml.contract import FEATURE_VERSION, MATCH_RESULT_LABELS, PredictionResponse
from ml.features.build_features import CONTEXT_COLUMNS, FEATURE_COLUMNS, process_season
from ml.features.fixtures import Fixture, score_fixtures, seed_season
from ml.predict import (
    load_feature_rows,
    probability_map,
    _envelope,
)
from ml.tests.test_features import make_season, mk


def context_row(api_id: int = 1, **overrides) -> dict:
    """A contract-valid MatchFeatures row (context + features only)."""
    row = {col: 1 for col in CONTEXT_COLUMNS}
    row.update(
        {
            "league": "premier",
            "season": "2020-2021",
            "match_date": "2021-01-05",
            "home_team": "T1",
            "away_team": "T2",
        }
    )
    for col in FEATURE_COLUMNS:
        if col.endswith("_win_rate"):
            row[col] = 0.5
        elif col.endswith("_position_before_match"):
            row[col] = 4
        else:
            row[col] = 0
    row["api_id"] = api_id
    row.update(overrides)
    return row


def tiny_fitted_pipeline():
    """A real fitted sklearn pipeline trained on integer-coded labels, exactly
    like ml/scoring.to_xy produces — so classes_ are [0, 1, 2]."""
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression

    rng = np.random.default_rng(3)
    X = rng.normal(size=(60, len(FEATURE_COLUMNS)))
    y = rng.integers(0, 3, size=60)
    return Pipeline(
        [("scaler", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))]
    ).fit(X, y)


# ---------------------------------------------------------------------------
# fixtures: leakage-safe scoring of scheduled matches
# ---------------------------------------------------------------------------

def test_fixture_features_equal_to_pipeline_rows_for_same_match():
    # Full 3-round season; treat round 3 as "scheduled".
    season = make_season("2020-2021")
    completed = season[:4]  # rounds 1-2
    round3 = season[4:]     # rounds to predict

    history, table, roster = seed_season(completed)
    fixtures = [
        Fixture(home_team_id=m.home_team_id, away_team_id=m.away_team_id, match_date=m.match_date)
        for m in round3
    ]
    fixture_rows = score_fixtures(history, table, roster, fixtures, league="premier")

    # The real pipeline scored the same matches within the full season — its
    # rows for round 3 must carry the same feature values.
    pipeline_rows = process_season(season, league="premier")
    for frow, m in zip(fixture_rows, round3):
        expected = next(r for r in pipeline_rows if (r["home_team_id"], r["away_team_id"]) == (m.home_team_id, m.away_team_id))
        for col in FEATURE_COLUMNS:
            assert frow[col] == expected[col], f"{col}: fixture {frow[col]} != pipeline {expected[col]}"


def test_fixture_observes_strictly_prior_results_only():
    # A 13:00 postponed match played on the same day as the 15:00 round is
    # observable (like the grouped pipeline: only equal kickoffs are
    # simultaneous). The fixture's own row is NOT applied back onto itself.
    season = make_season("2020-2021")
    completed = season[:4]
    early = mk(50, 1, 2, 2, 0, date(2021, 1, 15), kickoff=time(13, 0))

    history, table, roster = seed_season(completed + [early])
    rows = score_fixtures(
        history, table, roster,
        [Fixture(home_team_id=1, away_team_id=3, match_date=date(2021, 1, 15), kickoff_time=time(15, 0))],
    )
    row = rows[0]
    # team 1: 1v2 home win (D1)=3pts, 4v1 away loss (D2)=0pts, +3pts from the
    # early 13:00 win over team 2 on D3 => last-5 points = 6.
    assert row["home_team_points_last_5"] == 6


def test_fixture_with_no_prior_matches_uses_documented_defaults():
    # A brand-new/empty season: features must be 0 / 0.0 / NULL rest, matching
    # the season-opener policy rather than raising.
    season = make_season("2020-2021")
    history, table, roster = seed_season([])
    rows = score_fixtures(
        history, table, roster,
        [Fixture(season[0].home_team_id, season[0].away_team_id, season[0].match_date)],
    )
    assert len(rows) == 1
    row = rows[0]
    assert row["home_team_wins_last_5"] == 0
    assert row["home_team_home_win_rate"] == 0.0
    assert row["home_position_before_match"] == 1
    assert row["home_rest_days"] is None
    assert row["rest_days_difference"] is None


# ---------------------------------------------------------------------------
# predict: probability mapping + contract round-trips
# ---------------------------------------------------------------------------

def test_probability_map_maps_classes_and_normalizes():
    probs = probability_map(np.array([0.6, 0.3, 0.1]), ["DRAW", "AWAY_WIN", "HOME_WIN"])
    assert probs == {"DRAW": 0.6, "AWAY_WIN": 0.3, "HOME_WIN": 0.1}
    assert sum(probs.values()) == pytest.approx(1.0)


def test_score_rows_returns_valid_prediction_responses():
    rows = [context_row(api_id=1), context_row(api_id=2)]
    responses = _score_via_pipeline(rows)
    assert len(responses) == 2
    for r in responses:
        assert set(r.probabilities) == MATCH_RESULT_LABELS
        assert abs(sum(r.probabilities.values()) - 1.0) < 1e-3
        assert r.confidence == pytest.approx(r.probabilities[r.predicted_match_result.value])


def test_score_rows_loads_stored_model(monkeypatch, tmp_path):
    # score_rows() must pull the model from the model store (like the CLI path).
    from ml import model_store
    from ml.predict import score_rows

    pipeline = tiny_fitted_pipeline()
    monkeypatch.setattr(model_store, "MODELS_DIR", tmp_path / "models")
    model_store.save_model("m-smoke", pipeline, {"model_id": "m-smoke"})
    responses = score_rows([context_row(api_id=1)], "m-smoke")
    assert len(responses) == 1
    assert responses[0].model_id == "m-smoke"
    assert responses[0].feature_version == FEATURE_VERSION


def _score_via_pipeline(rows):
    """Score rows with a locally fitted pipeline (avoids disk/model-store)."""
    from ml.scoring import to_feature_matrix
    from ml.predict import _class_facing_labels
    pipeline = tiny_fitted_pipeline()
    X = to_feature_matrix(rows, FEATURE_COLUMNS)
    classes = _class_facing_labels(pipeline.classes_)
    responses = []
    for proba in pipeline.predict_proba(X):
        probabilities = probability_map(proba, classes)
        predicted = max(probabilities, key=probabilities.get)
        responses.append(
            PredictionResponse(
                probabilities=probabilities,
                predicted_match_result=predicted,
                confidence=probabilities[predicted],
                model_id="test",
                feature_version=FEATURE_VERSION,
            )
        )
    return responses


def test_prediction_response_validates_sum_and_confidence():
    from pydantic import ValidationError

    ok = PredictionResponse(
        probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.2},
        predicted_match_result="DRAW",
        confidence=0.3,
    )
    assert ok.confidence == 0.3
    with pytest.raises(ValidationError):
        PredictionResponse(
            probabilities={"HOME_WIN": 0.5, "DRAW": 0.3, "AWAY_WIN": 0.1},
            predicted_match_result="HOME_WIN",
            confidence=0.5,
        )


# ---------------------------------------------------------------------------
# predict: CLI helpers
# ---------------------------------------------------------------------------

def test_load_feature_rows_accepts_list_object_and_single_row(tmp_path):
    data = {
        "matches": [context_row(api_id=1), context_row(api_id=2)],
    }
    p = tmp_path / "rows.json"
    p.write_text(json.dumps(data))
    assert len(load_feature_rows(p)) == 2

    p2 = tmp_path / "single.json"
    p2.write_text(json.dumps(context_row(api_id=9)))
    rows = load_feature_rows(p2)
    assert rows[0]["api_id"] == 9


def test_load_feature_rows_rejects_bad_rows(tmp_path):
    from pydantic import ValidationError

    bad = context_row(api_id=1)
    bad["home_team_home_win_rate"] = 1.7  # out of range
    p = tmp_path / "bad.json"
    p.write_text(json.dumps([bad]))
    with pytest.raises(ValidationError):
        load_feature_rows(p)


def test_envelope_shape():
    rows = [context_row(api_id=1)]
    responses = _score_via_pipeline(rows)
    env = _envelope("features", None, "m-test", rows, responses)
    assert env["count"] == 1
    assert env["model_id"] == "m-test"
    assert env["predictions"][0]["match_date"] == "2021-01-05"
    assert set(env["predictions"][0]["prediction"]) >= {"probabilities", "predicted_match_result", "confidence"}

# ---------------------------------------------------------------------------
# load_matches: which seasons each call site is allowed to see
# ---------------------------------------------------------------------------

class _RecordingCursor:
    def __init__(self, calls):
        self._calls = calls

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, sql, params=None):
        self._calls.append((sql, params))

    def fetchall(self):
        return []


class _RecordingConn:
    def __init__(self):
        self.calls = []

    def cursor(self, cursor_factory=None):
        return _RecordingCursor(self.calls)


class _SeasonAwareConn:
    """Fake conn that answers the fixture-scoring query sequence."""

    def __init__(self):
        self.calls = []
        self.seasons_requested = []

    def cursor(self, cursor_factory=None):
        return _FixtureCursor(self)

    def record(self, sql, params):
        self.calls.append((sql, params))


class _FixtureCursor:
    def __init__(self, conn):
        self._conn = conn

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def execute(self, sql, params=None):
        self._conn.record(sql, params)

    def fetchone(self):
        for sql, _params in reversed(self._conn.calls):
            if "league_seasons ls" in sql and "EXISTS" in sql:
                self._conn.seasons_requested.append("2026-2027")
                return ["2026-2027"]
            if "team_aliases" in sql:
                return [7]
        return None

    def fetchall(self):
        return []


def test_load_matches_restricts_to_complete_seasons_by_default():
    from ml.features.build_features import load_matches

    conn = _RecordingConn()
    load_matches(conn, "premier")
    sql, params = conn.calls[0]
    assert "season_state" in sql
    assert params == ("premier", True)
    # The flag is negated inside the predicate. Asserting only the recorded
    # param missed the case where the SQL was written as
    # `(%s OR season_state = 'complete')`: with True that is plain TRUE, so
    # the in-progress season was never actually filtered out.
    assert _season_filter_is_correct(sql), "season filter predicate is inverted"


def _season_filter_is_correct(sql: str) -> bool:
    """True when complete_seasons_only=True actually excludes non-complete rows."""
    import re

    m = re.search(
        r"AND\s*\(\s*(NOT\s+)?%s\s+OR\s+ls\.season_state\s*=\s*'complete'\s*\)",
        sql,
    )
    if m is None:
        return False
    # The placeholder must be negated so that True reduces to the season_state
    # test, and False short-circuits to "all seasons".
    return m.group(1) is not None


def test_load_matches_can_include_in_progress_seasons_for_fixtures():
    from ml.features.build_features import load_matches

    conn = _RecordingConn()
    load_matches(conn, "premier", complete_seasons_only=False)
    _sql, params = conn.calls[0]
    assert params == ("premier", False)


def test_fixture_scoring_seeds_from_the_in_progress_season():
    # A part-played season is excluded from the training dataset but must still
    # supply fixture history, or Mode B would score every fixture with no form.
    from ml.features.build_features import build_fixture_rows

    conn = _SeasonAwareConn()
    build_fixture_rows(
        conn,
        [{"home_team": "Arsenal", "away_team": "Chelsea", "match_date": "2026-11-01"}],
        league="premier",
    )
    load_calls = [params for _sql, params in conn.calls if params and params[0] == "premier"]
    assert ("premier", False) in load_calls
    assert ("premier", True) not in load_calls
    assert conn.seasons_requested == ["2026-2027"]
