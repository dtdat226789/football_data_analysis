# ML Feature Layer — match-result prediction

Leakage-safe, deterministic feature engineering for the binary task
**predict `match_result`** ∈ {`HOME_WIN`, `DRAW`, `AWAY_WIN`} from
information available **before** the match.

## Principles

1. **PostgreSQL is the source of truth.** No raw API data, no snapshots —
   features are rebuilt from the `matches`/`league_seasons`/`seasons`/`leagues`
   tables via `ml.features.build_features.build_rows(conn)`.
2. **No temporal leakage.** Matches are processed per season in
   `(match_date, kickoff_time)` order, grouped so that simultaneous matches
   never observe each other's results. A match only ever observes the state
   built from strictly *earlier* matches — the same information a bettor
   would have at kick-off.
3. **No standings-table leak.** The DB's `standings` table holds *final*
   end-of-season snapshots, so group C features are recomputed from prior
   matches only (`ml/features/standings.py`).
4. **Deterministic.** Same DB content => byte-identical rows. Tie-break keys
   (`api_id`) give a total order even when two fixtures share a date/time.
5. **No schema/ETL changes.** The layer reads the analytics database as-is.
   Existing validation/profiling code is untouched.

## Pipeline

```
PostgreSQL
   -> ml.features.build_features.build_rows(conn)   (pure, per-season)
   -> ml.ml.validation.check_dataset(rows)          (in-process checks)
   -> ml.sql_check.run(rows)                        (independent SQL cross-check)
   -> ml/datasets/match_result_dataset.{json,csv}
   -> ml/datasets/split_manifest.json
   -> ml/datasets/validation_report.json
```

Run the build:

```bash
python3 ml/build_dataset.py            # -> exit 0 iff all checks pass
python3 ml/build_dataset.py --league premier
```

## Features (all pre-match)

| Group | Column | Meaning |
| --- | --- | --- |
| A form | `home_team_points_last_5` / `away_team_points_last_5` | points, last 5 matches any venue |
| A form | `home_team_wins_last_5` / `away_team_wins_last_5` | wins, last 5 |
| A form | `home_team_goals_scored_last_5` / `away_team_goals_scored_last_5` | goals for, last 5 |
| A form | `home_team_goals_conceded_last_5` / `away_team_goals_conceded_last_5` | goals against, last 5 |
| B venue | `home_team_home_win_rate` | home win rate, prior home games only |
| B venue | `home_team_home_goals_avg` | avg home goals scored, prior home games |
| B venue | `home_team_home_conceded_avg` | avg home goals conceded |
| B venue | `away_team_away_win_rate` | away win rate, prior away games only |
| B venue | `away_team_away_goals_avg` | avg away goals scored |
| B venue | `away_team_away_conceded_avg` | avg away goals conceded |
| C table | `home_position_before_match` / `away_position_before_match` | position in *running* table |
| C table | `position_difference` | home - away position |
| C table | `home_points_before_match` / `away_points_before_match` | running-table points |
| C table | `points_difference` | home - away points |
| D rest | `home_rest_days` / `away_rest_days` | whole days since last match |
| D rest | `rest_days_difference` | home - away rest days |

Ordering/resolving keys: `points DESC, goal_difference DESC, goals_for DESC`,
all ties share a position (1 + count of strictly-better teams).

Context columns: `api_id`, `league`, `season`, `game_index`,
`home_team_id/home_team`, `away_team_id/away_team`, `match_date`,
`home_team_games_before`, `away_team_games_before`.

Outcome columns: `home_score`, `away_score`, `match_result`.

### NULL policy

Only the rest group is ever absent, and only for a team with **no prior match
in the collected period** (a season opener — including postponed fixtures).
`rest_days_difference` is NULL whenever either side is NULL. Every other
feature defaults to 0 (counts) or 0.0 (rates). These defaults are documented
leakage-safe choices, not missing data.

## Train / holdout split

- Train: `2020-2021` … `2024-2025`
- Holdout: `2025-2026` (never seen during training)
- Split is by **season**, never by row, to avoid time-slice leakage.

## Validation

`ml.validation.check_dataset` asserts (errors unless noted):

- fixed column schema, unique `api_id` (no duplicate match rows)
- no NULLs outside the rest group
- ranges: win rates in `[0,1]`, averages ≥ 0, positions ≥ 1, scores ≥ 0,
  difference columns equal `home − away`
- valid `match_result` labels only
- rows within a season are ordered by `(match_date, game_index)`

`ml.sql_check.run` independently cross-checks the materialized dataset
against PostgreSQL: exact `api_id` parity, row count, and per-row scores.
Always run after a fresh DB migration.

## Tests

`ml/tests/test_features.py` (DB-free, synthetic fixtures):

- record semantics (home/draw/away points & win flags)
- form windowing, venue splits, empty windows
- standings ranking incl. ties
- rest days
- **leakage**: flipping a future match changes nothing upstream; a match's own
  result never affects its features; determinism of rebuilds
- validation detectability (duplicate id, bad NULL, out of range)

```bash
python3 -m pytest ml/tests/ -q
```

## Structure

```
ml/
├── build_dataset.py      CLI: build + materialize + validate (exit 0 iff ok)
├── db.py                 re-exports the project DB helper (single source of truth)
├── validation.py         in-process dataset checks
├── sql_check.py          independent SQL cross-check vs PostgreSQL
├── features/
│   ├── records.py        Match / TeamRecord dataclasses
│   ├── form.py           group A
│   ├── home_away.py      group B
│   ├── standings.py      group C (running table, no leak)
│   ├── rest.py           group D
│   └── build_features.py orchestrator + column registry + SQL loader
├── datasets/             versioned artifacts (JSON + CSV + manifests)
├── models/               reserved for trained models
├── notebooks/            reserved for EDA
├── train.py / evaluate.py / predict.py   stubs (next phase)
└── tests/
```

## Next steps (out of scope for this step)

- `ml/train.py` baseline classifier, `evaluate.py` on the holdout season,
  `predict.py` for a fixture list
- new feature groups (H2H, opponent strength, home/away calendars) — each
  must go through the same strictly-prior pipeline