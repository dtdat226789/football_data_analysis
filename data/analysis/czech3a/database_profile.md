# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:47:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech3a`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 28 |
| teams | 318 |
| team_aliases | 636 |
| team_seasons | 523 |
| matches | 5530 |
| standings | 1569 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `14`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech3a`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 272 | 17 | 2025-08-08 | 2026-06-06 |
| 2026-2027 | True | in_progress | 65 | 16 | 2026-08-07 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 5530 | 5530 | 0 |
| matches (league_season_id, game_index) | 5530 | 5530 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 5530 | 5527 | 3 |
| team_seasons (league_season_id, team_id) | 523 | 523 | 0 |
| team_seasons api_name within a season | 523 | 523 | 0 |
| team_seasons api_slug within a season | 523 | 523 | 0 |
| standings (league_season_id, team_id, view) | 1569 | 1569 | 0 |
| team_aliases (form, value) | 636 | 636 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 318 | 318 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `5530`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 5530 | 0.0% |
| kickoff_time | 0 | 5530 | 0.0% |
| home_team_id | 0 | 5530 | 0.0% |
| away_team_id | 0 | 5530 | 0.0% |
| home_score | 0 | 5530 | 0.0% |
| away_score | 0 | 5530 | 0.0% |
| home_ht | 8 | 5522 | 0.1% |
| away_ht | 8 | 5522 | 0.1% |
| first_goal_time | 398 | 5132 | 7.2% |
| first_goal_time_extra | 398 | 5132 | 7.2% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 7 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 149 | 44.2% |
| Draw | 76 | 22.6% |
| Away | 112 | 33.2% |
| Total | 337 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1085 |
| Average goals per match | 3.22 |
| Home goals | 583 (avg 1.73) |
| Away goals | 502 (avg 1.49) |
| Home goal share | 53.7% |
| Goalless matches | 24 (7.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 272 | 45.6% | 21.0% | 33.5% | 869 | 3.195 | 464 | 405 | 17 (6.2%) |
| 2026-2027 | 65 | 38.5% | 29.2% | 32.3% | 216 | 3.323 | 119 | 97 | 7 (10.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `313` of `337` (92.9%)
| metric | value |
|---|---|
| First goals recorded | 313 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 26.37 |
| Median (p50) | 19.0 |
| p25 | 9.0 |
| p75 | 39.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 130 |
| 16-30 | 77 |
| 31-45 | 44 |
| 46-60 | 36 |
| 61-75 | 12 |
| 76-90 | 13 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `99`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 27 |
| 1-0 | 25 |
| 0-0 | 24 |
| 2-2 | 22 |
| 3-1 | 22 |
| 2-1 | 20 |
| 2-0 | 20 |
| 0-1 | 19 |
| 1-3 | 18 |
| 0-2 | 17 |
| 1-2 | 17 |
| 3-2 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 3-6 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 3-5 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 106 | 31.5% |
| Tue | 1 | 0.3% |
| Wed | 27 | 8.0% |
| Thu | 2 | 0.6% |
| Fri | 36 | 10.7% |
| Sat | 165 | 49.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 272 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 65 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.8% vs overall 7.1% (deviation 3.7 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 38.5% vs overall 44.2% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 29.2% vs overall 22.6% |
| 9 | HIGH_SCORING_MATCHES | 8 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (3 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 272, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 65, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.8, "overall_goalless_pct": 7.1, "deviation_pp": 3.7}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 38.5, "overall_share": 44.2}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 29.2, "overall_share": 22.6}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 8, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 3}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 5530, "distinct": 5527, "duplicates": 3}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 5530, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 5132}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
