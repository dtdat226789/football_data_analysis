"""Feature group C: pre-match standings context.

The database's standings table holds the *final end-of-season* table fetched
from the API, so it can never be used as a pre-match feature. Instead the
running league table is recomputed here from matches strictly prior to each
match:

    table[team_id] = StandingsRow(played, points, goal_difference, goals_for)

Position is ranked over the whole season roster (all teams that appear in the
league season) using the standard sort key points DESC, goal_difference DESC,
goals_for DESC. Equal rows share a rank (position = 1 + number of teams
strictly better), so positions are not required to be unique — mirroring how a
real table looks before every team has played every other.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StandingsRow:
    played: int = 0
    points: int = 0
    goal_difference: int = 0
    goals_for: int = 0


def strictly_better(a: StandingsRow, b: StandingsRow) -> bool:
    """True when a ranks strictly above b (points, then GD, then GF)."""
    if a.points != b.points:
        return a.points > b.points
    if a.goal_difference != b.goal_difference:
        return a.goal_difference > b.goal_difference
    return a.goals_for > b.goals_for


def position(standings: dict[int, StandingsRow], roster: set[int], team_id: int) -> int:
    """League position of team_id before the next match (1-based)."""
    mine = standings[team_id]
    return 1 + sum(1 for other in roster if other != team_id and strictly_better(standings[other], mine))


def points_of(standings: dict[int, StandingsRow], team_id: int) -> int:
    return standings[team_id].points