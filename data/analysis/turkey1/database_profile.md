# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:14:52+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `turkey1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 598 |
| teams | 2203 |
| team_aliases | 4410 |
| team_seasons | 10063 |
| matches | 152397 |
| standings | 30189 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `88`
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
| thai1 | Thai League 1 | Thailand | 6 | 1248 |
| turkey1 | Super Lig | Turkey | 7 | 2251 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `turkey1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 420 | 21 | 2020-09-11 | 2021-05-15 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-13 | 2022-05-22 |
| 2022-2023 | False | complete | 342 | 19 | 2022-08-05 | 2023-06-07 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-11 | 2024-05-26 |
| 2024-2025 | False | complete | 342 | 19 | 2024-08-09 | 2025-06-01 |
| 2025-2026 | True | complete | 306 | 18 | 2025-08-08 | 2026-05-17 |
| 2026-2027 | True | in_progress | 81 | 18 | 2026-08-14 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 152397 | 152397 | 0 |
| matches (league_season_id, game_index) | 152397 | 152397 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 152397 | 152352 | 45 |
| team_seasons (league_season_id, team_id) | 10063 | 10063 | 0 |
| team_seasons api_name within a season | 10063 | 10063 | 0 |
| team_seasons api_slug within a season | 10063 | 10063 | 0 |
| standings (league_season_id, team_id, view) | 30189 | 30189 | 0 |
| team_aliases (form, value) | 4410 | 4410 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2203 | 2203 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `152397`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 152397 | 0.0% |
| kickoff_time | 0 | 152397 | 0.0% |
| home_team_id | 0 | 152397 | 0.0% |
| away_team_id | 0 | 152397 | 0.0% |
| home_score | 0 | 152397 | 0.0% |
| away_score | 0 | 152397 | 0.0% |
| home_ht | 533 | 151864 | 0.3% |
| away_ht | 533 | 151864 | 0.3% |
| first_goal_time | 12342 | 140055 | 8.1% |
| first_goal_time_extra | 12342 | 140055 | 8.1% |
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
| Home | 1013 | 45.0% |
| Draw | 565 | 25.1% |
| Away | 673 | 29.9% |
| Total | 2251 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6357 |
| Average goals per match | 2.824 |
| Home goals | 3553 (avg 1.578) |
| Away goals | 2804 (avg 1.246) |
| Home goal share | 55.9% |
| Goalless matches | 162 (7.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 420 | 41.2% | 28.1% | 30.7% | 1136 | 2.705 | 632 | 504 | 38 (9.0%) |
| 2021-2022 | 380 | 47.1% | 23.9% | 28.9% | 1067 | 2.808 | 606 | 461 | 23 (6.1%) |
| 2022-2023 | 342 | 45.0% | 21.3% | 33.6% | 1041 | 3.044 | 569 | 472 | 16 (4.7%) |
| 2023-2024 | 380 | 45.5% | 26.3% | 28.2% | 1062 | 2.795 | 599 | 463 | 28 (7.4%) |
| 2024-2025 | 342 | 48.5% | 23.4% | 28.1% | 1004 | 2.936 | 570 | 434 | 25 (7.3%) |
| 2025-2026 | 306 | 42.2% | 29.1% | 28.8% | 812 | 2.654 | 442 | 370 | 28 (9.2%) |
| 2026-2027 | 81 | 48.1% | 17.3% | 34.6% | 235 | 2.901 | 135 | 100 | 4 (4.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2058` of `2251` (91.4%)
| metric | value |
|---|---|
| First goals recorded | 2058 |
| Min minute | 1 |
| Max minute | 103 |
| Mean minute | 31.07 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 653 |
| 16-30 | 525 |
| 31-45 | 344 |
| 46-60 | 278 |
| 61-75 | 148 |
| 76-90 | 85 |
| 91-120 | 25 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `405`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 21 | 1..21 | 21 |
| 2020-2021 | goals | 21 | 1..21 | 21 |
| 2020-2021 | luck | 21 | 1..21 | 21 |
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 19 | 1..19 | 19 |
| 2022-2023 | goals | 19 | 1..19 | 19 |
| 2022-2023 | luck | 19 | 1..19 | 19 |
| 2023-2024 | classic | 20 | 1..20 | 20 |
| 2023-2024 | goals | 20 | 1..20 | 20 |
| 2023-2024 | luck | 20 | 1..20 | 20 |
| 2024-2025 | classic | 19 | 1..19 | 19 |
| 2024-2025 | goals | 19 | 1..19 | 19 |
| 2024-2025 | luck | 19 | 1..19 | 19 |
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 275 |
| 2-1 | 210 |
| 1-0 | 198 |
| 0-0 | 162 |
| 1-2 | 160 |
| 2-0 | 155 |
| 0-1 | 150 |
| 3-1 | 108 |
| 3-0 | 102 |
| 2-2 | 102 |
| 0-2 | 91 |
| 3-2 | 67 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-3 | 9 | 3 |
| 5-4 | 9 | 3 |
| 4-5 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 4 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 3 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 773 | 34.3% |
| Mon | 269 | 12.0% |
| Tue | 86 | 3.8% |
| Wed | 104 | 4.6% |
| Thu | 60 | 2.7% |
| Fri | 221 | 9.8% |
| Sat | 738 | 32.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 420 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 342 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 19 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 342 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 19 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 81 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 11 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 12 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 9.0% vs overall 7.2% (deviation 1.8 pp) |
| 13 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 4.7% vs overall 7.2% (deviation 2.5 pp) |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 9.2% vs overall 7.2% (deviation 2.0 pp) |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.9% vs overall 7.2% (deviation 2.3 pp) |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 17.3% vs overall 25.1% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 34.6% vs overall 29.9% |
| 18 | HIGH_SCORING_MATCHES | 22 match(es) with >= 8 total goals (extreme scorelines) |
| 19 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 20 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=474, fgte=474 rows) |
| 21 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=21 positions=1..21 teams=21 |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=21 positions=1..21 teams=21 |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=21 positions=1..21 teams=21 |
| 24 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=19 positions=1..19 teams=19 |
| 25 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=19 positions=1..19 teams=19 |
| 26 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=19 positions=1..19 teams=19 |
| 27 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=19 positions=1..19 teams=19 |
| 28 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=19 positions=1..19 teams=19 |
| 29 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=19 positions=1..19 teams=19 |
| 30 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 420, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 342, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 19, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 342, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 19, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 81, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `11.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `12.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 9.0, "overall_goalless_pct": 7.2, "deviation_pp": 1.8}`
- `13.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 4.7, "overall_goalless_pct": 7.2, "deviation_pp": 2.5}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 9.2, "overall_goalless_pct": 7.2, "deviation_pp": 2.0}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.9, "overall_goalless_pct": 7.2, "deviation_pp": 2.3}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 17.3, "overall_share": 25.1}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 34.6, "overall_share": 29.9}`
- `18.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 22, "threshold": 8, "examples": [{"scoreline": "6-3", "total_goals": 9, "count": 3}, {"scoreline": "5-4", "total_goals": 9, "count": 3}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 4}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `19.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 152397, "distinct": 152352, "duplicates": 45}`
- `20.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 152397, "fgt_inconsistent": 474, "fgte_inconsistent": 474, "n_with_fgt": 140055}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
