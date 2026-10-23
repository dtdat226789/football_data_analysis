"""Unit tests for the league-aware season helpers in db_common (no DB, no network).

These are the helpers the threaded ETL steps use to derive per-league season sets
(etl_01_registry, etl_02_identity, etl_03_matches_standings, validate_db,
validate_raw_to_db).
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import scripts.db_common as db_common

PREMIER_SEASONS = [
    "2020-2021",
    "2021-2022",
    "2022-2023",
    "2023-2024",
    "2024-2025",
    "2025-2026",
    "2026-2027",
]


# ── _season_sort_key ────────────────────────────────────────────────────────
def test_season_sort_key_range_and_single_year():
    assert db_common._season_sort_key("2025-2026") == (2025, 2026)
    assert db_common._season_sort_key("2026") == (2026, 2026)
    assert db_common._season_sort_key("bogus") == (0, 0)


def test_season_sort_key_orders_mixed():
    names = ["2026", "2024-2025", "2025-2026"]
    assert sorted(names, key=db_common._season_sort_key) == [
        "2024-2025",
        "2025-2026",
        "2026",
    ]


# ── season_date_window ───────────────────────────────────────────────────────
def test_season_date_window_split_season():
    assert db_common.season_date_window("2025-2026") == (date(2025, 6, 1), date(2026, 8, 15))


def test_season_date_window_calendar_year_spans_whole_year():
    # 18 leagues label their season '2026'; splitting on '-' used to raise
    # ValueError here.
    assert db_common.season_date_window("2026") == (date(2026, 1, 1), date(2026, 12, 31))


def test_season_date_window_unparseable_is_none():
    assert db_common.season_date_window("bogus") is None
    assert db_common.season_date_window("") is None


# ── is_season_active ─────────────────────────────────────────────────────────
def test_is_season_active_during_season():
    assert db_common.is_season_active("2026-2027", date(2026, 9, 28)) is True
    assert db_common.is_season_active("2026", date(2026, 9, 28)) is True


def test_is_season_active_once_window_has_closed():
    assert db_common.is_season_active("2025-2026", date(2026, 9, 28)) is False
    assert db_common.is_season_active("2025", date(2026, 9, 28)) is False


def test_is_season_active_boundaries_are_inclusive():
    assert db_common.is_season_active("2025-2026", date(2026, 8, 15)) is True
    assert db_common.is_season_active("2025-2026", date(2026, 8, 16)) is False


def test_is_season_active_unparseable_is_false():
    assert db_common.is_season_active("bogus", date(2026, 9, 28)) is False


# ── catalog_seasons ─────────────────────────────────────────────────────────
def test_catalog_seasons_premier_nonempty_and_declared():
    seasons = db_common.catalog_seasons("premier")
    assert seasons
    entry = db_common.load_json(db_common.RAW_DIR / "premier" / "leagues.json")
    declared = next(e["seasons"] for e in entry["leagues"] if e["league"] == "premier")
    assert seasons == declared


def test_catalog_seasons_unknown_league_is_empty():
    assert db_common.catalog_seasons("no-such-league") == []


# ── league_season_dirs ───────────────────────────────────────────────────────
def test_league_season_dirs_premier_chronological():
    dirs = db_common.league_season_dirs("premier")
    assert dirs == PREMIER_SEASONS


def test_league_season_dirs_unknown_league_is_empty():
    assert db_common.league_season_dirs("no-such-league") == []


# ── collected_seasons ────────────────────────────────────────────────────────
def test_collected_seasons_premier_all():
    seasons = db_common.collected_seasons("premier")
    assert seasons == PREMIER_SEASONS


def test_collected_seasons_unknown_league_is_empty():
    assert db_common.collected_seasons("no-such-league") == []


def test_collected_seasons_filters_incomplete(tmp_path, monkeypatch):
    league = "fantasy"
    base = tmp_path / league
    full = base / "2025-2026"
    partial = base / "2024-2025"
    for season in (full, partial):
        season.mkdir(parents=True)
        (season / "teams.json").write_text("[]")
        (season / "results.json").write_text("{}")
    for view in db_common.VIEWS:
        (full / f"table_{view}.json").write_text("{}")
        (partial / "table_luck.json").write_text("{}")

    monkeypatch.setattr(db_common, "RAW_DIR", tmp_path)
    assert db_common.collected_seasons(league) == ["2025-2026"]


def test_collected_seasons_wont_fall_back_to_premier_history(tmp_path, monkeypatch):
    league = "fantasy"
    base = tmp_path / league
    season = base / "2025-2026"
    season.mkdir(parents=True)
    (season / "teams.json").write_text("[]")
    (season / "results.json").write_text("{}")

    monkeypatch.setattr(db_common, "RAW_DIR", tmp_path)
    assert db_common.collected_seasons(league) == []


def test_collected_seasons_default_league_falls_back_when_dir_absent(
    tmp_path, monkeypatch
):
    empty = tmp_path / "empty"
    monkeypatch.setattr(db_common, "RAW_DIR", empty)
    assert empty.is_dir() is False
    assert db_common.collected_seasons("premier") == list(db_common.COLLECTED_SEASONS)


def test_collected_seasons_accepts_explicit_league(tmp_path, monkeypatch):
    league = "fantasy"
    season = tmp_path / league / "2026"
    season.mkdir(parents=True)
    (season / "teams.json").write_text("[]")
    (season / "results.json").write_text("{}")
    for view in db_common.VIEWS:
        (season / f"table_{view}.json").write_text("{}")

    monkeypatch.setattr(db_common, "RAW_DIR", tmp_path)
    assert db_common.collected_seasons(league) == ["2026"]
