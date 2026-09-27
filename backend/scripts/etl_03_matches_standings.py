"""Step 04 - Matches + Standings load.

Applies sql/04_matches_standings.sql (federates /results/ and /table/), then:

  matches  <-  {league}/{season}/results.json         (parsed score/ht, verbatim minutes)
  standings <- {league}/{season}/table_{view}.json    (core analytic columns + metrics JSONB)

first_goal_time_extra is stored with its validated semantics: NULL when the
match is goalless (no first goal exists), an integer >= 0 otherwise (0 = first
goal in normal time). No NULL->0 conversion.

Re-running refreshes rows: the matches upsert is DO UPDATE (matching the other
five), so a corrected upstream result replaces the stale one. Cancelled and
awarded matches are skipped before insert, so a match that *becomes* one is
neither updated nor removed - the schema has no status column to represent it.
That is a pre-existing gap, not a consequence of the upsert.

Usage:
    python backend/scripts/etl_03_matches_standings.py
    python backend/scripts/etl_03_matches_standings.py --league spain1
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, time as dtime

import psycopg2.extras

from db_common import (
    HT_ABSENT_MARKERS,
    LEAGUE,
    RAW_DIR,
    SENTINEL_KICKOFF,
    VIEWS,
    apply_sql,
    collected_seasons,
    get_conn,
    load_json,
    raw_file,
    score_status,
    split_score,
)

SKIP_DIR = RAW_DIR.parent / "validation" / "skipped_matches"

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


def league_season_lookup(cur, league: str) -> dict[str, int]:
    """Map season name -> league_seasons.id for the current league."""
    cur.execute(
        """
        SELECT s.name, ls.id
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        WHERE ls.league_id = (SELECT id FROM leagues WHERE api_key = %s)
        """,
        (league,),
    )
    return {name: lsid for name, lsid in cur.fetchall()}


def team_lookup(cur, league_season_id: int) -> dict[str, int]:
    """Map api_name -> team_id within one league season."""
    cur.execute(
        "SELECT api_name, team_id FROM team_seasons WHERE league_season_id = %s",
        (league_season_id,),
    )
    return {name: tid for name, tid in cur.fetchall()}


def load_matches(cur, league_season_id: int, season: str, league: str) -> tuple[int, list[dict], list[dict]]:
    path = raw_file(season, "results.json", league)
    results_json = load_json(path)
    team_ids = team_lookup(cur, league_season_id)

    n = 0
    skips: list[dict] = []
    time_unknown: list[dict] = []
    for m in results_json["matches"]:
        home_name = m["homeTeam"]
        away_name = m["awayTeam"]
        if home_name not in team_ids or away_name not in team_ids:
            raise KeyError(
                f"match {m['id']}: team not in {season} membership: {home_name}/{away_name}"
            )
        status = score_status(m.get("score"))
        if status != "playable":
            skips.append(
                {
                    "match_id": m.get("id"),
                    "league": league,
                    "season": season,
                    "score": m.get("score"),
                    "reason": (
                        "cancelled/awarded"
                        if status == "unplayed"
                        else "unparseable score"
                    ),
                }
            )
            continue
        ft = split_score(m["score"])
        raw_ht = m.get("ht_result")
        ht = None
        if raw_ht is not None and str(raw_ht).strip().lower() not in HT_ABSENT_MARKERS:
            ht = split_score(raw_ht)
            if ht is None:
                raise ValueError(f"match {m['id']}: unparseable ht_result {raw_ht!r}")

        raw_time = m.get("time")
        if isinstance(raw_time, str) and raw_time:
            kickoff = dtime.fromisoformat(raw_time)
        else:
            kickoff = dtime.fromisoformat(SENTINEL_KICKOFF)
            time_unknown.append(
                {
                    "match_id": m.get("id"),
                    "league": league,
                    "season": season,
                }
            )
        cur.execute(
            """
            INSERT INTO matches (
                api_id, league_season_id, game_index,
                home_team_id, away_team_id, match_date, kickoff_time,
                home_score, away_score, home_ht, away_ht,
                first_goal_time, first_goal_time_extra
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (api_id) DO UPDATE SET
                league_season_id = EXCLUDED.league_season_id,
                game_index = EXCLUDED.game_index,
                home_team_id = EXCLUDED.home_team_id,
                away_team_id = EXCLUDED.away_team_id,
                match_date = EXCLUDED.match_date,
                kickoff_time = EXCLUDED.kickoff_time,
                home_score = EXCLUDED.home_score,
                away_score = EXCLUDED.away_score,
                home_ht = EXCLUDED.home_ht,
                away_ht = EXCLUDED.away_ht,
                first_goal_time = EXCLUDED.first_goal_time,
                first_goal_time_extra = EXCLUDED.first_goal_time_extra
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
    return n, skips, time_unknown


def load_standings(cur, league_season_id: int, season: str, league: str) -> int:
    team_ids = team_lookup(cur, league_season_id)

    total = 0
    for view in VIEWS:
        path = raw_file(season, f"table_{view}.json", league)
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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="etl_03_matches_standings",
        description="Load matches and standings for one league.",
    )
    parser.add_argument("--league", default=LEAGUE, help="league slug (default: premier)")
    return parser.parse_args(argv)


def write_skip_report(league: str, skips: list[dict], time_unknown: list[dict]) -> None:
    path = SKIP_DIR / f"{league}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "league": league,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "n_skipped": len(skips),
        "skipped": skips,
        "n_kickoff_time_unknown": len(time_unknown),
        "kickoff_time_unknown": time_unknown,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    if skips:
        print(
            f"[04] {len(skips)} unplayed/unparseable match(es) skipped; "
            f"report at {path}"
        )
    if time_unknown:
        print(
            f"[04] {len(time_unknown)} match(es) loaded with sentinel kickoff time "
            f"(00:00:00); record at {path}"
        )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    league = args.league
    seasons = collected_seasons(league)

    conn = get_conn()
    try:
        apply_sql(conn, "04_matches_standings.sql")
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            ls_ids = league_season_lookup(cur, league)
            n_matches = 0
            n_standings = 0
            skips: list[dict] = []
            time_unknown: list[dict] = []
            for season in seasons:
                if season not in ls_ids:
                    print(f"[04] WARN: no registry pair for {season}; skipping")
                    continue
                ls_id = ls_ids[season]
                m, season_skips, season_time_unknown = load_matches(
                    cur, ls_id, season, league
                )
                skips += season_skips
                time_unknown += season_time_unknown
                s = load_standings(cur, ls_id, season, league)
                print(f"[04] {season}: +{m} matches, +{s} standings rows")
                n_matches += m
                n_standings += s
            print(f"[04] total loaded: {n_matches} matches, {n_standings} standings rows")
        conn.commit()
        write_skip_report(league, skips, time_unknown)
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())