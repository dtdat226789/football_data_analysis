"""Deterministic, database-free validation of a built feature dataset.

All checks operate on plain JSON (list of dicts), so the report can be produced
from a freshly-built dataset without needing a DB connection in tests:

  - target & column integrity: schema fixed, api_id unique
  - no nulls in feature-group A/B/C; group-D (rest) allowlisted
  - value ranges (win rates in [0,1], averages >= 0, positions >= 1, ...)
  - chronological: rows within a season are non-decreasing by (date, game_index)
  - train/holdout split by season with no row loss

This module only *checks*; the leakage safety itself is guaranteed by
build_features.py (strictly-prior grouping). ml/sql_check.py runs an
independent SQL-level consistency check against PostgreSQL.
"""
from __future__ import annotations

from datetime import date

from ml.contract import CONTEXT_COLUMNS, FEATURE_COLUMNS
from ml.features.build_features import MATERIALIZED_COLUMNS, MATCH_RESULTS, OUTCOME_COLUMNS

# Rest-days are the only features legitimately absent before a season opener.
NULLABLE = {"home_rest_days", "away_rest_days", "rest_days_difference"}

# Columns that must hold a concrete value: the fixed context block (ids, team
# names, date) plus every feature and score. The context block is included so a
# missing team_seasons row surfaces as an error instead of a null team name
# sneaking into a dataset that reports ok.
REQUIRED_COLUMNS = CONTEXT_COLUMNS + MATERIALIZED_COLUMNS

DEFAULT_TRAIN_SEASONS = ["2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025"]
DEFAULT_HOLDOUT_SEASONS = ["2025-2026"]


def expected_result(home_score: int, away_score: int) -> str:
    """The only match_result label consistent with a given scoreline."""
    if home_score > away_score:
        return "HOME_WIN"
    if home_score == away_score:
        return "DRAW"
    return "AWAY_WIN"


def check_dataset(rows: list[dict]) -> dict:
    """Run every validation check and return a severity-tagged report."""
    errors: list[str] = []
    warnings: list[str] = []
    stats: dict = {}

    # --- integrity: fixed schema, unique api_id ---
    expected = CONTEXT_COLUMNS + FEATURE_COLUMNS + OUTCOME_COLUMNS
    got = list(rows[0].keys()) if rows else []
    expected_set, got_set = set(expected), set(got)
    if rows:
        missing = expected_set - got_set
        extra = got_set - expected_set
        if missing:
            errors.append(f"missing columns: {sorted(missing)}")
        if extra:
            errors.append(f"unexpected columns: {sorted(extra)}")
        if len(got) != len(expected):
            errors.append(f"column order/count mismatch ({len(got)} != {len(expected)})")

    api_ids = [r["api_id"] for r in rows]
    stats["total_rows"] = len(rows)
    stats["unique_api_ids"] = len(set(api_ids))
    if len(api_ids) != len(set(api_ids)):
        errors.append("duplicate api_id rows present")

    # --- NULL policy ---
    for col in REQUIRED_COLUMNS:
        n = sum(1 for r in rows if r[col] is None)
        if col in NULLABLE:
            if n:
                warnings.append(f"column {col}: {n} NULL(s) (expected around season openers)")
            else:
                stats[f"nulls_{col}"] = 0
        else:
            if n:
                errors.append(f"column {col}: {n} NULL(s) are not allowed")
            else:
                stats[f"nulls_{col}"] = 0

    # --- value ranges ---
    if rows:
        win_rates = [r["home_team_home_win_rate"] for r in rows] + [
            r["away_team_away_win_rate"] for r in rows
        ]
        if not all(0.0 <= v <= 1.0 for v in win_rates):
            errors.append("win rates outside [0, 1]")
        avg_cols = [
            "home_team_home_goals_avg",
            "home_team_home_conceded_avg",
            "away_team_away_goals_avg",
            "away_team_away_conceded_avg",
        ]
        if not all(all(r[c] >= 0.0 for r in rows) for c in avg_cols):
            errors.append("goals averages negative")
        if not all(r["home_position_before_match"] >= 1 for r in rows):
            errors.append("home position < 1")
        if not all(r["away_position_before_match"] >= 1 for r in rows):
            errors.append("away position < 1")
        if not all(r["home_score"] >= 0 and r["away_score"] >= 0 for r in rows):
            errors.append("negative score present")
        if not all(r["match_result"] in MATCH_RESULTS for r in rows):
            errors.append("invalid match_result label")
        else:
            mismatched = [
                r["api_id"] for r in rows
                if r["match_result"] != expected_result(r["home_score"], r["away_score"])
            ]
            if mismatched:
                errors.append(
                    f"match_result inconsistent with the score for {len(mismatched)} row(s) "
                    f"(first: {mismatched[:5]})"
                )
        if not all(r["points_difference"] == r["home_points_before_match"] - r["away_points_before_match"] for r in rows):
            errors.append("points_difference inconsistent")
        if not all(r["position_difference"] == r["home_position_before_match"] - r["away_position_before_match"] for r in rows):
            errors.append("position_difference inconsistent")

    # --- chronological order within each season ---
    by_season: dict[str, list[dict]] = {}
    for r in rows:
        by_season.setdefault(r["season"], []).append(r)
    stats["seasons"] = sorted(by_season, key=season_key)
    bad = []
    for season, rs in by_season.items():
        prev = None
        for r in rs:
            if prev is not None and (r["match_date"], r["game_index"]) < prev:
                bad.append(f"{season} row {r['api_id']} out of order")
            prev = (r["match_date"], r["game_index"])
    if bad:
        errors.append("chronological ordering violated: " + "; ".join(bad[:5]))

    if rows:
        by_res = {}
        for r in rows:
            by_res[r["match_result"]] = by_res.get(r["match_result"], 0) + 1
        stats["target_distribution"] = dict(sorted(by_res.items()))

    # --- train / holdout split ---
    train_names = set(DEFAULT_TRAIN_SEASONS) & set(by_season)
    holdout_names = set(DEFAULT_HOLDOUT_SEASONS) & set(by_season)
    n_train = sum(len(rs) for s, rs in by_season.items() if s in train_names)
    n_holdout = sum(len(rs) for s, rs in by_season.items() if s in holdout_names)
    stats["train_seasons"] = sorted(train_names, key=season_key)
    stats["holdout_seasons"] = sorted(holdout_names, key=season_key)
    stats["train_rows"] = n_train
    stats["holdout_rows"] = n_holdout
    overlap = train_names & holdout_names
    if overlap:
        errors.append(f"season assigned to both train and holdout: {sorted(overlap)}")
    covered = n_train + n_holdout
    if covered != len(rows):
        warnings.append(
            f"rows outside train/holdout seasons ({len(rows) - covered}); expected for e.g. 2026-2027"
        )

    return {"ok": not errors, "errors": errors, "warnings": warnings, "stats": stats}


def season_key(name: str) -> tuple[int | None, int | None]:
    from ml import db

    return db.parse_season_years(name)