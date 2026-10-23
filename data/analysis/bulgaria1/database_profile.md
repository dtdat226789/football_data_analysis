# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:45:53+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `bulgaria1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 18 |
| teams | 217 |
| team_aliases | 434 |
| team_seasons | 344 |
| matches | 3428 |
| standings | 1032 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `9`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `bulgaria1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 294 | 17 | 2025-07-18 | 2026-05-29 |
| 2026-2027 | True | in_progress | 69 | 14 | 2026-07-17 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 3428 | 3428 | 0 |
| matches (league_season_id, game_index) | 3428 | 3428 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 3428 | 3426 | 2 |
| team_seasons (league_season_id, team_id) | 344 | 344 | 0 |
| team_seasons api_name within a season | 344 | 344 | 0 |
| team_seasons api_slug within a season | 344 | 344 | 0 |
| standings (league_season_id, team_id, view) | 1032 | 1032 | 0 |
| team_aliases (form, value) | 434 | 434 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 217 | 217 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `3428`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 3428 | 0.0% |
| kickoff_time | 0 | 3428 | 0.0% |
| home_team_id | 0 | 3428 | 0.0% |
| away_team_id | 0 | 3428 | 0.0% |
| home_score | 0 | 3428 | 0.0% |
| away_score | 0 | 3428 | 0.0% |
| home_ht | 4 | 3424 | 0.1% |
| away_ht | 4 | 3424 | 0.1% |
| first_goal_time | 264 | 3164 | 7.7% |
| first_goal_time_extra | 264 | 3164 | 7.7% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 4 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 156 | 43.0% |
| Draw | 99 | 27.3% |
| Away | 108 | 29.8% |
| Total | 363 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 861 |
| Average goals per match | 2.372 |
| Home goals | 471 (avg 1.298) |
| Away goals | 390 (avg 1.074) |
| Home goal share | 54.7% |
| Goalless matches | 39 (10.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 294 | 42.5% | 27.9% | 29.6% | 677 | 2.303 | 369 | 308 | 36 (12.2%) |
| 2026-2027 | 69 | 44.9% | 24.6% | 30.4% | 184 | 2.667 | 102 | 82 | 3 (4.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `323` of `363` (89.0%)
| metric | value |
|---|---|
| First goals recorded | 323 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 33.35 |
| Median (p50) | 29.0 |
| p25 | 12.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 97 |
| 16-30 | 71 |
| 31-45 | 56 |
| 46-60 | 48 |
| 61-75 | 32 |
| 76-90 | 14 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `93`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 14 | 1..14 | 14 |
| 2026-2027 | goals | 14 | 1..14 | 14 |
| 2026-2027 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 45 |
| 1-0 | 43 |
| 0-0 | 39 |
| 2-1 | 38 |
| 0-1 | 29 |
| 2-0 | 27 |
| 1-2 | 21 |
| 0-2 | 16 |
| 3-0 | 15 |
| 2-2 | 15 |
| 1-3 | 13 |
| 0-3 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 93 | 25.6% |
| Mon | 57 | 15.7% |
| Tue | 15 | 4.1% |
| Wed | 16 | 4.4% |
| Thu | 18 | 5.0% |
| Fri | 69 | 19.0% |
| Sat | 95 | 26.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 294 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 69 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 14 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.3% vs overall 10.7% (deviation 6.4 pp) |
| 7 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=3, fgte=3 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=14 positions=1..14 teams=14 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=14 positions=1..14 teams=14 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 294, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 69, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 14, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.3, "overall_goalless_pct": 10.7, "deviation_pp": 6.4}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 3428, "distinct": 3426, "duplicates": 2}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 3428, "fgt_inconsistent": 3, "fgte_inconsistent": 3, "n_with_fgt": 3164}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
