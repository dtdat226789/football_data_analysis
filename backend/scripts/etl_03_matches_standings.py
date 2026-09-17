"""Step 04 - Matches + Standings load.

Applies sql/04_matches_standings.sql (federates /results/ and /table/), then:

  matches  <-  {league}/{season}/results.json         (parsed score/ht, verbatim minutes)
  standings <- {league}/{season}/table_{view}.json    (core analytic columns + metrics JSONB)

first_goal_time_extra is stored with its validated semantics: NULL when the
match is goalless (no first goal exists), an integer >= 0 otherwise (0 = first
goal in normal time). No NULL->0 conversion.

Usage:
    python backend/scripts/etl_03_matches_standings.py
"""
from __future__ import annotations

import sys
from datetime import date, time as dtime

import psycopg2.extras

from db_common import (
    COLLECTED_SEASONS,
    LEAGUE,
    VIEWS,
    apply_sql,
    get_conn,
    load_json,
    parse_score,
    raw_file,
)

CORE_STANDING_KEYS = {
    "team",
    "position",
    "played",
    "won",
    "drawn",
    "lost",
    "goals_for",
    "goals_against",
    "goal_difference",
    "points",
}


def league_season_lookup(cur) -> dict[str, int]:
    """Map season name -> league_seasons.id for the current league."""
    cur.execute(
        """
        SELECT s.name, ls.id
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
        """,
        (LEAGUE,),
    )
    return {name: lsid for name, lsid in cur.fetchall()}


def team_lookup(cur, league_season_id: int) -> dict[str, int]:
    """Map api_name -> team_id within one league season."""
    cur.execute(
        "SELECT api_name, team_id FROM team_seasons WHERE league_season_id = %s",
        (league_season_id,),
    )
    return {name: tid for name, tid in cur.fetchall()}


def load_matches(cur, league_season_id: int, season: str) -> int:
    path = raw_file(season, "results.json")
    results_json = load_json(path)
    team_ids = team_lookup(cur, league_season_id)

    n = 0
    for m in results_json["matches"]:
        home_name = m["homeTeam"]
        away_name = m["awayTeam"]
        if home_name not in team_ids or away_name not in team_ids:
            raise KeyError(
                f"match {m['id']}: team not in {season} membership: {home_name}/{away_name}"
            )
        ft = parse_score(m["score"])
        ht = parse_score(m.get("ht_result"))
        if ft is None:
            raise ValueError(f"match {m['id']}: unparseable score {m['score']!r}")
        if m.get("ht_result") is not None and ht is None:
            raise ValueError(f"match {m['id']}: unparseable ht_result {m['ht_result']!r}")

        kickoff = dtime.fromisoformat(m["time"])
        cur.execute(
            """
            INSERT INTO matches (
                api_id, league_season_id, game_index,
                home_team_id, away_team_id, match_date, kickoff_time,
                home_score, away_score, home_ht, away_ht,
                first_goal_time, first_goal_time_extra
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (api_id) DO NOTHING
            """,
            (
                m["id"],
                league_season_id,
                m["game_index"],
                team_ids[home_name],
                team_ids[away_name],
                date.fromisoformat(m["date"]),
                kickoff,
                ft[0],
                ft[1],
                ht[0] if ht else None,
                ht[1] if ht else None,
                m.get("first_goal_time"),
                m.get("first_goal_time_extra"),
            ),
        )
        n += cur.rowcount
    return n


def load_standings(cur, league_season_id: int, season: str) -> int:
    team_ids = team_lookup(cur, league_season_id)

    total = 0
    for view in VIEWS:
        path = raw_file(season, f"table_{view}.json")
        table_json = load_json(path)
        for row in table_json["table"]:
            team_name = row["team"]
            if team_name not in team_ids:
                raise KeyError(f"standings row team {team_name!r} not in {season} membership")
            metrics = {
                k: v for k, v in row.items() if k not in CORE_STANDING_KEYS
            }
            cur.execute(
                """
                INSERT INTO standings (
                    league_season_id, team_id, view,
                    position, played, won, drawn, lost,
                    goals_for, goals_against, goal_difference, points,
                    metrics
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (league_season_id, team_id, view) DO UPDATE
                   SET position        = EXCLUDED.position,
                       played          = EXCLUDED.played,
                       won             = EXCLUDED.won,
                       drawn           = EXCLUDED.drawn,
                       lost            = EXCLUDED.lost,
                       goals_for       = EXCLUDED.goals_for,
                       goals_against   = EXCLUDED.goals_against,
                       goal_difference = EXCLUDED.goal_difference,
                       points          = EXCLUDED.points,
                       metrics         = EXCLUDED.metrics,
                       captured_at     = now()
                """,
                (
                    league_season_id,
                    team_ids[team_name],
                    view,
                    row["position"],
                    row["played"],
                    row["won"],
                    row["drawn"],
                    row["lost"],
                    row["goals_for"],
                    row["goals_against"],
                    row["goal_difference"],
                    row["points"],
                    psycopg2.extras.Json(metrics),
                ),
            )
            total += cur.rowcount
    return total


def main() -> int:
    conn = get_conn()
    try:
        apply_sql(conn, "04_matches_standings.sql")
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            ls_ids = league_season_lookup(cur)
            n_matches = 0
            n_standings = 0
            for season in COLLECTED_SEASONS:
                if season not in ls_ids:
                    print(f"[04] WARN: no registry pair for {season}; skipping")
                    continue
                ls_id = ls_ids[season]
                m = load_matches(cur, ls_id, season)
                s = load_standings(cur, ls_id, season)
                print(f"[04] {season}: +{m} matches, +{s} standings rows")
                n_matches += m
                n_standings += s
            print(f"[04] total loaded: {n_matches} matches, {n_standings} standings rows")
        conn.commit()
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())