# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:58:02+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `estonia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 43 |
| teams | 461 |
| team_aliases | 922 |
| team_seasons | 777 |
| matches | 8098 |
| standings | 2262 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `21`
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
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 34 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 640 |
| eng2 | League Two | England | 2 | 641 |
| estonia | Meistriliiga | Estonia | 2 | 325 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `estonia`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 180 | 10 | 2025-02-28 | 2025-11-08 |
| 2026 | True | in_progress | 145 | 10 | 2026-03-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 8098 | 8098 | 0 |
| matches (league_season_id, game_index) | 8098 | 8098 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 8098 | 8093 | 5 |
| team_seasons (league_season_id, team_id) | 777 | 777 | 0 |
| team_seasons api_name within a season | 777 | 777 | 0 |
| team_seasons api_slug within a season | 777 | 777 | 0 |
| standings (league_season_id, team_id, view) | 2262 | 2262 | 0 |
| team_aliases (form, value) | 922 | 922 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 461 | 461 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `8098`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 8098 | 0.0% |
| kickoff_time | 0 | 8098 | 0.0% |
| home_team_id | 0 | 8098 | 0.0% |
| away_team_id | 0 | 8098 | 0.0% |
| home_score | 0 | 8098 | 0.0% |
| away_score | 0 | 8098 | 0.0% |
| home_ht | 31 | 8067 | 0.4% |
| away_ht | 31 | 8067 | 0.4% |
| first_goal_time | 572 | 7526 | 7.1% |
| first_goal_time_extra | 572 | 7526 | 7.1% |
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
| Home | 151 | 46.5% |
| Draw | 42 | 12.9% |
| Away | 132 | 40.6% |
| Total | 325 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1028 |
| Average goals per match | 3.163 |
| Home goals | 572 (avg 1.76) |
| Away goals | 456 (avg 1.403) |
| Home goal share | 55.6% |
| Goalless matches | 9 (2.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 46.7% | 13.3% | 40.0% | 572 | 3.178 | 313 | 259 | 4 (2.2%) |
| 2026 | 145 | 46.2% | 12.4% | 41.4% | 456 | 3.145 | 259 | 197 | 5 (3.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `316` of `325` (97.2%)
| metric | value |
|---|---|
| First goals recorded | 316 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 27.47 |
| Median (p50) | 22.0 |
| p25 | 10.75 |
| p75 | 38.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 111 |
| 16-30 | 93 |
| 31-45 | 55 |
| 46-60 | 30 |
| 61-75 | 14 |
| 76-90 | 6 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `60`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-2 | 43 |
| 1-0 | 29 |
| 2-1 | 25 |
| 1-3 | 19 |
| 0-1 | 19 |
| 1-1 | 18 |
| 3-1 | 17 |
| 2-0 | 17 |
| 2-2 | 15 |
| 0-2 | 15 |
| 2-3 | 13 |
| 0-3 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-1 | 9 | 1 |
| 0-9 | 9 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 105 | 32.3% |
| Mon | 1 | 0.3% |
| Tue | 21 | 6.5% |
| Wed | 38 | 11.7% |
| Thu | 3 | 0.9% |
| Fri | 35 | 10.8% |
| Sat | 122 | 37.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 145 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 145, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "0-9", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 8098, "distinct": 8093, "duplicates": 5}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 8098, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 7526}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
