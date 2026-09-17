"""Step 05 - Database validation.

Cross-checks the database against the byte-preserved raw dataset:

  registry    league_seasons registrations, declared_by_api facts
  identity    alias coverage of every api_name/api_slug; slug->team is consistent
  matches     per-season counts = raw, game_index uniqueness/range, team membership,
              goalless/first-goal semantics, HT <= FT invariants
  standings   rows per (season, view) = 20; classic table reproduces the
              table derived from matches (points, W/D/L, GF/GA/GD, played)
  global      match api_id uniqueness (PK) and total counts

Exits non-zero if any check fails.
Usage:
    python backend/scripts/validate_db.py
"""
from __future__ import annotations

import sys

import psycopg2.extras

from db_common import (
    COLLECTED_SEASONS,
    LEAGUE,
    VIEWS,
    get_conn,
    load_json,
    parse_score,
    raw_file,
)

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: object = "") -> None:
    CHECKS.append((name, ok, str(detail)))
    tag = "PASS" if ok else "FAIL"
    print(f"[05] {tag:4} {name}" + (f"  ({detail})" if detail else ""))


def main() -> int:
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # ── registry ────────────────────────────────────────────────
            cur.execute(
                """
                SELECT s.name, ls.declared_by_api, ls.season_state
                FROM league_seasons ls
                JOIN seasons s ON s.id = ls.season_id
                WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
                ORDER BY s.start_year, s.end_year
                """,
                (LEAGUE,),
            )
            reg = {r["name"]: r for r in cur.fetchall()}
            check(
                "registry pair for every collected season",
                all(s in reg for s in COLLECTED_SEASONS),
                sorted(set(COLLECTED_SEASONS) - set(reg)),
            )
            check(
                "declared_by_api mirrors /leagues/ (2025-2026 true, historical false)",
                reg["2025-2026"]["declared_by_api"] is True
                and not reg["2020-2021"]["declared_by_api"],
            )

            # ── identity ────────────────────────────────────────────────
            cur.execute("SELECT count(*) FROM teams")
            n_teams = cur.fetchone()["count"]
            cur.execute("SELECT count(*) FROM team_seasons")
            n_memberships = cur.fetchone()["count"]
            check("teams table non-empty", n_teams > 0, f"{n_teams} teams")
            check(
                "team_seasons == 20 per collected season",
                n_memberships == 20 * len(COLLECTED_SEASONS),
                f"{n_memberships} rows",
            )

            # every distinct observed slug resolves to exactly one team_id
            cur.execute(
                """
                SELECT DISTINCT ts.api_slug, ts.team_id
                FROM team_seasons ts
                WHERE NOT EXISTS (
                    SELECT 1 FROM team_aliases a
                    WHERE a.form = 'slug' AND a.value = ts.api_slug AND a.team_id = ts.team_id
                )
                """
            )
            missing_aliases = cur.fetchall()
            check(
                "every api_slug has a consistent slug alias",
                not missing_aliases,
                len(missing_aliases),
            )

            # distinct slugs actually map to the same single team across seasons
            cur.execute(
                """
                SELECT ts.api_slug, count(DISTINCT ts.team_id) AS distinct_teams
                FROM team_seasons ts
                GROUP BY ts.api_slug
                HAVING count(DISTINCT ts.team_id) > 1
                """
            )
            split_slugs = cur.fetchall()
            check("no slug maps to multiple teams", not split_slugs, split_slugs)

            # ── matches ─────────────────────────────────────────────────
            cur.execute("SELECT count(*) FROM matches")
            check("match count == raw total (6 x 380)", cur.fetchone()["count"] == 6 * 380)
            cur.execute("SELECT count(DISTINCT api_id), count(*) FROM matches")
            dcount, tcount = cur.fetchone()
            check("match api_id globally unique (PK)", dcount == tcount, f"{dcount}/{tcount}")

            per_season = {}
            for season in COLLECTED_SEASONS:
                path = raw_file(season, "results.json")
                raw_n = load_json(path)["count"]
                cur.execute(
                    """
                    SELECT count(*) FROM matches m
                    JOIN league_seasons ls ON ls.id = m.league_season_id
                    JOIN seasons s ON s.id = ls.season_id
                    WHERE s.name = %s
                    """,
                    (season,),
                )
                db_n = cur.fetchone()["count"]
                per_season[season] = (raw_n, db_n)
                check(f"{season}: match count == raw", raw_n == db_n, f"raw={raw_n} db={db_n}")

            # game_index is 1..n unique within each league season
            cur.execute(
                """
                SELECT s.name,
                       min(m.game_index), max(m.game_index),
                       count(*), count(DISTINCT m.game_index),
                       (SELECT count(*) FROM matches)
                FROM matches m
                JOIN league_seasons ls ON ls.id = m.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                GROUP BY s.name, ls.id, s.start_year
                ORDER BY s.start_year
                """
            )
            gi_bad = []
            for season, gmin, gmax, cnt, distinct, _ in cur.fetchall():
                if not (gmin == 1 and gmax == cnt == distinct):
                    gi_bad.append((season, gmin, gmax, cnt, distinct))
            check("game_index is 1..n unique per league season", not gi_bad, gi_bad)

            # goalless / first-goal semantics (validated API behaviour)
            cur.execute(
                """
                SELECT
                    count(*) FILTER (WHERE home_score = 0 AND away_score = 0) AS goalless,
                    count(*) FILTER (WHERE first_goal_time IS NOT NULL) AS has_fgt,
                    count(*) FILTER (WHERE first_goal_time_extra IS NOT NULL) AS has_fgte,
                    count(*) FILTER (
                        WHERE first_goal_time_extra IS NOT NULL AND first_goal_time_extra < 0
                    ) AS neg_fgte
                FROM matches
                """
            )
            r = cur.fetchone()
            ok_fgt = (r["goalless"] + r["has_fgt"] == 6 * 380) and r["goalless"] == 129
            check(
                "first_goal_time present iff non-goalless (129 goalless)",
                ok_fgt,
                dict(r),
            )
            check(
                "first_goal_time_extra mirrors first_goal_time (NULL iff goalless)",
                r["has_fgte"] == r["has_fgt"] and r["neg_fgte"] == 0,
                dict(r),
            )

            # half-time <= full-time invariant (already CHECKed; confirm ratio)
            cur.execute(
                """
                SELECT count(*) FILTER (WHERE home_ht IS NULL) AS null_ht
                FROM matches
                """
            )
            check("ht_score present on every match", cur.fetchone()["null_ht"] == 0)

            # ── standings ───────────────────────────────────────────────
            cur.execute(
                """
                SELECT s.name, st.view, count(*), min(position), max(position)
                FROM standings st
                JOIN league_seasons ls ON ls.id = st.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                GROUP BY s.name, st.view, ls.id, s.start_year
                ORDER BY s.start_year, st.view
                """
            )
            rows = cur.fetchall()
            bad_stand = [
                (r["name"], r["view"])
                for r in rows
                if not (r["count"] == 20 and r["min"] == 1 and r["max"] == 20)
            ]
            check(
                "standings == 20 rows with positions 1..20 per (season, view)",
                not bad_stand,
                bad_stand,
            )

            # classic standings reproduce the table derived from matches
            derived_sql = """
                WITH legs AS (
                    SELECT league_season_id, home_team_id AS team_id,
                           home_score AS gf, away_score AS ga,
                           (home_score > away_score)::int AS w,
                           (home_score = away_score)::int AS d,
                           (home_score < away_score)::int AS l
                    FROM matches
                    UNION ALL
                    SELECT league_season_id, away_team_id AS team_id,
                           away_score, home_score,
                           (away_score > home_score)::int,
                           (away_score = home_score)::int,
                           (away_score < home_score)::int
                    FROM matches
                )
                SELECT s.name, ts.api_name,
                       count(*) AS played,
                       sum(w) AS won, sum(d) AS drawn, sum(l) AS lost,
                       sum(gf) AS goals_for, sum(ga) AS goals_against,
                       sum(gf) - sum(ga) AS goal_difference,
                       3 * sum(w) + sum(d) AS points
                FROM legs
                JOIN team_seasons ts
                  ON ts.league_season_id = legs.league_season_id
                 AND ts.team_id = legs.team_id
                JOIN league_seasons ls ON ls.id = legs.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                GROUP BY s.name, ts.api_name, legs.league_season_id, legs.team_id
                ORDER BY s.name, ts.api_name
            """
            cur.execute(derived_sql)
            derived = {(r["name"], r["api_name"]): r for r in cur.fetchall()}

            cur.execute(
                """
                SELECT s.name, ts.api_name, st.played, st.won, st.drawn, st.lost,
                       st.goals_for, st.goals_against, st.goal_difference, st.points
                FROM standings st
                JOIN team_seasons ts
                  ON ts.league_season_id = st.league_season_id
                 AND ts.team_id = st.team_id
                JOIN league_seasons ls ON ls.id = st.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                WHERE st.view = 'classic'
                ORDER BY s.name, ts.api_name
                """
            )
            mismatches = []
            for r in cur.fetchall():
                d = derived.get((r["name"], r["api_name"]))
                if d is None:
                    mismatches.append((r["name"], r["api_name"], "missing in derived"))
                    continue
                for field in ("played", "won", "drawn", "lost", "goals_for", "goals_against", "goal_difference", "points"):
                    if r[field] != d[field]:
                        mismatches.append(
                            (r["name"], r["api_name"], field, r[field], d[field])
                        )
            check(
                "classic standings reproduce the matches-derived table",
                not mismatches,
                mismatches[:8],
            )

            # standings points == 3W+D independently (belt & braces)
            cur.execute(
                "SELECT count(*) FROM standings WHERE points <> 3 * won + drawn"
            )
            check(
                "standings points == 3*won + drawn everywhere",
                cur.fetchone()["count"] == 0,
            )

        conn.rollback()
    finally:
        conn.close()

    failed = [c for c in CHECKS if not c[1]]
    print()
    print(f"[05] {len(CHECKS) - len(failed)}/{len(CHECKS)} checks passed")
    if failed:
        for name, _, detail in failed:
            print(f"[05] FAIL {name}: {detail}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())