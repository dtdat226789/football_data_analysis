# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:46:09+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `cha`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 20 |
| teams | 247 |
| team_aliases | 494 |
| team_seasons | 392 |
| matches | 4082 |
| standings | 1176 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `10`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `cha`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 559 | 24 | 2025-08-08 | 2026-05-23 |
| 2026-2027 | True | in_progress | 95 | 24 | 2026-08-14 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 4082 | 4082 | 0 |
| matches (league_season_id, game_index) | 4082 | 4082 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 4082 | 4080 | 2 |
| team_seasons (league_season_id, team_id) | 392 | 392 | 0 |
| team_seasons api_name within a season | 392 | 392 | 0 |
| team_seasons api_slug within a season | 392 | 392 | 0 |
| standings (league_season_id, team_id, view) | 1176 | 1176 | 0 |
| team_aliases (form, value) | 494 | 494 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 247 | 247 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `4082`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 4082 | 0.0% |
| kickoff_time | 0 | 4082 | 0.0% |
| home_team_id | 0 | 4082 | 0.0% |
| away_team_id | 0 | 4082 | 0.0% |
| home_score | 0 | 4082 | 0.0% |
| away_score | 0 | 4082 | 0.0% |
| home_ht | 6 | 4076 | 0.1% |
| away_ht | 6 | 4076 | 0.1% |
| first_goal_time | 309 | 3773 | 7.6% |
| first_goal_time_extra | 309 | 3773 | 7.6% |
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
| Home | 272 | 41.6% |
| Draw | 178 | 27.2% |
| Away | 204 | 31.2% |
| Total | 654 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1722 |
| Average goals per match | 2.633 |
| Home goals | 933 (avg 1.427) |
| Away goals | 789 (avg 1.206) |
| Home goal share | 54.2% |
| Goalless matches | 44 (6.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 559 | 41.7% | 26.7% | 31.7% | 1445 | 2.585 | 777 | 668 | 37 (6.6%) |
| 2026-2027 | 95 | 41.1% | 30.5% | 28.4% | 277 | 2.916 | 156 | 121 | 7 (7.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `609` of `654` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 609 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 29.57 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 215 |
| 16-30 | 147 |
| 31-45 | 99 |
| 46-60 | 78 |
| 61-75 | 40 |
| 76-90 | 24 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `144`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 94 |
| 2-1 | 73 |
| 1-0 | 64 |
| 1-2 | 59 |
| 0-1 | 46 |
| 0-0 | 44 |
| 2-2 | 38 |
| 3-1 | 35 |
| 0-2 | 32 |
| 2-0 | 32 |
| 1-3 | 25 |
| 3-0 | 24 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |
| 5-3 | 8 | 2 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 29 | 4.4% |
| Mon | 34 | 5.2% |
| Tue | 102 | 15.6% |
| Wed | 47 | 7.2% |
| Thu | 12 | 1.8% |
| Fri | 56 | 8.6% |
| Sat | 374 | 57.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 559 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 95 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=4, fgte=4 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 559, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 95, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 4082, "distinct": 4080, "duplicates": 2}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 4082, "fgt_inconsistent": 4, "fgte_inconsistent": 4, "n_with_fgt": 3773}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
