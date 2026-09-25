"""Football Data Analysis API - FastAPI application factory.

Data + analysis platform:

* **Versioned** routes under ``/api/v1`` (catalog, teams, standings, matches,
  analysis) backed by the live PostgreSQL analytics database (read-only,
  rolled back per request) plus the per-league JSON reports.
* **Backward-compatible** aliases for the original single-file analysis API
  (``/health``, ``/leagues``, ``/leagues/{league}/analysis[...]``).

Run it:
    uvicorn backend.apps.main:app --reload
"""
from __future__ import annotations

from fastapi import FastAPI

from . import common
from .routers import analysis, catalog, dashboard, fixtures, matches, standings, teams

API_VERSION = "1.0.0"


def create_app() -> FastAPI:
    app = FastAPI(
        title="Football Data Analysis API",
        description=(
            "Exposes the Common Data Analysis Framework: per-league analytical "
            "reports (modules 0-7) plus live database views of the analytics "
            "PostgreSQL (registry, standings, matches, teams). Read-only."
        ),
        version=API_VERSION,
    )

    app.include_router(catalog.router, prefix="/api/v1")
    app.include_router(standings.router, prefix="/api/v1")
    app.include_router(matches.router, prefix="/api/v1")
    app.include_router(teams.router, prefix="/api/v1")
    app.include_router(analysis.router, prefix="/api/v1/analysis")
    app.include_router(fixtures.router, prefix="/api/v1")
    app.include_router(dashboard.router, prefix="/api/v1")

    # Backward-compatible aliases (pre-refactor unprefixed paths).
    app.include_router(analysis.legacy, prefix="")

    def _health() -> dict:
        return {
            "status": "ok",
            "default_league": common.DEFAULT_LEAGUE,
            "n_leagues": len(common.LEAGUE_CONFIG),
            "modules": common.MODULE_NAMES,
        }

    @app.get("/health")
    def health() -> dict:
        return _health()

    @app.get("/api/v1/health")
    def health_v1() -> dict:
        return _health()

    return app


app = create_app()