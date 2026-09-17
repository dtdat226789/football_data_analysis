"""Fetch raw responses from the Football Charts API and dump them to data/raw/.

Each endpoint is stored as a JSON file keyed by endpoint name. The API key is
loaded from the project root .env file.

Usage:
    python backend/scripts/fetch_raw_data.py
"""
from __future__ import annotations

import json
from pathlib import Path

import httpx
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

import os

BASE_URL = "https://footballcharts-backend.onrender.com/api/v1"
API_KEY = os.getenv("FOOTBALL_CHARTS_API_KEY")
OUTPUT_DIR = ROOT_DIR / "data" / "raw"

LEAGUE = "premier"
SEASON = "2025-2026"
VIEWS = ["classic", "luck", "goals"]


def build_requests(client: httpx.Client) -> list[tuple[str, httpx.Response]]:
    """Return (output_stem, response) pairs for every endpoint to dump."""
    requests: list[tuple[str, httpx.Response]] = []

    requests.append(("leagues", client.get("/leagues/")))

    for view in VIEWS:
        requests.append(
            (
                f"table_{view}",
                client.get(
                    f"/leagues/{LEAGUE}/table/",
                    params={"season": SEASON, "view": view},
                ),
            )
        )

    requests.append(
        (
            "results",
            client.get(
                f"/leagues/{LEAGUE}/results/",
                params={"season": SEASON},
            ),
        )
    )

    fixtures = client.get(f"/leagues/{LEAGUE}/fixtures/").json()
    requests.append(("fixtures", client.get(f"/leagues/{LEAGUE}/fixtures/")))

    requests.append(("projection", client.get(f"/leagues/{LEAGUE}/projection/")))
    requests.append(
        (
            "goal_timing",
            client.get(
                f"/leagues/{LEAGUE}/goal-timing/",
                params={"season": SEASON},
            ),
        )
    )
    requests.append(
        (
            "teams",
            client.get(
                f"/leagues/{LEAGUE}/teams/",
                params={"season": SEASON},
            ),
        )
    )

    team_slug = client.get(
        f"/leagues/{LEAGUE}/teams/",
        params={"season": SEASON},
    ).json()["teams"][0]["slug"]
    requests.append(
        (
            f"team_page_{team_slug}",
            client.get(
                f"/leagues/{LEAGUE}/teams/{team_slug}/",
                params={"season": SEASON},
            ),
        )
    )

    matches = fixtures.get("matches", [])
    if matches:
        match_slug = matches[0]["slug"]
        requests.append(
            (f"match_detail_{match_slug.rsplit('/', 1)[-1]}", client.get(f"/matches/{match_slug}/"))
        )

    requests.append(("track_record", client.get("/track-record/")))

    return requests


def main() -> None:
    if not API_KEY:
        raise SystemExit("FOOTBALL_CHARTS_API_KEY not set in project root .env")

    headers = {"Authorization": f"Bearer {API_KEY}"}
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with httpx.Client(base_url=BASE_URL, headers=headers, timeout=60) as client:
        for stem, response in build_requests(client):
            if response.status_code != 200:
                print(f"SKIP {stem}: HTTP {response.status_code}")
                continue
            path = OUTPUT_DIR / f"{stem}.json"
            path.write_text(
                json.dumps(response.json(), indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"WROTE {path} ({len(response.content):,} bytes)")


if __name__ == "__main__":
    main()