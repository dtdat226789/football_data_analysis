# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:22:28+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `lithuania`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 362 |
| teams | 1304 |
| team_aliases | 2609 |
| team_seasons | 6007 |
| matches | 89966 |
| standings | 18021 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `53`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `lithuania`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 60 | 6 | 2020-03-06 | 2020-11-14 |
| 2021 | False | complete | 180 | 10 | 2021-03-05 | 2021-11-28 |
| 2022 | False | complete | 180 | 10 | 2022-03-04 | 2022-11-23 |
| 2023 | False | complete | 180 | 10 | 2023-03-03 | 2023-11-12 |
| 2024 | False | complete | 180 | 10 | 2024-03-01 | 2024-11-09 |
| 2025 | True | complete | 180 | 10 | 2025-02-28 | 2025-11-08 |
| 2026 | True | in_progress | 152 | 10 | 2026-02-21 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 89966 | 89966 | 0 |
| matches (league_season_id, game_index) | 89966 | 89966 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 89966 | 89952 | 14 |
| team_seasons (league_season_id, team_id) | 6007 | 6007 | 0 |
| team_seasons api_name within a season | 6007 | 6007 | 0 |
| team_seasons api_slug within a season | 6007 | 6007 | 0 |
| standings (league_season_id, team_id, view) | 18021 | 18021 | 0 |
| team_aliases (form, value) | 2609 | 2609 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1304 | 1304 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `89966`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 89966 | 0.0% |
| kickoff_time | 0 | 89966 | 0.0% |
| home_team_id | 0 | 89966 | 0.0% |
| away_team_id | 0 | 89966 | 0.0% |
| home_score | 0 | 89966 | 0.0% |
| away_score | 0 | 89966 | 0.0% |
| home_ht | 448 | 89518 | 0.5% |
| away_ht | 448 | 89518 | 0.5% |
| first_goal_time | 7215 | 82751 | 8.0% |
| first_goal_time_extra | 7215 | 82751 | 8.0% |
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
| Home | 446 | 40.1% |
| Draw | 291 | 26.2% |
| Away | 375 | 33.7% |
| Total | 1112 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2858 |
| Average goals per match | 2.57 |
| Home goals | 1527 (avg 1.373) |
| Away goals | 1331 (avg 1.197) |
| Home goal share | 53.4% |
| Goalless matches | 101 (9.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 60 | 40.0% | 23.3% | 36.7% | 156 | 2.6 | 84 | 72 | 2 (3.3%) |
| 2021 | 180 | 40.0% | 27.2% | 32.8% | 493 | 2.739 | 263 | 230 | 10 (5.6%) |
| 2022 | 180 | 41.7% | 25.6% | 32.8% | 471 | 2.617 | 253 | 218 | 15 (8.3%) |
| 2023 | 180 | 41.1% | 25.6% | 33.3% | 431 | 2.394 | 232 | 199 | 21 (11.7%) |
| 2024 | 180 | 36.7% | 27.8% | 35.6% | 423 | 2.35 | 214 | 209 | 23 (12.8%) |
| 2025 | 180 | 40.6% | 24.4% | 35.0% | 479 | 2.661 | 258 | 221 | 13 (7.2%) |
| 2026 | 152 | 40.8% | 27.6% | 31.6% | 405 | 2.664 | 223 | 182 | 17 (11.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1008` of `1112` (90.6%)
| metric | value |
|---|---|
| First goals recorded | 1008 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 33.13 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 48.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 307 |
| 16-30 | 239 |
| 31-45 | 170 |
| 46-60 | 142 |
| 61-75 | 75 |
| 76-90 | 57 |
| 91-120 | 18 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `198`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 6 | 1..6 | 6 |
| 2020 | goals | 6 | 1..6 | 6 |
| 2020 | luck | 6 | 1..6 | 6 |
| 2021 | classic | 10 | 1..10 | 10 |
| 2021 | goals | 10 | 1..10 | 10 |
| 2021 | luck | 10 | 1..10 | 10 |
| 2022 | classic | 10 | 1..10 | 10 |
| 2022 | goals | 10 | 1..10 | 10 |
| 2022 | luck | 10 | 1..10 | 10 |
| 2023 | classic | 10 | 1..10 | 10 |
| 2023 | goals | 10 | 1..10 | 10 |
| 2023 | luck | 10 | 1..10 | 10 |
| 2024 | classic | 10 | 1..10 | 10 |
| 2024 | goals | 10 | 1..10 | 10 |
| 2024 | luck | 10 | 1..10 | 10 |
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 126 |
| 0-1 | 113 |
| 0-0 | 101 |
| 2-1 | 97 |
| 1-0 | 88 |
| 2-0 | 86 |
| 0-2 | 63 |
| 1-2 | 61 |
| 2-2 | 54 |
| 3-0 | 43 |
| 3-1 | 39 |
| 0-3 | 35 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 363 | 32.6% |
| Mon | 47 | 4.2% |
| Tue | 58 | 5.2% |
| Wed | 117 | 10.5% |
| Thu | 36 | 3.2% |
| Fri | 157 | 14.1% |
| Sat | 334 | 30.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 60 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 6 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 152 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020 goalless share 3.3% vs overall 9.1% (deviation 5.8 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 5.6% vs overall 9.1% (deviation 3.5 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2023 goalless share 11.7% vs overall 9.1% (deviation 2.6 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024 goalless share 12.8% vs overall 9.1% (deviation 3.7 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 7.2% vs overall 9.1% (deviation 1.9 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 11.2% vs overall 9.1% (deviation 2.1 pp) |
| 22 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=388, fgte=388 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=6 positions=1..6 teams=6 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=6 positions=1..6 teams=6 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=6 positions=1..6 teams=6 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=10 positions=1..10 teams=10 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 60, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 6, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 152, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020", "season_goalless_pct": 3.3, "overall_goalless_pct": 9.1, "deviation_pp": 5.8}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 5.6, "overall_goalless_pct": 9.1, "deviation_pp": 3.5}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023", "season_goalless_pct": 11.7, "overall_goalless_pct": 9.1, "deviation_pp": 2.6}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024", "season_goalless_pct": 12.8, "overall_goalless_pct": 9.1, "deviation_pp": 3.7}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 7.2, "overall_goalless_pct": 9.1, "deviation_pp": 1.9}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 11.2, "overall_goalless_pct": 9.1, "deviation_pp": 2.1}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 89966, "distinct": 89952, "duplicates": 14}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 89966, "fgt_inconsistent": 388, "fgte_inconsistent": 388, "n_with_fgt": 82751}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 6, "min_pos": 1, "max_pos": 6, "distinct_teams": 6}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 6, "min_pos": 1, "max_pos": 6, "distinct_teams": 6}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 6, "min_pos": 1, "max_pos": 6, "distinct_teams": 6}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
