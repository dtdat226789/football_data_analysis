import os
from pathlib import Path

import httpx
import pytest
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

BASE_URL = "https://footballcharts-backend.onrender.com/api/v1"
API_KEY = os.getenv("FOOTBALL_CHARTS_API_KEY")

LEAGUES = [
    "premier",
    "spain1",
    "germany1",
    "italy1",
    "france1",
]

SEASONS = {
    "premier": "2025-2026",
    "spain1": "2025-2026",
    "germany1": "2025-2026",
    "italy1": "2025-2026",
    "france1": "2025-2026",
}

VIEWS = ["classic", "luck", "goals"]


@pytest.fixture(scope="session")
def api_client():
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    with httpx.Client(base_url=BASE_URL, headers=headers, timeout=30) as client:
        yield client


@pytest.fixture(scope="session")
def leagues_response(api_client):
    return api_client.get("/leagues/")


@pytest.fixture(scope="session")
def premier_table_response(api_client):
    return api_client.get(
        "/leagues/premier/table/",
        params={"season": SEASONS["premier"], "view": "classic"},
    )


@pytest.fixture(scope="session")
def premier_results_response(api_client):
    return api_client.get(
        "/leagues/premier/results/",
        params={"season": SEASONS["premier"]},
    )


@pytest.fixture(scope="session")
def premier_fixtures_response(api_client):
    return api_client.get("/leagues/premier/fixtures/")


@pytest.fixture(scope="session")
def premier_projection_response(api_client):
    return api_client.get("/leagues/premier/projection/")


@pytest.fixture(scope="session")
def premier_goal_timing_response(api_client):
    return api_client.get(
        "/leagues/premier/goal-timing/",
        params={"season": SEASONS["premier"]},
    )


@pytest.fixture(scope="session")
def premier_teams_response(api_client):
    return api_client.get(
        "/leagues/premier/teams/",
        params={"season": SEASONS["premier"]},
    )


@pytest.fixture(scope="session")
def premier_team_page_response(api_client):
    return api_client.get(
        "/leagues/premier/teams/Arsenal/",
        params={"season": SEASONS["premier"]},
    )


@pytest.fixture(scope="session")
def track_record_response(api_client):
    return api_client.get("/track-record/")


@pytest.fixture(scope="session")
def fixture_slug(premier_fixtures_response):
    matches = premier_fixtures_response.json().get("matches", [])
    if not matches:
        pytest.skip("No upcoming fixtures available to build a match slug")
    return matches[0]["slug"]


@pytest.fixture(scope="session")
def settled_match_slug(track_record_response):
    recent = track_record_response.json()["track_record"].get("recent", [])
    if not recent:
        pytest.skip("No settled predictions to build a match slug")
    return recent[0]["slug"]
