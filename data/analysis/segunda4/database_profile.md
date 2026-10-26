# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:48:07+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `segunda4`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 515 |
| teams | 1898 |
| team_aliases | 3800 |
| team_seasons | 8638 |
| matches | 129980 |
| standings | 25914 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `76`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `segunda4`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 180 | 20 | 2020-10-18 | 2021-03-21 |
| 2021-2022 | False | complete | 306 | 18 | 2021-09-04 | 2022-05-15 |
| 2022-2023 | False | complete | 306 | 18 | 2022-09-03 | 2023-05-14 |
| 2023-2024 | False | complete | 306 | 18 | 2023-09-02 | 2024-05-05 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-31 | 2025-05-04 |
| 2025-2026 | True | complete | 323 | 19 | 2025-09-06 | 2026-05-03 |
| 2026-2027 | True | in_progress | 67 | 18 | 2026-09-05 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 129980 | 129980 | 0 |
| matches (league_season_id, game_index) | 129980 | 129980 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 129980 | 129956 | 24 |
| team_seasons (league_season_id, team_id) | 8638 | 8638 | 0 |
| team_seasons api_name within a season | 8638 | 8638 | 0 |
| team_seasons api_slug within a season | 8638 | 8638 | 0 |
| standings (league_season_id, team_id, view) | 25914 | 25914 | 0 |
| team_aliases (form, value) | 3800 | 3800 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1898 | 1898 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `129980`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 129980 | 0.0% |
| kickoff_time | 0 | 129980 | 0.0% |
| home_team_id | 0 | 129980 | 0.0% |
| away_team_id | 0 | 129980 | 0.0% |
| home_score | 0 | 129980 | 0.0% |
| away_score | 0 | 129980 | 0.0% |
| home_ht | 488 | 129492 | 0.4% |
| away_ht | 488 | 129492 | 0.4% |
| first_goal_time | 10568 | 119412 | 8.1% |
| first_goal_time_extra | 10568 | 119412 | 8.1% |
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
| Home | 809 | 45.1% |
| Draw | 509 | 28.4% |
| Away | 476 | 26.5% |
| Total | 1794 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3986 |
| Average goals per match | 2.222 |
| Home goals | 2304 (avg 1.284) |
| Away goals | 1682 (avg 0.938) |
| Home goal share | 57.8% |
| Goalless matches | 201 (11.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 180 | 36.1% | 32.8% | 31.1% | 392 | 2.178 | 209 | 183 | 24 (13.3%) |
| 2021-2022 | 306 | 47.4% | 27.5% | 25.2% | 742 | 2.425 | 443 | 299 | 30 (9.8%) |
| 2022-2023 | 306 | 44.4% | 26.5% | 29.1% | 673 | 2.199 | 380 | 293 | 33 (10.8%) |
| 2023-2024 | 306 | 46.1% | 31.4% | 22.5% | 631 | 2.062 | 378 | 253 | 46 (15.0%) |
| 2024-2025 | 306 | 42.5% | 27.5% | 30.1% | 629 | 2.056 | 352 | 277 | 33 (10.8%) |
| 2025-2026 | 323 | 50.2% | 26.0% | 23.8% | 738 | 2.285 | 434 | 304 | 28 (8.7%) |
| 2026-2027 | 67 | 44.8% | 31.3% | 23.9% | 181 | 2.701 | 108 | 73 | 7 (10.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1591` of `1794` (88.7%)
| metric | value |
|---|---|
| First goals recorded | 1591 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 35.13 |
| Median (p50) | 30.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 432 |
| 16-30 | 385 |
| 31-45 | 274 |
| 46-60 | 214 |
| 61-75 | 138 |
| 76-90 | 121 |
| 91-120 | 27 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `387`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
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
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 265 |
| 1-1 | 239 |
| 0-0 | 201 |
| 0-1 | 172 |
| 2-1 | 156 |
| 2-0 | 148 |
| 1-2 | 111 |
| 0-2 | 86 |
| 3-1 | 69 |
| 2-2 | 59 |
| 3-0 | 52 |
| 3-2 | 39 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-0 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1522 | 84.8% |
| Tue | 1 | 0.1% |
| Wed | 26 | 1.4% |
| Sat | 245 | 13.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 180 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 4 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 5 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 6 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 7 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 8 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 9 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 10 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 323 matches, expected 380 |
| 11 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 12 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 67 matches, expected 380 |
| 13 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 14 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 13.3% vs overall 11.2% (deviation 2.1 pp) |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 36.1% vs overall 45.1% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 32.8% vs overall 28.4% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 31.1% vs overall 26.5% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 15.0% vs overall 11.2% (deviation 3.8 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 8.7% vs overall 11.2% (deviation 2.5 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 50.2% vs overall 45.1% |
| 22 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.701 vs overall 2.222 (deviation 0.479) |
| 23 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (24 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=429, fgte=429 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 41 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 180, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `4.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `5.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `6.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `7.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `8.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `9.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `10.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 323, "expected": 380}`
- `11.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `12.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 67, "expected": 380}`
- `13.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `14.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 13.3, "overall_goalless_pct": 11.2, "deviation_pp": 2.1}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 36.1, "overall_share": 45.1}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 32.8, "overall_share": 28.4}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 31.1, "overall_share": 26.5}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 15.0, "overall_goalless_pct": 11.2, "deviation_pp": 3.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 8.7, "overall_goalless_pct": 11.2, "deviation_pp": 2.5}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 50.2, "overall_share": 45.1}`
- `22.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.701, "overall_avg_goals": 2.222, "deviation": 0.479}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 129980, "distinct": 129956, "duplicates": 24}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 129980, "fgt_inconsistent": 429, "fgte_inconsistent": 429, "n_with_fgt": 119412}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
