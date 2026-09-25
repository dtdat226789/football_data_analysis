# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:55:03+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `azer`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 3 |
| league_seasons | 10 |
| teams | 76 |
| team_aliases | 152 |
| team_seasons | 138 |
| matches | 1344 |
| standings | 414 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `5`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `azer`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 200 | 13 | 2025-08-15 | 2026-05-28 |
| 2026-2027 | True | in_progress | 34 | 12 | 2026-08-14 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 1344 | 1344 | 0 |
| matches (league_season_id, game_index) | 1344 | 1344 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 1344 | 1342 | 2 |
| team_seasons (league_season_id, team_id) | 138 | 138 | 0 |
| team_seasons api_name within a season | 138 | 138 | 0 |
| team_seasons api_slug within a season | 138 | 138 | 0 |
| standings (league_season_id, team_id, view) | 414 | 414 | 0 |
| team_aliases (form, value) | 152 | 152 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 3 | 3 | 0 |
| teams.canonical_name | 76 | 76 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `1344`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 1344 | 0.0% |
| kickoff_time | 0 | 1344 | 0.0% |
| home_team_id | 0 | 1344 | 0.0% |
| away_team_id | 0 | 1344 | 0.0% |
| home_score | 0 | 1344 | 0.0% |
| away_score | 0 | 1344 | 0.0% |
| home_ht | 3 | 1341 | 0.2% |
| away_ht | 3 | 1341 | 0.2% |
| first_goal_time | 93 | 1251 | 6.9% |
| first_goal_time_extra | 93 | 1251 | 6.9% |
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
| Home | 93 | 39.7% |
| Draw | 56 | 23.9% |
| Away | 85 | 36.3% |
| Total | 234 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 600 |
| Average goals per match | 2.564 |
| Home goals | 312 (avg 1.333) |
| Away goals | 288 (avg 1.231) |
| Home goal share | 52.0% |
| Goalless matches | 21 (9.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 200 | 37.5% | 24.5% | 38.0% | 515 | 2.575 | 261 | 254 | 18 (9.0%) |
| 2026-2027 | 34 | 52.9% | 20.6% | 26.5% | 85 | 2.5 | 51 | 34 | 3 (8.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `212` of `234` (90.6%)
| metric | value |
|---|---|
| First goals recorded | 212 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.83 |
| Median (p50) | 32.0 |
| p25 | 15.0 |
| p75 | 51.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 58 |
| 16-30 | 42 |
| 31-45 | 43 |
| 46-60 | 38 |
| 61-75 | 20 |
| 76-90 | 9 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `75`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 13 | 1..13 | 13 |
| 2025-2026 | goals | 13 | 1..13 | 13 |
| 2025-2026 | luck | 13 | 1..13 | 13 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 25 |
| 1-1 | 24 |
| 0-1 | 22 |
| 0-0 | 21 |
| 2-1 | 19 |
| 2-0 | 16 |
| 0-2 | 14 |
| 1-2 | 13 |
| 0-3 | 12 |
| 2-2 | 10 |
| 1-3 | 9 |
| 3-0 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 73 | 31.2% |
| Mon | 21 | 9.0% |
| Tue | 11 | 4.7% |
| Wed | 1 | 0.4% |
| Thu | 6 | 2.6% |
| Fri | 52 | 22.2% |
| Sat | 70 | 29.9% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 200 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 13 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 34 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 52.9% vs overall 39.7% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 26.5% vs overall 36.3% |
| 8 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=13 positions=1..13 teams=13 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=13 positions=1..13 teams=13 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=13 positions=1..13 teams=13 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 200, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 13, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 34, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 52.9, "overall_share": 39.7}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 26.5, "overall_share": 36.3}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 1344, "distinct": 1342, "duplicates": 2}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 1344, "fgt_inconsistent": 2, "fgte_inconsistent": 2, "n_with_fgt": 1251}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
