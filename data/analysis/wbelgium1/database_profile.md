# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:52:23+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `wbelgium1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 612 |
| teams | 2239 |
| team_aliases | 4482 |
| team_seasons | 10262 |
| matches | 154857 |
| standings | 30786 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `90`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `wbelgium1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 90 | 10 | 2020-08-28 | 2021-03-30 |
| 2021-2022 | False | complete | 90 | 10 | 2021-08-20 | 2022-03-02 |
| 2022-2023 | False | complete | 110 | 11 | 2022-08-12 | 2023-03-04 |
| 2023-2024 | False | complete | 90 | 10 | 2023-08-25 | 2024-03-09 |
| 2024-2025 | False | complete | 84 | 8 | 2024-08-30 | 2025-03-29 |
| 2025-2026 | True | complete | 108 | 8 | 2025-09-06 | 2026-05-23 |
| 2026-2027 | True | in_progress | 28 | 8 | 2026-09-05 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 154857 | 154857 | 0 |
| matches (league_season_id, game_index) | 154857 | 154857 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 154857 | 154812 | 45 |
| team_seasons (league_season_id, team_id) | 10262 | 10262 | 0 |
| team_seasons api_name within a season | 10262 | 10262 | 0 |
| team_seasons api_slug within a season | 10262 | 10262 | 0 |
| standings (league_season_id, team_id, view) | 30786 | 30786 | 0 |
| team_aliases (form, value) | 4482 | 4482 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2239 | 2239 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `154857`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 154857 | 0.0% |
| kickoff_time | 0 | 154857 | 0.0% |
| home_team_id | 0 | 154857 | 0.0% |
| away_team_id | 0 | 154857 | 0.0% |
| home_score | 0 | 154857 | 0.0% |
| away_score | 0 | 154857 | 0.0% |
| home_ht | 568 | 154289 | 0.4% |
| away_ht | 568 | 154289 | 0.4% |
| first_goal_time | 12537 | 142320 | 8.1% |
| first_goal_time_extra | 12537 | 142320 | 8.1% |
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
| Home | 276 | 46.0% |
| Draw | 85 | 14.2% |
| Away | 239 | 39.8% |
| Total | 600 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2031 |
| Average goals per match | 3.385 |
| Home goals | 1106 (avg 1.843) |
| Away goals | 925 (avg 1.542) |
| Home goal share | 54.5% |
| Goalless matches | 25 (4.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 90 | 43.3% | 12.2% | 44.4% | 334 | 3.711 | 175 | 159 | 4 (4.4%) |
| 2021-2022 | 90 | 48.9% | 7.8% | 43.3% | 338 | 3.756 | 191 | 147 | 1 (1.1%) |
| 2022-2023 | 110 | 46.4% | 13.6% | 40.0% | 377 | 3.427 | 209 | 168 | 6 (5.5%) |
| 2023-2024 | 90 | 48.9% | 12.2% | 38.9% | 304 | 3.378 | 176 | 128 | 4 (4.4%) |
| 2024-2025 | 84 | 47.6% | 13.1% | 39.3% | 265 | 3.155 | 143 | 122 | 2 (2.4%) |
| 2025-2026 | 108 | 40.7% | 23.1% | 36.1% | 324 | 3.0 | 161 | 163 | 6 (5.6%) |
| 2026-2027 | 28 | 50.0% | 17.9% | 32.1% | 89 | 3.179 | 51 | 38 | 2 (7.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `575` of `600` (95.8%)
| metric | value |
|---|---|
| First goals recorded | 575 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 27.09 |
| Median (p50) | 20.0 |
| p25 | 9.0 |
| p75 | 40.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 237 |
| 16-30 | 133 |
| 31-45 | 94 |
| 46-60 | 55 |
| 61-75 | 31 |
| 76-90 | 21 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `195`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 10 | 1..10 | 10 |
| 2020-2021 | goals | 10 | 1..10 | 10 |
| 2020-2021 | luck | 10 | 1..10 | 10 |
| 2021-2022 | classic | 10 | 1..10 | 10 |
| 2021-2022 | goals | 10 | 1..10 | 10 |
| 2021-2022 | luck | 10 | 1..10 | 10 |
| 2022-2023 | classic | 11 | 1..11 | 11 |
| 2022-2023 | goals | 11 | 1..11 | 11 |
| 2022-2023 | luck | 11 | 1..11 | 11 |
| 2023-2024 | classic | 10 | 1..10 | 10 |
| 2023-2024 | goals | 10 | 1..10 | 10 |
| 2023-2024 | luck | 10 | 1..10 | 10 |
| 2024-2025 | classic | 8 | 1..8 | 8 |
| 2024-2025 | goals | 8 | 1..8 | 8 |
| 2024-2025 | luck | 8 | 1..8 | 8 |
| 2025-2026 | classic | 8 | 1..8 | 8 |
| 2025-2026 | goals | 8 | 1..8 | 8 |
| 2025-2026 | luck | 8 | 1..8 | 8 |
| 2026-2027 | classic | 8 | 1..8 | 8 |
| 2026-2027 | goals | 8 | 1..8 | 8 |
| 2026-2027 | luck | 8 | 1..8 | 8 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-0 | 50 |
| 0-2 | 40 |
| 1-1 | 40 |
| 0-1 | 37 |
| 2-1 | 35 |
| 1-0 | 33 |
| 1-2 | 30 |
| 3-0 | 28 |
| 0-3 | 27 |
| 0-0 | 25 |
| 0-4 | 24 |
| 1-3 | 23 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-2 | 11 | 1 |
| 0-11 | 11 | 1 |
| 10-0 | 10 | 1 |
| 2-8 | 10 | 1 |
| 1-9 | 10 | 1 |
| 9-0 | 9 | 1 |
| 8-1 | 9 | 3 |
| 7-2 | 9 | 1 |
| 1-8 | 9 | 1 |
| 8-0 | 8 | 4 |
| 7-1 | 8 | 3 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 3 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 34 | 5.7% |
| Tue | 12 | 2.0% |
| Wed | 14 | 2.3% |
| Fri | 156 | 26.0% |
| Sat | 384 | 64.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 90 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 90 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 110 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 11 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 90 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 84 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 8 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 108 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 8 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 28 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 8 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 44.4% vs overall 39.8% |
| 17 | SEASON_AVG_GOALS_OUTLIER | Season 2021-2022 avg goals 3.756 vs overall 3.385 (deviation 0.371) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 1.1% vs overall 4.2% (deviation 3.1 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 7.8% vs overall 14.2% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 2.4% vs overall 4.2% (deviation 1.8 pp) |
| 21 | SEASON_AVG_GOALS_OUTLIER | Season 2025-2026 avg goals 3.0 vs overall 3.385 (deviation 0.385) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 40.7% vs overall 46.0% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 23.1% vs overall 14.2% |
| 24 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.1% vs overall 4.2% (deviation 2.9 pp) |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 32.1% vs overall 39.8% |
| 26 | HIGH_SCORING_MATCHES | 24 match(es) with >= 8 total goals (extreme scorelines) |
| 27 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 28 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=506, fgte=506 rows) |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=11 positions=1..11 teams=11 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=11 positions=1..11 teams=11 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=11 positions=1..11 teams=11 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=8 positions=1..8 teams=8 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=8 positions=1..8 teams=8 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=8 positions=1..8 teams=8 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=8 positions=1..8 teams=8 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=8 positions=1..8 teams=8 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=8 positions=1..8 teams=8 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=8 positions=1..8 teams=8 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=8 positions=1..8 teams=8 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=8 positions=1..8 teams=8 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 90, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 90, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 110, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 11, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 90, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 84, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 8, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 108, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 8, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 28, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 8, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 44.4, "overall_share": 39.8}`
- `17.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2021-2022", "season_avg_goals": 3.756, "overall_avg_goals": 3.385, "deviation": 0.371}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 1.1, "overall_goalless_pct": 4.2, "deviation_pp": 3.1}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 7.8, "overall_share": 14.2}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 2.4, "overall_goalless_pct": 4.2, "deviation_pp": 1.8}`
- `21.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025-2026", "season_avg_goals": 3.0, "overall_avg_goals": 3.385, "deviation": 0.385}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 40.7, "overall_share": 46.0}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 23.1, "overall_share": 14.2}`
- `24.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.1, "overall_goalless_pct": 4.2, "deviation_pp": 2.9}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 32.1, "overall_share": 39.8}`
- `26.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 24, "threshold": 8, "examples": [{"scoreline": "9-2", "total_goals": 11, "count": 1}, {"scoreline": "0-11", "total_goals": 11, "count": 1}, {"scoreline": "10-0", "total_goals": 10, "count": 1}, {"scoreline": "2-8", "total_goals": 10, "count": 1}, {"scoreline": "1-9", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 3}, {"scoreline": "7-2", "total_goals": 9, "count": 1}]}`
- `27.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 154857, "distinct": 154812, "duplicates": 45}`
- `28.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 154857, "fgt_inconsistent": 506, "fgte_inconsistent": 506, "n_with_fgt": 142320}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
