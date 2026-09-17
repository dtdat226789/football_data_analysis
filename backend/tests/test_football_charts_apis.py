"""Tests for Football Charts API endpoints.

Base URL: https://footballcharts-backend.onrender.com/api/v1

Endpoints tested:
  - GET /leagues/                         All leagues + queryable seasons
  - GET /leagues/{league}/table/          Standings (classic | luck | goals)
  - GET /leagues/{league}/results/        Finished matches
  - GET /leagues/{league}/fixtures/       Upcoming matches with model probabilities
"""
from __future__ import annotations

import json

import httpx
import pytest

from .conftest import LEAGUES, SEASONS, VIEWS


# ── GET /leagues/ ──────────────────────────────────────────────────────────────


class TestGetLeagues:
    """Tests for the /leagues/ endpoint."""

    def test_returns_200(self, leagues_response: httpx.Response):
        assert leagues_response.status_code == 200

    def test_returns_json(self, leagues_response: httpx.Response):
        assert "application/json" in leagues_response.headers["content-type"]

    def test_top_level_keys(self, leagues_response: httpx.Response):
        data = leagues_response.json()
        required_keys = {"leagues", "count", "season_window", "attribution"}
        assert required_keys.issubset(data.keys())

    def test_count_matches_leagues_list(self, leagues_response: httpx.Response):
        data = leagues_response.json()
        assert data["count"] == len(data["leagues"])

    def test_leagues_is_non_empty_list(self, leagues_response: httpx.Response):
        data = leagues_response.json()
        assert isinstance(data["leagues"], list)
        assert len(data["leagues"]) > 0

    def test_each_league_has_required_fields(self, leagues_response: httpx.Response):
        required = {"league", "name", "country", "seasons", "url"}
        for entry in leagues_response.json()["leagues"]:
            assert required.issubset(entry.keys()), (
                f"League '{entry.get('league')}' missing fields: {required - entry.keys()}"
            )

    def test_seasons_are_lists_of_strings(self, leagues_response: httpx.Response):
        for entry in leagues_response.json()["leagues"]:
            assert isinstance(entry["seasons"], list)
            assert all(isinstance(s, str) for s in entry["seasons"])

    def test_known_leagues_present(self, leagues_response: httpx.Response):
        slugs = {e["league"] for e in leagues_response.json()["leagues"]}
        for slug in LEAGUES:
            assert slug in slugs, f"Expected league '{slug}' not found"


# ── GET /leagues/{league}/table/ ──────────────────────────────────────────────


class TestGetLeagueTable:
    """Tests for the /leagues/{league}/table/ endpoint."""

    @pytest.mark.parametrize("view", VIEWS)
    def test_status_code_per_view(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        assert r.status_code == 200, f"view={view} returned {r.status_code}"

    @pytest.mark.parametrize("view", VIEWS)
    def test_top_level_keys(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        data = r.json()
        assert data["view"] == view
        assert "table" in data
        assert isinstance(data["table"], list)

    @pytest.mark.parametrize("view", VIEWS)
    def test_table_has_20_teams(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        assert len(r.json()["table"]) == 20

    @pytest.mark.parametrize("view", VIEWS)
    def test_table_item_fields(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        table = r.json()["table"]
        required = {
            "team", "position", "played", "won", "drawn", "lost",
            "goals_for", "goals_against", "goal_difference", "points",
        }
        for row in table:
            assert required.issubset(row.keys()), (
                f"Team '{row.get('team')}' missing: {required - row.keys()}"
            )

    @pytest.mark.parametrize("view", VIEWS)
    def test_positions_are_sequential(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        positions = [row["position"] for row in r.json()["table"]]
        assert positions == list(range(1, len(positions) + 1))

    @pytest.mark.parametrize("view", VIEWS)
    def test_points_non_negative(self, api_client: httpx.Client, view: str):
        r = api_client.get(
            "/leagues/premier/table/",
            params={"season": SEASONS["premier"], "view": view},
        )
        for row in r.json()["table"]:
            assert row["points"] >= 0
            assert row["played"] >= 0

    def test_unknown_league_returns_404(self, api_client: httpx.Client):
        r = api_client.get(
            "/leagues/nonexistent/table/",
            params={"season": "2025-2026", "view": "classic"},
        )
        assert r.status_code == 404
        error = r.json()["error"]
        assert error["code"] == "unknown_league"

    @pytest.mark.parametrize("league", LEAGUES[:3])
    def test_multiple_leagues(self, api_client: httpx.Client, league: str):
        r = api_client.get(
            f"/leagues/{league}/table/",
            params={"season": SEASONS[league], "view": "classic"},
        )
        assert r.status_code == 200
        assert len(r.json()["table"]) > 0


# ── GET /leagues/{league}/results/ ────────────────────────────────────────────


class TestGetLeagueResults:
    """Tests for the /leagues/{league}/results/ endpoint."""

    def test_status_code(self, premier_results_response: httpx.Response):
        assert premier_results_response.status_code == 200

    def test_top_level_keys(self, premier_results_response: httpx.Response):
        data = premier_results_response.json()
        assert "matches" in data
        assert "count" in data
        assert data["count"] == len(data["matches"])

    def test_matches_are_non_empty(self, premier_results_response: httpx.Response):
        matches = premier_results_response.json()["matches"]
        assert len(matches) > 0

    def test_match_fields(self, premier_results_response: httpx.Response):
        match = premier_results_response.json()["matches"][0]
        required = {
            "id", "game_index", "date", "time",
            "homeTeam", "awayTeam", "score", "ht_result",
        }
        assert required.issubset(match.keys())

    def test_score_format(self, premier_results_response: httpx.Response):
        for match in premier_results_response.json()["matches"]:
            score = match["score"]
            assert ":" in score, f"Invalid score format: {score}"
            parts = score.split(":")
            assert len(parts) == 2
            assert parts[0].strip().isdigit()
            assert parts[1].strip().isdigit()

    def test_team_filter(self, api_client: httpx.Client):
        r = api_client.get(
            "/leagues/premier/results/",
            params={"season": SEASONS["premier"], "team": "Arsenal"},
        )
        assert r.status_code == 200
        matches = r.json()["matches"]
        assert len(matches) > 0
        for m in matches:
            assert "Arsenal" in (m["homeTeam"], m["awayTeam"])

    def test_dates_are_chronological(self, premier_results_response: httpx.Response):
        matches = premier_results_response.json()["matches"]
        dates = [m["date"] for m in matches]
        assert dates == sorted(dates)

    @pytest.mark.parametrize("league", LEAGUES[:3])
    def test_multiple_leagues(self, api_client: httpx.Client, league: str):
        r = api_client.get(
            f"/leagues/{league}/results/",
            params={"season": SEASONS[league]},
        )
        assert r.status_code == 200
        assert r.json()["count"] > 0


# ── GET /leagues/{league}/fixtures/ ───────────────────────────────────────────


class TestGetLeagueFixtures:
    """Tests for the /leagues/{league}/fixtures/ endpoint."""

    def test_status_code(self, premier_fixtures_response: httpx.Response):
        assert premier_fixtures_response.status_code == 200

    def test_top_level_keys(self, premier_fixtures_response: httpx.Response):
        data = premier_fixtures_response.json()
        assert "matches" in data
        assert "count" in data

    def test_matches_is_list(self, premier_fixtures_response: httpx.Response):
        assert isinstance(premier_fixtures_response.json()["matches"], list)

    def test_fixture_has_model_predictions(self, premier_fixtures_response: httpx.Response):
        matches = premier_fixtures_response.json()["matches"]
        assert len(matches) > 0, "No upcoming fixtures to test"
        fixture = matches[0]
        assert "model_predictions" in fixture
        preds = fixture["model_predictions"]
        assert len(preds) > 0, "No model predictions found"
        model_key = next(iter(preds))
        model = preds[model_key]
        assert "raw" in model
        assert "calibrated" in model
        assert "ratings" in model

    def test_prediction_probabilities_valid_range(self, premier_fixtures_response: httpx.Response):
        for fixture in premier_fixtures_response.json()["matches"]:
            preds = fixture["model_predictions"]
            for model_name, model in preds.items():
                raw = model.get("raw", {})
                for key in ("home", "away", "btts_yes", "over_1.5", "over_2.5"):
                    if key in raw:
                        prob = raw[key]
                        assert 0.0 <= prob <= 1.0, (
                            f"{model_name}.{key}={prob} out of [0,1] for "
                            f"{fixture.get('home_team')} vs {fixture.get('away_team')}"
                        )

    def test_fixture_required_fields(self, premier_fixtures_response: httpx.Response):
        required = {
            "home_team", "away_team", "match_date",
            "status", "league", "model_predictions",
        }
        for fixture in premier_fixtures_response.json()["matches"]:
            assert required.issubset(fixture.keys()), (
                f"Fixture missing fields: {required - fixture.keys()}"
            )

    def test_fixture_dates_are_future(self, premier_fixtures_response: httpx.Response):
        from datetime import date
        today = date.today()
        for fixture in premier_fixtures_response.json()["matches"]:
            fixture_date = date.fromisoformat(fixture["match_date"])
            assert fixture_date >= today, (
                f"Fixture {fixture['home_team']} vs {fixture['away_team']} "
                f"is in the past: {fixture['match_date']}"
            )

    @pytest.mark.parametrize("league", LEAGUES[:3])
    def test_multiple_leagues(self, api_client: httpx.Client, league: str):
        r = api_client.get(f"/leagues/{league}/fixtures/")
        assert r.status_code == 200
        assert isinstance(r.json()["matches"], list)
