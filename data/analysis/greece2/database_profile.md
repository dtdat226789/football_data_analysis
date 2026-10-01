# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:51:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `greece2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 65 |
| teams | 704 |
| team_aliases | 1408 |
| team_seasons | 1192 |
| matches | 11599 |
| standings | 3402 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `31`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `greece2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 265 | 20 | 2025-09-13 | 2026-04-26 |
| 2026-2027 | True | in_progress | 32 | 16 | 2026-09-05 | 2026-09-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 11599 | 11599 | 0 |
| matches (league_season_id, game_index) | 11599 | 11599 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 11599 | 11589 | 10 |
| team_seasons (league_season_id, team_id) | 1192 | 1192 | 0 |
| team_seasons api_name within a season | 1192 | 1192 | 0 |
| team_seasons api_slug within a season | 1192 | 1192 | 0 |
| standings (league_season_id, team_id, view) | 3402 | 3402 | 0 |
| team_aliases (form, value) | 1408 | 1408 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 704 | 704 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `11599`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 11599 | 0.0% |
| kickoff_time | 0 | 11599 | 0.0% |
| home_team_id | 0 | 11599 | 0.0% |
| away_team_id | 0 | 11599 | 0.0% |
| home_score | 0 | 11599 | 0.0% |
| away_score | 0 | 11599 | 0.0% |
| home_ht | 34 | 11565 | 0.3% |
| away_ht | 34 | 11565 | 0.3% |
| first_goal_time | 819 | 10780 | 7.1% |
| first_goal_time_extra | 819 | 10780 | 7.1% |
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
| Home | 138 | 46.5% |
| Draw | 68 | 22.9% |
| Away | 91 | 30.6% |
| Total | 297 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 676 |
| Average goals per match | 2.276 |
| Home goals | 392 (avg 1.32) |
| Away goals | 284 (avg 0.956) |
| Home goal share | 58.0% |
| Goalless matches | 24 (8.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 265 | 44.2% | 23.0% | 32.8% | 607 | 2.291 | 348 | 259 | 21 (7.9%) |
| 2026-2027 | 32 | 65.6% | 21.9% | 12.5% | 69 | 2.156 | 44 | 25 | 3 (9.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `273` of `297` (91.9%)
| metric | value |
|---|---|
| First goals recorded | 273 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 34.59 |
| Median (p50) | 31.0 |
| p25 | 13.0 |
| p75 | 54.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 84 |
| 16-30 | 52 |
| 31-45 | 46 |
| 46-60 | 41 |
| 61-75 | 32 |
| 76-90 | 13 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `108`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 49 |
| 1-1 | 35 |
| 0-1 | 31 |
| 2-0 | 27 |
| 0-0 | 24 |
| 1-2 | 20 |
| 2-1 | 18 |
| 3-0 | 16 |
| 0-2 | 15 |
| 2-2 | 9 |
| 3-1 | 9 |
| 0-3 | 7 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 147 | 49.5% |
| Mon | 14 | 4.7% |
| Wed | 9 | 3.0% |
| Sat | 127 | 42.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 265 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 32 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 65.6% vs overall 46.5% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 12.5% vs overall 30.6% |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 265, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 32, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 65.6, "overall_share": 46.5}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 12.5, "overall_share": 30.6}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 11599, "distinct": 11589, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 11599, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 10780}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
