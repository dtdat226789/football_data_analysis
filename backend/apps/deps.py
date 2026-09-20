"""Shared FastAPI dependencies: read-only DB access and validation helpers.

PostgreSQL is treated as a read-only source of truth: every request that opens
a cursor rolls the transaction back before closing, so the API never mutates
the analytics database.
"""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import psycopg2.extras
from fastapi import HTTPException

from .common import DEFAULT_LEAGUE, LEAGUE_CONFIG, ensure_scripts_path

ensure_scripts_path()

from db_common import get_conn, parse_season_years  # noqa: E402

MAX_LIMIT = 200


@contextmanager
def fetched_cursor() -> Iterator[psycopg2.extras.DictCursor]:
    """Read-only cursor: always rolled back, never committed."""
    conn = get_conn()
    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        try:
            yield cur
        finally:
            cur.close()
        conn.rollback()
    finally:
        conn.close()


def norm_pagination(limit: int, offset: int, max_limit: int = MAX_LIMIT) -> tuple[int, int]:
    """Clamp offset/limit to a sane window."""
    return min(max(limit, 1), max_limit), max(offset, 0)


def require_league(league: str) -> None:
    if league not in LEAGUE_CONFIG:
        raise HTTPException(status_code=404, detail=f"unknown league '{league}'")


def resolve_team_id(cur, slug: str) -> int | None:
    """Resolve a name or slug to a canonical team id via team_aliases."""
    cur.execute(
        """
        SELECT team_id FROM team_aliases
        WHERE form IN ('name', 'slug') AND value = %s
        ORDER BY (form = 'slug') DESC
        LIMIT 1
        """,
        (slug,),
    )
    row = cur.fetchone()
    return row[0] if row else None


def resolve_latest_season(cur, league: str) -> str | None:
    """Latest collected season (the one that actually has matches)."""
    cur.execute(
        """
        SELECT s.name
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
          AND EXISTS (SELECT 1 FROM matches m WHERE m.league_season_id = ls.id)
        ORDER BY s.start_year DESC, s.end_year DESC
        LIMIT 1
        """,
        (league,),
    )
    row = cur.fetchone()
    return row[0] if row else None


def ensure_season(cur, league: str, season: str) -> None:
    """404 for seasons the league has not registered."""
    cur.execute(
        """
        SELECT 1
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
          AND s.name = %s
        """,
        (league, season),
    )
    if cur.fetchone() is None:
        raise HTTPException(
            status_code=404, detail=f"unknown season '{season}' for league '{league}'"
        )