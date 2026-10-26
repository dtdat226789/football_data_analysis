# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:44:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `russia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 445 |
| teams | 1672 |
| team_aliases | 3345 |
| team_seasons | 7566 |
| matches | 114524 |
| standings | 22698 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `66`
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
| india1 | ISL | India | 7 | 723 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2355 |
| italy19 | Primavera 1 | Italy | 7 | 1997 |
| italy2 | Serie B | Italy | 7 | 2368 |
| italy3a | Serie C - Group A | Italy | 7 | 2383 |
| italy3b | Serie C - Group B | Italy | 7 | 2364 |
| japan1 | J1 League | Japan | 8 | 2334 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1507 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1020 |
| lithuania | TOPLYGA | Lithuania | 7 | 1110 |
| morocco | Botola Pro | Morocco | 7 | 1481 |
| national | National League | England | 6 | 2885 |
| north | National League North | England | 7 | 2994 |
| norway | Eliteserien | Norway | 7 | 1626 |
| poland1 | Ekstraklasa | Poland | 7 | 1873 |
| poland2 | Division 1 | Poland | 7 | 1962 |
| portugal1 | Liga Portugal | Portugal | 2 | 384 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1908 |
| premier | Premier League | England | 7 | 2355 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2007 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1985 |
| romania1 | Superliga | Romania | 7 | 1651 |
| russia | Premier League | Russia | 7 | 1541 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `russia`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-08-08 | 2021-05-16 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-23 | 2022-05-21 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-15 | 2023-06-03 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-21 | 2024-05-25 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-20 | 2025-05-24 |
| 2025-2026 | True | complete | 244 | 18 | 2025-07-18 | 2026-05-23 |
| 2026-2027 | True | in_progress | 97 | 16 | 2026-07-24 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 114524 | 114524 | 0 |
| matches (league_season_id, game_index) | 114524 | 114524 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 114524 | 114506 | 18 |
| team_seasons (league_season_id, team_id) | 7566 | 7566 | 0 |
| team_seasons api_name within a season | 7566 | 7566 | 0 |
| team_seasons api_slug within a season | 7566 | 7566 | 0 |
| standings (league_season_id, team_id, view) | 22698 | 22698 | 0 |
| team_aliases (form, value) | 3345 | 3345 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1672 | 1672 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `114524`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 114524 | 0.0% |
| kickoff_time | 0 | 114524 | 0.0% |
| home_team_id | 0 | 114524 | 0.0% |
| away_team_id | 0 | 114524 | 0.0% |
| home_score | 0 | 114524 | 0.0% |
| away_score | 0 | 114524 | 0.0% |
| home_ht | 476 | 114048 | 0.4% |
| away_ht | 476 | 114048 | 0.4% |
| first_goal_time | 9174 | 105350 | 8.0% |
| first_goal_time_extra | 9174 | 105350 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 112 |
| home_ht | 0 | 7 |
| away_ht | 0 | 7 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 693 | 45.0% |
| Draw | 394 | 25.6% |
| Away | 454 | 29.5% |
| Total | 1541 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4177 |
| Average goals per match | 2.711 |
| Home goals | 2356 (avg 1.529) |
| Away goals | 1821 (avg 1.182) |
| Home goal share | 56.4% |
| Goalless matches | 112 (7.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 48.3% | 20.8% | 30.8% | 637 | 2.654 | 374 | 263 | 17 (7.1%) |
| 2021-2022 | 240 | 43.3% | 24.6% | 32.1% | 639 | 2.663 | 359 | 280 | 18 (7.5%) |
| 2022-2023 | 240 | 47.1% | 22.5% | 30.4% | 730 | 3.042 | 411 | 319 | 14 (5.8%) |
| 2023-2024 | 240 | 47.1% | 27.5% | 25.4% | 637 | 2.654 | 359 | 278 | 20 (8.3%) |
| 2024-2025 | 240 | 42.9% | 27.1% | 30.0% | 648 | 2.7 | 364 | 284 | 20 (8.3%) |
| 2025-2026 | 244 | 45.1% | 27.5% | 27.5% | 615 | 2.52 | 350 | 265 | 15 (6.1%) |
| 2026-2027 | 97 | 35.1% | 34.0% | 30.9% | 271 | 2.794 | 139 | 132 | 8 (8.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1426` of `1541` (92.5%)
| metric | value |
|---|---|
| First goals recorded | 1426 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 32.55 |
| Median (p50) | 27.0 |
| p25 | 13.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 433 |
| 16-30 | 345 |
| 31-45 | 249 |
| 46-60 | 193 |
| 61-75 | 108 |
| 76-90 | 77 |
| 91-120 | 21 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `342`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 16 | 1..16 | 16 |
| 2021-2022 | goals | 16 | 1..16 | 16 |
| 2021-2022 | luck | 16 | 1..16 | 16 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 186 |
| 1-0 | 157 |
| 2-1 | 133 |
| 2-0 | 121 |
| 0-0 | 112 |
| 0-1 | 109 |
| 1-2 | 103 |
| 2-2 | 79 |
| 3-1 | 75 |
| 0-2 | 74 |
| 3-0 | 56 |
| 1-3 | 42 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 622 | 40.4% |
| Mon | 94 | 6.1% |
| Tue | 9 | 0.6% |
| Wed | 32 | 2.1% |
| Thu | 22 | 1.4% |
| Fri | 100 | 6.5% |
| Sat | 662 | 43.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 244 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 97 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 20.8% vs overall 25.6% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 25.4% vs overall 29.5% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 35.1% vs overall 45.0% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 34.0% vs overall 25.6% |
| 20 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 21 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows) |
| 22 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=417, fgte=417 rows) |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 244, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 97, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 20.8, "overall_share": 25.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 25.4, "overall_share": 29.5}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 35.1, "overall_share": 45.0}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 34.0, "overall_share": 25.6}`
- `20.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `21.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 114524, "distinct": 114506, "duplicates": 18}`
- `22.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 114524, "fgt_inconsistent": 417, "fgte_inconsistent": 417, "n_with_fgt": 105350}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
