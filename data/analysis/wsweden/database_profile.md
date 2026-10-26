# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:53:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `wsweden`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 633 |
| teams | 2302 |
| team_aliases | 4608 |
| team_seasons | 10528 |
| matches | 157730 |
| standings | 31584 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `93`
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
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |
| saudi2 | Division 1 | Saudi Arabia | 7 | 2054 |
| scot-champ | Championship | Scotland | 7 | 1105 |
| scot-premier | Premiership | Scotland | 7 | 1282 |
| scot1 | League One | Scotland | 7 | 1060 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1779 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1797 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1795 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1794 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1784 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1725 |
| slovenia1 | Prva liga | Slovenia | 7 | 1126 |
| south | National League South | England | 7 | 3000 |
| spain1 | LaLiga | Spain | 7 | 2375 |
| spain2 | LaLiga2 | Spain | 7 | 2935 |
| sweden1 | Allsvenskan | Sweden | 7 | 1638 |
| sweden2 | Superettan | Sweden | 7 | 1660 |
| swiss1 | Super League | Switzerland | 7 | 1229 |
| swiss2 | Challenge League | Switzerland | 7 | 1140 |
| thai1 | Thai League 1 | Thailand | 6 | 1244 |
| turkey1 | Super Lig | Turkey | 7 | 2246 |
| turkey2 | 1. Lig | Turkey | 7 | 2175 |
| wbelgium1 | Super League Women | Belgium | 7 | 600 |
| wfrance1 | Premiere Ligue Women | France | 7 | 829 |
| wgermany1 | Bundesliga Women | Germany | 7 | 893 |
| wsweden | Allsvenskan Women | Sweden | 7 | 1151 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `wsweden`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 132 | 12 | 2020-06-27 | 2020-11-15 |
| 2021 | False | complete | 132 | 12 | 2021-04-17 | 2021-11-06 |
| 2022 | False | complete | 182 | 14 | 2022-03-26 | 2022-11-05 |
| 2023 | False | complete | 182 | 14 | 2023-03-24 | 2023-11-11 |
| 2024 | False | complete | 182 | 14 | 2024-04-13 | 2024-11-09 |
| 2025 | True | complete | 182 | 14 | 2025-03-22 | 2025-11-16 |
| 2026 | True | in_progress | 159 | 14 | 2026-03-28 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 157730 | 157730 | 0 |
| matches (league_season_id, game_index) | 157730 | 157730 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 157730 | 157685 | 45 |
| team_seasons (league_season_id, team_id) | 10528 | 10528 | 0 |
| team_seasons api_name within a season | 10528 | 10528 | 0 |
| team_seasons api_slug within a season | 10528 | 10528 | 0 |
| standings (league_season_id, team_id, view) | 31584 | 31584 | 0 |
| team_aliases (form, value) | 4608 | 4608 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2302 | 2302 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `157730`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 157730 | 0.0% |
| kickoff_time | 0 | 157730 | 0.0% |
| home_team_id | 0 | 157730 | 0.0% |
| away_team_id | 0 | 157730 | 0.0% |
| home_score | 0 | 157730 | 0.0% |
| away_score | 0 | 157730 | 0.0% |
| home_ht | 573 | 157157 | 0.4% |
| away_ht | 573 | 157157 | 0.4% |
| first_goal_time | 12690 | 145040 | 8.0% |
| first_goal_time_extra | 12690 | 145040 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 15 |
| first_goal_time | 1 | 112 |
| home_ht | 0 | 7 |
| away_ht | 0 | 8 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 536 | 46.6% |
| Draw | 198 | 17.2% |
| Away | 417 | 36.2% |
| Total | 1151 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3497 |
| Average goals per match | 3.038 |
| Home goals | 1911 (avg 1.66) |
| Away goals | 1586 (avg 1.378) |
| Home goal share | 54.6% |
| Goalless matches | 58 (5.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 132 | 45.5% | 16.7% | 37.9% | 383 | 2.902 | 206 | 177 | 5 (3.8%) |
| 2021 | 132 | 49.2% | 22.7% | 28.0% | 355 | 2.689 | 218 | 137 | 11 (8.3%) |
| 2022 | 182 | 47.8% | 13.2% | 39.0% | 559 | 3.071 | 309 | 250 | 7 (3.8%) |
| 2023 | 182 | 44.5% | 20.9% | 34.6% | 565 | 3.104 | 298 | 267 | 11 (6.0%) |
| 2024 | 182 | 44.5% | 17.0% | 38.5% | 558 | 3.066 | 300 | 258 | 16 (8.8%) |
| 2025 | 182 | 46.7% | 13.7% | 39.6% | 606 | 3.33 | 311 | 295 | 4 (2.2%) |
| 2026 | 159 | 48.4% | 17.6% | 34.0% | 471 | 2.962 | 269 | 202 | 4 (2.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1093` of `1151` (95.0%)
| metric | value |
|---|---|
| First goals recorded | 1093 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 28.36 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 413 |
| 16-30 | 272 |
| 31-45 | 163 |
| 46-60 | 127 |
| 61-75 | 73 |
| 76-90 | 35 |
| 91-120 | 10 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `282`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 12 | 1..12 | 12 |
| 2020 | goals | 12 | 1..12 | 12 |
| 2020 | luck | 12 | 1..12 | 12 |
| 2021 | classic | 12 | 1..12 | 12 |
| 2021 | goals | 12 | 1..12 | 12 |
| 2021 | luck | 12 | 1..12 | 12 |
| 2022 | classic | 14 | 1..14 | 14 |
| 2022 | goals | 14 | 1..14 | 14 |
| 2022 | luck | 14 | 1..14 | 14 |
| 2023 | classic | 14 | 1..14 | 14 |
| 2023 | goals | 14 | 1..14 | 14 |
| 2023 | luck | 14 | 1..14 | 14 |
| 2024 | classic | 14 | 1..14 | 14 |
| 2024 | goals | 14 | 1..14 | 14 |
| 2024 | luck | 14 | 1..14 | 14 |
| 2025 | classic | 14 | 1..14 | 14 |
| 2025 | goals | 14 | 1..14 | 14 |
| 2025 | luck | 14 | 1..14 | 14 |
| 2026 | classic | 14 | 1..14 | 14 |
| 2026 | goals | 14 | 1..14 | 14 |
| 2026 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 114 |
| 1-1 | 89 |
| 0-1 | 88 |
| 1-2 | 85 |
| 2-1 | 80 |
| 2-0 | 75 |
| 0-2 | 61 |
| 0-0 | 58 |
| 3-0 | 55 |
| 0-3 | 45 |
| 3-1 | 42 |
| 4-0 | 42 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 1-15 | 16 | 1 |
| 10-0 | 10 | 2 |
| 8-2 | 10 | 1 |
| 1-9 | 10 | 2 |
| 9-0 | 9 | 1 |
| 8-1 | 9 | 2 |
| 6-3 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 4 |
| 6-2 | 8 | 3 |
| 5-3 | 8 | 1 |
| 2-6 | 8 | 1 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 450 | 39.1% |
| Mon | 107 | 9.3% |
| Tue | 7 | 0.6% |
| Wed | 63 | 5.5% |
| Thu | 47 | 4.1% |
| Fri | 115 | 10.0% |
| Sat | 362 | 31.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 132 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 182 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 14 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 182 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 14 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 182 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 14 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 182 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 14 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 159 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 14 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 8.3% vs overall 5.0% (deviation 3.3 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021 draw outcome share 22.7% vs overall 17.2% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021 away outcome share 28.0% vs overall 36.2% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024 goalless share 8.8% vs overall 5.0% (deviation 3.8 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 2.2% vs overall 5.0% (deviation 2.8 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 2.5% vs overall 5.0% (deviation 2.5 pp) |
| 22 | HIGH_SCORING_MATCHES | 22 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=511, fgte=511 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=12 positions=1..12 teams=12 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=12 positions=1..12 teams=12 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=12 positions=1..12 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=14 positions=1..14 teams=14 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=14 positions=1..14 teams=14 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=14 positions=1..14 teams=14 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=14 positions=1..14 teams=14 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=14 positions=1..14 teams=14 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=14 positions=1..14 teams=14 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=14 positions=1..14 teams=14 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=14 positions=1..14 teams=14 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=14 positions=1..14 teams=14 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=14 positions=1..14 teams=14 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=14 positions=1..14 teams=14 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=14 positions=1..14 teams=14 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=14 positions=1..14 teams=14 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=14 positions=1..14 teams=14 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 132, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 182, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 14, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 182, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 14, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 182, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 14, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 182, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 14, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 159, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 14, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 8.3, "overall_goalless_pct": 5.0, "deviation_pp": 3.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "draw", "season_share": 22.7, "overall_share": 17.2}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "away", "season_share": 28.0, "overall_share": 36.2}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024", "season_goalless_pct": 8.8, "overall_goalless_pct": 5.0, "deviation_pp": 3.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 2.2, "overall_goalless_pct": 5.0, "deviation_pp": 2.8}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 2.5, "overall_goalless_pct": 5.0, "deviation_pp": 2.5}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 22, "threshold": 8, "examples": [{"scoreline": "1-15", "total_goals": 16, "count": 1}, {"scoreline": "10-0", "total_goals": 10, "count": 2}, {"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "1-9", "total_goals": 10, "count": 2}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 2}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 157730, "distinct": 157685, "duplicates": 45}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 157730, "fgt_inconsistent": 511, "fgte_inconsistent": 511, "n_with_fgt": 145040}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
