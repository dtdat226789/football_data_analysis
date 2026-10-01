# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:47:48+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `denmark1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 32 |
| teams | 350 |
| team_aliases | 700 |
| team_seasons | 580 |
| matches | 6111 |
| standings | 1740 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `16`
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
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 333 |
| denmark1 | Superliga | Denmark | 2 | 248 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `denmark1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 193 | 12 | 2025-07-18 | 2026-05-21 |
| 2026-2027 | True | in_progress | 55 | 12 | 2026-07-24 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 6111 | 6111 | 0 |
| matches (league_season_id, game_index) | 6111 | 6111 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 6111 | 6106 | 5 |
| team_seasons (league_season_id, team_id) | 580 | 580 | 0 |
| team_seasons api_name within a season | 580 | 580 | 0 |
| team_seasons api_slug within a season | 580 | 580 | 0 |
| standings (league_season_id, team_id, view) | 1740 | 1740 | 0 |
| team_aliases (form, value) | 700 | 700 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 350 | 350 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `6111`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 6111 | 0.0% |
| kickoff_time | 0 | 6111 | 0.0% |
| home_team_id | 0 | 6111 | 0.0% |
| away_team_id | 0 | 6111 | 0.0% |
| home_score | 0 | 6111 | 0.0% |
| away_score | 0 | 6111 | 0.0% |
| home_ht | 8 | 6103 | 0.1% |
| away_ht | 8 | 6103 | 0.1% |
| first_goal_time | 422 | 5689 | 6.9% |
| first_goal_time_extra | 422 | 5689 | 6.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 104 | 41.9% |
| Draw | 61 | 24.6% |
| Away | 83 | 33.5% |
| Total | 248 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 763 |
| Average goals per match | 3.077 |
| Home goals | 404 (avg 1.629) |
| Away goals | 359 (avg 1.448) |
| Home goal share | 52.9% |
| Goalless matches | 12 (4.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 193 | 41.5% | 23.3% | 35.2% | 599 | 3.104 | 320 | 279 | 11 (5.7%) |
| 2026-2027 | 55 | 43.6% | 29.1% | 27.3% | 164 | 2.982 | 84 | 80 | 1 (1.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `236` of `248` (95.2%)
| metric | value |
|---|---|
| First goals recorded | 236 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 28.05 |
| Median (p50) | 21.0 |
| p25 | 9.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 96 |
| 16-30 | 54 |
| 31-45 | 31 |
| 46-60 | 30 |
| 61-75 | 8 |
| 76-90 | 13 |
| 91-120 | 4 |

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
| 1-1 | 27 |
| 2-1 | 25 |
| 1-0 | 22 |
| 1-2 | 21 |
| 0-2 | 17 |
| 2-2 | 14 |
| 2-0 | 14 |
| 0-0 | 12 |
| 2-3 | 10 |
| 0-1 | 9 |
| 3-1 | 8 |
| 3-2 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 157 | 63.3% |
| Mon | 34 | 13.7% |
| Tue | 1 | 0.4% |
| Wed | 4 | 1.6% |
| Thu | 5 | 2.0% |
| Fri | 33 | 13.3% |
| Sat | 14 | 5.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 193 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 55 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.8% vs overall 4.8% (deviation 3.0 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 29.1% vs overall 24.6% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 27.3% vs overall 33.5% |
| 9 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 193, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 55, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.8, "overall_goalless_pct": 4.8, "deviation_pp": 3.0}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 29.1, "overall_share": 24.6}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 27.3, "overall_share": 33.5}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 2}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 6111, "distinct": 6106, "duplicates": 5}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 6111, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 5689}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
