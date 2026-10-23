"""Unit tests for the shared score classification helpers (no DB, no network).

split_score / score_status in db_common drive both the ETL load (etl_03) and
the count expectations of the validators (validate_db, validate_raw_to_db).
"""
from __future__ import annotations

from scripts.db_common import score_status, split_score


# ── split_score ─────────────────────────────────────────────────────────────
def test_split_score_plain():
    assert split_score("2:1") == (2, 1)
    assert split_score("0:0") == (0, 0)
    assert split_score("10:0") == (10, 0)


def test_split_score_strips_outcome_suffixes():
    assert split_score("2:1AfP") == (2, 1)
    assert split_score("1:3AET") == (1, 3)
    assert split_score("0:1AfP") == (0, 1)
    assert split_score("2:0AET") == (2, 0)
    assert split_score("4:3AET") == (4, 3)


def test_split_score_rejects_unplayed_and_garbage():
    assert split_score("CAN.") is None
    assert split_score("AWA.") is None
    assert split_score("2:0CAN.") is None
    assert split_score("abc") is None
    assert split_score("Not found") is None
    assert split_score(None) is None
    assert split_score(15) is None


# ── score_status ────────────────────────────────────────────────────────────
def test_score_status_playable():
    assert score_status("1:0") == "playable"
    assert score_status("3:2AET") == "playable"
    assert score_status("2:1AfP") == "playable"


def test_score_status_unplayed():
    assert score_status("CAN.") == "unplayed"
    assert score_status("AWA.") == "unplayed"
    assert score_status("2:0CAN.") == "unplayed"


def test_score_status_unparseable():
    assert score_status("abc") == "unparseable"
    assert score_status(None) == "unparseable"
    assert score_status("1-0") == "unparseable"
