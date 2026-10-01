# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:45:36+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `brazil2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 16 |
| teams | 199 |
| team_aliases | 398 |
| team_seasons | 313 |
| matches | 3065 |
| standings | 939 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `8`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `brazil2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 380 | 57 | 2025-04-05 | 2025-11-23 |
| 2026 | True | in_progress | 299 | 20 | 2026-03-21 | 2026-09-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 3065 | 3065 | 0 |
| matches (league_season_id, game_index) | 3065 | 3065 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 3065 | 3063 | 2 |
| team_seasons (league_season_id, team_id) | 313 | 313 | 0 |
| team_seasons api_name within a season | 313 | 313 | 0 |
| team_seasons api_slug within a season | 313 | 313 | 0 |
| standings (league_season_id, team_id, view) | 939 | 939 | 0 |
| team_aliases (form, value) | 398 | 398 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 199 | 199 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `3065`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 3065 | 0.0% |
| kickoff_time | 0 | 3065 | 0.0% |
| home_team_id | 0 | 3065 | 0.0% |
| away_team_id | 0 | 3065 | 0.0% |
| home_score | 0 | 3065 | 0.0% |
| away_score | 0 | 3065 | 0.0% |
| home_ht | 3 | 3062 | 0.1% |
| away_ht | 3 | 3062 | 0.1% |
| first_goal_time | 224 | 2841 | 7.3% |
| first_goal_time_extra | 224 | 2841 | 7.3% |
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
| Home | 308 | 45.4% |
| Draw | 198 | 29.2% |
| Away | 173 | 25.5% |
| Total | 679 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1544 |
| Average goals per match | 2.274 |
| Home goals | 892 (avg 1.314) |
| Away goals | 652 (avg 0.96) |
| Home goal share | 57.8% |
| Goalless matches | 59 (8.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 380 | 45.8% | 30.5% | 23.7% | 843 | 2.218 | 491 | 352 | 33 (8.7%) |
| 2026 | 299 | 44.8% | 27.4% | 27.8% | 701 | 2.344 | 401 | 300 | 26 (8.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `620` of `679` (91.3%)
| metric | value |
|---|---|
| First goals recorded | 620 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 34.81 |
| Median (p50) | 29.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 170 |
| 16-30 | 151 |
| 31-45 | 101 |
| 46-60 | 85 |
| 61-75 | 61 |
| 76-90 | 34 |
| 91-120 | 18 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `231`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 57 | 1..57 | 57 |
| 2025 | goals | 57 | 1..57 | 57 |
| 2025 | luck | 57 | 1..57 | 57 |
| 2026 | classic | 20 | 1..20 | 20 |
| 2026 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 98 |
| 1-1 | 97 |
| 2-1 | 81 |
| 0-1 | 61 |
| 2-0 | 60 |
| 0-0 | 59 |
| 1-2 | 49 |
| 2-2 | 37 |
| 3-0 | 25 |
| 0-2 | 23 |
| 1-3 | 16 |
| 3-1 | 16 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 211 | 31.1% |
| Mon | 64 | 9.4% |
| Tue | 74 | 10.9% |
| Wed | 51 | 7.5% |
| Thu | 40 | 5.9% |
| Fri | 59 | 8.7% |
| Sat | 180 | 26.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | TEAM_COUNT_UNEXPECTED | Season 2025 has 57 teams, expected 20 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026 has 299 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 4 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 5 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 6 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=57 positions=1..57 teams=57 |
| 8 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=57 positions=1..57 teams=57 |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=57 positions=1..57 teams=57 |
- `1.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 57, "expected": 20}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 299, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `4.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `5.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 3065, "distinct": 3063, "duplicates": 2}`
- `6.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 3065, "fgt_inconsistent": 2, "fgte_inconsistent": 2, "n_with_fgt": 2841}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 57, "min_pos": 1, "max_pos": 57, "distinct_teams": 57}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 57, "min_pos": 1, "max_pos": 57, "distinct_teams": 57}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 57, "min_pos": 1, "max_pos": 57, "distinct_teams": 57}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
