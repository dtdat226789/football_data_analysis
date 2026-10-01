"""Standings API: league table views (classic / luck / goals) from PostgreSQL."""
from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import (
    ensure_season,
    fetched_cursor,
    require_league,
    resolve_latest_season,
)

router = APIRouter(tags=["standings"])


@router.get("/leagues/{league}/standings")
def standings(
    league: str,
    season: str | None = None,
    view: Literal["classic", "luck", "goals"] = "classic",
) -> dict:
    require_league(league)
    with fetched_cursor() as cur:
        if season is None:
            season = resolve_latest_season(cur, league)
            if season is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"no collected data for league '{league}'",
                )
        else:
            ensure_season(cur, league, season)
        cur.execute(
            """
            SELECT ts.api_name AS team, st.position, st.played, st.won, st.drawn,
                   st.lost, st.goals_for, st.goals_against, st.goal_difference,
                   st.points, st.metrics
            FROM standings st
            JOIN team_seasons ts
              ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
            JOIN league_seasons ls ON ls.id = st.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
              AND s.name = %s AND st.view = %s
            ORDER BY st.position
            """,
            (league, season, view),
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {
        "league": league,
        "league_name": common.league_name(league),
        "season": season,
        "view": view,
        "rows": rows,
    }