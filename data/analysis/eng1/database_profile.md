# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:57:38+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `eng1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 39 |
| teams | 427 |
| team_aliases | 854 |
| team_seasons | 709 |
| matches | 7132 |
| standings | 2058 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `19`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 669 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 330 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 326 |
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 34 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 640 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `eng1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 557 | 24 | 2025-08-01 | 2026-05-24 |
| 2026-2027 | True | in_progress | 83 | 24 | 2026-08-15 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 7132 | 7132 | 0 |
| matches (league_season_id, game_index) | 7132 | 7132 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 7132 | 7127 | 5 |
| team_seasons (league_season_id, team_id) | 709 | 709 | 0 |
| team_seasons api_name within a season | 709 | 709 | 0 |
| team_seasons api_slug within a season | 709 | 709 | 0 |
| standings (league_season_id, team_id, view) | 2058 | 2058 | 0 |
| team_aliases (form, value) | 854 | 854 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 427 | 427 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `7132`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 7132 | 0.0% |
| kickoff_time | 0 | 7132 | 0.0% |
| home_team_id | 0 | 7132 | 0.0% |
| away_team_id | 0 | 7132 | 0.0% |
| home_score | 0 | 7132 | 0.0% |
| away_score | 0 | 7132 | 0.0% |
| home_ht | 8 | 7124 | 0.1% |
| away_ht | 8 | 7124 | 0.1% |
| first_goal_time | 518 | 6614 | 7.3% |
| first_goal_time_extra | 518 | 6614 | 7.3% |
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
| Home | 286 | 44.7% |
| Draw | 166 | 25.9% |
| Away | 188 | 29.4% |
| Total | 640 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1705 |
| Average goals per match | 2.664 |
| Home goals | 952 (avg 1.488) |
| Away goals | 753 (avg 1.177) |
| Home goal share | 55.8% |
| Goalless matches | 41 (6.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 46.1% | 25.0% | 28.9% | 1462 | 2.625 | 823 | 639 | 33 (5.9%) |
| 2026-2027 | 83 | 34.9% | 32.5% | 32.5% | 243 | 2.928 | 129 | 114 | 8 (9.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `599` of `640` (93.6%)
| metric | value |
|---|---|
| First goals recorded | 599 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 31.74 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 196 |
| 16-30 | 139 |
| 31-45 | 100 |
| 46-60 | 79 |
| 61-75 | 47 |
| 76-90 | 28 |
| 91-120 | 10 |

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
| 1-1 | 79 |
| 1-0 | 77 |
| 2-1 | 61 |
| 0-1 | 53 |
| 1-2 | 45 |
| 0-0 | 41 |
| 2-2 | 38 |
| 2-0 | 34 |
| 3-0 | 29 |
| 0-2 | 28 |
| 3-1 | 24 |
| 1-3 | 20 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 15 | 2.3% |
| Mon | 25 | 3.9% |
| Tue | 102 | 15.9% |
| Wed | 14 | 2.2% |
| Thu | 26 | 4.1% |
| Fri | 24 | 3.8% |
| Sat | 434 | 67.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 557 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 83 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 9.6% vs overall 6.4% (deviation 3.2 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 34.9% vs overall 44.7% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 32.5% vs overall 25.9% |
| 9 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 557, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 83, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 9.6, "overall_goalless_pct": 6.4, "deviation_pp": 3.2}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 34.9, "overall_share": 44.7}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 32.5, "overall_share": 25.9}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 7132, "distinct": 7127, "duplicates": 5}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 7132, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 6614}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
