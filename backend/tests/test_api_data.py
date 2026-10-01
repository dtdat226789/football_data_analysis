"""Tests for the live-database API routers (catalog / standings / matches / teams).

These exercise the read-only PostgreSQL-backed endpoints against the real
analytics database (premier collection), mirroring how the query-layer of the
framework is verified end-to-end. Requires DATABASE_URL from the project .env.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from apps.main import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# ── meta / catalog ──────────────────────────────────────────────────────────
def test_meta(client):
    r = client.get("/api/v1/meta")
    assert r.status_code == 200
    body = r.json()
    assert body["api_version"] == "1.0.0"
    assert body["n_leagues"] == 93
    assert body["database"]["reachable"] is True


def test_leagues(client):
    r = client.get("/api/v1/leagues")
    assert r.status_code == 200
    slugs = {item["slug"]: item for item in r.json()}
    assert "premier" in slugs and "spain1" in slugs
    assert slugs["premier"]["has_data"] is True
    assert slugs["premier"]["matches"] == 380


def test_league_detail(client):
    r = client.get("/api/v1/leagues/premier")
    assert r.status_code == 200
    body = r.json()
    assert body["has_data"] is True
    assert body["seasons"]
    by_season = {s["season"]: s for s in body["seasons"]}
    assert by_season["2025-2026"]["matches"] == 380
    assert by_season["2020-2021"]["declared_by_api"] is False
    assert {s["season"] for s in body["seasons"] if s["matches"] == 380} >= {
        "2020-2021", "2021-2022", "2022-2023",
        "2023-2024", "2024-2025", "2025-2026",
    }
    assert 0 < by_season["2026-2027"]["matches"] < 380  # in-progress season


def test_league_seasons_endpoint(client):
    r = client.get("/api/v1/leagues/premier/seasons")
    assert r.status_code == 200
    assert len(r.json()["seasons"]) >= 6


def test_league_unknown_404(client):
    assert client.get("/api/v1/leagues/no-such-league").status_code == 404


# ── standings ───────────────────────────────────────────────────────────────
def test_standings_default_season(client):
    r = client.get("/api/v1/leagues/premier/standings")
    assert r.status_code == 200
    body = r.json()
    assert body["season"] == "2026-2027"  # latest season with collected data
    assert body["view"] == "classic"
    assert len(body["rows"]) == 20
    assert [row["position"] for row in body["rows"]] == list(range(1, 21))


def test_standings_explicit_season_and_views(client):
    for view in ("classic", "luck", "goals"):
        r = client.get(
            "/api/v1/leagues/premier/standings",
            params={"season": "2025-2026", "view": view},
        )
        assert r.status_code == 200
        body = r.json()
        assert len(body["rows"]) == 20
        assert all(row["points"] == 3 * row["won"] + row["drawn"] for row in body["rows"])


def test_standings_unknown_season_404(client):
    assert (
        client.get("/api/v1/leagues/premier/standings", params={"season": "1999-2000"}).status_code
        == 404
    )


def test_standings_invalid_view_422(client):
    assert (
        client.get("/api/v1/leagues/premier/standings", params={"view": "bogus"}).status_code
        == 422
    )


# ── matches ──────────────────────────────────────────────────────────────────
def test_matches_paginated(client):
    r = client.get(
        "/api/v1/leagues/premier/matches",
        params={"season": "2025-2026", "limit": 10},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 380
    assert len(body["matches"]) == 10
    first = body["matches"][0]
    for key in ("api_id", "home_team", "away_team", "home_score", "away_score", "match_date"):
        assert key in first


def test_matches_date_filter(client):
    r = client.get(
        "/api/v1/leagues/premier/matches",
        params={"season": "2025-2026", "from_date": "2026-08-01"},
    )
    assert r.status_code == 200
    assert r.json()["total"] < 380


def test_matches_unknown_season_404(client):
    assert (
        client.get("/api/v1/leagues/premier/matches", params={"season": "1999-2000"}).status_code
        == 404
    )


def test_single_match(client):
    r = client.get(
        "/api/v1/leagues/premier/matches", params={"season": "2025-2026", "limit": 1}
    )
    api_id = r.json()["matches"][0]["api_id"]
    r = client.get(f"/api/v1/matches/{api_id}")
    assert r.status_code == 200
    body = r.json()
    assert body["api_id"] == api_id
    # The page shows the name; the slug only ever feeds the link.
    assert body["league"] == "premier"
    assert body["league_name"] == "Premier League"


def test_single_match_missing_404(client):
    assert client.get("/api/v1/matches/999999999").status_code == 404


# ── teams ────────────────────────────────────────────────────────────────────
def test_list_teams(client):
    r = client.get("/api/v1/teams", params={"limit": 5})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] > 0
    assert len(body["teams"]) == 5


def test_team_detail(client):
    r = client.get("/api/v1/teams/Arsenal")
    assert r.status_code == 200
    body = r.json()
    assert body["team"]["canonical_name"] == "Arsenal"
    assert body["memberships"]
    assert all("league" in m and "season" in m for m in body["memberships"])


def test_team_unknown_404(client):
    assert client.get("/api/v1/teams/no-such-team").status_code == 404


def test_team_form(client):
    r = client.get(
        "/api/v1/teams/Arsenal/form",
        params={"league": "premier", "season": "2025-2026", "n": 5},
    )
    assert r.status_code == 200
    results = r.json()["results"]
    assert len(results) == 5
    assert all(res["team_result"] in ("W", "D", "L") for res in results)


def test_team_matches(client):
    r = client.get(
        "/api/v1/teams/Arsenal/matches",
        params={"league": "premier", "season": "2025-2026", "limit": 3},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 38
    assert len(body["matches"]) == 3
    assert all("Arsenal" in (m["home_team"], m["away_team"]) for m in body["matches"])


def test_team_standings(client):
    r = client.get(
        "/api/v1/teams/Arsenal/standings",
        params={"league": "premier", "season": "2025-2026"},
    )
    assert r.status_code == 200
    row = r.json()["row"]
    assert row is not None
    assert 1 <= row["position"] <= 20


def test_team_stats(client):
    r = client.get(
        "/api/v1/teams/arsenal/stats",
        params={"league": "premier", "view": "classic"},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["team"] == "arsenal"
    assert body["league"] == "premier"
    assert body["view"] == "classic"
    assert len(body["seasons"]) >= 6
    seasons = body["seasons"]
    assert all(
        set(keys) <= set(s)
        for s in seasons
        for keys in [("season", "position", "played", "points")]
    )
    assert body["totals"]["played"] == sum(s["played"] for s in seasons)
    assert body["best"]["position"] == min(s["position"] for s in seasons)
    for venue in body["home_away"]:
        assert set(body["home_away"][venue]) >= {"played", "won", "points"}


def test_team_stats_with_view(client):
    r = client.get(
        "/api/v1/teams/arsenal/stats",
        params={"league": "premier", "view": "luck"},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["view"] == "luck"
    assert all("points" in s for s in body["seasons"])


def test_team_stats_unknown_404(client):
    assert client.get("/api/v1/teams/no-such-team/stats").status_code == 404