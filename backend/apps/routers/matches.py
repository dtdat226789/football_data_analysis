"""Matches API: paginated, filterable match feeds from PostgreSQL (read-only)."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import (
    ensure_season,
    fetched_cursor,
    norm_pagination,
    require_league,
    resolve_latest_season,
)

router = APIRouter(tags=["matches"])

_MATCH_COLUMNS = """
    s.name AS season, m.game_index, m.match_date, m.kickoff_time,
    th.api_name AS home_team, ta.api_name AS away_team,
    m.home_score, m.away_score, m.home_ht, m.away_ht,
    m.first_goal_time, m.first_goal_time_extra
"""
_MATCH_JOINS = """
    FROM matches m
    JOIN league_seasons ls ON ls.id = m.league_season_id
    JOIN seasons s ON s.id = ls.season_id
    JOIN team_seasons th ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
    JOIN team_seasons ta ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
"""


def _resolve_season(cur, league: str, season: str | None) -> str:
    if season is None:
        season = resolve_latest_season(cur, league)
        if season is None:
            raise HTTPException(
                status_code=404,
                detail=f"no collected data for league '{league}'",
            )
    else:
        ensure_season(cur, league, season)
    return season


@router.get("/leagues/{league}/matches")
def list_matches(
    league: str,
    season: str | None = None,
    from_date: str | None = None,
    to_date: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    require_league(league)
    limit, offset = norm_pagination(limit, offset)
    with fetched_cursor() as cur:
        season = _resolve_season(cur, league, season)
        filters = [
            "ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)",
            "s.name = %s",
        ]
        params: list = [league, season]
        if from_date:
            filters.append("m.match_date >= %s")
            params.append(from_date)
        if to_date:
            filters.append("m.match_date <= %s")
            params.append(to_date)
        where = " AND ".join(filters)

        cur.execute(
            f"SELECT count(*) FROM matches m JOIN league_seasons ls "
            f"ON ls.id = m.league_season_id JOIN seasons s ON s.id = ls.season_id "
            f"WHERE {where}",
            params,
        )
        total = cur.fetchone()[0]
        cur.execute(
            f"SELECT m.api_id, {_MATCH_COLUMNS} {_MATCH_JOINS} "
            f"WHERE {where} ORDER BY m.match_date, m.kickoff_time, m.game_index "
            f"LIMIT %s OFFSET %s",
            params + [limit, offset],
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {
        "league": league,
        "season": season,
        "total": total,
        "limit": limit,
        "offset": offset,
        "matches": rows,
    }


@router.get("/matches/{api_id}")
def get_match(api_id: int) -> dict:
    with fetched_cursor() as cur:
        cur.execute(
            f"SELECT m.api_id, {_MATCH_COLUMNS}, l.api_key AS league "
            f"{_MATCH_JOINS} JOIN leagues l ON l.id = ls.league_id "
            f"WHERE m.api_id = %s",
            (api_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail=f"match {api_id} not found")
    return dict(row)