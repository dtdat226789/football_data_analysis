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
| `WORKER_SHARED_SECRET` | production | Shared secret the Cloudflare Worker sends as `X-Worker-Secret`; direct API requests are rejected when set. |
| `BACKEND_SHARED_SECRET` | production | Worker-side equivalent of `WORKER_SHARED_SECRET`; set with `wrangler secret put BACKEND_SHARED_SECRET`. |
| `API_RATE_LIMIT_PER_MINUTE` | no | In-process fallback rate limit. Use Cloudflare rate limiting as the primary control. |
| `DISABLE_DOCS` | production | Set to `1` to disable `/docs`, `/redoc` and `/openapi.json`. |
| `ALLOW_INSECURE_API` | local only | Explicit opt-out of the fail-closed secret check for local development/tests. Never set in production. |
| `ALLOW_NO_RATE_LIMITER` | `wrangler dev` only | Lets the Worker serve without the `ratelimits` binding. Never set in production. |

The frontend reads `API_PORT` from `frontend/.env` (default `5173`), which is the
port the Vite dev server proxies `/api` and `/health` to.

## Build the database

The schema lives in `sql/` as ordered parts, `00_reset.sql` through
`06_index_tuning.sql`. `build_database.py` now applies migrations by default:
`migrate.py` records a `0001_baseline` version from the idempotent 01/02/04/06
files, then applies any later `sql/migrations/*.sql` exactly once. Destructive
resets are opt-in via `--reset-local`, which refuses any DSN whose host is not
`localhost`, `127.0.0.1` or `[::1]`. ETL validation and reconciliation steps
still run after schema setup.

```bash
python3 backend/scripts/build_league_config.py     # once: refresh league catalog
python3 backend/scripts/collect_raw_data.py        # optional: spend quota
python3 backend/scripts/build_database.py          # migrate + raw -> Postgres
python3 backend/scripts/build_database.py --reset-local  # local DB only
python3 backend/scripts/run_analysis.py            # analysis reports
python3 backend/scripts/build_dashboard.py         # all-league HTML dashboard
```

`build_all_leagues.py` chains the last three across every configured league and
accepts the same guarded `--reset-local` flag. `run_analysis.py` runs each
module as its own subprocess, so one module failing does not stop the rest, and
the exit code is non-zero only if a module failed.

`compare_row_counts.py --snapshot PATH` records row counts for every known
table; `--before A --after B` fails if any table lost rows. The daily refresh
takes snapshots around the Neon dump/restore so a partial publish triggers the
rollback path instead of silently losing data.

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
| `GET /api/v1/teams/{slug}/kpi`, `GET /api/v1/club-analysis` | Sample-style team KPI and club dashboards (goals-based proxies; no xG/shot data is collected) |
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
bash scripts/generate_ml_artifacts.sh                # all of the above + baseline gate
```

Features are rebuilt from PostgreSQL only, per season, in
`(match_date, kickoff_time)` order, so a match never observes a later result.
Train is `2020-2021`…`2024-2025`; holdout is `2025-2026`. Model artifacts under
`ml/models/` are gitignored, so `scripts/generate_ml_artifacts.sh` rebuilds the
dataset, applies the baseline promotion gate and writes `match_predictions.json`
before every image build (CI, daily refresh and backend deploy). A candidate is
promoted only when it beats the constant majority baseline on dev log-loss *and*
accuracy; the holdout can veto a regression, in which case the majority baseline
is promoted and the prediction artifact is regenerated from it.

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

### Production security settings

Generate one value and install it in both places:

```bash
openssl rand -hex 32
```

1. Render service → Environment → add `WORKER_SHARED_SECRET` with that value,
   plus `DISABLE_DOCS=1` and `API_RATE_LIMIT_PER_MINUTE=120`.
2. Cloudflare Worker (same value):

   ```bash
   npx wrangler@4.165.0 secret put BACKEND_SHARED_SECRET --name football-web
   ```

   The Worker strips any client-supplied secret before injecting this one as
   `X-Worker-Secret`, so a direct request cannot pass itself off as the Worker.
   `deploy-web.yml` fails fast when the Worker secret is not configured.
3. The `/api/*` (and `/health`) rate-limit rule lives in version control: the
   `ratelimits` binding in `wrangler.jsonc` plus the check in `worker/index.js`
   allow 120 requests/minute per client IP in each Cloudflare location and
   return `429` with `Retry-After: 60`. Static assets are not limited; the
   Render-side `API_RATE_LIMIT_PER_MINUTE` limiter is the second line of defence.

The Worker also adds CSP, HSTS, clickjacking and MIME-sniffing headers to both
API and static responses.

Protected routes fail closed: if `WORKER_SHARED_SECRET` is missing, the API
returns `503` instead of serving unauthenticated data. The backend limiter keys
on `X-Worker-Client-IP`, which the Worker overwrites with Cloudflare's view of
the client IP; `CF-Connecting-IP` and `X-Forwarded-For` from callers are ignored.
`/docs`, `/redoc` and `/openapi.json` require the same shared secret when enabled.

### Credential rotation

If a secret may have leaked (including through a committed or world-readable
`.env`), treat it as compromised. Rotation is an operator action — code cannot
revoke credentials:

1. **Football Charts API key** — revoke/issue a key in the provider dashboard,
   update the `FOOTBALL_CHARTS_API_KEY` GitHub Actions secret and the local
   `.env`, then re-run the preflight in `daily-refresh.yml`.
2. **Database password** — rotate the password on the Neon role, update the
   `NEON_DATABASE_URL` GitHub Actions secret (and the `DATABASE_URL` used by the
   backend), then restart the backend. `daily-refresh.yml` uses a separate
   local build database, so rotation does not affect its rebuild.
3. **Worker/backend shared secret** — generate a new value with
   `openssl rand -hex 32`, set `WORKER_SHARED_SECRET` in Render and
   `wrangler secret put BACKEND_SHARED_SECRET` together, then redeploy both.
4. Keep `.env` at mode `600` (`icacls` on Windows if the mount ignores chmod),
   never commit it, and verify with `git check-ignore -v .env`.

## Daily refresh

```bash
bash scripts/refresh_data.sh [--dry-run] [--force]
```

Collects live seasons, fetches fixtures and per-match details, validates raw
data, rebuilds the database, analysis and dashboard, then generates gated ML
artifacts. It runs at most once per calendar day (a stamp file records the last
fully successful run), fails soft between stages, and never touches git. Each
stage writes `logs/refresh_summary.json`; CI refuses to publish or deploy unless
all seven stages report `ok`, so a late failure can no longer be masked by a
successful database line in the log. The validator exits non-zero when it finds
errors, but the known backlog is tracked in `logs/.validation_baseline.json`:
only new regressions, new leagues with errors and unreadable reports fail the
stage. A clean CI checkout has no baseline, so it records counts rather than
blocking on historical data issues. On Windows, `scripts/install_task.ps1`
registers it as a scheduled task that wakes WSL; `scripts/uninstall_task.ps1`
removes it.

Both `deploy-backend.yml` and `daily-refresh.yml` tag the running `latest` image
as `previous`, poll `/health` after the Render deploy hook, and restore `previous`
to `latest` plus re-trigger the hook if the new image never becomes healthy.
`render.yaml` is the service blueprint template; replace the Docker Hub username
placeholder once, keep `DATABASE_URL` and `WORKER_SHARED_SECRET` in Render's
secret UI (`sync: false`), and set `healthCheckPath: /health`.

## Tests

```bash
python3 -m pytest -q                 # 679 tests; live-API tests skip without a key
npm test --prefix worker             # node:test
cd frontend && npm test              # vitest
```

101 of the backend tests call the live Football Charts API and are **skipped
unless `FOOTBALL_CHARTS_API_KEY` is set**, so `pytest` works offline and in CI
without spending quota. Database-backed tests skip when PostgreSQL is
unreachable.

## CI

`.github/workflows/ci.yml` runs three jobs:

- **backend** — spins up PostgreSQL 16, installs `requirements.txt` + ruff, runs
  `ruff check .`, builds the database from the committed `premier` sample raw
  data, generates the gated ML artifacts, then runs `pytest` (with
  `FOOTBALL_CHARTS_API_KEY` empty, so live tests skip).
- **worker** — `npm test --prefix worker` (Node's built-in test runner, no
  dependencies).
- **frontend** — `npm ci`, then `npm run lint`, `npm run typecheck`,
  `npm test`, `npm run build`.

`deploy-backend.yml` watches backend/Dockerfile/ML changes and ships an image
with freshly generated prediction artifacts without waiting for the daily data
rebuild. `deploy-web.yml` watches only frontend/worker assets.

## Release checklist

```bash
cd frontend && npm ci && npm run check && npm run build && cd ..
ruff check . && python3 -m pytest -q
npm test --prefix worker
npx wrangler@4.165.0 deploy --dry-run
```

The Wrangler dry run needs no credentials and validates the Worker bundle,
including the rate-limit binding. Before pushing, check the built app
(`npm run preview` in `frontend/`, with the API on `API_PORT`) at desktop and
mobile widths: dashboard, matches, league, team, match and fixture pages,
keyboard focus/skip links and reduced-motion behaviour. A push to `main`
triggers `deploy-web.yml` for the SPA + Worker; `daily-refresh.yml` owns data
rebuilds, the backend image and the Render deploy hook.

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
