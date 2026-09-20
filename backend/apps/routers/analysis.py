"""Analysis report API: serves the JSON/PNG outputs of run_analysis.py.

Two route sets:

* ``router``   mounted at ``/api/v1/analysis`` -> ``/{league}`` etc.
* ``legacy``   mounted unprefixed (backward-compatible aliases for the
  original single-file API): ``/leagues/{league}/analysis`` etc.

The endpoints are read-only file lookups over ``common.ANALYSIS_DIR``.
"""
from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from .. import common

router = APIRouter(tags=["analysis"])
legacy = APIRouter(tags=["analysis-legacy"])

MODULE_NAMES = common.MODULE_NAMES


def _require_known_league(league: str) -> None:
    if league not in common.LEAGUE_CONFIG:
        raise HTTPException(status_code=404, detail=f"unknown league '{league}'")


def analysis_bundle(league: str) -> dict:
    _require_known_league(league)
    report_dir = common.league_report_dir(league)
    if report_dir is None:
        return {
            "league": league,
            "meta": common.LEAGUE_CONFIG[league],
            "has_data": False,
            "reports": {},
            "missing": MODULE_NAMES,
            "charts": [],
        }
    reports: dict = {}
    missing: list[str] = []
    for module, _label in common.MODULES:
        payload = common.read_report(report_dir, module)
        if payload is None:
            missing.append(module)
        else:
            reports[module] = payload
    return {
        "league": league,
        "meta": common.LEAGUE_CONFIG[league],
        "has_data": True,
        "reports": reports,
        "missing": missing,
        "charts": common.list_charts(report_dir),
    }


def analysis_module(league: str, module: str) -> dict:
    if module not in MODULE_NAMES:
        raise HTTPException(status_code=404, detail=f"unknown module '{module}'")
    _require_known_league(league)
    report_dir = common.league_report_dir(league)
    payload = common.read_report(report_dir, module) if report_dir else None
    if payload is None:
        raise HTTPException(
            status_code=404,
            detail=f"no '{module}' report for league '{league}' (run run_analysis.py)",
        )
    return payload


def analysis_charts(league: str) -> dict:
    report_dir = common.league_report_dir(league)
    if report_dir is None:
        raise HTTPException(status_code=404, detail=f"no data for league '{league}'")
    return {"league": league, "charts": common.list_charts(report_dir)}


def analysis_chart(league: str, chart: str) -> FileResponse:
    report_dir = common.league_report_dir(league)
    if report_dir is None:
        raise HTTPException(status_code=404, detail=f"no data for league '{league}'")
    path = report_dir / "charts" / chart
    if not (path.is_file() and chart.endswith(".png")):
        raise HTTPException(status_code=404, detail=f"chart '{chart}' not found")
    return FileResponse(path, media_type="image/png")


def list_leagues() -> list[dict]:
    return common.league_listing()


# v1 shape (mounted at /api/v1/analysis). Charts routes are registered before
# the generic {module} route so "charts" is never captured as a module name.
router.add_api_route(
    "/{league}", analysis_bundle, methods=["GET"], response_model=None
)
router.add_api_route(
    "/{league}/charts", analysis_charts, methods=["GET"], response_model=None
)
router.add_api_route(
    "/{league}/charts/{chart}", analysis_chart, methods=["GET"], response_model=None
)
router.add_api_route(
    "/{league}/{module}", analysis_module, methods=["GET"], response_model=None
)

# Legacy unprefixed aliases (original analysis_api.py surface).
legacy.add_api_route("/leagues", list_leagues, methods=["GET"], response_model=None)
legacy.add_api_route(
    "/leagues/{league}/analysis", analysis_bundle, methods=["GET"], response_model=None
)
legacy.add_api_route(
    "/leagues/{league}/analysis/{module}",
    analysis_module,
    methods=["GET"],
    response_model=None,
)
legacy.add_api_route(
    "/leagues/{league}/charts", analysis_charts, methods=["GET"], response_model=None
)
legacy.add_api_route(
    "/leagues/{league}/charts/{chart}",
    analysis_chart,
    methods=["GET"],
    response_model=None,
)