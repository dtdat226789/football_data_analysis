# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:04:14+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `primera1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 131 |
| teams | 1297 |
| team_aliases | 2594 |
| team_seasons | 2359 |
| matches | 25316 |
| standings | 6795 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `60`
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
| portugal2 | Liga Portugal 2 | Portugal | 2 | 363 |
| premier | Premier League | England | 7 | 2330 |
| primera1 | Primera RFEF - Group 1 | Spain | 2 | 448 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `primera1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 398 | 21 | 2025-08-29 | 2026-05-23 |
| 2026-2027 | True | in_progress | 50 | 20 | 2026-08-28 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 25316 | 25316 | 0 |
| matches (league_season_id, game_index) | 25316 | 25316 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 25316 | 25302 | 14 |
| team_seasons (league_season_id, team_id) | 2359 | 2359 | 0 |
| team_seasons api_name within a season | 2359 | 2359 | 0 |
| team_seasons api_slug within a season | 2359 | 2359 | 0 |
| standings (league_season_id, team_id, view) | 6795 | 6795 | 0 |
| team_aliases (form, value) | 2594 | 2594 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1297 | 1297 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `25316`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 25316 | 0.0% |
| kickoff_time | 0 | 25316 | 0.0% |
| home_team_id | 0 | 25316 | 0.0% |
| away_team_id | 0 | 25316 | 0.0% |
| home_score | 0 | 25316 | 0.0% |
| away_score | 0 | 25316 | 0.0% |
| home_ht | 47 | 25269 | 0.2% |
| away_ht | 47 | 25269 | 0.2% |
| first_goal_time | 1755 | 23561 | 6.9% |
| first_goal_time_extra | 1755 | 23561 | 6.9% |
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
| Home | 205 | 45.8% |
| Draw | 126 | 28.1% |
| Away | 117 | 26.1% |
| Total | 448 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1107 |
| Average goals per match | 2.471 |
| Home goals | 627 (avg 1.4) |
| Away goals | 480 (avg 1.071) |
| Home goal share | 56.6% |
| Goalless matches | 42 (9.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 398 | 45.7% | 28.4% | 25.9% | 974 | 2.447 | 554 | 420 | 39 (9.8%) |
| 2026-2027 | 50 | 46.0% | 26.0% | 28.0% | 133 | 2.66 | 73 | 60 | 3 (6.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `406` of `448` (90.6%)
| metric | value |
|---|---|
| First goals recorded | 406 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.13 |
| Median (p50) | 29.5 |
| p25 | 14.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 110 |
| 16-30 | 101 |
| 31-45 | 73 |
| 46-60 | 52 |
| 61-75 | 40 |
| 76-90 | 21 |
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
| 1-0 | 60 |
| 1-1 | 57 |
| 2-1 | 45 |
| 0-0 | 42 |
| 2-0 | 38 |
| 0-1 | 32 |
| 1-2 | 25 |
| 2-2 | 23 |
| 3-0 | 19 |
| 0-2 | 19 |
| 3-1 | 15 |
| 1-3 | 10 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-3 | 9 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 198 | 44.2% |
| Mon | 2 | 0.4% |
| Tue | 1 | 0.2% |
| Wed | 3 | 0.7% |
| Fri | 46 | 10.3% |
| Sat | 198 | 44.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 398 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 50 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.0% vs overall 9.4% (deviation 3.4 pp) |
| 6 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 398, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 50, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.0, "overall_goalless_pct": 9.4, "deviation_pp": 3.4}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 25316, "distinct": 25302, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 25316, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 23561}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
