"""Database access for the ml layer.

Reuses the project's single connection helper (backend/scripts/db_common.py)
instead of duplicating the DSN/connection logic, preserving the existing
architecture: everything reads from the same PostgreSQL source of truth and
the same root .env.
"""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "backend" / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from db_common import LEAGUE, get_conn, parse_season_years  # noqa: E402

__all__ = ["LEAGUE", "get_conn", "parse_season_years"]
