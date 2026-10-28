# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:46:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `eng2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 139 |
| teams | 519 |
| team_aliases | 1038 |
| team_seasons | 2358 |
| matches | 35641 |
| standings | 7074 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `21`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2620 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1457 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1640 |
| czech2 | ChNL | Czech Republic | 7 | 1478 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 925 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 61 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3455 |
| eng2 | League Two | England | 7 | 3466 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `eng2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 552 | 24 | 2020-09-12 | 2021-05-08 |
| 2021-2022 | False | complete | 552 | 24 | 2021-08-07 | 2022-05-07 |
| 2022-2023 | False | complete | 552 | 24 | 2022-07-30 | 2023-05-08 |
| 2023-2024 | False | complete | 552 | 24 | 2023-08-05 | 2024-04-27 |
| 2024-2025 | False | complete | 552 | 24 | 2024-08-09 | 2025-05-03 |
| 2025-2026 | True | complete | 557 | 24 | 2025-08-02 | 2026-05-25 |
| 2026-2027 | True | in_progress | 149 | 24 | 2026-08-15 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 35641 | 35641 | 0 |
| matches (league_season_id, game_index) | 35641 | 35641 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 35641 | 35636 | 5 |
| team_seasons (league_season_id, team_id) | 2358 | 2358 | 0 |
| team_seasons api_name within a season | 2358 | 2358 | 0 |
| team_seasons api_slug within a season | 2358 | 2358 | 0 |
| standings (league_season_id, team_id, view) | 7074 | 7074 | 0 |
| team_aliases (form, value) | 1038 | 1038 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 519 | 519 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `35641`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 35641 | 0.0% |
| kickoff_time | 0 | 35641 | 0.0% |
| home_team_id | 0 | 35641 | 0.0% |
| away_team_id | 0 | 35641 | 0.0% |
| home_score | 0 | 35641 | 0.0% |
| away_score | 0 | 35641 | 0.0% |
| home_ht | 342 | 35299 | 1.0% |
| away_ht | 342 | 35299 | 1.0% |
| first_goal_time | 3121 | 32520 | 8.8% |
| first_goal_time_extra | 3121 | 32520 | 8.8% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 1466 | 42.3% |
| Draw | 943 | 27.2% |
| Away | 1057 | 30.5% |
| Total | 3466 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 8797 |
| Average goals per match | 2.538 |
| Home goals | 4800 (avg 1.385) |
| Away goals | 3997 (avg 1.153) |
| Home goal share | 54.6% |
| Goalless matches | 286 (8.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 552 | 40.4% | 27.4% | 32.2% | 1303 | 2.361 | 696 | 607 | 57 (10.3%) |
| 2021-2022 | 552 | 41.8% | 27.5% | 30.6% | 1359 | 2.462 | 747 | 612 | 51 (9.2%) |
| 2022-2023 | 552 | 41.5% | 29.0% | 29.5% | 1294 | 2.344 | 708 | 586 | 54 (9.8%) |
| 2023-2024 | 552 | 44.9% | 23.7% | 31.3% | 1645 | 2.98 | 901 | 744 | 27 (4.9%) |
| 2024-2025 | 552 | 42.0% | 28.6% | 29.3% | 1377 | 2.495 | 757 | 620 | 48 (8.7%) |
| 2025-2026 | 557 | 41.8% | 25.0% | 33.2% | 1434 | 2.575 | 764 | 670 | 37 (6.6%) |
| 2026-2027 | 149 | 47.0% | 34.9% | 18.1% | 385 | 2.584 | 227 | 158 | 12 (8.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `3180` of `3466` (91.7%)
| metric | value |
|---|---|
| First goals recorded | 3180 |
| Min minute | 1 |
| Max minute | 103 |
| Mean minute | 31.51 |
| Median (p50) | 26.0 |
| p25 | 11.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 1029 |
| 16-30 | 752 |
| 31-45 | 518 |
| 46-60 | 440 |
| 61-75 | 244 |
| 76-90 | 151 |
| 91-120 | 46 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `504`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 24 | 1..24 | 24 |
| 2020-2021 | goals | 24 | 1..24 | 24 |
| 2020-2021 | luck | 24 | 1..24 | 24 |
| 2021-2022 | classic | 24 | 1..24 | 24 |
| 2021-2022 | goals | 24 | 1..24 | 24 |
| 2021-2022 | luck | 24 | 1..24 | 24 |
| 2022-2023 | classic | 24 | 1..24 | 24 |
| 2022-2023 | goals | 24 | 1..24 | 24 |
| 2022-2023 | luck | 24 | 1..24 | 24 |
| 2023-2024 | classic | 24 | 1..24 | 24 |
| 2023-2024 | goals | 24 | 1..24 | 24 |
| 2023-2024 | luck | 24 | 1..24 | 24 |
| 2024-2025 | classic | 24 | 1..24 | 24 |
| 2024-2025 | goals | 24 | 1..24 | 24 |
| 2024-2025 | luck | 24 | 1..24 | 24 |
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
| 1-1 | 443 |
| 1-0 | 394 |
| 2-1 | 316 |
| 0-1 | 296 |
| 0-0 | 286 |
| 2-0 | 254 |
| 1-2 | 246 |
| 0-2 | 183 |
| 2-2 | 170 |
| 3-0 | 127 |
| 3-1 | 121 |
| 1-3 | 107 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-2 | 11 | 1 |
| 5-5 | 10 | 3 |
| 6-3 | 9 | 2 |
| 5-4 | 9 | 3 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 6 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 3 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 31 | 0.9% |
| Mon | 133 | 3.8% |
| Tue | 728 | 21.0% |
| Wed | 35 | 1.0% |
| Thu | 49 | 1.4% |
| Fri | 155 | 4.5% |
| Sat | 2335 | 67.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 552 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 552 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 24 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 552 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 24 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 552 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 24 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 552 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 24 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 557 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 149 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 10.3% vs overall 8.3% (deviation 2.0 pp) |
| 17 | SEASON_AVG_GOALS_OUTLIER | Season 2023-2024 avg goals 2.98 vs overall 2.538 (deviation 0.442) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 4.9% vs overall 8.3% (deviation 3.4 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 6.6% vs overall 8.3% (deviation 1.7 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 47.0% vs overall 42.3% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 34.9% vs overall 27.2% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 18.1% vs overall 30.5% |
| 23 | HIGH_SCORING_MATCHES | 26 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=24 positions=1..24 teams=24 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=24 positions=1..24 teams=24 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=24 positions=1..24 teams=24 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=24 positions=1..24 teams=24 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=24 positions=1..24 teams=24 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=24 positions=1..24 teams=24 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 552, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 552, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 24, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 552, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 24, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 552, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 24, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 552, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 24, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 557, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 149, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 10.3, "overall_goalless_pct": 8.3, "deviation_pp": 2.0}`
- `17.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023-2024", "season_avg_goals": 2.98, "overall_avg_goals": 2.538, "deviation": 0.442}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 4.9, "overall_goalless_pct": 8.3, "deviation_pp": 3.4}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 6.6, "overall_goalless_pct": 8.3, "deviation_pp": 1.7}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 47.0, "overall_share": 42.3}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 34.9, "overall_share": 27.2}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 18.1, "overall_share": 30.5}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 26, "threshold": 8, "examples": [{"scoreline": "9-2", "total_goals": 11, "count": 1}, {"scoreline": "5-5", "total_goals": 10, "count": 3}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "5-4", "total_goals": 9, "count": 3}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 35641, "distinct": 35636, "duplicates": 5}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 35641, "fgt_inconsistent": 312, "fgte_inconsistent": 312, "n_with_fgt": 32520}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
