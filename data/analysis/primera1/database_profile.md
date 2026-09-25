# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:42:23+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `primera1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 130 |
| teams | 1296 |
| team_aliases | 2592 |
| team_seasons | 2358 |
| matches | 25156 |
| standings | 6792 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `60`
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
| poland2 | Division 1 | Poland | 2 | 408 |
| portugal1 | Liga Portugal | Portugal | 2 | 370 |
| portugal2 | Liga Portugal 2 | Portugal | 2 | 363 |
| premier | Premier League | England | 7 | 2330 |
| primera1 | Primera RFEF - Group 1 | Spain | 2 | 438 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `primera1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 398 | 21 | 2025-08-29 | 2026-05-23 |
| 2026-2027 | True | in_progress | 40 | 20 | 2026-08-28 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 25156 | 25156 | 0 |
| matches (league_season_id, game_index) | 25156 | 25156 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 25156 | 25142 | 14 |
| team_seasons (league_season_id, team_id) | 2358 | 2358 | 0 |
| team_seasons api_name within a season | 2358 | 2358 | 0 |
| team_seasons api_slug within a season | 2358 | 2358 | 0 |
| standings (league_season_id, team_id, view) | 6792 | 6792 | 0 |
| team_aliases (form, value) | 2592 | 2592 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1296 | 1296 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `25156`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 25156 | 0.0% |
| kickoff_time | 0 | 25156 | 0.0% |
| home_team_id | 0 | 25156 | 0.0% |
| away_team_id | 0 | 25156 | 0.0% |
| home_score | 0 | 25156 | 0.0% |
| away_score | 0 | 25156 | 0.0% |
| home_ht | 47 | 25109 | 0.2% |
| away_ht | 47 | 25109 | 0.2% |
| first_goal_time | 1744 | 23412 | 6.9% |
| first_goal_time_extra | 1744 | 23412 | 6.9% |
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
| Home | 202 | 46.1% |
| Draw | 122 | 27.9% |
| Away | 114 | 26.0% |
| Total | 438 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1079 |
| Average goals per match | 2.463 |
| Home goals | 614 (avg 1.402) |
| Away goals | 465 (avg 1.062) |
| Home goal share | 56.9% |
| Goalless matches | 41 (9.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 398 | 45.7% | 28.4% | 25.9% | 974 | 2.447 | 554 | 420 | 39 (9.8%) |
| 2026-2027 | 40 | 50.0% | 22.5% | 27.5% | 105 | 2.625 | 60 | 45 | 2 (5.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `397` of `438` (90.6%)
| metric | value |
|---|---|
| First goals recorded | 397 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.09 |
| Median (p50) | 29.0 |
| p25 | 14.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 109 |
| 16-30 | 97 |
| 31-45 | 71 |
| 46-60 | 52 |
| 61-75 | 39 |
| 76-90 | 20 |
| 91-120 | 9 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `123`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 21 | 1..21 | 21 |
| 2025-2026 | goals | 21 | 1..21 | 21 |
| 2025-2026 | luck | 21 | 1..21 | 21 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 58 |
| 1-1 | 56 |
| 2-1 | 45 |
| 0-0 | 41 |
| 2-0 | 37 |
| 0-1 | 31 |
| 1-2 | 25 |
| 2-2 | 22 |
| 3-0 | 19 |
| 0-2 | 19 |
| 3-1 | 15 |
| 1-3 | 10 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-3 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 193 | 44.1% |
| Mon | 2 | 0.5% |
| Tue | 1 | 0.2% |
| Wed | 3 | 0.7% |
| Fri | 46 | 10.5% |
| Sat | 193 | 44.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 398 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 40 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 5.0% vs overall 9.4% (deviation 4.4 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 22.5% vs overall 27.9% |
| 7 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 398, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 40, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 5.0, "overall_goalless_pct": 9.4, "deviation_pp": 4.4}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 22.5, "overall_share": 27.9}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "6-3", "total_goals": 9, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 25156, "distinct": 25142, "duplicates": 14}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 25156, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 23412}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
