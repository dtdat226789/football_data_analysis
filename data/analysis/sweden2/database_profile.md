# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:32:43+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `sweden2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 571 |
| teams | 2115 |
| team_aliases | 4234 |
| team_seasons | 9681 |
| matches | 146392 |
| standings | 29043 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `84`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2620 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1457 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1640 |
| czech2 | ChNL | Czech Republic | 7 | 1478 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 925 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 61 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3455 |
| eng2 | League Two | England | 7 | 3466 |
| estonia | Meistriliiga | Estonia | 7 | 1167 |
| finland1 | Veikkausliiga | Finland | 7 | 945 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2133 |
| france2 | Ligue 2 | France | 7 | 2224 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1699 |
| germany1 | Bundesliga | Germany | 7 | 1690 |
| germany2 | 2. Bundesliga | Germany | 7 | 1921 |
| germany3 | 3. Liga | Germany | 7 | 2383 |
| greece1 | Super League | Greece | 7 | 1211 |
| greece2 | Super League 2 | Greece | 7 | 1835 |
| holland1 | Eredivisie | Netherlands | 7 | 1941 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1253 |
| hungary2 | NB II. | Hungary | 7 | 2013 |
| india1 | ISL | India | 7 | 725 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2360 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2370 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1023 |
| lithuania | TOPLYGA | Lithuania | 7 | 1112 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2885 |
| north | National League North | England | 7 | 2994 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1965 |
| portugal1 | Liga Portugal | Portugal | 2 | 388 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1911 |
| premier | Premier League | England | 7 | 2360 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1990 |
| romania1 | Superliga | Romania | 7 | 1653 |
| russia | Premier League | Russia | 7 | 1544 |
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |
| saudi2 | Division 1 | Saudi Arabia | 7 | 2054 |
| scot-champ | Championship | Scotland | 7 | 1105 |
| scot-premier | Premiership | Scotland | 7 | 1284 |
| scot1 | League One | Scotland | 7 | 1060 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1782 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1801 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1801 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1799 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1789 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1726 |
| slovenia1 | Prva liga | Slovenia | 7 | 1126 |
| south | National League South | England | 7 | 3000 |
| spain1 | LaLiga | Spain | 7 | 2379 |
| spain2 | LaLiga2 | Spain | 7 | 2939 |
| sweden1 | Allsvenskan | Sweden | 7 | 1640 |
| sweden2 | Superettan | Sweden | 7 | 1662 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `sweden2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 240 | 16 | 2020-06-16 | 2020-12-05 |
| 2021 | False | complete | 240 | 16 | 2021-04-10 | 2021-11-27 |
| 2022 | False | complete | 240 | 16 | 2022-04-02 | 2022-11-05 |
| 2023 | False | complete | 240 | 16 | 2023-04-01 | 2023-11-11 |
| 2024 | False | complete | 240 | 16 | 2024-03-30 | 2024-11-09 |
| 2025 | True | complete | 240 | 16 | 2025-03-29 | 2025-11-08 |
| 2026 | True | in_progress | 222 | 16 | 2026-04-03 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 146392 | 146392 | 0 |
| matches (league_season_id, game_index) | 146392 | 146392 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 146392 | 146347 | 45 |
| team_seasons (league_season_id, team_id) | 9681 | 9681 | 0 |
| team_seasons api_name within a season | 9681 | 9681 | 0 |
| team_seasons api_slug within a season | 9681 | 9681 | 0 |
| standings (league_season_id, team_id, view) | 29043 | 29043 | 0 |
| team_aliases (form, value) | 4234 | 4234 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2115 | 2115 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `146392`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 146392 | 0.0% |
| kickoff_time | 0 | 146392 | 0.0% |
| home_team_id | 0 | 146392 | 0.0% |
| away_team_id | 0 | 146392 | 0.0% |
| home_score | 0 | 146392 | 0.0% |
| away_score | 0 | 146392 | 0.0% |
| home_ht | 503 | 145889 | 0.3% |
| away_ht | 503 | 145889 | 0.3% |
| first_goal_time | 11931 | 134461 | 8.2% |
| first_goal_time_extra | 11931 | 134461 | 8.2% |
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
| Home | 725 | 43.6% |
| Draw | 446 | 26.8% |
| Away | 491 | 29.5% |
| Total | 1662 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4599 |
| Average goals per match | 2.767 |
| Home goals | 2559 (avg 1.54) |
| Away goals | 2040 (avg 1.227) |
| Home goal share | 55.6% |
| Goalless matches | 120 (7.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 240 | 44.2% | 25.8% | 30.0% | 647 | 2.696 | 357 | 290 | 17 (7.1%) |
| 2021 | 240 | 44.6% | 27.1% | 28.3% | 612 | 2.55 | 338 | 274 | 19 (7.9%) |
| 2022 | 240 | 43.3% | 26.2% | 30.4% | 697 | 2.904 | 388 | 309 | 14 (5.8%) |
| 2023 | 240 | 46.2% | 26.7% | 27.1% | 673 | 2.804 | 390 | 283 | 17 (7.1%) |
| 2024 | 240 | 45.0% | 27.9% | 27.1% | 633 | 2.638 | 358 | 275 | 20 (8.3%) |
| 2025 | 240 | 42.1% | 27.1% | 30.8% | 686 | 2.858 | 384 | 302 | 18 (7.5%) |
| 2026 | 222 | 39.6% | 27.0% | 33.3% | 651 | 2.932 | 344 | 307 | 15 (6.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1541` of `1662` (92.7%)
| metric | value |
|---|---|
| First goals recorded | 1541 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 30.23 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 526 |
| 16-30 | 381 |
| 31-45 | 245 |
| 46-60 | 189 |
| 61-75 | 107 |
| 76-90 | 77 |
| 91-120 | 16 |

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
| 1-1 | 192 |
| 2-1 | 156 |
| 1-0 | 147 |
| 0-1 | 126 |
| 0-0 | 120 |
| 2-0 | 119 |
| 1-2 | 114 |
| 2-2 | 111 |
| 0-2 | 75 |
| 3-1 | 61 |
| 3-2 | 55 |
| 3-0 | 53 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 414 | 24.9% |
| Mon | 232 | 14.0% |
| Tue | 157 | 9.4% |
| Wed | 83 | 5.0% |
| Thu | 48 | 2.9% |
| Fri | 80 | 4.8% |
| Sat | 648 | 39.0% |

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
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 222 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 17 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 18 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=441, fgte=441 rows) |
| 19 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=16 positions=1..16 teams=16 |
| 20 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=16 positions=1..16 teams=16 |
| 21 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=16 positions=1..16 teams=16 |
| 22 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=16 positions=1..16 teams=16 |
| 23 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
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
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 222, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `17.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 146392, "distinct": 146347, "duplicates": 45}`
- `18.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 146392, "fgt_inconsistent": 441, "fgte_inconsistent": 441, "n_with_fgt": 134461}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
