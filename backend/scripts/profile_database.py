"""Phase 4 / Step 1 - Database exploration and profiling.

Reads the Football Charts analytics database (PostgreSQL) *read-only* and
produces a reproducible profiling report under data/analysis/:

    database_profile.json     # machine-readable: everything the profiler knows
    database_profile.md       # human-readable summary split into
                              #   1. Observed data
                              #   2. Calculated statistics
                              #   3. Warnings & anomalies

The profiler never writes to the database: every statement is a SELECT and the
transaction is rolled back before the connection closes. The raw dataset under
data/raw/ is likewise untouched.

All statistics are computed from the matches / standings / team_seasons tables
(PostgreSQL), not from the raw JSON. Reports are reproducible: every number is
recomputed on each run and the CLI configuration is recorded verbatim in the
report, so a report can be re-generated at any time and diffed.

Usage:
    python backend/scripts/profile_database.py
    python backend/scripts/profile_database.py --league premier
    python backend/scripts/profile_database.py --out-dir data/analysis \
        --score-threshold 9 --avg-goals-deviation 0.4
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import psycopg2.extras

# Make db_common resolvable whether run as a script or imported under
# scripts.profile_database in tests (same import-time path pattern as
# validate_raw_data.py).
sys.path.insert(0, str(Path(__file__).resolve().parent))

from db_common import (
    LEAGUE,
    VIEWS,
    get_conn,
    parse_season_years,
)
from analysis_common import rel_to_root

VERSION = "1.0.0"
SCRIPT_NAME = "backend/scripts/profile_database.py"

ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_OUT_DIR = ROOT_DIR / "data" / "analysis"
REPORT_STEM = "database_profile"

EXPECTED_MATCHES_PER_SEASON = 380
EXPECTED_TEAMS_PER_SEASON = 20
EXPECTED_STANDINGS_ROWS = 20

FIRST_GOAL_BUCKETS = [
    (1, 15), (16, 30), (31, 45),
    (46, 60), (61, 75), (76, 90), (91, 120),
]

# columns of `matches` that must never be NULL
REQUIRED_MATCH_FIELDS = [
    "match_date", "kickoff_time", "home_team_id", "away_team_id",
    "home_score", "away_score",
]

TABLES = [
    "leagues", "seasons", "league_seasons",
    "teams", "team_aliases", "team_seasons",
    "matches", "standings",
]


# ── configuration ────────────────────────────────────────────────────────────
def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="profile_database",
        description="Profile the Football Charts analytics database (read-only).",
    )
    parser.add_argument("--league", default=LEAGUE, help="league slug to profile (default: premier)")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR,
                        help="output directory for the report (default: data/analysis)")
    parser.add_argument("--score-threshold", type=int, default=8,
                        help="flag matches with >= N total goals (default: 8)")
    parser.add_argument("--avg-goals-deviation", type=float, default=0.35,
                        help="flag seasons whose avg goals differ from the overall avg by more than this")
    parser.add_argument("--goalless-deviation-pp", type=float, default=1.5,
                        help="flag seasons whose goalless share deviates by more than this many percentage points")
    parser.add_argument("--outcome-deviation-pp", type=float, default=4.0,
                        help="flag seasons whose H/D/A outcome share deviates by more than this many percentage points")
    parser.add_argument("--expected-matches-per-season", type=int, default=EXPECTED_MATCHES_PER_SEASON)
    parser.add_argument("--expected-teams-per-season", type=int, default=EXPECTED_TEAMS_PER_SEASON)
    parser.add_argument("--expected-standings-rows", type=int, default=EXPECTED_STANDINGS_ROWS)
    return parser.parse_args(argv)


def args_to_config(args: argparse.Namespace) -> dict:
    return {
        "league": args.league,
        "out_dir": rel_to_root(args.out_dir),
        "score_threshold": args.score_threshold,
        "avg_goals_deviation": args.avg_goals_deviation,
        "goalless_deviation_pp": args.goalless_deviation_pp,
        "outcome_deviation_pp": args.outcome_deviation_pp,
        "expected_matches_per_season": args.expected_matches_per_season,
        "expected_teams_per_season": args.expected_teams_per_season,
        "expected_standings_rows": args.expected_standings_rows,
    }


# ── pure helpers (unit-testable without a database) ──────────────────────────
def round_pct(count: int, total: int, ndigits: int = 1) -> float | None:
    """Percentage of count/total, rounded; None when total <= 0."""
    if total <= 0:
        return None
    return round(100.0 * count / total, ndigits)


def classify_outcome(home: int, away: int) -> str:
    if home > away:
        return "home"
    if home == away:
        return "draw"
    return "away"


def percentile(sorted_values: list[int], q: float) -> int | float | None:
    """Linear-interpolation percentile on a pre-sorted list (median-friendly)."""
    if not sorted_values:
        return None
    n = len(sorted_values)
    if n == 1:
        return sorted_values[0]
    pos = (n - 1) * q
    lo = int(pos)
    frac = pos - lo
    lo_val = sorted_values[lo]
    hi_val = sorted_values[min(lo + 1, n - 1)]
    return round(lo_val + frac * (hi_val - lo_val), 2)


def summarize_first_goal_times(times: list[int]) -> dict | None:
    """Summary stats for a list of first-goal minutes."""
    if not times:
        return None
    s = sorted(times)
    return {
        "n": len(s),
        "min": s[0],
        "max": s[-1],
        "mean": round(statistics.fmean(s), 2),
        "p25": percentile(s, 0.25),
        "p50": percentile(s, 0.50),
        "p75": percentile(s, 0.75),
    }


def bucket_first_goal_times(times: list[int], buckets=FIRST_GOAL_BUCKETS) -> dict:
    """Number of first goals per minute bucket."""
    return {
        f"{lo}-{hi}": sum(1 for t in times if lo <= t <= hi)
        for lo, hi in buckets
    }


def aggregate_match_stats(grouped: dict[str, list[tuple[int, int, int]]]) -> dict:
    """Aggregate (home, away, count) rows into outcome/goal statistics.

    Returns one stats dict per group key, mirroring the schema:
        n_matches, home_wins, draws, away_wins, *_pct,
        home_goals, away_goals, total_goals, avg_goals,
        avg_home_goals, avg_away_goals, home_goal_share,
        goalless, goalless_pct
    """
    result: dict[str, dict] = {}
    for key, rows in grouped.items():
        n = home_wins = draws = away_wins = 0
        home_goals = away_goals = goalless = 0
        for h, a, c in rows:
            n += c
            home_goals += h * c
            away_goals += a * c
            if h > a:
                home_wins += c
            elif h == a:
                draws += c
            else:
                away_wins += c
            if h == 0 and a == 0:
                goalless += c
        total_goals = home_goals + away_goals
        result[key] = {
            "n_matches": n,
            "home_wins": home_wins,
            "draws": draws,
            "away_wins": away_wins,
            "home_win_pct": round_pct(home_wins, n),
            "draw_pct": round_pct(draws, n),
            "away_win_pct": round_pct(away_wins, n),
            "home_goals": home_goals,
            "away_goals": away_goals,
            "total_goals": total_goals,
            "avg_goals": round(total_goals / n, 3) if n else None,
            "avg_home_goals": round(home_goals / n, 3) if n else None,
            "avg_away_goals": round(away_goals / n, 3) if n else None,
            "home_goal_share": round_pct(home_goals, total_goals),
            "goalless": goalless,
            "goalless_pct": round_pct(goalless, n),
        }
    return result


def top_scorelines(rows: list[tuple[int, int, int]], limit: int = 12) -> list[dict]:
    counter = Counter()
    for h, a, n in rows:
        counter[(h, a)] += n
    return [
        {"scoreline": f"{h}-{a}", "count": c}
        for (h, a), c in counter.most_common(limit)
    ]


def extreme_scorelines(rows: list[tuple[int, int, int]], threshold: int) -> list[dict]:
    hits = sorted(
        ((h + a, h, a, c) for h, a, c in rows if h + a >= threshold),
        reverse=True,
    )
    return [
        {"scoreline": f"{h}-{a}", "total_goals": total, "count": c}
        for total, h, a, c in hits
    ]


def season_sort_key(name: str) -> tuple:
    start, end = parse_season_years(name)
    return start or 0, end or 0, name


# ── query layer (SELECT-only) ────────────────────────────────────────────────
def table_counts(cur) -> dict[str, int]:
    out: dict[str, int] = {}
    for table in TABLES:
        cur.execute(f"SELECT count(*) FROM {table}")  # TABLES is a fixed whitelist
        out[table] = cur.fetchone()[0]
    return out


def leagues_with_data(cur) -> list[dict]:
    cur.execute(
        """
        SELECT l.api_key, l.name, l.country,
               count(DISTINCT ls.id) AS n_registered_seasons,
               count(DISTINCT m.api_id) AS n_matches
        FROM leagues l
        LEFT JOIN league_seasons ls ON ls.league_id = l.id
        LEFT JOIN matches m ON m.league_season_id = ls.id
        GROUP BY l.api_key, l.name, l.country
        ORDER BY l.api_key
        """
    )
    return [dict(r) for r in cur.fetchall()]


def registered_seasons(cur, league: str) -> dict:
    """Registry rows for the profiled league, with data-derived coverage."""
    cur.execute(
        """
        SELECT s.name AS season, ls.declared_by_api, ls.season_state,
               count(DISTINCT m.api_id) AS n_matches,
               count(DISTINCT ts.team_id) AS n_teams,
               min(m.match_date) AS min_date,
               max(m.match_date) AS max_date
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        LEFT JOIN matches m ON m.league_season_id = ls.id
        LEFT JOIN team_seasons ts ON ts.league_season_id = ls.id
        WHERE l.api_key = %s
        GROUP BY s.name, ls.declared_by_api, ls.season_state, s.start_year
        ORDER BY s.start_year, s.name
        """,
        (league,),
    )
    rows = []
    for r in cur.fetchall():
        d = dict(r)
        d["min_date"] = str(d["min_date"]) if d["min_date"] else None
        d["max_date"] = str(d["max_date"]) if d["max_date"] else None
        rows.append(d)
    has_data = [r for r in rows if r["n_matches"] > 0]
    no_data = [r["season"] for r in rows if r["n_matches"] == 0]
    return {
        "n_registered": len(rows),
        "n_with_data": len(has_data),
        "seasons_without_data": no_data,
        "seasons": rows,
    }


def duplicate_checks(cur) -> list[dict]:
    checks = [
        ("matches.api_id (natural PK)", "SELECT count(*) AS n, count(DISTINCT api_id) AS distinct_n FROM matches"),
        ("matches (league_season_id, game_index)",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, game_index)) AS distinct_n FROM matches"),
        ("matches same fixture on same date (league_season, home, away, match_date)",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, home_team_id, away_team_id, match_date)) AS distinct_n FROM matches"),
        ("team_seasons (league_season_id, team_id)",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, team_id)) AS distinct_n FROM team_seasons"),
        ("team_seasons api_name within a season",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, api_name)) AS distinct_n FROM team_seasons"),
        ("team_seasons api_slug within a season",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, api_slug)) AS distinct_n FROM team_seasons"),
        ("standings (league_season_id, team_id, view)",
         "SELECT count(*) AS n, count(DISTINCT (league_season_id, team_id, view)) AS distinct_n FROM standings"),
        ("team_aliases (form, value)",
         "SELECT count(*) AS n, count(DISTINCT (form, value)) AS distinct_n FROM team_aliases"),
        ("leagues.api_key", "SELECT count(*) AS n, count(DISTINCT api_key) AS distinct_n FROM leagues"),
        ("seasons.name", "SELECT count(*) AS n, count(DISTINCT name) AS distinct_n FROM seasons"),
        ("teams.canonical_name", "SELECT count(*) AS n, count(DISTINCT canonical_name) AS distinct_n FROM teams"),
    ]
    out = []
    for name, sql in checks:
        cur.execute(sql)
        n, distinct_n = cur.fetchone()
        out.append({"check": name, "rows": n, "distinct": distinct_n, "duplicates": n - distinct_n})
    return out


def null_counts(cur) -> dict:
    fields = [
        "match_date", "kickoff_time", "home_team_id", "away_team_id",
        "home_score", "away_score", "home_ht", "away_ht",
        "first_goal_time", "first_goal_time_extra",
    ]
    exprs = ",\n  ".join(
        f"count(*) FILTER (WHERE {f} IS NULL) AS null_{f}" for f in fields
    )
    cur.execute(f"SELECT count(*) AS total, {exprs} FROM matches")
    row = cur.fetchone()
    total = row["total"]
    out: dict = {"total": total, "fields": {}}
    for f in fields:
        n_null = row[f"null_{f}"]
        out["fields"][f] = {
            "n_null": n_null,
            "n_not_null": total - n_null,
            "null_pct": round_pct(n_null, total),
        }
    return out


def first_goal_consistency(cur) -> dict:
    cur.execute(
        """
        SELECT
            count(*) AS total,
            count(*) FILTER (WHERE (first_goal_time IS NULL)
                                 <> (home_score = 0 AND away_score = 0)) AS fgt_inconsistent,
            count(*) FILTER (WHERE (first_goal_time_extra IS NULL)
                                 <> (home_score = 0 AND away_score = 0)) AS fgte_inconsistent,
            count(*) FILTER (WHERE first_goal_time IS NOT NULL) AS n_with_fgt
        FROM matches
        """
    )
    return dict(cur.fetchone())


def value_ranges(cur) -> dict:
    cur.execute(
        """
        SELECT min(home_score) AS min_home, max(home_score) AS max_home,
               min(away_score) AS min_away, max(away_score) AS max_away,
               min(first_goal_time) AS min_fgt, max(first_goal_time) AS max_fgt,
               min(home_ht) AS min_ht_home, max(home_ht) AS max_ht_home,
               min(away_ht) AS min_ht_away, max(away_ht) AS max_ht_away
        FROM matches
        """
    )
    return {k: (int(v) if v is not None else None) for k, v in dict(cur.fetchone()).items()}


def scoreline_rows(cur, league: str) -> tuple[list[tuple[int, int, int]], dict, list[str]]:
    cur.execute(
        """
        SELECT s.name AS season, m.home_score AS h, m.away_score AS a, count(*) AS n
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        GROUP BY s.name, m.home_score, m.away_score
        """,
        (league,),
    )
    overall: Counter = Counter()
    by_season: dict[str, list[tuple[int, int, int]]] = {}
    for season, h, a, n in cur.fetchall():
        overall[(h, a)] += n
        by_season.setdefault(season, []).append((h, a, n))
    for rows in by_season.values():
        rows.sort()
    order = sorted(by_season, key=season_sort_key)
    return [(h, a, n) for (h, a), n in overall.items()], by_season, order


def first_goal_rows(cur, league: str) -> tuple[list[int], dict[str, list[int]], list[str]]:
    cur.execute(
        """
        SELECT s.name AS season, m.first_goal_time, count(*) AS n
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s AND m.first_goal_time IS NOT NULL
        GROUP BY s.name, m.first_goal_time
        ORDER BY s.name, m.first_goal_time
        """,
        (league,),
    )
    overall: list[int] = []
    by_season: dict[str, list[int]] = {}
    order: list[str] = []
    for season, fgt, n in cur.fetchall():
        overall.extend([fgt] * n)
        by_season.setdefault(season, []).extend([fgt] * n)
        if season not in order:
            order.append(season)
    order.sort(key=season_sort_key)
    return overall, by_season, order


def standings_coverage(cur, league: str) -> dict:
    cur.execute(
        """
        SELECT s.name AS season, st.view,
               count(*) AS n_rows,
               min(st.position) AS min_pos,
               max(st.position) AS max_pos,
               count(DISTINCT st.team_id) AS distinct_teams
        FROM standings st
        JOIN league_seasons ls ON ls.id = st.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        GROUP BY s.name, st.view, s.start_year
        ORDER BY s.start_year, st.view
        """,
        (league,),
    )
    rows = [dict(r) for r in cur.fetchall()]
    return {"n_pairs": len(rows), "n_rows": sum(r["n_rows"] for r in rows), "pairs": rows}


def weekday_distribution(cur, league: str) -> list[dict]:
    cur.execute(
        """
        SELECT EXTRACT(DOW FROM match_date)::int AS dow,
               to_char(match_date, 'Dy') AS label,
               count(*) AS n
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        GROUP BY dow, label
        ORDER BY dow
        """,
        (league,),
    )
    rows = [dict(r) for r in cur.fetchall()]
    total = sum(r["n"] for r in rows) or 1
    for r in rows:
        r["pct"] = round_pct(r["n"], total)
    return rows


def database_meta(cur) -> dict:
    cur.execute("SELECT current_database() AS dbname, version() AS version")
    row = cur.fetchone()
    return {
        "database_name": row["dbname"],
        "server_version": row["version"].split(" on ", 1)[0],
    }


# ── anomaly detection ─────────────────────────────────────────────────────────
def detect_anomalies(profile: dict, cfg: dict) -> list[dict]:
    """Rule-based warning detection over an assembled profile."""
    warnings: list[dict] = []
    exp_matches = cfg["expected_matches_per_season"]
    exp_teams = cfg["expected_teams_per_season"]
    exp_stand_rows = cfg["expected_standings_rows"]

    def warn(code: str, message: str, **details) -> None:
        warnings.append({"code": code, "severity": "warning", "message": message, "details": details or {}})

    observed = profile["observed"]
    calculated = profile["calculated"]

    for s in observed["league_seasons"]["seasons"]:
        if s["n_matches"] == 0:
            warn(
                "SEASON_REGISTERED_NO_DATA",
                f"Season {s['season']} is registered but has no match data "
                f"(declared_by_api={s['declared_by_api']}, state={s['season_state']})",
                season=s["season"],
            )
        if s["n_matches"] != exp_matches:
            warn(
                "MATCH_COUNT_UNEXPECTED",
                f"Season {s['season']} has {s['n_matches']} matches, expected {exp_matches}",
                season=s["season"], n_matches=s["n_matches"], expected=exp_matches,
            )
        if s["n_teams"] not in (0, exp_teams):
            warn(
                "TEAM_COUNT_UNEXPECTED",
                f"Season {s['season']} has {s['n_teams']} teams, expected {exp_teams}",
                season=s["season"], n_teams=s["n_teams"], expected=exp_teams,
            )
        if s["n_matches"] > 0 and s["season_state"] != "complete":
            warn(
                "SEASON_STATE_NOT_COMPLETE",
                f"Season {s['season']} has data but state is '{s['season_state']}'",
                season=s["season"], season_state=s["season_state"],
            )

    overall = calculated["overall"]
    for s in calculated["per_season"]:
        if overall["avg_goals"] is not None and s["avg_goals"] is not None:
            deviation = abs(s["avg_goals"] - overall["avg_goals"])
            if deviation > cfg["avg_goals_deviation"]:
                warn(
                    "SEASON_AVG_GOALS_OUTLIER",
                    f"Season {s['season']} avg goals {s['avg_goals']} vs overall {overall['avg_goals']} "
                    f"(deviation {deviation:.3f})",
                    season=s["season"], season_avg_goals=s["avg_goals"],
                    overall_avg_goals=overall["avg_goals"], deviation=round(deviation, 3),
                )
        if overall["goalless_pct"] is not None and s["goalless_pct"] is not None:
            deviation = abs(s["goalless_pct"] - overall["goalless_pct"])
            if deviation > cfg["goalless_deviation_pp"]:
                warn(
                    "GOALLESS_SHARE_OUTLIER",
                    f"Season {s['season']} goalless share {s['goalless_pct']}% vs overall {overall['goalless_pct']}% "
                    f"(deviation {deviation:.1f} pp)",
                    season=s["season"], season_goalless_pct=s["goalless_pct"],
                    overall_goalless_pct=overall["goalless_pct"], deviation_pp=round(deviation, 1),
                )
        for label, key in (("home", "home_win_pct"), ("draw", "draw_pct"), ("away", "away_win_pct")):
            ov = overall[key]
            if ov is not None and s[key] is not None and abs(s[key] - ov) > cfg["outcome_deviation_pp"]:
                warn(
                    "OUTCOME_SHARE_OUTLIER",
                    f"Season {s['season']} {label} outcome share {s[key]}% vs overall {ov}%",
                    season=s["season"], outcome=label, season_share=s[key], overall_share=ov,
                )

    extreme = calculated["extreme_scorelines"]
    if extreme:
        n = sum(e["count"] for e in extreme)
        warn(
            "HIGH_SCORING_MATCHES",
            f"{n} match(es) with >= {cfg['score_threshold']} total goals (extreme scorelines)",
            n_matches=n, threshold=cfg["score_threshold"],
            examples=extreme[:8],
        )

    for d in observed["duplicates"]:
        if d["duplicates"] > 0:
            warn(
                "DUPLICATE_ROWS",
                f"Duplicate rows detected in {d['check']} ({d['duplicates']} extra rows)",
                check=d["check"], rows=d["rows"], distinct=d["distinct"], duplicates=d["duplicates"],
            )

    for field, info in observed["null_counts"]["fields"].items():
        if field in REQUIRED_MATCH_FIELDS and info["n_null"] > 0:
            warn(
                "NULL_IN_REQUIRED_FIELD",
                f"{info['n_null']} NULL value(s) in matches.{field} (must never be NULL)",
                field=field, n_null=info["n_null"],
            )

    fc = observed["first_goal_consistency"]
    if fc["fgt_inconsistent"] or fc["fgte_inconsistent"]:
        warn(
            "FIRST_GOAL_NULL_INCONSISTENCY",
            f"first_goal_time/first_goal_time_extra NULL semantics broken "
            f"(fgt={fc['fgt_inconsistent']}, fgte={fc['fgte_inconsistent']} rows)",
            **fc,
        )

    for st in calculated["standings"]["pairs"]:
        if (
            st["n_rows"] != exp_stand_rows
            or st["min_pos"] != 1
            or st["max_pos"] != exp_stand_rows
            or st["distinct_teams"] != exp_stand_rows
        ):
            warn(
                "STANDINGS_INCOMPLETE",
                f"Standings {st['season']}/{st['view']} rows={st['n_rows']} "
                f"positions={st['min_pos']}..{st['max_pos']} teams={st['distinct_teams']}",
                season=st["season"], view=st["view"], n_rows=st["n_rows"],
                min_pos=st["min_pos"], max_pos=st["max_pos"], distinct_teams=st["distinct_teams"],
            )

    return warnings


# ── profile assembly ─────────────────────────────────────────────────────────
def build_profile(conn, cfg: dict) -> dict:
    profile = {
        "report_name": REPORT_STEM,
        "script": {"name": SCRIPT_NAME, "version": VERSION},
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "config": cfg,
        "meta": {"database": None},
        "observed": {
            "tables": None,
            "leagues": None,
            "league_seasons": None,
            "duplicates": None,
            "null_counts": None,
            "first_goal_consistency": None,
            "value_ranges": None,
        },
        "calculated": {
            "overall": None,
            "per_season": None,
            "first_goal": None,
            "standings": None,
            "weekday_distribution": None,
            "scorelines": None,
            "extreme_scorelines": None,
        },
        "warnings": [],
    }

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        profile["meta"]["database"] = database_meta(cur)
        profile["observed"]["tables"] = table_counts(cur)
        profile["observed"]["leagues"] = leagues_with_data(cur)
        profile["observed"]["league_seasons"] = registered_seasons(cur, cfg["league"])
        profile["observed"]["duplicates"] = duplicate_checks(cur)
        profile["observed"]["null_counts"] = null_counts(cur)
        profile["observed"]["first_goal_consistency"] = first_goal_consistency(cur)
        profile["observed"]["value_ranges"] = value_ranges(cur)

        overall_rows, per_season_rows, season_order = scoreline_rows(cur, cfg["league"])
        grouped = {"overall": overall_rows}
        grouped.update({s: per_season_rows[s] for s in season_order})
        match_stats = aggregate_match_stats(grouped)
        profile["calculated"]["overall"] = match_stats["overall"]
        profile["calculated"]["per_season"] = [
            {"season": s, **match_stats[s]} for s in season_order
        ]
        profile["calculated"]["scorelines"] = {"most_common": top_scorelines(overall_rows)}
        profile["calculated"]["extreme_scorelines"] = extreme_scorelines(
            overall_rows, cfg["score_threshold"]
        )

        fg_times, fg_by_season, fg_order = first_goal_rows(cur, cfg["league"])
        profile["calculated"]["first_goal"] = {
            "n_with_fgt": len(fg_times),
            "summary": summarize_first_goal_times(fg_times),
            "buckets": bucket_first_goal_times(fg_times),
            "per_season": {
                s: {
                    "n_with_fgt": len(fg_by_season[s]),
                    "summary": summarize_first_goal_times(fg_by_season[s]),
                    "buckets": bucket_first_goal_times(fg_by_season[s]),
                }
                for s in fg_order
            },
        }

        standings = standings_coverage(cur, cfg["league"])
        n_data_seasons = profile["observed"]["league_seasons"]["n_with_data"]
        standings["expected_pairs"] = n_data_seasons * len(VIEWS)
        standings["coverage_complete"] = (
            standings["n_pairs"] == standings["expected_pairs"]
        )
        profile["calculated"]["standings"] = standings

        profile["calculated"]["weekday_distribution"] = weekday_distribution(cur, cfg["league"])

    profile["warnings"] = detect_anomalies(profile, cfg)
    return profile


# ── report rendering ─────────────────────────────────────────────────────────
def fmt_pct(value: float | None, ndigits: int = 1) -> str:
    if value is None:
        return "-"
    return f"{value:.{ndigits}f}%"


def fmt_markdown_table(headers: list[str], rows: list[list]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def render_markdown(profile: dict) -> str:
    cfg = profile["config"]
    obs = profile["observed"]
    calc = profile["calculated"]
    db = profile["meta"]["database"]
    lines: list[str] = []
    add = lines.append

    add("# Football Charts Database Profile")
    add(f"- Report: `{profile['report_name']}`")
    add(f"- Generated: {profile['generated_at']}")
    add(f"- Script: `{profile['script']['name']}` v{profile['script']['version']}")
    add(f"- Database: `{db['database_name']}` ({db['server_version']})")
    add(f"- Scope: league `{cfg['league']}`")

    # ── 1. Observed ────────────────────────────────────────────────────
    add("")
    add("## 1. Observed data")

    add("")
    add("### 1.1 Table row counts")
    add(fmt_markdown_table(
        ["table", "rows"],
        [[t, obs["tables"][t]] for t in TABLES],
    ))

    leagues = obs["leagues"]
    with_data = [l for l in leagues if l["n_matches"] > 0]
    add("")
    add("### 1.2 Leagues with data")
    add(f"- Catalog leagues: `{len(leagues)}`")
    add(f"- Leagues with match data: `{len(with_data)}`")
    if with_data:
        add(fmt_markdown_table(
            ["api_key", "name", "country", "registered_seasons", "matches"],
            [[l["api_key"], l["name"], l["country"], l["n_registered_seasons"], l["n_matches"]]
             for l in with_data],
        ))
    else:
        add("  none")

    reg = obs["league_seasons"]
    add("")
    add("### 1.3 Registered seasons vs seasons with data")
    add(f"- Registered league_seasons for `{cfg['league']}`: `{reg['n_registered']}`")
    add(f"- With match data: `{reg['n_with_data']}`")
    add(f"- Registered but no data: `{reg['seasons_without_data'] or 'none'}`")
    add("")
    add(fmt_markdown_table(
        ["season", "declared_by_api", "state", "matches", "teams", "first match", "last match"],
        [
            [
                s["season"], s["declared_by_api"], s["season_state"],
                s["n_matches"], s["n_teams"],
                s["min_date"] or "-", s["max_date"] or "-",
            ]
            for s in reg["seasons"]
        ],
    ))

    add("")
    add("### 1.4 Duplicate checks")
    dupes = [d for d in obs["duplicates"] if d["duplicates"] > 0]
    add(fmt_markdown_table(
        ["check", "rows", "distinct", "duplicates"],
        [[d["check"], d["rows"], d["distinct"], d["duplicates"]] for d in obs["duplicates"]],
    ))
    if dupes:
        add("  > **WARNING:** duplicates found, see section 3.")

    nc = obs["null_counts"]
    add("")
    add("### 1.5 NULL counts (matches, important fields)")
    add(f"- Total matches: `{nc['total']}`")
    add("")
    add(fmt_markdown_table(
        ["field", "n_null", "n_not_null", "null_pct"],
        [[f, v["n_null"], v["n_not_null"], fmt_pct(v["null_pct"])]
         for f, v in nc["fields"].items()],
    ))
    add("  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.")

    add("")
    add("### 1.6 Value ranges")
    vr = obs["value_ranges"]
    fgc = obs["first_goal_consistency"]
    add(fmt_markdown_table(
        ["metric", "min", "max"],
        [
            ["home_score", vr["min_home"], vr["max_home"]],
            ["away_score", vr["min_away"], vr["max_away"]],
            ["first_goal_time", vr["min_fgt"], vr["max_fgt"]],
            ["home_ht", vr["min_ht_home"], vr["max_ht_home"]],
            ["away_ht", vr["min_ht_away"], vr["max_ht_away"]],
        ],
    ))
    add(f"- first_goal_time NULL semantics consistent: `{fgc['fgt_inconsistent'] == 0 and fgc['fgte_inconsistent'] == 0}`")

    # ── 2. Calculated ──────────────────────────────────────────────────
    add("")
    add("## 2. Calculated statistics")
    ov = calc["overall"]
    add("")
    add("### 2.1 Outcome distribution (overall)")
    add(fmt_markdown_table(
        ["outcome", "count", "pct"],
        [
            ["Home", ov["home_wins"], fmt_pct(ov["home_win_pct"])],
            ["Draw", ov["draws"], fmt_pct(ov["draw_pct"])],
            ["Away", ov["away_wins"], fmt_pct(ov["away_win_pct"])],
            ["Total", ov["n_matches"], "100.0%"],
        ],
    ))

    add("")
    add("### 2.2 Goals")
    add(fmt_markdown_table(
        ["metric", "value"],
        [
            ["Total goals", ov["total_goals"]],
            ["Average goals per match", ov["avg_goals"]],
            ["Home goals", f"{ov['home_goals']} (avg {ov['avg_home_goals']})"],
            ["Away goals", f"{ov['away_goals']} (avg {ov['avg_away_goals']})"],
            ["Home goal share", fmt_pct(ov["home_goal_share"])],
            ["Goalless matches", f"{ov['goalless']} ({fmt_pct(ov['goalless_pct'])})"],
        ],
    ))

    add("")
    add("### 2.3 Per-season breakdown")
    add(fmt_markdown_table(
        ["season", "matches", "H%", "D%", "A%", "total goals", "avg goals",
         "home goals", "away goals", "goalless"],
        [
            [
                s["season"], s["n_matches"], fmt_pct(s["home_win_pct"]),
                fmt_pct(s["draw_pct"]), fmt_pct(s["away_win_pct"]),
                s["total_goals"], s["avg_goals"], s["home_goals"], s["away_goals"],
                f"{s['goalless']} ({fmt_pct(s['goalless_pct'])})",
            ]
            for s in calc["per_season"]
        ],
    ))

    fg = calc["first_goal"]
    add("")
    add("### 2.4 First-goal timing")
    add(f"- Matches with a recorded first-goal time: `{fg['n_with_fgt']}` "
        f"of `{ov['n_matches']}` ({fmt_pct(round_pct(fg['n_with_fgt'], ov['n_matches']))})")
    if fg["summary"]:
        add(fmt_markdown_table(
            ["metric", "value"],
            [
                ["First goals recorded", fg["summary"]["n"]],
                ["Min minute", fg["summary"]["min"]],
                ["Max minute", fg["summary"]["max"]],
                ["Mean minute", fg["summary"]["mean"]],
                ["Median (p50)", fg["summary"]["p50"]],
                ["p25", fg["summary"]["p25"]],
                ["p75", fg["summary"]["p75"]],
            ],
        ))
        add("")
        add("First-goal minute buckets (count):")
        add(fmt_markdown_table(
            ["bucket", "count"],
            [[b, c] for b, c in fg["buckets"].items()],
        ))

    st = calc["standings"]
    add("")
    add("### 2.5 Standings coverage")
    add(f"- (season, view) pairs present: `{st['n_pairs']}` of `{st['expected_pairs']}` expected")
    add(f"- Standings rows total: `{st['n_rows']}`")
    add(f"- Coverage complete: `{st['coverage_complete']}`")
    if st["pairs"]:
        add("")
        add(fmt_markdown_table(
            ["season", "view", "rows", "positions", "distinct teams"],
            [
                [
                    p["season"], p["view"], p["n_rows"],
                    f"{p['min_pos']}..{p['max_pos']}", p["distinct_teams"],
                ]
                for p in st["pairs"]
            ],
        ))

    add("")
    add("### 2.6 Scorelines")
    add("Most common full-time scorelines:")
    add(fmt_markdown_table(
        ["scoreline", "count"],
        [[s["scoreline"], s["count"]] for s in calc["scorelines"]["most_common"]],
    ))
    if calc["extreme_scorelines"]:
        add("")
        add(f"Extreme scorelines (>= {cfg['score_threshold']} total goals):")
        add(fmt_markdown_table(
            ["scoreline", "total goals", "count"],
            [[s["scoreline"], s["total_goals"], s["count"]]
             for s in calc["extreme_scorelines"]],
        ))

    add("")
    add("### 2.7 Match weekday distribution")
    add(fmt_markdown_table(
        ["weekday", "count", "pct"],
        [[w["label"], w["n"], fmt_pct(w["pct"])] for w in calc["weekday_distribution"]],
    ))

    # ── 3. Warnings ────────────────────────────────────────────────────
    add("")
    add("## 3. Warnings & anomalies")
    warnings = profile["warnings"]
    if not warnings:
        add("None.")
    else:
        add(fmt_markdown_table(
            ["#", "code", "message"],
            [[i + 1, w["code"], w["message"]] for i, w in enumerate(warnings)],
        ))
        for i, w in enumerate(warnings, 1):
            if w["details"]:
                add(f"- `{i}.` `{w['code']}` details: `{json.dumps(w['details'], ensure_ascii=False)}`")

    add("")
    add("---")
    add("*All statistics are computed from PostgreSQL tables (read-only). "
       "Run with `python backend/scripts/profile_database.py` to regenerate.*")
    return "\n".join(lines)


def render_json(profile: dict) -> str:
    return json.dumps(profile, indent=2, ensure_ascii=False, default=str)


# ── entry point ──────────────────────────────────────────────────────────────
def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    cfg = args_to_config(args)

    conn = get_conn()
    try:
        t0 = time.time()
        profile = build_profile(conn, cfg)
        conn.rollback()
        elapsed = time.time() - t0
    finally:
        conn.close()

    out_dir = Path(cfg["out_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"{REPORT_STEM}.json"
    md_path = out_dir / f"{REPORT_STEM}.md"
    json_path.write_text(render_json(profile) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(profile) + "\n", encoding="utf-8")

    ov = profile["calculated"]["overall"]
    print(f"profile {cfg['league']}: {ov['n_matches']} matches, "
          f"{ov['total_goals']} goals (avg {ov['avg_goals']}), "
          f"{ov['goalless']} goalless, "
          f"{len(profile['warnings'])} warning(s) — wrote {json_path} and {md_path} "
          f"in {elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
