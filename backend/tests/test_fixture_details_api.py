"""Tests for the single-fixture detail endpoint (backend/apps/routers/fixtures.py).

Two layers are covered:

  * file-only — the fixture row, the full dc_v2 block, kickoff metadata, logos
    and slug resolution, with the database made unavailable on purpose.
  * database  — matchday, form, venue split, the pre-match panel and head-to-head,
    driven through a stub cursor so the derived logic is tested without a
    live PostgreSQL (the same technique ml/tests/test_predict.py uses).

Runs against a temporary fixtures directory, so nothing here reads real data.
"""
from __future__ import annotations

import json
import sys
from contextlib import contextmanager
from datetime import date, timedelta
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.routers.fixtures as fixtures  # noqa: E402
from apps import routers  # noqa: E402
from apps.main import app  # noqa: E402

SLUG = "spain/primera-rfef-group-1/2026-09-26-a-vs-b"
TAIL = "2026-09-26-a-vs-b"
MATCH_DATE = "2026-09-26"

# The list feed only carries fixtures that have not been played, and this sample's
# date is fixed, so the feed needs a second, always-future match to read from.
# FIXTURE stays on its original date: the detail endpoint is date-agnostic and
# must keep serving a fixture that has since been kicked off.
FUTURE_SLUG = "spain/primera-rfef-group-1/2026-09-27-c-vs-d"
FUTURE_TAIL = "2026-09-27-c-vs-d"
FUTURE_DATE = (date.today() + timedelta(days=1)).isoformat()

DC_V2 = {
    "xi": 0.0019,
    "model": "dc_v2.0",
    "sigma": 0.5,
    "raw": {
        "home": 0.2846, "away": 0.4687, "btts_yes": 0.561,
        "over_0.5": 0.9399, "over_1.5": 0.7723, "over_2.5": 0.5348,
        "ht_over_0.5": 0.6079, "ht_over_1.5": 0.2383,
        "expected_ht_goals": 0.9329,
        "expected_away_goals": 1.6137, "expected_home_goals": 1.204,
    },
    "calibrated": {
        "home": 0.2557, "away": 0.5032, "btts_yes": 0.5577,
        "over_1.5": 0.7868, "over_2.5": 0.5609,
        "ht_over_0.5": 0.6168,
    },
    "gates": {"leans": False, "probabilities": True},
    "ratings": {"home": {"attack": -0.131, "defence": 0.075},
                "away": {"attack": 0.264, "defence": -0.026}},
    "effective_matches": {"home": 34.6, "away": 15.6},
    "data_status": {"stale": False, "matches_behind": 0},
    "data_through": "2026-09-19",
    "computed_at": "2026-09-22T14:36:31+00:00",
}

FIXTURE = {
    "slug": SLUG,
    "home_team": "A", "away_team": "B",
    "match_date": MATCH_DATE, "time": "14:30",
    "status": "scheduled", "country": "Spain",
    "real_league_name": "Primera RFEF",
    "model_predictions": {"dc_v2": DC_V2},
}

# Same fixture, dated so it is still upcoming, so the list feed has a row to
# compare the detail payload against.
FUTURE_FIXTURE = {
    "slug": FUTURE_SLUG,
    "home_team": "C", "away_team": "D",
    "match_date": FUTURE_DATE, "time": "18:00",
    "status": "scheduled", "country": "Spain",
    "real_league_name": "Primera RFEF",
    "model_predictions": {"dc_v2": DC_V2},
}

COLLECTED_DETAIL = {
    "match": {
        "slug": SLUG,
        "match_status": "scheduled",
        "season": "2026-2027",
        "match_datetime": "2026-09-26T14:30:00+00:00",
        "label": "Matchday 5",
        "league_phase_status": "regular_season",
        "portal_link": "https://football-charts.com/spain/primera-rfef-group-1/2026-09-26-a-vs-b",
        "home_team_logo": "https://cdn.example/a.png",
        "away_team_logo": "https://cdn.example/b.png",
        "home_form": ["W", "D", "W"],
        "away_form": ["L", "W", "D"],
    },
    "attribution": "Data by football-charts.com",
}


# ---------------------------------------------------------------------------
# Stub cursor
# ---------------------------------------------------------------------------


class _StubCursor:
    """Answers the detail endpoint's queries from canned rows.

    Each marker is a distinctive fragment of one of the endpoint's SQL strings;
    the first marker found in the normalized query wins, so markers are listed
    most specific first.
    """

    def __init__(self, table):
        self._table = table
        self.queries: list[str] = []
        self._rows: list = []

    def execute(self, sql, params=None):
        normalized = " ".join(sql.split())
        self.queries.append(normalized)
        self._rows = []
        # New season lookup by league
        if "FROM league_seasons ls" in normalized and "s.start_year DESC" in normalized and "HAVING count(m.api_id)" not in normalized:
            self._rows = [{"id": 5, "season": "2026-2027", "season_state": "in_progress", "start_year": 2026, "end_year": 2027}]
            return self
        for marker, handler in self._table:
            if marker in normalized:
                self._rows = handler(params) if callable(handler) else list(handler)
                return self

    def fetchone(self):
        return self._rows[0] if self._rows else None

    def fetchall(self):
        return list(self._rows)

    def close(self):
        pass


def _match_row(api_id, match_date, home, away, home_score, away_score, home_id, away_id, game_index=1):
    return {
        "api_id": api_id,
        "match_date": date.fromisoformat(match_date),
        "kickoff_time": "15:00:00",
        "game_index": game_index,
        "home_team": home, "away_team": away,
        "home_score": home_score, "away_score": away_score,
        "home_team_id": home_id, "away_team_id": away_id,
    }


def _db_table(home_id=11, away_id=22, last_round=8):
    """Rows for a league season that has played 8 rounds before the fixture."""
    # Home side (id 11) last five: three home games plus two away, so the goal
    # sums prove the venue is taken into account.
    home_form = [
        _match_row(501, "2026-09-12", "A", "X", 2, 0, home_id, 99, game_index=8),
        _match_row(502, "2026-09-05", "Y", "A", 1, 1, 98, home_id, game_index=7),
        _match_row(503, "2026-08-29", "A", "Z", 3, 1, home_id, 97, game_index=6),
        _match_row(504, "2026-08-22", "A", "W", 1, 0, home_id, 96, game_index=5),
    ]
    away_form = [
        _match_row(601, "2026-09-19", "B", "Q", 2, 2, away_id, 88, game_index=8),
        _match_row(602, "2026-09-12", "R", "B", 0, 2, 87, away_id, game_index=7),
    ]
    return [
        ("FROM team_aliases", lambda p: [(home_id if p[0] == "A" else away_id,)]),
        ("HAVING count(m.api_id) > 0",
         [{"id": 5, "season": "2026-2027", "season_state": "in_progress"}]),
        ("max(game_index) AS last_round", [{"last_round": last_round}]),
        ("AND view = 'classic'", [
            {"position": 3, "played": 8, "won": 5, "drawn": 1, "lost": 2,
             "goals_for": 14, "goals_against": 9, "goal_difference": 5, "points": 16},
        ]),
        ("ORDER BY m.match_date DESC, m.kickoff_time DESC, m.game_index DESC",
         lambda p: home_form if p[2] == home_id else away_form),
        ("AS wins", [{"played": 3, "wins": 2, "draws": 1, "losses": 0,
                      "goals_for": 6, "goals_against": 1}]),
        ("AS played FROM matches m", [{"played": 4}]),
        ("m.api_id DESC", [
            {"api_id": 301, "match_date": date.fromisoformat("2026-02-08"),
             "season": "2025-2026", "game_index": 22, "home_score": 1,
             "away_score": 1, "home_team": "A", "away_team": "B"},
        ]),
        ("AS home_team_wins", [{"played": 3, "home_team_wins": 2, "draws": 1,
                                "goals_for": 4, "goals_against": 2}]),
    ]


@contextmanager
def _stub_cursor(table):
    yield _StubCursor(table)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def fixtures_dir(tmp_path, monkeypatch):
    directory = tmp_path / "fixtures"
    directory.mkdir()
    (directory / "primera1.json").write_text(
        json.dumps({"league": "primera1", "count": 2, "matches": [FIXTURE, FUTURE_FIXTURE]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(routers.fixtures, "FIXTURES_DIR", directory)
    # The database is deliberately unavailable: every file-only assertion below
    # must hold with no PostgreSQL at all.
    @contextmanager
    def _no_db():
        raise RuntimeError("database unavailable")

    monkeypatch.setattr(fixtures, "fetched_cursor", _no_db)
    return directory


@pytest.fixture()
def client(fixtures_dir):
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def with_detail(fixtures_dir):
    details = fixtures_dir / "details"
    details.mkdir()
    (details / f"primera1__{TAIL}.json").write_text(
        json.dumps(COLLECTED_DETAIL), encoding="utf-8"
    )
    return details


# ---------------------------------------------------------------------------
# Lookup
# ---------------------------------------------------------------------------


def test_detail_by_slug_tail(client):
    r = client.get(f"/api/v1/fixtures/primera1/{TAIL}")
    assert r.status_code == 200
    body = r.json()
    assert body["slug"] == SLUG
    assert body["match_id"] == TAIL
    assert body["league"] == "primera1"
    assert body["match_date"] == MATCH_DATE


def test_detail_by_full_slug_with_slashes(client):
    """Upstream slugs embed slashes; the :path converter has to accept them."""
    r = client.get(f"/api/v1/fixtures/primera1/{SLUG}")
    assert r.status_code == 200
    assert r.json()["slug"] == SLUG


def test_detail_accepts_json_suffix(client):
    assert client.get(f"/api/v1/fixtures/primera1/{TAIL}.json").status_code == 200


def test_detail_unknown_fixture(client):
    r = client.get("/api/v1/fixtures/primera1/1999-01-01-x-vs-y")
    assert r.status_code == 404
    assert "not found" in r.json()["detail"]


def test_detail_unknown_league(client):
    assert client.get(f"/api/v1/fixtures/nope/{TAIL}").status_code == 404


def test_detail_league_without_a_fixtures_file(client):
    """A catalog league nobody collected fixtures for has no fixture to open."""
    r = client.get("/api/v1/fixtures/premier/2026-09-26-a-vs-b")
    assert r.status_code == 404


def test_league_detail_route_still_wins(client):
    """/fixtures/{league} must not be shadowed by the detail route.

    That route serves the raw stored dump, so it is not filtered by date and
    still reports the played fixture alongside the upcoming one.
    """
    r = client.get("/api/v1/fixtures/primera1")
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 2
    assert "model_predictions" in body["matches"][0]


# ---------------------------------------------------------------------------
# Predictability
# ---------------------------------------------------------------------------


def test_predictability_exposes_the_whole_dc_v2_block(client):
    pred = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]
    assert pred["model"] == "dc_v2.0"
    assert pred["xi"] == 0.0019
    assert pred["sigma"] == 0.5
    assert pred["gates"] == {"leans": False, "probabilities": True}
    assert pred["ratings"]["home"]["attack"] == -0.131
    assert pred["effective_matches"] == {"home": 34.6, "away": 15.6}
    assert pred["data_through"] == "2026-09-19"
    assert pred["expected_goals"] == {
        "home": 1.204, "away": 1.6137, "half_time_total": 0.9329,
    }


def test_draw_probability_is_derived_from_the_remainder(client):
    probs = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["probabilities"]
    assert probs == {"home": 0.2557, "draw": 0.2411, "away": 0.5032}
    assert round(probs["home"] + probs["draw"] + probs["away"], 6) == 1.0


def test_draw_not_inferred_when_probabilities_do_not_sum_to_one():
    """A split that overflows 1 yields null, not a negative probability."""
    assert fixtures._probability_triple({"home": 0.9, "away": 0.4}) == {
        "home": 0.9, "draw": None, "away": 0.4,
    }
    # Exactly 1.0 is a real (if extreme) reading: no mass left for a draw.
    assert fixtures._probability_triple({"home": 0.9, "away": 0.1})["draw"] == 0.0


def test_draw_null_when_probabilities_missing():
    assert fixtures._probability_triple({"home": 0.5})["draw"] is None


def test_goal_lines_carry_raw_and_calibrated(client):
    lines = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["lines"]
    by_line = {row["line"]: row for row in lines}
    assert set(by_line) == {
        "over_0.5", "over_1.5", "over_2.5", "ht_over_0.5", "ht_over_1.5",
    }
    assert by_line["over_2.5"]["raw"] == 0.5348
    assert by_line["over_2.5"]["calibrated"] == 0.5609
    # A line the model did not calibrate keeps a null rather than borrowing raw.
    assert by_line["over_0.5"]["calibrated"] is None
    assert by_line["ht_over_0.5"]["scope"] == "half_time"
    assert by_line["over_1.5"]["scope"] == "full_time"
    # Full time first, then half time, each in ascending line order.
    assert [row["line"] for row in lines][:3] == ["over_0.5", "over_1.5", "over_2.5"]


def test_detail_serves_the_whole_derived_market_menu(client):
    """dc_v2 publishes no handicap, correct score or HT/FT; these are derived."""
    pred = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]
    families = {row["family"] for row in pred["markets"]}
    assert {
        "result", "double_chance", "totals", "btts",
        "asian_handicap", "team_total", "correct_score", "ht_ft",
    } <= families
    keys = {row["key"] for row in pred["markets"]}
    assert "ft.asian_handicap.-0.5_home" in keys
    assert "ft.correct_score.1_0" in keys or "ft.correct_score.1-0" in keys


def test_market_rows_carry_provenance_and_are_tagged_by_scope(client):
    rows = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["markets"]
    for row in rows:
        assert row["provenance"] in ("model", "modelled")
        assert row["scope"] in ("full_time", "half_time", "half_to_full")
        assert 0.0 <= row["probability"] <= 1.0
    # Full time is measured; half time carries the split assumption and is badged.
    assert all(row["provenance"] == "model" for row in rows if row["scope"] == "full_time")
    assert all(row["provenance"] == "modelled" for row in rows if row["scope"] != "full_time")


def test_detail_selected_chips_respect_threshold_ceiling_and_cap(client):
    selected = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["selected"]
    assert 0 < len(selected) <= 6
    for row in selected:
        assert 0.6 <= row["probability"] <= 0.95
        assert row["promotable"] is True


def test_list_feed_carries_only_the_selected_chips(client):
    """The merged feed must not carry a full market table on every row."""
    listed = client.get("/api/v1/fixtures", params={"league": "primera1"}).json()["matches"][0]
    assert "markets" not in listed["predictions"]
    assert 0 < len(listed["predictions"]["selected"]) <= 6


def test_selected_chips_agree_with_the_detail_market_table(client):
    body = client.get(f"/api/v1/fixtures/primera1/{FUTURE_TAIL}").json()
    pred = body["predictability"]
    listed = client.get("/api/v1/fixtures", params={"league": "primera1"}).json()["matches"][0]
    assert pred["selected"] == listed["predictions"]["selected"]
    by_key = {row["key"]: row for row in pred["markets"]}
    for chip in pred["selected"]:
        assert by_key[chip["key"]]["probability"] == chip["probability"]


def test_market_query_returns_only_that_markets_explanation(client):
    """The point of the query: one market's arithmetic, not the whole fixture."""
    response = client.get(f"/api/v1/fixtures/primera1/{TAIL}", params={"market": "ft.result.home"})
    body = response.json()
    assert response.status_code == 200
    assert body["league"] == "primera1"
    assert body["match_id"] == TAIL
    assert body["market_key"] == "ft.result.home"
    # The full payload is deliberately absent, so the page is not refetched.
    assert "predictability" not in body
    detail = body["market"]
    assert detail["family"] == "result"
    assert detail["settlement"]["push"] == 0.0
    assert detail["settlement"]["win"] + detail["settlement"]["lose"] == pytest.approx(1.0, abs=0.001)
    assert detail["paying_cells"] > 0
    assert detail["grid_cells"] == 81
    assert all(0.0 <= cell["probability"] <= 1.0 for cell in detail["cells"])


def test_market_explanation_reproduces_the_published_probability(client):
    """The explanation must add up to the number the chip and table already show."""
    pred = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]
    for row in pred["markets"]:
        detail = client.get(
            f"/api/v1/fixtures/primera1/{TAIL}", params={"market": row["key"]}
        ).json()["market"]
        if detail is None:
            continue
        settlement = detail["settlement"]
        # A line that can refund is quoted at its win probability, which is what
        # the table shows; the push is a partial refund, not a separate outcome.
        assert settlement["win"] == pytest.approx(row["probability"], abs=0.0002), row["key"]
        if isinstance(row.get("push"), (int, float)) and row["push"] > 0:
            assert settlement["push"] == pytest.approx(row["push"], abs=0.0002), row["key"]


def test_quarter_line_explains_the_half_stake_split(client):
    """A quarter line settles on a scoreline in two ways; both must be labelled."""
    rows = {
        row["key"]: row
        for row in client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["markets"]
    }
    key = next(k for k in rows if k.startswith("ft.asian_handicap.") and k.endswith("_home")
               and rows[k].get("line") == -0.25)
    detail = client.get(f"/api/v1/fixtures/primera1/{TAIL}", params={"market": key}).json()["market"]
    assert detail["settlement"]["push"] > 0
    # Every draw is a level result, so every drawn scoreline is the cell where
    # the two half-stakes disagree: the model is paid half and refunded half.
    split = [c for c in detail["cells"] if "+" in c["outcome"]]
    assert len(split) == 9
    assert {c["outcome"] for c in split} == {"push+lose"}
    assert all(c["home_goals"] == c["away_goals"] for c in split)
    # A split cell is measured against the push it feeds, and only half of a
    # quarter-line cell pushes, so the share is half the cell over the push total.
    assert split[0]["share"] == pytest.approx(
        split[0]["probability"] / 2 / detail["settlement"]["push"], abs=0.001
    )
    # Shares are shares of an outcome, so each set has to add up.
    assert sum(c["share"] for c in split) == pytest.approx(1.0, abs=0.01)
    # Nothing outside the draw splits.
    assert [c for c in detail["cells"] if c not in split] == [
        c for c in detail["cells"] if c["outcome"] in ("win", "lose")
    ]


def test_market_cells_only_ever_cover_the_paying_sides(client):
    """No cell may be listed that would not have paid the bet."""
    detail = client.get(
        f"/api/v1/fixtures/primera1/{TAIL}", params={"market": "ft.totals.over_2.5"}
    ).json()["market"]
    for cell in detail["cells"]:
        home, away = (int(part) for part in cell["score"].split("-"))
        assert home + away > 2.5
    assert detail["paying_cells"] == len(
        [c for c in detail["cells"]]  # every listed cell is a paying cell
    )


def test_half_time_full_time_market_explains_its_factors(client):
    """HT/FT is a product of two 1X2 splits, so it has factors and no scorelines."""
    keys = [
        row["key"]
        for row in client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["predictability"]["markets"]
        if row["family"] == "ht_ft"
    ]
    assert keys
    detail = client.get(
        f"/api/v1/fixtures/primera1/{TAIL}", params={"market": keys[0]}
    ).json()["market"]
    assert detail["factors"]["half_time"]["home"] > 0
    assert detail["factors"]["full_time"]["home"] > 0
    assert detail["cells"] == []


def test_unknown_market_key_is_a_404(client):
    response = client.get(f"/api/v1/fixtures/primera1/{TAIL}", params={"market": "ft.result.nope"})
    assert response.status_code == 404
    assert "ft.result.nope" in response.json()["detail"]


def test_market_explanation_without_a_model_block_is_a_404(tmp_path, monkeypatch):
    """A fixture with no prediction has no markets, so no key can resolve."""
    directory = tmp_path / "fixtures"
    directory.mkdir()
    (directory / "primera1.json").write_text(
        json.dumps({"league": "primera1", "matches": [{**FIXTURE, "model_predictions": {}}]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", directory)
    with TestClient(app) as client:
        response = client.get(f"/api/v1/fixtures/primera1/{TAIL}", params={"market": "ft.result.home"})
    assert response.status_code == 404


def test_detail_route_without_a_market_query_is_unchanged(client):
    """The page payload must not regress: still the full fixture, no market key."""
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert "market" not in body
    assert "market_key" not in body
    assert body["predictability"]["markets"]


def test_market_table_and_selection_are_empty_without_lambdas(tmp_path, monkeypatch):
    """No invented zeros: a block without goal expectations serves no markets."""
    block = json.loads(json.dumps(DC_V2))
    del block["raw"]["expected_home_goals"]
    del block["raw"]["expected_away_goals"]
    directory = tmp_path / "fixtures"
    directory.mkdir()
    (directory / "primera1.json").write_text(
        json.dumps({"league": "primera1", "matches": [
            {**FUTURE_FIXTURE, "model_predictions": {"dc_v2": block}},
        ]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", directory)
    with TestClient(app) as client:
        pred = client.get(f"/api/v1/fixtures/primera1/{FUTURE_TAIL}").json()["predictability"]
        listed = client.get("/api/v1/fixtures", params={"league": "primera1"}).json()["matches"][0]
    # The published numbers are still served; only the derived menu is empty.
    assert pred["markets"] == []
    assert pred["selected"] == []
    assert pred["raw"]["btts_yes"] == 0.561
    assert listed["predictions"]["selected"] == []


def test_summary_matches_the_list_feed(client):
    """A detail view must never disagree with the row it was opened from."""
    detail = client.get(f"/api/v1/fixtures/primera1/{FUTURE_TAIL}").json()
    listed = client.get("/api/v1/fixtures", params={"league": "primera1"}).json()["matches"][0]
    assert detail["predictability"]["summary"] == listed["predictions"]


def test_predictability_null_without_a_model_block(tmp_path, monkeypatch):
    directory = tmp_path / "fixtures"
    directory.mkdir()
    (directory / "primera1.json").write_text(
        json.dumps({"league": "primera1", "matches": [{**FIXTURE, "model_predictions": {}}]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", directory)
    with TestClient(app) as client:
        body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["predictability"] is None
    assert body["match_date"] == MATCH_DATE


# ---------------------------------------------------------------------------
# Kickoff metadata, logos, collected detail
# ---------------------------------------------------------------------------


def test_kickoff_metadata_from_the_collected_detail(client, with_detail):
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["detail_collected"] is True
    assert body["kickoff"]["match_datetime"] == "2026-09-26T14:30:00+00:00"
    assert body["kickoff"]["label"] == "Matchday 5"
    assert body["kickoff"]["league_phase_status"] == "regular_season"
    assert body["kickoff"]["portal_link"].startswith("https://football-charts.com/")
    assert body["season"] == "2026-2027"


def test_teams_carry_logos(client, with_detail):
    teams = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["teams"]
    assert teams["home"]["logo"] == "https://cdn.example/a.png"
    assert teams["away"]["logo"] == "https://cdn.example/b.png"
    assert teams["home"]["name"] == "A"


def test_missing_detail_file_degrades(client):
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["detail_collected"] is False
    assert body["teams"]["home"]["logo"] is None
    # The fixtures file still supplies the plain kickoff time.
    assert body["kickoff"]["time"] == "14:30"
    assert body["predictability"] is not None


def test_corrupt_detail_file_is_ignored(client, with_detail):
    (with_detail / f"primera1__{TAIL}.json").write_text("{not json", encoding="utf-8")
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["detail_collected"] is False
    assert body["predictability"] is not None


# ---------------------------------------------------------------------------
# Degradation without a database
# ---------------------------------------------------------------------------


def test_database_sections_are_null_without_history(client):
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["matchday"] is None
    assert body["pre_match"] is None
    assert body["head_to_head"] is None
    assert body["season"] is None
    assert body["standings"] == {"home": None, "away": None}
    # ... and the file-derived sections are untouched.
    assert body["predictability"]["model"] == "dc_v2.0"
    assert body["match_date"] == MATCH_DATE


def test_missing_database_url_does_not_escape_the_request(fixtures_dir, monkeypatch):
    """db_common.get_conn() reports an absent DATABASE_URL with sys.exit()."""

    @contextmanager
    def _sys_exit():
        raise SystemExit("DATABASE_URL not set")
        yield  # pragma: no cover

    monkeypatch.setattr(fixtures, "fetched_cursor", _sys_exit)
    with TestClient(app, raise_server_exceptions=False) as client:
        r = client.get(f"/api/v1/fixtures/primera1/{TAIL}")
    assert r.status_code == 200
    assert r.json()["matchday"] is None


# ---------------------------------------------------------------------------
# Database-derived sections
# ---------------------------------------------------------------------------


@pytest.fixture()
def db_client(fixtures_dir, monkeypatch):
    monkeypatch.setattr(fixtures, "fetched_cursor", lambda: _stub_cursor(_db_table()))
    with TestClient(app) as c:
        yield c


def test_matchday_is_the_round_after_the_last_played(db_client):
    assert db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["matchday"] == 9


def test_matchday_of_a_season_opener(monkeypatch, fixtures_dir):
    table = _db_table()
    table[2] = ("max(game_index) AS last_round", [{"last_round": None}])
    monkeypatch.setattr(fixtures, "fetched_cursor", lambda: _stub_cursor(table))
    with TestClient(app) as client:
        assert client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["matchday"] == 1


def test_season_and_table_come_from_the_database(db_client):
    body = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["season"] == "2026-2027"
    assert body["season_state"] == "in_progress"
    assert body["standings"]["home"]["position"] == 3
    assert body["standings"]["home"]["points"] == 16


def test_form_uses_the_team_perspective_not_the_home_perspective(db_client):
    """Regression: goals must be summed from the team's own side of the score.

    Team A is away at Y in one of its last four, so a naive sum of `home_score`
    would report the opponent's goal as A's.
    """
    form = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["teams"]["home"]["form"]
    assert [r["date"] for r in form] == ["2026-09-12", "2026-09-05", "2026-08-29", "2026-08-22"]
    assert [r["team_result"] for r in form] == ["W", "D", "W", "W"]


def test_pre_match_panel_groups_venue_aware_columns(db_client):
    pre = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["pre_match"]
    assert pre is not None
    assert pre["game_index"] == 9
    assert pre["season"] == "2026-2027"
    groups = pre["groups"]
    # Home side's venue columns are the *_home_* ones, away side's the *_away_*.
    assert groups["venue"]["home_team_home_win_rate"]["value"] == pytest.approx(0.6667, abs=1e-3)
    assert groups["venue"]["away_team_away_win_rate"]["value"] == pytest.approx(0.6667, abs=1e-3)
    assert groups["form_last_5"]["home_team_points_last_5"]["value"] == 10
    assert groups["rest"]["home_rest_days"]["value"] == 14
    assert groups["rest"]["rest_days_difference"]["value"] == 7
    assert groups["load"]["away_team_games_before"]["value"] == 4
    assert groups["table_before_match"]["home_position_before_match"]["value"] == 3
    assert groups["table_before_match"]["position_difference"]["value"] == 0
    # The reused panel renders its caption from these, so they must be present.
    assert pre["home_team"] == "A"
    assert pre["away_team"] == "B"
    assert pre["home_team_id"] == 11
    assert pre["away_team_id"] == 22
    assert pre["group_labels"]["venue"] == "Venue split"


def test_pre_match_uses_dataset_column_names(db_client):
    """The panel is only reusable while its keys match the real dataset."""
    dataset_path = (
        Path(__file__).resolve().parents[2] / "ml" / "datasets" / "match_result_dataset.json"
    )
    if not dataset_path.exists():
        pytest.skip("dataset not built; run ml/build_dataset.py")
    dataset = json.loads(dataset_path.read_bytes())
    columns = set(dataset[0])
    pre = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["pre_match"]
    surfaced = {
        cell_key
        for group in pre["groups"].values()
        for cell_key in group
    }
    assert surfaced, "expected pre-match features to be surfaced"
    assert surfaced <= columns, surfaced - columns


def test_rest_days_measured_from_the_last_match(db_client):
    teams = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["teams"]
    # A last played 2026-09-12, B last played 2026-09-19; fixture is 2026-09-26.
    assert teams["home"]["rest_days"] == 14
    assert teams["away"]["rest_days"] == 7


def test_head_to_head_is_bounded_by_the_fixture_date(db_client):
    h2h = db_client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["head_to_head"]
    assert h2h["summary"]["played"] == 3
    assert h2h["summary"]["home_team_wins"] == 2
    assert h2h["summary"]["draws"] == 1
    assert h2h["summary"]["away_team_wins"] == 0
    assert h2h["truncated"] is True
    assert h2h["matches"][0]["api_id"] == 301
    # Same envelope as /matches/{api_id}/insights, so one component renders both.
    assert set(h2h) == {"limit", "summary", "truncated", "matches"}


def test_head_to_head_absent_for_a_first_meeting(fixtures_dir, monkeypatch):
    table = _db_table()
    table[-1] = ("AS home_team_wins", [{"played": 0}])
    table[-2] = ("m.api_id DESC", [])
    monkeypatch.setattr(fixtures, "fetched_cursor", lambda: _stub_cursor(table))
    with TestClient(app) as client:
        h2h = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()["head_to_head"]
    assert h2h["matches"] == []
    assert h2h["summary"] is None
    assert h2h["truncated"] is False


def test_unresolved_teams_skip_history_but_keep_the_fixture(fixtures_dir, monkeypatch):
    """An unknown team must not take the whole page down with it."""
    table = [entry for entry in _db_table() if entry[0] != "FROM team_aliases"]
    table.insert(0, ("FROM team_aliases", []))
    monkeypatch.setattr(fixtures, "fetched_cursor", lambda: _stub_cursor(table))
    with TestClient(app) as client:
        body = client.get(f"/api/v1/fixtures/primera1/{TAIL}").json()
    assert body["pre_match"] is None
    assert body["head_to_head"] is None
    # Matchday and the table do not need either team resolved.
    assert body["matchday"] == 9
    assert body["predictability"]["model"] == "dc_v2.0"


# ---------------------------------------------------------------------------
# Storage conventions shared with the collector
# ---------------------------------------------------------------------------


def test_detail_filename_matches_the_collector():
    """The router and fetch_fixture_details.py must name files identically."""
    sys.path.insert(0, str(BACKEND / "scripts"))
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "fetch_fixture_details", BACKEND / "scripts" / "fetch_fixture_details.py"
    )
    collector = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(collector)
    except SystemExit:
        pytest.skip("FOOTBALL_CHARTS_API_KEY not configured")

    for slug in (SLUG, "a/b/c", "no-slash", "trailing/"):
        assert fixtures.slug_tail(slug) == collector.slug_tail(slug)
        assert fixtures.detail_file("premier", slug) == collector.DETAILS_DIR / (
            f"premier__{collector.slug_tail(slug)}.json"
        )


def test_detail_still_serves_a_fixture_that_has_been_played(client):
    """Filtering is a list-feed concern; a past fixture must stay reachable.

    Opening the page for a match that kicked off yesterday is a normal thing to
    do, and the prediction block it was opened from has not expired.
    """
    assert MATCH_DATE < date.today().isoformat()   # the sample really is past
    body = client.get(f"/api/v1/fixtures/primera1/{TAIL}")
    assert body.status_code == 200
    assert body.json()["match_date"] == MATCH_DATE
    assert body.json()["predictability"]["markets"]
    # ...but it is not advertised as upcoming.
    listed = client.get("/api/v1/fixtures", params={"league": "primera1"}).json()
    assert [m["slug"] for m in listed["matches"]] == [FUTURE_SLUG]
