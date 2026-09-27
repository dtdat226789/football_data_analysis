"""Fetch the rich /matches/{slug}/ payload for every upcoming fixture.

fetch_fixtures.py stores the league fixtures endpoints, which carry enough for a
list row but not for a match page: no team logos, no form arrays, no
match_datetime. This script walks the collected fixtures dumps, resolves each
one's upstream slug and stores that match's own payload alongside them.

Only the fields the API surfaces are kept (plus the whole dc_v2 block); the
upstream response is pruned rather than mirrored so the detail directory stays
a cache of this project's own shape rather than a shadow copy of someone else's
schema. Everything else is already in the fixtures dump.

Layout:

    data/raw/fixtures/details/{league}__{date}-home-vs-away.json
    data/raw/fixtures/details/manifest.json

Usage:
    python backend/scripts/fetch_fixture_details.py
    python backend/scripts/fetch_fixture_details.py --league premier eng1
    python backend/scripts/fetch_fixture_details.py --overwrite --delay 0.5
    python backend/scripts/fetch_fixture_details.py --limit 2   # sample a league
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

log = logging.getLogger("fetch_fixture_details")

REQUEST_DELAY_SECONDS = 0.5
MAX_RETRIES = 3
RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

FIXTURES_DIR = ROOT_DIR / "data" / "raw" / "fixtures"
DETAILS_DIR = FIXTURES_DIR / "details"

# Upstream match fields worth storing. Anything absent is simply not published
# for a scheduled match (scores, first-goal times) and stays absent.
KEPT_FIELDS = (
    "id",
    "label",
    "slug",
    "league",
    "real_league_name",
    "country",
    "season",
    "status",
    "match_status",
    "match_date",
    "match_datetime",
    "time",
    "home_team",
    "away_team",
    "home_team_logo",
    "away_team_logo",
    "home_form",
    "away_form",
    "match_minute",
    "finished_at",
    "league_phase_status",
    "portal_link",
    "predictions_allowed",
    "predictions_calculated_at",
    "created_at",
    "updated_at",
)


def build_client() -> httpx.Client:
    """Return the shared httpx client used across the project (see conftest)."""
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set in project root .env")
    return httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=60,
    )


def slug_tail(slug: str) -> str:
    """Trailing `date-home-vs-away` segment of an upstream slug.

    Kept byte-identical to apps.routers.fixtures.slug_tail: the two must agree on
    the filename or the API will look for a file the collector never wrote.
    """
    return (slug or "").rstrip("/").rsplit("/", 1)[-1]


def get_json(client: httpx.Client, url: str) -> dict | None:
    """GET an endpoint and return parsed JSON, or None when unavailable.

    Mirrors fetch_fixtures.get_json: transient failures are retried with
    backoff, honouring Retry-After, and a non-retryable status is logged and
    skipped rather than raised, so one bad slug cannot abort a league.
    """
    for attempt in range(MAX_RETRIES):
        try:
            response = client.get(url)
        except httpx.HTTPError as exc:
            log.warning("NETWORK %s -> %s: %s", url, exc.__class__.__name__, exc)
        else:
            if response.status_code == 200:
                return response.json()
            if response.status_code in RETRYABLE_STATUS_CODES:
                retry_after = response.headers.get("retry-after")
                wait = float(retry_after) if retry_after else float(2**attempt)
                log.warning(
                    "HTTP %s %s; retrying in %.1fs (attempt %d/%d)",
                    response.status_code, url, wait, attempt + 1, MAX_RETRIES,
                )
                time.sleep(wait)
                continue
            log.error("HTTP %s %s (match unavailable; skipping)", response.status_code, url)
            return None
        time.sleep(float(2**attempt))

    log.error("GAVE UP %s after %d attempts", url, MAX_RETRIES)
    return None


def prune_match(match: dict) -> dict:
    """Keep the fields the fixture detail page reads."""
    return {key: match[key] for key in KEPT_FIELDS if key in match}


def fixture_slugs(path: Path, limit: int | None = None) -> list[str]:
    """Upstream slugs for one league's collected fixtures, in kickoff order."""
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, ValueError):
        return []
    matches = payload.get("matches") or [] if isinstance(payload, dict) else []
    matches = sorted(matches, key=lambda m: (m.get("match_date") or "", m.get("time") or ""))
    slugs = [m.get("slug") for m in matches if m.get("slug")]
    return slugs[:limit] if limit else slugs


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fetch_fixture_details",
        description="Fetch /matches/{slug}/ detail payloads for collected upcoming fixtures.",
    )
    parser.add_argument(
        "--league",
        action="append",
        default=None,
        metavar="SLUG",
        help="only fetch these league slugs (repeatable); default: every collected fixtures file",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="only fetch the next N fixtures per league (useful for sampling)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="re-download details even if they already exist",
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

    if not FIXTURES_DIR.is_dir():
        print(f"ERROR: no fixtures at {FIXTURES_DIR}; run fetch_fixtures.py first")
        return 1

    files = (
        [FIXTURES_DIR / f"{league}.json" for league in args.league]
        if args.league
        else sorted(p for p in FIXTURES_DIR.glob("*.json") if p.name != "manifest.json")
    )
    files = [p for p in files if p.exists()]
    if not files:
        print("fetch_fixture_details: no collected fixtures files to read")
        return 1

    DETAILS_DIR.mkdir(parents=True, exist_ok=True)
    manifest: dict = {"written": [], "skipped": [], "failed": []}

    with build_client() as client:
        for path in files:
            league = path.stem
            slugs = fixture_slugs(path, args.limit)
            if not slugs:
                log.info("EMPTY %s (no fixtures)", league)
                continue
            for slug in slugs:
                if args.delay:
                    time.sleep(args.delay)
                out_path = DETAILS_DIR / f"{league}__{slug_tail(slug)}.json"
                if out_path.exists() and not args.overwrite:
                    manifest["skipped"].append(out_path.name)
                    continue

                payload = get_json(client, f"/matches/{slug}/")
                if payload is None:
                    manifest["failed"].append(f"{league}/{slug}")
                    continue
                match = payload.get("match")
                if not isinstance(match, dict):
                    log.error("NO MATCH %s (unexpected payload shape)", slug)
                    manifest["failed"].append(f"{league}/{slug}")
                    continue

                out_path.write_text(
                    json.dumps(
                        {"match": prune_match(match), "attribution": payload.get("attribution")},
                        indent=2,
                        ensure_ascii=False,
                    ),
                    encoding="utf-8",
                )
                manifest["written"].append(out_path.name)
                log.info(
                    "OK    %s  %s vs %s  %s",
                    out_path.name,
                    match.get("home_team"),
                    match.get("away_team"),
                    match.get("match_status") or match.get("status"),
                )

    manifest_path = DETAILS_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\nfetch_fixture_details summary:")
    print(
        f"  written: {len(manifest['written'])}  "
        f"skipped: {len(manifest['skipped'])}  failed: {len(manifest['failed'])}"
    )
    print(f"  manifest: {manifest_path.relative_to(ROOT_DIR)}")
    if manifest["failed"]:
        print(f"  WARN failed fixtures: {len(manifest['failed'])} (see manifest)")

    return 0 if not manifest["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
