"""Dashboard API: aggregate view for the landing page (read-only).

One call backs the whole global dashboard — top leagues, current leaders,
recent + upcoming matches, and the league catalog grouped by region. All
database reads use ``fetched_cursor`` (rolled back per request); upcoming
matches come from the fixtures file dump with their model predictions.
"""
from __future__ import annotations

from fastapi import APIRouter

from .. import common
from ..deps import fetched_cursor
from .fixtures import FIXTURES_DIR, fixture_rows

router = APIRouter(tags=["dashboard"])

TOP_LEAGUES_LIMIT = 8
TOP_CLUBS_LIMIT = 12
RECENT_MATCHES_LIMIT = 10
UPCOMING_MATCHES_LIMIT = 10


def _match_counts(cur) -> dict[str, int]:
    """slug -> number of collected matches in the analytics DB."""
    cur.execute(
        """
        SELECT l.api_key AS slug, count(*) AS matches
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN leagues l ON l.id = ls.league_id
        GROUP BY l.id
        """
    )
    return {r["slug"]: r["matches"] for r in cur.fetchall()}


def _top_leagues(cur, counts: dict[str, int]) -> list[dict]:
    rows = [
        {
            "slug": slug,
            "name": meta.get("name", slug),
            "country": meta.get("country", ""),
            "region": common.regions.league_region(meta.get("country", "")),
            "teams": meta.get("teams", 0),
            "matches": counts.get(slug, 0),
            "has_data": common.league_report_dir(slug) is not None,
        }
        for slug, meta in common.LEAGUE_CONFIG.items()
    ]
    rows.sort(key=lambda r: r["matches"], reverse=True)
    return rows[:TOP_LEAGUES_LIMIT]


def _top_clubs(cur) -> list[dict]:
    """Current league leaders (position 1, classic view, latest season)."""
    cur.execute(
        """
        WITH latest AS (
            SELECT DISTINCT ON (ls.league_id) ls.league_id, ls.id AS league_season_id,
                   s.name AS season
            FROM league_seasons ls
            JOIN seasons s ON s.id = ls.season_id
            WHERE EXISTS (SELECT 1 FROM matches m WHERE m.league_season_id = ls.id)
            ORDER BY ls.league_id, s.start_year DESC, s.end_year DESC
        )
        SELECT l.api_key AS league, l.name AS league_name, l.country,
               latest.season, st.position, st.points, ts.api_name AS team
        FROM standings st
        JOIN latest ON latest.league_season_id = st.league_season_id
        JOIN team_seasons ts
          ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
        JOIN leagues l ON l.id = latest.league_id
        WHERE st.view = 'classic' AND st.position = 1
        ORDER BY st.points DESC
        LIMIT %s
        """,
        (TOP_CLUBS_LIMIT,),
    )
    rows = [dict(r) for r in cur.fetchall()]
    for row in rows:
        row["region"] = common.regions.league_region(row.get("country") or "")
    return rows


def _leagues_by_region(cur, counts: dict[str, int]) -> dict[str, list[dict]]:
    """League catalog grouped into dashboard region buckets."""
    buckets: dict[str, list[dict]] = {"europe": [], "asia": [], "america": [], "other": []}
    for slug, meta in common.LEAGUE_CONFIG.items():
        region = common.regions.league_region(meta.get("country", ""))
        buckets[region].append(
            {
                "slug": slug,
                "name": meta.get("name", slug),
                "country": meta.get("country", ""),
                "region": region,
                "teams": meta.get("teams", 0),
                "matches": counts.get(slug, 0),
                "has_data": common.league_report_dir(slug) is not None,
                "has_fixtures": (FIXTURES_DIR / f"{slug}.json").exists(),
            }
        )
    for region in buckets:
        buckets[region].sort(key=lambda r: r["matches"], reverse=True)
    return buckets


@router.get("/dashboard")
def dashboard() -> dict:
    """Aggregate payload for the global landing dashboard."""
    from .matches import recent_matches

    with fetched_cursor() as cur:
        counts = _match_counts(cur)
        top_leagues = _top_leagues(cur, counts)
        top_clubs = _top_clubs(cur)
        leagues_by_region = _leagues_by_region(cur, counts)

    upcoming = fixture_rows()
    upcoming.sort(key=lambda r: r["predictions"]["confidence"], reverse=True)
    recent = recent_matches(limit=RECENT_MATCHES_LIMIT)["matches"]

    return {
        "generated_at": None,
        "meta": {
            "n_leagues": len(common.LEAGUE_CONFIG),
            "with_fixtures": sum(bool(leagues_by_region[r]) for r in leagues_by_region),
            "n_upcoming": len(upcoming),
        },
        "top_leagues": top_leagues,
        "top_clubs": top_clubs,
        "recent_matches": recent,
        "upcoming_matches": upcoming[:UPCOMING_MATCHES_LIMIT],
        "leagues_by_region": leagues_by_region,
    }