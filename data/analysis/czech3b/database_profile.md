# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:56:45+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech3b`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 30 |
| teams | 336 |
| team_aliases | 672 |
| team_seasons | 556 |
| matches | 5838 |
| standings | 1668 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `15`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 669 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 330 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 326 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech3b`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 272 | 17 | 2025-08-09 | 2026-06-07 |
| 2026-2027 | True | in_progress | 54 | 16 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 5838 | 5838 | 0 |
| matches (league_season_id, game_index) | 5838 | 5838 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 5838 | 5834 | 4 |
| team_seasons (league_season_id, team_id) | 556 | 556 | 0 |
| team_seasons api_name within a season | 556 | 556 | 0 |
| team_seasons api_slug within a season | 556 | 556 | 0 |
| standings (league_season_id, team_id, view) | 1668 | 1668 | 0 |
| team_aliases (form, value) | 672 | 672 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 336 | 336 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `5838`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 5838 | 0.0% |
| kickoff_time | 0 | 5838 | 0.0% |
| home_team_id | 0 | 5838 | 0.0% |
| away_team_id | 0 | 5838 | 0.0% |
| home_score | 0 | 5838 | 0.0% |
| away_score | 0 | 5838 | 0.0% |
| home_ht | 8 | 5830 | 0.1% |
| away_ht | 8 | 5830 | 0.1% |
| first_goal_time | 408 | 5430 | 7.0% |
| first_goal_time_extra | 408 | 5430 | 7.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 140 | 42.9% |
| Draw | 76 | 23.3% |
| Away | 110 | 33.7% |
| Total | 326 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1079 |
| Average goals per match | 3.31 |
| Home goals | 588 (avg 1.804) |
| Away goals | 491 (avg 1.506) |
| Home goal share | 54.5% |
| Goalless matches | 12 (3.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 44.1% | 22.1% | 33.8% | 912 | 3.353 | 495 | 417 | 7 (2.6%) |
| 2026-2027 | 54 | 37.0% | 29.6% | 33.3% | 167 | 3.093 | 93 | 74 | 5 (9.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `314` of `326` (96.3%)
| metric | value |
|---|---|
| First goals recorded | 314 |
| Min minute | 1 |
| Max minute | 91 |
| Mean minute | 25.77 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 38.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 121 |
| 16-30 | 86 |
| 31-45 | 56 |
| 46-60 | 33 |
| 61-75 | 8 |
| 76-90 | 9 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `99`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 36 |
| 1-2 | 23 |
| 2-0 | 22 |
| 1-0 | 21 |
| 2-2 | 20 |
| 2-1 | 20 |
| 0-2 | 17 |
| 3-0 | 17 |
| 0-1 | 16 |
| 2-3 | 13 |
| 0-0 | 12 |
| 3-1 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-9 | 11 | 1 |
| 8-1 | 9 | 1 |
| 3-6 | 9 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 145 | 44.5% |
| Tue | 1 | 0.3% |
| Wed | 31 | 9.5% |
| Thu | 4 | 1.2% |
| Fri | 9 | 2.8% |
| Sat | 136 | 41.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 272 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 54 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 9.3% vs overall 3.7% (deviation 5.6 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 37.0% vs overall 42.9% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 29.6% vs overall 23.3% |
| 9 | HIGH_SCORING_MATCHES | 9 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (4 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 272, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 54, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 9.3, "overall_goalless_pct": 3.7, "deviation_pp": 5.6}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 37.0, "overall_share": 42.9}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 29.6, "overall_share": 23.3}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 9, "threshold": 8, "examples": [{"scoreline": "2-9", "total_goals": 11, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 5838, "distinct": 5834, "duplicates": 4}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 5838, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 5430}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
