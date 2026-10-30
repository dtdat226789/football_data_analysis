# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:12:05+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `segunda3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 508 |
| teams | 1867 |
| team_aliases | 3738 |
| team_seasons | 8509 |
| matches | 128438 |
| standings | 25527 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `75`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `segunda3`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 200 | 21 | 2020-10-17 | 2021-03-31 |
| 2021-2022 | False | complete | 306 | 18 | 2021-09-05 | 2022-05-15 |
| 2022-2023 | False | complete | 306 | 18 | 2022-09-03 | 2023-05-14 |
| 2023-2024 | False | complete | 306 | 18 | 2023-09-02 | 2024-05-05 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-31 | 2025-05-04 |
| 2025-2026 | True | complete | 306 | 18 | 2025-09-06 | 2026-05-03 |
| 2026-2027 | True | in_progress | 71 | 18 | 2026-09-05 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 128438 | 128438 | 0 |
| matches (league_season_id, game_index) | 128438 | 128438 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 128438 | 128414 | 24 |
| team_seasons (league_season_id, team_id) | 8509 | 8509 | 0 |
| team_seasons api_name within a season | 8509 | 8509 | 0 |
| team_seasons api_slug within a season | 8509 | 8509 | 0 |
| standings (league_season_id, team_id, view) | 25527 | 25527 | 0 |
| team_aliases (form, value) | 3738 | 3738 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1867 | 1867 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `128438`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 128438 | 0.0% |
| kickoff_time | 0 | 128438 | 0.0% |
| home_team_id | 0 | 128438 | 0.0% |
| away_team_id | 0 | 128438 | 0.0% |
| home_score | 0 | 128438 | 0.0% |
| away_score | 0 | 128438 | 0.0% |
| home_ht | 485 | 127953 | 0.4% |
| away_ht | 485 | 127953 | 0.4% |
| first_goal_time | 10382 | 118056 | 8.1% |
| first_goal_time_extra | 10382 | 118056 | 8.1% |
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
| Home | 780 | 43.3% |
| Draw | 545 | 30.3% |
| Away | 476 | 26.4% |
| Total | 1801 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4159 |
| Average goals per match | 2.309 |
| Home goals | 2378 (avg 1.32) |
| Away goals | 1781 (avg 0.989) |
| Home goal share | 57.2% |
| Goalless matches | 190 (10.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 200 | 44.5% | 31.5% | 24.0% | 415 | 2.075 | 249 | 166 | 25 (12.5%) |
| 2021-2022 | 306 | 45.4% | 30.7% | 23.9% | 697 | 2.278 | 414 | 283 | 30 (9.8%) |
| 2022-2023 | 306 | 41.8% | 32.7% | 25.5% | 652 | 2.131 | 363 | 289 | 42 (13.7%) |
| 2023-2024 | 306 | 44.1% | 28.1% | 27.8% | 742 | 2.425 | 424 | 318 | 31 (10.1%) |
| 2024-2025 | 306 | 37.3% | 29.1% | 33.7% | 724 | 2.366 | 390 | 334 | 27 (8.8%) |
| 2025-2026 | 306 | 45.8% | 31.7% | 22.5% | 742 | 2.425 | 434 | 308 | 33 (10.8%) |
| 2026-2027 | 71 | 49.3% | 22.5% | 28.2% | 187 | 2.634 | 104 | 83 | 2 (2.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1611` of `1801` (89.5%)
| metric | value |
|---|---|
| First goals recorded | 1611 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.5 |
| Median (p50) | 30.0 |
| p25 | 13.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 464 |
| 16-30 | 362 |
| 31-45 | 283 |
| 46-60 | 214 |
| 61-75 | 151 |
| 76-90 | 117 |
| 91-120 | 20 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `387`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 21 | 1..21 | 21 |
| 2020-2021 | goals | 21 | 1..21 | 21 |
| 2020-2021 | luck | 21 | 1..21 | 21 |
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
| 1-0 | 257 |
| 1-1 | 253 |
| 0-0 | 190 |
| 0-1 | 172 |
| 2-1 | 158 |
| 1-2 | 117 |
| 2-0 | 113 |
| 2-2 | 88 |
| 0-2 | 72 |
| 3-0 | 70 |
| 3-1 | 69 |
| 1-3 | 33 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-3 | 10 | 1 |
| 4-6 | 10 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1517 | 84.2% |
| Mon | 2 | 0.1% |
| Tue | 4 | 0.2% |
| Wed | 32 | 1.8% |
| Thu | 3 | 0.2% |
| Fri | 1 | 0.1% |
| Sat | 242 | 13.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 200 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 306 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 71 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 12.5% vs overall 10.5% (deviation 2.0 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 13.7% vs overall 10.5% (deviation 3.2 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 8.8% vs overall 10.5% (deviation 1.7 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 37.3% vs overall 43.3% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 33.7% vs overall 26.4% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.8% vs overall 10.5% (deviation 7.7 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 49.3% vs overall 43.3% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 22.5% vs overall 30.3% |
| 24 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=427, fgte=427 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=21 positions=1..21 teams=21 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=21 positions=1..21 teams=21 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=21 positions=1..21 teams=21 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 200, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 306, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 71, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 12.5, "overall_goalless_pct": 10.5, "deviation_pp": 2.0}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 13.7, "overall_goalless_pct": 10.5, "deviation_pp": 3.2}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 8.8, "overall_goalless_pct": 10.5, "deviation_pp": 1.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 37.3, "overall_share": 43.3}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 33.7, "overall_share": 26.4}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.8, "overall_goalless_pct": 10.5, "deviation_pp": 7.7}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 49.3, "overall_share": 43.3}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 22.5, "overall_share": 30.3}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 128438, "distinct": 128414, "duplicates": 24}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 128438, "fgt_inconsistent": 427, "fgte_inconsistent": 427, "n_with_fgt": 118056}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
