"""Tests for the fixtures API (backend/apps/routers/fixtures.py).

Runs against a temporary fixtures directory (no database, no live server),
so the endpoints are exercised exactly as the dashboard consumes them.
"""
from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.common as common  # noqa: E402
from apps import routers  # noqa: E402
from apps.main import app  # noqa: E402

# Fixture dates are relative to today on purpose. The list endpoint hides
# anything already played, so hardcoded dates would turn these samples into
# "played" matches the day after they were written.
TODAY = date.today()
SOON = (TODAY + timedelta(days=1)).isoformat()      # A vs B
LATER = (TODAY + timedelta(days=2)).isoformat()     # C vs D
FAR = (TODAY + timedelta(days=5)).isoformat()       # E vs F

SAMPLE = {
    "league": "primera1",
    "count": 2,
    "matches": [
        {
            "slug": "spain/primera-rfef-group-1/2026-09-26-a-vs-b",
            "home_team": "A", "away_team": "B",
            "match_date": SOON, "time": "14:30",
            "status": "scheduled", "country": "Spain",
            "model_predictions": {
                "dc_v2": {
                    "calibrated": {"home": 0.52, "away": 0.17, "btts_yes": 0.47,
                                   "over_1.5": 0.70, "over_2.5": 0.44, "over_3.5": 0.24},
                    "raw": {"expected_home_goals": 1.57, "expected_away_goals": 0.84},
                    "computed_at": "2026-09-22T00:00:00+00:00",
                    "data_through": "2026-09-20",
                }
            },
        },
        {
            "slug": "spain/primera-rfef-group-1/2026-09-27-c-vs-d",
            "home_team": "C", "away_team": "D",
            "match_date": LATER, "time": "16:15",
            "status": "scheduled", "country": "Spain",
            "model_predictions": {
                "dc_v2": {
                    "calibrated": {"home": 0.90, "away": 0.03},
                }
            },
        },
    ],
}


@pytest.fixture()
def fixtures_client(tmp_path, monkeypatch):
    fixtures_dir = tmp_path / "fixtures"
    fixtures_dir.mkdir()
    (fixtures_dir / "primera1.json").write_text(
        json.dumps(SAMPLE), encoding="utf-8"
    )
    ((fixtures_dir / "spain1.json")).write_text(
        json.dumps({
            "league": "spain1", "count": 1,
            "matches": [{
                "slug": "spain/laliga/2026-10-01-e-vs-f",
                "home_team": "E", "away_team": "F",
                "match_date": FAR, "time": "20:00",
                "status": "scheduled", "country": "Spain",
                "model_predictions": {"dc_v2": {"calibrated": {"home": 0.60, "away": 0.10}}},
            }],
        }),
        encoding="utf-8",
    )
    monkeypatch.setattr(routers.fixtures, "FIXTURES_DIR", fixtures_dir)
    with TestClient(app) as client:
        yield client


def test_merged_sorted_by_confidence(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"limit": 10})
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 3
    confidences = [m["predictions"]["confidence"] for m in body["matches"]]
    assert confidences == sorted(confidences, reverse=True)
    first = body["matches"][0]
    assert first["home_team"] == "C"
    assert first["predictions"]["home"] == 0.90


def test_merged_sorted_by_date(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"sort": "date", "limit": 10})
    dates = [m["match_date"] for m in r.json()["matches"]]
    assert dates == sorted(dates)


def test_league_filter(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"league": "primera1"})
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 2
    assert {m["league"] for m in body["matches"]} == {"primera1"}


def test_rows_carry_the_league_name_not_just_the_slug(fixtures_client):
    # The dump on disk has no league name of its own, so the API resolves it
    # from the catalog: a reader must never have to decode "primera1".
    r = fixtures_client.get("/api/v1/fixtures", params={"limit": 10})
    body = r.json()
    assert body["league_name"] is None  # unscoped feed, so no league to name
    for m in body["matches"]:
        assert m["league_name"] == common.league_name(m["league"])
        assert m["league_name"] != m["league"]


def test_scoped_feed_names_its_league(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"league": "primera1"})
    body = r.json()
    assert body["league_name"] == "Primera RFEF - Group 1"
    assert all(m["league_name"] == "Primera RFEF - Group 1" for m in body["matches"])


def test_single_league_feed_names_its_league(fixtures_client):
    body = fixtures_client.get("/api/v1/fixtures/primera1").json()
    assert body["league_name"] == "Primera RFEF - Group 1"


def test_unknown_league(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures", params={"league": "nope"})
    assert r.status_code == 404


def test_league_full_payload(fixtures_client):
    r = fixtures_client.get("/api/v1/fixtures/primera1")
    assert r.status_code == 200
    body = r.json()
    assert body["league"] == "primera1"
    assert "model_predictions" in body["matches"][0]


def test_empty_fixtures_dir(tmp_path, monkeypatch):
    import apps.routers.fixtures as fixtures
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", tmp_path / "none")
    with TestClient(app) as client:
        r = client.get("/api/v1/fixtures")
        assert r.status_code == 200
        assert r.json()["matches"] == []

# ---------------------------------------------------------------------------
# "Upcoming" means not yet played
#
# The upstream feed is a snapshot whose `status` field never leaves
# "scheduled", so a dump collected last week still lists matches that have since
# been kicked off. The date is the only trustworthy signal, so the list endpoint
# filters on it. These cover that boundary directly.
# ---------------------------------------------------------------------------


def _write(tmp_path, name, matches):
    d = tmp_path / "fixtures"
    d.mkdir(exist_ok=True)
    (d / f"{name}.json").write_text(
        json.dumps({"league": name, "count": len(matches), "matches": matches}),
        encoding="utf-8",
    )
    return d


def _client(tmp_path, monkeypatch, name, matches):
    import apps.routers.fixtures as fixtures
    _write(tmp_path, name, matches)
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", tmp_path / "fixtures")
    return TestClient(app)


def _match(slug, match_date, home="A", away="B"):
    return {
        "slug": f"spain/x/{slug}",
        "home_team": home, "away_team": away,
        "match_date": match_date, "time": "12:00",
        "status": "scheduled",
        "model_predictions": {"dc_v2": {"calibrated": {"home": 0.5, "away": 0.2}}},
    }


def test_played_fixtures_are_not_listed_as_upcoming(tmp_path, monkeypatch):
    past = (TODAY - timedelta(days=1)).isoformat()
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("2026-01-01-old", past, home="Old"),
        _match("2026-01-02-new", SOON, home="New"),
    ])
    with client:
        body = client.get("/api/v1/fixtures").json()
    assert body["count"] == 1
    assert [m["home_team"] for m in body["matches"]] == ["New"]


def test_todays_fixture_is_still_upcoming(tmp_path, monkeypatch):
    # Date-only comparison: a match later today must not disappear, since the
    # feed carries no reliable kickoff timezone to compare the clock against.
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("today", TODAY.isoformat()),
    ])
    with client:
        assert client.get("/api/v1/fixtures").json()["count"] == 1


def test_yesterdays_fixture_is_gone(tmp_path, monkeypatch):
    yesterday = (TODAY - timedelta(days=1)).isoformat()
    client = _client(tmp_path, monkeypatch, "primera1", [_match("yest", yesterday)])
    with client:
        body = client.get("/api/v1/fixtures").json()
    assert body["count"] == 0
    assert body["matches"] == []
    assert body["first_date"] is None


def test_first_date_reports_the_soonest_fixture(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("d4", (TODAY + timedelta(days=4)).isoformat()),
        _match("d1", SOON),
        _match("d2", LATER),
    ])
    with client:
        assert client.get("/api/v1/fixtures").json()["first_date"] == SOON


def test_filter_applies_to_both_sort_orders(tmp_path, monkeypatch):
    past = (TODAY - timedelta(days=3)).isoformat()
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("old", past, home="Old"), _match("new", SOON, home="New"),
    ])
    with client:
        for sort in ("date", "confidence"):
            body = client.get("/api/v1/fixtures", params={"sort": sort}).json()
            assert [m["home_team"] for m in body["matches"]] == ["New"], sort


def test_rows_without_a_parsable_date_are_kept(tmp_path, monkeypatch):
    # Dropping these would silently hide a fixture; keeping them is the safer
    # failure, and the row simply sorts last.
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("nodate", None, home="NoDate"),
        _match("baddate", "not-a-date", home="BadDate"),
        _match("real", SOON, home="Real"),
    ])
    with client:
        body = client.get("/api/v1/fixtures", params={"sort": "date"}).json()
    assert body["count"] == 3
    assert {m["home_team"] for m in body["matches"]} == {"NoDate", "BadDate", "Real"}
    assert body["first_date"] == SOON


def test_date_min_returns_the_whole_stored_snapshot(tmp_path, monkeypatch):
    past = (TODAY - timedelta(days=9)).isoformat()
    import apps.routers.fixtures as fixtures
    _write(tmp_path, "primera1", [_match("old", past), _match("new", SOON)])
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", tmp_path / "fixtures")
    assert len(fixtures.fixture_rows(today=date.min)) == 2
    assert len(fixtures.fixture_rows(today=TODAY)) == 1


def test_limit_counts_upcoming_only(tmp_path, monkeypatch):
    past = (TODAY - timedelta(days=2)).isoformat()
    client = _client(tmp_path, monkeypatch, "primera1", [
        _match("p1", past), _match("p2", past), _match("n1", SOON), _match("n2", LATER),
    ])
    with client:
        body = client.get("/api/v1/fixtures", params={"limit": 1}).json()
    # `total` counts every upcoming fixture, `count`/`returned` only this slice —
    # the same split /matches/{id} uses, so a client can page either feed.
    assert body["total"] == 2
    assert body["count"] == body["returned"] == 1
    assert body["limit"] == 1
    assert body["has_more"] is True
    assert len(body["matches"]) == 1


# ---------------------------------------------------------------------------
# Paging, date windows and the confidence floor
#
# The stored snapshot is a weekend burst: a few hundred fixtures spread over a
# handful of days. Flat-slicing that into one list sorted by confidence hides
# everything past the first page and makes the page boundary move as new matches
# are collected, so the list is paged by date and can be narrowed to a day.
# ---------------------------------------------------------------------------


def _week():
    """Six upcoming fixtures, two per day across the next three days."""
    return [
        _match(f"d{day}-{n}", (TODAY + timedelta(days=day)).isoformat(), home=f"D{day}-{n}")
        for day in (1, 2, 3)
        for n in (1, 2)
    ]


def test_offset_pages_through_without_repeating_or_skipping(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    seen = []
    with client:
        for offset in (0, 2, 4):
            body = client.get(
                "/api/v1/fixtures", params={"sort": "date", "limit": 2, "offset": offset}
            ).json()
            assert body["total"] == 6
            assert body["has_more"] is (offset < 4)
            seen += [m["slug"] for m in body["matches"]]
    assert len(set(seen)) == 6


def test_date_sort_is_stable_across_pages(tmp_path, monkeypatch):
    """Confidence order would reshuffle between pages and double up fixtures."""
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        first = client.get("/api/v1/fixtures", params={"sort": "date", "limit": 3}).json()
        second = client.get(
            "/api/v1/fixtures", params={"sort": "date", "limit": 3, "offset": 3}
        ).json()
    assert [m["match_date"] for m in first["matches"]] <= [m["match_date"] for m in second["matches"]]
    assert not ({m["slug"] for m in first["matches"]} & {m["slug"] for m in second["matches"]})


def test_paging_past_the_end_returns_an_empty_page_not_an_error(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        body = client.get("/api/v1/fixtures", params={"limit": 2, "offset": 99}).json()
    assert body["matches"] == []
    assert body["returned"] == 0
    assert body["total"] == 6
    assert body["has_more"] is False


def test_dates_lists_every_day_present_for_grouping(tmp_path, monkeypatch):
    """The UI groups rows by day, so it needs the day list up front."""
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        body = client.get("/api/v1/fixtures", params={"sort": "date"}).json()
    assert body["dates"] == [
        (TODAY + timedelta(days=d)).isoformat() for d in (1, 2, 3)
    ]
    assert body["first_date"] == body["dates"][0]
    assert body["last_date"] == body["dates"][-1]


def test_day_counts_cover_the_whole_filtered_set_not_just_the_page(tmp_path, monkeypatch):
    """A page boundary can split a day, and the UI has to be able to say so.

    Counting only the rows on the page would make a 40-match day that got cut
    at 10 look like a 10-match day.
    """
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        body = client.get(
            "/api/v1/fixtures", params={"sort": "date", "limit": 1}
        ).json()
    assert body["returned"] == 1
    assert body["day_counts"] == {
        (TODAY + timedelta(days=d)).isoformat(): 2 for d in (1, 2, 3)
    }
    # The single row on the page is a fragment of a two-match day.
    assert body["day_counts"][body["matches"][0]["match_date"]] == 2


def test_day_counts_follow_the_filters(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    day2 = (TODAY + timedelta(days=2)).isoformat()
    with client:
        body = client.get(
            "/api/v1/fixtures", params={"from_date": day2, "to_date": day2}
        ).json()
    assert body["day_counts"] == {day2: 2}
    assert sum(body["day_counts"].values()) == body["total"]


def test_date_window_keeps_only_the_days_asked_for(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    day2 = (TODAY + timedelta(days=2)).isoformat()
    with client:
        body = client.get(
            "/api/v1/fixtures", params={"from_date": day2, "to_date": day2}
        ).json()
    assert body["total"] == 2
    assert body["dates"] == [day2]
    assert {m["match_date"] for m in body["matches"]} == {day2}


def test_an_open_ended_window_only_bounds_one_side(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    day2 = (TODAY + timedelta(days=2)).isoformat()
    with client:
        forward = client.get("/api/v1/fixtures", params={"from_date": day2}).json()
        backward = client.get("/api/v1/fixtures", params={"to_date": day2}).json()
    assert forward["total"] == 4
    assert backward["total"] == 4


def test_a_date_window_forces_date_order(tmp_path, monkeypatch):
    """Confidence order across a single day is meaningless noise to a reader."""
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    day2 = (TODAY + timedelta(days=2)).isoformat()
    with client:
        body = client.get(
            "/api/v1/fixtures", params={"from_date": day2, "to_date": day2, "sort": "confidence"}
        ).json()
    # Asked for confidence order, got date order, and the response says so
    # rather than echoing the request back and letting a caller assume otherwise.
    assert body["sort"] == "date"
    assert [m["home_team"] for m in body["matches"]] == ["D2-1", "D2-2"]


def test_a_malformed_window_is_rejected_rather_than_silently_ignored(tmp_path, monkeypatch):
    """A bad query param is a client error, not a filter that quietly does nothing.

    This reverses an earlier decision to ignore an unparsable window. Ignoring it
    answered "here is everything" while the caller believed they had filtered,
    which is worse than an error. The leniency that is still correct lives on the
    other side of the boundary: a stored fixture row with no usable date, which
    cannot satisfy a window and is dropped by the window rather than the
    request. See test_date_less_rows_are_dropped_by_a_window_but_kept_without_one.
    """
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        r = client.get("/api/v1/fixtures", params={"from_date": "not-a-date"})
    assert r.status_code == 422


def test_an_inverted_window_is_rejected(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        r = client.get(
            "/api/v1/fixtures",
            params={
                "from_date": (TODAY + timedelta(days=5)).isoformat(),
                "to_date": TODAY.isoformat(),
            },
        )
    assert r.status_code == 422
    assert "after" in r.json()["detail"]


def test_date_less_rows_are_dropped_by_a_window_but_kept_without_one(tmp_path, monkeypatch):
    """A window is a claim about dates; a row with no date cannot satisfy it."""
    client = _client(tmp_path, monkeypatch, "primera1", [
        *_week(), _match("nodate", None, home="NoDate"),
    ])
    with client:
        everything = client.get("/api/v1/fixtures").json()
        windowed = client.get(
            "/api/v1/fixtures", params={"from_date": (TODAY + timedelta(days=1)).isoformat()}
        ).json()
    assert everything["total"] == 7
    assert windowed["total"] == 6
    assert "NoDate" not in {m["home_team"] for m in windowed["matches"]}


def test_min_confidence_keeps_only_fixtures_the_model_is_sure_about(tmp_path, monkeypatch):
    def confident(name, prob):
        return {
            "slug": f"spain/x/{name}",
            "home_team": name, "away_team": "B",
            "match_date": SOON, "time": "12:00", "status": "scheduled",
            "model_predictions": {"dc_v2": {"calibrated": {"home": prob, "away": 1 - prob}}},
        }

    client = _client(tmp_path, monkeypatch, "primera1", [
        confident("Sure", 0.95), confident("Edge", 0.55),
    ])
    with client:
        # confidence is the model's strongest side, so 0.6 keeps only Sure.
        body = client.get("/api/v1/fixtures", params={"min_confidence": 0.6}).json()
    assert body["total"] == 1
    assert body["matches"][0]["home_team"] == "Sure"
    assert body["matches"][0]["predictions"]["confidence"] >= 0.6
    assert body["min_confidence"] == 0.6


def test_min_confidence_of_zero_keeps_everything(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    with client:
        body = client.get("/api/v1/fixtures", params={"min_confidence": 0}).json()
    assert body["total"] == 6


def test_a_row_with_no_prediction_does_not_pass_the_confidence_floor(tmp_path, monkeypatch):
    client = _client(tmp_path, monkeypatch, "primera1", [
        {**_match("bare", SOON), "model_predictions": {}},
    ])
    with client:
        assert client.get("/api/v1/fixtures", params={"min_confidence": 0.1}).json()["total"] == 0


def test_filters_narrow_total_before_paging(tmp_path, monkeypatch):
    """total must describe the filtered set, or paging cannot be trusted."""
    client = _client(tmp_path, monkeypatch, "primera1", _week())
    day2 = (TODAY + timedelta(days=2)).isoformat()
    with client:
        body = client.get(
            "/api/v1/fixtures", params={"from_date": day2, "to_date": day2, "limit": 1}
        ).json()
    assert body["total"] == 2
    assert body["returned"] == 1
    assert body["has_more"] is True
    assert body["from_date"] == day2


def test_the_plain_list_still_leads_with_the_models_best_picks(tmp_path, monkeypatch):
    """The unfiltered default is a short "best picks" read, not a list to walk."""
    def confident(home, prob):
        return {
            "slug": f"spain/x/{home}",
            "home_team": home, "away_team": "B",
            "match_date": SOON, "time": "12:00", "status": "scheduled",
            "model_predictions": {"dc_v2": {"calibrated": {"home": prob, "away": 1 - prob}}},
        }

    client = _client(tmp_path, monkeypatch, "primera1", [
        confident("Weak", 0.4), confident("Strong", 0.95),
    ])
    with client:
        body = client.get("/api/v1/fixtures").json()
    assert body["sort"] == "confidence"
    assert [m["home_team"] for m in body["matches"]] == ["Strong", "Weak"]


def test_dashboard_upcoming_excludes_played(tmp_path, monkeypatch):
    past = (TODAY - timedelta(days=1)).isoformat()
    import apps.routers.fixtures as fixtures
    _write(tmp_path, "primera1", [_match("old", past), _match("new", SOON)])
    monkeypatch.setattr(fixtures, "FIXTURES_DIR", tmp_path / "fixtures")
    with TestClient(app) as client:
        meta = client.get("/api/v1/dashboard").json()["meta"]
    assert meta["n_upcoming"] == 1
