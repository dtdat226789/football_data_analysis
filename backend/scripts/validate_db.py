"""Step 05 - Database validation.

Cross-checks the database against the byte-preserved raw dataset:

  registry    league_seasons registrations, declared_by_api facts
  identity    alias coverage of every api_name/api_slug; slug->team is consistent
  matches     per-season counts = loadable raw matches, game_index uniqueness/range,
              team membership, goalless/first-goal semantics, HT null-pairing
  standings   rows per (season, view) = league teams at distinct raw positions;
              classic table reproduces the table derived from matches (points,
              W/D/L, GF/GA/GD, played) for leagues/seasons whose raw matches are
              all loadable
  global      match api_id uniqueness (PK) and total counts

Every count is scoped to the current league, so a database holding multiple
leagues validates each one independently. Cancelled/awarded ('CAN.'/'AWA.'),
unparseable, and membership-missing raw matches are excluded from expected
counts because the matches schema cannot represent them (etl_03 skips them and
logs them under data/validation/skipped_matches/). A raw match counts as
loadable when its score is playable and both teams belong to the season's
teams.json roster - the same rule etl_03 applies. Teams.json entries sharing a
slug are one club: etl_02 merges them into a single team_seasons row (last
 entry wins), so identity and standings expectations count one team per slug.
 Roster entries that never play a match in results.json and are a hyphen-variant
 of a participant (upstream phantom rows, e.g. 'MG-Bahia' vs 'Bahia') are
 dropped by etl_02 before the slug merge and excluded here the same way.

Exits non-zero if any check fails.
Usage:
    python backend/scripts/validate_db.py
    python backend/scripts/validate_db.py --league spain1
"""
from __future__ import annotations

import argparse
import sys

import psycopg2.extras

from db_common import (
    LEAGUE,
    VIEWS,
    catalog_seasons,
    collected_seasons,
    get_conn,
    load_json,
    phantom_team_names,
    raw_file,
    score_status,
)

CHECKS: list[tuple[str, bool, str]] = []


def roster_for_season(teams_data: dict, matches: list) -> dict[str, str]:
    """The roster etl_02 builds for a season: phantom rows dropped, then slug merge.

    Returns slug -> the api_name that ends up in team_seasons.
    """
    phantoms = phantom_team_names(teams_data.get("teams", []), matches)
    kept = [
        t
        for t in teams_data.get("teams", [])
        if not (isinstance(t, dict) and t.get("team") in phantoms)
    ]
    return roster_by_slug({"teams": kept})


def check(name: str, ok: bool, detail: object = "") -> None:
    CHECKS.append((name, ok, str(detail)))
    tag = "PASS" if ok else "FAIL"
    print(f"[05] {tag:4} {name}" + (f"  ({detail})" if detail else ""))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="validate_db",
        description="Cross-check the database against the raw dataset.",
    )
    parser.add_argument("--league", default=LEAGUE, help="league slug (default: premier)")
    return parser.parse_args(argv)


def loadable_count(raw: dict, roster: set[str]) -> int:
    """Raw matches etl_03 will load: playable score and both teams in roster."""
    return sum(
        1
        for m in raw.get("matches", [])
        if isinstance(m, dict)
        and m.get("homeTeam") in roster
        and m.get("awayTeam") in roster
        and score_status(m.get("score")) == "playable"
    )


def roster_by_slug(teams_data: dict) -> dict[str, str]:
    """teams.json entries merged by slug: etl_02 keeps the last name per slug.

    Returns slug -> the api_name that ends up in team_seasons.
    """
    merged: dict[str, str] = {}
    for t in teams_data.get("teams", []):
        if isinstance(t, dict):
            merged[t["slug"]] = t["team"]
    return merged


def table_position_bound(table_data: dict, roster: set[str]) -> int:
    """Highest raw position etl_03 can load; rows outside the roster are skipped."""
    return max(
        (
            r.get("position")
            for r in table_data.get("table", [])
            if isinstance(r, dict) and r.get("team") in roster
        ),
        default=0,
    )


GAME_INDEX_QUERY = """
SELECT s.name AS season,
       min(m.game_index) AS gmin,
       max(m.game_index) AS gmax,
       count(*) AS cnt,
       count(DISTINCT m.game_index) AS distinct
FROM matches m
JOIN league_seasons ls ON ls.id = m.league_season_id
JOIN seasons s ON s.id = ls.season_id
JOIN leagues l ON l.id = ls.league_id
WHERE l.api_key = %s
GROUP BY s.name, s.start_year
ORDER BY s.start_year
"""


def game_index_problems(cur, league: str, clean_seasons: set[str]) -> list[tuple]:
    """Seasons whose game_index is duplicated, or gapped inside a clean season.

    A clean season (every raw match loadable) must carry game_index 1..n with
    no holes. A season with skipped, awarded or membership-missing matches
    legitimately has gaps, but must still never reuse a game_index.
    """
    cur.execute(GAME_INDEX_QUERY, (league,))
    problems: list[tuple] = []
    for row in cur.fetchall():
        season = row["season"]
        gmin, gmax, cnt, distinct = (
            row["gmin"], row["gmax"], row["cnt"], row["distinct"],
        )
        duplicate = distinct != cnt
        contiguous = gmin == 1 and gmax == cnt == distinct
        if duplicate or (season in clean_seasons and not contiguous):
            problems.append((season, gmin, gmax, cnt, distinct))
    return problems


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    league = args.league
    seasons = collected_seasons(league)
    declared = set(catalog_seasons(league))

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
                (league,),
            )
            reg = {r["name"]: r for r in cur.fetchall()}
            check(
                "registry pair for every collected season",
                all(s in reg for s in seasons),
                sorted(set(seasons) - set(reg)),
            )
            check(
                "declared_by_api mirrors /leagues/ (declared true, others false)",
                (
                    all(reg.get(s, {}).get("declared_by_api") is True for s in declared)
                    and all(
                        not reg.get(s, {}).get("declared_by_api")
                        for s in seasons
                        if s not in declared
                    )
                ),
                declared,
            )

            # ── identity ────────────────────────────────────────────────
            cur.execute("SELECT count(*) FROM teams")
            n_teams = cur.fetchone()["count"]
            season_teams: dict[str, int] = {}
            season_roster: dict[str, set[str]] = {}
            for season in seasons:
                teams_data = load_json(raw_file(season, "teams.json", league))
                results_path = raw_file(season, "results.json", league)
                results = (
                    load_json(results_path) if results_path.exists() else {"matches": []}
                )
                # etl_02 drops phantom roster rows, then merges the remaining
                # entries sharing a slug into one team_seasons row (last entry
                # wins for api_name), so the roster is one name per slug.
                merged = roster_for_season(teams_data, results.get("matches", []))
                season_teams[season] = len(merged)
                season_roster[season] = set(merged.values())
            cur.execute(
                """
                SELECT s.name, count(*) AS n
                FROM team_seasons ts
                JOIN league_seasons ls ON ls.id = ts.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE l.api_key = %s
                GROUP BY s.name, ls.id, s.start_year
                ORDER BY s.start_year
                """,
                (league,),
            )
            n_memberships = {r["name"]: r["n"] for r in cur.fetchall()}
            check("teams table non-empty", n_teams > 0, f"{n_teams} teams")
            check(
                "team_seasons == league teams per collected season",
                sorted(n_memberships) == sorted(season_teams)
                and all(
                    n_memberships.get(s) == season_teams[s] for s in seasons
                ),
                {
                    s: f"{n_memberships.get(s)} rows (expected {season_teams[s]})"
                    for s in seasons
                },
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
            cur.execute(
                """
                SELECT count(*) FROM matches m
                JOIN league_seasons ls ON ls.id = m.league_season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE l.api_key = %s
                """,
                (league,),
            )
            total_db = cur.fetchone()["count"]

            raw_counts: dict[str, int] = {}
            clean_seasons: set[str] = set()
            for season in seasons:
                raw = load_json(raw_file(season, "results.json", league))
                raw_counts[season] = loadable_count(raw, season_roster[season])
                if raw_counts[season] == len(raw.get("matches", [])):
                    clean_seasons.add(season)
            expected_total = sum(raw_counts[s] for s in seasons)
            check(
                "match count == loadable raw total",
                total_db == expected_total,
                f"db={total_db} expected={expected_total}",
            )
            cur.execute("SELECT count(DISTINCT api_id), count(*) FROM matches")
            dcount, tcount = cur.fetchone()
            check("match api_id globally unique (PK)", dcount == tcount, f"{dcount}/{tcount}")

            for season in seasons:
                raw_n = raw_counts[season]
                cur.execute(
                    """
                    SELECT count(*) FROM matches m
                    JOIN league_seasons ls ON ls.id = m.league_season_id
                    JOIN seasons s ON s.id = ls.season_id
                    JOIN leagues l ON l.id = ls.league_id
                    WHERE s.name = %s AND l.api_key = %s
                    """,
                    (season, league),
                )
                db_n = cur.fetchone()["count"]
                check(
                    f"{season}: match count == loadable raw",
                    raw_n == db_n,
                    f"raw={raw_n} db={db_n}",
                )

            gi_bad = game_index_problems(cur, league, clean_seasons)
            check(
                "game_index contiguous 1..n when clean, unique otherwise",
                not gi_bad,
                gi_bad,
            )

            # goalless matches never carry a first-goal time; fgt_extra mirrors fgt
            cur.execute(
                """
                SELECT
                    count(*) FILTER (WHERE home_score = 0 AND away_score = 0) AS goalless,
                    count(*) FILTER (
                        WHERE home_score = 0 AND away_score = 0
                          AND first_goal_time IS NOT NULL
                    ) AS goalless_with_fgt,
                    count(*) FILTER (
                        WHERE (first_goal_time IS NULL) <> (first_goal_time_extra IS NULL)
                    ) AS fgt_mirror_broken,
                    count(*) FILTER (
                        WHERE first_goal_time_extra IS NOT NULL AND first_goal_time_extra < 0
                    ) AS neg_fgte
                FROM matches m
                JOIN league_seasons ls ON ls.id = m.league_season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE l.api_key = %s
                """,
                (league,),
            )
            r = cur.fetchone()
            check(
                "no first_goal_time on a goalless match",
                r["goalless_with_fgt"] == 0,
                dict(r),
            )
            check(
                "first_goal_time_extra mirrors first_goal_time (and non-negative)",
                r["fgt_mirror_broken"] == 0 and r["neg_fgte"] == 0,
                dict(r),
            )

            # half-time scores are recorded together or not at all
            cur.execute(
                """
                SELECT count(*) FILTER (WHERE (home_ht IS NULL) <> (away_ht IS NULL)) AS stride,
                       count(*) FILTER (WHERE home_ht IS NULL) AS null_ht
                FROM matches m
                JOIN league_seasons ls ON ls.id = m.league_season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE l.api_key = %s
                """,
                (league,),
            )
            ht_r = cur.fetchone()
            check(
                "half-time scores null together (or absent via 'Not found')",
                ht_r["stride"] == 0,
                f"null_ht={ht_r['null_ht']}",
            )

            # ── standings ───────────────────────────────────────────────
            # Every roster team must have one row per view, at a distinct raw
            # position. A raw table row for a team outside the roster is
            # skipped by etl_03, so its position may leave a hole below the
            # highest loadable position - that is mirrored here via table_max
            # instead of demanding an exact 1..n range.
            table_max: dict[tuple[str, str], int] = {}
            for season in seasons:
                for view in VIEWS:
                    data = load_json(raw_file(season, f"table_{view}.json", league))
                    table_max[(season, view)] = table_position_bound(
                        data, season_roster[season]
                    )
            cur.execute(
                """
                SELECT s.name, st.view, count(*), min(position), max(position),
                       count(DISTINCT position) AS distinct_positions
                FROM standings st
                JOIN league_seasons ls ON ls.id = st.league_season_id
                JOIN seasons s ON s.id = ls.season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE l.api_key = %s
                GROUP BY s.name, st.view, ls.id, s.start_year
                ORDER BY s.start_year, st.view
                """,
                (league,),
            )
            rows = cur.fetchall()
            groups = {(r["name"], r["view"]) for r in rows}
            missing_groups = [
                (s, v) for s in seasons for v in VIEWS if (s, v) not in groups
            ]
            check(
                "standings loaded for every (season, view)",
                not missing_groups,
                missing_groups,
            )
            bad_stand = [
                (r["name"], r["view"])
                for r in rows
                if not (
                    r["count"] == season_teams.get(r["name"])
                    and r["min"] >= 1
                    and r["max"] <= table_max.get((r["name"], r["view"]), 0)
                    and r["distinct_positions"] == r["count"]
                )
            ]
            check(
                "standings == league teams at distinct raw positions per (season, view)",
                not bad_stand,
                bad_stand,
            )

            # classic standings reproduce the table derived from matches,
            # for seasons whose raw matches are all loadable AND whose retained
            # season_state is 'complete' (a 'complete' season whose standings
            # snapshot predates its results file is genuinely drifted data)
            checked = clean_seasons & {
                s for s in seasons if reg.get(s, {}).get("season_state") == "complete"
            }
            if checked:
                check_list = list(checked)
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
                    JOIN leagues l ON l.id = ls.league_id
                    WHERE l.api_key = %s AND s.name = ANY(%s::text[])
                    GROUP BY s.name, ts.api_name, legs.league_season_id, legs.team_id
                    ORDER BY s.name, ts.api_name
                """
                cur.execute(derived_sql, (league, check_list))
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
                    JOIN leagues l ON l.id = ls.league_id
                    WHERE st.view = 'classic' AND l.api_key = %s
                      AND s.name = ANY(%s::text[])
                    ORDER BY s.name, ts.api_name
                    """,
                    (league, check_list),
                )
                mismatches = []
                drift = []
                by_season = {}
                for r in cur.fetchall():
                    by_season.setdefault(r["name"], []).append(r)
                for season, st_rows in by_season.items():
                    d_rows = [
                        derived.get((season, row["api_name"])) for row in st_rows
                    ]
                    if any(d is None for d in d_rows):
                        drift.append(season)
                        continue
                    if sum(r["played"] for r in st_rows) != sum(
                        d["played"] for d in d_rows
                    ):
                        drift.append(season)
                        continue
                    for r, d in zip(st_rows, d_rows):
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
                check(
                    "classic reproduction checked for clean seasons",
                    True,
                    {
                        "compared": sorted(set(by_season) - set(drift)),
                        "scale_drifted": sorted(drift),
                    },
                )
            else:
                check(
                    "classic standings reproduce the matches-derived table",
                    True,
                    "no fully-loadable, complete seasons for this league",
                )

            # standings points == 3W+D independently (belt & braces)
            cur.execute(
                """
                SELECT count(*) FROM standings st
                JOIN league_seasons ls ON ls.id = st.league_season_id
                JOIN leagues l ON l.id = ls.league_id
                WHERE st.points <> 3 * st.won + st.drawn AND l.api_key = %s
                """,
                (league,),
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
