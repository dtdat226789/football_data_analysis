"""Teams API: canonical identity, season memberships, form, matches, standings.

Team identity is resolved through ``team_aliases`` so any observed name or slug
spelling maps back to one canonical team, exactly as the ETL does.
"""
from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException

from .. import common
from ..deps import (
    ensure_season,
    fetched_cursor,
    norm_pagination,
    require_league,
    resolve_latest_season,
    resolve_team_id,
)
from .matches import _MATCH_COLUMNS, _MATCH_JOINS

router = APIRouter(tags=["teams"])


def _require_team(cur, slug: str) -> int:
    team_id = resolve_team_id(cur, slug)
    if team_id is None:
        raise HTTPException(status_code=404, detail=f"team '{slug}' not found")
    return team_id


def _resolve_league_season(cur, league: str, season: str | None) -> str:
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


@router.get("/teams")
def list_teams(limit: int = 50, offset: int = 0) -> dict:
    limit, offset = norm_pagination(limit, offset)
    with fetched_cursor() as cur:
        cur.execute("SELECT count(*) FROM teams")
        total = cur.fetchone()[0]
        cur.execute(
            "SELECT id, canonical_name, canonical_slug FROM teams "
            "ORDER BY canonical_name LIMIT %s OFFSET %s",
            (limit, offset),
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {"total": total, "limit": limit, "offset": offset, "teams": rows}


@router.get("/teams/{slug}")
def team_detail(slug: str) -> dict:
    with fetched_cursor() as cur:
        team_id = _require_team(cur, slug)
        cur.execute(
            "SELECT canonical_name, canonical_slug FROM teams WHERE id = %s",
            (team_id,),
        )
        team = cur.fetchone()
        cur.execute(
            """
            SELECT l.api_key AS league, l.name AS league_name, s.name AS season,
                   s.start_year, s.end_year, ts.api_name, ts.api_slug, ts.logo_url
            FROM team_seasons ts
            JOIN league_seasons ls ON ls.id = ts.league_season_id
            JOIN leagues l ON l.id = ls.league_id
            JOIN seasons s ON s.id = ls.season_id
            WHERE ts.team_id = %s
            ORDER BY l.api_key, s.start_year, s.end_year
            """,
            (team_id,),
        )
        memberships = cur.fetchall()
    return {
        "slug": slug,
        "team": dict(team),
        "memberships": [dict(m) for m in memberships],
    }


@router.get("/teams/{slug}/matches")
def team_matches(
    slug: str,
    league: str = common.DEFAULT_LEAGUE,
    season: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    require_league(league)
    limit, offset = norm_pagination(limit, offset)
    with fetched_cursor() as cur:
        team_id = _require_team(cur, slug)
        season = _resolve_league_season(cur, league, season)
        cur.execute(
            "SELECT count(*) FROM matches m JOIN league_seasons ls "
            "ON ls.id = m.league_season_id JOIN seasons s ON s.id = ls.season_id "
            "WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s) "
            "AND s.name = %s AND (m.home_team_id = %s OR m.away_team_id = %s)",
            (league, season, team_id, team_id),
        )
        total = cur.fetchone()[0]
        cur.execute(
            f"SELECT m.api_id, {_MATCH_COLUMNS} {_MATCH_JOINS} "
            f"WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s) "
            f"AND s.name = %s AND (m.home_team_id = %s OR m.away_team_id = %s) "
            f"ORDER BY m.match_date, m.kickoff_time, m.game_index "
            f"LIMIT %s OFFSET %s",
            (league, season, team_id, team_id, limit, offset),
        )
        rows = [dict(r) for r in cur.fetchall()]
    return {
        "team": slug,
        "league": league,
        "season": season,
        "total": total,
        "limit": limit,
        "offset": offset,
        "matches": rows,
    }


@router.get("/teams/{slug}/form")
def team_form(
    slug: str,
    league: str = common.DEFAULT_LEAGUE,
    season: str | None = None,
    context: Literal["all", "home", "away"] = "all",
    n: int = 5,
) -> dict:
    require_league(league)
    n = min(max(n, 1), 20)
    with fetched_cursor() as cur:
        team_id = _require_team(cur, slug)
        season = _resolve_league_season(cur, league, season)
        filters = [
            "ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)",
            "s.name = %s",
            "(m.home_team_id = %s OR m.away_team_id = %s)",
        ]
        params: list = [league, season, team_id, team_id]
        if context == "home":
            filters.append("m.home_team_id = %s")
            params.append(team_id)
        elif context == "away":
            filters.append("m.away_team_id = %s")
            params.append(team_id)
        where = " AND ".join(filters)
        cur.execute(
            f"""
            SELECT m.match_date, m.kickoff_time, m.game_index,
                   th.api_name AS home_team, ta.api_name AS away_team,
                   m.home_score, m.away_score, m.home_team_id, m.away_team_id
            FROM matches m
            JOIN league_seasons ls ON ls.id = m.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            JOIN team_seasons th ON th.league_season_id = m.league_season_id AND th.team_id = m.home_team_id
            JOIN team_seasons ta ON ta.league_season_id = m.league_season_id AND ta.team_id = m.away_team_id
            WHERE {where}
            ORDER BY m.match_date DESC, m.kickoff_time DESC, m.game_index DESC
            LIMIT %s
            """,
            params + [n],
        )
        raw = cur.fetchall()
    results = [_form_result(r, team_id) for r in raw]
    return {
        "team": slug,
        "league": league,
        "season": season,
        "context": context,
        "results": results,
    }


def _form_result(row, team_id: int) -> dict:
    home_score, away_score = row["home_score"], row["away_score"]
    is_home = row["home_team_id"] == team_id
    gf, ga = (home_score, away_score) if is_home else (away_score, home_score)
    if gf > ga:
        outcome, points = "W", 3
    elif gf == ga:
        outcome, points = "D", 1
    else:
        outcome, points = "L", 0
    return {
        "date": str(row["match_date"]),
        "kickoff_time": str(row["kickoff_time"]),
        "game_index": row["game_index"],
        "home_team": row["home_team"],
        "away_team": row["away_team"],
        "home_score": home_score,
        "away_score": away_score,
        "team_result": outcome,
        "points": points,
        "goal_difference": gf - ga,
    }


@router.get("/teams/{slug}/standings")
def team_standings(
    slug: str,
    league: str = common.DEFAULT_LEAGUE,
    season: str | None = None,
    view: Literal["classic", "luck", "goals"] = "classic",
) -> dict:
    require_league(league)
    with fetched_cursor() as cur:
        team_id = _require_team(cur, slug)
        season = _resolve_league_season(cur, league, season)
        cur.execute(
            """
            SELECT st.position, st.played, st.won, st.drawn, st.lost,
                   st.goals_for, st.goals_against, st.goal_difference,
                   st.points, st.metrics
            FROM standings st
            JOIN league_seasons ls ON ls.id = st.league_season_id
            JOIN seasons s ON s.id = ls.season_id
            WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
              AND s.name = %s AND st.view = %s AND st.team_id = %s
            """,
            (league, season, view, team_id),
        )
        row = cur.fetchone()
    return {
        "team": slug,
        "league": league,
        "season": season,
        "view": view,
        "row": dict(row) if row else None,
    }


def _team_stats_data(cur, slug: str, league: str, view: str) -> dict:
    """Aggregate a team's per-season tables and home/away splits for a league."""
    team_id = _require_team(cur, slug)
    cur.execute("SELECT id FROM leagues WHERE api_key = %s", (league,))
    league_row = cur.fetchone()
    if league_row is None:
        raise HTTPException(status_code=404, detail=f"unknown league '{league}'")
    league_id = league_row[0]

    cur.execute(
        """
        SELECT s.name AS season, st.position, st.played, st.won, st.drawn,
               st.lost, st.goals_for, st.goals_against, st.goal_difference,
               st.points
        FROM standings st
        JOIN league_seasons ls ON ls.id = st.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s AND st.team_id = %s AND st.view = %s
        ORDER BY s.start_year, s.end_year
        """,
        (league, team_id, view),
    )
    seasons = [dict(r) for r in cur.fetchall()]

    cur.execute(
        """
        SELECT m.home_team_id = %(team)s AS is_home,
               count(*) AS played,
               count(*) FILTER (
                   WHERE m.home_score > m.away_score
               ) AS home_won,
               count(*) FILTER (
                   WHERE m.away_score > m.home_score
               ) AS away_won,
               count(*) FILTER (WHERE m.home_score = m.away_score) AS drawn,
               count(*) FILTER (WHERE m.home_score < m.away_score) AS home_lost,
               count(*) FILTER (WHERE m.away_score < m.home_score) AS away_lost,
               sum(CASE WHEN m.home_team_id = %(team)s THEN m.home_score ELSE m.away_score END) AS gf,
               sum(CASE WHEN m.home_team_id = %(team)s THEN m.away_score ELSE m.home_score END) AS ga
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %(league)s
          AND (m.home_team_id = %(team)s OR m.away_team_id = %(team)s)
        GROUP BY m.home_team_id = %(team)s
        """,
        {"league": league, "team": team_id},
    )
    sides: dict = {}
    for r in cur.fetchall():
        is_home = bool(r["is_home"])
        won = r["home_won"] if is_home else r["away_won"]
        lost = r["home_lost"] if is_home else r["away_lost"]
        played = r["played"]
        point = 3 * won + r["drawn"]
        sides["home" if is_home else "away"] = {
            "played": played,
            "won": won,
            "drawn": r["drawn"],
            "lost": lost,
            "goals_for": r["gf"] or 0,
            "goals_against": r["ga"] or 0,
            "points": point,
            "win_pct": round(100 * won / played, 1) if played else 0.0,
        }

    played = sum(s["played"] for s in seasons)
    totals = {
        "played": played,
        "won": sum(s["won"] for s in seasons),
        "drawn": sum(s["drawn"] for s in seasons),
        "lost": sum(s["lost"] for s in seasons),
        "goals_for": sum(s["goals_for"] for s in seasons),
        "goals_against": sum(s["goals_against"] for s in seasons),
        "points": sum(s["points"] for s in seasons),
        "ppg": round(sum(s["points"] for s in seasons) / played, 2) if played else 0.0,
    }
    totals["goal_difference"] = totals["goals_for"] - totals["goals_against"]
    positions = [s["position"] for s in seasons if s["position"] is not None]
    return {
        "team": slug,
        "league": league,
        "view": view,
        "seasons": seasons,
        "totals": totals,
        "home_away": sides,
        "best": {
            "position": min(positions) if positions else None,
            "position_season": next(
                (s["season"] for s in seasons if s["position"] == min(positions)),
                None,
            ) if positions else None,
            "points": max((s["points"] for s in seasons), default=None),
        },
    }


@router.get("/teams/{slug}/stats")
def team_stats(
    slug: str,
    league: str = common.DEFAULT_LEAGUE,
    view: Literal["classic", "luck", "goals"] = "classic",
) -> dict:
    require_league(league)
    with fetched_cursor() as cur:
        return _team_stats_data(cur, slug, league, view)