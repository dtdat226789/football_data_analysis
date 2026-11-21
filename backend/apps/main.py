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

import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from . import common
from .security import install_security
from .routers import analysis, catalog, dashboard, fixtures, kpi, matches, standings, teams
from db_common import DatabaseNotConfigured

API_VERSION = "1.0.0"


def create_app() -> FastAPI:
    disable_docs = os.getenv("DISABLE_DOCS", "").strip().lower() in {
        "1",
        "true",
        "yes",
        "on",
    }
    app = FastAPI(
        title="Football Data Analysis API",
        description=(
            "Exposes the Common Data Analysis Framework: per-league analytical "
            "reports (modules 0-7) plus live database views of the analytics "
            "PostgreSQL (registry, standings, matches, teams). Read-only."
        ),
        version=API_VERSION,
        docs_url=None if disable_docs else "/docs",
        redoc_url=None if disable_docs else "/redoc",
        openapi_url=None if disable_docs else "/openapi.json",
    )
    install_security(app)

    app.include_router(catalog.router, prefix="/api/v1")
    app.include_router(standings.router, prefix="/api/v1")
    app.include_router(matches.router, prefix="/api/v1")
    app.include_router(teams.router, prefix="/api/v1")
    app.include_router(analysis.router, prefix="/api/v1/analysis")
    app.include_router(fixtures.router, prefix="/api/v1")
    app.include_router(dashboard.router, prefix="/api/v1")
    app.include_router(kpi.router, prefix="/api/v1")

    # Backward-compatible aliases (pre-refactor unprefixed paths).
    app.include_router(analysis.legacy, prefix="")

    def _health() -> dict:
        return {
            "status": "ok",
            "default_league": common.DEFAULT_LEAGUE,
            "default_league_name": common.league_name(common.DEFAULT_LEAGUE),
            "n_leagues": len(common.LEAGUE_CONFIG),
            "modules": common.MODULE_NAMES,
        }

    @app.get("/health")
    def health() -> dict:
        return _health()

    @app.get("/api/v1/health")
    def health_v1() -> dict:
        return _health()

    @app.exception_handler(DatabaseNotConfigured)
    async def database_not_configured(_request, _exc):
        # A missing DATABASE_URL is a deployment problem, not a request crash.
        return JSONResponse({"detail": "database unavailable"}, status_code=503)

    return app


app = create_app()
