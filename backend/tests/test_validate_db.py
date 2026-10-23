"""Unit tests for validate_db helpers (no DB, no network).

Only the pure helpers are covered here; the full validation run needs a live
PostgreSQL database, but the count expectations are computed from raw JSON
with the same score classification the ETL uses.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from scripts.validate_db import (  # noqa: E402
    GAME_INDEX_QUERY,
    game_index_problems,
    loadable_count,
    roster_by_slug,
    roster_for_season,
    table_position_bound,
)
from scripts.db_common import score_status  # noqa: E402

ROSTER = {"Arsenal", "Chelsea", "Liverpool"}


class _StubCursor:
    """Records the query it is given and replays canned rows."""

    def __init__(self, rows):
        self._rows = rows
        self.executed: list[tuple[str, object]] = []

    def execute(self, sql, params=None):
        self.executed.append((sql, params))

    def fetchall(self):
        return self._rows


def _row(season, gmin, gmax, cnt, distinct):
    return {
        "season": season, "gmin": gmin, "gmax": gmax,
        "cnt": cnt, "distinct": distinct,
    }


# ── loadable_count ───────────────────────────────────────────────────────────
def raw_match(score, home="Arsenal", away="Chelsea"):
    return {"score": score, "homeTeam": home, "awayTeam": away}


def test_loadable_count_counts_only_playable_matches():
    raw = {
        "matches": [
            raw_match("1:0"),
            raw_match("2:1AfP"),
            raw_match("1:3AET"),
            raw_match("CAN."),
            raw_match("AWA."),
            raw_match("2:0CAN."),
            raw_match("garbage"),
            raw_match(None),
            {"team": "not-a-match-row"},
        ]
    }
    assert loadable_count(raw, ROSTER) == 3


def test_loadable_count_excludes_membership_missing_matches():
    raw = {
        "matches": [
            raw_match("1:0"),
            raw_match("2:1", home="B. Monchengladbach"),
            raw_match("2:1", away="B.93"),
        ]
    }
    assert loadable_count(raw, ROSTER) == 1


def test_loadable_count_empty():
    assert loadable_count({"matches": []}, ROSTER) == 0
    assert loadable_count({}, ROSTER) == 0


def test_loadable_count_agrees_with_score_status_and_roster():
    raw = {
        "matches": [
            raw_match("1:0"),
            raw_match("CAN."),
            raw_match("2:1", home="B. Monchengladbach"),
            raw_match(None),
        ]
    }
    assert loadable_count(raw, ROSTER) == sum(
        1
        for m in raw["matches"]
        if m.get("homeTeam") in ROSTER
        and m.get("awayTeam") in ROSTER
        and score_status(m.get("score")) == "playable"
    )

# ── roster_by_slug ───────────────────────────────────────────────────────────
def test_roster_by_slug_keeps_one_name_per_slug():
    # kuwait 2026-2027 lists the same club twice (Al-Fahaheel / Al Fahaheel)
    teams = {
        "teams": [
            {"team": "Al Qadisiya", "slug": "al-qadisiya"},
            {"team": "Al-Fahaheel", "slug": "al-fahaheel"},
            {"team": "Al Fahaheel", "slug": "al-fahaheel"},
        ]
    }
    merged = roster_by_slug(teams)
    assert merged == {
        "al-qadisiya": "Al Qadisiya",
        "al-fahaheel": "Al Fahaheel",  # last entry wins, as in etl_02
    }
    assert set(merged.values()) == {"Al Qadisiya", "Al Fahaheel"}


def test_roster_by_slug_empty_and_ignores_non_dicts():
    assert roster_by_slug({}) == {}
    assert roster_by_slug({"teams": [{"team": "Arsenal", "slug": "arsenal"}, 7]}) == {
        "arsenal": "Arsenal",
    }


# ── roster_for_season ───────────────────────────────────────────────────────
def test_roster_for_season_drops_phantom_rows_then_merges_by_slug():
    # brazil1 2025: 'MG-Bahia'/'Atletico' never play a match and are name
    # variants of participants, so etl_02 keeps only the 20 real teams
    teams = {
        "teams": [
            {"team": "Bahia", "slug": "bahia"},
            {"team": "MG-Bahia", "slug": "mg-bahia"},
            {"team": "Atletico", "slug": "atletico"},  # variant of Atletico-MG
            {"team": "Atletico-MG", "slug": "atletico-mg"},
            {"team": "Al-Fahaheel", "slug": "al-fahaheel"},
            {"team": "Al Fahaheel", "slug": "al-fahaheel"},  # dupe slug, kept
        ]
    }
    matches = [
        {"homeTeam": "Bahia", "awayTeam": "Atletico-MG"},
    ]
    merged = roster_for_season(teams, matches)
    assert merged == {
        "bahia": "Bahia",
        "atletico-mg": "Atletico-MG",
        "al-fahaheel": "Al Fahaheel",
    }


def test_roster_for_season_no_matches_keeps_everything():
    teams = {
        "teams": [
            {"team": "Bahia", "slug": "bahia"},
            {"team": "MG-Bahia", "slug": "mg-bahia"},
        ]
    }
    assert roster_for_season(teams, []) == {
        "bahia": "Bahia",
        "mg-bahia": "MG-Bahia",  # pre-season: no participants, nothing filtered
    }


# ── table_position_bound ─────────────────────────────────────────────────────
def test_table_position_bound_excludes_rows_outside_roster():
    table = {
        "table": [
            {"team": "Al Qadisiya", "position": 1},
            {"team": "Al-Fahaheel", "position": 2},  # losing duplicate spelling
            {"team": "Al Fahaheel", "position": 3},
        ]
    }
    roster = {"Al Qadisiya", "Al Fahaheel"}
    assert table_position_bound(table, roster) == 3  # hole at 2 tolerated below


def test_table_position_bound_empty_table():
    assert table_position_bound({"table": []}, {"Arsenal"}) == 0
    assert table_position_bound({}, {"Arsenal"}) == 0


# ── game_index_problems ─────────────────────────────────────────────────────
def test_game_index_check_actually_runs_its_query():
    # Regression: the check used to call fetchall() with no execute() before it,
    # so psycopg2 returned [] and the check reported PASS while testing nothing.
    cur = _StubCursor([_row("2024-2025", 1, 380, 380, 380)])
    problems = game_index_problems(cur, "premier", {"2024-2025"})
    assert len(cur.executed) == 1
    assert cur.executed[0][0] == GAME_INDEX_QUERY
    assert cur.executed[0][1] == ("premier",)
    assert problems == []


def test_game_index_clean_season_must_be_contiguous():
    assert game_index_problems(
        _StubCursor([_row("2024-2025", 1, 380, 380, 380)]), "premier", {"2024-2025"}
    ) == []
    # a gap: max is 380 but only 379 rows, so it is not 1..n
    assert game_index_problems(
        _StubCursor([_row("2024-2025", 1, 380, 379, 379)]), "premier", {"2024-2025"}
    ) == [("2024-2025", 1, 380, 379, 379)]
    # does not start at 1
    assert game_index_problems(
        _StubCursor([_row("2024-2025", 2, 381, 380, 380)]), "premier", {"2024-2025"}
    ) == [("2024-2025", 2, 381, 380, 380)]


def test_game_index_duplicate_is_always_a_problem():
    rows = [_row("2023-2024", 1, 380, 380, 379)]
    assert game_index_problems(_StubCursor(rows), "premier", {"2023-2024"})
    # gaps are legitimate when the season is not clean
    assert game_index_problems(_StubCursor(rows), "premier", set()) == [
        ("2023-2024", 1, 380, 380, 379)
    ]


def test_game_index_query_counts_distinct_game_index():
    assert "count(DISTINCT m.game_index)" in GAME_INDEX_QUERY
    assert "GROUP BY s.name" in GAME_INDEX_QUERY
