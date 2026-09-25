# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:59:23+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 57 |
| teams | 626 |
| team_aliases | 1252 |
| team_seasons | 1048 |
| matches | 10133 |
| standings | 2970 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `27`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany1`: `2`
- With match data: `0`
- Registered but no data: `['2025-2026', '2026-2027']`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 0 | 18 | - | - |
| 2026-2027 | True | in_progress | 0 | 17 | - | - |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 10133 | 10133 | 0 |
| matches (league_season_id, game_index) | 10133 | 10133 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 10133 | 10123 | 10 |
| team_seasons (league_season_id, team_id) | 1048 | 1048 | 0 |
| team_seasons api_name within a season | 1048 | 1048 | 0 |
| team_seasons api_slug within a season | 1048 | 1048 | 0 |
| standings (league_season_id, team_id, view) | 2970 | 2970 | 0 |
| team_aliases (form, value) | 1252 | 1252 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 626 | 626 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `10133`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 10133 | 0.0% |
| kickoff_time | 0 | 10133 | 0.0% |
| home_team_id | 0 | 10133 | 0.0% |
| away_team_id | 0 | 10133 | 0.0% |
| home_score | 0 | 10133 | 0.0% |
| away_score | 0 | 10133 | 0.0% |
| home_ht | 34 | 10099 | 0.3% |
| away_ht | 34 | 10099 | 0.3% |
| first_goal_time | 722 | 9411 | 7.1% |
| first_goal_time_extra | 722 | 9411 | 7.1% |
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
| Home | 0 | - |
| Draw | 0 | - |
| Away | 0 | - |
| Total | 0 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 0 |
| Average goals per match | None |
| Home goals | 0 (avg None) |
| Away goals | 0 (avg None) |
| Home goal share | - |
| Goalless matches | 0 (-) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `0` of `0` (-)

### 2.5 Standings coverage
- (season, view) pairs present: `0` of `0` expected
- Standings rows total: `0`
- Coverage complete: `True`

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | SEASON_REGISTERED_NO_DATA | Season 2025-2026 is registered but has no match data (declared_by_api=True, state=complete) |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 0 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 4 | SEASON_REGISTERED_NO_DATA | Season 2026-2027 is registered but has no match data (declared_by_api=True, state=in_progress) |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 0 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 17 teams, expected 20 |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
- `1.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2025-2026"}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 0, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `4.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2026-2027"}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 0, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 17, "expected": 20}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 10133, "distinct": 10123, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 10133, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 9411}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
