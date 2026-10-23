"""Tests for the dashboard API (backend/apps/routers/dashboard.py).

The region buckets and top-league ranking are pure (no cursor needed) and are
unit-tested against the real LEAGUE_CONFIG. The DB-backed end-to-end route is
tested when PostgreSQL is reachable, otherwise skipped.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.common as common  # noqa: E402
from apps.routers import dashboard  # noqa: E402


def test_top_leagues_ranks_by_match_count():
    counts = {"germany1": 5, "premier": 100, "spain1": 50}
    rows = dashboard._top_leagues(None, counts)
    slugs = [r["slug"] for r in rows]
    assert slugs[:3] == ["premier", "spain1", "germany1"]
    assert rows[0]["region"] == "europe"
    leagueless = dashboard._top_leagues(None, {})
    # Still returns catalog leagues ranked, but every one has zero matches.
    assert leagueless == [] or all(r["matches"] == 0 for r in leagueless)


def test_leagues_by_region_has_all_buckets():
    buckets = dashboard._leagues_by_region(None, {})
    assert set(buckets) == {"europe", "asia", "america", "other"}
    all_leagues = sum(len(v) for v in buckets.values())
    assert all_leagues == len(common.LEAGUE_CONFIG)


def test_dashboard_endpoint_dict_matches_display_slug():
    # Region tag on the listing and on detail must agree.
    listing = common.league_listing()
    for item in listing:
        meta = common.LEAGUE_CONFIG[item["slug"]]
        assert item["region"] == common.regions.league_region(meta["country"] or "")


def _db_reachable() -> bool:
    try:
        from apps.deps import get_conn
    except Exception:
        return False
    try:
        conn = get_conn()
        conn.close()
        return True
    except Exception:
        return False


@pytest.mark.skipif(not _db_reachable(), reason="PostgreSQL not reachable")
def test_dashboard_endpoint():
    from apps.main import app

    with TestClient(app) as client:
        r = client.get("/api/v1/dashboard")
        assert r.status_code == 200
        body = r.json()
        assert set(body["leagues_by_region"]) == {"europe", "asia", "america", "other"}
        assert isinstance(body["top_leagues"], list)
        assert isinstance(body["top_clubs"], list)
        assert isinstance(body["recent_matches"], list)
        assert isinstance(body["upcoming_matches"], list)


@pytest.mark.skipif(not _db_reachable(), reason="PostgreSQL not reachable")
def test_recent_matches_rows_carry_no_derived_region():
    """`recent_matches` is reused here to build the dashboard's recent list.

    It used to attach a `region` to every row. Nothing read it — the dashboard's
    own buckets come from `_leagues_by_region`, which derives its own — so it was
    dead weight on the hottest read in the app. This guards the removal: a row
    that grew a derived field again would silently re-couple the two.
    """
    from apps.main import app

    with TestClient(app) as client:
        body = client.get("/api/v1/matches/recent", params={"limit": 5}).json()
        rows = body["matches"]
        assert rows, "expected collected matches"
        for row in rows:
            assert "region" not in row
            # `country` is the raw field a client would derive it from.
            assert "country" in row

        # The dashboard's buckets are unaffected by the row shape.
        dashboard_body = client.get("/api/v1/dashboard").json()
        assert set(dashboard_body["leagues_by_region"]) == {"europe", "asia", "america", "other"}
