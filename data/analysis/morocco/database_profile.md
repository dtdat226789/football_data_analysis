# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:41:07+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `morocco`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 369 |
| teams | 1330 |
| team_aliases | 2661 |
| team_seasons | 6120 |
| matches | 91353 |
| standings | 18360 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `54`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `morocco`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-12-04 | 2021-07-28 |
| 2021-2022 | False | complete | 240 | 16 | 2021-09-10 | 2022-07-05 |
| 2022-2023 | False | complete | 240 | 16 | 2022-09-01 | 2023-06-23 |
| 2023-2024 | False | complete | 240 | 16 | 2023-08-25 | 2024-06-14 |
| 2024-2025 | False | complete | 240 | 16 | 2024-08-30 | 2025-05-12 |
| 2025-2026 | True | complete | 248 | 17 | 2025-09-12 | 2026-07-05 |
| 2026-2027 | True | in_progress | 33 | 16 | 2026-09-24 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 91353 | 91353 | 0 |
| matches (league_season_id, game_index) | 91353 | 91353 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 91353 | 91339 | 14 |
| team_seasons (league_season_id, team_id) | 6120 | 6120 | 0 |
| team_seasons api_name within a season | 6120 | 6120 | 0 |
| team_seasons api_slug within a season | 6120 | 6120 | 0 |
| standings (league_season_id, team_id, view) | 18360 | 18360 | 0 |
| team_aliases (form, value) | 2661 | 2661 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1330 | 1330 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `91353`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 91353 | 0.0% |
| kickoff_time | 0 | 91353 | 0.0% |
| home_team_id | 0 | 91353 | 0.0% |
| away_team_id | 0 | 91353 | 0.0% |
| home_score | 0 | 91353 | 0.0% |
| away_score | 0 | 91353 | 0.0% |
| home_ht | 446 | 90907 | 0.5% |
| away_ht | 446 | 90907 | 0.5% |
| first_goal_time | 7402 | 83951 | 8.1% |
| first_goal_time_extra | 7402 | 83951 | 8.1% |
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
| Home | 592 | 40.0% |
| Draw | 474 | 32.0% |
| Away | 415 | 28.0% |
| Total | 1481 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3284 |
| Average goals per match | 2.217 |
| Home goals | 1773 (avg 1.197) |
| Away goals | 1511 (avg 1.02) |
| Home goal share | 54.0% |
| Goalless matches | 194 (13.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 37.9% | 32.9% | 29.2% | 540 | 2.25 | 295 | 245 | 34 (14.2%) |
| 2021-2022 | 240 | 40.8% | 34.2% | 25.0% | 519 | 2.163 | 284 | 235 | 40 (16.7%) |
| 2022-2023 | 240 | 40.8% | 32.1% | 27.1% | 512 | 2.133 | 285 | 227 | 34 (14.2%) |
| 2023-2024 | 240 | 41.2% | 30.4% | 28.3% | 534 | 2.225 | 292 | 242 | 30 (12.5%) |
| 2024-2025 | 240 | 43.3% | 28.3% | 28.3% | 555 | 2.312 | 298 | 257 | 22 (9.2%) |
| 2025-2026 | 248 | 37.9% | 34.3% | 27.8% | 539 | 2.173 | 285 | 254 | 29 (11.7%) |
| 2026-2027 | 33 | 24.2% | 30.3% | 45.5% | 85 | 2.576 | 34 | 51 | 5 (15.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1287` of `1481` (86.9%)
| metric | value |
|---|---|
| First goals recorded | 1287 |
| Min minute | 1 |
| Max minute | 104 |
| Mean minute | 34.92 |
| Median (p50) | 31.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 357 |
| 16-30 | 284 |
| 31-45 | 220 |
| 46-60 | 216 |
| 61-75 | 102 |
| 76-90 | 74 |
| 91-120 | 34 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `339`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 16 | 1..16 | 16 |
| 2021-2022 | goals | 16 | 1..16 | 16 |
| 2021-2022 | luck | 16 | 1..16 | 16 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 216 |
| 0-0 | 194 |
| 1-0 | 178 |
| 2-1 | 150 |
| 0-1 | 133 |
| 1-2 | 102 |
| 2-0 | 101 |
| 0-2 | 69 |
| 2-2 | 57 |
| 3-0 | 47 |
| 3-1 | 43 |
| 3-2 | 37 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 425 | 28.7% |
| Mon | 65 | 4.4% |
| Tue | 99 | 6.7% |
| Wed | 191 | 12.9% |
| Thu | 141 | 9.5% |
| Fri | 186 | 12.6% |
| Sat | 374 | 25.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 248 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 33 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 16.7% vs overall 13.1% (deviation 3.6 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 9.2% vs overall 13.1% (deviation 3.9 pp) |
| 18 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.576 vs overall 2.217 (deviation 0.359) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 15.2% vs overall 13.1% (deviation 2.1 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 24.2% vs overall 40.0% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 45.5% vs overall 28.0% |
| 22 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=388, fgte=388 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 248, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 33, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 16.7, "overall_goalless_pct": 13.1, "deviation_pp": 3.6}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 9.2, "overall_goalless_pct": 13.1, "deviation_pp": 3.9}`
- `18.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.576, "overall_avg_goals": 2.217, "deviation": 0.359}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 15.2, "overall_goalless_pct": 13.1, "deviation_pp": 2.1}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 24.2, "overall_share": 40.0}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 45.5, "overall_share": 28.0}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 91353, "distinct": 91339, "duplicates": 14}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 91353, "fgt_inconsistent": 388, "fgte_inconsistent": 388, "n_with_fgt": 83951}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
