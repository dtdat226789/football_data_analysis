# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:54:23+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `algir1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 2 |
| league_seasons | 2 |
| teams | 19 |
| team_aliases | 38 |
| team_seasons | 32 |
| matches | 262 |
| standings | 96 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `1`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `algir1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 240 | 16 | 2025-08-21 | 2026-06-06 |
| 2026-2027 | True | in_progress | 22 | 16 | 2026-09-03 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 262 | 262 | 0 |
| matches (league_season_id, game_index) | 262 | 262 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 262 | 260 | 2 |
| team_seasons (league_season_id, team_id) | 32 | 32 | 0 |
| team_seasons api_name within a season | 32 | 32 | 0 |
| team_seasons api_slug within a season | 32 | 32 | 0 |
| standings (league_season_id, team_id, view) | 96 | 96 | 0 |
| team_aliases (form, value) | 38 | 38 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 2 | 2 | 0 |
| teams.canonical_name | 19 | 19 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `262`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 262 | 0.0% |
| kickoff_time | 0 | 262 | 0.0% |
| home_team_id | 0 | 262 | 0.0% |
| away_team_id | 0 | 262 | 0.0% |
| home_score | 0 | 262 | 0.0% |
| away_score | 0 | 262 | 0.0% |
| home_ht | 0 | 262 | 0.0% |
| away_ht | 0 | 262 | 0.0% |
| first_goal_time | 21 | 241 | 8.0% |
| first_goal_time_extra | 21 | 241 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 7 |
| away_score | 0 | 5 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 4 |
| away_ht | 0 | 3 |
- first_goal_time NULL semantics consistent: `True`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 130 | 49.6% |
| Draw | 77 | 29.4% |
| Away | 55 | 21.0% |
| Total | 262 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 600 |
| Average goals per match | 2.29 |
| Home goals | 361 (avg 1.378) |
| Away goals | 239 (avg 0.912) |
| Home goal share | 60.2% |
| Goalless matches | 21 (8.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 50.0% | 29.2% | 20.8% | 544 | 2.267 | 325 | 219 | 20 (8.3%) |
| 2026-2027 | 22 | 45.5% | 31.8% | 22.7% | 56 | 2.545 | 36 | 20 | 1 (4.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `241` of `262` (92.0%)
| metric | value |
|---|---|
| First goals recorded | 241 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 35.5 |
| Median (p50) | 29.0 |
| p25 | 15.0 |
| p75 | 53.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 65 |
| 16-30 | 64 |
| 31-45 | 31 |
| 46-60 | 33 |
| 61-75 | 23 |
| 76-90 | 20 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 49 |
| 1-1 | 38 |
| 2-1 | 25 |
| 2-0 | 23 |
| 0-1 | 22 |
| 0-0 | 21 |
| 2-2 | 16 |
| 1-2 | 15 |
| 3-1 | 9 |
| 0-2 | 8 |
| 3-0 | 8 |
| 3-2 | 7 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-3 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 24 | 9.2% |
| Mon | 16 | 6.1% |
| Tue | 18 | 6.9% |
| Wed | 23 | 8.8% |
| Thu | 30 | 11.5% |
| Fri | 80 | 30.5% |
| Sat | 71 | 27.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 22 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.5% vs overall 8.0% (deviation 3.5 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 45.5% vs overall 49.6% |
| 8 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 22, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.5, "overall_goalless_pct": 8.0, "deviation_pp": 3.5}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 45.5, "overall_share": 49.6}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 262, "distinct": 260, "duplicates": 2}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
