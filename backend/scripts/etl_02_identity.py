"""Step 02/03 - Identity schema + team matching.

Applies sql/02_identity.sql, then performs team matching:
  - teams        create one row per physical club (surrogate PK)
  - team_aliases seed 'name' and 'slug' aliases (source='api_seed')
  - team_seasons preserve the original API name/slug/logo for each (league, season)

Matching rule: resolve by slug alias first; fall back to name alias (covers a
future rename where the slug changes but the display name is still recognized).
A spelling that maps to a different team than expected raises a clear error
(identity collision) instead of silently splitting/rejoining identity.

Usage:
    python backend/scripts/etl_02_identity.py
"""
from __future__ import annotations

import sys

import psycopg2.extras

from db_common import (
    COLLECTED_SEASONS,
    LEAGUE,
    apply_sql,
    get_conn,
    load_json,
    raw_file,
)

ALIAS_SOURCE = "api_seed"


def ensure_alias(cur, team_id: int, form: str, value: str) -> None:
    """Bind (form, value) to team_id. Detect genuine collisions loudly."""
    cur.execute(
        "SELECT team_id FROM team_aliases WHERE form = %s AND value = %s",
        (form, value),
    )
    row = cur.fetchone()
    if row is None:
        cur.execute(
            "INSERT INTO team_aliases (team_id, form, value, source) VALUES (%s, %s, %s, %s)",
            (team_id, form, value, ALIAS_SOURCE),
        )
        return
    existing = row[0]
    if existing != team_id:
        raise ValueError(
            f"IDENTITY COLLISION: {form}='{value}' already bound to team {existing}, "
            f"cannot bind to team {team_id}"
        )


def resolve_team(cur, slug: str, name: str) -> int:
    """Return the team id for an observed (slug, name); create when unknown."""
    cur.execute(
        "SELECT team_id FROM team_aliases WHERE form = 'slug' AND value = %s", (slug,)
    )
    row = cur.fetchone()
    if row:
        team_id = row[0]
        ensure_alias(cur, team_id, "name", name)
        return team_id

    cur.execute(
        "SELECT team_id FROM team_aliases WHERE form = 'name' AND value = %s", (name,)
    )
    row = cur.fetchone()
    if row:
        team_id = row[0]
        ensure_alias(cur, team_id, "slug", slug)
        return team_id

    cur.execute(
        "INSERT INTO teams (canonical_name, canonical_slug) VALUES (%s, %s) RETURNING id",
        (name, slug),
    )
    team_id = cur.fetchone()[0]
    ensure_alias(cur, team_id, "slug", slug)
    ensure_alias(cur, team_id, "name", name)
    return team_id


def main() -> int:
    conn = get_conn()
    try:
        apply_sql(conn, "02_identity.sql")
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            n_memberships = 0
            for season in COLLECTED_SEASONS:
                path = raw_file(season, "teams.json")
                teams_json = load_json(path)

                cur.execute(
                    """
                    SELECT ls.id
                    FROM league_seasons ls
                    JOIN seasons s ON s.id = ls.season_id
                    WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
                      AND s.name = %s
                    """,
                    (LEAGUE, season),
                )
                row = cur.fetchone()
                if row is None:
                    print(f"[03] WARN: no league_seasons registration for {season}; skipping")
                    continue
                league_season_id = row[0]

                for t in teams_json["teams"]:
                    api_name = t["team"]
                    api_slug = t["slug"]
                    team_id = resolve_team(cur, api_slug, api_name)

                    cur.execute(
                        """
                        UPDATE teams
                           SET canonical_name = %s, canonical_slug = %s
                         WHERE id = %s
                        """,
                        (api_name, api_slug, team_id),
                    )
                    cur.execute(
                        """
                        INSERT INTO team_seasons (league_season_id, team_id, api_name, api_slug, logo_url)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (league_season_id, team_id) DO UPDATE
                           SET api_name = EXCLUDED.api_name,
                               api_slug = EXCLUDED.api_slug,
                               logo_url = EXCLUDED.logo_url
                        """,
                        (league_season_id, team_id, api_name, api_slug, t.get("logo_url")),
                    )
                    n_memberships += 1

            cur.execute("SELECT count(*) FROM teams")
            print(f"[03] teams rows: {cur.fetchone()[0]}")
            cur.execute("SELECT count(*) FROM team_aliases")
            print(f"[03] aliases rows: {cur.fetchone()[0]} (source={ALIAS_SOURCE})")
            cur.execute("SELECT count(*) FROM team_seasons")
            print(f"[03] team_seasons rows: {cur.fetchone()[0]} (observed {n_memberships})")
        conn.commit()
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())