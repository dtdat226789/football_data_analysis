"""Tests for the country → region mapping (backend/apps/regions.py)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

import apps.common as common  # noqa: E402
from apps import regions  # noqa: E402


@pytest.mark.parametrize(
    ("country", "expected"),
    [
        ("England", "europe"),
        ("Germany", "europe"),
        ("Czech Republic", "europe"),
        ("Japan", "asia"),
        ("South Korea", "asia"),
        ("Saudi Arabia", "asia"),
        ("Brazil", "america"),
        ("Australia", "other"),
    ],
)
def test_region_buckets(country, expected):
    assert regions.league_region(country) == expected


def test_fallback_for_unknown_country():
    assert regions.league_region("Narnia") == "other"
    assert regions.league_region("") == "other"


def test_every_catalog_country_maps_to_a_fixed_region():
    known = {"europe", "asia", "america", "other"}
    for meta in common.LEAGUE_CONFIG.values():
        region = regions.league_region(meta.get("country", ""))
        assert region in known, f"unmapped region for {meta.get('country')}"