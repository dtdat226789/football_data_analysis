"""Shared helpers for the database build & validation pipeline (steps 01-06).

Every step script in this package loads the project .env, opens a psycopg2
connection to DATABASE_URL and works against the SQL migration files in sql/.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

SQL_DIR = ROOT_DIR / "sql"
RAW_DIR = ROOT_DIR / "data" / "raw"

LEAGUE = "premier"
COLLECTED_SEASONS = [
    "2020-2021",
    "2021-2022",
    "2022-2023",
    "2023-2024",
    "2024-2025",
    "2025-2026",
]
VIEWS = ["classic", "luck", "goals"]


def get_conn() -> psycopg2.extensions.connection:
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        sys.exit("DATABASE_URL not set in project root .env")
    return psycopg2.connect(dsn)


def apply_sql(conn, filename: str) -> None:
    """Execute one migration file inside the current transaction."""
    path = SQL_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Migration not found: {path}")
    with conn.cursor() as cur:
        cur.execute(path.read_text())
    conn.commit()
    print(f"[schema] applied {filename}")


def raw_file(season: str, name: str) -> Path:
    return RAW_DIR / LEAGUE / season / name


def load_json(path: Path) -> dict:
    return json.loads(path.read_bytes())


def parse_season_years(name: str) -> tuple[int | None, int | None]:
    """Best-effort parse of an opaque season string for start/end ordering.

    '2020-2021' -> (2020, 2021); '2026' -> (2026, 2026); unknown -> (None, None).
    """
    parts = [p for p in name.split("-") if p.isdigit()]
    if not parts:
        return None, None
    start = int(parts[0])
    end = int(parts[-1]) if len(parts) > 1 else start
    return min(start, end), max(start, end)


def parse_score(raw: str | None) -> tuple[int, int] | None:
    """Parse an upstream 'H:A' score string into (home, away), or None."""
    if not isinstance(raw, str) or raw.count(":") != 1:
        return None
    a, b = raw.split(":")
    if not a.isdigit() or not b.isdigit():
        return None
    return int(a), int(b)