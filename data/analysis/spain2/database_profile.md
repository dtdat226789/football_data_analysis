# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:49:49+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `spain2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 557 |
| teams | 2073 |
| team_aliases | 4150 |
| team_seasons | 9457 |
| matches | 142925 |
| standings | 28371 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `82`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `spain2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 462 | 22 | 2020-09-12 | 2021-05-30 |
| 2021-2022 | False | complete | 462 | 22 | 2021-08-13 | 2022-05-29 |
| 2022-2023 | False | complete | 462 | 22 | 2022-08-12 | 2023-05-28 |
| 2023-2024 | False | complete | 462 | 22 | 2023-08-11 | 2024-06-02 |
| 2024-2025 | False | complete | 462 | 22 | 2024-08-15 | 2025-06-01 |
| 2025-2026 | True | complete | 509 | 23 | 2025-08-15 | 2026-06-20 |
| 2026-2027 | True | in_progress | 116 | 22 | 2026-08-14 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 142925 | 142925 | 0 |
| matches (league_season_id, game_index) | 142925 | 142925 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 142925 | 142880 | 45 |
| team_seasons (league_season_id, team_id) | 9457 | 9457 | 0 |
| team_seasons api_name within a season | 9457 | 9457 | 0 |
| team_seasons api_slug within a season | 9457 | 9457 | 0 |
| standings (league_season_id, team_id, view) | 28371 | 28371 | 0 |
| team_aliases (form, value) | 4150 | 4150 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2073 | 2073 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `142925`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 142925 | 0.0% |
| kickoff_time | 0 | 142925 | 0.0% |
| home_team_id | 0 | 142925 | 0.0% |
| away_team_id | 0 | 142925 | 0.0% |
| home_score | 0 | 142925 | 0.0% |
| away_score | 0 | 142925 | 0.0% |
| home_ht | 500 | 142425 | 0.3% |
| away_ht | 500 | 142425 | 0.3% |
| first_goal_time | 11696 | 131229 | 8.2% |
| first_goal_time_extra | 11696 | 131229 | 8.2% |
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
| Home | 1311 | 44.7% |
| Draw | 846 | 28.8% |
| Away | 778 | 26.5% |
| Total | 2935 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6856 |
| Average goals per match | 2.336 |
| Home goals | 3922 (avg 1.336) |
| Away goals | 2934 (avg 1.0) |
| Home goal share | 57.2% |
| Goalless matches | 304 (10.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 462 | 43.3% | 28.6% | 28.1% | 949 | 2.054 | 541 | 408 | 50 (10.8%) |
| 2021-2022 | 462 | 43.7% | 29.7% | 26.6% | 1122 | 2.429 | 645 | 477 | 43 (9.3%) |
| 2022-2023 | 462 | 44.2% | 33.3% | 22.5% | 932 | 2.017 | 544 | 388 | 68 (14.7%) |
| 2023-2024 | 462 | 46.5% | 30.1% | 23.4% | 1039 | 2.249 | 615 | 424 | 50 (10.8%) |
| 2024-2025 | 462 | 46.3% | 28.1% | 25.5% | 1169 | 2.53 | 670 | 499 | 44 (9.5%) |
| 2025-2026 | 509 | 43.8% | 25.3% | 30.8% | 1335 | 2.623 | 729 | 606 | 40 (7.9%) |
| 2026-2027 | 116 | 45.7% | 21.6% | 32.8% | 310 | 2.672 | 178 | 132 | 9 (7.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2630` of `2935` (89.6%)
| metric | value |
|---|---|
| First goals recorded | 2630 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 34.1 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 768 |
| 16-30 | 600 |
| 31-45 | 442 |
| 46-60 | 391 |
| 61-75 | 222 |
| 76-90 | 155 |
| 91-120 | 52 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `465`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 22 | 1..22 | 22 |
| 2020-2021 | goals | 22 | 1..22 | 22 |
| 2020-2021 | luck | 22 | 1..22 | 22 |
| 2021-2022 | classic | 22 | 1..22 | 22 |
| 2021-2022 | goals | 22 | 1..22 | 22 |
| 2021-2022 | luck | 22 | 1..22 | 22 |
| 2022-2023 | classic | 22 | 1..22 | 22 |
| 2022-2023 | goals | 22 | 1..22 | 22 |
| 2022-2023 | luck | 22 | 1..22 | 22 |
| 2023-2024 | classic | 22 | 1..22 | 22 |
| 2023-2024 | goals | 22 | 1..22 | 22 |
| 2023-2024 | luck | 22 | 1..22 | 22 |
| 2024-2025 | classic | 22 | 1..22 | 22 |
| 2024-2025 | goals | 22 | 1..22 | 22 |
| 2024-2025 | luck | 22 | 1..22 | 22 |
| 2025-2026 | classic | 23 | 1..23 | 23 |
| 2025-2026 | goals | 23 | 1..23 | 23 |
| 2025-2026 | luck | 23 | 1..23 | 23 |
| 2026-2027 | classic | 22 | 1..22 | 22 |
| 2026-2027 | goals | 22 | 1..22 | 22 |
| 2026-2027 | luck | 22 | 1..22 | 22 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 396 |
| 1-1 | 390 |
| 0-0 | 304 |
| 2-1 | 280 |
| 0-1 | 265 |
| 2-0 | 233 |
| 1-2 | 183 |
| 2-2 | 134 |
| 0-2 | 115 |
| 3-1 | 110 |
| 3-0 | 93 |
| 1-3 | 73 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 2 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1184 | 40.3% |
| Mon | 274 | 9.3% |
| Tue | 50 | 1.7% |
| Wed | 84 | 2.9% |
| Thu | 69 | 2.4% |
| Fri | 265 | 9.0% |
| Sat | 1009 | 34.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 462 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 22 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 462 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 22 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 462 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 22 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 462 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 22 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 462 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 22 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 509 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 23 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 116 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 22 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 14.7% vs overall 10.4% (deviation 4.3 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 33.3% vs overall 28.8% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 7.9% vs overall 10.4% (deviation 2.5 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 away outcome share 30.8% vs overall 26.5% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.8% vs overall 10.4% (deviation 2.6 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 21.6% vs overall 28.8% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 32.8% vs overall 26.5% |
| 23 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=440, fgte=440 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=22 positions=1..22 teams=22 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=22 positions=1..22 teams=22 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=22 positions=1..22 teams=22 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=22 positions=1..22 teams=22 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=22 positions=1..22 teams=22 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=22 positions=1..22 teams=22 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=22 positions=1..22 teams=22 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=22 positions=1..22 teams=22 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=22 positions=1..22 teams=22 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=22 positions=1..22 teams=22 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=22 positions=1..22 teams=22 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=22 positions=1..22 teams=22 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=22 positions=1..22 teams=22 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=22 positions=1..22 teams=22 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=22 positions=1..22 teams=22 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=23 positions=1..23 teams=23 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=23 positions=1..23 teams=23 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=23 positions=1..23 teams=23 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=22 positions=1..22 teams=22 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=22 positions=1..22 teams=22 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=22 positions=1..22 teams=22 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 462, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 22, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 462, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 22, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 462, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 22, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 462, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 22, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 462, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 22, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 509, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 23, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 116, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 22, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 14.7, "overall_goalless_pct": 10.4, "deviation_pp": 4.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 33.3, "overall_share": 28.8}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 7.9, "overall_goalless_pct": 10.4, "deviation_pp": 2.5}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "away", "season_share": 30.8, "overall_share": 26.5}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.8, "overall_goalless_pct": 10.4, "deviation_pp": 2.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 21.6, "overall_share": 28.8}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 32.8, "overall_share": 26.5}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 142925, "distinct": 142880, "duplicates": 45}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 142925, "fgt_inconsistent": 440, "fgte_inconsistent": 440, "n_with_fgt": 131229}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
