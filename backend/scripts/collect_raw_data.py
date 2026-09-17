"""POC data-collection pipeline for the Football Charts API.

Collects the raw API responses for a league/season combination under data/raw/
without parsing or transforming the payloads (each file is the server's body,
written byte-for-byte).

Layout (league and season are unambiguous):

    data/raw/{league}/leagues.json                 # GET /leagues/
    data/raw/{league}/{season}/teams.json          # GET /leagues/{league}/teams/
    data/raw/{league}/{season}/results.json        # GET /leagues/{league}/results/
    data/raw/{league}/{season}/table_{view}.json   # GET /leagues/{league}/table/

The collector is idempotent: files that already exist are skipped unless
--overwrite is given. Non-200 responses (e.g. an unavailable season) are logged
and skipped rather than raising. Requests are spaced out (--delay) and transient
5xx/429 responses are retried with backoff, honouring Retry-After when present.

Examples:
    # full POC: Premier League, 2020-21 .. 2025-26, classic/luck/goals tables
    python backend/scripts/collect_raw_data.py

    # a single league/season
    python backend/scripts/collect_raw_data.py --league premier --season 2024-2025

    # force re-download of everything
    python backend/scripts/collect_raw_data.py --overwrite
"""
from __future__ import annotations

import argparse
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

log = logging.getLogger("collect_raw_data")

# ── POC configuration (all overridable via CLI) ──────────────────────────────
DEFAULT_LEAGUE = "premier"
DEFAULT_SEASONS = [
    "2020-2021",
    "2021-2022",
    "2022-2023",
    "2023-2024",
    "2024-2025",
    "2025-2026",
]
DEFAULT_VIEWS = ["classic", "luck", "goals"]

REQUEST_DELAY_SECONDS = 1.0
MAX_RETRIES = 3
RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

OUTPUT_DIR = ROOT_DIR / "data" / "raw"


def build_client() -> httpx.Client:
    """Return the shared httpx client used across the project (see conftest)."""
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set in project root .env")
    return httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=60,
    )


def get_raw(
    client: httpx.Client,
    url: str,
    params: dict | None = None,
    max_retries: int = MAX_RETRIES,
) -> bytes | None:
    """GET an endpoint and return the raw response body.

    Returns None (after logging) when the endpoint is unavailable. Transient
    failures (429 and 5xx) are retried with backoff, honouring the Retry-After
    header when the server provides it.
    """
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
                return response.content
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


def collect_file(
    client: httpx.Client,
    url: str,
    params: dict | None,
    out_path: Path,
    overwrite: bool,
    delay: float,
) -> None:
    """Save one endpoint response under out_path, or skip when it exists."""
    try:
        rel = out_path.relative_to(ROOT_DIR)
    except ValueError:
        rel = out_path
    if out_path.exists() and not overwrite:
        log.info("SKIP  %s (already exists)", rel)
        return
    if delay:
        time.sleep(delay)
    content = get_raw(client, url, params)
    if content is None:
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(content)
    log.info("OK    %s (%d bytes)", rel, len(content))


def collect_league(
    client: httpx.Client,
    league: str,
    seasons: list[str],
    views: list[str],
    overwrite: bool,
    delay: float,
) -> None:
    """Collect league information once, then teams/results/table per season."""
    collect_file(client, "/leagues/", None, OUTPUT_DIR / league / "leagues.json", overwrite, delay)

    for season in seasons:
        season_dir = OUTPUT_DIR / league / season
        collect_file(
            client,
            f"/leagues/{league}/teams/",
            {"season": season},
            season_dir / "teams.json",
            overwrite,
            delay,
        )
        collect_file(
            client,
            f"/leagues/{league}/results/",
            {"season": season},
            season_dir / "results.json",
            overwrite,
            delay,
        )
        for view in views:
            collect_file(
                client,
                f"/leagues/{league}/table/",
                {"season": season, "view": view},
                season_dir / f"table_{view}.json",
                overwrite,
                delay,
            )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="collect_raw_data",
        description="Collect raw Football Charts API responses under data/raw/.",
    )
    parser.add_argument("--league", default=DEFAULT_LEAGUE, help="league slug (default: premier)")
    parser.add_argument(
        "--season",
        action="append",
        metavar="YYYY-YYYY",
        help="season to collect; repeatable, default: all POC seasons",
    )
    parser.add_argument(
        "--view",
        action="append",
        metavar="VIEW",
        help="table view; repeatable, default: classic luck goals",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="re-download files even if they already exist",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=REQUEST_DELAY_SECONDS,
        help=f"seconds between requests (default: {REQUEST_DELAY_SECONDS})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)-5s %(message)s", stream=sys.stdout)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    seasons = args.season or DEFAULT_SEASONS
    views = args.view or DEFAULT_VIEWS

    with build_client() as client:
        collect_league(client, args.league, seasons, views, args.overwrite, args.delay)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())