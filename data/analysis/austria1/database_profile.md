# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:54:44+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `austria1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 3 |
| league_seasons | 6 |
| teams | 45 |
| team_aliases | 90 |
| team_seasons | 81 |
| matches | 831 |
| standings | 243 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `3`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `austria1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 195 | 12 | 2025-08-01 | 2026-05-25 |
| 2026-2027 | True | in_progress | 42 | 12 | 2026-07-31 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 831 | 831 | 0 |
| matches (league_season_id, game_index) | 831 | 831 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 831 | 829 | 2 |
| team_seasons (league_season_id, team_id) | 81 | 81 | 0 |
| team_seasons api_name within a season | 81 | 81 | 0 |
| team_seasons api_slug within a season | 81 | 81 | 0 |
| standings (league_season_id, team_id, view) | 243 | 243 | 0 |
| team_aliases (form, value) | 90 | 90 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 3 | 3 | 0 |
| teams.canonical_name | 45 | 45 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `831`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 831 | 0.0% |
| kickoff_time | 0 | 831 | 0.0% |
| home_team_id | 0 | 831 | 0.0% |
| away_team_id | 0 | 831 | 0.0% |
| home_score | 0 | 831 | 0.0% |
| away_score | 0 | 831 | 0.0% |
| home_ht | 0 | 831 | 0.0% |
| away_ht | 0 | 831 | 0.0% |
| first_goal_time | 51 | 780 | 6.1% |
| first_goal_time_extra | 51 | 780 | 6.1% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 4 |
- first_goal_time NULL semantics consistent: `True`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 106 | 44.7% |
| Draw | 59 | 24.9% |
| Away | 72 | 30.4% |
| Total | 237 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 656 |
| Average goals per match | 2.768 |
| Home goals | 359 (avg 1.515) |
| Away goals | 297 (avg 1.253) |
| Home goal share | 54.7% |
| Goalless matches | 13 (5.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 195 | 43.1% | 25.6% | 31.3% | 527 | 2.703 | 280 | 247 | 12 (6.2%) |
| 2026-2027 | 42 | 52.4% | 21.4% | 26.2% | 129 | 3.071 | 79 | 50 | 1 (2.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `224` of `237` (94.5%)
| metric | value |
|---|---|
| First goals recorded | 224 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 30.96 |
| Median (p50) | 24.0 |
| p25 | 11.75 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 80 |
| 16-30 | 47 |
| 31-45 | 40 |
| 46-60 | 27 |
| 61-75 | 12 |
| 76-90 | 16 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `72`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 29 |
| 1-0 | 26 |
| 2-1 | 23 |
| 0-2 | 18 |
| 2-2 | 15 |
| 2-0 | 14 |
| 0-0 | 13 |
| 1-2 | 13 |
| 3-0 | 13 |
| 3-1 | 13 |
| 1-3 | 11 |
| 0-1 | 10 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-0 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 112 | 47.3% |
| Mon | 3 | 1.3% |
| Tue | 5 | 2.1% |
| Wed | 6 | 2.5% |
| Fri | 16 | 6.8% |
| Sat | 95 | 40.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 195 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 42 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.4% vs overall 5.5% (deviation 3.1 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 52.4% vs overall 44.7% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 26.2% vs overall 30.4% |
| 9 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 195, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 42, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.4, "overall_goalless_pct": 5.5, "deviation_pp": 3.1}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 52.4, "overall_share": 44.7}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 26.2, "overall_share": 30.4}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "8-0", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 831, "distinct": 829, "duplicates": 2}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
