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
    # `has_data` reports whether analysis reports exist under data/analysis/.
    # That is build output and is gitignored, so it is False on a fresh clone and
    # in CI until run_analysis.py has run; only its presence and type are
    # guaranteed. The match counts below come from the database and are real.
    assert isinstance(slugs["premier"]["has_data"], bool)
    assert slugs["premier"]["matches"] == 380


def test_league_detail(client):
    r = client.get("/api/v1/leagues/premier")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body["has_data"], bool)  # see test_leagues
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


# ── date filter validation ───────────────────────────────────────────────────
# These params used to be bare strings handed straight to psycopg2: a malformed
# value raised out of the driver and surfaced as a 500.
DATE_FILTER_ENDPOINTS = [
    "/api/v1/matches/recent",
    "/api/v1/leagues/premier/matches",
    "/api/v1/fixtures",
]


@pytest.mark.parametrize("url", DATE_FILTER_ENDPOINTS)
@pytest.mark.parametrize("bad", ["not-a-date", "2025-13-45", "31/12/2025", "2025-02-30"])
def test_malformed_date_is_422_not_500(client, url, bad):
    for param in ("from_date", "to_date"):
        r = client.get(url, params={param: bad})
        assert r.status_code == 422, f"{url}?{param}={bad} -> {r.status_code}"


@pytest.mark.parametrize("url", DATE_FILTER_ENDPOINTS)
def test_inverted_date_window_is_422(client, url):
    r = client.get(url, params={"from_date": "2026-05-01", "to_date": "2026-01-01"})
    assert r.status_code == 422
    assert "after" in r.json()["detail"]


@pytest.mark.parametrize("url", DATE_FILTER_ENDPOINTS)
def test_valid_date_window_is_accepted(client, url):
    assert client.get(url, params={"from_date": "2026-01-01", "to_date": "2026-12-31"}).status_code == 200


@pytest.mark.parametrize("url", DATE_FILTER_ENDPOINTS)
def test_open_ended_date_window_is_accepted(client, url):
    assert client.get(url, params={"from_date": "2026-01-01"}).status_code == 200
    assert client.get(url, params={"to_date": "2026-01-01"}).status_code == 200


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


def test_list_teams_search_narrows_the_registry(client):
    """`q` filters server-side, so a term is found off the first page.

    The registry spans every league, so a client-side filter over one page of
    50 could only match rows it had already fetched.
    """
    everything = client.get("/api/v1/teams", params={"limit": 1}).json()
    assert everything["total"] > 50, "guard: registry must exceed one page"

    r = client.get("/api/v1/teams", params={"q": "arsenal"})
    assert r.status_code == 200
    body = r.json()
    assert body["q"] == "arsenal"
    assert 0 < body["total"] < everything["total"]
    names = [t["canonical_name"] for t in body["teams"]]
    assert "Arsenal" in names
    assert all("arsenal" in name.lower() for name in names)


def test_list_teams_search_is_case_insensitive(client):
    lower = client.get("/api/v1/teams", params={"q": "arsenal"}).json()
    upper = client.get("/api/v1/teams", params={"q": "ARSENAL"}).json()
    assert lower["teams"] == upper["teams"]


def test_list_teams_search_matches_slug(client):
    r = client.get("/api/v1/teams", params={"q": "aston-villa"})
    assert r.status_code == 200
    assert [t["canonical_name"] for t in r.json()["teams"]] == ["Aston Villa"]


def test_list_teams_search_counts_matches_across_the_whole_registry(client):
    """The reported total is the match count, not the size of the returned page."""
    body = client.get("/api/v1/teams", params={"q": "manchester", "limit": 1}).json()
    assert len(body["teams"]) == 1
    assert body["total"] >= len(body["teams"])


def test_list_teams_blank_search_is_ignored(client):
    unfiltered = client.get("/api/v1/teams", params={"limit": 1}).json()
    for blank in ["", "   "]:
        body = client.get("/api/v1/teams", params={"q": blank, "limit": 1}).json()
        assert body["total"] == unfiltered["total"]


def test_list_teams_search_with_no_match_is_empty_not_an_error(client):
    r = client.get("/api/v1/teams", params={"q": "definitely-not-a-club-xyzzy"})
    assert r.status_code == 200
    body = r.json()
    assert body["total"] == 0
    assert body["teams"] == []


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


def test_team_stats_best_describes_one_season(client):
    """position, position_season and points must all come from the same row.

    position used to be min(position) while points was max(points), which are
    usually different seasons, so the card implied a single season record that
    never existed.
    """
    body = client.get("/api/v1/teams/arsenal/stats", params={"league": "premier"}).json()
    best = body["best"]
    assert best["position"] is not None
    row = next(s for s in body["seasons"] if s["season"] == best["position_season"])
    assert best["position"] == row["position"]
    assert best["points"] == row["points"]
    assert best["played"] == row["played"]


def test_team_stats_season_scopes_the_aggregate(client):
    """`season` narrows totals and the venue split; the per-season history stays."""
    everything = client.get("/api/v1/teams/arsenal/stats", params={"league": "premier"}).json()
    assert everything["scope"] == "all"
    assert everything["season"] is None

    seasons = everything["seasons"]
    target = max(seasons, key=lambda s: s["played"])
    scoped = client.get(
        "/api/v1/teams/arsenal/stats",
        params={"league": "premier", "season": target["season"]},
    ).json()

    assert scoped["scope"] == target["season"]
    assert len(scoped["seasons"]) == len(seasons), "history must not be narrowed"
    assert scoped["totals"]["played"] == target["played"]
    assert scoped["totals"]["points"] == target["points"]
    assert scoped["totals"]["goals_for"] == target["goals_for"]
    venue_total = sum(v["played"] for v in scoped["home_away"].values())
    assert venue_total == target["played"], "venue split must match the scope"


def test_team_stats_season_scope_differs_from_career(client):
    """The scope has to actually change the numbers, or the selector is a no-op."""
    career = client.get("/api/v1/teams/arsenal/stats", params={"league": "premier"}).json()
    scoped = client.get(
        "/api/v1/teams/arsenal/stats",
        params={"league": "premier", "season": career["seasons"][0]["season"]},
    ).json()
    assert scoped["totals"]["played"] < career["totals"]["played"]
    assert scoped["totals"]["played"] == career["seasons"][0]["played"]


def test_team_stats_unknown_season_is_404(client):
    r = client.get(
        "/api/v1/teams/arsenal/stats",
        params={"league": "premier", "season": "1999-2000"},
    )
    assert r.status_code == 404


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


@pytest.mark.parametrize(
    "endpoint",
    ["matches", "form", "standings", "stats"],
)
def test_team_in_a_league_it_does_not_play_in_is_404(client, endpoint):
    """An empty 200 was indistinguishable from "they have not played yet".

    require_league only proves the league is registered, so a real team paired
    with the wrong league used to look like a genuine empty result.
    """
    r = client.get(f"/api/v1/teams/arsenal/{endpoint}", params={"league": "germany1"})
    assert r.status_code == 404
    assert "does not play" in r.json()["detail"]


@pytest.mark.parametrize(
    "endpoint",
    ["matches", "form", "standings", "stats"],
)
def test_team_in_its_own_league_is_still_200(client, endpoint):
    assert client.get(f"/api/v1/teams/arsenal/{endpoint}", params={"league": "premier"}).status_code == 200


def test_league_membership_is_checked_across_seasons_not_just_the_requested_one(client):
    """A missing season for a real member is a 404 about the season, not the league."""
    career = client.get(
        "/api/v1/teams/arsenal/matches", params={"league": "premier"}
    ).json()
    assert career["total"] > 0
    seasons = sorted({m["season"] for m in career["matches"]})
    assert seasons, "fixture is expected to return matches with a season label"
    r = client.get(
        "/api/v1/teams/arsenal/matches",
        params={"league": "premier", "season": seasons[0]},
    )
    assert r.status_code == 200
    assert "does not play" not in r.text
