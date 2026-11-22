"""Tests for stale fixture-cache cleanup helpers."""
from __future__ import annotations

from scripts.fetch_fixture_details import prune_stale_details
from scripts.fetch_fixtures import prune_stale_files


def test_prune_stale_files_full_sweep(tmp_path):
    for name in ("premier.json", "old.json", "manifest.json"):
        (tmp_path / name).write_text("{}")
    removed = prune_stale_files(tmp_path, set(), {"premier.json"})
    assert [p.name for p in removed] == ["old.json"]
    assert sorted(p.name for p in tmp_path.glob("*.json")) == ["manifest.json", "premier.json"]


def test_prune_stale_files_partial_sweep_leaves_other_leagues(tmp_path):
    for name in ("premier.json", "germany1.json"):
        (tmp_path / name).write_text("{}")
    removed = prune_stale_files(tmp_path, {"premier.json"}, set())
    assert [p.name for p in removed] == ["premier.json"]
    assert (tmp_path / "germany1.json").exists()


def test_prune_stale_details_scoped_to_league(tmp_path):
    names = [
        "premier__2026-08-15-arsenal-vs-chelsea.json",
        "premier__2026-08-22-arsenal-vs-liverpool.json",
        "germany1__2026-08-15-bayern-vs-dortmund.json",
        "manifest.json",
    ]
    for name in names:
        (tmp_path / name).write_text("{}")
    removed = prune_stale_details(
        tmp_path,
        {"premier__2026-08-15-arsenal-vs-chelsea.json"},
        {"premier__"},
    )
    assert [p.name for p in removed] == ["premier__2026-08-22-arsenal-vs-liverpool.json"]
    assert (tmp_path / "germany1__2026-08-15-bayern-vs-dortmund.json").exists()


def test_prune_stale_details_full_sweep(tmp_path):
    for name in ("premier__a.json", "germany1__b.json", "manifest.json"):
        (tmp_path / name).write_text("{}")
    removed = prune_stale_details(tmp_path, {"premier__a.json"}, set())
    assert [p.name for p in removed] == ["germany1__b.json"]
