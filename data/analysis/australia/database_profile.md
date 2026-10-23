# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:43:49+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `australia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 3 |
| league_seasons | 4 |
| teams | 32 |
| team_aliases | 64 |
| team_seasons | 57 |
| matches | 595 |
| standings | 171 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `2`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |
| australia | A-League | Australia | 2 | 332 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `australia`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2024-2025 | True | complete | 169 | 13 | 2024-10-18 | 2025-05-04 |
| 2025-2026 | True | complete | 163 | 12 | 2025-10-17 | 2026-05-23 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 595 | 595 | 0 |
| matches (league_season_id, game_index) | 595 | 595 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 595 | 593 | 2 |
| team_seasons (league_season_id, team_id) | 57 | 57 | 0 |
| team_seasons api_name within a season | 57 | 57 | 0 |
| team_seasons api_slug within a season | 57 | 57 | 0 |
| standings (league_season_id, team_id, view) | 171 | 171 | 0 |
| team_aliases (form, value) | 64 | 64 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 3 | 3 | 0 |
| teams.canonical_name | 32 | 32 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `595`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 595 | 0.0% |
| kickoff_time | 0 | 595 | 0.0% |
| home_team_id | 0 | 595 | 0.0% |
| away_team_id | 0 | 595 | 0.0% |
| home_score | 0 | 595 | 0.0% |
| away_score | 0 | 595 | 0.0% |
| home_ht | 0 | 595 | 0.0% |
| away_ht | 0 | 595 | 0.0% |
| first_goal_time | 39 | 556 | 6.6% |
| first_goal_time_extra | 39 | 556 | 6.6% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 7 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 4 |
- first_goal_time NULL semantics consistent: `True`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 121 | 36.4% |
| Draw | 87 | 26.2% |
| Away | 124 | 37.3% |
| Total | 332 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1018 |
| Average goals per match | 3.066 |
| Home goals | 524 (avg 1.578) |
| Away goals | 494 (avg 1.488) |
| Home goal share | 51.5% |
| Goalless matches | 17 (5.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 169 | 34.9% | 26.0% | 39.1% | 556 | 3.29 | 280 | 276 | 8 (4.7%) |
| 2025-2026 | 163 | 38.0% | 26.4% | 35.6% | 462 | 2.834 | 244 | 218 | 9 (5.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `315` of `332` (94.9%)
| metric | value |
|---|---|
| First goals recorded | 315 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 28.58 |
| Median (p50) | 20.0 |
| p25 | 10.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 128 |
| 16-30 | 63 |
| 31-45 | 47 |
| 46-60 | 42 |
| 61-75 | 20 |
| 76-90 | 9 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `75`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2024-2025 | classic | 13 | 1..13 | 13 |
| 2024-2025 | goals | 13 | 1..13 | 13 |
| 2024-2025 | luck | 13 | 1..13 | 13 |
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 35 |
| 2-2 | 30 |
| 1-2 | 29 |
| 0-1 | 26 |
| 1-0 | 25 |
| 2-1 | 23 |
| 0-0 | 17 |
| 0-2 | 17 |
| 1-3 | 15 |
| 2-0 | 15 |
| 4-1 | 13 |
| 2-3 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 2 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 71 | 21.4% |
| Mon | 8 | 2.4% |
| Tue | 10 | 3.0% |
| Wed | 9 | 2.7% |
| Thu | 6 | 1.8% |
| Fri | 70 | 21.1% |
| Sat | 158 | 47.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 169 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 13 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 163 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 5 | HIGH_SCORING_MATCHES | 7 match(es) with >= 8 total goals (extreme scorelines) |
| 6 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=13 positions=1..13 teams=13 |
| 8 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=13 positions=1..13 teams=13 |
| 9 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=13 positions=1..13 teams=13 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 169, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 13, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 163, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `5.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 7, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `6.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 595, "distinct": 593, "duplicates": 2}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
