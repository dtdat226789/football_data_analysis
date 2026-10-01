# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:46:48+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 24 |
| teams | 284 |
| team_aliases | 568 |
| team_seasons | 458 |
| matches | 4881 |
| standings | 1374 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `12`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 280 | 18 | 2025-07-18 | 2026-05-31 |
| 2026-2027 | True | in_progress | 71 | 16 | 2026-07-25 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 4881 | 4881 | 0 |
| matches (league_season_id, game_index) | 4881 | 4881 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 4881 | 4879 | 2 |
| team_seasons (league_season_id, team_id) | 458 | 458 | 0 |
| team_seasons api_name within a season | 458 | 458 | 0 |
| team_seasons api_slug within a season | 458 | 458 | 0 |
| standings (league_season_id, team_id, view) | 1374 | 1374 | 0 |
| team_aliases (form, value) | 568 | 568 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 284 | 284 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `4881`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 4881 | 0.0% |
| kickoff_time | 0 | 4881 | 0.0% |
| home_team_id | 0 | 4881 | 0.0% |
| away_team_id | 0 | 4881 | 0.0% |
| home_score | 0 | 4881 | 0.0% |
| away_score | 0 | 4881 | 0.0% |
| home_ht | 7 | 4874 | 0.1% |
| away_ht | 7 | 4874 | 0.1% |
| first_goal_time | 356 | 4525 | 7.3% |
| first_goal_time_extra | 356 | 4525 | 7.3% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 150 | 42.7% |
| Draw | 82 | 23.4% |
| Away | 119 | 33.9% |
| Total | 351 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 941 |
| Average goals per match | 2.681 |
| Home goals | 501 (avg 1.427) |
| Away goals | 440 (avg 1.254) |
| Home goal share | 53.2% |
| Goalless matches | 27 (7.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 280 | 42.1% | 23.9% | 33.9% | 740 | 2.643 | 393 | 347 | 23 (8.2%) |
| 2026-2027 | 71 | 45.1% | 21.1% | 33.8% | 201 | 2.831 | 108 | 93 | 4 (5.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `323` of `351` (92.0%)
| metric | value |
|---|---|
| First goals recorded | 323 |
| Min minute | 1 |
| Max minute | 88 |
| Mean minute | 29.83 |
| Median (p50) | 25.0 |
| p25 | 13.0 |
| p75 | 42.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 104 |
| 16-30 | 84 |
| 31-45 | 63 |
| 46-60 | 35 |
| 61-75 | 24 |
| 76-90 | 13 |
| 91-120 | 0 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `102`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 37 |
| 2-0 | 35 |
| 2-1 | 31 |
| 1-0 | 28 |
| 1-2 | 28 |
| 0-0 | 27 |
| 0-1 | 24 |
| 0-2 | 20 |
| 3-1 | 17 |
| 1-3 | 15 |
| 2-2 | 14 |
| 0-3 | 14 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 1 |
| 6-2 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 141 | 40.2% |
| Mon | 1 | 0.3% |
| Tue | 7 | 2.0% |
| Wed | 10 | 2.8% |
| Fri | 6 | 1.7% |
| Sat | 186 | 53.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 280 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 71 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 5.6% vs overall 7.7% (deviation 2.1 pp) |
| 7 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 280, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 71, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 5.6, "overall_goalless_pct": 7.7, "deviation_pp": 2.1}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 4881, "distinct": 4879, "duplicates": 2}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 4881, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 4525}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
