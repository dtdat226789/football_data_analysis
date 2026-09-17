"""POC data-validation pipeline for the Football Charts raw dataset.

Reads the raw JSON responses collected under data/raw/ (by
scripts/collect_raw_data.py) and validates each league/season combination
without modifying the raw data and without transforming anything.

Produced report files:
    data/validation/poc_validation_report.json   # machine-readable
    data/validation/poc_validation_report.md     # human-readable

Every finding is classified PASS / WARNING / ERROR and, for warnings and
errors, records: category, code, severity, league, season, file, message,
relevant counts and example values.

The collector is documented in scripts/collect_raw_data.py; this module reuses
its scope constants (DEFAULT_LEAGUE, DEFAULT_SEASONS, DEFAULT_VIEWS) and its
raw output directory (OUTPUT_DIR).

Usage:
    python backend/scripts/validate_raw_data.py
    python backend/scripts/validate_raw_data.py --season 2020-2021
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime, time as dtime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))

from scripts.collect_raw_data import (  # noqa: E402
    DEFAULT_LEAGUE,
    DEFAULT_SEASONS,
    DEFAULT_VIEWS,
    OUTPUT_DIR,
)

VALIDATION_DIR = ROOT_DIR / "data" / "validation"
REPORT_JSON = VALIDATION_DIR / "poc_validation_report.json"
REPORT_MD = VALIDATION_DIR / "poc_validation_report.md"

EXPECTED_TEAMS_PER_SEASON = 20
EXPECTED_CORE_MATCH_FIELDS = [
    "id", "game_index", "date", "time",
    "homeTeam", "awayTeam", "score", "ht_result",
    "first_goal_time", "first_goal_time_extra", "goalless",
]
TEAMS_REQUIRED_FIELDS = ["team", "slug", "position", "points", "played", "logo_url"]
TABLE_CORE_FIELDS = [
    "team", "position", "played", "won", "drawn", "lost",
    "goals_for", "goals_against", "goal_difference", "points",
]

SEVERITY_ERROR = "ERROR"
SEVERITY_WARNING = "WARNING"
SEVERITY_PASS = "PASS"

ISSUES: list[dict] = []


# ── issue registry ────────────────────────────────────────────────────────────
def add_issue(
    category: str,
    code: str,
    severity: str,
    message: str,
    *,
    league: str | None = None,
    season: str | None = None,
    file: str | None = None,
    details: dict | None = None,
    examples: list | None = None,
) -> None:
    ISSUES.append(
        {
            "category": category,
            "code": code,
            "severity": severity,
            "league": league,
            "season": season,
            "file": file,
            "message": message,
            "details": details or {},
            "examples": examples or [],
        }
    )


def category_status(category: str) -> str:
    levels = ISSUES
    if any(i["category"] == category and i["severity"] == SEVERITY_ERROR for i in levels):
        return SEVERITY_ERROR
    if any(i["category"] == category and i["severity"] == SEVERITY_WARNING for i in levels):
        return SEVERITY_WARNING
    return SEVERITY_PASS


def http_file(league: str, season: str | None, endpoint: str) -> Path:
    if season is None:
        return OUTPUT_DIR / league / endpoint
    return OUTPUT_DIR / league / season / endpoint


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT_DIR))
    except ValueError:
        return str(p)


def load_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_bytes())
    except Exception as exc:
        add_issue(
            "response_structure",
            "FILE_UNREADABLE",
            SEVERITY_ERROR,
            f"File exists but is not valid JSON: {exc}",
            file=rel(path),
            details={"error": str(exc)},
        )
        return None
    return data


def fmt_list(items: list, limit: int = 8) -> str:
    if not items:
        return ""
    shown = items[:limit]
    s = ", ".join(str(x) for x in shown)
    if len(items) > limit:
        s += f", ... ({len(items) - limit} more)"
    return s


# ── 1. file completeness ──────────────────────────────────────────────────────
def check_files(league: str, seasons: list[str], views: list[str]) -> dict:
    expected: list[tuple[Path, str, str | None]] = [
        (http_file(league, None, "leagues.json"), "leagues.json", None)
    ]
    for season in seasons:
        expected.append((http_file(league, season, "teams.json"), "teams.json", season))
        expected.append((http_file(league, season, "results.json"), "results.json", season))
        for view in views:
            expected.append((http_file(league, season, f"table_{view}.json"), f"table_{view}.json", season))

    present, missing = [], []
    for path, endpoint, season in expected:
        if path.exists():
            present.append(rel(path))
        else:
            missing.append(rel(path))
            add_issue(
                "file_completeness",
                "FILE_MISSING",
                SEVERITY_ERROR,
                f"Expected file is missing: {endpoint}",
                league=league,
                season=season,
                file=rel(path),
            )
    return {
        "status": category_status("file_completeness"),
        "expected_count": len(expected),
        "present_count": len(present),
        "missing_files": missing,
    }


# ── 2. response structure ─────────────────────────────────────────────────────
def check_leagues_structure(league: str, seasons: list[str]) -> dict:
    path = http_file(league, None, "leagues.json")
    data = load_json(path)
    if data is None:
        return {"status": SEVERITY_ERROR, "league_entry": None}
    result: dict = {"status": SEVERITY_PASS, "declared_seasons": None}
    if not {"leagues", "count"}.issubset(data.keys()):
        add_issue(
            "response_structure",
            "LEAGUES_TOP_KEYS",
            SEVERITY_ERROR,
            f"Unexpected top-level keys: {sorted(data.keys())}",
            file=rel(path),
            details={"expected": ["leagues", "count"], "actual": sorted(data.keys())},
        )
        result["status"] = category_status("response_structure")
    leagues = data.get("leagues")
    if not isinstance(leagues, list):
        add_issue(
            "response_structure",
            "LEAGUES_NOT_LIST",
            SEVERITY_ERROR,
            "'leagues' is not a list",
            file=rel(path),
            details={"type": type(leagues).__name__},
        )
    entries = [e for e in leagues if isinstance(e, dict) and e.get("league") == league] if isinstance(leagues, list) else []
    if not entries:
        add_issue(
            "response_structure",
            "LEAGUE_ENTRY_MISSING",
            SEVERITY_ERROR,
            f"No entry for league '{league}' in /leagues/ response",
            file=rel(path),
        )
    else:
        declared = entries[0].get("seasons", [])
        result["declared_seasons"] = declared
        undeclared = [s for s in seasons if s not in declared]
        if undeclared:
            add_issue(
                "response_structure",
                "SEASON_NOT_DECLARED",
                SEVERITY_WARNING,
                "Historical seasons are fetched directly but not declared by /leagues/ (expected API behaviour: current + previous only)",
                league=league,
                file=rel(path),
                details={"declared_seasons": declared, "undeclared_seasons": undeclared},
            )
    if isinstance(data.get("count"), int) and isinstance(leagues, list) and data["count"] != len(leagues):
        add_issue(
            "response_structure",
            "LEAGUES_COUNT_MISMATCH",
            SEVERITY_WARNING,
            "/leagues/ count field does not match the number of league entries",
            file=rel(path),
            details={"count": data["count"], "n_entries": len(leagues)},
        )
    result["status"] = category_status("response_structure")
    return result


def check_seasonal_structure(league: str, seasons: list[str], views: list[str]) -> dict:
    for season in seasons:
        teams = load_json(http_file(league, season, "teams.json"))
        if teams:
            keys = set(teams.keys())
            for required, label in [("league", "teams"), ("season", "teams"), ("teams", "teams")]:
                if required not in keys:
                    add_issue(
                        "response_structure",
                        f"TEAMS_TOP_KEYS_{required.upper()}",
                        SEVERITY_ERROR,
                        f"Missing top-level '{required}' in teams response",
                        league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                        details={"actual_keys": sorted(keys)},
                    )
            if teams.get("league") != league:
                add_issue(
                    "response_structure",
                    "TEAMS_LEAGUE_MISMATCH",
                    SEVERITY_ERROR,
                    f"teams response 'league' is '{teams.get('league')}', expected '{league}'",
                    league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                )
            if teams.get("season") != season:
                add_issue(
                    "response_structure",
                    "TEAMS_SEASON_MISMATCH",
                    SEVERITY_ERROR,
                    f"teams response 'season' is '{teams.get('season')}', expected '{season}'",
                    league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                )
            if not isinstance(teams.get("teams"), list) or len(teams.get("teams", [])) == 0:
                add_issue(
                    "response_structure",
                    "TEAMS_EMPTY",
                    SEVERITY_ERROR,
                    "teams list is empty or not a list",
                    league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                )

        results = load_json(http_file(league, season, "results.json"))
        if results:
            keys = set(results.keys())
            for required in ["league", "season", "count", "matches"]:
                if required not in keys:
                    add_issue(
                        "response_structure",
                        "RESULTS_TOP_KEYS",
                        SEVERITY_ERROR,
                        f"Missing top-level '{required}' in results response",
                        league=league, season=season, file=rel(http_file(league, season, "results.json")),
                        details={"actual_keys": sorted(keys)},
                    )
            if results.get("league") != league:
                add_issue(
                    "response_structure",
                    "RESULTS_LEAGUE_MISMATCH", SEVERITY_ERROR,
                    f"results 'league' is '{results.get('league')}', expected '{league}'",
                    league=league, season=season, file=rel(http_file(league, season, "results.json")),
                )
            if results.get("season") != season:
                add_issue(
                    "response_structure",
                    "RESULTS_SEASON_MISMATCH", SEVERITY_ERROR,
                    f"results 'season' is '{results.get('season')}', expected '{season}'",
                    league=league, season=season, file=rel(http_file(league, season, "results.json")),
                )
            matches = results.get("matches")
            if isinstance(matches, list) and results.get("count") != len(matches):
                add_issue(
                    "response_structure",
                    "RESULTS_COUNT_MISMATCH",
                    SEVERITY_ERROR,
                    "results 'count' does not match len(matches)",
                    league=league, season=season, file=rel(http_file(league, season, "results.json")),
                    details={"count": results.get("count"), "len_matches": len(matches)},
                )

        for view in views:
            table = load_json(http_file(league, season, f"table_{view}.json"))
            if not table:
                continue
            keys = set(table.keys())
            if not {"league", "season", "view", "table"}.issubset(keys):
                add_issue(
                    "response_structure",
                    "TABLE_TOP_KEYS",
                    SEVERITY_ERROR,
                    f"Unexpected top-level keys in table_{view} response",
                    league=league, season=season, file=rel(http_file(league, season, f"table_{view}.json")),
                    details={"actual_keys": sorted(keys)},
                )
            if table.get("view") != view:
                add_issue(
                    "response_structure",
                    "TABLE_VIEW_MISMATCH",
                    SEVERITY_ERROR,
                    f"table response 'view' is '{table.get('view')}', expected '{view}'",
                    league=league, season=season, file=rel(http_file(league, season, f"table_{view}.json")),
                )
            if table.get("season") != season:
                add_issue(
                    "response_structure",
                    "TABLE_SEASON_MISMATCH",
                    SEVERITY_ERROR,
                    f"table response 'season' is '{table.get('season')}', expected '{season}'",
                    league=league, season=season, file=rel(http_file(league, season, f"table_{view}.json")),
                )
            if not isinstance(table.get("table"), list) or len(table.get("table", [])) == 0:
                add_issue(
                    "response_structure",
                    "TABLE_EMPTY",
                    SEVERITY_ERROR,
                    f"table_{view} list is empty or not a list",
                    league=league, season=season, file=rel(http_file(league, season, f"table_{view}.json")),
                )
    return {"status": category_status("response_structure")}


# ── 3. teams ──────────────────────────────────────────────────────────────────
def normalize_team_name(name: str) -> str:
    return " ".join(name.strip().lower().split())


def check_teams(league: str, seasons: list[str]) -> dict:
    per_season: dict = {}
    field_sets: list[set] = []
    for season in seasons:
        path = http_file(league, season, "teams.json")
        data = load_json(path)
        rec: dict = {"teams": None}
        if data is None or not isinstance(data.get("teams"), list):
            per_season[season] = rec
            continue
        teams = data["teams"]
        rec["n_teams"] = len(teams)
        if len(teams) != EXPECTED_TEAMS_PER_SEASON:
            add_issue(
                "teams", "TEAMS_COUNT",
                SEVERITY_WARNING if len(teams) > 0 else SEVERITY_ERROR,
                f"Team count is {len(teams)}, expected {EXPECTED_TEAMS_PER_SEASON}",
                league=league, season=season, file=rel(path),
                details={"expected": EXPECTED_TEAMS_PER_SEASON, "actual": len(teams)},
            )
        names = [t.get("team") for t in teams if isinstance(t, dict)]
        dupes = [n for n, c in Counter(n for n in names if n).items() if c > 1]
        if dupes:
            add_issue(
                "teams", "TEAMS_DUPLICATE_NAME", SEVERITY_ERROR,
                f"Duplicate team names: {dupes}",
                league=league, season=season, file=rel(path), examples=dupes,
            )
        for t in teams:
            if not isinstance(t, dict):
                add_issue("teams", "TEAMS_ROW_NOT_DICT", SEVERITY_ERROR, "A teams entry is not an object", league=league, season=season, file=rel(path))
                continue
            for field in TEAMS_REQUIRED_FIELDS:
                if field not in t:
                    add_issue(
                        "teams", "TEAMS_MISSING_FIELD", SEVERITY_ERROR,
                        f"Team '{t.get('team')}' missing field '{field}'",
                        league=league, season=season, file=rel(path),
                        details={"team": t.get("team"), "field": field},
                    )
            slug, name = t.get("slug"), t.get("team")
            if name and slug:
                expected_slug = "-".join(normalize_team_name(name).split())
                if slug != expected_slug:
                    add_issue(
                        "teams", "TEAMS_SLUG_MISMATCH", SEVERITY_WARNING,
                        f"Slug '{slug}' does not match normalized name '{expected_slug}'",
                        league=league, season=season, file=rel(path),
                        details={"team": name, "slug": slug, "expected_slug": expected_slug},
                    )
        positions = [t.get("position") for t in teams if isinstance(t, dict)]
        if positions and (sorted(positions) != list(range(1, len(positions) + 1))):
            add_issue(
                "teams", "TEAMS_POSITION_ISSUE", SEVERITY_ERROR,
                "Positions are not a unique 1..n sequence",
                league=league, season=season, file=rel(path),
                details={"positions": positions},
            )
        field_sets.append(set().union(*[set(t.keys()) for t in teams if isinstance(t, dict)]))
        per_season[season] = rec
    return {"status": category_status("teams"), "per_season": per_season, "field_sets": [sorted(s) for s in field_sets]}


# ── 4. results ────────────────────────────────────────────────────────────────
def parse_score(raw: str) -> tuple[int, int] | None:
    if not isinstance(raw, str) or raw.count(":") != 1:
        return None
    a, b = raw.split(":")
    if not a.isdigit() or not b.isdigit():
        return None
    return int(a), int(b)


def season_window(season: str) -> tuple[date, date]:
    start_year, end_year = (int(x) for x in season.split("-"))
    return date(start_year, 6, 1), date(end_year, 8, 15)


def check_results(league: str, seasons: list[str]) -> dict:
    per_season: dict = {}
    field_sets: list[set] = []
    for season in seasons:
        path = http_file(league, season, "results.json")
        data = load_json(path)
        rec: dict = {"n_matches": None}
        per_season[season] = rec
        if data is None or not isinstance(data.get("matches"), list):
            continue
        matches = data["matches"]
        rec["n_matches"] = len(matches)
        if len(matches) == 0:
            add_issue("results", "RESULTS_EMPTY", SEVERITY_ERROR, "No matches", league=league, season=season, file=rel(path))
        expected = EXPECTED_TEAMS_PER_SEASON * (EXPECTED_TEAMS_PER_SEASON - 1)
        if len(matches) != expected:
            add_issue(
                "results", "RESULTS_COUNT_UNEXPECTED", SEVERITY_WARNING,
                f"Match count is {len(matches)}, expected {expected} for a complete {EXPECTED_TEAMS_PER_SEASON}-team double round-robin",
                league=league, season=season, file=rel(path),
                details={"expected": expected, "actual": len(matches)},
            )
        ids = [m.get("id") for m in matches]
        gi = [m.get("game_index") for m in matches]
        id_dups = [i for i, c in Counter(ids).items() if c > 1]
        gi_dups = [i for i, c in Counter(gi).items() if c > 1]
        if id_dups:
            add_issue("results", "RESULTS_DUPLICATE_ID", SEVERITY_ERROR, f"Duplicate match ids: {id_dups}", league=league, season=season, file=rel(path), examples=id_dups[:8])
        if gi_dups:
            add_issue("results", "RESULTS_DUPLICATE_GAME_INDEX", SEVERITY_ERROR, f"Duplicate game_index values: {gi_dups}", league=league, season=season, file=rel(path), examples=gi_dups[:8])
        if gi and (min(gi) != 1 or max(gi) != len(matches) or len(set(gi)) != len(gi)):
            add_issue(
                "results", "GAME_INDEX_RANGE", SEVERITY_WARNING,
                f"game_index is not exactly 1..{len(matches)}",
                league=league, season=season, file=rel(path),
                details={"min": min(gi), "max": max(gi), "n_unique": len(set(gi))},
            )
        window = season_window(season)
        dates = []
        for m in matches:
            if not isinstance(m, dict):
                add_issue("results", "RESULTS_ROW_NOT_DICT", SEVERITY_ERROR, "A match entry is not an object", league=league, season=season, file=rel(path))
                continue
            mid = m.get("id")
            for field in EXPECTED_CORE_MATCH_FIELDS:
                if field not in m:
                    add_issue("results", "RESULTS_MISSING_FIELD", SEVERITY_ERROR, f"Match {mid} missing field '{field}'", league=league, season=season, file=rel(path), details={"match_id": mid, "field": field})
            d = m.get("date")
            if d is not None:
                try:
                    dt = date.fromisoformat(d)
                    dates.append(d)
                    if not (window[0] <= dt <= window[1]):
                        add_issue("results", "RESULTS_DATE_OUT_OF_SEASON", SEVERITY_WARNING, f"Match {mid} date {d} outside season window", league=league, season=season, file=rel(path), details={"match_id": mid, "date": d, "window": [str(x) for x in window]})
                except ValueError:
                    add_issue("results", "RESULTS_INVALID_DATE", SEVERITY_ERROR, f"Match {mid} has invalid date '{d}'", league=league, season=season, file=rel(path), details={"match_id": mid, "date": d})
            t = m.get("time")
            if t is not None:
                try:
                    dtime.fromisoformat(t)
                    if not (len(t) == 8 and t[2] == ":" and t[5] == ":"):
                        raise ValueError("non HH:MM:SS")
                except ValueError:
                    add_issue("results", "RESULTS_INVALID_TIME", SEVERITY_ERROR, f"Match {mid} has invalid time '{t}'", league=league, season=season, file=rel(path), details={"match_id": mid, "time": t})
            score = parse_score(m.get("score"))
            if score is None:
                add_issue("results", "RESULTS_INVALID_SCORE", SEVERITY_ERROR, f"Match {mid} has invalid score '{m.get('score')}'", league=league, season=season, file=rel(path), details={"match_id": mid, "score": m.get("score")})
            ht = parse_score(m.get("ht_result"))
            if m.get("ht_result") is None:
                add_issue(
                    "results", "RESULTS_HT_NULL", SEVERITY_WARNING,
                    f"Match {mid} has a null half-time score",
                    league=league, season=season, file=rel(path), details={"match_id": mid},
                )
            elif ht is None:
                add_issue("results", "RESULTS_INVALID_HT", SEVERITY_ERROR, f"Match {mid} has invalid half-time score '{m.get('ht_result')}'", league=league, season=season, file=rel(path), details={"match_id": mid, "ht_result": m.get("ht_result")})
            else:
                if score and (ht[0] > score[0] or ht[1] > score[1]):
                    add_issue("results", "RESULTS_HT_FT_INCONSISTENT", SEVERITY_ERROR, f"Match {mid}: half-time {ht} exceeds full-time {score}", league=league, season=season, file=rel(path), details={"match_id": mid, "ht_result": m.get("ht_result"), "score": m.get("score")})
            goal = m.get("goalless")
            if goal is not None and not isinstance(goal, bool):
                add_issue("results", "RESULTS_GOALLESS_TYPE", SEVERITY_WARNING, f"Match {mid} 'goalless' is not boolean", league=league, season=season, file=rel(path), details={"match_id": mid, "goalless": goal})
            if goal and score and score != (0, 0):
                add_issue("results", "RESULTS_GOALLESS_SCORE", SEVERITY_ERROR, f"Match {mid} marked goalless but score is {m.get('score')}", league=league, season=season, file=rel(path), details={"match_id": mid, "score": m.get("score")})
            fgt = m.get("first_goal_time")
            fgte = m.get("first_goal_time_extra")
            ft_null = fgt is None
            if bool(goal) != ft_null and goal is not None:
                add_issue("results", "FIRST_GOAL_NULL_CONSISTENCY", SEVERITY_WARNING, f"Match {mid}: goalless={goal} but first_goal_time is {'null' if ft_null else fgt}", league=league, season=season, file=rel(path), details={"match_id": mid, "goalless": goal, "first_goal_time": fgt})
            if fgt is not None and not isinstance(fgt, int):
                add_issue("results", "FIRST_GOAL_TYPE", SEVERITY_ERROR, f"Match {mid} 'first_goal_time' is not an int", league=league, season=season, file=rel(path), details={"match_id": mid, "first_goal_time": fgt, "type": type(fgt).__name__})
            elif isinstance(fgt, int) and not (1 <= fgt <= 120):
                add_issue("results", "FIRST_GOAL_RANGE", SEVERITY_WARNING, f"Match {mid} 'first_goal_time' is {fgt}", league=league, season=season, file=rel(path), details={"match_id": mid, "first_goal_time": fgt})
            if fgte is not None:
                if not isinstance(fgte, int) or fgte < 0:
                    add_issue("results", "FIRST_GOAL_EXTRA_TYPE", SEVERITY_WARNING, f"Match {mid} 'first_goal_time_extra' is {fgte!r}", league=league, season=season, file=rel(path), details={"match_id": mid, "first_goal_time_extra": fgte})
            if m.get("homeTeam") == m.get("awayTeam") and m.get("homeTeam"):
                add_issue("results", "RESULTS_SELF_MATCH", SEVERITY_ERROR, f"Match {mid} is a self-match: {m.get('homeTeam')}", league=league, season=season, file=rel(path), details={"match_id": mid, "homeTeam": m.get("homeTeam")})
        if dates and dates != sorted(dates):
            add_issue("results", "RESULTS_NOT_CHRONOLOGICAL", SEVERITY_WARNING, "Matches are not in chronological date order", league=league, season=season, file=rel(path), details={"n_out_of_order": sum(1 for i in range(1, len(dates)) if dates[i] < dates[i - 1])})
        field_sets.append(set().union(*[set(m.keys()) for m in matches if isinstance(m, dict)]))
    return {"status": category_status("results"), "per_season": per_season, "field_sets": [sorted(s) for s in field_sets]}


# ── 5. team references (results vs teams) ─────────────────────────────────────
def check_team_references(league: str, seasons: list[str]) -> dict:
    for season in seasons:
        teams_data = load_json(http_file(league, season, "teams.json"))
        results_data = load_json(http_file(league, season, "results.json"))
        if not teams_data or not results_data:
            continue
        team_names = {t["team"] for t in teams_data.get("teams", []) if isinstance(t, dict)}
        result_names = set()
        for m in results_data.get("matches", []):
            if isinstance(m, dict):
                result_names.update([m.get("homeTeam"), m.get("awayTeam")])
        result_names.discard(None)
        missing = sorted(result_names - team_names)
        unused = sorted(team_names - result_names)
        if missing:
            add_issue(
                "team_references", "RESULTS_TEAM_MISSING_FROM_TEAMS", SEVERITY_WARNING,
                f"Teams in results absent from teams.json ({len(missing)}): {fmt_list(missing)}",
                league=league, season=season, file=rel(http_file(league, season, "results.json")),
                examples=missing[:8],
            )
        if unused:
            add_issue(
                "team_references", "TEAMS_UNUSED_IN_RESULTS", SEVERITY_WARNING,
                f"Teams in teams.json never appearing in results ({len(unused)}): {fmt_list(unused)}",
                league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                examples=unused[:8],
            )
    return {"status": category_status("team_references")}


# ── 6. match identity ─────────────────────────────────────────────────────────
def check_match_identity(league: str, seasons: list[str]) -> dict:
    season_ids: dict[str, set[int]] = {}
    per_season: dict = {}
    for season in seasons:
        data = load_json(http_file(league, season, "results.json"))
        rec: dict = {"n_matches": None}
        per_season[season] = rec
        if data is None or not isinstance(data.get("matches"), list):
            continue
        matches = data["matches"]
        ids = [m.get("id") for m in matches]
        rec["n_matches"] = len(matches)
        rec["id_min"] = min(ids) if ids else None
        rec["id_max"] = max(ids) if ids else None
        rec["game_index_min"] = min(m.get("game_index") for m in matches)
        rec["game_index_max"] = max(m.get("game_index") for m in matches)
        bad = [i for i in ids if not isinstance(i, int) or i <= 0]
        if bad:
            add_issue("match_identity", "MATCH_ID_NOT_POSITIVE_INT", SEVERITY_ERROR, "Non-positive / non-int match ids found", league=league, season=season, examples=[str(b) for b in bad[:8]])
        if len(set(ids)) != len(ids):
            add_issue("match_identity", "MATCH_ID_DUPLICATE", SEVERITY_ERROR, "Match ids not unique within season", league=league, season=season)
        season_ids[season] = set(ids)

    collisions = []
    season_list = list(season_ids)
    for i in range(len(season_list)):
        for j in range(i + 1, len(season_list)):
            hit = season_ids[season_list[i]] & season_ids[season_list[j]]
            if hit:
                collisions.append((season_list[i], season_list[j], sorted(hit)[:8]))
    if collisions:
        add_issue(
            "match_identity", "MATCH_ID_CROSS_SEASON_OVERLAP", SEVERITY_ERROR,
            "Match ids repeat across seasons; ids are not globally unique",
            league=league, details={"collisions": collisions},
        )
    # optional: cross-pull stability against the legacy flat 2025-2026 dump
    legacy = OUTPUT_DIR / "results.json"
    if legacy.exists():
        try:
            old = json.loads(legacy.read_bytes())
            if old.get("league") == league and old.get("season") == "2025-2026" and season_ids.get("2025-2026") is not None:
                old_ids = {m["id"] for m in old["matches"]}
                if old_ids != season_ids["2025-2026"]:
                    add_issue(
                        "match_identity", "MATCH_ID_PULL_DRIFT", SEVERITY_WARNING,
                        "Match ids differ from the earlier raw pull of 2025-2026",
                        league=league, season="2025-2026", file=rel(legacy),
                        details={"old_only": len(old_ids - season_ids["2025-2026"]), "new_only": len(season_ids["2025-2026"] - old_ids)},
                    )
        except Exception:
            pass
    return {"status": category_status("match_identity"), "per_season": per_season}


# ── 7. table ──────────────────────────────────────────────────────────────────
def check_tables(league: str, seasons: list[str], views: list[str]) -> dict:
    per_season: dict = {}
    seen_ids: dict[str, set[int]] = {}
    for season in seasons:
        per_season[season] = {}
        base = http_file(league, season, "table_classic.json")
        teams_data = load_json(http_file(league, season, "teams.json"))
        team_names = {t["team"] for t in teams_data.get("teams", [])} if teams_data else set()
        for view in views:
            path = http_file(league, season, f"table_{view}.json")
            data = load_json(path)
            rec: dict = {"rows": None, "view": view}
            per_season[season][view] = rec
            if data is None or not isinstance(data.get("table"), list):
                continue
            rows = data["table"]
            rec["rows"] = len(rows)
            if len(rows) != EXPECTED_TEAMS_PER_SEASON:
                add_issue(
                    "table", "TABLE_ROWS_UNEXPECTED",
                    SEVERITY_WARNING if len(rows) > 0 else SEVERITY_ERROR,
                    f"table_{view} has {len(rows)} rows, expected {EXPECTED_TEAMS_PER_SEASON}",
                    league=league, season=season, file=rel(path),
                    details={"expected": EXPECTED_TEAMS_PER_SEASON, "actual": len(rows)},
                )
            names = [r.get("team") for r in rows]
            dupes = [n for n, c in Counter(n for n in names if n).items() if c > 1]
            if dupes:
                add_issue("table", "TABLE_DUPLICATE_TEAM", SEVERITY_ERROR, f"Duplicate table team rows: {dupes}", league=league, season=season, file=rel(path), examples=dupes)
            for row in rows:
                if not isinstance(row, dict):
                    add_issue("table", "TABLE_ROW_NOT_DICT", SEVERITY_ERROR, "A table row is not an object", league=league, season=season, file=rel(path))
                    continue
                for field in TABLE_CORE_FIELDS:
                    if field not in row:
                        add_issue("table", "TABLE_MISSING_FIELD", SEVERITY_ERROR, f"Table row '{row.get('team')}' missing field '{field}'", league=league, season=season, file=rel(path), details={"team": row.get("team"), "field": field})
            positions = [r.get("position") for r in rows]
            if positions and (sorted(positions) != list(range(1, len(positions) + 1))):
                add_issue("table", "TABLE_POSITION_ISSUE", SEVERITY_ERROR, "Table positions are not a unique 1..n sequence", league=league, season=season, file=rel(path), details={"positions": positions})
            row_ids = [r.get("id") for r in rows]
            if len(set(row_ids)) != len(row_ids):
                add_issue("table", "TABLE_ROW_ID_DUPLICATE", SEVERITY_ERROR, "Table row ids are not unique", league=league, season=season, file=rel(path))
            if view == "classic":
                seen_ids[season] = set(row_ids)
                if team_names and set(names) != team_names:
                    extra = sorted(set(names) - team_names)
                    missing = sorted(team_names - set(names))
                    add_issue(
                        "table", "TABLE_TEAM_VS_TEAMS_MISMATCH", SEVERITY_WARNING,
                        f"Table teams differ from teams.json ({len(extra)} extra, {len(missing)} missing)",
                        league=league, season=season, file=rel(path),
                        details={"in_table_not_in_teams": extra, "in_teams_not_in_table": missing},
                    )
    # table id stability across seasons
    seasons_with = [s for s in seen_ids if seen_ids[s]]
    intersected = set.intersection(*[seen_ids[s] for s in seasons_with]) if seasons_with else set()
    if seasons_with:
        stable_count = len({tid for tid, c in Counter(tid for s in seasons_with for tid in seen_ids[s]).items() if c == len(seasons_with)})
        add_issue(
            "table", "TABLE_ID_SEASON_SCOPED", SEVERITY_WARNING,
            f"Table row 'id' is not a stable team identifier: only {stable_count} of {len(set().union(*[seen_ids[s] for s in seasons_with]))} distinct ids appear in every collected season",
            league=league, file=rel(http_file(league, seasons[0], "table_classic.json")),
            details={"n_seasons": len(seasons_with), "distinct_ids_overall": len(set().union(*[seen_ids[s] for s in seasons_with])), "ids_in_all_seasons": stable_count},
        )
    return {"status": category_status("table"), "per_season": per_season}


# ── 8. cross-endpoint consistency ─────────────────────────────────────────────
def check_cross_endpoint(league: str, seasons: list[str]) -> dict:
    for season in seasons:
        teams_data = load_json(http_file(league, season, "teams.json"))
        results_data = load_json(http_file(league, season, "results.json"))
        table_data = load_json(http_file(league, season, "table_classic.json"))
        if not teams_data:
            continue
        team_names = [t["team"] for t in teams_data.get("teams", [])]
        team_set = set(team_names)
        if results_data:
            rn = set()
            for m in results_data.get("matches", []):
                if isinstance(m, dict):
                    rn.update([m.get("homeTeam"), m.get("awayTeam")])
            rn.discard(None)
            if rn != team_set:
                add_issue(
                    "cross_endpoint", "RESULTS_TEAMS_VS_TEAMS", SEVERITY_WARNING,
                    f"Results teams differ from teams.json ({len(rn ^ team_set)} differing names)",
                    league=league, season=season, file=rel(http_file(league, season, "teams.json")),
                    details={"only_in_results": sorted(rn - team_set), "only_in_teams": sorted(team_set - rn)},
                )
        if table_data and isinstance(table_data.get("table"), list):
            tn = [r["team"] for r in table_data["table"]]
            if set(tn) != team_set:
                add_issue(
                    "cross_endpoint", "TABLE_TEAMS_VS_TEAMS", SEVERITY_WARNING,
                    "Table team set differs from teams.json",
                    league=league, season=season, file=rel(http_file(league, season, "table_classic.json")),
                    details={"only_in_table": sorted(set(tn) - team_set), "only_in_teams": sorted(team_set - set(tn))},
                )
            order_match = tn == team_names
            if not order_match:
                add_issue(
                    "cross_endpoint", "TABLE_ORDER_VS_TEAMS", SEVERITY_WARNING,
                    "table_classic row order differs from teams.json order",
                    league=league, season=season, file=rel(http_file(league, season, "table_classic.json")),
                )
    return {"status": category_status("cross_endpoint")}


# ── 9. historical consistency ─────────────────────────────────────────────────
def check_historical(league: str, seasons: list[str]) -> dict:
    team_counts, match_counts = {}, {}
    roster: dict[str, list[str]] = {}
    for season in seasons:
        td = load_json(http_file(league, season, "teams.json"))
        rd = load_json(http_file(league, season, "results.json"))
        if td and isinstance(td.get("teams"), list):
            names = [t["team"] for t in td["teams"]]
            team_counts[season] = len(names)
            roster[season] = names
        if rd and isinstance(rd.get("matches"), list):
            match_counts[season] = len(rd["matches"])
    churn: dict[str, dict] = {}
    prev = None
    for season in seasons:
        if prev is not None and season in roster:
            churn[season] = {
                "added": sorted(set(roster[season]) - set(roster[prev])),
                "removed": sorted(set(roster[prev]) - set(roster[season])),
            }
        prev = season if season in roster else prev
    if len(set(team_counts.values())) > 1:
        add_issue(
            "historical", "TEAM_COUNT_CHANGE", SEVERITY_WARNING,
            "Team count varies across seasons",
            league=league, details={"per_season": team_counts},
        )
    if len(set(match_counts.values())) > 1:
        add_issue(
            "historical", "MATCH_COUNT_CHANGE", SEVERITY_WARNING,
            "Match count varies across seasons",
            league=league, details={"per_season": match_counts},
        )
    # recurring issues
    counters = Counter((i["code"], i["severity"]) for i in ISSUES if i["category"] not in ("historical",))
    recurring = [{"code": c, "severity": s, "n": n} for (c, s), n in sorted(counters.items(), key=lambda kv: -kv[1])]
    return {
        "status": category_status("historical"),
        "team_counts": team_counts,
        "match_counts": match_counts,
        "roster_churn": churn,
        "recurring_issues": recurring,
    }


# ── report assembly ───────────────────────────────────────────────────────────
def build_report(league: str, seasons: list[str], views: list[str]) -> dict:
    ISSUES.clear()
    checks = {
        "file_completeness": check_files(league, seasons, views),
        "response_structure": check_leagues_structure(league, seasons),
        "seasonal_structure": check_seasonal_structure(league, seasons, views),
        "teams": check_teams(league, seasons),
        "results": check_results(league, seasons),
        "team_references": check_team_references(league, seasons),
        "match_identity": check_match_identity(league, seasons),
        "table": check_tables(league, seasons, views),
        "cross_endpoint": check_cross_endpoint(league, seasons),
        "historical": check_historical(league, seasons),
    }
    merged_checks = {
        "response_structure": {
            "status": category_status("response_structure"),
            "leagues": checks["response_structure"],
            "seasonal": checks["seasonal_structure"],
        }
    }
    del checks["response_structure"], checks["seasonal_structure"]
    errors = sum(1 for i in ISSUES if i["severity"] == SEVERITY_ERROR)
    warnings = sum(1 for i in ISSUES if i["severity"] == SEVERITY_WARNING)
    return {
        "report_name": "poc_validation_report",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "scope": {"league": league, "seasons": seasons, "views": views},
        "overall": {"errors": errors, "warnings": warnings, "pass": 0, "categories": sorted(set(i["category"] for i in ISSUES) | set(checks.keys()) | set(merged_checks.keys()))},
        "checks": {**merged_checks, **checks},
        "issues": ISSUES,
    }


def render_markdown(report: dict) -> str:
    status_icon = {SEVERITY_ERROR: "ERROR", SEVERITY_WARNING: "WARNING", SEVERITY_PASS: "PASS"}
    lines = ["# Football Charts Raw Data — POC Validation Report", ""]
    lines.append(f"- Generated: {report['generated_at']}")
    scope = report["scope"]
    lines.append(f"- Scope: league `{scope['league']}`; seasons {', '.join(scope['seasons'])}; table views {', '.join(scope['views'])}")
    o = report["overall"]
    lines.append(f"- Overall: **{o['errors']} errors**, **{o['warnings']} warnings**")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    lines.append("| # | Severity | Code | Category | Season | File | Message |")
    lines.append("|---|----------|------|----------|--------|------|---------|")
    for n, issue in enumerate(report["issues"], 1):
        sev = issue["severity"]
        if sev == SEVERITY_PASS:
            continue
        f = issue["file"] or ""
        if f.startswith("data/raw/"):
            f = f.replace("data/raw/", "")
        lines.append(f"| {n} | {sev} | `{issue['code']}` | {issue['category']} | {issue['season'] or '-'} | {f} | {issue['message']} |")
    lines.append("")
    lines.append("## Per-check summary")
    lines.append("")
    lines.append("| Check | Status |")
    lines.append("|-------|--------|")
    for name, check in report["checks"].items():
        status = check.get("status", SEVERITY_PASS)
        lines.append(f"| {name} | {status_icon.get(status, status)} |")
    lines.append("")
    lines.append("## Check details")
    lines.append("")
    for name, check in report["checks"].items():
        lines.append(f"### {name}")
        status = check.get("status", SEVERITY_PASS)
        lines.append(f"**Status:** {status_icon.get(status, status)}")
        for key, value in check.items():
            if key.startswith("_") or key == "status":
                continue
            if key in ("per_season",) and isinstance(value, dict):
                lines.append(f"**{key}:**")
                for s, v in value.items():
                    lines.append(f"- `{s}`: {json.dumps(v, ensure_ascii=False)}")
            elif key in ("recurring_issues", "team_counts", "match_counts", "roster_churn"):
                lines.append(f"**{key}:**")
                lines.append("```json")
                lines.append(json.dumps(value, indent=2, ensure_ascii=False))
                lines.append("```")
            else:
                lines.append(f"**{key}:** `{json.dumps(value, ensure_ascii=False)}`")
        lines.append("")
    issues_by_season = {}
    all_seasons = scope["seasons"]
    for s in all_seasons:
        issues_by_season[s] = [i for i in report["issues"] if i.get("season") == s and i["severity"] != SEVERITY_PASS]
    lines.append("## Issues by season")
    lines.append("")
    lines.append("| Season | Errors | Warnings |")
    lines.append("|--------|--------|----------|")
    for s in all_seasons:
        e = sum(1 for i in issues_by_season.get(s, []) if i["severity"] == SEVERITY_ERROR)
        w = sum(1 for i in issues_by_season.get(s, []) if i["severity"] == SEVERITY_WARNING)
        lines.append(f"| {s} | {e} | {w} |")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append("Reads the byte-preserved raw JSON files under `data/raw/` produced by `scripts/collect_raw_data.py`. Each league/season/endpoint is validated for file presence, top-level schema, required fields, value formats, uniqueness constraints, and cross-endpoint consistency. Findings are classified PASS / WARNING / ERROR; nothing is modified.")
    return "\n".join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="validate_raw_data", description="Validate the collected Football Charts raw dataset.")
    parser.add_argument("--league", default=DEFAULT_LEAGUE)
    parser.add_argument("--season", action="append", metavar="YYYY-YYYY", help="season to validate; repeatable, default: all POC seasons")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    seasons = args.season or DEFAULT_SEASONS
    views = DEFAULT_VIEWS
    report = build_report(args.league, seasons, views)
    VALIDATION_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_MD.write_text(render_markdown(report), encoding="utf-8")
    o = report["overall"]
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")
    print(f"errors={o['errors']} warnings={o['warnings']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())