# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:22+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `ireland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 79 |
| teams | 823 |
| team_aliases | 1646 |
| team_seasons | 1420 |
| matches | 13873 |
| standings | 4086 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `38`
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
| finland1 | Veikkausliiga | Finland | 2 | 273 |
| finland2 | Ykkosliiga | Finland | 2 | 255 |
| france1 | Ligue 1 | France | 2 | 355 |
| france2 | Ligue 2 | France | 2 | 373 |
| france3 | Ligue 3 | France | 2 | 371 |
| germany-north | Regionalliga North | Germany | 2 | 408 |
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 449 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 289 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 466 |
| holland3 | Tweede Divisie | Netherlands | 2 | 376 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 338 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `ireland1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 180 | 10 | 2025-02-14 | 2025-11-01 |
| 2026 | True | in_progress | 158 | 10 | 2026-02-06 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 13873 | 13873 | 0 |
| matches (league_season_id, game_index) | 13873 | 13873 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 13873 | 13863 | 10 |
| team_seasons (league_season_id, team_id) | 1420 | 1420 | 0 |
| team_seasons api_name within a season | 1420 | 1420 | 0 |
| team_seasons api_slug within a season | 1420 | 1420 | 0 |
| standings (league_season_id, team_id, view) | 4086 | 4086 | 0 |
| team_aliases (form, value) | 1646 | 1646 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 823 | 823 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `13873`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 13873 | 0.0% |
| kickoff_time | 0 | 13873 | 0.0% |
| home_team_id | 0 | 13873 | 0.0% |
| away_team_id | 0 | 13873 | 0.0% |
| home_score | 0 | 13873 | 0.0% |
| away_score | 0 | 13873 | 0.0% |
| home_ht | 35 | 13838 | 0.3% |
| away_ht | 35 | 13838 | 0.3% |
| first_goal_time | 929 | 12944 | 6.7% |
| first_goal_time_extra | 929 | 12944 | 6.7% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 137 | 40.5% |
| Draw | 103 | 30.5% |
| Away | 98 | 29.0% |
| Total | 338 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 875 |
| Average goals per match | 2.589 |
| Home goals | 483 (avg 1.429) |
| Away goals | 392 (avg 1.16) |
| Home goal share | 55.2% |
| Goalless matches | 30 (8.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 42.8% | 28.9% | 28.3% | 437 | 2.428 | 248 | 189 | 15 (8.3%) |
| 2026 | 158 | 38.0% | 32.3% | 29.7% | 438 | 2.772 | 235 | 203 | 15 (9.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `308` of `338` (91.1%)
| metric | value |
|---|---|
| First goals recorded | 308 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 30.01 |
| Median (p50) | 25.0 |
| p25 | 11.75 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 99 |
| 16-30 | 82 |
| 31-45 | 57 |
| 46-60 | 35 |
| 61-75 | 14 |
| 76-90 | 15 |
| 91-120 | 6 |

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
| 1-1 | 46 |
| 1-0 | 35 |
| 2-1 | 33 |
| 0-0 | 30 |
| 1-2 | 30 |
| 2-0 | 26 |
| 0-1 | 26 |
| 2-2 | 24 |
| 2-3 | 12 |
| 0-2 | 11 |
| 3-0 | 10 |
| 3-2 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 18 | 5.3% |
| Mon | 57 | 16.9% |
| Tue | 1 | 0.3% |
| Wed | 1 | 0.3% |
| Fri | 232 | 68.6% |
| Sat | 29 | 8.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 158 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 158, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 13873, "distinct": 13863, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 13873, "fgt_inconsistent": 7, "fgte_inconsistent": 7, "n_with_fgt": 12944}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
