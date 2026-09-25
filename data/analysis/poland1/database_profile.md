# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:40:51+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `poland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 115 |
| teams | 1192 |
| team_aliases | 2384 |
| team_seasons | 2065 |
| matches | 21247 |
| standings | 5913 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `55`
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
| ireland2 | Division 1 | Ireland | 2 | 339 |
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |
| italy3a | Serie C - Group A | Italy | 2 | 440 |
| italy3b | Serie C - Group B | Italy | 2 | 417 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |
| korea1 | K League 1 | South Korea | 2 | 377 |
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |
| lithuania | TOPLYGA | Lithuania | 2 | 324 |
| morocco | Botola Pro | Morocco | 2 | 488 |
| national | National League | England | 2 | 665 |
| north | National League North | England | 2 | 668 |
| norway | Eliteserien | Norway | 2 | 408 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `poland1`: `2`
- With match data: `0`
- Registered but no data: `['2025-2026', '2026-2027']`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 0 | 18 | - | - |
| 2026-2027 | True | in_progress | 0 | 18 | - | - |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 21247 | 21247 | 0 |
| matches (league_season_id, game_index) | 21247 | 21247 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 21247 | 21233 | 14 |
| team_seasons (league_season_id, team_id) | 2065 | 2065 | 0 |
| team_seasons api_name within a season | 2065 | 2065 | 0 |
| team_seasons api_slug within a season | 2065 | 2065 | 0 |
| standings (league_season_id, team_id, view) | 5913 | 5913 | 0 |
| team_aliases (form, value) | 2384 | 2384 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1192 | 1192 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `21247`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 21247 | 0.0% |
| kickoff_time | 0 | 21247 | 0.0% |
| home_team_id | 0 | 21247 | 0.0% |
| away_team_id | 0 | 21247 | 0.0% |
| home_score | 0 | 21247 | 0.0% |
| away_score | 0 | 21247 | 0.0% |
| home_ht | 46 | 21201 | 0.2% |
| away_ht | 46 | 21201 | 0.2% |
| first_goal_time | 1487 | 19760 | 7.0% |
| first_goal_time_extra | 1487 | 19760 | 7.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 6 |
| away_ht | 0 | 6 |
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
| 6 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=23, fgte=23 rows) |
- `1.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2025-2026"}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 0, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `4.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2026-2027"}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 0, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 21247, "distinct": 21233, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 21247, "fgt_inconsistent": 23, "fgte_inconsistent": 23, "n_with_fgt": 19760}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
