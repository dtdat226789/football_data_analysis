# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:00:10+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `greece2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 65 |
| teams | 703 |
| team_aliases | 1406 |
| team_seasons | 1191 |
| matches | 11516 |
| standings | 3399 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `31`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `greece2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 265 | 20 | 2025-09-13 | 2026-04-26 |
| 2026-2027 | True | in_progress | 24 | 16 | 2026-09-05 | 2026-09-21 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 11516 | 11516 | 0 |
| matches (league_season_id, game_index) | 11516 | 11516 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 11516 | 11506 | 10 |
| team_seasons (league_season_id, team_id) | 1191 | 1191 | 0 |
| team_seasons api_name within a season | 1191 | 1191 | 0 |
| team_seasons api_slug within a season | 1191 | 1191 | 0 |
| standings (league_season_id, team_id, view) | 3399 | 3399 | 0 |
| team_aliases (form, value) | 1406 | 1406 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 703 | 703 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `11516`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 11516 | 0.0% |
| kickoff_time | 0 | 11516 | 0.0% |
| home_team_id | 0 | 11516 | 0.0% |
| away_team_id | 0 | 11516 | 0.0% |
| home_score | 0 | 11516 | 0.0% |
| away_score | 0 | 11516 | 0.0% |
| home_ht | 34 | 11482 | 0.3% |
| away_ht | 34 | 11482 | 0.3% |
| first_goal_time | 813 | 10703 | 7.1% |
| first_goal_time_extra | 813 | 10703 | 7.1% |
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
| Home | 131 | 45.3% |
| Draw | 67 | 23.2% |
| Away | 91 | 31.5% |
| Total | 289 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 661 |
| Average goals per match | 2.287 |
| Home goals | 379 (avg 1.311) |
| Away goals | 282 (avg 0.976) |
| Home goal share | 57.3% |
| Goalless matches | 23 (8.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 265 | 44.2% | 23.0% | 32.8% | 607 | 2.291 | 348 | 259 | 21 (7.9%) |
| 2026-2027 | 24 | 58.3% | 25.0% | 16.7% | 54 | 2.25 | 31 | 23 | 2 (8.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `266` of `289` (92.0%)
| metric | value |
|---|---|
| First goals recorded | 266 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 34.61 |
| Median (p50) | 31.0 |
| p25 | 13.0 |
| p75 | 53.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 81 |
| 16-30 | 51 |
| 31-45 | 46 |
| 46-60 | 40 |
| 61-75 | 31 |
| 76-90 | 12 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `108`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 46 |
| 1-1 | 35 |
| 0-1 | 31 |
| 2-0 | 25 |
| 0-0 | 23 |
| 1-2 | 20 |
| 2-1 | 17 |
| 3-0 | 16 |
| 0-2 | 15 |
| 2-2 | 9 |
| 3-1 | 9 |
| 0-3 | 7 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 141 | 48.8% |
| Mon | 12 | 4.2% |
| Wed | 9 | 3.1% |
| Sat | 127 | 43.9% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 265 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 24 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 58.3% vs overall 45.3% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 16.7% vs overall 31.5% |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 265, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 24, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 58.3, "overall_share": 45.3}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 16.7, "overall_share": 31.5}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 11516, "distinct": 11506, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 11516, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 10703}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
