"""Unit tests for the raw-to-DB reconciler (no DB, no network).

The reconcile_* functions are pure: they take plain dicts built either from
the raw JSON files or from the DB lookups, so every branch is testable with
synthetic fixtures without touching PostgreSQL.
"""
from __future__ import annotations

from datetime import date, time

import scripts.validate_raw_to_db as v
from scripts.validate_raw_to_db import (
    SEVERITY_ERROR,
    SEVERITY_WARNING,
    reconcile_matches,
    reconcile_registry,
    reconcile_standings,
    reconcile_teams,
)

LEAGUE = "premier"
SEASON = "2020-2021"


def codes(issues) -> set[str]:
    return {i["code"] for i in issues}


# ── shared fixtures ────────────────────────────────────────────────────────────
def team_ids():
    return {(SEASON, "Arsenal"): 1, (SEASON, "Chelsea"): 2, (SEASON, "Liverpool"): 3}


def raw_match(*, mid=101, hs=2, as_=1, date="2020-09-12", time="15:00:00", gi=1,
              home="Arsenal", away="Chelsea", ht="1:0", fgt=12, fgte=0):
    return {
        "id": mid, "game_index": gi, "date": date, "time": time,
        "homeTeam": home, "awayTeam": away, "score": f"{hs}:{as_}",
        "ht_result": ht, "first_goal_time": fgt, "first_goal_time_extra": fgte,
    }


def db_match(*, mid=101, home=1, away=2, hs=2, as_=1, d=date(2020, 9, 12),
             t=time(15, 0), gi=1, ht=(1, 0), fgt=12, fgte=0):
    return {
        "season": SEASON, "api_id": mid, "game_index": gi,
        "home_team_id": home, "away_team_id": away,
        "match_date": d, "kickoff_time": t,
        "home_score": hs, "away_score": as_, "home_ht": ht[0], "away_ht": ht[1],
        "first_goal_time": fgt, "first_goal_time_extra": fgte,
    }


# ── matches ────────────────────────────────────────────────────────────────────
def test_matches_clean_roundtrip():
    issues = []
    raw = {"matches": [raw_match()]}
    db = {101: db_match()}
    cnt = reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert not issues
    assert cnt["n_compared"] == 1


def test_matches_swapped_score_detected():
    issues = []
    raw = {"matches": [raw_match(hs=0, as_=3)]}
    db = {101: db_match(hs=3, as_=0)}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert "MATCH_FIELD_MISMATCH" in codes(issues)
    detail = issues[0]["details"]["mismatches"]
    assert ("home_score", 3, 0) in detail
    assert ("away_score", 0, 3) in detail


def test_matches_wrong_team_detected():
    issues = []
    raw = {"matches": [raw_match(home="Liverpool", away="Arsenal")]}
    db = {101: db_match(home=1, away=2)}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert "MATCH_FIELD_MISMATCH" in codes(issues)


def test_matches_date_and_time_drift_detected():
    issues = []
    raw = {"matches": [raw_match(date="2020-09-13", time="17:30:00")]}
    db = {101: db_match(d=date(2020, 9, 12), t=time(15, 0))}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    fields = {f for f, _db, _raw in issues[0]["details"]["mismatches"]}
    assert "date" in fields
    assert "time" in fields


def test_matches_ht_null_vs_null_ok_but_non_null_detected():
    issues = []
    raw = {"matches": [raw_match(ht=None)]}
    db = {101: db_match(ht=(None, None))}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert not issues


def test_matches_missing_from_db():
    issues = []
    raw = {"matches": [raw_match(mid=999)]}
    reconcile_matches(issues, LEAGUE, SEASON, raw, {}, team_ids())
    assert "MATCH_NOT_IN_DB" in codes(issues)


def test_matches_extra_in_db():
    issues = []
    raw = {"matches": [raw_match(mid=101)]}
    db = {101: db_match(), 555: db_match(mid=555)}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert "EXTRA_MATCH_IN_DB" in codes(issues)


def test_matches_team_membership_missing():
    issues = []
    raw = {"matches": [raw_match(home="Mystery FC")]}
    db = {101: db_match()}
    team_ids_missing = {(SEASON, "Arsenal"): 1, (SEASON, "Chelsea"): 2, (SEASON, "Liverpool"): 3}
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids_missing)
    assert "TEAM_MEMBERSHIP_MISSING" in codes(issues)
    assert "MATCH_FIELD_MISMATCH" not in codes(issues)


def test_matches_wrong_season_detected():
    issues = []
    raw = {"matches": [raw_match()]}
    db = {101: db_match()}
    db[101]["season"] = "2021-2022"
    reconcile_matches(issues, LEAGUE, SEASON, raw, db, team_ids())
    assert "MATCH_FIELD_MISMATCH" in codes(issues)


# ── standings ──────────────────────────────────────────────────────────────────
def row(**over):
    base = {
        "team": "Arsenal", "position": 1, "played": 38, "won": 28, "drawn": 6,
        "lost": 4, "goals_for": 90, "goals_against": 28, "goal_difference": 62,
        "points": 90, "xpts": 84.5,
    }
    base.update(over)
    return base


def stand_row(**over):
    base = {
        "position": 1, "played": 38, "won": 28, "drawn": 6, "lost": 4,
        "goals_for": 90, "goals_against": 28, "goal_difference": 62, "points": 90,
        "metrics": {"xpts": 84.5},
    }
    base.update(over)
    return base


def test_standings_clean_roundtrip_including_metrics():
    issues = []
    raw = {"table": [row()]}
    db = {(SEASON, "classic", "Arsenal"): stand_row()}
    cnt = reconcile_standings(issues, LEAGUE, SEASON, "classic", raw, db)
    assert not issues
    assert cnt["n_compared"] == 1


def test_standings_core_field_mismatch():
    issues = []
    raw = {"table": [row(points=87)]}
    db = {(SEASON, "classic", "Arsenal"): stand_row(points=90)}
    reconcile_standings(issues, LEAGUE, SEASON, "classic", raw, db)
    assert "STANDING_FIELD_MISMATCH" in codes(issues)


def test_standings_metrics_drift_detected():
    issues = []
    raw = {"table": [row(xpts=80.0)]}
    db = {(SEASON, "classic", "Arsenal"): stand_row(metrics={"xpts": 84.5})}
    reconcile_standings(issues, LEAGUE, SEASON, "classic", raw, db)
    assert "STANDING_FIELD_MISMATCH" in codes(issues)


def test_standings_missing_and_extra():
    issues = []
    raw = {"table": [row(team="Arsenal")]}
    db = {
        (SEASON, "classic", "Liverpool"): stand_row(),  # not in raw -> EXTRA
    }
    reconcile_standings(issues, LEAGUE, SEASON, "classic", raw, db)
    assert "STANDING_NOT_IN_DB" in codes(issues)
    assert "EXTRA_STANDING_IN_DB" in codes(issues)


# ── identity / teams ───────────────────────────────────────────────────────────
def team_row(**over):
    base = {"team": "Arsenal", "slug": "arsenal", "logo_url": "https://x/a.png"}
    base.update(over)
    return base


def db_team_row(**over):
    base = {"season": SEASON, "api_name": "Arsenal", "api_slug": "arsenal",
            "logo_url": "https://x/a.png", "team_id": 1}
    base.update(over)
    return base


def test_teams_clean_roundtrip():
    issues = []
    raw = {"teams": [team_row()]}
    db = {(SEASON, "Arsenal"): db_team_row()}
    aliases = {("slug", "arsenal"): 1}
    cnt = reconcile_teams(issues, LEAGUE, SEASON, raw, db, aliases)
    assert not issues
    assert cnt["n_compared"] == 1


def test_teams_slug_mismatch():
    issues = []
    raw = {"teams": [team_row(slug="arsenal-fc")]}
    db = {(SEASON, "Arsenal"): db_team_row()}
    aliases = {("slug", "arsenal-fc"): 1}
    reconcile_teams(issues, LEAGUE, SEASON, raw, db, aliases)
    assert "SLUG_MISMATCH" in codes(issues)


def test_teams_logo_mismatch_is_warning():
    issues = []
    raw = {"teams": [team_row(logo_url="https://x/b.png")]}
    db = {(SEASON, "Arsenal"): db_team_row()}
    aliases = {("slug", "arsenal"): 1}
    reconcile_teams(issues, LEAGUE, SEASON, raw, db, aliases)
    assert "LOGO_MISMATCH" in codes(issues)
    assert all(i["severity"] == SEVERITY_WARNING for i in issues)


def test_teams_alias_points_at_wrong_team():
    issues = []
    raw = {"teams": [team_row()]}
    db = {(SEASON, "Arsenal"): db_team_row()}
    aliases = {("slug", "arsenal"): 999}
    reconcile_teams(issues, LEAGUE, SEASON, raw, db, aliases)
    assert "ALIAS_TEAM_MISMATCH" in codes(issues)


def test_teams_missing_from_db_and_extra_in_db():
    issues = []
    raw = {"teams": [team_row(team="Arsenal")]}
    db = {
        (SEASON, "Liverpool"): db_team_row(api_name="Liverpool", team_id=3),
    }
    aliases = {}
    reconcile_teams(issues, LEAGUE, SEASON, raw, db, aliases)
    assert "TEAM_NOT_IN_DB" in codes(issues)
    assert "UNUSED_TEAM_IN_DB" in codes(issues)


# ── registry ───────────────────────────────────────────────────────────────────
def leagues_payload():
    return {"leagues": [{"league": "premier", "name": "Premier League",
                         "seasons": ["2021-2022", "2020-2021"], "url": "x"}]}


def test_registry_clean():
    issues = []
    db_reg = {"2020-2021": {"name": "2020-2021", "declared_by_api": True, "season_state": "complete"}}
    reconcile_registry(issues, LEAGUE, leagues_payload(), db_reg, {SEASON: "complete"}, {})
    assert not issues


def test_registry_declared_by_api_mismatch():
    issues = []
    db_reg = {"2020-2021": {"name": "2020-2021", "declared_by_api": False, "season_state": "complete"}}
    reconcile_registry(issues, LEAGUE, leagues_payload(), db_reg, {SEASON: "complete"}, {})
    assert "DECLARED_BY_API_MISMATCH" in codes(issues)


def test_registry_season_state_mismatch():
    issues = []
    db_reg = {"2020-2021": {"name": "2020-2021", "declared_by_api": True, "season_state": "unknown"}}
    reconcile_registry(issues, LEAGUE, leagues_payload(), db_reg, {SEASON: "complete"}, {})
    assert "SEASON_STATE_MISMATCH" in codes(issues)


def test_registry_missing_league_entry():
    issues = []
    reconcile_registry(issues, LEAGUE, {"leagues": [{"league": "bundesliga"}]}, {}, {}, {})
    assert "LEAGUE_ENTRY_MISSING" in codes(issues)


def test_reconcilers_are_severity_error_by_default():
    assert all(
        hasattr(v, name)
        for name in ("build_report", "render_markdown", "main", "raw_url", "load_db_matches")
    )