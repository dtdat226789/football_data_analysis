# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:48:01+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `denmark2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 34 |
| teams | 361 |
| team_aliases | 722 |
| team_seasons | 603 |
| matches | 6111 |
| standings | 1740 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `16`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `denmark2`: `2`
- With match data: `0`
- Registered but no data: `['2025-2026', '2026-2027']`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 0 | 11 | - | - |
| 2026-2027 | True | in_progress | 0 | 12 | - | - |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 6111 | 6111 | 0 |
| matches (league_season_id, game_index) | 6111 | 6111 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 6111 | 6106 | 5 |
| team_seasons (league_season_id, team_id) | 603 | 603 | 0 |
| team_seasons api_name within a season | 603 | 603 | 0 |
| team_seasons api_slug within a season | 603 | 603 | 0 |
| standings (league_season_id, team_id, view) | 1740 | 1740 | 0 |
| team_aliases (form, value) | 722 | 722 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 361 | 361 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `6111`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 6111 | 0.0% |
| kickoff_time | 0 | 6111 | 0.0% |
| home_team_id | 0 | 6111 | 0.0% |
| away_team_id | 0 | 6111 | 0.0% |
| home_score | 0 | 6111 | 0.0% |
| away_score | 0 | 6111 | 0.0% |
| home_ht | 8 | 6103 | 0.1% |
| away_ht | 8 | 6103 | 0.1% |
| first_goal_time | 422 | 5689 | 6.9% |
| first_goal_time_extra | 422 | 5689 | 6.9% |
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
| 3 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 11 teams, expected 20 |
| 4 | SEASON_REGISTERED_NO_DATA | Season 2026-2027 is registered but has no match data (declared_by_api=True, state=in_progress) |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 0 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
- `1.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2025-2026"}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 0, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 11, "expected": 20}`
- `4.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2026-2027"}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 0, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 6111, "distinct": 6106, "duplicates": 5}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 6111, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 5689}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
