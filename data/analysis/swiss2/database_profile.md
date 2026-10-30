# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:14:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `swiss2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 585 |
| teams | 2142 |
| team_aliases | 4288 |
| team_seasons | 9832 |
| matches | 148898 |
| standings | 29496 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `86`
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
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1782 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1801 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1801 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1799 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1789 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1728 |
| slovenia1 | Prva liga | Slovenia | 7 | 1130 |
| south | National League South | England | 7 | 3012 |
| spain1 | LaLiga | Spain | 7 | 2380 |
| spain2 | LaLiga2 | Spain | 7 | 2940 |
| sweden1 | Allsvenskan | Sweden | 7 | 1645 |
| sweden2 | Superettan | Sweden | 7 | 1664 |
| swiss1 | Super League | Switzerland | 7 | 1232 |
| swiss2 | Challenge League | Switzerland | 7 | 1141 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `swiss2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 180 | 10 | 2020-09-18 | 2021-05-20 |
| 2021-2022 | False | complete | 180 | 10 | 2021-07-23 | 2022-05-21 |
| 2022-2023 | False | complete | 180 | 10 | 2022-07-15 | 2023-05-27 |
| 2023-2024 | False | complete | 180 | 10 | 2023-07-21 | 2024-05-20 |
| 2024-2025 | False | complete | 180 | 11 | 2024-07-19 | 2025-05-23 |
| 2025-2026 | True | complete | 186 | 11 | 2025-07-25 | 2026-05-15 |
| 2026-2027 | True | in_progress | 55 | 10 | 2026-07-24 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 148898 | 148898 | 0 |
| matches (league_season_id, game_index) | 148898 | 148898 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 148898 | 148853 | 45 |
| team_seasons (league_season_id, team_id) | 9832 | 9832 | 0 |
| team_seasons api_name within a season | 9832 | 9832 | 0 |
| team_seasons api_slug within a season | 9832 | 9832 | 0 |
| standings (league_season_id, team_id, view) | 29496 | 29496 | 0 |
| team_aliases (form, value) | 4288 | 4288 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2142 | 2142 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `148898`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 148898 | 0.0% |
| kickoff_time | 0 | 148898 | 0.0% |
| home_team_id | 0 | 148898 | 0.0% |
| away_team_id | 0 | 148898 | 0.0% |
| home_score | 0 | 148898 | 0.0% |
| away_score | 0 | 148898 | 0.0% |
| home_ht | 502 | 148396 | 0.3% |
| away_ht | 502 | 148396 | 0.3% |
| first_goal_time | 12063 | 136835 | 8.1% |
| first_goal_time_extra | 12063 | 136835 | 8.1% |
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
| Home | 501 | 43.9% |
| Draw | 284 | 24.9% |
| Away | 356 | 31.2% |
| Total | 1141 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3442 |
| Average goals per match | 3.017 |
| Home goals | 1881 (avg 1.649) |
| Away goals | 1561 (avg 1.368) |
| Home goal share | 54.6% |
| Goalless matches | 67 (5.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 180 | 46.7% | 25.0% | 28.3% | 503 | 2.794 | 290 | 213 | 10 (5.6%) |
| 2021-2022 | 180 | 49.4% | 20.6% | 30.0% | 585 | 3.25 | 324 | 261 | 11 (6.1%) |
| 2022-2023 | 180 | 41.1% | 27.2% | 31.7% | 564 | 3.133 | 304 | 260 | 9 (5.0%) |
| 2023-2024 | 180 | 41.7% | 28.3% | 30.0% | 517 | 2.872 | 282 | 235 | 11 (6.1%) |
| 2024-2025 | 180 | 40.0% | 26.1% | 33.9% | 540 | 3.0 | 281 | 259 | 11 (6.1%) |
| 2025-2026 | 186 | 44.6% | 21.5% | 33.9% | 566 | 3.043 | 300 | 266 | 12 (6.5%) |
| 2026-2027 | 55 | 43.6% | 27.3% | 29.1% | 167 | 3.036 | 100 | 67 | 3 (5.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1073` of `1141` (94.0%)
| metric | value |
|---|---|
| First goals recorded | 1073 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 27.87 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 425 |
| 16-30 | 245 |
| 31-45 | 166 |
| 46-60 | 131 |
| 61-75 | 64 |
| 76-90 | 31 |
| 91-120 | 11 |

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
| 2024-2025 | classic | 11 | 1..11 | 11 |
| 2024-2025 | goals | 11 | 1..11 | 11 |
| 2024-2025 | luck | 11 | 1..11 | 11 |
| 2025-2026 | classic | 11 | 1..11 | 11 |
| 2025-2026 | goals | 11 | 1..11 | 11 |
| 2025-2026 | luck | 11 | 1..11 | 11 |
| 2026-2027 | classic | 10 | 1..10 | 10 |
| 2026-2027 | goals | 10 | 1..10 | 10 |
| 2026-2027 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 131 |
| 2-1 | 115 |
| 1-0 | 85 |
| 1-2 | 73 |
| 2-0 | 71 |
| 2-2 | 71 |
| 0-0 | 67 |
| 0-2 | 64 |
| 3-1 | 54 |
| 0-1 | 51 |
| 3-0 | 45 |
| 1-3 | 44 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-3 | 9 | 1 |
| 4-5 | 9 | 3 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 172 | 15.1% |
| Mon | 42 | 3.7% |
| Tue | 88 | 7.7% |
| Wed | 13 | 1.1% |
| Thu | 9 | 0.8% |
| Fri | 572 | 50.1% |
| Sat | 245 | 21.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 180 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 11 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 186 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 11 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 55 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 49.4% vs overall 43.9% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 20.6% vs overall 24.9% |
| 18 | HIGH_SCORING_MATCHES | 11 match(es) with >= 8 total goals (extreme scorelines) |
| 19 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 20 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=443, fgte=443 rows) |
| 21 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=10 positions=1..10 teams=10 |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=10 positions=1..10 teams=10 |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=10 positions=1..10 teams=10 |
| 24 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=10 positions=1..10 teams=10 |
| 25 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=10 positions=1..10 teams=10 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=10 positions=1..10 teams=10 |
| 27 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=10 positions=1..10 teams=10 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=10 positions=1..10 teams=10 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=11 positions=1..11 teams=11 |
| 34 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=11 positions=1..11 teams=11 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=11 positions=1..11 teams=11 |
| 36 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=11 positions=1..11 teams=11 |
| 37 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=11 positions=1..11 teams=11 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=11 positions=1..11 teams=11 |
| 39 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 180, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 11, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 186, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 11, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 55, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 49.4, "overall_share": 43.9}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 20.6, "overall_share": 24.9}`
- `18.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 11, "threshold": 8, "examples": [{"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 3}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}]}`
- `19.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 148898, "distinct": 148853, "duplicates": 45}`
- `20.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 148898, "fgt_inconsistent": 443, "fgte_inconsistent": 443, "n_with_fgt": 136835}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
