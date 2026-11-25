"""Tests for non-destructive database safety helpers."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

from scripts.build_database import is_local_database
from scripts.compare_row_counts import compare_counts


@pytest.mark.parametrize(
    ("dsn", "expected"),
    [
        ("postgresql://u:p@localhost/db", True),
        ("postgresql://u:p@127.0.0.1:5432/db", True),
        ("postgresql://u:p@[::1]:5432/db", True),
        ("postgresql://u:p@neon.example.com/db", False),
        ("sqlite:///football.db", False),
    ],
)
def test_is_local_database(dsn, expected):
    assert is_local_database(dsn) is expected


def test_compare_counts_ignores_growth_and_new_tables():
    assert compare_counts({"matches": 10}, {"matches": 12, "teams": 20}) == []


def test_compare_counts_reports_data_loss():
    issues = compare_counts(
        {"matches": 10, "teams": 20, "seasons": 3},
        {"matches": 9, "teams": 20, "seasons": 1},
    )
    assert issues == ["matches: 10 -> 9", "seasons: 3 -> 1"]


def test_reset_drops_the_migration_ledger():
    path = Path(__file__).resolve().parents[2] / "sql" / "00_reset.sql"
    block = re.search(r"DROP TABLE IF EXISTS(.*?)CASCADE;", path.read_text(), re.S)
    assert block is not None
    names = {line.strip().rstrip(",") for line in block.group(1).splitlines() if line.strip()}
    assert "schema_migrations" in names
