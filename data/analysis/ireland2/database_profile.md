# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:55:55+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `ireland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 81 |
| teams | 833 |
| team_aliases | 1666 |
| team_seasons | 1441 |
| matches | 14318 |
| standings | 4149 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `39`
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
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 337 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 333 |
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 40 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 644 |
| eng2 | League Two | England | 2 | 651 |
| estonia | Meistriliiga | Estonia | 2 | 325 |
| finland1 | Veikkausliiga | Finland | 2 | 273 |
| finland2 | Ykkosliiga | Finland | 2 | 260 |
| france1 | Ligue 1 | France | 2 | 355 |
| france2 | Ligue 2 | France | 2 | 373 |
| france3 | Ligue 3 | France | 2 | 388 |
| germany-north | Regionalliga North | Germany | 2 | 415 |
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 450 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 297 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 474 |
| holland3 | Tweede Divisie | Netherlands | 2 | 385 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 339 |
| ireland2 | Division 1 | Ireland | 2 | 344 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `ireland2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 179 | 10 | 2025-02-14 | 2025-10-17 |
| 2026 | True | in_progress | 165 | 10 | 2026-02-13 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 14318 | 14318 | 0 |
| matches (league_season_id, game_index) | 14318 | 14318 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 14318 | 14308 | 10 |
| team_seasons (league_season_id, team_id) | 1441 | 1441 | 0 |
| team_seasons api_name within a season | 1441 | 1441 | 0 |
| team_seasons api_slug within a season | 1441 | 1441 | 0 |
| standings (league_season_id, team_id, view) | 4149 | 4149 | 0 |
| team_aliases (form, value) | 1666 | 1666 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 833 | 833 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `14318`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 14318 | 0.0% |
| kickoff_time | 0 | 14318 | 0.0% |
| home_team_id | 0 | 14318 | 0.0% |
| away_team_id | 0 | 14318 | 0.0% |
| home_score | 0 | 14318 | 0.0% |
| away_score | 0 | 14318 | 0.0% |
| home_ht | 36 | 14282 | 0.3% |
| away_ht | 36 | 14282 | 0.3% |
| first_goal_time | 955 | 13363 | 6.7% |
| first_goal_time_extra | 955 | 13363 | 6.7% |
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
| Home | 165 | 48.0% |
| Draw | 80 | 23.3% |
| Away | 99 | 28.8% |
| Total | 344 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 958 |
| Average goals per match | 2.785 |
| Home goals | 550 (avg 1.599) |
| Away goals | 408 (avg 1.186) |
| Home goal share | 57.4% |
| Goalless matches | 19 (5.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 179 | 45.3% | 23.5% | 31.3% | 502 | 2.804 | 279 | 223 | 10 (5.6%) |
| 2026 | 165 | 50.9% | 23.0% | 26.1% | 456 | 2.764 | 271 | 185 | 9 (5.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `324` of `344` (94.2%)
| metric | value |
|---|---|
| First goals recorded | 324 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 31.07 |
| Median (p50) | 25.5 |
| p25 | 10.0 |
| p75 | 48.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 113 |
| 16-30 | 76 |
| 31-45 | 46 |
| 46-60 | 43 |
| 61-75 | 29 |
| 76-90 | 12 |
| 91-120 | 5 |

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
| 2-1 | 41 |
| 1-1 | 36 |
| 0-1 | 34 |
| 1-0 | 29 |
| 2-0 | 25 |
| 2-2 | 23 |
| 1-2 | 20 |
| 0-0 | 19 |
| 3-1 | 18 |
| 0-2 | 15 |
| 3-2 | 12 |
| 0-3 | 9 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 2 | 0.6% |
| Mon | 35 | 10.2% |
| Tue | 1 | 0.3% |
| Fri | 277 | 80.5% |
| Sat | 29 | 8.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 179 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 165 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 179, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 165, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 14318, "distinct": 14308, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 14318, "fgt_inconsistent": 8, "fgte_inconsistent": 8, "n_with_fgt": 13363}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
