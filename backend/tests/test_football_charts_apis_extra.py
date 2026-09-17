"""Tests for additional Football Charts API endpoints.

Base URL: https://footballcharts-backend.onrender.com/api/v1

Endpoints tested:
  - GET /leagues/{league}/projection/          Monte Carlo season projection
  - GET /leagues/{league}/goal-timing/         Goal-timing heat map
  - GET /leagues/{league}/teams/               Teams in table order
  - GET /leagues/{league}/teams/{team}/        Team page
  - GET /matches/{slug}/                       Match detail
  - GET /track-record/                         Settled prediction ledger
"""
from __future__ import annotations

import httpx

from .conftest import SEASONS

TEAM_COUNT = 20
TIME_BINS = ["0-15", "15-30", "30-45", "45+", "46-60", "60-75", "75-90", "90+"]


# ── GET /leagues/{league}/projection/ ─────────────────────────────────────────


class TestGetProjection:
    """Tests for the /leagues/{league}/projection/ endpoint."""

    def test_status_code(self, premier_projection_response: httpx.Response):
        assert premier_projection_response.status_code == 200

    def test_top_level_keys(self, premier_projection_response: httpx.Response):
        data = premier_projection_response.json()
        assert set(data.keys()) == {"projection", "attribution"}

    def test_projection_field_keys(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        assert "league" in proj
        assert "season" in proj
        assert "run_date" in proj
        assert "teams" in proj
        assert isinstance(proj["teams"], dict)

    def test_teams_count(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        assert len(proj["teams"]) == TEAM_COUNT

    def test_team_entry_fields(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        required = {
            "title", "top4", "bottom1", "bottom2", "bottom3",
            "pts_now", "mean_pts", "p10_pts", "p90_pts",
            "played", "gd_now", "position_matrix",
        }
        for team, entry in proj["teams"].items():
            assert required.issubset(entry.keys()), (
                f"Team '{team}' missing fields: {required - entry.keys()}"
            )

    def test_position_matrix_length(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        for team, entry in proj["teams"].items():
            assert len(entry["position_matrix"]) == TEAM_COUNT, (
                f"Team '{team}' position_matrix should have {TEAM_COUNT} slots"
            )

    def test_position_matrix_weights_normalized(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        for team, entry in proj["teams"].items():
            weights = [w for w in entry["position_matrix"] if isinstance(w, (int, float))]
            assert 0.95 <= sum(weights) <= 1.05, (
                f"Team '{team}' position weights sum to {sum(weights):.3f}, "
                "expected ~1.0"
            )

    def test_probabilities_in_range(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        prob_fields = ("title", "top4", "bottom1", "bottom2", "bottom3")
        for team, entry in proj["teams"].items():
            for field in prob_fields:
                assert 0.0 <= entry[field] <= 1.0, (
                    f"Team '{team}'.{field}={entry[field]} out of [0,1]"
                )

    def test_n_sims_positive(self, premier_projection_response: httpx.Response):
        proj = premier_projection_response.json()["projection"]
        assert proj["n_sims"] > 0

    def test_unknown_league_returns_null(self, api_client: httpx.Client):
        r = api_client.get("/leagues/badxx/projection/")
        assert r.status_code == 200
        assert r.json()["projection"] is None


# ── GET /leagues/{league}/goal-timing/ ────────────────────────────────────────


class TestGetGoalTiming:
    """Tests for the /leagues/{league}/goal-timing/ endpoint."""

    def test_status_code(self, premier_goal_timing_response: httpx.Response):
        assert premier_goal_timing_response.status_code == 200

    def test_top_level_keys(self, premier_goal_timing_response: httpx.Response):
        data = premier_goal_timing_response.json()
        assert "league" in data
        assert "season" in data
        assert "time_bins" in data
        assert "stats" in data
        assert "data" in data

    def test_time_bins(self, premier_goal_timing_response: httpx.Response):
        data = premier_goal_timing_response.json()
        assert data["time_bins"] == TIME_BINS

    def test_stats_keys(self, premier_goal_timing_response: httpx.Response):
        stats = premier_goal_timing_response.json()["stats"]
        assert {"total_goals", "most_active_period", "period_totals",
                "late_goals", "match_count"}.issubset(stats.keys())

    def test_period_totals_sum_to_total(self, premier_goal_timing_response: httpx.Response):
        stats = premier_goal_timing_response.json()["stats"]
        assert sum(stats["period_totals"]) == stats["total_goals"]
        assert len(stats["period_totals"]) == len(TIME_BINS)

    def test_most_active_period_is_valid_bin(self, premier_goal_timing_response: httpx.Response):
        stats = premier_goal_timing_response.json()["stats"]
        assert stats["most_active_period"] in TIME_BINS

    def test_match_count(self, premier_goal_timing_response: httpx.Response):
        stats = premier_goal_timing_response.json()["stats"]
        assert stats["match_count"] == 380

    def test_team_rows(self, premier_goal_timing_response: httpx.Response):
        data = premier_goal_timing_response.json()["data"]
        assert isinstance(data, list)
        assert len(data) == TEAM_COUNT
        for row in data:
            assert "team" in row
            assert "total" in row
            assert "bins" in row
            assert set(row["bins"].keys()) == set(TIME_BINS)

    def test_team_bins_sum_to_total(self, premier_goal_timing_response: httpx.Response):
        for row in premier_goal_timing_response.json()["data"]:
            assert sum(row["bins"].values()) == row["total"], (
                f"Bins for '{row['team']}' do not sum to total {row['total']}"
            )

    def test_unknown_league_returns_404(self, api_client: httpx.Client):
        r = api_client.get(
            "/leagues/badxx/goal-timing/",
            params={"season": SEASONS["premier"]},
        )
        assert r.status_code == 404


# ── GET /leagues/{league}/teams/ ──────────────────────────────────────────────


class TestGetTeams:
    """Tests for the /leagues/{league}/teams/ endpoint."""

    def test_status_code(self, premier_teams_response: httpx.Response):
        assert premier_teams_response.status_code == 200

    def test_top_level_keys(self, premier_teams_response: httpx.Response):
        data = premier_teams_response.json()
        assert "league" in data
        assert "season" in data
        assert "teams" in data

    def test_team_fields(self, premier_teams_response: httpx.Response):
        teams = premier_teams_response.json()["teams"]
        assert isinstance(teams, list)
        assert len(teams) == TEAM_COUNT
        required = {"team", "slug", "position", "points", "played", "logo_url"}
        for team in teams:
            assert required.issubset(team.keys()), (
                f"Team '{team.get('team')}' missing: {required - team.keys()}"
            )

    def test_positions_sequential(self, premier_teams_response: httpx.Response):
        positions = [t["position"] for t in premier_teams_response.json()["teams"]]
        assert positions == list(range(1, len(positions) + 1))

    def test_slugs_are_slugs(self, premier_teams_response: httpx.Response):
        for team in premier_teams_response.json()["teams"]:
            assert team["slug"] == team["slug"].lower()
            assert " " not in team["slug"]

    def test_unknown_league_returns_404(self, api_client: httpx.Client):
        r = api_client.get("/leagues/badxx/teams/")
        assert r.status_code == 404


# ── GET /leagues/{league}/teams/{team}/ ───────────────────────────────────────


class TestGetTeamPage:
    """Tests for the /leagues/{league}/teams/{team}/ endpoint."""

    def test_status_code(self, premier_team_page_response: httpx.Response):
        assert premier_team_page_response.status_code == 200

    def test_top_level_keys(self, premier_team_page_response: httpx.Response):
        data = premier_team_page_response.json()
        assert "team" in data
        assert "slug" in data
        assert "league" in data
        assert "season" in data
        assert "seasons" in data
        assert "ranking" in data
        assert "matches" in data
        assert "goal_bins" in data
        assert "stats" in data

    def test_team_identity(self, premier_team_page_response: httpx.Response):
        data = premier_team_page_response.json()
        assert data["team"] == "Arsenal"
        assert data["slug"] == "arsenal"

    def test_ranking_present(self, premier_team_page_response: httpx.Response):
        ranking = premier_team_page_response.json()["ranking"]
        assert "team" in ranking
        assert "position" in ranking
        assert "points" in ranking
        assert ranking["team"] == "Arsenal"

    def test_matches_non_empty(self, premier_team_page_response: httpx.Response):
        matches = premier_team_page_response.json()["matches"]
        assert isinstance(matches, list)
        assert len(matches) > 0
        required = {"id", "date", "time", "home", "away", "venue",
                    "score", "ht", "outcome"}
        for m in matches:
            assert required.issubset(m.keys()), (
                f"Match missing: {required - m.keys()}"
            )

    def test_seasons_back_to_2020(self, premier_team_page_response: httpx.Response):
        seasons = premier_team_page_response.json()["seasons"]
        assert len(seasons) >= 2
        assert "2020-2021" in seasons
        assert seasons == sorted(seasons, reverse=True)

    def test_goal_bins_length(self, premier_team_page_response: httpx.Response):
        data = premier_team_page_response.json()
        assert data["time_bins"] == TIME_BINS
        assert len(data["goal_bins"]) == len(TIME_BINS)
        assert len(data["first_goal_bins"]) == len(TIME_BINS) + 1

    def test_first_goal_bins_include_no_goal(self, premier_team_page_response: httpx.Response):
        first_goal_bins = premier_team_page_response.json()["first_goal_bins"]
        times = [b["time"] for b in first_goal_bins]
        assert times[: len(TIME_BINS)] == TIME_BINS
        assert "No Goal" in times

    def test_stats_keys(self, premier_team_page_response: httpx.Response):
        stats = premier_team_page_response.json()["stats"]
        assert isinstance(stats, dict)
        assert len(stats) > 0

    def test_unknown_team_returns_404(self, api_client: httpx.Client):
        r = api_client.get("/leagues/premier/teams/NonexistentFC/")
        assert r.status_code == 404
        assert r.json()["error"]["code"] == "not_found"


# ── GET /matches/{slug}/ ──────────────────────────────────────────────────────


class TestGetMatchDetail:
    """Tests for the /matches/{slug}/ endpoint."""

    def test_upcoming_match_status_code(self, api_client: httpx.Client, fixture_slug: str):
        r = api_client.get(f"/matches/{fixture_slug}/")
        assert r.status_code == 200

    def test_upcoming_match_fields(self, api_client: httpx.Client, fixture_slug: str):
        r = api_client.get(f"/matches/{fixture_slug}/")
        match = r.json()["match"]
        assert "slug" in match
        assert "home_team" in match
        assert "away_team" in match
        assert "match_date" in match
        assert "model_predictions" in match
        assert match["slug"] == fixture_slug

    def test_upcoming_match_model_predictions(self, api_client: httpx.Client, fixture_slug: str):
        match = api_client.get(f"/matches/{fixture_slug}/").json()["match"]
        preds = match["model_predictions"]
        assert isinstance(preds, dict)
        assert len(preds) > 0
        model = next(iter(preds.values()))
        assert "raw" in model
        assert "calibrated" in model

    def test_settled_match_fields(self, api_client: httpx.Client, settled_match_slug: str):
        r = api_client.get(f"/matches/{settled_match_slug}/")
        assert r.status_code == 200
        match = r.json()["match"]
        assert match["slug"] == settled_match_slug
        assert match["match_status"].upper() == "FT"
        assert isinstance(match["home_score"], int)
        assert isinstance(match["away_score"], int)
        assert "ht_result" in match
        assert "finished_at" in match

    def test_settled_match_probability(self, api_client: httpx.Client, settled_match_slug: str):
        match = api_client.get(f"/matches/{settled_match_slug}/").json()["match"]
        prob = match["prediction_probability"]
        assert prob is None or 0.0 <= prob <= 1.0

    def test_unknown_slug_returns_404(self, api_client: httpx.Client):
        r = api_client.get("/matches/does/not-exist/")
        assert r.status_code == 404
        assert r.json()["error"]["code"] == "not_found"


# ── GET /track-record/ ────────────────────────────────────────────────────────


class TestGetTrackRecord:
    """Tests for the /track-record/ endpoint."""

    def test_status_code(self, track_record_response: httpx.Response):
        assert track_record_response.status_code == 200

    def test_top_level_keys(self, track_record_response: httpx.Response):
        data = track_record_response.json()
        assert set(data.keys()) == {"track_record", "attribution"}

    def test_track_record_field_keys(self, track_record_response: httpx.Response):
        tr = track_record_response.json()["track_record"]
        required = {"signals_only", "summary", "by_market", "by_market_all",
                    "daily_by_family", "policy_markers", "daily",
                    "recent", "pending", "accuracy"}
        assert required.issubset(tr.keys())

    def test_summary_consistency(self, track_record_response: httpx.Response):
        summary = track_record_response.json()["track_record"]["summary"]
        required = {"n", "won", "lost", "void", "pl", "hit_rate"}
        assert required.issubset(summary.keys())
        assert summary["won"] + summary["lost"] + summary["void"] == summary["n"]
        assert 0.0 <= summary["hit_rate"] <= 1.0

    def test_by_market_consistency(self, track_record_response: httpx.Response):
        by_market = track_record_response.json()["track_record"]["by_market"]
        assert isinstance(by_market, dict)
        assert len(by_market) > 0
        for market, stats in by_market.items():
            assert stats["won"] + stats["lost"] + stats["void"] == stats["n"], (
                f"Market '{market}' totals do not reconcile"
            )

    def test_recent_predictions(self, track_record_response: httpx.Response):
        recent = track_record_response.json()["track_record"]["recent"]
        assert isinstance(recent, list)
        assert len(recent) > 0
        required = {"slug", "home_team", "away_team", "match_date",
                    "market", "side", "outcome", "pl", "model_prob"}
        for record in recent:
            assert required.issubset(record.keys()), (
                f"Record missing: {required - record.keys()}"
            )
            assert record["outcome"] in {"won", "lost", "void"}

    def test_daily_totals(self, track_record_response: httpx.Response):
        daily = track_record_response.json()["track_record"]["daily"]
        assert isinstance(daily, list)
        assert len(daily) > 0
        assert {"date", "n", "won", "pl", "cum_pl"}.issubset(daily[0].keys())

    def test_accuracy_buckets(self, track_record_response: httpx.Response):
        accuracy = track_record_response.json()["track_record"]["accuracy"]
        assert {"n", "brier", "buckets"}.issubset(accuracy.keys())
        buckets = accuracy["buckets"]
        assert isinstance(buckets, list)
        assert len(buckets) >= 3
        for bucket in buckets:
            assert {"lo", "hi", "n", "avg_prob", "hit_rate"}.issubset(bucket.keys())
            assert bucket["hi"] > bucket["lo"]