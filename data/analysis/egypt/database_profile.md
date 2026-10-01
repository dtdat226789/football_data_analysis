# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:48:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `egypt`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 37 |
| teams | 402 |
| team_aliases | 804 |
| team_seasons | 661 |
| matches | 6523 |
| standings | 1914 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `18`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `egypt`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 322 | 21 | 2025-08-08 | 2026-05-29 |
| 2026-2027 | True | in_progress | 50 | 20 | 2026-08-21 | 2026-09-17 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 6523 | 6523 | 0 |
| matches (league_season_id, game_index) | 6523 | 6523 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 6523 | 6518 | 5 |
| team_seasons (league_season_id, team_id) | 661 | 661 | 0 |
| team_seasons api_name within a season | 661 | 661 | 0 |
| team_seasons api_slug within a season | 661 | 661 | 0 |
| standings (league_season_id, team_id, view) | 1914 | 1914 | 0 |
| team_aliases (form, value) | 804 | 804 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 402 | 402 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `6523`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 6523 | 0.0% |
| kickoff_time | 0 | 6523 | 0.0% |
| home_team_id | 0 | 6523 | 0.0% |
| away_team_id | 0 | 6523 | 0.0% |
| home_score | 0 | 6523 | 0.0% |
| away_score | 0 | 6523 | 0.0% |
| home_ht | 8 | 6515 | 0.1% |
| away_ht | 8 | 6515 | 0.1% |
| first_goal_time | 479 | 6044 | 7.3% |
| first_goal_time_extra | 479 | 6044 | 7.3% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 128 | 34.4% |
| Draw | 132 | 35.5% |
| Away | 112 | 30.1% |
| Total | 372 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 754 |
| Average goals per match | 2.027 |
| Home goals | 384 (avg 1.032) |
| Away goals | 370 (avg 0.995) |
| Home goal share | 50.9% |
| Goalless matches | 56 (15.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 322 | 33.9% | 37.9% | 28.3% | 651 | 2.022 | 336 | 315 | 51 (15.8%) |
| 2026-2027 | 50 | 38.0% | 20.0% | 42.0% | 103 | 2.06 | 48 | 55 | 5 (10.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `316` of `372` (84.9%)
| metric | value |
|---|---|
| First goals recorded | 316 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 37.3 |
| Median (p50) | 35.5 |
| p25 | 15.75 |
| p75 | 53.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 79 |
| 16-30 | 64 |
| 31-45 | 54 |
| 46-60 | 57 |
| 61-75 | 29 |
| 76-90 | 26 |
| 91-120 | 7 |

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
| 1-1 | 59 |
| 0-0 | 56 |
| 1-0 | 51 |
| 0-1 | 35 |
| 1-2 | 29 |
| 2-1 | 27 |
| 2-0 | 24 |
| 0-2 | 20 |
| 2-2 | 17 |
| 0-3 | 10 |
| 1-3 | 9 |
| 3-1 | 8 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 54 | 14.5% |
| Mon | 47 | 12.6% |
| Tue | 46 | 12.4% |
| Wed | 57 | 15.3% |
| Thu | 48 | 12.9% |
| Fri | 60 | 16.1% |
| Sat | 60 | 16.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 322 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 50 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.0% vs overall 15.1% (deviation 5.1 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 20.0% vs overall 35.5% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 42.0% vs overall 30.1% |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 322, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 50, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.0, "overall_goalless_pct": 15.1, "deviation_pp": 5.1}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 20.0, "overall_share": 35.5}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 42.0, "overall_share": 30.1}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 6523, "distinct": 6518, "duplicates": 5}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 6523, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 6044}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
