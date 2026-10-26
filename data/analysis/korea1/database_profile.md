# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:39:36+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `korea1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 335 |
| teams | 1246 |
| team_aliases | 2492 |
| team_seasons | 5713 |
| matches | 85642 |
| standings | 17139 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `49`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `korea1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 132 | 12 | 2020-05-08 | 2020-09-20 |
| 2021 | False | complete | 198 | 12 | 2021-02-27 | 2021-10-24 |
| 2022 | False | complete | 198 | 12 | 2022-02-19 | 2022-09-18 |
| 2023 | False | complete | 198 | 12 | 2023-02-25 | 2023-10-08 |
| 2024 | False | complete | 198 | 12 | 2024-03-01 | 2024-10-06 |
| 2025 | True | complete | 198 | 12 | 2025-02-15 | 2025-10-18 |
| 2026 | True | in_progress | 198 | 12 | 2026-02-28 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 85642 | 85642 | 0 |
| matches (league_season_id, game_index) | 85642 | 85642 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 85642 | 85632 | 10 |
| team_seasons (league_season_id, team_id) | 5713 | 5713 | 0 |
| team_seasons api_name within a season | 5713 | 5713 | 0 |
| team_seasons api_slug within a season | 5713 | 5713 | 0 |
| standings (league_season_id, team_id, view) | 17139 | 17139 | 0 |
| team_aliases (form, value) | 2492 | 2492 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1246 | 1246 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `85642`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 85642 | 0.0% |
| kickoff_time | 0 | 85642 | 0.0% |
| home_team_id | 0 | 85642 | 0.0% |
| away_team_id | 0 | 85642 | 0.0% |
| home_score | 0 | 85642 | 0.0% |
| away_score | 0 | 85642 | 0.0% |
| home_ht | 418 | 85224 | 0.5% |
| away_ht | 418 | 85224 | 0.5% |
| first_goal_time | 6853 | 78789 | 8.0% |
| first_goal_time_extra | 6853 | 78789 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 518 | 39.2% |
| Draw | 376 | 28.5% |
| Away | 426 | 32.3% |
| Total | 1320 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3367 |
| Average goals per match | 2.551 |
| Home goals | 1769 (avg 1.34) |
| Away goals | 1598 (avg 1.211) |
| Home goal share | 52.5% |
| Goalless matches | 114 (8.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 132 | 37.9% | 26.5% | 35.6% | 338 | 2.561 | 171 | 167 | 12 (9.1%) |
| 2021 | 198 | 38.9% | 28.8% | 32.3% | 482 | 2.434 | 249 | 233 | 23 (11.6%) |
| 2022 | 198 | 38.9% | 29.8% | 31.3% | 508 | 2.566 | 269 | 239 | 13 (6.6%) |
| 2023 | 198 | 38.9% | 30.3% | 30.8% | 498 | 2.515 | 267 | 231 | 16 (8.1%) |
| 2024 | 198 | 46.0% | 23.2% | 30.8% | 533 | 2.692 | 297 | 236 | 12 (6.1%) |
| 2025 | 198 | 41.9% | 26.3% | 31.8% | 512 | 2.586 | 275 | 237 | 16 (8.1%) |
| 2026 | 198 | 31.8% | 33.8% | 34.3% | 496 | 2.505 | 241 | 255 | 22 (11.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1205` of `1320` (91.3%)
| metric | value |
|---|---|
| First goals recorded | 1205 |
| Min minute | 1 |
| Max minute | 100 |
| Mean minute | 36.21 |
| Median (p50) | 31.0 |
| p25 | 15.0 |
| p75 | 53.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 304 |
| 16-30 | 290 |
| 31-45 | 201 |
| 46-60 | 182 |
| 61-75 | 118 |
| 76-90 | 79 |
| 91-120 | 31 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `252`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 12 | 1..12 | 12 |
| 2020 | goals | 12 | 1..12 | 12 |
| 2020 | luck | 12 | 1..12 | 12 |
| 2021 | classic | 12 | 1..12 | 12 |
| 2021 | goals | 12 | 1..12 | 12 |
| 2021 | luck | 12 | 1..12 | 12 |
| 2022 | classic | 12 | 1..12 | 12 |
| 2022 | goals | 12 | 1..12 | 12 |
| 2022 | luck | 12 | 1..12 | 12 |
| 2023 | classic | 12 | 1..12 | 12 |
| 2023 | goals | 12 | 1..12 | 12 |
| 2023 | luck | 12 | 1..12 | 12 |
| 2024 | classic | 12 | 1..12 | 12 |
| 2024 | goals | 12 | 1..12 | 12 |
| 2024 | luck | 12 | 1..12 | 12 |
| 2025 | classic | 12 | 1..12 | 12 |
| 2025 | goals | 12 | 1..12 | 12 |
| 2025 | luck | 12 | 1..12 | 12 |
| 2026 | classic | 12 | 1..12 | 12 |
| 2026 | goals | 12 | 1..12 | 12 |
| 2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 172 |
| 1-0 | 140 |
| 0-1 | 127 |
| 0-0 | 114 |
| 2-1 | 114 |
| 1-2 | 107 |
| 2-0 | 92 |
| 2-2 | 81 |
| 3-1 | 50 |
| 0-2 | 50 |
| 3-2 | 39 |
| 1-3 | 37 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 459 | 34.8% |
| Mon | 12 | 0.9% |
| Tue | 100 | 7.6% |
| Wed | 139 | 10.5% |
| Thu | 6 | 0.5% |
| Fri | 73 | 5.5% |
| Sat | 531 | 40.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 198 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 198 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 198 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 198 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 12 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 198 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 12 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 198 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 11.6% vs overall 8.6% (deviation 3.0 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 6.6% vs overall 8.6% (deviation 2.0 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2024 goalless share 6.1% vs overall 8.6% (deviation 2.5 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2024 home outcome share 46.0% vs overall 39.2% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2024 draw outcome share 23.2% vs overall 28.5% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 11.1% vs overall 8.6% (deviation 2.5 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026 home outcome share 31.8% vs overall 39.2% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026 draw outcome share 33.8% vs overall 28.5% |
| 24 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=367, fgte=367 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=12 positions=1..12 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=12 positions=1..12 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=12 positions=1..12 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=12 positions=1..12 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=12 positions=1..12 teams=12 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=12 positions=1..12 teams=12 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=12 positions=1..12 teams=12 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=12 positions=1..12 teams=12 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=12 positions=1..12 teams=12 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=12 positions=1..12 teams=12 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 198, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 198, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 198, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 198, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 12, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 198, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 12, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 198, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 11.6, "overall_goalless_pct": 8.6, "deviation_pp": 3.0}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 6.6, "overall_goalless_pct": 8.6, "deviation_pp": 2.0}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024", "season_goalless_pct": 6.1, "overall_goalless_pct": 8.6, "deviation_pp": 2.5}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "home", "season_share": 46.0, "overall_share": 39.2}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "draw", "season_share": 23.2, "overall_share": 28.5}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 11.1, "overall_goalless_pct": 8.6, "deviation_pp": 2.5}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "home", "season_share": 31.8, "overall_share": 39.2}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "draw", "season_share": 33.8, "overall_share": 28.5}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 85642, "distinct": 85632, "duplicates": 10}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 85642, "fgt_inconsistent": 367, "fgte_inconsistent": 367, "n_with_fgt": 78789}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
