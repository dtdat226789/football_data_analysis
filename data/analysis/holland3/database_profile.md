# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:02:54+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `holland3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 244 |
| teams | 931 |
| team_aliases | 1862 |
| team_seasons | 4223 |
| matches | 61759 |
| standings | 12669 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `36`
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
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3460 |
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1169 |
| finland1 | Veikkausliiga | Finland | 7 | 945 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2134 |
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1699 |
| germany1 | Bundesliga | Germany | 7 | 1690 |
| germany2 | 2. Bundesliga | Germany | 7 | 1921 |
| germany3 | 3. Liga | Germany | 7 | 2383 |
| greece1 | Super League | Greece | 7 | 1211 |
| greece2 | Super League 2 | Greece | 7 | 1836 |
| holland1 | Eredivisie | Netherlands | 7 | 1941 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `holland3`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 47 | 18 | 2020-09-05 | 2020-10-10 |
| 2021-2022 | False | complete | 306 | 18 | 2021-08-21 | 2022-06-04 |
| 2022-2023 | False | complete | 306 | 18 | 2022-08-20 | 2023-05-27 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-19 | 2024-05-25 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-17 | 2025-05-24 |
| 2025-2026 | True | complete | 322 | 25 | 2025-08-16 | 2026-06-13 |
| 2026-2027 | True | in_progress | 100 | 18 | 2026-08-15 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 61759 | 61759 | 0 |
| matches (league_season_id, game_index) | 61759 | 61759 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 61759 | 61749 | 10 |
| team_seasons (league_season_id, team_id) | 4223 | 4223 | 0 |
| team_seasons api_name within a season | 4223 | 4223 | 0 |
| team_seasons api_slug within a season | 4223 | 4223 | 0 |
| standings (league_season_id, team_id, view) | 12669 | 12669 | 0 |
| team_aliases (form, value) | 1862 | 1862 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 931 | 931 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `61759`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 61759 | 0.0% |
| kickoff_time | 0 | 61759 | 0.0% |
| home_team_id | 0 | 61759 | 0.0% |
| away_team_id | 0 | 61759 | 0.0% |
| home_score | 0 | 61759 | 0.0% |
| away_score | 0 | 61759 | 0.0% |
| home_ht | 394 | 61365 | 0.6% |
| away_ht | 394 | 61365 | 0.6% |
| first_goal_time | 4873 | 56886 | 7.9% |
| first_goal_time_extra | 4873 | 56886 | 7.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 760 | 44.9% |
| Draw | 349 | 20.6% |
| Away | 584 | 34.5% |
| Total | 1693 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5463 |
| Average goals per match | 3.227 |
| Home goals | 2946 (avg 1.74) |
| Away goals | 2517 (avg 1.487) |
| Home goal share | 53.9% |
| Goalless matches | 58 (3.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 47 | 42.6% | 31.9% | 25.5% | 143 | 3.043 | 78 | 65 | 2 (4.3%) |
| 2021-2022 | 306 | 50.3% | 19.6% | 30.1% | 940 | 3.072 | 525 | 415 | 9 (2.9%) |
| 2022-2023 | 306 | 45.1% | 21.2% | 33.7% | 978 | 3.196 | 532 | 446 | 14 (4.6%) |
| 2023-2024 | 306 | 38.9% | 23.2% | 37.9% | 966 | 3.157 | 497 | 469 | 12 (3.9%) |
| 2024-2025 | 306 | 43.8% | 18.0% | 38.2% | 1016 | 3.32 | 541 | 475 | 10 (3.3%) |
| 2025-2026 | 322 | 47.5% | 19.6% | 32.9% | 1069 | 3.32 | 584 | 485 | 10 (3.1%) |
| 2026-2027 | 100 | 42.0% | 20.0% | 38.0% | 351 | 3.51 | 189 | 162 | 1 (1.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1634` of `1693` (96.5%)
| metric | value |
|---|---|
| First goals recorded | 1634 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 28.65 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 42.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 585 |
| 16-30 | 413 |
| 31-45 | 272 |
| 46-60 | 193 |
| 61-75 | 108 |
| 76-90 | 45 |
| 91-120 | 18 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `399`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..18 | 18 |
| 2020-2021 | goals | 18 | 1..18 | 18 |
| 2020-2021 | luck | 18 | 1..18 | 18 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 1..18 | 18 |
| 2024-2025 | luck | 18 | 1..18 | 18 |
| 2025-2026 | classic | 25 | 1..25 | 25 |
| 2025-2026 | goals | 25 | 1..25 | 25 |
| 2025-2026 | luck | 25 | 1..25 | 25 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 160 |
| 2-1 | 145 |
| 2-0 | 117 |
| 1-2 | 111 |
| 1-0 | 106 |
| 2-2 | 97 |
| 0-1 | 95 |
| 0-2 | 93 |
| 3-1 | 88 |
| 3-0 | 72 |
| 1-3 | 72 |
| 0-0 | 58 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-7 | 11 | 1 |
| 5-5 | 10 | 1 |
| 2-8 | 10 | 1 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 2 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 38 | 2.2% |
| Mon | 8 | 0.5% |
| Tue | 50 | 3.0% |
| Wed | 23 | 1.4% |
| Thu | 4 | 0.2% |
| Fri | 2 | 0.1% |
| Sat | 1568 | 92.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 47 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 322 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 25 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 100 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 31.9% vs overall 20.6% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 25.5% vs overall 34.5% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 50.3% vs overall 44.9% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 30.1% vs overall 34.5% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 38.9% vs overall 44.9% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.0% vs overall 3.4% (deviation 2.4 pp) |
| 22 | HIGH_SCORING_MATCHES | 22 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=339, fgte=339 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..18 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=25 positions=1..25 teams=25 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=25 positions=1..25 teams=25 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=25 positions=1..25 teams=25 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 47, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 322, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 25, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 100, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 31.9, "overall_share": 20.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 25.5, "overall_share": 34.5}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 50.3, "overall_share": 44.9}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 30.1, "overall_share": 34.5}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 38.9, "overall_share": 44.9}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.0, "overall_goalless_pct": 3.4, "deviation_pp": 2.4}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 22, "threshold": 8, "examples": [{"scoreline": "4-7", "total_goals": 11, "count": 1}, {"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "2-8", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 1}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 61759, "distinct": 61749, "duplicates": 10}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 61759, "fgt_inconsistent": 339, "fgte_inconsistent": 339, "n_with_fgt": 56886}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
