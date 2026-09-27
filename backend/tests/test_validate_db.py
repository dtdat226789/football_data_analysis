"""Unit tests for validate_db helpers (no DB, no network).

Only the pure helpers are covered here; the full validation run needs a live
PostgreSQL database, but the count expectations are computed from raw JSON
with the same score classification the ETL uses.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from scripts.validate_db import GAME_INDEX_QUERY, game_index_problems, playable_count  # noqa: E402
from scripts.db_common import score_status  # noqa: E402


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


# ── playable_count ──────────────────────────────────────────────────────────
def test_playable_count_counts_only_playable_matches():
    raw = {
        "matches": [
            {"score": "1:0"},
            {"score": "2:1AfP"},
            {"score": "1:3AET"},
            {"score": "CAN."},
            {"score": "AWA."},
            {"score": "2:0CAN."},
            {"score": "garbage"},
            {"score": None},
            {"team": "not-a-match-row"},
        ]
    }
    assert playable_count(raw) == 3


def test_playable_count_empty():
    assert playable_count({"matches": []}) == 0
    assert playable_count({}) == 0


def test_playable_count_agrees_with_score_status():
    raw = {"matches": [{"score": s} for s in ("1:0", "CAN.", "abc", None)]}
    assert playable_count(raw) == sum(
        1
        for m in raw["matches"]
        if score_status(m["score"]) == "playable"
    )

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
