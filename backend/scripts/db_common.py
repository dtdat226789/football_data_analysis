"""Shared helpers for the database build & validation pipeline (steps 01-06).

Every step script in this package loads the project .env, opens a psycopg2
connection to DATABASE_URL and works against the SQL migration files in sql/.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import date
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

SQL_DIR = ROOT_DIR / "sql"
RAW_DIR = ROOT_DIR / "data" / "raw"

LEAGUE = "premier"
COLLECTED_SEASONS = [
    "2020-2021",
    "2021-2022",
    "2022-2023",
    "2023-2024",
    "2024-2025",
    "2025-2026",
]
VIEWS = ["classic", "luck", "goals"]

# Leagues whose format is not a plain full double round-robin. Matches for a
# split/playoff league are still stored as the formula value; analyses that
# care about format can branch on this flag.
FORMAT_OVERRIDES = {
    "scot-premier": "split",
    "austria1": "split",
    "belgium1": "playoff",
    "greece1": "playoff",
    "romania1": "playoff",
}

# Fallback entries used only when data/raw/league_teams.json is unavailable
# (e.g. tests that build the DB before the config probe has run).
_FALLBACK_CONFIG = {
    "premier": {"name": "Premier League", "country": "England", "teams": 20},
    "spain1": {"name": "LaLiga", "country": "Spain", "teams": 20},
    "germany1": {"name": "Bundesliga", "country": "Germany", "teams": 18},
    "italy1": {"name": "Serie A", "country": "Italy", "teams": 20},
    "france1": {"name": "Ligue 1", "country": "France", "teams": 18},
}


def _load_league_config() -> dict:
    """Build LEAGUE_CONFIG from the probed league table when it exists.

    Source of truth is data/raw/league_teams.json (written by
    backend/scripts/build_league_config.py): every catalog league gets a row
    with name/country/teams/url. match counts default to the formula
    teams*(teams-1) and are overrideable per league.
    """
    path = RAW_DIR / "league_teams.json"
    if not path.exists():
        rows = _FALLBACK_CONFIG
    else:
        try:
            rows = json.loads(path.read_bytes())
        except ValueError:
            rows = _FALLBACK_CONFIG

    config: dict = {}
    for slug, meta in rows.items():
        teams = int(meta.get("teams", 20))
        config[slug] = {
            "name": meta.get("name", slug),
            "country": meta.get("country", ""),
            "teams": teams,
            "matches": meta.get("matches", teams * (teams - 1)),
            "views": meta.get("views", VIEWS),
            "format": FORMAT_OVERRIDES.get(slug, meta.get("format", "round-robin")),
            "url": meta.get("url", ""),
        }
    return config


# Per-league expectations. Kept in one place so the whole pipeline (build,
# profile, analysis) can adapt to a country/format just by adding a row to
# data/raw/league_teams.json and re-running build_league_config.py.
#   teams / matches   flagship full-season format (double round-robin)
#   name, country     display metadata from the /leagues/ catalog
LEAGUE_CONFIG = _load_league_config()


def league_meta(league: str) -> dict:
    """Per-league config with safe defaults for leagues not yet registered."""
    meta = LEAGUE_CONFIG.get(league, {})
    return {
        "name": meta.get("name", league),
        "country": meta.get("country", ""),
        "teams": meta.get("teams", 20),
        "matches": meta.get("matches", 380),
        "views": meta.get("views", VIEWS),
        "format": meta.get("format", "round-robin"),
        "url": meta.get("url", ""),
    }


def catalog_seasons(league: str | None = None) -> list[str]:
    """Declared seasons for a league from its local /leagues/ catalog.

    Reads data/raw/{league}/leagues.json (the raw catalog file) and returns the
    seasons the API declares for that league, in catalog order. Returns []
    when the file or league entry is missing.
    """
    lg = league or LEAGUE
    path = RAW_DIR / lg / "leagues.json"
    if not path.exists():
        return []
    data = load_json(path)
    entry = next((e for e in data.get("leagues", []) if e.get("league") == lg), None)
    if entry is None:
        return []
    return list(entry.get("seasons", []))


def _season_sort_key(name: str) -> tuple[int, int]:
    start, end = parse_season_years(name)
    if start is None or end is None:
        return (0, 0)
    return (start, end)


def league_season_dirs(league: str | None = None) -> list[str]:
    """Season names that exist as directories under data/raw/{league}/."""
    lg = league or LEAGUE
    base = RAW_DIR / lg
    if not base.is_dir():
        return []
    return sorted(
        (d.name for d in base.iterdir() if d.is_dir()),
        key=_season_sort_key,
    )


def collected_seasons(league: str | None = None) -> list[str]:
    """Seasons with collected raw data for a league.

    A season counts as collected when its data/raw/{league}/{season}/ directory
    contains teams.json, results.json and the three table views. Falls back to
    COLLECTED_SEASONS only when the league directory is entirely absent and the
    league is the default (the historical set remains authoritative for it).
    """
    lg = league or LEAGUE
    dirs = league_season_dirs(lg)
    if not dirs:
        return list(COLLECTED_SEASONS) if lg == LEAGUE else []
    return [
        s for s in dirs
        if (RAW_DIR / lg / s / "teams.json").exists()
        and (RAW_DIR / lg / s / "results.json").exists()
        and all((RAW_DIR / lg / s / f"table_{v}.json").exists() for v in VIEWS)
    ]


def get_conn() -> psycopg2.extensions.connection:
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        sys.exit("DATABASE_URL not set in project root .env")
    return psycopg2.connect(dsn)


def apply_sql(conn, filename: str) -> None:
    """Execute one migration file inside the current transaction."""
    path = SQL_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Migration not found: {path}")
    with conn.cursor() as cur:
        cur.execute(path.read_text())
    conn.commit()
    print(f"[schema] applied {filename}")


def raw_file(season: str, name: str, league: str | None = None) -> Path:
    lg = league or LEAGUE
    return RAW_DIR / lg / season / name


def load_json(path: Path) -> dict:
    return json.loads(path.read_bytes())


def parse_season_years(name: str) -> tuple[int | None, int | None]:
    """Best-effort parse of an opaque season string for start/end ordering.

    '2020-2021' -> (2020, 2021); '2026' -> (2026, 2026); unknown -> (None, None).
    """
    parts = [p for p in name.split("-") if p.isdigit()]
    if not parts:
        return None, None
    start = int(parts[0])
    end = int(parts[-1]) if len(parts) > 1 else start
    return min(start, end), max(start, end)


# Kickoff/finish bounds used to turn an opaque season label into a calendar
# window. European split seasons start in late summer and finish in May.
SPLIT_SEASON_START = (6, 1)
SPLIT_SEASON_END = (8, 15)


def season_date_window(name: str) -> tuple[date, date] | None:
    """Inclusive date window a season label is expected to cover.

    '2025-2026' -> 2025-06-01 .. 2026-08-15 (split season, Europe)
    '2026'      -> 2026-01-01 .. 2026-12-31 (calendar-year season)
    a label with no parseable year returns None.
    """
    start_year, end_year = parse_season_years(name)
    if start_year is None or end_year is None:
        return None
    if start_year == end_year:
        return date(start_year, 1, 1), date(end_year, 12, 31)
    return date(start_year, *SPLIT_SEASON_START), date(end_year, *SPLIT_SEASON_END)


def is_season_active(name: str, today: date | None = None) -> bool:
    """True when `today` falls inside the season's calendar window."""
    window = season_date_window(name)
    if window is None:
        return False
    return window[0] <= (today or date.today()) <= window[1]


# Half-time result strings the API uses when a HT score is unavailable.
HT_ABSENT_MARKERS = {"", "not found", "n/a", "none", "null"}

SENTINEL_KICKOFF = "00:00:00"


def split_score(raw: str | None) -> tuple[int, int] | None:
    """Split an upstream score string into a regulation (home, away) result.

    Trailing outcome suffixes are stripped: '2:1AfP' (after penalties) and
    '1:3AET' (after extra time) yield the regulation score used for the table.
    Cancelled / awarded markers ('CAN.', 'AWA.', '2:0CAN.') and non-scores
    return None.
    """
    if not isinstance(raw, str):
        return None
    if "CAN" in raw.upper() or "AWA" in raw.upper():
        return None
    base = raw.strip()
    while base and not base[-1].isdigit():
        base = base[:-1]
    if base.count(":") != 1:
        return None
    a, b = base.split(":")
    if not a.isdigit() or not b.isdigit():
        return None
    return int(a), int(b)


def score_status(raw: str | None) -> str:
    """Classify a raw score string for the ETL and the validators.

    'playable'      a regulation result is present ('1:0', '2:1AfP', '1:3AET')
    'unplayed'      cancelled or awarded match ('CAN.', 'AWA.', '2:0CAN.');
                    the matches schema cannot represent these (no status
                    column), so the ETL skips them.
    'unparseable'   anything else, including a missing score.
    """
    if not isinstance(raw, str):
        return "unparseable"
    marker = raw.upper()
    if "CAN" in marker or "AWA" in marker:
        return "unplayed"
    return "playable" if split_score(raw) is not None else "unparseable"


_SEASON_STATES = {"complete", "in_progress", "unknown"}
_SEASON_STATE_VARIANTS = {"in_season": "in_progress"}


def normalize_season_state(raw: str | None) -> str:
    """Map an upstream season_state onto the DB enum ('complete'|'in_progress'|'unknown').

    The API reports an ongoing season as 'in_season'; the registry constraint
    (01_registry.sql) uses 'in_progress'. Unknown variants fall back to
    'unknown' so a new API value can never violate the CHECK constraint.
    """
    value = (raw or "unknown").strip().lower()
    if value in _SEASON_STATES:
        return value
    return _SEASON_STATE_VARIANTS.get(value, "unknown")