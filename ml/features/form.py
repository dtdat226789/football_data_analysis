"""Feature group A: recent form (last N completed matches, any venue).

The input is a team's list of prior TeamRecords that the orchestrator appends
in strictly chronological order, so the "last N" slice is the N most recent
matches completed before the target match.

An empty window (a team's first match of the collected period) yields 0 for
every aggregate; this is a documented, leakage-safe default rather than NULL.
"""
from __future__ import annotations

from .records import TeamRecord

DEFAULT_WINDOW = 5


def last_records(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> list[TeamRecord]:
    """The n most recent records (empty when the team has no prior matches)."""
    if not records:
        return []
    return records[-n:]


def points_last(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> int:
    """Points earned across the last n matches (3 for a win, 1 for a draw)."""
    return sum(r.points for r in last_records(records, n))


def wins_last(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> int:
    """Number of wins across the last n matches."""
    return sum(r.is_win for r in last_records(records, n))


def goals_scored_last(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> int:
    """Goals scored across the last n matches."""
    return sum(r.goals_for for r in last_records(records, n))


def goals_conceded_last(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> int:
    """Goals conceded across the last n matches."""
    return sum(r.goals_against for r in last_records(records, n))


def all_family_last(records: list[TeamRecord], n: int = DEFAULT_WINDOW) -> dict:
    """Return the whole per-team form block (helper used by the orchestrator)."""
    return {
        "points_last": points_last(records, n),
        "wins_last": wins_last(records, n),
        "goals_scored_last": goals_scored_last(records, n),
        "goals_conceded_last": goals_conceded_last(records, n),
    }
