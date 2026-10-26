# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:36:13+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `hungary2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 258 |
| teams | 972 |
| team_aliases | 1944 |
| team_seasons | 4433 |
| matches | 64940 |
| standings | 13299 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `38`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 913 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1021 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1795 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2620 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1457 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1637 |
| czech2 | ChNL | Czech Republic | 7 | 1477 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1086 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1417 |
| denmark1 | Superliga | Denmark | 7 | 921 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 61 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3455 |
| eng2 | League Two | England | 7 | 3466 |
| estonia | Meistriliiga | Estonia | 7 | 1166 |
| finland1 | Veikkausliiga | Finland | 7 | 944 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2127 |
| france2 | Ligue 2 | France | 7 | 2224 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1696 |
| germany1 | Bundesliga | Germany | 7 | 1688 |
| germany2 | 2. Bundesliga | Germany | 7 | 1918 |
| germany3 | 3. Liga | Germany | 7 | 2380 |
| greece1 | Super League | Greece | 7 | 1207 |
| greece2 | Super League 2 | Greece | 7 | 1832 |
| holland1 | Eredivisie | Netherlands | 7 | 1936 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1250 |
| hungary2 | NB II. | Hungary | 7 | 2012 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `hungary2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-08-01 | 2021-05-16 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-01 | 2022-05-22 |
| 2022-2023 | False | complete | 380 | 20 | 2022-07-30 | 2023-05-21 |
| 2023-2024 | False | complete | 306 | 18 | 2023-07-30 | 2024-05-26 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-28 | 2025-05-25 |
| 2025-2026 | True | complete | 240 | 16 | 2025-07-27 | 2026-05-17 |
| 2026-2027 | True | in_progress | 86 | 16 | 2026-07-25 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 64940 | 64940 | 0 |
| matches (league_season_id, game_index) | 64940 | 64940 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 64940 | 64930 | 10 |
| team_seasons (league_season_id, team_id) | 4433 | 4433 | 0 |
| team_seasons api_name within a season | 4433 | 4433 | 0 |
| team_seasons api_slug within a season | 4433 | 4433 | 0 |
| standings (league_season_id, team_id, view) | 13299 | 13299 | 0 |
| team_aliases (form, value) | 1944 | 1944 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 972 | 972 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `64940`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 64940 | 0.0% |
| kickoff_time | 0 | 64940 | 0.0% |
| home_team_id | 0 | 64940 | 0.0% |
| away_team_id | 0 | 64940 | 0.0% |
| home_score | 0 | 64940 | 0.0% |
| away_score | 0 | 64940 | 0.0% |
| home_ht | 399 | 64541 | 0.6% |
| away_ht | 399 | 64541 | 0.6% |
| first_goal_time | 5109 | 59831 | 7.9% |
| first_goal_time_extra | 5109 | 59831 | 7.9% |
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
| Home | 873 | 43.4% |
| Draw | 526 | 26.1% |
| Away | 613 | 30.5% |
| Total | 2012 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5201 |
| Average goals per match | 2.585 |
| Home goals | 2859 (avg 1.421) |
| Away goals | 2342 (avg 1.164) |
| Home goal share | 55.0% |
| Goalless matches | 146 (7.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 45.8% | 23.7% | 30.5% | 984 | 2.589 | 549 | 435 | 28 (7.4%) |
| 2021-2022 | 380 | 42.1% | 26.8% | 31.1% | 981 | 2.582 | 548 | 433 | 34 (8.9%) |
| 2022-2023 | 380 | 41.3% | 27.1% | 31.6% | 972 | 2.558 | 518 | 454 | 25 (6.6%) |
| 2023-2024 | 306 | 42.5% | 26.5% | 31.0% | 753 | 2.461 | 409 | 344 | 22 (7.2%) |
| 2024-2025 | 240 | 43.8% | 29.2% | 27.1% | 653 | 2.721 | 365 | 288 | 20 (8.3%) |
| 2025-2026 | 240 | 43.8% | 25.0% | 31.2% | 602 | 2.508 | 322 | 280 | 15 (6.2%) |
| 2026-2027 | 86 | 48.8% | 23.3% | 27.9% | 256 | 2.977 | 148 | 108 | 2 (2.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1862` of `2012` (92.5%)
| metric | value |
|---|---|
| First goals recorded | 1862 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 32.03 |
| Median (p50) | 27.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 587 |
| 16-30 | 439 |
| 31-45 | 337 |
| 46-60 | 245 |
| 61-75 | 133 |
| 76-90 | 103 |
| 91-120 | 18 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `378`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 20 | 1..20 | 20 |
| 2022-2023 | goals | 20 | 1..20 | 20 |
| 2022-2023 | luck | 20 | 1..20 | 20 |
| 2023-2024 | classic | 18 | 1..19 | 18 |
| 2023-2024 | goals | 18 | 1..26 | 18 |
| 2023-2024 | luck | 18 | 1..36 | 18 |
| 2024-2025 | classic | 16 | 1..17 | 16 |
| 2024-2025 | goals | 16 | 7..28 | 16 |
| 2024-2025 | luck | 16 | 1..46 | 16 |
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 262 |
| 1-0 | 225 |
| 0-1 | 198 |
| 2-1 | 174 |
| 2-0 | 151 |
| 0-0 | 146 |
| 1-2 | 136 |
| 2-2 | 102 |
| 0-2 | 87 |
| 3-1 | 80 |
| 3-0 | 68 |
| 3-2 | 48 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 2 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |
| 2-7 | 9 | 1 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1559 | 77.5% |
| Mon | 106 | 5.3% |
| Tue | 1 | 0.0% |
| Wed | 211 | 10.5% |
| Thu | 7 | 0.3% |
| Fri | 6 | 0.3% |
| Sat | 122 | 6.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 86 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 9 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 10 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 8.9% vs overall 7.3% (deviation 1.6 pp) |
| 11 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.977 vs overall 2.585 (deviation 0.392) |
| 12 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.3% vs overall 7.3% (deviation 5.0 pp) |
| 13 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 48.8% vs overall 43.4% |
| 14 | HIGH_SCORING_MATCHES | 12 match(es) with >= 8 total goals (extreme scorelines) |
| 15 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 16 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=344, fgte=344 rows) |
| 17 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..19 teams=18 |
| 18 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..26 teams=18 |
| 19 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..36 teams=18 |
| 20 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..17 teams=16 |
| 21 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=7..28 teams=16 |
| 22 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..46 teams=16 |
| 23 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 86, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `9.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `10.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 8.9, "overall_goalless_pct": 7.3, "deviation_pp": 1.6}`
- `11.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.977, "overall_avg_goals": 2.585, "deviation": 0.392}`
- `12.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.3, "overall_goalless_pct": 7.3, "deviation_pp": 5.0}`
- `13.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 48.8, "overall_share": 43.4}`
- `14.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 12, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `15.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 64940, "distinct": 64930, "duplicates": 10}`
- `16.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 64940, "fgt_inconsistent": 344, "fgte_inconsistent": 344, "n_with_fgt": 59831}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 26, "distinct_teams": 18}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 36, "distinct_teams": 18}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 17, "distinct_teams": 16}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 7, "max_pos": 28, "distinct_teams": 16}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 46, "distinct_teams": 16}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
