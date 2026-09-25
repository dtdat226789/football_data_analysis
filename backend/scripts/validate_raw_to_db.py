"""Step 05b - Raw-to-database field-level reconciliation.

Reads the byte-preserved raw dataset under data/raw/ (produced by
collect_raw_data.py) and, field-by-field, compares it against the rows the
ETL pipeline loaded into PostgreSQL:

  registry   leagues.json   -> leagues / league_seasons
                               (declared_by_api, season_state)
  identity   teams.json     -> team_seasons
                               (api_name, api_slug, logo_url, slug-alias -> team)
  matches    results.json   -> matches
                               (game_index, teams, date, time, score, ht,
                                first_goal_time, first_goal_time_extra)
  standings  table_*.json   -> standings
                               (position, played, W/D/L, GF/GA/GD, points, metrics)

Unlike validate_db.py (count parity + derived invariants), every check here is
a per-field value comparison between the raw source of truth and the loaded
row, so a silent mis-mapping during ETL (swapped score, wrong team, datetime
drift, metrics drift ...) is caught directly.

Read-only: all DB access runs inside a transaction that is rolled back (no DML).

Produced reports (mirroring validate_raw_data.py):
    data/validation/raw_to_db_report.json   # machine-readable
    data/validation/raw_to_db_report.md     # human-readable

Exit code is 0 only when there are no ERROR-level findings.

Usage:
    python backend/scripts/validate_raw_to_db.py
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import psycopg2.extras

# Make db_common resolvable whether run as a script or imported under
# scripts.validate_raw_to_db in tests (same import-time path pattern as
# validate_raw_data.py / profile_database.py).
sys.path.insert(0, str(Path(__file__).resolve().parent))

from db_common import (
    collected_seasons,
    LEAGUE,
    RAW_DIR,
    SENTINEL_KICKOFF,
    VIEWS,
    get_conn,
    load_json,
    normalize_season_state,
    score_status,
    split_score,
)

VALIDATION_DIR = RAW_DIR.parent / "validation"
REPORT_JSON = VALIDATION_DIR / "raw_to_db_report.json"
REPORT_MD = VALIDATION_DIR / "raw_to_db_report.md"

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
CORE_STANDING_FIELDS = [
    "position",
    "played",
    "won",
    "drawn",
    "lost",
    "goals_for",
    "goals_against",
    "goal_difference",
    "points",
]

SEVERITY_ERROR = "ERROR"
SEVERITY_WARNING = "WARNING"
SEVERITY_PASS = "PASS"


def raw_url(league: str, season: str | None, name: str) -> Path:
    if season is None:
        return RAW_DIR / league / name
    return RAW_DIR / league / season / name


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(RAW_DIR.parent))
    except ValueError:
        return str(p)


def add_issue(
    issues: list[dict],
    category: str,
    code: str,
    severity: str,
    message: str,
    *,
    league: str | None = None,
    season: str | None = None,
    file: str | None = None,
    details: dict | None = None,
) -> None:
    issues.append(
        {
            "category": category,
            "code": code,
            "severity": severity,
            "league": league,
            "season": season,
            "file": file,
            "message": message,
            "details": details or {},
        }
    )


def category_status(issues: list[dict], category: str) -> str:
    if any(i["category"] == category and i["severity"] == SEVERITY_ERROR for i in issues):
        return SEVERITY_ERROR
    if any(i["category"] == category and i["severity"] == SEVERITY_WARNING for i in issues):
        return SEVERITY_WARNING
    return SEVERITY_PASS


# ── registry ──────────────────────────────────────────────────────────────────
def reconcile_registry(
    issues: list[dict],
    league: str,
    raw_leagues: dict,
    db_registry: dict[str, dict],
    results_states: dict[str, str],
    results_summaries: dict[str, dict],
) -> dict:
    """league_seasons must mirror /leagues/ declaration and results.json state."""
    n_compared = 0
    entry = next(
        (e for e in raw_leagues.get("leagues", []) if isinstance(e, dict) and e.get("league") == league),
        None,
    )
    if entry is None:
        add_issue(
            issues, "registry", "LEAGUE_ENTRY_MISSING", SEVERITY_ERROR,
            f"No entry for league '{league}' in /leagues/ response",
            league=league, file="leagues.json",
        )
        return {"n_compared": 0}

    raw_declared = set(entry.get("seasons", []) or [])
    for name, row in db_registry.items():
        n_compared += 1
        expected = name in raw_declared
        if row.get("declared_by_api") != expected:
            add_issue(
                issues, "registry", "DECLARED_BY_API_MISMATCH", SEVERITY_ERROR,
                f"league_seasons.declared_by_api={row.get('declared_by_api')} but '/leagues/' "
                f"declares season {name} = {expected}",
                league=league, season=name, file="leagues.json",
                details={"db": row.get("declared_by_api"), "raw": expected},
            )
    for season, raw_state in results_states.items():
        row = db_registry.get(season)
        if row is None:
            add_issue(
                issues, "registry", "SEASON_NOT_REGISTERED", SEVERITY_ERROR,
                f"No league_seasons row for collected season '{season}'",
                league=league, season=season, file=f"{season}/results.json",
                details=results_summaries.get(season, {}),
            )
            continue
        n_compared += 1
        if row.get("season_state") != normalize_season_state(raw_state):
            add_issue(
                issues, "registry", "SEASON_STATE_MISMATCH", SEVERITY_ERROR,
                f"league_seasons.season_state={row.get('season_state')} but results.json "
                f"says '{raw_state}'",
                league=league, season=season, file=f"{season}/results.json",
                details={"db": row.get("season_state"), "raw": raw_state},
            )
    return {"n_compared": n_compared}


# ── identity ──────────────────────────────────────────────────────────────────
def reconcile_teams(
    issues: list[dict],
    league: str,
    season: str,
    raw: dict,
    db: dict[tuple[str, str], dict],
    aliases: dict[tuple[str, str], int],
) -> dict:
    """teams.json must match team_seasons (slug, logo) and the slug alias mapping."""
    n_compared = 0
    raw_names: set[str] = set()
    for t in raw.get("teams", []):
        if not isinstance(t, dict):
            continue
        name, slug = t.get("team"), t.get("slug")
        raw_names.add(name)
        row = db.get((season, name))
        if row is None:
            add_issue(
                issues, "identity", "TEAM_NOT_IN_DB", SEVERITY_ERROR,
                f"Team '{name}' in teams.json has no team_seasons row",
                league=league, season=season, file=f"{season}/teams.json",
                details={"team": name},
            )
            continue
        n_compared += 1
        if row.get("api_slug") != slug:
            add_issue(
                issues, "identity", "SLUG_MISMATCH", SEVERITY_ERROR,
                f"api_slug '{row.get('api_slug')}' != raw slug '{slug}' for '{name}'",
                league=league, season=season, file=f"{season}/teams.json",
                details={"team": name, "db": row.get("api_slug"), "raw": slug},
            )
        raw_logo = t.get("logo_url") or None
        db_logo = row.get("logo_url") or None
        if raw_logo != db_logo:
            add_issue(
                issues, "identity", "LOGO_MISMATCH", SEVERITY_WARNING,
                f"logo_url differs for '{name}'",
                league=league, season=season, file=f"{season}/teams.json",
                details={"team": name, "db": db_logo, "raw": raw_logo},
            )
        alias_tid = aliases.get(("slug", slug))
        if alias_tid is None:
            add_issue(
                issues, "identity", "SLUG_ALIAS_MISSING", SEVERITY_ERROR,
                f"No slug alias seeded for '{slug}' ({name})",
                league=league, season=season, file=f"{season}/teams.json",
                details={"team": name, "slug": slug},
            )
        elif alias_tid != row.get("team_id"):
            add_issue(
                issues, "identity", "ALIAS_TEAM_MISMATCH", SEVERITY_ERROR,
                f"slug '{slug}' alias resolves to team {alias_tid} but team_seasons "
                f"binds it to team {row.get('team_id')}",
                league=league, season=season, file=f"{season}/teams.json",
                details={"team": name, "alias_team": alias_tid, "team_seasons_team": row.get("team_id")},
            )
    for (s, name) in db:
        if s == season and name not in raw_names:
            add_issue(
                issues, "identity", "UNUSED_TEAM_IN_DB", SEVERITY_ERROR,
                f"team_seasons has '{name}' which teams.json does not list",
                league=league, season=season,
                details={"team": name},
            )
    return {"n_compared": n_compared}


# ── matches ───────────────────────────────────────────────────────────────────
def reconcile_matches(
    issues: list[dict],
    league: str,
    season: str,
    raw: dict,
    db: dict[int, dict],
    team_ids: dict[tuple[str, str], int],
) -> dict:
    """Every playable raw match must be reproduced exactly in the matches table.

    Cancelled/awarded ('CAN.'/'AWA.') and unparseable raw matches are skipped by
    the ETL and logged to data/validation/skipped_matches/, so they are ignored
    here (and never reported as MATCH_NOT_IN_DB).
    """
    n_compared = 0
    raw_ids: set[int] = set()
    for m in raw.get("matches", []):
        if not isinstance(m, dict):
            continue
        if score_status(m.get("score")) != "playable":
            continue
        mid = m.get("id")
        raw_ids.add(mid)
        row = db.get(mid)
        if row is None:
            add_issue(
                issues, "matches", "MATCH_NOT_IN_DB", SEVERITY_ERROR,
                f"Match {mid} in results.json is absent from the matches table",
                league=league, season=season, file=f"{season}/results.json",
                details={"match_id": mid},
            )
            continue
        n_compared += 1
        mismatches: list[tuple[str, object, object]] = []
        ft = split_score(m.get("score"))
        ht = split_score(m.get("ht_result"))
        if row.get("season") != season:
            mismatches.append(("season", row.get("season"), season))
        for field, raw_val in (
            ("game_index", m.get("game_index")),
            ("first_goal_time", m.get("first_goal_time")),
            ("first_goal_time_extra", m.get("first_goal_time_extra")),
        ):
            if row.get(field) != raw_val:
                mismatches.append((field, row.get(field), raw_val))
        if ft and row.get("home_score") != ft[0]:
            mismatches.append(("home_score", row.get("home_score"), ft[0]))
        if ft and row.get("away_score") != ft[1]:
            mismatches.append(("away_score", row.get("away_score"), ft[1]))
        db_ht = (row.get("home_ht"), row.get("away_ht"))
        raw_ht = ht if ht is not None else (None, None)
        if db_ht != raw_ht:
            mismatches.append(("ht", list(db_ht), list(raw_ht)))
        if row.get("match_date") is not None and row["match_date"].isoformat() != m.get("date"):
            mismatches.append(("date", row["match_date"].isoformat(), m.get("date")))
        raw_time = m.get("time")
        if row.get("kickoff_time") is not None:
            db_time = row["kickoff_time"].strftime("%H:%M:%S")
            if raw_time is None:
                # etl_03 stores a 00:00:00 sentinel when the raw kickoff time is absent
                if db_time != SENTINEL_KICKOFF:
                    mismatches.append(("time", db_time, raw_time))
            elif db_time != raw_time:
                mismatches.append(("time", db_time, raw_time))
        home_tid = team_ids.get((season, m.get("homeTeam")))
        away_tid = team_ids.get((season, m.get("awayTeam")))
        if home_tid is None or away_tid is None:
            add_issue(
                issues, "matches", "TEAM_MEMBERSHIP_MISSING", SEVERITY_ERROR,
                f"Match {mid}: home/away team not in {season} team_seasons",
                league=league, season=season, file=f"{season}/results.json",
                details={"match_id": mid, "home": m.get("homeTeam"), "away": m.get("awayTeam")},
            )
        else:
            if row.get("home_team_id") != home_tid:
                mismatches.append(("home_team_id", row.get("home_team_id"), home_tid))
            if row.get("away_team_id") != away_tid:
                mismatches.append(("away_team_id", row.get("away_team_id"), away_tid))
        if mismatches:
            add_issue(
                issues, "matches", "MATCH_FIELD_MISMATCH", SEVERITY_ERROR,
                f"Match {mid} differs from results.json in {len(mismatches)} field(s)",
                league=league, season=season, file=f"{season}/results.json",
                details={"match_id": mid, "mismatches": mismatches[:12]},
            )
    for aid, row in db.items():
        if row.get("season") == season and aid not in raw_ids:
            add_issue(
                issues, "matches", "EXTRA_MATCH_IN_DB", SEVERITY_ERROR,
                f"Match {aid} exists in the DB but not in {season} results.json",
                league=league, season=season,
                details={"match_id": aid},
            )
    return {"n_compared": n_compared}


# ── standings ─────────────────────────────────────────────────────────────────
def reconcile_standings(
    issues: list[dict],
    league: str,
    season: str,
    view: str,
    raw: dict,
    db: dict[tuple[str, str, str], dict],
) -> dict:
    """table_{view}.json must match the standings table (core columns + metrics)."""
    n_compared = 0
    raw_names: set[str] = set()
    for row in raw.get("table", []):
        if not isinstance(row, dict):
            continue
        name = row.get("team")
        raw_names.add(name)
        db_row = db.get((season, view, name))
        if db_row is None:
            add_issue(
                issues, "standings", "STANDING_NOT_IN_DB", SEVERITY_ERROR,
                f"table_{view} row '{name}' is absent from the standings table",
                league=league, season=season, file=f"{season}/table_{view}.json",
                details={"team": name, "view": view},
            )
            continue
        n_compared += 1
        mismatches: list[tuple[str, object, object]] = []
        for field in CORE_STANDING_FIELDS:
            if row.get(field) != db_row.get(field):
                mismatches.append((field, db_row.get(field), row.get(field)))
        raw_metrics = {k: v for k, v in row.items() if k not in CORE_STANDING_KEYS}
        if db_row.get("metrics") != raw_metrics:
            mismatches.append(("metrics", db_row.get("metrics"), raw_metrics))
        if mismatches:
            add_issue(
                issues, "standings", "STANDING_FIELD_MISMATCH", SEVERITY_ERROR,
                f"table_{view} '{name}' differs from standings in {len(mismatches)} field(s)",
                league=league, season=season, file=f"{season}/table_{view}.json",
                details={"team": name, "view": view, "mismatches": mismatches[:12]},
            )
    for (s, v, name) in db:
        if (s, v) == (season, view) and name not in raw_names:
            add_issue(
                issues, "standings", "EXTRA_STANDING_IN_DB", SEVERITY_ERROR,
                f"standings has '{name}' under {season}/{view} but table_{view}.json does not",
                league=league, season=season,
                details={"team": name, "view": view},
            )
    return {"n_compared": n_compared}


# ── DB lookups ───────────────────────────────────────────────────────────────
def load_db_registry(cur, league: str) -> dict[str, dict]:
    cur.execute(
        """
        SELECT s.name, ls.declared_by_api, ls.season_state
        FROM league_seasons ls
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        """,
        (league,),
    )
    return {r["name"]: dict(r) for r in cur.fetchall()}


def load_db_teams(cur, league: str) -> dict[tuple[str, str], dict]:
    cur.execute(
        """
        SELECT s.name AS season, ts.api_name, ts.api_slug, ts.logo_url, ts.team_id
        FROM team_seasons ts
        JOIN league_seasons ls ON ls.id = ts.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        """,
        (league,),
    )
    return {(r["season"], r["api_name"]): dict(r) for r in cur.fetchall()}


def load_db_aliases(cur) -> dict[tuple[str, str], int]:
    cur.execute("SELECT form, value, team_id FROM team_aliases")
    return {(r["form"], r["value"]): r["team_id"] for r in cur.fetchall()}


def load_db_matches(cur, league: str) -> dict[int, dict]:
    cur.execute(
        """
        SELECT m.api_id, m.game_index, m.home_team_id, m.away_team_id,
               m.match_date, m.kickoff_time,
               m.home_score, m.away_score, m.home_ht, m.away_ht,
               m.first_goal_time, m.first_goal_time_extra,
               s.name AS season
        FROM matches m
        JOIN league_seasons ls ON ls.id = m.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        """,
        (league,),
    )
    return {r["api_id"]: dict(r) for r in cur.fetchall()}


def load_db_standings(cur, league: str) -> dict[tuple[str, str, str], dict]:
    cur.execute(
        """
        SELECT s.name AS season, st.view, ts.api_name,
               st.position, st.played, st.won, st.drawn, st.lost,
               st.goals_for, st.goals_against, st.goal_difference, st.points,
               st.metrics
        FROM standings st
        JOIN team_seasons ts
          ON ts.league_season_id = st.league_season_id AND ts.team_id = st.team_id
        JOIN league_seasons ls ON ls.id = st.league_season_id
        JOIN seasons s ON s.id = ls.season_id
        JOIN leagues l ON l.id = ls.league_id
        WHERE l.api_key = %s
        """,
        (league,),
    )
    return {(r["season"], r["view"], r["api_name"]): dict(r) for r in cur.fetchall()}


# ── report assembly ───────────────────────────────────────────────────────────
def build_report(league: str, seasons: list[str], views: list[str]) -> dict:
    issues: list[dict] = []

    leagues_path = raw_url(league, None, "leagues.json")
    if not leagues_path.exists():
        add_issue(
            issues, "file_completeness", "LEAGUES_MISSING", SEVERITY_ERROR,
            "leagues.json not collected",
            league=league, file="leagues.json",
        )
        raw_leagues: dict = {}
        results_states: dict[str, str] = {}
        results_summaries: dict[str, dict] = {}
    else:
        raw_leagues = load_json(leagues_path)
        results_states = {}
        results_summaries = {}
        for season in seasons:
            rpath = raw_url(league, season, "results.json")
            if rpath.exists():
                rj = load_json(rpath)
                results_states[season] = rj.get("season_state", "unknown")
                results_summaries[season] = {
                    "matches": len(rj.get("matches", [])),
                    "count": rj.get("count"),
                }

    db = {"teams": {}, "aliases": {}, "matches": {}, "standings": {}, "registry": {}}
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            db["registry"] = load_db_registry(cur, league)
            db["teams"] = load_db_teams(cur, league)
            db["aliases"] = load_db_aliases(cur)
            db["matches"] = load_db_matches(cur, league)
            db["standings"] = load_db_standings(cur, league)
        conn.rollback()
    finally:
        conn.close()

    counts = {"registry": 0, "identity": 0, "matches": 0, "standings": 0}

    counts["registry"] = reconcile_registry(
        issues, league, raw_leagues, db["registry"], results_states, results_summaries
    )["n_compared"]

    team_ids = {(s, name): row["team_id"] for (s, name), row in db["teams"].items()}
    for season in seasons:
        tpath = raw_url(league, season, "teams.json")
        if tpath.exists():
            counts["identity"] += reconcile_teams(
                issues, league, season, load_json(tpath), db["teams"], db["aliases"]
            )["n_compared"]
        rpath = raw_url(league, season, "results.json")
        if rpath.exists():
            counts["matches"] += reconcile_matches(
                issues, league, season, load_json(rpath), db["matches"], team_ids
            )["n_compared"]
        for view in views:
            s_path = raw_url(league, season, f"table_{view}.json")
            if s_path.exists():
                counts["standings"] += reconcile_standings(
                    issues, league, season, view, load_json(s_path), db["standings"]
                )["n_compared"]

    categories = ["registry", "identity", "matches", "standings"]
    if not raw_leagues:
        categories.append("file_completeness")
    checks = {
        c: {"status": category_status(issues, c), "compared": counts[c] if c in counts else None}
        for c in categories
    }

    errors = sum(1 for i in issues if i["severity"] == SEVERITY_ERROR)
    warnings = sum(1 for i in issues if i["severity"] == SEVERITY_WARNING)
    return {
        "report_name": "raw_to_db_report",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "scope": {"league": league, "seasons": seasons, "views": views},
        "overall": {
            "errors": errors,
            "warnings": warnings,
            "pass": 0,
            "compared": counts,
            "categories": categories,
        },
        "checks": checks,
        "issues": issues,
    }


def render_markdown(report: dict) -> str:
    lines = ["# Football Charts — Raw-to-Database Reconciliation Report", ""]
    lines.append(f"- Generated: {report['generated_at']}")
    scope = report["scope"]
    lines.append(
        f"- Scope: league `{scope['league']}`; seasons {', '.join(scope['seasons'])}; "
        f"table views {', '.join(scope['views'])}"
    )
    o = report["overall"]
    compared = o.get("compared", {})
    lines.append(
        f"- Overall: **{o['errors']} errors**, **{o['warnings']} warnings** | "
        f"compared={', '.join(f'{k}={v}' for k, v in compared.items())}"
    )
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    lines.append("| # | Severity | Code | Category | Season | Message |")
    lines.append("|---|----------|------|----------|--------|---------|")
    for n, issue in enumerate(report["issues"], 1):
        if issue["severity"] == SEVERITY_PASS:
            continue
        lines.append(
            f"| {n} | {issue['severity']} | `{issue['code']}` | {issue['category']} | "
            f"{issue['season'] or '-'} | {issue['message']} |"
        )
    lines.append("")
    lines.append("## Per-check summary")
    lines.append("")
    lines.append("| Check | Status | Compared |")
    lines.append("|-------|--------|----------|")
    for name, check in report["checks"].items():
        lines.append(f"| {name} | {check['status']} | {check.get('compared') or '-'} |")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "Reads the byte-preserved raw JSON files under `data/raw/` and compares them "
        "field-by-field against the rows the ETL pipeline loaded into PostgreSQL. "
        "Read-only (transaction is rolled back). Any value that differs between the "
        "raw source of truth and the loaded row is reported as an ERROR. Logo drift is "
        "reported as a WARNING."
    )
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="validate_raw_to_db",
        description="Field-level reconciliation between data/raw/ and PostgreSQL.",
    )
    parser.add_argument("--league", default=LEAGUE)
    parser.add_argument("--season", action="append", metavar="YYYY-YYYY",
                        help="season to check; repeatable, default: all collected seasons")
    parser.add_argument("--view", action="append", metavar="VIEW",
                        help="table view; repeatable, default: classic luck goals")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    seasons = args.season or collected_seasons(args.league)
    views = args.view or VIEWS
    report = build_report(args.league, seasons, views)
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_MD.write_text(render_markdown(report), encoding="utf-8")
    o = report["overall"]
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")
    print(f"compared={o.get('compared')} errors={o['errors']} warnings={o['warnings']}")
    return 0 if o["errors"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())