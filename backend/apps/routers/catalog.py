"""Catalog API: leagues and seasons, config merged with the live DB registry."""
from __future__ import annotations

from fastapi import APIRouter

from .. import common
from ..deps import fetched_cursor, require_league

router = APIRouter(tags=["catalog"])


def _season_rows(cur, league: str) -> list[dict]:
    cur.execute(
        """
        SELECT s.name AS season, s.start_year, s.end_year,
               ls.declared_by_api, ls.season_state,
               (SELECT count(*) FROM matches m WHERE m.league_season_id = ls.id) AS matches,
               (SELECT count(DISTINCT ts.team_id) FROM team_seasons ts
                 WHERE ts.league_season_id = ls.id) AS teams,
               (SELECT count(*) FROM standings st
                 WHERE st.league_season_id = ls.id AND st.view = 'classic') AS standings_rows
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
        ORDER BY s.start_year, s.end_year
        """,
        (league,),
    )
    return [dict(r) for r in cur.fetchall()]


@router.get("/meta")
def meta() -> dict:
    try:
        with fetched_cursor() as cur:
            cur.execute("SELECT count(*) FROM leagues")
            db_leagues = cur.fetchone()[0]
        database: dict = {"reachable": True, "leagues": db_leagues}
    except Exception as exc:  # noqa: BLE001 - report unavailability, never crash
        database = {"reachable": False, "error": str(exc)}
    return {
        "api_version": "1.0.0",
        "default_league": common.DEFAULT_LEAGUE,
        "n_leagues": len(common.LEAGUE_CONFIG),
        "modules": common.MODULE_NAMES,
        "database": database,
    }


@router.get("/leagues")
def list_leagues() -> list[dict]:
    return common.league_listing()


@router.get("/leagues/{league}")
def league_detail(league: str) -> dict:
    require_league(league)
    meta = common.LEAGUE_CONFIG[league]
    with fetched_cursor() as cur:
        seasons = _season_rows(cur, league)
    return {
        "league": league,
        **meta,
        "has_data": common.league_report_dir(league) is not None,
        "seasons": seasons,
    }


@router.get("/leagues/{league}/seasons")
def league_seasons(league: str) -> dict:
    require_league(league)
    with fetched_cursor() as cur:
        seasons = _season_rows(cur, league)
    return {"league": league, "seasons": seasons}