"""Unit tests for validate_db helpers (no DB, no network).

Only the pure helpers are covered here; the full validation run needs a live
PostgreSQL database, but the count expectations are computed from raw JSON
with the same score classification the ETL uses.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from scripts.validate_db import playable_count  # noqa: E402
from scripts.db_common import score_status  # noqa: E402


# ── playable_count ──────────────────────────────────────────────────────────
def test_playable_count_counts_only_playable_matches():
    raw = {
        "matches": [
            {"score": "1:0"},
            {"score": "2:1AfP"},
            {"score": "1:3AET"},
            {"score": "CAN."},
            {"score": "AWA."},
            {"score": "2:0CAN."},
            {"score": "garbage"},
            {"score": None},
            {"team": "not-a-match-row"},
        ]
    }
    assert playable_count(raw) == 3


def test_playable_count_empty():
    assert playable_count({"matches": []}) == 0
    assert playable_count({}) == 0


def test_playable_count_agrees_with_score_status():
    raw = {"matches": [{"score": s} for s in ("1:0", "CAN.", "abc", None)]}
    assert playable_count(raw) == sum(
        1
        for m in raw["matches"]
        if score_status(m["score"]) == "playable"
    )