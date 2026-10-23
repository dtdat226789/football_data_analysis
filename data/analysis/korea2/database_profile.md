# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:00:26+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `korea2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 99 |
| teams | 1045 |
| team_aliases | 2090 |
| team_seasons | 1806 |
| matches | 18368 |
| standings | 5244 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `48`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `korea2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 273 | 28 | 2025-02-22 | 2025-11-23 |
| 2026 | True | in_progress | 220 | 17 | 2026-02-28 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 18368 | 18368 | 0 |
| matches (league_season_id, game_index) | 18368 | 18368 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 18368 | 18354 | 14 |
| team_seasons (league_season_id, team_id) | 1806 | 1806 | 0 |
| team_seasons api_name within a season | 1806 | 1806 | 0 |
| team_seasons api_slug within a season | 1806 | 1806 | 0 |
| standings (league_season_id, team_id, view) | 5244 | 5244 | 0 |
| team_aliases (form, value) | 2090 | 2090 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1045 | 1045 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `18368`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 18368 | 0.0% |
| kickoff_time | 0 | 18368 | 0.0% |
| home_team_id | 0 | 18368 | 0.0% |
| away_team_id | 0 | 18368 | 0.0% |
| home_score | 0 | 18368 | 0.0% |
| away_score | 0 | 18368 | 0.0% |
| home_ht | 39 | 18329 | 0.2% |
| away_ht | 39 | 18329 | 0.2% |
| first_goal_time | 1310 | 17058 | 7.1% |
| first_goal_time_extra | 1310 | 17058 | 7.1% |
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
| Home | 173 | 35.1% |
| Draw | 153 | 31.0% |
| Away | 167 | 33.9% |
| Total | 493 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1274 |
| Average goals per match | 2.584 |
| Home goals | 662 (avg 1.343) |
| Away goals | 612 (avg 1.241) |
| Home goal share | 52.0% |
| Goalless matches | 42 (8.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 273 | 35.2% | 29.3% | 35.5% | 686 | 2.513 | 360 | 326 | 26 (9.5%) |
| 2026 | 220 | 35.0% | 33.2% | 31.8% | 588 | 2.673 | 302 | 286 | 16 (7.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `451` of `493` (91.5%)
| metric | value |
|---|---|
| First goals recorded | 451 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 34.81 |
| Median (p50) | 30.0 |
| p25 | 13.5 |
| p75 | 50.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 134 |
| 16-30 | 92 |
| 31-45 | 83 |
| 46-60 | 65 |
| 61-75 | 38 |
| 76-90 | 30 |
| 91-120 | 9 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `135`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 28 | 1..28 | 28 |
| 2025 | goals | 28 | 1..28 | 28 |
| 2025 | luck | 28 | 1..28 | 28 |
| 2026 | classic | 17 | 1..17 | 17 |
| 2026 | goals | 17 | 1..17 | 17 |
| 2026 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 64 |
| 0-1 | 56 |
| 0-0 | 42 |
| 2-2 | 42 |
| 1-0 | 41 |
| 2-1 | 36 |
| 1-2 | 35 |
| 2-0 | 29 |
| 0-2 | 24 |
| 1-3 | 17 |
| 3-1 | 16 |
| 3-0 | 15 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 217 | 44.0% |
| Mon | 5 | 1.0% |
| Tue | 2 | 0.4% |
| Wed | 5 | 1.0% |
| Fri | 22 | 4.5% |
| Sat | 242 | 49.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 273 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 28 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 220 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 17 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=28 positions=1..28 teams=28 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=28 positions=1..28 teams=28 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=28 positions=1..28 teams=28 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=17 positions=1..17 teams=17 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=17 positions=1..17 teams=17 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 273, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 28, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 220, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 17, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 18368, "distinct": 18354, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 18368, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 17058}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 28, "min_pos": 1, "max_pos": 28, "distinct_teams": 28}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 28, "min_pos": 1, "max_pos": 28, "distinct_teams": 28}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 28, "min_pos": 1, "max_pos": 28, "distinct_teams": 28}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
