"""Score scheduled (upcoming) fixtures with the same leakage-safe features.

The dataset pipeline (build_features.process_season) scores *completed* matches
by replaying a season strictly in chronological order and never observing the
result being scored. A scheduled fixture must be scored the same way, with one
difference: its result never gets applied (it has not happened yet).

This module is DB-free. The DB-aware wrapper ``build_fixture_rows`` lives in
``build_features.py`` and only:

  1. resolves the fixture's team names to DB team ids (team_aliases),
  2. loads the current season's *completed* matches,
  3. calls ``seed_season`` to replay them, then ``score_fixtures``.

``seed_season`` replays completed matches with the exact grouping used by
``process_season`` (equal match_date + kickoff_time replay simultaneously), so
the state a fixture sees is byte-identical to what the training rows saw at
the same point in the season. The equivalence is verified in
``ml/tests/test_predict.py``.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, time

from .records import TeamRecord
from .standings import StandingsRow


@dataclass(frozen=True)
class Fixture:
    """A scheduled match that has not been played (no scores, no result)."""
    home_team_id: int
    away_team_id: int
    match_date: date
    kickoff_time: time | None = None


def _feature_block(m, home_records, away_records, table, roster) -> dict:
    """feature_block from the orchestrator, imported lazily to avoid a cycle."""
    from .build_features import feature_block

    return feature_block(m, home_records, away_records, table, roster)


def _apply_result(table, team_id, rec) -> None:
    from .build_features import apply_result

    apply_result(table, team_id, rec)


def seed_season(completed: list) -> tuple[dict[int, list[TeamRecord]], dict[int, StandingsRow], set[int]]:
    """Replay completed matches into (history, running table, roster).

    ``completed`` must be chronologically ordered with the same
    ``(match_date, kickoff_time)`` grouping semantics as the feature layer.
    """
    history: dict[int, list[TeamRecord]] = defaultdict(list)
    table: dict[int, StandingsRow] = defaultdict(StandingsRow)
    roster = {m.home_team_id for m in completed} | {m.away_team_id for m in completed}
    for tid in roster:
        table[tid]

    i, n = 0, len(completed)
    while i < n:
        key = (completed[i].match_date, completed[i].kickoff_time)
        j = i
        while j < n and (completed[j].match_date, completed[j].kickoff_time) == key:
            j += 1
        for m in completed[i:j]:
            home_rec, away_rec = m.as_records()
            history[m.home_team_id].append(home_rec)
            history[m.away_team_id].append(away_rec)
            _apply_result(table, m.home_team_id, home_rec)
            _apply_result(table, m.away_team_id, away_rec)
        i = j
    return history, table, roster


def score_fixtures(
    history: dict[int, list[TeamRecord]],
    table: dict[int, StandingsRow],
    roster: set[int],
    fixtures: list[Fixture],
    league: str | None = None,
) -> list[dict]:
    """Feature rows for scheduled fixtures (leakage-free: results never applied).

    Each returned row holds the 23 features plus a small context block used for
    display / output. A team with no prior match in the season gets the same
    documented defaults as a season opener (rest days NULL, everything else 0).
    """
    rows: list[dict] = []
    for f in fixtures:
        row = _feature_block(f, history[f.home_team_id], history[f.away_team_id], table, roster)
        row["league"] = league
        row["home_team_id"] = f.home_team_id
        row["away_team_id"] = f.away_team_id
        row["match_date"] = f.match_date.isoformat()
        row["season"] = None
        rows.append(row)
    return rows
