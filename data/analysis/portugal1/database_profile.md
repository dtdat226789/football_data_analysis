# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:03:24+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `portugal1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 120 |
| teams | 1233 |
| team_aliases | 2466 |
| team_seasons | 2140 |
| matches | 22175 |
| standings | 6138 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `57`
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
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |
| italy3a | Serie C - Group A | Italy | 2 | 450 |
| italy3b | Serie C - Group B | Italy | 2 | 426 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |
| korea1 | K League 1 | South Korea | 2 | 378 |
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |
| lithuania | TOPLYGA | Lithuania | 2 | 324 |
| morocco | Botola Pro | Morocco | 3 | 488 |
| national | National League | England | 2 | 677 |
| north | National League North | England | 2 | 680 |
| norway | Eliteserien | Norway | 2 | 408 |
| poland2 | Division 1 | Poland | 2 | 408 |
| portugal1 | Liga Portugal | Portugal | 2 | 370 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `portugal1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 308 | 19 | 2025-08-08 | 2026-05-28 |
| 2026-2027 | True | in_progress | 62 | 18 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 22175 | 22175 | 0 |
| matches (league_season_id, game_index) | 22175 | 22175 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 22175 | 22161 | 14 |
| team_seasons (league_season_id, team_id) | 2140 | 2140 | 0 |
| team_seasons api_name within a season | 2140 | 2140 | 0 |
| team_seasons api_slug within a season | 2140 | 2140 | 0 |
| standings (league_season_id, team_id, view) | 6138 | 6138 | 0 |
| team_aliases (form, value) | 2466 | 2466 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1233 | 1233 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `22175`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 22175 | 0.0% |
| kickoff_time | 0 | 22175 | 0.0% |
| home_team_id | 0 | 22175 | 0.0% |
| away_team_id | 0 | 22175 | 0.0% |
| home_score | 0 | 22175 | 0.0% |
| away_score | 0 | 22175 | 0.0% |
| home_ht | 47 | 22128 | 0.2% |
| away_ht | 47 | 22128 | 0.2% |
| first_goal_time | 1542 | 20633 | 7.0% |
| first_goal_time_extra | 1542 | 20633 | 7.0% |
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
| Home | 151 | 40.8% |
| Draw | 102 | 27.6% |
| Away | 117 | 31.6% |
| Total | 370 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 993 |
| Average goals per match | 2.684 |
| Home goals | 542 (avg 1.465) |
| Away goals | 451 (avg 1.219) |
| Home goal share | 54.6% |
| Goalless matches | 25 (6.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 308 | 41.2% | 27.3% | 31.5% | 823 | 2.672 | 460 | 363 | 21 (6.8%) |
| 2026-2027 | 62 | 38.7% | 29.0% | 32.3% | 170 | 2.742 | 82 | 88 | 4 (6.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `345` of `370` (93.2%)
| metric | value |
|---|---|
| First goals recorded | 345 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 31.21 |
| Median (p50) | 26.0 |
| p25 | 11.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 120 |
| 16-30 | 67 |
| 31-45 | 64 |
| 46-60 | 44 |
| 61-75 | 30 |
| 76-90 | 16 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `111`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 36 |
| 2-2 | 35 |
| 0-1 | 34 |
| 1-0 | 34 |
| 1-2 | 30 |
| 0-0 | 25 |
| 2-1 | 24 |
| 2-0 | 24 |
| 3-1 | 19 |
| 3-0 | 19 |
| 0-2 | 18 |
| 4-0 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 133 | 35.9% |
| Mon | 48 | 13.0% |
| Tue | 2 | 0.5% |
| Wed | 3 | 0.8% |
| Thu | 3 | 0.8% |
| Fri | 36 | 9.7% |
| Sat | 145 | 39.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 308 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 62 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 308, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 62, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 22175, "distinct": 22161, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 22175, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 20633}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
