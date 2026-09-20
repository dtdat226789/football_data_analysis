"""Unit tests for the database profiler (no database, no network).

Covers the pure helpers (percentages, outcomes, aggregation, first-goal
timing, scorelines, anomaly detection) and the report renderers. Query-layer
functions are thin wrappers around read-only SQL exercised against the live
database by running the profiler directly.
"""
from __future__ import annotations

import json

import pytest

import scripts.profile_database as p


def make_cfg(**overrides) -> dict:
    cfg = {
        "league": "premier",
        "out_dir": "/tmp/profiler_out",
        "score_threshold": 8,
        "avg_goals_deviation": 0.35,
        "goalless_deviation_pp": 1.5,
        "outcome_deviation_pp": 4.0,
        "expected_matches_per_season": 380,
        "expected_teams_per_season": 20,
        "expected_standings_rows": 20,
    }
    cfg.update(overrides)
    return cfg


def base_profile(cfg: dict) -> dict:
    """A minimal, internally consistent profile that should pass clean."""
    rows = [(1, 0, 170), (1, 1, 100), (0, 1, 90), (0, 0, 20)]
    stats = p.aggregate_match_stats({"overall": rows})["overall"]
    season_stats = {"season": "2020-2021", **stats}
    return {
        "report_name": "database_profile",
        "script": {"name": p.SCRIPT_NAME, "version": p.VERSION},
        "generated_at": "2026-09-17T00:00:00+00:00",
        "config": cfg,
        "meta": {"database": {"database_name": "football_charts", "server_version": "PostgreSQL"}},
        "observed": {
            "tables": {
                "leagues": 93, "seasons": 1, "league_seasons": 1,
                "teams": 20, "team_aliases": 40, "team_seasons": 20,
                "matches": 380, "standings": 20,
            },
            "leagues": [
                {"api_key": "premier", "name": "Premier League", "country": "England",
                 "n_registered_seasons": 1, "n_matches": 380}
            ],
            "league_seasons": {
                "n_registered": 1,
                "n_with_data": 1,
                "seasons_without_data": [],
                "seasons": [
                    {
                        "season": "2020-2021",
                        "declared_by_api": False,
                        "season_state": "complete",
                        "n_matches": 380,
                        "n_teams": 20,
                        "min_date": "2020-09-12",
                        "max_date": "2021-05-23",
                    }
                ],
            },
            "duplicates": [
                {"check": "matches.api_id (natural PK)", "rows": 380, "distinct": 380, "duplicates": 0},
                {"check": "matches same fixture on same date", "rows": 380, "distinct": 380, "duplicates": 0},
            ],
            "null_counts": {
                "total": 380,
                "fields": {
                    "match_date": {"n_null": 0, "n_not_null": 380, "null_pct": 0.0},
                    "home_score": {"n_null": 0, "n_not_null": 380, "null_pct": 0.0},
                    "first_goal_time": {"n_null": 0, "n_not_null": 380, "null_pct": 0.0},
                },
            },
            "first_goal_consistency": {
                "total": 380,
                "fgt_inconsistent": 0,
                "fgte_inconsistent": 0,
                "n_with_fgt": 380,
            },
            "value_ranges": {
                "min_home": 0, "max_home": 5, "min_away": 0, "max_away": 5,
                "min_fgt": 1, "max_fgt": 90,
                "min_ht_home": 0, "max_ht_home": 3, "min_ht_away": 0, "max_ht_away": 3,
            },
        },
        "calculated": {
            "overall": stats,
            "per_season": [season_stats],
            "first_goal": {
                "n_with_fgt": 360,
                "summary": p.summarize_first_goal_times([10, 20, 30, 40]),
                "buckets": p.bucket_first_goal_times([10, 20, 30, 40]),
                "per_season": {},
            },
            "standings": {
                "n_pairs": 1,
                "expected_pairs": 1,
                "n_rows": 20,
                "coverage_complete": True,
                "pairs": [
                    {
                        "season": "2020-2021",
                        "view": "classic",
                        "n_rows": 20,
                        "min_pos": 1,
                        "max_pos": 20,
                        "distinct_teams": 20,
                    }
                ],
            },
            "scorelines": {"most_common": [{"scoreline": "1-0", "count": 170}]},
            "extreme_scorelines": [],
            "weekday_distribution": [{"label": "Sat", "n": 250, "pct": 65.8}],
        },
        "warnings": [],
    }


# ── pure helpers ─────────────────────────────────────────────────────────────
def test_round_pct():
    assert p.round_pct(1, 4) == 25.0
    assert p.round_pct(1, 3) == 33.3
    assert p.round_pct(0, 0) is None
    assert p.round_pct(1, 0) is None
    assert p.round_pct(2, 3, ndigits=0) == 67.0


def test_classify_outcome():
    assert p.classify_outcome(2, 1) == "home"
    assert p.classify_outcome(1, 1) == "draw"
    assert p.classify_outcome(0, 2) == "away"


def test_percentile():
    s = sorted([10, 20, 30, 40])
    assert p.percentile(s, 0.5) == 25
    assert p.percentile([7], 0.5) == 7
    assert p.percentile([], 0.5) is None


def test_summarize_first_goal_times_empty():
    assert p.summarize_first_goal_times([]) is None


def test_summarize_first_goal_times():
    s = p.summarize_first_goal_times([10, 20, 30, 40])
    assert s["min"] == 10
    assert s["max"] == 40
    assert s["mean"] == 25.0
    assert s["n"] == 4


def test_bucket_first_goal_times():
    b = p.bucket_first_goal_times([1, 15, 16, 45, 46, 90, 91, 120])
    assert b["1-15"] == 2
    assert b["16-30"] == 1
    assert b["31-45"] == 1
    assert b["46-60"] == 1
    assert b["76-90"] == 1
    assert b["91-120"] == 2


def test_aggregate_match_stats():
    rows = [(1, 0, 10), (1, 1, 5), (0, 2, 5), (0, 0, 2)]
    s = p.aggregate_match_stats({"group": rows})["group"]
    assert s["n_matches"] == 22
    assert s["home_wins"] == 10
    assert s["draws"] == 7  # 5 x 1-1 + 2 x 0-0
    assert s["away_wins"] == 5
    assert s["home_win_pct"] == round(100 * 10 / 22, 1)
    assert s["home_goals"] == 10 + 5 + 0 + 0
    assert s["away_goals"] == 0 + 5 + 10 + 0
    assert s["total_goals"] == s["home_goals"] + s["away_goals"]
    assert s["goalless"] == 2
    assert s["home_goal_share"] == round(100 * s["home_goals"] / s["total_goals"], 1)


def test_top_and_extreme_scorelines():
    rows = [(0, 8, 1), (1, 0, 5), (9, 0, 2), (1, 1, 3)]
    assert p.top_scorelines(rows, limit=2)[0]["scoreline"] == "1-0"
    extreme = p.extreme_scorelines(rows, 8)
    assert [e["scoreline"] for e in extreme] == ["9-0", "0-8"]
    assert p.extreme_scorelines(rows, 99) == []


def test_season_sort_key():
    names = ["2025-2026", "2020-2021", "2022-2023"]
    assert sorted(names, key=p.season_sort_key) == ["2020-2021", "2022-2023", "2025-2026"]


# ── anomaly detection ────────────────────────────────────────────────────────
def test_clean_profile_has_no_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    assert p.detect_anomalies(profile, cfg) == []


def test_registry_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    profile["observed"]["league_seasons"]["seasons"].append(
        {"season": "2026-2027", "declared_by_api": True, "season_state": "unknown",
         "n_matches": 0, "n_teams": 0, "min_date": None, "max_date": None}
    )
    profile["observed"]["league_seasons"]["n_registered"] = 2
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "SEASON_REGISTERED_NO_DATA" in codes
    assert "MATCH_COUNT_UNEXPECTED" in codes
    assert "TEAM_COUNT_UNEXPECTED" not in codes  # 0 teams is the no-data case


def test_team_count_and_state_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    s = profile["observed"]["league_seasons"]["seasons"][0]
    s["n_teams"] = 19
    s["season_state"] = "in_progress"
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "TEAM_COUNT_UNEXPECTED" in codes
    assert "SEASON_STATE_NOT_COMPLETE" in codes


def test_numeric_outlier_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    outlier = p.aggregate_match_stats({"x": [(5, 0, 380)]})["x"]
    profile["calculated"]["per_season"].append({"season": "2023-2024", **outlier})
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "SEASON_AVG_GOALS_OUTLIER" in codes
    assert "GOALLESS_SHARE_OUTLIER" in codes
    assert "OUTCOME_SHARE_OUTLIER" in codes


def test_duplicate_null_and_fgt_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    profile["observed"]["duplicates"][1]["duplicates"] = 2
    profile["observed"]["null_counts"]["fields"]["match_date"]["n_null"] = 3
    profile["observed"]["first_goal_consistency"]["fgt_inconsistent"] = 1
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "DUPLICATE_ROWS" in codes
    assert "NULL_IN_REQUIRED_FIELD" in codes
    assert "FIRST_GOAL_NULL_INCONSISTENCY" in codes


def test_null_in_optional_field_is_not_warning():
    cfg = make_cfg()
    profile = base_profile(cfg)
    profile["observed"]["null_counts"]["fields"]["first_goal_time"]["n_null"] = 129
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "NULL_IN_REQUIRED_FIELD" not in codes


def test_high_scoring_and_standings_warnings():
    cfg = make_cfg()
    profile = base_profile(cfg)
    profile["calculated"]["extreme_scorelines"] = [
        {"scoreline": "9-0", "total_goals": 9, "count": 2}
    ]
    profile["calculated"]["standings"]["pairs"][0]["n_rows"] = 19
    codes = [w["code"] for w in p.detect_anomalies(profile, cfg)]
    assert "HIGH_SCORING_MATCHES" in codes
    assert "STANDINGS_INCOMPLETE" in codes


def test_thresholds_are_configurable():
    profile = base_profile(make_cfg())
    strictness = make_cfg(avg_goals_deviation=10.0, goalless_deviation_pp=10.0,
                          outcome_deviation_pp=10.0, score_threshold=99)
    assert p.detect_anomalies(profile, strictness) == []


# ── renderers ────────────────────────────────────────────────────────────────
def test_render_markdown_has_three_sections(capsys):
    cfg = make_cfg()
    profile = base_profile(cfg)
    profile["warnings"] = p.detect_anomalies(profile, cfg)
    md = p.render_markdown(profile)
    assert "## 1. Observed data" in md
    assert "## 2. Calculated statistics" in md
    assert "## 3. Warnings & anomalies" in md
    assert "None." in md  # clean report shows no warnings


def test_render_json_serializable():
    profile = base_profile(make_cfg())
    profile["warnings"] = p.detect_anomalies(profile, make_cfg())
    json.dumps(p.render_json(profile))


def test_args_roundtrip_defaults():
    args = p.parse_args([])
    cfg = p.args_to_config(args)
    assert cfg["league"] == p.LEAGUE
    assert cfg["score_threshold"] == 8
    assert cfg["expected_matches_per_season"] == p.EXPECTED_MATCHES_PER_SEASON


def test_args_allow_customisation():
    args = p.parse_args(["--league", "spain1", "--score-threshold", "9",
                         "--avg-goals-deviation", "0.5"])
    cfg = p.args_to_config(args)
    assert cfg["league"] == "spain1"
    assert cfg["score_threshold"] == 9
    assert cfg["avg_goals_deviation"] == 0.5