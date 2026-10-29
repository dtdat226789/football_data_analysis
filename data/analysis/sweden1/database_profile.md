# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:17:09+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `sweden1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 564 |
| teams | 2098 |
| team_aliases | 4200 |
| team_seasons | 9569 |
| matches | 144817 |
| standings | 28707 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `83`
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
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3460 |
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1169 |
| finland1 | Veikkausliiga | Finland | 7 | 945 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2134 |
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1699 |
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
| india1 | ISL | India | 7 | 726 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2363 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2377 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2894 |
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
| saudi2 | Division 1 | Saudi Arabia | 7 | 2058 |
| scot-champ | Championship | Scotland | 7 | 1106 |
| scot-premier | Premiership | Scotland | 7 | 1284 |
| scot1 | League One | Scotland | 7 | 1061 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1782 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1801 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1801 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1799 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1789 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1726 |
| slovenia1 | Prva liga | Slovenia | 7 | 1128 |
| south | National League South | England | 7 | 3011 |
| spain1 | LaLiga | Spain | 7 | 2380 |
| spain2 | LaLiga2 | Spain | 7 | 2940 |
| sweden1 | Allsvenskan | Sweden | 7 | 1641 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `sweden1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 240 | 16 | 2020-06-14 | 2020-12-06 |
| 2021 | False | complete | 240 | 16 | 2021-04-10 | 2021-12-04 |
| 2022 | False | complete | 240 | 16 | 2022-04-02 | 2022-11-06 |
| 2023 | False | complete | 240 | 16 | 2023-04-01 | 2023-11-12 |
| 2024 | False | complete | 240 | 16 | 2024-03-30 | 2024-11-10 |
| 2025 | True | complete | 240 | 16 | 2025-03-29 | 2025-11-09 |
| 2026 | True | in_progress | 201 | 16 | 2026-04-04 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 144817 | 144817 | 0 |
| matches (league_season_id, game_index) | 144817 | 144817 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 144817 | 144772 | 45 |
| team_seasons (league_season_id, team_id) | 9569 | 9569 | 0 |
| team_seasons api_name within a season | 9569 | 9569 | 0 |
| team_seasons api_slug within a season | 9569 | 9569 | 0 |
| standings (league_season_id, team_id, view) | 28707 | 28707 | 0 |
| team_aliases (form, value) | 4200 | 4200 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2098 | 2098 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `144817`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 144817 | 0.0% |
| kickoff_time | 0 | 144817 | 0.0% |
| home_team_id | 0 | 144817 | 0.0% |
| away_team_id | 0 | 144817 | 0.0% |
| home_score | 0 | 144817 | 0.0% |
| away_score | 0 | 144817 | 0.0% |
| home_ht | 499 | 144318 | 0.3% |
| away_ht | 499 | 144318 | 0.3% |
| first_goal_time | 11813 | 133004 | 8.2% |
| first_goal_time_extra | 11813 | 133004 | 8.2% |
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
| Home | 700 | 42.7% |
| Draw | 396 | 24.1% |
| Away | 545 | 33.2% |
| Total | 1641 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4590 |
| Average goals per match | 2.797 |
| Home goals | 2516 (avg 1.533) |
| Away goals | 2074 (avg 1.264) |
| Home goal share | 54.8% |
| Goalless matches | 101 (6.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 240 | 37.1% | 32.1% | 30.8% | 674 | 2.808 | 356 | 318 | 17 (7.1%) |
| 2021 | 240 | 45.0% | 24.6% | 30.4% | 638 | 2.658 | 365 | 273 | 19 (7.9%) |
| 2022 | 240 | 44.2% | 25.0% | 30.8% | 662 | 2.758 | 371 | 291 | 15 (6.2%) |
| 2023 | 240 | 46.7% | 19.6% | 33.8% | 665 | 2.771 | 373 | 292 | 17 (7.1%) |
| 2024 | 240 | 45.4% | 21.7% | 32.9% | 680 | 2.833 | 376 | 304 | 11 (4.6%) |
| 2025 | 240 | 40.0% | 22.1% | 37.9% | 683 | 2.846 | 354 | 329 | 14 (5.8%) |
| 2026 | 201 | 39.8% | 23.9% | 36.3% | 588 | 2.925 | 321 | 267 | 8 (4.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1540` of `1641` (93.8%)
| metric | value |
|---|---|
| First goals recorded | 1540 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 30.79 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 519 |
| 16-30 | 363 |
| 31-45 | 243 |
| 46-60 | 232 |
| 61-75 | 92 |
| 76-90 | 65 |
| 91-120 | 26 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `336`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 16 | 1..16 | 16 |
| 2020 | goals | 16 | 1..16 | 16 |
| 2020 | luck | 16 | 1..16 | 16 |
| 2021 | classic | 16 | 1..16 | 16 |
| 2021 | goals | 16 | 1..16 | 16 |
| 2021 | luck | 16 | 1..16 | 16 |
| 2022 | classic | 16 | 1..16 | 16 |
| 2022 | goals | 16 | 1..16 | 16 |
| 2022 | luck | 16 | 1..16 | 16 |
| 2023 | classic | 16 | 1..16 | 16 |
| 2023 | goals | 16 | 1..16 | 16 |
| 2023 | luck | 16 | 1..16 | 16 |
| 2024 | classic | 16 | 1..16 | 16 |
| 2024 | goals | 16 | 1..16 | 16 |
| 2024 | luck | 16 | 1..16 | 16 |
| 2025 | classic | 16 | 1..16 | 16 |
| 2025 | goals | 16 | 1..16 | 16 |
| 2025 | luck | 16 | 1..16 | 16 |
| 2026 | classic | 16 | 1..16 | 16 |
| 2026 | goals | 16 | 1..16 | 16 |
| 2026 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 187 |
| 0-1 | 141 |
| 1-0 | 133 |
| 1-2 | 131 |
| 2-0 | 131 |
| 2-1 | 123 |
| 0-0 | 101 |
| 2-2 | 90 |
| 3-0 | 78 |
| 0-2 | 72 |
| 3-1 | 66 |
| 1-3 | 52 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-6 | 11 | 1 |
| 8-2 | 10 | 1 |
| 6-4 | 10 | 1 |
| 8-1 | 9 | 1 |
| 4-5 | 9 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 752 | 45.8% |
| Mon | 335 | 20.4% |
| Tue | 9 | 0.5% |
| Wed | 72 | 4.4% |
| Thu | 95 | 5.8% |
| Fri | 27 | 1.6% |
| Sat | 351 | 21.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 240 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 16 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 201 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020 home outcome share 37.1% vs overall 42.7% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 draw outcome share 32.1% vs overall 24.1% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 7.9% vs overall 6.2% (deviation 1.7 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2023 draw outcome share 19.6% vs overall 24.1% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2024 goalless share 4.6% vs overall 6.2% (deviation 1.6 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2025 away outcome share 37.9% vs overall 33.2% |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 4.0% vs overall 6.2% (deviation 2.2 pp) |
| 23 | HIGH_SCORING_MATCHES | 11 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=440, fgte=440 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 240, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 16, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 201, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "home", "season_share": 37.1, "overall_share": 42.7}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "draw", "season_share": 32.1, "overall_share": 24.1}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 7.9, "overall_goalless_pct": 6.2, "deviation_pp": 1.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "draw", "season_share": 19.6, "overall_share": 24.1}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024", "season_goalless_pct": 4.6, "overall_goalless_pct": 6.2, "deviation_pp": 1.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025", "outcome": "away", "season_share": 37.9, "overall_share": 33.2}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 4.0, "overall_goalless_pct": 6.2, "deviation_pp": 2.2}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 11, "threshold": 8, "examples": [{"scoreline": "5-6", "total_goals": 11, "count": 1}, {"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 144817, "distinct": 144772, "duplicates": 45}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 144817, "fgt_inconsistent": 440, "fgte_inconsistent": 440, "n_with_fgt": 133004}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
