# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:47:29+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `segunda2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 501 |
| teams | 1838 |
| team_aliases | 3680 |
| team_seasons | 8380 |
| matches | 126391 |
| standings | 25140 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `74`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `segunda2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 200 | 21 | 2020-10-17 | 2021-04-02 |
| 2021-2022 | False | complete | 306 | 18 | 2021-09-04 | 2022-05-15 |
| 2022-2023 | False | complete | 306 | 18 | 2022-09-03 | 2023-05-14 |
| 2023-2024 | False | complete | 306 | 18 | 2023-09-03 | 2024-05-05 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-31 | 2025-05-04 |
| 2025-2026 | True | complete | 306 | 18 | 2025-09-06 | 2026-05-03 |
| 2026-2027 | True | in_progress | 67 | 18 | 2026-09-06 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 126391 | 126391 | 0 |
| matches (league_season_id, game_index) | 126391 | 126391 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 126391 | 126371 | 20 |
| team_seasons (league_season_id, team_id) | 8380 | 8380 | 0 |
| team_seasons api_name within a season | 8380 | 8380 | 0 |
| team_seasons api_slug within a season | 8380 | 8380 | 0 |
| standings (league_season_id, team_id, view) | 25140 | 25140 | 0 |
| team_aliases (form, value) | 3680 | 3680 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1838 | 1838 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `126391`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 126391 | 0.0% |
| kickoff_time | 0 | 126391 | 0.0% |
| home_team_id | 0 | 126391 | 0.0% |
| away_team_id | 0 | 126391 | 0.0% |
| home_score | 0 | 126391 | 0.0% |
| away_score | 0 | 126391 | 0.0% |
| home_ht | 486 | 125905 | 0.4% |
| away_ht | 486 | 125905 | 0.4% |
| first_goal_time | 10175 | 116216 | 8.1% |
| first_goal_time_extra | 10175 | 116216 | 8.1% |
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
| Home | 785 | 43.7% |
| Draw | 502 | 27.9% |
| Away | 510 | 28.4% |
| Total | 1797 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4250 |
| Average goals per match | 2.365 |
| Home goals | 2436 (avg 1.356) |
| Away goals | 1814 (avg 1.009) |
| Home goal share | 57.3% |
| Goalless matches | 195 (10.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 200 | 45.0% | 28.0% | 27.0% | 433 | 2.165 | 256 | 177 | 23 (11.5%) |
| 2021-2022 | 306 | 39.2% | 32.0% | 28.8% | 760 | 2.484 | 415 | 345 | 35 (11.4%) |
| 2022-2023 | 306 | 47.4% | 26.5% | 26.1% | 694 | 2.268 | 414 | 280 | 34 (11.1%) |
| 2023-2024 | 306 | 45.4% | 26.1% | 28.4% | 708 | 2.314 | 419 | 289 | 39 (12.7%) |
| 2024-2025 | 306 | 44.1% | 24.8% | 31.0% | 719 | 2.35 | 396 | 323 | 28 (9.2%) |
| 2025-2026 | 306 | 42.5% | 29.1% | 28.4% | 769 | 2.513 | 440 | 329 | 28 (9.2%) |
| 2026-2027 | 67 | 38.8% | 32.8% | 28.4% | 167 | 2.493 | 96 | 71 | 8 (11.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1602` of `1797` (89.1%)
| metric | value |
|---|---|
| First goals recorded | 1602 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 33.91 |
| Median (p50) | 28.0 |
| p25 | 14.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 460 |
| 16-30 | 381 |
| 31-45 | 283 |
| 46-60 | 210 |
| 61-75 | 148 |
| 76-90 | 105 |
| 91-120 | 15 |

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
| 1-1 | 237 |
| 1-0 | 212 |
| 0-0 | 195 |
| 0-1 | 175 |
| 2-0 | 149 |
| 2-1 | 132 |
| 1-2 | 104 |
| 0-2 | 84 |
| 3-1 | 69 |
| 3-0 | 66 |
| 2-2 | 58 |
| 3-2 | 43 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1166 | 64.9% |
| Tue | 1 | 0.1% |
| Wed | 28 | 1.6% |
| Thu | 4 | 0.2% |
| Fri | 7 | 0.4% |
| Sat | 591 | 32.9% |

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
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 67 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 39.2% vs overall 43.7% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 32.0% vs overall 27.9% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 12.7% vs overall 10.9% (deviation 1.8 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 9.2% vs overall 10.9% (deviation 1.7 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 9.2% vs overall 10.9% (deviation 1.7 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 38.8% vs overall 43.7% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 32.8% vs overall 27.9% |
| 23 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=427, fgte=427 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=21 positions=1..21 teams=21 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=21 positions=1..21 teams=21 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=21 positions=1..21 teams=21 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
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
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 67, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 39.2, "overall_share": 43.7}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 32.0, "overall_share": 27.9}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 12.7, "overall_goalless_pct": 10.9, "deviation_pp": 1.8}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 9.2, "overall_goalless_pct": 10.9, "deviation_pp": 1.7}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 9.2, "overall_goalless_pct": 10.9, "deviation_pp": 1.7}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 38.8, "overall_share": 43.7}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 32.8, "overall_share": 27.9}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 126391, "distinct": 126371, "duplicates": 20}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 126391, "fgt_inconsistent": 427, "fgte_inconsistent": 427, "n_with_fgt": 116216}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
