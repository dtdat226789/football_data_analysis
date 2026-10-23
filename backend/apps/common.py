"""Shared constants and helpers for the Football Data Analysis API.

The API serves two data sources without coupling them:

* **Live PostgreSQL** (matches / standings / teams / registry) via routers that
  use ``apps.deps`` for read-only (rollback) access.
* **Per-league JSON reports** produced by ``run_analysis.py`` (the analytical
  modules) via ``apps.routers.analysis``.

League configuration and season helpers are re-exported from
``backend/scripts/db_common.py`` so the API never diverges from the pipeline.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
BACKEND_SCRIPTS = str(Path(__file__).resolve().parents[1] / "scripts")


def ensure_scripts_path() -> None:
    """Put backend/scripts on sys.path so db_common is importable everywhere."""
    if BACKEND_SCRIPTS not in sys.path:
        sys.path.insert(0, BACKEND_SCRIPTS)


ensure_scripts_path()

from db_common import (  # noqa: E402
    LEAGUE as DEFAULT_LEAGUE,
    LEAGUE_CONFIG,
    league_meta,
)

from . import regions  # noqa: E402

ANALYSIS_DIR = ROOT_DIR / "data" / "analysis"

MODULES = [
    ("database_profile", "database profile"),
    ("matches_analysis", "match outcomes"),
    ("goals_analysis", "goal analysis"),
    ("teams_analysis", "team analysis"),
    ("season_trends", "season trends"),
    ("scoreline_analysis", "scoreline analysis"),
    ("relationships", "relationships"),
    ("findings", "consolidated findings"),
]
MODULE_NAMES = [name for name, _ in MODULES]


def league_name(league: str | None) -> str | None:
    """Human-readable name for a league slug.

    The one place a slug is turned into something worth showing a reader, so
    that every endpoint labels a league identically ("wsweden" is always
    "Allsvenskan Women", never the raw upstream spelling and never the slug).
    Falls back to the slug itself for an unregistered league and to None when
    there is no league at all (an unscoped feed), which keeps optional filters
    distinguishable from a real one.
    """
    if not league:
        return None
    return league_meta(league)["name"]


def league_config() -> dict[str, dict]:
    """slug -> {name, country, teams, matches, views, format, url}."""
    return dict(LEAGUE_CONFIG)


def league_listing() -> list[dict]:
    """Every league with its config, region and whether analysis reports exist."""
    return [
        {
            "slug": slug,
            **meta,
            "region": regions.league_region(meta.get("country", "")),
            "has_data": league_report_dir(slug) is not None,
        }
        for slug, meta in LEAGUE_CONFIG.items()
    ]


def league_report_dir(league: str) -> Path | None:
    """Directory holding a league's reports, or None when nothing was generated.

    Reports live under ``data/analysis/{league}/``. For backwards compatibility
    the default league is also resolved against the flat ``data/analysis/``
    directory when its per-league folder is absent.
    """
    per_league = ANALYSIS_DIR / league
    if per_league.is_dir():
        return per_league
    if league == DEFAULT_LEAGUE and (ANALYSIS_DIR / "matches_analysis.json").exists():
        return ANALYSIS_DIR
    return None


def read_report(report_dir: Path, module: str) -> dict | None:
    path = report_dir / f"{module}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def list_charts(report_dir: Path) -> list[str]:
    charts_dir = report_dir / "charts"
    if not charts_dir.is_dir():
        return []
    return sorted(p.name for p in charts_dir.glob("*.png"))
