# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:09:45+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `poland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 403 |
| teams | 1468 |
| team_aliases | 2937 |
| team_seasons | 6790 |
| matches | 102863 |
| standings | 20370 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `59`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `poland2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 18 | 2020-08-28 | 2021-06-13 |
| 2021-2022 | False | complete | 306 | 18 | 2021-07-30 | 2022-05-22 |
| 2022-2023 | False | complete | 306 | 18 | 2022-07-15 | 2023-06-03 |
| 2023-2024 | False | complete | 306 | 18 | 2023-07-21 | 2024-05-26 |
| 2024-2025 | False | complete | 306 | 18 | 2024-07-19 | 2025-05-25 |
| 2025-2026 | True | complete | 328 | 19 | 2025-07-18 | 2026-05-31 |
| 2026-2027 | True | in_progress | 108 | 18 | 2026-07-24 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 102863 | 102863 | 0 |
| matches (league_season_id, game_index) | 102863 | 102863 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 102863 | 102849 | 14 |
| team_seasons (league_season_id, team_id) | 6790 | 6790 | 0 |
| team_seasons api_name within a season | 6790 | 6790 | 0 |
| team_seasons api_slug within a season | 6790 | 6790 | 0 |
| standings (league_season_id, team_id, view) | 20370 | 20370 | 0 |
| team_aliases (form, value) | 2937 | 2937 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1468 | 1468 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `102863`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 102863 | 0.0% |
| kickoff_time | 0 | 102863 | 0.0% |
| home_team_id | 0 | 102863 | 0.0% |
| away_team_id | 0 | 102863 | 0.0% |
| home_score | 0 | 102863 | 0.0% |
| away_score | 0 | 102863 | 0.0% |
| home_ht | 455 | 102408 | 0.4% |
| away_ht | 455 | 102408 | 0.4% |
| first_goal_time | 8158 | 94705 | 7.9% |
| first_goal_time_extra | 8158 | 94705 | 7.9% |
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
| Home | 804 | 40.9% |
| Draw | 536 | 27.3% |
| Away | 626 | 31.8% |
| Total | 1966 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5208 |
| Average goals per match | 2.649 |
| Home goals | 2821 (avg 1.435) |
| Away goals | 2387 (avg 1.214) |
| Home goal share | 54.2% |
| Goalless matches | 146 (7.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 43.8% | 25.5% | 30.7% | 713 | 2.33 | 396 | 317 | 29 (9.5%) |
| 2021-2022 | 306 | 37.9% | 29.4% | 32.7% | 760 | 2.484 | 405 | 355 | 30 (9.8%) |
| 2022-2023 | 306 | 40.2% | 30.1% | 29.7% | 808 | 2.641 | 439 | 369 | 20 (6.5%) |
| 2023-2024 | 306 | 42.5% | 25.5% | 32.0% | 814 | 2.66 | 453 | 361 | 23 (7.5%) |
| 2024-2025 | 306 | 38.2% | 27.1% | 34.6% | 831 | 2.716 | 435 | 396 | 24 (7.8%) |
| 2025-2026 | 328 | 41.5% | 27.1% | 31.4% | 991 | 3.021 | 531 | 460 | 15 (4.6%) |
| 2026-2027 | 108 | 44.4% | 24.1% | 31.5% | 291 | 2.694 | 162 | 129 | 5 (4.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1818` of `1966` (92.5%)
| metric | value |
|---|---|
| First goals recorded | 1818 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 31.72 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 584 |
| 16-30 | 427 |
| 31-45 | 319 |
| 46-60 | 233 |
| 61-75 | 129 |
| 76-90 | 100 |
| 91-120 | 26 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `381`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..19 | 18 |
| 2020-2021 | goals | 18 | 1..19 | 18 |
| 2020-2021 | luck | 18 | 1..19 | 18 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..19 | 18 |
| 2022-2023 | goals | 18 | 1..19 | 18 |
| 2022-2023 | luck | 18 | 1..19 | 18 |
| 2023-2024 | classic | 18 | 1..19 | 18 |
| 2023-2024 | goals | 18 | 1..19 | 18 |
| 2023-2024 | luck | 18 | 1..19 | 18 |
| 2024-2025 | classic | 18 | 1..19 | 18 |
| 2024-2025 | goals | 18 | 2..19 | 18 |
| 2024-2025 | luck | 18 | 1..19 | 18 |
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
| 1-1 | 247 |
| 2-1 | 185 |
| 1-0 | 177 |
| 0-1 | 176 |
| 0-0 | 146 |
| 1-2 | 144 |
| 2-0 | 138 |
| 2-2 | 118 |
| 0-2 | 97 |
| 3-0 | 79 |
| 3-1 | 65 |
| 1-3 | 47 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 602 | 30.6% |
| Mon | 156 | 7.9% |
| Tue | 48 | 2.4% |
| Wed | 84 | 4.3% |
| Thu | 49 | 2.5% |
| Fri | 368 | 18.7% |
| Sat | 659 | 33.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 328 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 108 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 9.5% vs overall 7.4% (deviation 2.1 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 9.8% vs overall 7.4% (deviation 2.4 pp) |
| 18 | SEASON_AVG_GOALS_OUTLIER | Season 2025-2026 avg goals 3.021 vs overall 2.649 (deviation 0.372) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 4.6% vs overall 7.4% (deviation 2.8 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.6% vs overall 7.4% (deviation 2.8 pp) |
| 21 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..19 teams=18 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..19 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..19 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..19 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..19 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..19 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..19 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..19 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..19 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..19 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=2..19 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..19 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 328, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 108, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 9.5, "overall_goalless_pct": 7.4, "deviation_pp": 2.1}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 9.8, "overall_goalless_pct": 7.4, "deviation_pp": 2.4}`
- `18.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025-2026", "season_avg_goals": 3.021, "overall_avg_goals": 2.649, "deviation": 0.372}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 4.6, "overall_goalless_pct": 7.4, "deviation_pp": 2.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.6, "overall_goalless_pct": 7.4, "deviation_pp": 2.8}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 102863, "distinct": 102849, "duplicates": 14}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 102863, "fgt_inconsistent": 397, "fgte_inconsistent": 397, "n_with_fgt": 94705}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 2, "max_pos": 19, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
