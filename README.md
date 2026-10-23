# Football Data Analysis

An end-to-end football match-data platform: collect raw fixtures, standings and
tables from the Football Charts API, load them into PostgreSQL, run match-result
analysis and ML, and serve it through a FastAPI backend and a React frontend.

93 leagues are configured. The `premier` league is committed as sample raw data,
so the database can be rebuilt without spending API quota.

## What it does

- **Ingest** — fetch league catalogs, teams, fixtures and table views from the
  upstream API, keeping one raw JSON copy per league/season.
- **Load** — a versioned SQL schema (`sql/`) and an ordered ETL that turns the
  raw JSON into a read-only analytics database, with reconciliation checks
  against the raw files.
- **Analyse** — eight analysis modules (0–7) that emit per-league JSON reports
  and PNG charts.
- **Model** — a leakage-safe feature layer and match-result classifier
  (`HOME_WIN` / `DRAW` / `AWAY_WIN`) built only from pre-match information.
- **Serve** — a FastAPI app (versioned `/api/v1` plus backward-compatible
  aliases) and a React SPA with a dashboard, league/team/match pages, upcoming
  fixtures and model predictions.

## Layout

| Path | What lives there |
| --- | --- |
| `backend/apps/` | FastAPI app: routers, deps, markets, regions |
| `backend/scripts/` | The pipeline: collect → validate → ETL → analyse → dashboard |
| `backend/tests/` | Backend + pipeline test suite (pytest) |
| `ml/` | Dataset build, feature engineering, training, scoring, prediction |
| `frontend/` | React + Vite SPA (i18n, vitest) |
| `data/` | Raw samples, catalogs, generated analysis and validation reports |
| `sql/` | Schema DDL, applied as ordered parts |
| `scripts/` | Daily refresh and the Windows scheduled-task installer |

## Requirements

- Python 3.11+
- Node.js 20+
- PostgreSQL 14+

## Setup

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # then fill in the two secrets
cd frontend && npm install && cd ..
```

## Environment variables

Read from the environment, or from `.env` via `python-dotenv`.

| Variable | Required | Purpose |
| --- | --- | --- |
| `FOOTBALL_CHARTS_API_KEY` | yes | Upstream API key. Free tier returns current + previous season only. |
| `DATABASE_URL` | yes | PostgreSQL DSN. |
| `FETCH_DELAY_SECONDS` | no | Delay between upstream requests in `fetch_fixtures.py`. |

The frontend reads `API_PORT` from `frontend/.env` (default `5173`), which is the
port the Vite dev server proxies `/api` and `/health` to.

## Build the database

The schema lives in `sql/` as ordered parts, `00_reset.sql` through
`06_index_tuning.sql`. `build_database.py` chains reset → registry → identity →
matches+standings → validation → raw-to-DB reconciliation → index tuning. Each
step is also runnable on its own (`etl_01_registry.py`, `etl_02_identity.py`,
`etl_03_matches_standings.py`, `validate_db.py`, `validate_raw_to_db.py`,
`tune_indexes.py`).

```bash
python3 backend/scripts/build_league_config.py     # once: refresh league catalog
python3 backend/scripts/collect_raw_data.py        # optional: spend quota
python3 backend/scripts/build_database.py          # raw -> Postgres
python3 backend/scripts/run_analysis.py            # analysis reports
python3 backend/scripts/build_dashboard.py         # all-league HTML dashboard
```

`build_all_leagues.py` chains the last three across every configured league.
`run_analysis.py` runs each module as its own subprocess, so one module failing
does not stop the rest, and the exit code is non-zero only if a module failed.

## Run it

```bash
uvicorn apps.main:app --reload --port 5173          # from backend/
cd frontend && npm run dev                          # serves on 5174, proxies /api
```

- Interactive API docs: <http://localhost:5173/docs>
- Frontend: <http://localhost:5174>
- Health: `GET /health` and `GET /api/v1/health`

### API overview

All database access is read-only: every request opens a cursor and rolls the
transaction back before closing.

| Route | Purpose |
| --- | --- |
| `GET /api/v1/health`, `GET /health` | App status, default league, module names |
| `GET /api/v1/meta`, `/api/v1/leagues`, `/api/v1/leagues/{league}`, `/api/v1/leagues/{league}/seasons` | Catalog and league metadata |
| `GET /api/v1/leagues/{league}/standings` | Standings (`classic` / `luck` / `goals` views) |
| `GET /api/v1/leagues/{league}/matches`, `GET /api/v1/matches/recent`, `GET /api/v1/matches/{api_id}`, `/api/v1/matches/{api_id}/insights` | Match listings, detail and model insights |
| `GET /api/v1/teams`, `/api/v1/teams/{slug}` (+ `/matches`, `/form`, `/standings`, `/stats`) | Team listings, detail and form/stats |
| `GET /api/v1/fixtures`, `/api/v1/fixtures/{league}`, `/api/v1/fixtures/{league}/{match_id}` | Upcoming fixtures with model predictions |
| `GET /api/v1/dashboard` | Aggregate landing-page payload |
| `GET /api/v1/analysis/...`, legacy `/leagues/{league}/analysis...` | Analysis report bundle, per-module JSON and PNG charts |

The legacy analysis paths are kept as backward-compatible aliases for the
original single-file API.

## Analysis modules

`run_analysis.py` executes the Common Data Analysis Framework in dependency
order for a league, writing `data/analysis/<league>/`:

| # | Stem | Report |
| --- | --- | --- |
| 0 | `database_profile` | Database profile |
| 1 | `matches_analysis` | Match outcomes |
| 2 | `goals_analysis` | Goal analysis |
| 3 | `teams_analysis` | Team analysis |
| 4 | `season_trends` | Season trends |
| 5 | `scoreline_analysis` | Scoreline analysis |
| 6 | `relationships` | Relationships |
| 7 | `findings` | Consolidated findings |

Use `--league`, `--out-dir`, `--only` and `--skip` to scope a run.

## ML

See [`ml/README.md`](ml/README.md) for the full contract. In short:

```bash
python3 ml/build_dataset.py                         # materialise + validate dataset
python3 ml/train.py                                 # fit + select model
python3 ml/evaluate.py                              # holdout-season report
python3 ml/predict.py --features rows.json          # score hand-built rows
python3 ml/predict.py --league premier              # upcoming fixtures
python3 -m ml.backfill_predictions                  # match-detail prediction artifact
```

Features are rebuilt from PostgreSQL only, per season, in
`(match_date, kickoff_time)` order, so a match never observes a later result.
Train is `2020-2021`…`2024-2025`; holdout is `2025-2026`. Model artifacts under
`ml/models/` are gitignored; the API serves committed JSON artifacts instead.

## Frontend

React 18 + Vite SPA with routes for the dashboard, leagues, teams, matches,
match detail and fixture detail. It ships an English/Vietnamese catalogue with a
language and IANA time-zone picker (persisted to `localStorage`), URL-backed
search/pagination state, and components covered by vitest.

```bash
cd frontend
npm run dev        # dev server
npm run build      # production build
npm run check      # lint + typecheck + test
```

## Daily refresh

```bash
bash scripts/refresh_data.sh [--dry-run] [--force]
```

Collects live seasons, fetches fixtures, validates raw data, rebuilds the
database, analysis and dashboard. It runs at most once per calendar day (a stamp
file records the last fully successful run), fails soft between stages, and never
touches git. On Windows, `scripts/install_task.ps1` registers it as a scheduled
task that wakes WSL; `scripts/uninstall_task.ps1` removes it.

## Tests

```bash
python3 -m pytest -q                 # 738 tests (637 offline, 101 live-API)
cd frontend && npm test              # vitest
```

101 of the backend tests call the live Football Charts API and are **skipped
unless `FOOTBALL_CHARTS_API_KEY` is set**, so `pytest` works offline and in CI
without spending quota. Database-backed tests skip when PostgreSQL is
unreachable.

## CI

`.github/workflows/ci.yml` runs two jobs:

- **backend** — spins up PostgreSQL 16, installs `requirements.txt` + ruff, runs
  `ruff check .`, builds the database from the committed `premier` sample raw
  data, then runs `pytest` (with `FOOTBALL_CHARTS_API_KEY` empty, so live tests
  skip).
- **frontend** — `npm ci`, then `npm run lint`, `npm run typecheck`,
  `npm test`, `npm run build`.

## Lint

```bash
ruff check .                         # backend / ml / scripts
cd frontend && npm run lint          # eslint
cd frontend && npm run typecheck     # tsc -p jsconfig.json
```

Ruff is configured in `pyproject.toml`. The rule set is deliberately limited to
bug-finding families (pyflakes, bugbear, datetimez, statements, unused args);
stylistic families were dropped because they produced ~200 findings that were
review opinions rather than defects. `E501` is off: line length is left to
review.

## Notes

- `data/analysis/**` and `data/validation/**` are generated. The reports
  deliberately store repo-relative paths so they stay portable.
- `ml/` imports `backend/` by path, which is why `pyproject.toml` sets
  `pythonpath` for pytest.
- The `venv/` checked out on Windows (`venv\Scripts`) cannot be used from WSL;
  `refresh_data.sh` uses the system `python3` instead.
