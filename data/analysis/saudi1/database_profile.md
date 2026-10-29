# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:12:10+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `saudi1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 452 |
| teams | 1698 |
| team_aliases | 3398 |
| team_seasons | 7687 |
| matches | 116457 |
| standings | 23061 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `67`
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
| hungary1 | NB I. | Hungary | 7 | 1253 |
| hungary2 | NB II. | Hungary | 7 | 2013 |
| india1 | ISL | India | 7 | 726 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2363 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2377 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2894 |
| north | National League North | England | 7 | 3004 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1966 |
| portugal1 | Liga Portugal | Portugal | 2 | 389 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1912 |
| premier | Premier League | England | 7 | 2360 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1990 |
| romania1 | Superliga | Romania | 7 | 1654 |
| russia | Premier League | Russia | 7 | 1544 |
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `saudi1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-10-17 | 2021-05-30 |
| 2021-2022 | False | complete | 240 | 16 | 2021-08-11 | 2022-06-27 |
| 2022-2023 | False | complete | 240 | 16 | 2022-08-25 | 2023-05-31 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-11 | 2024-05-27 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-22 | 2025-05-26 |
| 2025-2026 | True | complete | 314 | 19 | 2025-08-28 | 2026-05-21 |
| 2026-2027 | True | in_progress | 91 | 18 | 2026-08-13 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 116457 | 116457 | 0 |
| matches (league_season_id, game_index) | 116457 | 116457 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 116457 | 116439 | 18 |
| team_seasons (league_season_id, team_id) | 7687 | 7687 | 0 |
| team_seasons api_name within a season | 7687 | 7687 | 0 |
| team_seasons api_slug within a season | 7687 | 7687 | 0 |
| standings (league_season_id, team_id, view) | 23061 | 23061 | 0 |
| team_aliases (form, value) | 3398 | 3398 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1698 | 1698 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `116457`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 116457 | 0.0% |
| kickoff_time | 0 | 116457 | 0.0% |
| home_team_id | 0 | 116457 | 0.0% |
| away_team_id | 0 | 116457 | 0.0% |
| home_score | 0 | 116457 | 0.0% |
| away_score | 0 | 116457 | 0.0% |
| home_ht | 476 | 115981 | 0.4% |
| away_ht | 476 | 115981 | 0.4% |
| first_goal_time | 9287 | 107170 | 8.0% |
| first_goal_time_extra | 9287 | 107170 | 8.0% |
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
| Home | 751 | 43.2% |
| Draw | 403 | 23.2% |
| Away | 583 | 33.6% |
| Total | 1737 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5045 |
| Average goals per match | 2.904 |
| Home goals | 2677 (avg 1.541) |
| Away goals | 2368 (avg 1.363) |
| Home goal share | 53.1% |
| Goalless matches | 100 (5.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 38.8% | 24.2% | 37.1% | 746 | 3.108 | 381 | 365 | 9 (3.8%) |
| 2021-2022 | 240 | 45.4% | 27.9% | 26.7% | 637 | 2.654 | 359 | 278 | 17 (7.1%) |
| 2022-2023 | 240 | 46.2% | 20.8% | 32.9% | 648 | 2.7 | 348 | 300 | 12 (5.0%) |
| 2023-2024 | 306 | 42.2% | 24.5% | 33.3% | 909 | 2.971 | 482 | 427 | 24 (7.8%) |
| 2024-2025 | 306 | 43.8% | 18.6% | 37.6% | 902 | 2.948 | 477 | 425 | 12 (3.9%) |
| 2025-2026 | 314 | 44.3% | 22.9% | 32.8% | 943 | 3.003 | 500 | 443 | 16 (5.1%) |
| 2026-2027 | 91 | 39.6% | 26.4% | 34.1% | 260 | 2.857 | 130 | 130 | 10 (11.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1636` of `1737` (94.2%)
| metric | value |
|---|---|
| First goals recorded | 1636 |
| Min minute | 1 |
| Max minute | 102 |
| Mean minute | 31.37 |
| Median (p50) | 25.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 510 |
| 16-30 | 418 |
| 31-45 | 267 |
| 46-60 | 241 |
| 61-75 | 103 |
| 76-90 | 63 |
| 91-120 | 34 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `363`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 6..26 | 16 |
| 2020-2021 | luck | 16 | 1..32 | 16 |
| 2021-2022 | classic | 16 | 1..17 | 16 |
| 2021-2022 | goals | 16 | 5..26 | 16 |
| 2021-2022 | luck | 16 | 1..32 | 16 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 1..18 | 18 |
| 2024-2025 | luck | 18 | 1..18 | 18 |
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..19 | 18 |
| 2026-2027 | goals | 18 | 1..19 | 18 |
| 2026-2027 | luck | 18 | 1..19 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 197 |
| 1-0 | 174 |
| 2-1 | 137 |
| 1-2 | 129 |
| 2-0 | 116 |
| 0-1 | 105 |
| 0-0 | 100 |
| 2-2 | 90 |
| 3-1 | 78 |
| 0-2 | 77 |
| 3-0 | 67 |
| 1-3 | 65 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 1 |
| 9-0 | 9 | 1 |
| 0-9 | 9 | 2 |
| 7-1 | 8 | 1 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 3 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 171 | 9.8% |
| Mon | 130 | 7.5% |
| Tue | 113 | 6.5% |
| Wed | 95 | 5.5% |
| Thu | 362 | 20.8% |
| Fri | 424 | 24.4% |
| Sat | 442 | 25.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 314 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 91 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 3.8% vs overall 5.8% (deviation 2.0 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 38.8% vs overall 43.2% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 27.9% vs overall 23.2% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 26.7% vs overall 33.6% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 7.8% vs overall 5.8% (deviation 2.0 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 3.9% vs overall 5.8% (deviation 1.9 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 18.6% vs overall 23.2% |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 11.0% vs overall 5.8% (deviation 5.2 pp) |
| 24 | HIGH_SCORING_MATCHES | 12 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=418, fgte=418 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=6..26 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..32 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..17 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=5..26 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..32 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..19 teams=18 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..19 teams=18 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..19 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 314, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 91, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 3.8, "overall_goalless_pct": 5.8, "deviation_pp": 2.0}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 38.8, "overall_share": 43.2}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 27.9, "overall_share": 23.2}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 26.7, "overall_share": 33.6}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 7.8, "overall_goalless_pct": 5.8, "deviation_pp": 2.0}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 3.9, "overall_goalless_pct": 5.8, "deviation_pp": 1.9}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 18.6, "overall_share": 23.2}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 11.0, "overall_goalless_pct": 5.8, "deviation_pp": 5.2}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 12, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "0-9", "total_goals": 9, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 3}, {"scoreline": "3-5", "total_goals": 8, "count": 3}, {"scoreline": "0-8", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 116457, "distinct": 116439, "duplicates": 18}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 116457, "fgt_inconsistent": 418, "fgte_inconsistent": 418, "n_with_fgt": 107170}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 6, "max_pos": 26, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 32, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 17, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 5, "max_pos": 26, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 32, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
