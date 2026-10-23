# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:46:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `china`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 22 |
| teams | 265 |
| team_aliases | 530 |
| team_seasons | 424 |
| matches | 4530 |
| standings | 1272 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `11`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 679 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `china`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 240 | 16 | 2025-02-22 | 2025-11-22 |
| 2026 | True | in_progress | 208 | 16 | 2026-03-06 | 2026-09-18 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 4530 | 4530 | 0 |
| matches (league_season_id, game_index) | 4530 | 4530 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 4530 | 4528 | 2 |
| team_seasons (league_season_id, team_id) | 424 | 424 | 0 |
| team_seasons api_name within a season | 424 | 424 | 0 |
| team_seasons api_slug within a season | 424 | 424 | 0 |
| standings (league_season_id, team_id, view) | 1272 | 1272 | 0 |
| team_aliases (form, value) | 530 | 530 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 265 | 265 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `4530`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 4530 | 0.0% |
| kickoff_time | 0 | 4530 | 0.0% |
| home_team_id | 0 | 4530 | 0.0% |
| away_team_id | 0 | 4530 | 0.0% |
| home_score | 0 | 4530 | 0.0% |
| away_score | 0 | 4530 | 0.0% |
| home_ht | 6 | 4524 | 0.1% |
| away_ht | 6 | 4524 | 0.1% |
| first_goal_time | 328 | 4202 | 7.2% |
| first_goal_time_extra | 328 | 4202 | 7.2% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 207 | 46.2% |
| Draw | 118 | 26.3% |
| Away | 123 | 27.5% |
| Total | 448 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1414 |
| Average goals per match | 3.156 |
| Home goals | 802 (avg 1.79) |
| Away goals | 612 (avg 1.366) |
| Home goal share | 56.7% |
| Goalless matches | 19 (4.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 46.7% | 25.8% | 27.5% | 771 | 3.212 | 432 | 339 | 9 (3.8%) |
| 2026 | 208 | 45.7% | 26.9% | 27.4% | 643 | 3.091 | 370 | 273 | 10 (4.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `429` of `448` (95.8%)
| metric | value |
|---|---|
| First goals recorded | 429 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 28.95 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 42.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 149 |
| 16-30 | 105 |
| 31-45 | 84 |
| 46-60 | 50 |
| 61-75 | 21 |
| 76-90 | 18 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 16 | 1..16 | 16 |
| 2025 | goals | 16 | 1..16 | 16 |
| 2025 | luck | 16 | 1..16 | 16 |
| 2026 | classic | 16 | 1..16 | 16 |
| 2026 | goals | 16 | 1..16 | 16 |
| 2026 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 55 |
| 1-0 | 43 |
| 2-1 | 34 |
| 2-2 | 33 |
| 1-2 | 32 |
| 2-0 | 31 |
| 3-1 | 26 |
| 0-0 | 19 |
| 0-1 | 19 |
| 3-2 | 16 |
| 3-0 | 14 |
| 1-3 | 14 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 114 | 25.4% |
| Mon | 12 | 2.7% |
| Tue | 23 | 5.1% |
| Wed | 32 | 7.1% |
| Thu | 8 | 1.8% |
| Fri | 82 | 18.3% |
| Sat | 177 | 39.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 208 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=4, fgte=4 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 208, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 3}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 4530, "distinct": 4528, "duplicates": 2}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 4530, "fgt_inconsistent": 4, "fgte_inconsistent": 4, "n_with_fgt": 4202}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
