# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:15:08+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `turkey2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 605 |
| teams | 2226 |
| team_aliases | 4456 |
| team_seasons | 10197 |
| matches | 154577 |
| standings | 30591 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `89`
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
| turkey2 | 1. Lig | Turkey | 7 | 2180 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `turkey2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 18 | 2020-09-11 | 2021-05-09 |
| 2021-2022 | False | complete | 342 | 19 | 2021-08-13 | 2022-05-21 |
| 2022-2023 | False | complete | 341 | 19 | 2022-08-12 | 2023-05-21 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-11 | 2024-05-11 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-09 | 2025-05-11 |
| 2025-2026 | True | complete | 385 | 20 | 2025-08-08 | 2026-05-24 |
| 2026-2027 | True | in_progress | 120 | 20 | 2026-08-07 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 154577 | 154577 | 0 |
| matches (league_season_id, game_index) | 154577 | 154577 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 154577 | 154532 | 45 |
| team_seasons (league_season_id, team_id) | 10197 | 10197 | 0 |
| team_seasons api_name within a season | 10197 | 10197 | 0 |
| team_seasons api_slug within a season | 10197 | 10197 | 0 |
| standings (league_season_id, team_id, view) | 30591 | 30591 | 0 |
| team_aliases (form, value) | 4456 | 4456 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2226 | 2226 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `154577`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 154577 | 0.0% |
| kickoff_time | 0 | 154577 | 0.0% |
| home_team_id | 0 | 154577 | 0.0% |
| away_team_id | 0 | 154577 | 0.0% |
| home_score | 0 | 154577 | 0.0% |
| away_score | 0 | 154577 | 0.0% |
| home_ht | 565 | 154012 | 0.4% |
| away_ht | 565 | 154012 | 0.4% |
| first_goal_time | 12535 | 142042 | 8.1% |
| first_goal_time_extra | 12535 | 142042 | 8.1% |
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
| Home | 963 | 44.2% |
| Draw | 520 | 23.9% |
| Away | 697 | 32.0% |
| Total | 2180 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5861 |
| Average goals per match | 2.689 |
| Home goals | 3211 (avg 1.473) |
| Away goals | 2650 (avg 1.216) |
| Home goal share | 54.8% |
| Goalless matches | 161 (7.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 42.8% | 21.2% | 35.9% | 854 | 2.791 | 449 | 405 | 22 (7.2%) |
| 2021-2022 | 342 | 48.8% | 22.5% | 28.7% | 901 | 2.635 | 497 | 404 | 24 (7.0%) |
| 2022-2023 | 341 | 43.1% | 23.2% | 33.7% | 915 | 2.683 | 485 | 430 | 24 (7.0%) |
| 2023-2024 | 306 | 41.8% | 25.2% | 33.0% | 725 | 2.369 | 390 | 335 | 28 (9.2%) |
| 2024-2025 | 380 | 45.8% | 23.9% | 30.3% | 1011 | 2.661 | 572 | 439 | 28 (7.4%) |
| 2025-2026 | 385 | 45.5% | 24.7% | 29.9% | 1125 | 2.922 | 644 | 481 | 28 (7.3%) |
| 2026-2027 | 120 | 34.2% | 30.0% | 35.8% | 330 | 2.75 | 174 | 156 | 7 (5.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1987` of `2180` (91.1%)
| metric | value |
|---|---|
| First goals recorded | 1987 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 31.95 |
| Median (p50) | 27.0 |
| p25 | 12.5 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 610 |
| 16-30 | 481 |
| 31-45 | 332 |
| 46-60 | 300 |
| 61-75 | 147 |
| 76-90 | 94 |
| 91-120 | 23 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `402`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..18 | 18 |
| 2020-2021 | goals | 18 | 1..18 | 18 |
| 2020-2021 | luck | 18 | 1..18 | 18 |
| 2021-2022 | classic | 19 | 1..19 | 19 |
| 2021-2022 | goals | 19 | 1..19 | 19 |
| 2021-2022 | luck | 19 | 1..19 | 19 |
| 2022-2023 | classic | 19 | 1..19 | 19 |
| 2022-2023 | goals | 19 | 1..19 | 19 |
| 2022-2023 | luck | 19 | 1..19 | 19 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 257 |
| 1-0 | 209 |
| 2-1 | 192 |
| 0-1 | 177 |
| 2-0 | 161 |
| 0-0 | 161 |
| 1-2 | 140 |
| 0-2 | 117 |
| 3-0 | 95 |
| 2-2 | 85 |
| 3-1 | 82 |
| 0-3 | 79 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 10-1 | 11 | 1 |
| 8-1 | 9 | 2 |
| 6-3 | 9 | 1 |
| 2-7 | 9 | 1 |
| 1-8 | 9 | 1 |
| 0-9 | 9 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 3 |
| 5-3 | 8 | 3 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 802 | 36.8% |
| Mon | 214 | 9.8% |
| Tue | 78 | 3.6% |
| Wed | 90 | 4.1% |
| Thu | 65 | 3.0% |
| Fri | 211 | 9.7% |
| Sat | 720 | 33.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 342 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 19 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 341 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 19 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 385 matches, expected 380 |
| 10 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 120 matches, expected 380 |
| 11 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 48.8% vs overall 44.2% |
| 13 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 9.2% vs overall 7.4% (deviation 1.8 pp) |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 5.8% vs overall 7.4% (deviation 1.6 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 34.2% vs overall 44.2% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 30.0% vs overall 23.9% |
| 17 | HIGH_SCORING_MATCHES | 15 match(es) with >= 8 total goals (extreme scorelines) |
| 18 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 19 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=506, fgte=506 rows) |
| 20 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..18 teams=18 |
| 21 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..18 teams=18 |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..18 teams=18 |
| 23 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=19 positions=1..19 teams=19 |
| 24 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=19 positions=1..19 teams=19 |
| 25 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=19 positions=1..19 teams=19 |
| 26 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=19 positions=1..19 teams=19 |
| 27 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=19 positions=1..19 teams=19 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=19 positions=1..19 teams=19 |
| 29 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 342, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 19, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 341, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 19, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 385, "expected": 380}`
- `10.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 120, "expected": 380}`
- `11.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 48.8, "overall_share": 44.2}`
- `13.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 9.2, "overall_goalless_pct": 7.4, "deviation_pp": 1.8}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 5.8, "overall_goalless_pct": 7.4, "deviation_pp": 1.6}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 34.2, "overall_share": 44.2}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 30.0, "overall_share": 23.9}`
- `17.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 15, "threshold": 8, "examples": [{"scoreline": "10-1", "total_goals": 11, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 2}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "1-8", "total_goals": 9, "count": 1}, {"scoreline": "0-9", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 3}]}`
- `18.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 154577, "distinct": 154532, "duplicates": 45}`
- `19.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 154577, "fgt_inconsistent": 506, "fgte_inconsistent": 506, "n_with_fgt": 142042}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
