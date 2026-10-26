# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:50:46+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `swiss1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 578 |
| teams | 2131 |
| team_aliases | 4266 |
| team_seasons | 9760 |
| matches | 147452 |
| standings | 29280 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `85`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `swiss1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 180 | 10 | 2020-09-19 | 2021-05-21 |
| 2021-2022 | False | complete | 180 | 10 | 2021-07-24 | 2022-05-22 |
| 2022-2023 | False | complete | 180 | 10 | 2022-07-16 | 2023-05-29 |
| 2023-2024 | False | complete | 198 | 12 | 2023-07-22 | 2024-04-21 |
| 2024-2025 | False | complete | 198 | 12 | 2024-07-20 | 2025-04-21 |
| 2025-2026 | True | complete | 230 | 13 | 2025-07-25 | 2026-05-21 |
| 2026-2027 | True | in_progress | 63 | 12 | 2026-07-25 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 147452 | 147452 | 0 |
| matches (league_season_id, game_index) | 147452 | 147452 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 147452 | 147407 | 45 |
| team_seasons (league_season_id, team_id) | 9760 | 9760 | 0 |
| team_seasons api_name within a season | 9760 | 9760 | 0 |
| team_seasons api_slug within a season | 9760 | 9760 | 0 |
| standings (league_season_id, team_id, view) | 29280 | 29280 | 0 |
| team_aliases (form, value) | 4266 | 4266 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2131 | 2131 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `147452`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 147452 | 0.0% |
| kickoff_time | 0 | 147452 | 0.0% |
| home_team_id | 0 | 147452 | 0.0% |
| away_team_id | 0 | 147452 | 0.0% |
| home_score | 0 | 147452 | 0.0% |
| away_score | 0 | 147452 | 0.0% |
| home_ht | 502 | 146950 | 0.3% |
| away_ht | 502 | 146950 | 0.3% |
| first_goal_time | 11973 | 135479 | 8.1% |
| first_goal_time_extra | 11973 | 135479 | 8.1% |
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
| Home | 533 | 43.4% |
| Draw | 328 | 26.7% |
| Away | 368 | 29.9% |
| Total | 1229 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3760 |
| Average goals per match | 3.059 |
| Home goals | 2076 (avg 1.689) |
| Away goals | 1684 (avg 1.37) |
| Home goal share | 55.2% |
| Goalless matches | 54 (4.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 180 | 40.6% | 28.3% | 31.1% | 515 | 2.861 | 281 | 234 | 12 (6.7%) |
| 2021-2022 | 180 | 41.7% | 28.3% | 30.0% | 585 | 3.25 | 317 | 268 | 4 (2.2%) |
| 2022-2023 | 180 | 39.4% | 32.2% | 28.3% | 537 | 2.983 | 297 | 240 | 10 (5.6%) |
| 2023-2024 | 198 | 50.0% | 24.7% | 25.3% | 569 | 2.874 | 330 | 239 | 8 (4.0%) |
| 2024-2025 | 198 | 47.0% | 26.3% | 26.8% | 565 | 2.854 | 321 | 244 | 9 (4.5%) |
| 2025-2026 | 230 | 40.4% | 24.8% | 34.8% | 753 | 3.274 | 407 | 346 | 10 (4.3%) |
| 2026-2027 | 63 | 46.0% | 15.9% | 38.1% | 236 | 3.746 | 123 | 113 | 1 (1.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1174` of `1229` (95.5%)
| metric | value |
|---|---|
| First goals recorded | 1174 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 28.5 |
| Median (p50) | 23.0 |
| p25 | 9.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 446 |
| 16-30 | 278 |
| 31-45 | 181 |
| 46-60 | 128 |
| 61-75 | 87 |
| 76-90 | 41 |
| 91-120 | 13 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `237`
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
| 2023-2024 | classic | 12 | 1..12 | 12 |
| 2023-2024 | goals | 12 | 1..12 | 12 |
| 2023-2024 | luck | 12 | 1..12 | 12 |
| 2024-2025 | classic | 12 | 1..12 | 12 |
| 2024-2025 | goals | 12 | 1..12 | 12 |
| 2024-2025 | luck | 12 | 1..12 | 12 |
| 2025-2026 | classic | 13 | 1..13 | 13 |
| 2025-2026 | goals | 13 | 1..13 | 13 |
| 2025-2026 | luck | 13 | 1..13 | 13 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 159 |
| 2-1 | 118 |
| 1-0 | 93 |
| 2-2 | 91 |
| 1-2 | 85 |
| 0-1 | 72 |
| 2-0 | 67 |
| 3-1 | 62 |
| 0-0 | 54 |
| 0-2 | 52 |
| 3-0 | 47 |
| 1-3 | 40 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-8 | 11 | 1 |
| 2-7 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 544 | 44.3% |
| Mon | 24 | 2.0% |
| Tue | 32 | 2.6% |
| Wed | 98 | 8.0% |
| Thu | 53 | 4.3% |
| Fri | 6 | 0.5% |
| Sat | 472 | 38.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 180 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 198 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 198 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 12 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 230 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 13 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 6.7% vs overall 4.4% (deviation 2.3 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 2.2% vs overall 4.4% (deviation 2.2 pp) |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 32.2% vs overall 26.7% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 50.0% vs overall 43.4% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 25.3% vs overall 29.9% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 away outcome share 34.8% vs overall 29.9% |
| 22 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.746 vs overall 3.059 (deviation 0.687) |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.6% vs overall 4.4% (deviation 2.8 pp) |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 15.9% vs overall 26.7% |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 38.1% vs overall 29.9% |
| 26 | HIGH_SCORING_MATCHES | 8 match(es) with >= 8 total goals (extreme scorelines) |
| 27 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 28 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=442, fgte=442 rows) |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=12 positions=1..12 teams=12 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=13 positions=1..13 teams=13 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=13 positions=1..13 teams=13 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=13 positions=1..13 teams=13 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 180, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 198, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 198, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 12, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 230, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 13, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 6.7, "overall_goalless_pct": 4.4, "deviation_pp": 2.3}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 2.2, "overall_goalless_pct": 4.4, "deviation_pp": 2.2}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 32.2, "overall_share": 26.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 50.0, "overall_share": 43.4}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 25.3, "overall_share": 29.9}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "away", "season_share": 34.8, "overall_share": 29.9}`
- `22.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.746, "overall_avg_goals": 3.059, "deviation": 0.687}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.6, "overall_goalless_pct": 4.4, "deviation_pp": 2.8}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 15.9, "overall_share": 26.7}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 38.1, "overall_share": 29.9}`
- `26.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 8, "threshold": 8, "examples": [{"scoreline": "3-8", "total_goals": 11, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `27.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 147452, "distinct": 147407, "duplicates": 45}`
- `28.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 147452, "fgt_inconsistent": 442, "fgte_inconsistent": 442, "n_with_fgt": 135479}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
