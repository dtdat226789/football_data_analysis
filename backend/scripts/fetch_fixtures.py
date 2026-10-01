"""Fetch upcoming fixtures with model predictions from the Football Charts API.

Hits GET /leagues/{league}/fixtures/ for every league in the catalog (or the
subset selected with --league) and dumps each league's full response as a JSON
file under data/raw/fixtures/, preserving the server's payload including the
model_predictions block (dc_v2 model probabilities, calibrated lines, gates).

Only non-empty responses (count > 0, i.e. there are scheduled/upcoming
fixtures) are written, so leagues with no upcoming matches are skipped and the
results manifest records them without creating a file.

Layout:

    data/raw/fixtures/{league}.json     # GET /leagues/{league}/fixtures/
    data/raw/fixtures/manifest.json     # per-league summary + file map

Usage:
    python backend/scripts/fetch_fixtures.py
    python backend/scripts/fetch_fixtures.py --league premier germany1
    python backend/scripts/fetch_fixtures.py --overwrite
    python backend/scripts/fetch_fixtures.py --overwrite --delay 3

Re-running without --overwrite skips any league whose file already exists, so a
routine refresh needs it. The gap between requests defaults to 2s and can be
raised per run with --delay or permanently with FETCH_DELAY_SECONDS in .env.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT_DIR / "backend"))
load_dotenv(ROOT_DIR / ".env")

from tests.conftest import API_KEY, BASE_URL  # noqa: E402

log = logging.getLogger("fetch_fixtures")

# Politeness gap between requests. Configured in one place, like API_PORT: the
# environment wins, then the project .env, then the default. Raise it to be
# gentler on the feed -- a full catalog sweep is 93 sequential requests, so the
# delay is what the API actually feels.
REQUEST_DELAY_SECONDS = float(os.getenv("FETCH_DELAY_SECONDS", "2.0"))
MAX_RETRIES = 3
RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)

OUTPUT_DIR = ROOT_DIR / "data" / "raw" / "fixtures"
CATALOG_PATH = ROOT_DIR / "data" / "raw" / "leagues.json"


def build_client() -> httpx.Client:
    """Return the shared httpx client used across the project (see conftest)."""
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set in project root .env")
    return httpx.Client(
        base_url=BASE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=60,
    )


def load_catalog(path: Path) -> list[dict]:
    """Load the league catalog from the local leagues.json dump if present."""
    try:
        payload = json.loads(path.read_bytes())
    except (OSError, ValueError):
        return []
    leagues = payload.get("leagues", []) if isinstance(payload, dict) else []
    return [item for item in leagues if isinstance(item, dict) and item.get("league")]


def get_json(client: httpx.Client, url: str) -> dict | None:
    """GET an endpoint and return parsed JSON, or None when unavailable.

    Transient failures (429 and 5xx) are retried with backoff, honouring the
    Retry-After header when the server provides it.
    """
    for attempt in range(MAX_RETRIES):
        try:
            response = client.get(url)
        except httpx.HTTPError as exc:
            log.warning(
                "NETWORK %s -> %s: %s",
                url,
                exc.__class__.__name__,
                exc,
            )
        else:
            if response.status_code == 200:
                return response.json()
            if response.status_code in RETRYABLE_STATUS_CODES:
                retry_after = response.headers.get("retry-after")
                wait = float(retry_after) if retry_after else float(2**attempt)
                log.warning(
                    "HTTP %s %s; retrying in %.1fs (attempt %d/%d)",
                    response.status_code,
                    url,
                    wait,
                    attempt + 1,
                    MAX_RETRIES,
                )
                time.sleep(wait)
                continue
            log.error("HTTP %s %s (endpoint unavailable; skipping)", response.status_code, url)
            return None
        time.sleep(float(2**attempt))

    log.error("GAVE UP %s after %d attempts", url, MAX_RETRIES)
    return None


def summarize_predictions(payload: dict) -> list[dict]:
    """Extract a compact per-match summary from a fixtures response."""
    rows: list[dict] = []
    for match in payload.get("matches", []) or []:
        preds = (match.get("model_predictions") or {}).get("dc_v2") or {}
        calibrated = preds.get("calibrated") or {}
        raw = preds.get("raw") or {}
        rows.append(
            {
                "slug": match.get("slug"),
                "home_team": match.get("home_team"),
                "away_team": match.get("away_team"),
                "match_date": match.get("match_date"),
                "time": match.get("time"),
                "status": match.get("status"),
                "home": calibrated.get("home"),
                "away": calibrated.get("away"),
                "btts_yes": calibrated.get("btts_yes"),
                "over_1_5": calibrated.get("over_1.5"),
                "over_2_5": calibrated.get("over_2.5"),
                "expected_home_goals": raw.get("expected_home_goals"),
                "expected_away_goals": raw.get("expected_away_goals"),
                "computed_at": preds.get("computed_at"),
                "data_through": preds.get("data_through") or (preds.get("data_status") or {}).get("data_through"),
            }
        )
    return rows


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="fetch_fixtures",
        description="Fetch upcoming fixtures with model predictions for catalog leagues.",
    )
    parser.add_argument(
        "--league",
        action="append",
        default=None,
        metavar="SLUG",
        help="only fetch these league slugs (repeatable); default: every catalog league",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="re-download fixtures even if they already exist",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=REQUEST_DELAY_SECONDS,
        help=f"seconds between requests (default: {REQUEST_DELAY_SECONDS})",
    )
    parser.add_argument(
        "--catalog",
        default=str(CATALOG_PATH),
        help=f"path to a leagues.json catalog dump (default: {CATALOG_PATH})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)-5s %(message)s", stream=sys.stdout)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    catalog = load_catalog(Path(args.catalog))
    if not catalog:
        print(f"ERROR: no catalog at {args.catalog}; run fetch_raw_data.py first")
        return 1

    slugs = args.league or [item["league"] for item in catalog]
    if not slugs:
        print("fetch_fixtures: no leagues requested")
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest: dict = {"written": [], "empty": [], "failed": []}

    with build_client() as client:
        for league in slugs:
            if args.delay:
                time.sleep(args.delay)
            url = f"/leagues/{league}/fixtures/"
            out_path = OUTPUT_DIR / f"{league}.json"
            if out_path.exists() and not args.overwrite:
                log.info("SKIP  %s (already exists)", out_path.relative_to(ROOT_DIR))
                manifest["written"].append(league)
                continue

            payload = get_json(client, url)
            if payload is None:
                manifest["failed"].append(league)
                continue

            count = payload.get("count", len(payload.get("matches") or []))
            if not count:
                log.info("EMPTY %s (no upcoming fixtures)", league)
                manifest["empty"].append(league)
                continue

            out_path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            manifest["written"].append(league)
            summary = summarize_predictions(payload)
            log.info("OK    %s (%d fixtures) -> %s", league, count, out_path.relative_to(ROOT_DIR))
            for row in summary:
                print(
                    f"  {row['match_date']} {row['time'] or ''}  "
                    f"{row['home_team']} vs {row['away_team']}  "
                    f"[{row['status']}]  P(home)={row['home']}  P(away)={row['away']}  "
                    f"BTTS={row['btts_yes']}  O2.5={row['over_2_5']}"
                )

    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("\nfetch_fixtures summary:")
    print(f"  written: {len(manifest['written'])}  empty: {len(manifest['empty'])}  failed: {len(manifest['failed'])}")
    print(f"  manifest: {manifest_path.relative_to(ROOT_DIR)}")
    if manifest["failed"]:
        print(f"  WARN failed leagues: {', '.join(manifest['failed'])}")

    return 0 if not manifest["failed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())