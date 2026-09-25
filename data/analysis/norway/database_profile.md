# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:04:03+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `norway`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 113 |
| teams | 1171 |
| team_aliases | 2342 |
| team_seasons | 2029 |
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
- Registered league_seasons for `norway`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 240 | 16 | 2025-03-29 | 2025-11-30 |
| 2026 | True | in_progress | 168 | 16 | 2026-03-14 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 21247 | 21247 | 0 |
| matches (league_season_id, game_index) | 21247 | 21247 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 21247 | 21233 | 14 |
| team_seasons (league_season_id, team_id) | 2029 | 2029 | 0 |
| team_seasons api_name within a season | 2029 | 2029 | 0 |
| team_seasons api_slug within a season | 2029 | 2029 | 0 |
| standings (league_season_id, team_id, view) | 5913 | 5913 | 0 |
| team_aliases (form, value) | 2342 | 2342 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1171 | 1171 | 0 |
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
| Home | 204 | 50.0% |
| Draw | 78 | 19.1% |
| Away | 126 | 30.9% |
| Total | 408 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1293 |
| Average goals per match | 3.169 |
| Home goals | 744 (avg 1.824) |
| Away goals | 549 (avg 1.346) |
| Home goal share | 57.5% |
| Goalless matches | 17 (4.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 49.2% | 18.8% | 32.1% | 762 | 3.175 | 434 | 328 | 11 (4.6%) |
| 2026 | 168 | 51.2% | 19.6% | 29.2% | 531 | 3.161 | 310 | 221 | 6 (3.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `390` of `408` (95.6%)
| metric | value |
|---|---|
| First goals recorded | 390 |
| Min minute | 1 |
| Max minute | 91 |
| Mean minute | 26.31 |
| Median (p50) | 22.0 |
| p25 | 8.0 |
| p75 | 39.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 160 |
| 16-30 | 89 |
| 31-45 | 64 |
| 46-60 | 43 |
| 61-75 | 20 |
| 76-90 | 13 |
| 91-120 | 1 |

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
| 1-1 | 39 |
| 2-1 | 39 |
| 2-0 | 30 |
| 1-0 | 30 |
| 1-2 | 26 |
| 3-1 | 24 |
| 0-2 | 19 |
| 0-1 | 19 |
| 3-0 | 18 |
| 2-2 | 18 |
| 0-0 | 17 |
| 3-2 | 15 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 1 |
| 8-1 | 9 | 1 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 7-1 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 228 | 55.9% |
| Mon | 26 | 6.4% |
| Tue | 2 | 0.5% |
| Wed | 17 | 4.2% |
| Thu | 6 | 1.5% |
| Fri | 32 | 7.8% |
| Sat | 97 | 23.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 168 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 9 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=23, fgte=23 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 168, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 9, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 21247, "distinct": 21233, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 21247, "fgt_inconsistent": 23, "fgte_inconsistent": 23, "n_with_fgt": 19760}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
