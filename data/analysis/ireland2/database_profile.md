# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:31+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `ireland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 81 |
| teams | 832 |
| team_aliases | 1664 |
| team_seasons | 1440 |
| matches | 14212 |
| standings | 4146 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `39`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `ireland2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 179 | 10 | 2025-02-14 | 2025-10-17 |
| 2026 | True | in_progress | 160 | 10 | 2026-02-13 | 2026-09-18 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 14212 | 14212 | 0 |
| matches (league_season_id, game_index) | 14212 | 14212 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 14212 | 14202 | 10 |
| team_seasons (league_season_id, team_id) | 1440 | 1440 | 0 |
| team_seasons api_name within a season | 1440 | 1440 | 0 |
| team_seasons api_slug within a season | 1440 | 1440 | 0 |
| standings (league_season_id, team_id, view) | 4146 | 4146 | 0 |
| team_aliases (form, value) | 1664 | 1664 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 832 | 832 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `14212`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 14212 | 0.0% |
| kickoff_time | 0 | 14212 | 0.0% |
| home_team_id | 0 | 14212 | 0.0% |
| away_team_id | 0 | 14212 | 0.0% |
| home_score | 0 | 14212 | 0.0% |
| away_score | 0 | 14212 | 0.0% |
| home_ht | 36 | 14176 | 0.3% |
| away_ht | 36 | 14176 | 0.3% |
| first_goal_time | 949 | 13263 | 6.7% |
| first_goal_time_extra | 949 | 13263 | 6.7% |
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
| Home | 162 | 47.8% |
| Draw | 79 | 23.3% |
| Away | 98 | 28.9% |
| Total | 339 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 941 |
| Average goals per match | 2.776 |
| Home goals | 541 (avg 1.596) |
| Away goals | 400 (avg 1.18) |
| Home goal share | 57.5% |
| Goalless matches | 19 (5.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 179 | 45.3% | 23.5% | 31.3% | 502 | 2.804 | 279 | 223 | 10 (5.6%) |
| 2026 | 160 | 50.6% | 23.1% | 26.2% | 439 | 2.744 | 262 | 177 | 9 (5.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `319` of `339` (94.1%)
| metric | value |
|---|---|
| First goals recorded | 319 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 30.94 |
| Median (p50) | 25.0 |
| p25 | 10.0 |
| p75 | 48.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 112 |
| 16-30 | 75 |
| 31-45 | 45 |
| 46-60 | 42 |
| 61-75 | 28 |
| 76-90 | 12 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `60`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-1 | 39 |
| 1-1 | 36 |
| 0-1 | 34 |
| 1-0 | 28 |
| 2-0 | 25 |
| 2-2 | 23 |
| 1-2 | 20 |
| 0-0 | 19 |
| 3-1 | 18 |
| 0-2 | 15 |
| 3-2 | 12 |
| 0-3 | 9 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 2 | 0.6% |
| Mon | 35 | 10.3% |
| Tue | 1 | 0.3% |
| Fri | 273 | 80.5% |
| Sat | 28 | 8.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 179 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 160 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 179, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 160, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 14212, "distinct": 14202, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 14212, "fgt_inconsistent": 8, "fgte_inconsistent": 8, "n_with_fgt": 13263}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
