# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:03:33+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `morocco`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 107 |
| teams | 1100 |
| team_aliases | 2200 |
| team_seasons | 1901 |
| matches | 19506 |
| standings | 5529 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `52`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `morocco`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2024-2025 | True | complete | 240 | 16 | 2024-08-30 | 2025-05-12 |
| 2025-2026 | True | complete | 248 | 17 | 2025-09-12 | 2026-07-05 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 19506 | 19506 | 0 |
| matches (league_season_id, game_index) | 19506 | 19506 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 19506 | 19492 | 14 |
| team_seasons (league_season_id, team_id) | 1901 | 1901 | 0 |
| team_seasons api_name within a season | 1901 | 1901 | 0 |
| team_seasons api_slug within a season | 1901 | 1901 | 0 |
| standings (league_season_id, team_id, view) | 5529 | 5529 | 0 |
| team_aliases (form, value) | 2200 | 2200 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1100 | 1100 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `19506`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 19506 | 0.0% |
| kickoff_time | 0 | 19506 | 0.0% |
| home_team_id | 0 | 19506 | 0.0% |
| away_team_id | 0 | 19506 | 0.0% |
| home_score | 0 | 19506 | 0.0% |
| away_score | 0 | 19506 | 0.0% |
| home_ht | 40 | 19466 | 0.2% |
| away_ht | 40 | 19466 | 0.2% |
| first_goal_time | 1408 | 18098 | 7.2% |
| first_goal_time_extra | 1408 | 18098 | 7.2% |
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
| Home | 198 | 40.6% |
| Draw | 153 | 31.4% |
| Away | 137 | 28.1% |
| Total | 488 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1094 |
| Average goals per match | 2.242 |
| Home goals | 583 (avg 1.195) |
| Away goals | 511 (avg 1.047) |
| Home goal share | 53.3% |
| Goalless matches | 51 (10.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 240 | 43.3% | 28.3% | 28.3% | 555 | 2.312 | 298 | 257 | 22 (9.2%) |
| 2025-2026 | 248 | 37.9% | 34.3% | 27.8% | 539 | 2.173 | 285 | 254 | 29 (11.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `437` of `488` (89.5%)
| metric | value |
|---|---|
| First goals recorded | 437 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 36.07 |
| Median (p50) | 33.0 |
| p25 | 16.0 |
| p75 | 52.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 106 |
| 16-30 | 100 |
| 31-45 | 76 |
| 46-60 | 82 |
| 61-75 | 36 |
| 76-90 | 25 |
| 91-120 | 12 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `99`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 81 |
| 1-0 | 62 |
| 0-0 | 51 |
| 2-1 | 50 |
| 2-0 | 42 |
| 1-2 | 38 |
| 0-1 | 36 |
| 0-2 | 22 |
| 2-2 | 19 |
| 3-0 | 16 |
| 1-3 | 13 |
| 0-3 | 10 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 165 | 33.8% |
| Mon | 22 | 4.5% |
| Tue | 10 | 2.0% |
| Wed | 54 | 11.1% |
| Thu | 52 | 10.7% |
| Fri | 71 | 14.5% |
| Sat | 114 | 23.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 248 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 5 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 6 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=18, fgte=18 rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 8 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 9 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 248, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `5.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 19506, "distinct": 19492, "duplicates": 14}`
- `6.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 19506, "fgt_inconsistent": 18, "fgte_inconsistent": 18, "n_with_fgt": 18098}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
