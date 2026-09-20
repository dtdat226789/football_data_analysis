"""Feature group B: venue-specific performance (prior home / prior away games).

For the home team only its prior *home* games are used (is_home=True), and for
the away team only its prior *away* games (is_home=False). Only matches that
strictly precede the target match are ever in the record list.

An empty venue window (e.g. the home team's first home game of the season)
yields 0.0 for the rate and averages; documented, leakage-safe default.
"""
from __future__ import annotations

from .records import TeamRecord


def venue_records(records: list[TeamRecord], *, is_home: bool) -> list[TeamRecord]:
    """Filter records to one venue (home or away)."""
    return [r for r in records if r.is_home is is_home]


def win_rate(records: list[TeamRecord], *, is_home: bool) -> float:
    """Win percentage over prior games at the given venue (0.0 if none)."""
    vr = venue_records(records, is_home=is_home)
    if not vr:
        return 0.0
    return round(sum(r.is_win for r in vr) / len(vr), 6)


def goals_avg(records: list[TeamRecord], *, is_home: bool) -> float:
    """Average goals scored per prior game at the given venue (0.0 if none)."""
    vr = venue_records(records, is_home=is_home)
    if not vr:
        return 0.0
    return round(sum(r.goals_for for r in vr) / len(vr), 6)


def conceded_avg(records: list[TeamRecord], *, is_home: bool) -> float:
    """Average goals conceded per prior game at the given venue (0.0 if none)."""
    vr = venue_records(records, is_home=is_home)
    if not vr:
        return 0.0
    return round(sum(r.goals_against for r in vr) / len(vr), 6)