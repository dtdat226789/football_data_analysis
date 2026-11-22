"""Apply schema migrations in order and record applied versions.

The existing idempotent schema files (01/02/04/06) are applied as the baseline
on an untracked database. Future changes belong in sql/migrations/*.sql and are
applied once each, in lexical order.
"""
from __future__ import annotations

import sys
from pathlib import Path

from db_common import SQL_DIR, get_conn

MIGRATIONS_DIR = SQL_DIR / "migrations"
BASELINE_FILES = (
    "01_registry.sql",
    "02_identity.sql",
    "04_matches_standings.sql",
    "06_index_tuning.sql",
)
BASELINE_VERSION = "0001_baseline"


def ensure_migration_table(conn) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version     TEXT PRIMARY KEY,
                applied_at  TIMESTAMPTZ NOT NULL DEFAULT now()
            )
            """
        )
    conn.commit()


def applied_versions(conn) -> set[str]:
    with conn.cursor() as cur:
        cur.execute("SELECT version FROM schema_migrations")
        return {row[0] for row in cur.fetchall()}


def apply_files(conn, files: list[Path]) -> None:
    with conn.cursor() as cur:
        for path in files:
            cur.execute(path.read_text(encoding="utf-8"))
    conn.commit()


def record(conn, version: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO schema_migrations (version) VALUES (%s) "
            "ON CONFLICT (version) DO NOTHING",
            (version,),
        )
    conn.commit()


def main(argv: list[str] | None = None) -> int:
    conn = get_conn()
    try:
        ensure_migration_table(conn)
        done = applied_versions(conn)

        if BASELINE_VERSION not in done:
            missing = [SQL_DIR / name for name in BASELINE_FILES]
            absent = [str(path) for path in missing if not path.exists()]
            if absent:
                raise FileNotFoundError("Missing baseline schema: " + ", ".join(absent))
            apply_files(conn, missing)
            record(conn, BASELINE_VERSION)
            print(f"[migrate] applied {BASELINE_VERSION}")
            done.add(BASELINE_VERSION)

        for path in sorted(MIGRATIONS_DIR.glob("*.sql")):
            version = path.stem
            if version in done:
                continue
            apply_files(conn, [path])
            record(conn, version)
            print(f"[migrate] applied {version}")
    finally:
        conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
