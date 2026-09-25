"""Step 01 - Registry load.

Populates:
    leagues        <- every entry of /leagues/ (the discovery catalog)
    seasons        <- global season dictionary (league declared + collected seasons)
    league_seasons <- {league} x {declared, collected} pairs (our history registry)

This is the fix for SEASON_NOT_DECLARED: /leagues/ only declares current +
previous, so the authoritative historical registry lives in our database,
recorded via declared_by_api.

Usage:
    python backend/scripts/etl_01_registry.py
    python backend/scripts/etl_01_registry.py --league spain1
"""
from __future__ import annotations

import argparse
import sys

from db_common import (
    LEAGUE,
    RAW_DIR,
    apply_sql,
    collected_seasons,
    get_conn,
    load_json,
    normalize_season_state,
    parse_season_years,
    raw_file,
)


def upsert_leagues(cur, leagues_json: dict) -> int:
    n = 0
    for entry in leagues_json["leagues"]:
        cur.execute(
            """
            INSERT INTO leagues (api_key, name, country, url)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (api_key) DO UPDATE
               SET name = EXCLUDED.name,
                   country = EXCLUDED.country,
                   url = EXCLUDED.url
            """,
            (entry["league"], entry["name"], entry.get("country"), entry.get("url")),
        )
        n += 1
    return n


def upsert_season(cur, name: str) -> None:
    start, end = parse_season_years(name)
    cur.execute(
        """
        INSERT INTO seasons (name, start_year, end_year)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO UPDATE
           SET start_year = EXCLUDED.start_year,
               end_year   = EXCLUDED.end_year
        """,
        (name, start, end),
    )


def upsert_league_season(
    cur, league_id: int, season_id: int, declared_by_api: bool, season_state: str
) -> None:
    cur.execute(
        """
        INSERT INTO league_seasons (league_id, season_id, declared_by_api, season_state)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (league_id, season_id) DO UPDATE
           SET declared_by_api = EXCLUDED.declared_by_api,
               season_state    = EXCLUDED.season_state
        """,
        (league_id, season_id, declared_by_api, season_state),
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="etl_01_registry",
        description="Load registry tables (leagues / seasons / league_seasons).",
    )
    parser.add_argument("--league", default=LEAGUE, help="league slug (default: premier)")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    league = args.league
    leagues_path = RAW_DIR / league / "leagues.json"
    if not leagues_path.exists():
        print(f"ERROR: missing {leagues_path}")
        return 1
    leagues_json = load_json(leagues_path)

    entry = next((e for e in leagues_json["leagues"] if e["league"] == league), None)
    if entry is None:
        print(f"ERROR: no {league} entry in /leagues/")
        return 1
    declared = list(entry.get("seasons", []))
    collected = collected_seasons(league)

    conn = get_conn()
    try:
        apply_sql(conn, "01_registry.sql")
        with conn.cursor() as cur:
            n_leagues = upsert_leagues(cur, leagues_json)
            print(f"[01] leagues: {n_leagues} upserted (catalog)")

            cur.execute("SELECT id FROM leagues WHERE api_key = %s", (league,))
            league_id = cur.fetchone()[0]

            # Global season dictionary: declared seasons + collected seasons.
            season_names = sorted(
                set(declared) | set(collected),
                key=lambda name: parse_season_years(name) or (0, 0),
            )
            for name in season_names:
                upsert_season(cur, name)
            print(f"[01] seasons: attempted {len(season_names)} upserts")

            # Registry pairs. Collected seasons carry their own season_state.
            for name in season_names:
                cur.execute("SELECT id FROM seasons WHERE name = %s", (name,))
                season_id = cur.fetchone()[0]
                declared_flag = name in declared
                state = "unknown"
                if name in collected:
                    results = load_json(raw_file(name, "results.json", league))
                    state = normalize_season_state(results.get("season_state", "unknown"))
                upsert_league_season(
                    cur, league_id, season_id, declared_flag, state
                )

            cur.execute(
                """
                SELECT s.name, ls.declared_by_api, ls.season_state
                FROM league_seasons ls
                JOIN seasons s ON s.id = ls.season_id
                WHERE ls.league_id = %s
                ORDER BY s.start_year, s.end_year
                """,
                (league_id,),
            )
            rows = cur.fetchall()
            print(f"[01] league_seasons registrations: {len(rows)}")
            for name, declared_flag, state in rows:
                print(f"       {name:12} declared_by_api={declared_flag!s:5} state={state}")
        conn.commit()
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())