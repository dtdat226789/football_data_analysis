"""Build the per-league configuration table used to run the analysis pipeline.

Every league in the Football Charts catalog (data/raw/leagues.json) is probed
once via GET /leagues/{league}/teams/ for its most recent season to learn the
current team count. The result is written to data/raw/league_teams.json in the
shape consumed by db_common.LEAGUE_CONFIG:

    {
      "premier": {
        "name": "Premier League", "country": "England", "teams": 20,
        "season": "2025-2026", "seasons": ["2026-2027", "2025-2026"],
        "url": "https://www.football-charts.com/leagues/england/premier-league"
      }, ...
    }

Only the team count is fetched; name/country/url/seasons come from the catalog.
The probe is idempotent: existing league_teams.json entries are kept unless
--overwrite is given. A league whose newest season returns no teams falls back
to its previous season; a league with no data in either is recorded with
teams: 0 so it is easy to spot.

Usage:
    python backend/scripts/build_league_config.py
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))
load_dotenv(ROOT_DIR / ".env")

from tests.conftest import API_KEY, BASE_URL  # noqa: E402

log = logging.getLogger("build_league_config")

REQUEST_DELAY_SECONDS = 1.0
MAX_RETRIES = 3
RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

# Plausible team-count band for a single division. Counts outside this range
# are treated as API anomalies (e.g. a promotion/playoff blob) and ignored.
MIN_PLAUSIBLE_TEAMS = 8
MAX_PLAUSIBLE_TEAMS = 30

# Leagues whose newest-season team list is known to under-report the full
# first-team complement (a club missing from the still-open season). These
# override the probed count; the probe still fills every other league.
TEAM_COUNT_OVERRIDES = {
    "germany1": 18,  # Bundesliga: 18 clubs, API shows 17 while 2026-27 is open
}

CATALOG_PATH = ROOT_DIR / "data" / "raw" / "leagues.json"
OUTPUT_PATH = ROOT_DIR / "data" / "raw" / "league_teams.json"


def build_client() -> httpx.Client:
    """Return the shared httpx client used across the project (see conftest)."""
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set in project root .env")
    return httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=60,
    )


def _season_start(name: str) -> tuple[int, int]:
    """Order seasons by (start_year, end_year); '2026' == (2026, 2026)."""
    parts = [p for p in name.split("-") if p.isdigit()]
    if not parts:
        return (0, 0)
    start, end = int(parts[0]), int(parts[-1])
    return min(start, end), max(start, end)


def order_seasons(seasons: list[str]) -> list[str]:
    """Sort seasons newest-first by (start_year, end_year)."""
    return sorted(seasons, key=_season_start, reverse=True)


def get_json(
    client: httpx.Client,
    url: str,
    params: dict | None = None,
    max_retries: int = MAX_RETRIES,
) -> dict | None:
    """GET an endpoint and return the parsed JSON body, or None on failure."""
    for attempt in range(max_retries):
        try:
            response = client.get(url, params=params)
        except httpx.HTTPError as exc:
            log.warning(
                "NETWORK %s %s -> %s: %s",
                url,
                params or "",
                exc.__class__.__name__,
                exc,
            )
        else:
            if response.status_code == 200:
                try:
                    return response.json()
                except ValueError:
                    log.error("BAD JSON %s %s", url, params or "")
                    return None
            if response.status_code in RETRYABLE_STATUS_CODES:
                retry_after = response.headers.get("retry-after")
                wait = float(retry_after) if retry_after else float(2**attempt)
                log.warning(
                    "HTTP %s %s %s; retrying in %.1fs (attempt %d/%d)",
                    response.status_code,
                    url,
                    params or "",
                    wait,
                    attempt + 1,
                    max_retries,
                )
                time.sleep(wait)
                continue
            log.error(
                "HTTP %s %s %s (endpoint unavailable; skipping)",
                response.status_code,
                url,
                params or "",
            )
            return None
        time.sleep(float(2**attempt))
    log.error("GAVE UP %s %s after %d attempts", url, params or "", max_retries)
    return None


def probe_league(
    client: httpx.Client,
    league: str,
    catalog: dict,
    delay: float,
) -> dict:
    """Fetch the team count for one league, preferring the current season.

    Every catalog season is probed; the newest (current) season with a
    plausible team count wins, since completed seasons in the API can carry
    inflated lists (e.g. France 21, Eredivisie 24). TEAM_COUNT_OVERRIDES fixes
    the rare case where the open season under-reports a known complement.
    """
    seasons = order_seasons(catalog.get("seasons", []))
    if not seasons:
        log.warning("%-10s no seasons in catalog", league)
        return {
            "name": catalog.get("name", league),
            "country": catalog.get("country", ""),
            "teams": 0,
            "season": None,
            "seasons": [],
            "url": catalog.get("url", ""),
        }

    probes: list[tuple[str, int]] = []
    for season in seasons:
        if delay:
            time.sleep(delay)
        body = get_json(client, f"/leagues/{league}/teams/", {"season": season})
        teams = len((body or {}).get("teams") or [])
        log.info("%-10s %s -> %d teams", league, season, teams)
        probes.append((season, teams))

    for season, teams in probes:
        if MIN_PLAUSIBLE_TEAMS <= teams <= MAX_PLAUSIBLE_TEAMS:
            teams = TEAM_COUNT_OVERRIDES.get(league, teams)
            return {
                "name": catalog.get("name", league),
                "country": catalog.get("country", ""),
                "teams": teams,
                "season": season,
                "seasons": catalog.get("seasons", []),
                "url": catalog.get("url", ""),
            }

    return {
        "name": catalog.get("name", league),
        "country": catalog.get("country", ""),
        "teams": TEAM_COUNT_OVERRIDES.get(league, 0),
        "season": None,
        "seasons": catalog.get("seasons", []),
        "url": catalog.get("url", ""),
    }


def load_catalog(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"Catalog not found: {path}")
    data = json.loads(Path(path).read_bytes())
    return {item["league"]: item for item in data.get("leagues", [])}


def load_existing(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(Path(path).read_bytes())
        except ValueError:
            log.warning("Ignoring unparseable %s", path)
    return {}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="build_league_config",
        description="Probe team counts for every catalog league and write league_teams.json.",
    )
    parser.add_argument("--overwrite", action="store_true", help="re-probe cached leagues")
    parser.add_argument("--delay", type=float, default=REQUEST_DELAY_SECONDS, help="seconds between requests")
    parser.add_argument(
        "--league",
        action="append",
        default=None,
        help="only probe these leagues (repeatable); default: all catalog leagues",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    catalog = load_catalog(CATALOG_PATH)
    existing = load_existing(OUTPUT_PATH)

    slugs = args.league if args.league else sorted(catalog)
    probes: dict[str, dict] = dict(existing)
    configs_needed = [s for s in slugs if s not in existing or args.overwrite]

    if not configs_needed:
        print("all requested leagues already present; use --overwrite to re-probe")
    else:
        with build_client() as client:
            for slug in configs_needed:
                probes[slug] = probe_league(client, slug, catalog[slug], args.delay)

    OUTPUT_PATH.write_text(json.dumps(probes, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUTPUT_PATH} ({len(probes)} leagues)")
    for slug, cfg in sorted(probes.items()):
        marker = "" if cfg["teams"] > 0 else "  <-- NO DATA"
        print(f"  {slug:<12} {cfg['teams']:>3} teams  {cfg.get('season')}{marker}")
    return 0


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
    )
    raise SystemExit(main())