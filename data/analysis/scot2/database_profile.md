# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:10:47+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `scot2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 487 |
| teams | 1768 |
| team_aliases | 3540 |
| team_seasons | 8123 |
| matches | 123054 |
| standings | 24369 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `72`
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
| germany-north | Regionalliga North | Germany | 7 | 1700 |
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
| india1 | ISL | India | 7 | 727 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2368 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2380 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2368 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 594 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1485 |
| national | National League | England | 6 | 2897 |
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
| saudi2 | Division 1 | Saudi Arabia | 7 | 2061 |
| scot-champ | Championship | Scotland | 7 | 1106 |
| scot-premier | Premiership | Scotland | 7 | 1290 |
| scot1 | League One | Scotland | 7 | 1061 |
| scot2 | League Two | Scotland | 7 | 1053 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `scot2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 90 | 10 | 2020-10-17 | 2021-04-20 |
| 2021-2022 | False | complete | 180 | 10 | 2021-07-31 | 2022-04-30 |
| 2022-2023 | False | complete | 180 | 10 | 2022-07-30 | 2023-05-06 |
| 2023-2024 | False | complete | 180 | 10 | 2023-08-05 | 2024-05-04 |
| 2024-2025 | False | complete | 180 | 10 | 2024-08-03 | 2025-05-03 |
| 2025-2026 | True | complete | 188 | 12 | 2025-08-02 | 2026-05-16 |
| 2026-2027 | True | in_progress | 55 | 10 | 2026-08-01 | 2026-10-17 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 123054 | 123054 | 0 |
| matches (league_season_id, game_index) | 123054 | 123054 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 123054 | 123034 | 20 |
| team_seasons (league_season_id, team_id) | 8123 | 8123 | 0 |
| team_seasons api_name within a season | 8123 | 8123 | 0 |
| team_seasons api_slug within a season | 8123 | 8123 | 0 |
| standings (league_season_id, team_id, view) | 24369 | 24369 | 0 |
| team_aliases (form, value) | 3540 | 3540 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1768 | 1768 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `123054`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 123054 | 0.0% |
| kickoff_time | 0 | 123054 | 0.0% |
| home_team_id | 0 | 123054 | 0.0% |
| away_team_id | 0 | 123054 | 0.0% |
| home_score | 0 | 123054 | 0.0% |
| away_score | 0 | 123054 | 0.0% |
| home_ht | 484 | 122570 | 0.4% |
| away_ht | 484 | 122570 | 0.4% |
| first_goal_time | 9809 | 113245 | 8.0% |
| first_goal_time_extra | 9809 | 113245 | 8.0% |
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
| Home | 449 | 42.6% |
| Draw | 266 | 25.3% |
| Away | 338 | 32.1% |
| Total | 1053 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2875 |
| Average goals per match | 2.73 |
| Home goals | 1550 (avg 1.472) |
| Away goals | 1325 (avg 1.258) |
| Home goal share | 53.9% |
| Goalless matches | 67 (6.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 90 | 38.9% | 20.0% | 41.1% | 245 | 2.722 | 122 | 123 | 6 (6.7%) |
| 2021-2022 | 180 | 37.8% | 25.0% | 37.2% | 468 | 2.6 | 238 | 230 | 12 (6.7%) |
| 2022-2023 | 180 | 43.3% | 23.9% | 32.8% | 489 | 2.717 | 268 | 221 | 8 (4.4%) |
| 2023-2024 | 180 | 40.6% | 32.2% | 27.2% | 467 | 2.594 | 252 | 215 | 17 (9.4%) |
| 2024-2025 | 180 | 50.0% | 20.6% | 29.4% | 469 | 2.606 | 276 | 193 | 13 (7.2%) |
| 2025-2026 | 188 | 39.9% | 29.3% | 30.9% | 552 | 2.936 | 289 | 263 | 9 (4.8%) |
| 2026-2027 | 55 | 54.5% | 18.2% | 27.3% | 185 | 3.364 | 105 | 80 | 2 (3.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `986` of `1053` (93.6%)
| metric | value |
|---|---|
| First goals recorded | 986 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 30.71 |
| Median (p50) | 25.0 |
| p25 | 12.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 325 |
| 16-30 | 250 |
| 31-45 | 157 |
| 46-60 | 117 |
| 61-75 | 86 |
| 76-90 | 39 |
| 91-120 | 12 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `216`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 10 | 1..10 | 10 |
| 2020-2021 | goals | 10 | 1..10 | 10 |
| 2020-2021 | luck | 10 | 1..10 | 10 |
| 2021-2022 | classic | 10 | 1..10 | 10 |
| 2021-2022 | goals | 10 | 1..10 | 10 |
| 2021-2022 | luck | 10 | 1..10 | 10 |
| 2022-2023 | classic | 10 | 1..10 | 10 |
| 2022-2023 | goals | 10 | 1..10 | 10 |
| 2022-2023 | luck | 10 | 1..10 | 10 |
| 2023-2024 | classic | 10 | 1..10 | 10 |
| 2023-2024 | goals | 10 | 1..10 | 10 |
| 2023-2024 | luck | 10 | 1..10 | 10 |
| 2024-2025 | classic | 10 | 1..10 | 10 |
| 2024-2025 | goals | 10 | 1..10 | 10 |
| 2024-2025 | luck | 10 | 1..10 | 10 |
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |
| 2026-2027 | classic | 10 | 1..10 | 10 |
| 2026-2027 | goals | 10 | 1..10 | 10 |
| 2026-2027 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 128 |
| 2-0 | 100 |
| 1-0 | 97 |
| 2-1 | 90 |
| 0-1 | 81 |
| 1-2 | 69 |
| 0-0 | 67 |
| 2-2 | 61 |
| 0-2 | 49 |
| 3-1 | 46 |
| 1-3 | 34 |
| 3-0 | 29 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-3 | 10 | 1 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 1 |
| 4-4 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 6 | 0.6% |
| Mon | 2 | 0.2% |
| Tue | 91 | 8.6% |
| Wed | 6 | 0.6% |
| Thu | 2 | 0.2% |
| Fri | 23 | 2.2% |
| Sat | 923 | 87.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 90 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 188 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 55 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 20.0% vs overall 25.3% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 41.1% vs overall 32.1% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 37.8% vs overall 42.6% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 37.2% vs overall 32.1% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 4.4% vs overall 6.4% (deviation 2.0 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 9.4% vs overall 6.4% (deviation 3.0 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 draw outcome share 32.2% vs overall 25.3% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 27.2% vs overall 32.1% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 50.0% vs overall 42.6% |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 20.6% vs overall 25.3% |
| 26 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 4.8% vs overall 6.4% (deviation 1.6 pp) |
| 27 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.364 vs overall 2.73 (deviation 0.634) |
| 28 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.6% vs overall 6.4% (deviation 2.8 pp) |
| 29 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 54.5% vs overall 42.6% |
| 30 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 18.2% vs overall 25.3% |
| 31 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 27.3% vs overall 32.1% |
| 32 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 33 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows) |
| 34 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=426, fgte=426 rows) |
| 35 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=10 positions=1..10 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=10 positions=1..10 teams=10 |
| 45 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=10 positions=1..10 teams=10 |
| 46 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=10 positions=1..10 teams=10 |
| 47 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=10 positions=1..10 teams=10 |
| 48 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=10 positions=1..10 teams=10 |
| 49 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=10 positions=1..10 teams=10 |
| 50 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 51 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 52 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 53 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=10 positions=1..10 teams=10 |
| 54 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=10 positions=1..10 teams=10 |
| 55 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 90, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 188, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 55, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 20.0, "overall_share": 25.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 41.1, "overall_share": 32.1}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 37.8, "overall_share": 42.6}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 37.2, "overall_share": 32.1}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 4.4, "overall_goalless_pct": 6.4, "deviation_pp": 2.0}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 9.4, "overall_goalless_pct": 6.4, "deviation_pp": 3.0}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "draw", "season_share": 32.2, "overall_share": 25.3}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 27.2, "overall_share": 32.1}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 50.0, "overall_share": 42.6}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 20.6, "overall_share": 25.3}`
- `26.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 4.8, "overall_goalless_pct": 6.4, "deviation_pp": 1.6}`
- `27.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.364, "overall_avg_goals": 2.73, "deviation": 0.634}`
- `28.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.6, "overall_goalless_pct": 6.4, "deviation_pp": 2.8}`
- `29.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 54.5, "overall_share": 42.6}`
- `30.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 18.2, "overall_share": 25.3}`
- `31.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 27.3, "overall_share": 32.1}`
- `32.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `33.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 123054, "distinct": 123034, "duplicates": 20}`
- `34.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 123054, "fgt_inconsistent": 426, "fgte_inconsistent": 426, "n_with_fgt": 113245}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `50.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `51.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `52.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `53.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `54.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `55.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
