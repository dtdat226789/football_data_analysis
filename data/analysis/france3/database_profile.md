# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:51:52+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `france3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 181 |
| teams | 688 |
| team_aliases | 1376 |
| team_seasons | 3037 |
| matches | 44982 |
| standings | 9111 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `27`
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
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1171 |
| finland1 | Veikkausliiga | Finland | 7 | 946 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2134 |
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `france3`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 36 | 2020-08-21 | 2021-05-15 |
| 2021-2022 | False | complete | 306 | 18 | 2021-08-06 | 2022-05-13 |
| 2022-2023 | False | complete | 306 | 18 | 2022-08-12 | 2023-05-26 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-11 | 2024-05-18 |
| 2024-2025 | False | complete | 272 | 17 | 2024-08-16 | 2025-05-16 |
| 2025-2026 | True | complete | 303 | 50 | 2025-08-08 | 2026-05-15 |
| 2026-2027 | True | in_progress | 103 | 19 | 2026-08-07 | 2026-10-17 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 44982 | 44982 | 0 |
| matches (league_season_id, game_index) | 44982 | 44982 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 44982 | 44972 | 10 |
| team_seasons (league_season_id, team_id) | 3037 | 3037 | 0 |
| team_seasons api_name within a season | 3037 | 3037 | 0 |
| team_seasons api_slug within a season | 3037 | 3037 | 0 |
| standings (league_season_id, team_id, view) | 9111 | 9111 | 0 |
| team_aliases (form, value) | 1376 | 1376 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 688 | 688 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `44982`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 44982 | 0.0% |
| kickoff_time | 0 | 44982 | 0.0% |
| home_team_id | 0 | 44982 | 0.0% |
| away_team_id | 0 | 44982 | 0.0% |
| home_score | 0 | 44982 | 0.0% |
| away_score | 0 | 44982 | 0.0% |
| home_ht | 378 | 44604 | 0.8% |
| away_ht | 378 | 44604 | 0.8% |
| first_goal_time | 3866 | 41116 | 8.6% |
| first_goal_time_extra | 3866 | 41116 | 8.6% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 10 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 772 | 40.6% |
| Draw | 583 | 30.7% |
| Away | 547 | 28.8% |
| Total | 1902 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4638 |
| Average goals per match | 2.438 |
| Home goals | 2540 (avg 1.335) |
| Away goals | 2098 (avg 1.103) |
| Home goal share | 54.8% |
| Goalless matches | 191 (10.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 38.6% | 36.3% | 25.2% | 684 | 2.235 | 384 | 300 | 45 (14.7%) |
| 2021-2022 | 306 | 44.1% | 26.1% | 29.7% | 766 | 2.503 | 429 | 337 | 28 (9.2%) |
| 2022-2023 | 306 | 38.6% | 31.4% | 30.1% | 766 | 2.503 | 409 | 357 | 26 (8.5%) |
| 2023-2024 | 306 | 45.1% | 26.5% | 28.4% | 779 | 2.546 | 438 | 341 | 22 (7.2%) |
| 2024-2025 | 272 | 40.8% | 31.6% | 27.6% | 651 | 2.393 | 357 | 294 | 28 (10.3%) |
| 2025-2026 | 303 | 36.0% | 33.0% | 31.0% | 738 | 2.436 | 384 | 354 | 32 (10.6%) |
| 2026-2027 | 103 | 41.7% | 28.2% | 30.1% | 254 | 2.466 | 139 | 115 | 10 (9.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1705` of `1902` (89.6%)
| metric | value |
|---|---|
| First goals recorded | 1705 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 31.38 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 525 |
| 16-30 | 436 |
| 31-45 | 296 |
| 46-60 | 215 |
| 61-75 | 142 |
| 76-90 | 72 |
| 91-120 | 19 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `528`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 36 | 1..36 | 36 |
| 2020-2021 | goals | 36 | 1..36 | 36 |
| 2020-2021 | luck | 36 | 1..36 | 36 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 17 | 1..17 | 17 |
| 2024-2025 | goals | 17 | 1..17 | 17 |
| 2024-2025 | luck | 17 | 1..17 | 17 |
| 2025-2026 | classic | 50 | 1..50 | 50 |
| 2025-2026 | goals | 50 | 1..50 | 50 |
| 2025-2026 | luck | 50 | 1..50 | 50 |
| 2026-2027 | classic | 19 | 1..19 | 19 |
| 2026-2027 | goals | 19 | 1..19 | 19 |
| 2026-2027 | luck | 19 | 1..19 | 19 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 280 |
| 1-0 | 212 |
| 0-0 | 191 |
| 0-1 | 159 |
| 2-1 | 158 |
| 2-0 | 137 |
| 1-2 | 137 |
| 2-2 | 98 |
| 0-2 | 80 |
| 3-1 | 66 |
| 3-0 | 64 |
| 1-3 | 50 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 1 |
| 6-2 | 8 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 7 | 0.4% |
| Mon | 127 | 6.7% |
| Tue | 88 | 4.6% |
| Wed | 35 | 1.8% |
| Thu | 34 | 1.8% |
| Fri | 1415 | 74.4% |
| Sat | 196 | 10.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 36 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 272 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 17 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 303 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 50 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 103 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 19 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 14.7% vs overall 10.0% (deviation 4.7 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 36.3% vs overall 30.7% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 26.1% vs overall 30.7% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 7.2% vs overall 10.0% (deviation 2.8 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 45.1% vs overall 40.6% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 draw outcome share 26.5% vs overall 30.7% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 36.0% vs overall 40.6% |
| 23 | HIGH_SCORING_MATCHES | 7 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=323, fgte=323 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=36 positions=1..36 teams=36 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=36 positions=1..36 teams=36 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=36 positions=1..36 teams=36 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=17 positions=1..17 teams=17 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=17 positions=1..17 teams=17 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=17 positions=1..17 teams=17 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=50 positions=1..50 teams=50 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=50 positions=1..50 teams=50 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=50 positions=1..50 teams=50 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=19 positions=1..19 teams=19 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=19 positions=1..19 teams=19 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=19 positions=1..19 teams=19 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 36, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 272, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 17, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 303, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 50, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 103, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 19, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 14.7, "overall_goalless_pct": 10.0, "deviation_pp": 4.7}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 36.3, "overall_share": 30.7}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 26.1, "overall_share": 30.7}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 7.2, "overall_goalless_pct": 10.0, "deviation_pp": 2.8}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 45.1, "overall_share": 40.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "draw", "season_share": 26.5, "overall_share": 30.7}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 36.0, "overall_share": 40.6}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 7, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 44982, "distinct": 44972, "duplicates": 10}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 44982, "fgt_inconsistent": 323, "fgte_inconsistent": 323, "n_with_fgt": 41116}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
