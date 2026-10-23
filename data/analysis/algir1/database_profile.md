# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:43:29+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `algir1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 2 |
| league_seasons | 2 |
| teams | 19 |
| team_aliases | 38 |
| team_seasons | 32 |
| matches | 263 |
| standings | 96 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `1`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `algir1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 240 | 16 | 2025-08-21 | 2026-06-06 |
| 2026-2027 | True | in_progress | 23 | 16 | 2026-09-03 | 2026-09-22 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 263 | 263 | 0 |
| matches (league_season_id, game_index) | 263 | 263 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 263 | 261 | 2 |
| team_seasons (league_season_id, team_id) | 32 | 32 | 0 |
| team_seasons api_name within a season | 32 | 32 | 0 |
| team_seasons api_slug within a season | 32 | 32 | 0 |
| standings (league_season_id, team_id, view) | 96 | 96 | 0 |
| team_aliases (form, value) | 38 | 38 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 2 | 2 | 0 |
| teams.canonical_name | 19 | 19 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `263`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 263 | 0.0% |
| kickoff_time | 0 | 263 | 0.0% |
| home_team_id | 0 | 263 | 0.0% |
| away_team_id | 0 | 263 | 0.0% |
| home_score | 0 | 263 | 0.0% |
| away_score | 0 | 263 | 0.0% |
| home_ht | 0 | 263 | 0.0% |
| away_ht | 0 | 263 | 0.0% |
| first_goal_time | 22 | 241 | 8.4% |
| first_goal_time_extra | 22 | 241 | 8.4% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 7 |
| away_score | 0 | 5 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 4 |
| away_ht | 0 | 3 |
- first_goal_time NULL semantics consistent: `True`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 130 | 49.4% |
| Draw | 78 | 29.7% |
| Away | 55 | 20.9% |
| Total | 263 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 600 |
| Average goals per match | 2.281 |
| Home goals | 361 (avg 1.373) |
| Away goals | 239 (avg 0.909) |
| Home goal share | 60.2% |
| Goalless matches | 22 (8.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 50.0% | 29.2% | 20.8% | 544 | 2.267 | 325 | 219 | 20 (8.3%) |
| 2026-2027 | 23 | 43.5% | 34.8% | 21.7% | 56 | 2.435 | 36 | 20 | 2 (8.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `241` of `263` (91.6%)
| metric | value |
|---|---|
| First goals recorded | 241 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 35.51 |
| Median (p50) | 29.0 |
| p25 | 15.0 |
| p75 | 53.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 65 |
| 16-30 | 64 |
| 31-45 | 31 |
| 46-60 | 33 |
| 61-75 | 23 |
| 76-90 | 20 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 49 |
| 1-1 | 38 |
| 2-1 | 25 |
| 2-0 | 23 |
| 0-0 | 22 |
| 0-1 | 22 |
| 2-2 | 16 |
| 1-2 | 15 |
| 3-1 | 9 |
| 0-2 | 8 |
| 3-0 | 8 |
| 3-2 | 7 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-3 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 24 | 9.1% |
| Mon | 16 | 6.1% |
| Tue | 19 | 7.2% |
| Wed | 23 | 8.7% |
| Thu | 30 | 11.4% |
| Fri | 80 | 30.4% |
| Sat | 71 | 27.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 23 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 43.5% vs overall 49.4% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 34.8% vs overall 29.7% |
| 8 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 23, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 43.5, "overall_share": 49.4}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 34.8, "overall_share": 29.7}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 263, "distinct": 261, "duplicates": 2}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
