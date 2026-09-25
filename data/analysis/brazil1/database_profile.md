# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:55:25+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `brazil1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 14 |
| teams | 142 |
| team_aliases | 284 |
| team_seasons | 236 |
| matches | 2385 |
| standings | 708 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `7`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `brazil1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 380 | 40 | 2025-03-29 | 2025-12-07 |
| 2026 | True | in_progress | 277 | 20 | 2026-01-28 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 2385 | 2385 | 0 |
| matches (league_season_id, game_index) | 2385 | 2385 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 2385 | 2383 | 2 |
| team_seasons (league_season_id, team_id) | 236 | 236 | 0 |
| team_seasons api_name within a season | 236 | 236 | 0 |
| team_seasons api_slug within a season | 236 | 236 | 0 |
| standings (league_season_id, team_id, view) | 708 | 708 | 0 |
| team_aliases (form, value) | 284 | 284 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 142 | 142 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `2385`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 2385 | 0.0% |
| kickoff_time | 0 | 2385 | 0.0% |
| home_team_id | 0 | 2385 | 0.0% |
| away_team_id | 0 | 2385 | 0.0% |
| home_score | 0 | 2385 | 0.0% |
| away_score | 0 | 2385 | 0.0% |
| home_ht | 3 | 2382 | 0.1% |
| away_ht | 3 | 2382 | 0.1% |
| first_goal_time | 164 | 2221 | 6.9% |
| first_goal_time_extra | 164 | 2221 | 6.9% |
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
| Home | 321 | 48.9% |
| Draw | 176 | 26.8% |
| Away | 160 | 24.4% |
| Total | 657 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1698 |
| Average goals per match | 2.584 |
| Home goals | 1001 (avg 1.524) |
| Away goals | 697 (avg 1.061) |
| Home goal share | 59.0% |
| Goalless matches | 43 (6.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 380 | 50.3% | 26.1% | 23.7% | 959 | 2.524 | 580 | 379 | 27 (7.1%) |
| 2026 | 277 | 46.9% | 27.8% | 25.3% | 739 | 2.668 | 421 | 318 | 16 (5.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `614` of `657` (93.5%)
| metric | value |
|---|---|
| First goals recorded | 614 |
| Min minute | 1 |
| Max minute | 106 |
| Mean minute | 31.82 |
| Median (p50) | 27.0 |
| p25 | 14.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 184 |
| 16-30 | 158 |
| 31-45 | 107 |
| 46-60 | 85 |
| 61-75 | 48 |
| 76-90 | 18 |
| 91-120 | 14 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `180`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 40 | 1..40 | 40 |
| 2025 | goals | 40 | 1..40 | 40 |
| 2025 | luck | 40 | 1..40 | 40 |
| 2026 | classic | 20 | 1..20 | 20 |
| 2026 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 87 |
| 1-0 | 79 |
| 2-1 | 72 |
| 2-0 | 61 |
| 0-1 | 44 |
| 0-0 | 43 |
| 1-2 | 43 |
| 2-2 | 35 |
| 3-0 | 29 |
| 3-1 | 26 |
| 0-2 | 25 |
| 3-2 | 18 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-0 | 8 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 275 | 41.9% |
| Mon | 50 | 7.6% |
| Tue | 27 | 4.1% |
| Wed | 43 | 6.5% |
| Thu | 99 | 15.1% |
| Fri | 35 | 5.3% |
| Sat | 128 | 19.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | TEAM_COUNT_UNEXPECTED | Season 2025 has 40 teams, expected 20 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026 has 277 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 4 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 5 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 6 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=40 positions=1..40 teams=40 |
| 8 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=40 positions=1..40 teams=40 |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=40 positions=1..40 teams=40 |
- `1.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 40, "expected": 20}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 277, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `4.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `5.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 2385, "distinct": 2383, "duplicates": 2}`
- `6.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 2385, "fgt_inconsistent": 2, "fgte_inconsistent": 2, "n_with_fgt": 2221}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 40, "min_pos": 1, "max_pos": 40, "distinct_teams": 40}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 40, "min_pos": 1, "max_pos": 40, "distinct_teams": 40}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 40, "min_pos": 1, "max_pos": 40, "distinct_teams": 40}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
