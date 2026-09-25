# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:03:04+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `kuwait`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 101 |
| teams | 1056 |
| team_aliases | 2112 |
| team_seasons | 1827 |
| matches | 18358 |
| standings | 5307 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `49`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `kuwait`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 98 | 10 | 2025-09-12 | 2026-06-29 |
| 2026-2027 | True | in_progress | 18 | 12 | 2026-08-25 | 2026-09-06 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 18358 | 18358 | 0 |
| matches (league_season_id, game_index) | 18358 | 18358 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 18358 | 18344 | 14 |
| team_seasons (league_season_id, team_id) | 1827 | 1827 | 0 |
| team_seasons api_name within a season | 1827 | 1827 | 0 |
| team_seasons api_slug within a season | 1827 | 1827 | 0 |
| standings (league_season_id, team_id, view) | 5307 | 5307 | 0 |
| team_aliases (form, value) | 2112 | 2112 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1056 | 1056 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `18358`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 18358 | 0.0% |
| kickoff_time | 0 | 18358 | 0.0% |
| home_team_id | 0 | 18358 | 0.0% |
| away_team_id | 0 | 18358 | 0.0% |
| home_score | 0 | 18358 | 0.0% |
| away_score | 0 | 18358 | 0.0% |
| home_ht | 39 | 18319 | 0.2% |
| away_ht | 39 | 18319 | 0.2% |
| first_goal_time | 1308 | 17050 | 7.1% |
| first_goal_time_extra | 1308 | 17050 | 7.1% |
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
| Home | 48 | 41.4% |
| Draw | 29 | 25.0% |
| Away | 39 | 33.6% |
| Total | 116 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 311 |
| Average goals per match | 2.681 |
| Home goals | 174 (avg 1.5) |
| Away goals | 137 (avg 1.181) |
| Home goal share | 55.9% |
| Goalless matches | 8 (6.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 98 | 40.8% | 25.5% | 33.7% | 257 | 2.622 | 145 | 112 | 7 (7.1%) |
| 2026-2027 | 18 | 44.4% | 22.2% | 33.3% | 54 | 3.0 | 29 | 25 | 1 (5.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `108` of `116` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 108 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 33.19 |
| Median (p50) | 30.0 |
| p25 | 15.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 30 |
| 16-30 | 26 |
| 31-45 | 21 |
| 46-60 | 19 |
| 61-75 | 7 |
| 76-90 | 4 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `66`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 10 | 1..10 | 10 |
| 2025-2026 | goals | 10 | 1..10 | 10 |
| 2025-2026 | luck | 10 | 1..10 | 10 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 17 |
| 1-0 | 12 |
| 0-2 | 10 |
| 0-1 | 10 |
| 1-2 | 9 |
| 0-0 | 8 |
| 2-1 | 7 |
| 3-0 | 6 |
| 4-1 | 5 |
| 1-3 | 4 |
| 2-0 | 4 |
| 4-0 | 3 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 22 | 19.0% |
| Mon | 15 | 12.9% |
| Tue | 13 | 11.2% |
| Wed | 10 | 8.6% |
| Thu | 16 | 13.8% |
| Fri | 24 | 20.7% |
| Sat | 16 | 13.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 98 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 18 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=10 positions=1..10 teams=10 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 98, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 18, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 18358, "distinct": 18344, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 18358, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 17050}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
