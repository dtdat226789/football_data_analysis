# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:23:53+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `norway`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 389 |
| teams | 1417 |
| team_aliases | 2835 |
| team_seasons | 6539 |
| matches | 98960 |
| standings | 19617 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `57`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `norway`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 240 | 16 | 2020-06-16 | 2020-12-22 |
| 2021 | False | complete | 240 | 16 | 2021-05-09 | 2021-12-12 |
| 2022 | False | complete | 240 | 16 | 2022-04-02 | 2022-11-13 |
| 2023 | False | complete | 240 | 16 | 2023-04-10 | 2023-12-03 |
| 2024 | False | complete | 240 | 16 | 2024-03-31 | 2024-12-01 |
| 2025 | True | complete | 240 | 16 | 2025-03-29 | 2025-11-30 |
| 2026 | True | in_progress | 192 | 16 | 2026-03-14 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 98960 | 98960 | 0 |
| matches (league_season_id, game_index) | 98960 | 98960 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 98960 | 98946 | 14 |
| team_seasons (league_season_id, team_id) | 6539 | 6539 | 0 |
| team_seasons api_name within a season | 6539 | 6539 | 0 |
| team_seasons api_slug within a season | 6539 | 6539 | 0 |
| standings (league_season_id, team_id, view) | 19617 | 19617 | 0 |
| team_aliases (form, value) | 2835 | 2835 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1417 | 1417 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `98960`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 98960 | 0.0% |
| kickoff_time | 0 | 98960 | 0.0% |
| home_team_id | 0 | 98960 | 0.0% |
| away_team_id | 0 | 98960 | 0.0% |
| home_score | 0 | 98960 | 0.0% |
| away_score | 0 | 98960 | 0.0% |
| home_ht | 455 | 98505 | 0.5% |
| away_ht | 455 | 98505 | 0.5% |
| first_goal_time | 7866 | 91094 | 7.9% |
| first_goal_time_extra | 7866 | 91094 | 7.9% |
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
| Home | 762 | 46.7% |
| Draw | 365 | 22.4% |
| Away | 505 | 30.9% |
| Total | 1632 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5079 |
| Average goals per match | 3.112 |
| Home goals | 2882 (avg 1.766) |
| Away goals | 2197 (avg 1.346) |
| Home goal share | 56.7% |
| Goalless matches | 77 (4.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 240 | 45.0% | 24.2% | 30.8% | 758 | 3.158 | 432 | 326 | 13 (5.4%) |
| 2021 | 240 | 45.4% | 27.1% | 27.5% | 732 | 3.05 | 433 | 299 | 14 (5.8%) |
| 2022 | 240 | 45.4% | 23.8% | 30.8% | 781 | 3.254 | 437 | 344 | 7 (2.9%) |
| 2023 | 240 | 50.8% | 17.5% | 31.7% | 748 | 3.117 | 430 | 318 | 13 (5.4%) |
| 2024 | 240 | 41.7% | 25.0% | 33.3% | 681 | 2.837 | 363 | 318 | 13 (5.4%) |
| 2025 | 240 | 49.2% | 18.8% | 32.1% | 762 | 3.175 | 434 | 328 | 11 (4.6%) |
| 2026 | 192 | 50.0% | 19.8% | 30.2% | 617 | 3.214 | 353 | 264 | 6 (3.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1554` of `1632` (95.2%)
| metric | value |
|---|---|
| First goals recorded | 1554 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 29.37 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 549 |
| 16-30 | 385 |
| 31-45 | 248 |
| 46-60 | 191 |
| 61-75 | 108 |
| 76-90 | 57 |
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
| 1-1 | 168 |
| 2-1 | 141 |
| 1-0 | 130 |
| 1-2 | 115 |
| 2-2 | 97 |
| 2-0 | 94 |
| 0-1 | 94 |
| 3-1 | 78 |
| 0-0 | 77 |
| 3-0 | 75 |
| 0-2 | 68 |
| 1-3 | 61 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-3 | 10 | 1 |
| 5-5 | 10 | 1 |
| 8-1 | 9 | 1 |
| 7-2 | 9 | 3 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 2 |
| 7-1 | 8 | 1 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 5 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 975 | 59.7% |
| Mon | 97 | 5.9% |
| Tue | 27 | 1.7% |
| Wed | 112 | 6.9% |
| Thu | 52 | 3.2% |
| Fri | 49 | 3.0% |
| Sat | 320 | 19.6% |

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
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 192 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2021 draw outcome share 27.1% vs overall 22.4% |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 2.9% vs overall 4.7% (deviation 1.8 pp) |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2023 home outcome share 50.8% vs overall 46.7% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2023 draw outcome share 17.5% vs overall 22.4% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2024 home outcome share 41.7% vs overall 46.7% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 3.1% vs overall 4.7% (deviation 1.6 pp) |
| 22 | HIGH_SCORING_MATCHES | 21 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=394, fgte=394 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
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
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 192, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "draw", "season_share": 27.1, "overall_share": 22.4}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 2.9, "overall_goalless_pct": 4.7, "deviation_pp": 1.8}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "home", "season_share": 50.8, "overall_share": 46.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "draw", "season_share": 17.5, "overall_share": 22.4}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "home", "season_share": 41.7, "overall_share": 46.7}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 3.1, "overall_goalless_pct": 4.7, "deviation_pp": 1.6}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 21, "threshold": 8, "examples": [{"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 3}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 98960, "distinct": 98946, "duplicates": 14}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 98960, "fgt_inconsistent": 394, "fgte_inconsistent": 394, "n_with_fgt": 91094}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
