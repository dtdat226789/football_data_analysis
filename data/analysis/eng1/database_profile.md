# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:49:35+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `eng1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 132 |
| teams | 502 |
| team_aliases | 1004 |
| team_seasons | 2190 |
| matches | 32202 |
| standings | 6570 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `20`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1697 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2623 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1461 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1640 |
| czech2 | ChNL | Czech Republic | 7 | 1478 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1089 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1423 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1771 |
| eng1 | League One | England | 7 | 3460 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `eng1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 552 | 24 | 2020-09-12 | 2021-05-09 |
| 2021-2022 | False | complete | 552 | 24 | 2021-08-07 | 2022-04-30 |
| 2022-2023 | False | complete | 552 | 24 | 2022-07-30 | 2023-05-07 |
| 2023-2024 | False | complete | 552 | 24 | 2023-08-05 | 2024-04-27 |
| 2024-2025 | False | complete | 552 | 24 | 2024-08-09 | 2025-05-03 |
| 2025-2026 | True | complete | 557 | 24 | 2025-08-01 | 2026-05-24 |
| 2026-2027 | True | in_progress | 143 | 24 | 2026-08-15 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 32202 | 32202 | 0 |
| matches (league_season_id, game_index) | 32202 | 32202 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 32202 | 32197 | 5 |
| team_seasons (league_season_id, team_id) | 2190 | 2190 | 0 |
| team_seasons api_name within a season | 2190 | 2190 | 0 |
| team_seasons api_slug within a season | 2190 | 2190 | 0 |
| standings (league_season_id, team_id, view) | 6570 | 6570 | 0 |
| team_aliases (form, value) | 1004 | 1004 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 502 | 502 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `32202`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 32202 | 0.0% |
| kickoff_time | 0 | 32202 | 0.0% |
| home_team_id | 0 | 32202 | 0.0% |
| away_team_id | 0 | 32202 | 0.0% |
| home_score | 0 | 32202 | 0.0% |
| away_score | 0 | 32202 | 0.0% |
| home_ht | 342 | 31860 | 1.1% |
| away_ht | 342 | 31860 | 1.1% |
| first_goal_time | 2837 | 29365 | 8.8% |
| first_goal_time_extra | 2837 | 29365 | 8.8% |
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
| Home | 1500 | 43.4% |
| Draw | 865 | 25.0% |
| Away | 1095 | 31.6% |
| Total | 3460 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 9068 |
| Average goals per match | 2.621 |
| Home goals | 4947 (avg 1.43) |
| Away goals | 4121 (avg 1.191) |
| Home goal share | 54.6% |
| Goalless matches | 244 (7.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 552 | 40.4% | 23.9% | 35.7% | 1447 | 2.621 | 744 | 703 | 38 (6.9%) |
| 2021-2022 | 552 | 44.7% | 26.4% | 28.8% | 1489 | 2.697 | 828 | 661 | 37 (6.7%) |
| 2022-2023 | 552 | 43.7% | 25.4% | 31.0% | 1414 | 2.562 | 781 | 633 | 41 (7.4%) |
| 2023-2024 | 552 | 42.4% | 24.5% | 33.2% | 1427 | 2.585 | 778 | 649 | 38 (6.9%) |
| 2024-2025 | 552 | 43.1% | 23.9% | 33.0% | 1427 | 2.585 | 775 | 652 | 46 (8.3%) |
| 2025-2026 | 557 | 46.1% | 25.0% | 28.9% | 1462 | 2.625 | 823 | 639 | 33 (5.9%) |
| 2026-2027 | 143 | 42.0% | 28.7% | 29.4% | 402 | 2.811 | 218 | 184 | 11 (7.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `3216` of `3460` (92.9%)
| metric | value |
|---|---|
| First goals recorded | 3216 |
| Min minute | 1 |
| Max minute | 110 |
| Mean minute | 30.94 |
| Median (p50) | 25.0 |
| p25 | 11.75 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 1064 |
| 16-30 | 789 |
| 31-45 | 519 |
| 46-60 | 416 |
| 61-75 | 244 |
| 76-90 | 146 |
| 91-120 | 38 |

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
| 1-1 | 407 |
| 1-0 | 374 |
| 2-1 | 330 |
| 0-1 | 292 |
| 1-2 | 253 |
| 2-0 | 251 |
| 0-0 | 244 |
| 0-2 | 191 |
| 2-2 | 169 |
| 3-0 | 129 |
| 3-1 | 122 |
| 1-3 | 89 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 1 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 1 |
| 6-2 | 8 | 1 |
| 4-4 | 8 | 8 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 80 | 2.3% |
| Mon | 121 | 3.5% |
| Tue | 808 | 23.4% |
| Wed | 55 | 1.6% |
| Thu | 56 | 1.6% |
| Fri | 121 | 3.5% |
| Sat | 2219 | 64.1% |

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
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 143 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 35.7% vs overall 31.6% |
| 17 | HIGH_SCORING_MATCHES | 16 match(es) with >= 8 total goals (extreme scorelines) |
| 18 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 19 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows) |
| 20 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=24 positions=1..24 teams=24 |
| 21 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=24 positions=1..24 teams=24 |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=24 positions=1..24 teams=24 |
| 23 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=24 positions=1..24 teams=24 |
| 24 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=24 positions=1..24 teams=24 |
| 25 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=24 positions=1..24 teams=24 |
| 26 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 27 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 29 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 30 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 32 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 33 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 34 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 35 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 39 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 40 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
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
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 143, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 35.7, "overall_share": 31.6}`
- `17.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 16, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 8}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `18.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 32202, "distinct": 32197, "duplicates": 5}`
- `19.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 32202, "fgt_inconsistent": 312, "fgte_inconsistent": 312, "n_with_fgt": 29365}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
