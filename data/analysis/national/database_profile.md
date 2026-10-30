# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:02:41+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `national`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 375 |
| teams | 1359 |
| team_aliases | 2719 |
| team_seasons | 6263 |
| matches | 94411 |
| standings | 18789 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `55`
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
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1089 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1423 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1771 |
| eng1 | League One | England | 7 | 3460 |
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1171 |
| finland1 | Veikkausliiga | Finland | 7 | 946 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2134 |
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1700 |
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
| india1 | ISL | India | 7 | 727 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2368 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2380 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2368 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 594 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1485 |
| national | National League | England | 6 | 2897 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `national`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2021-2022 | False | complete | 506 | 23 | 2021-08-21 | 2022-05-15 |
| 2022-2023 | False | complete | 552 | 24 | 2022-08-06 | 2023-04-29 |
| 2023-2024 | False | complete | 552 | 24 | 2023-08-05 | 2024-04-20 |
| 2024-2025 | False | complete | 552 | 24 | 2024-08-10 | 2025-05-05 |
| 2025-2026 | True | complete | 557 | 24 | 2025-08-09 | 2026-05-10 |
| 2026-2027 | True | in_progress | 178 | 24 | 2026-08-08 | 2026-10-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 94411 | 94411 | 0 |
| matches (league_season_id, game_index) | 94411 | 94411 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 94411 | 94397 | 14 |
| team_seasons (league_season_id, team_id) | 6263 | 6263 | 0 |
| team_seasons api_name within a season | 6263 | 6263 | 0 |
| team_seasons api_slug within a season | 6263 | 6263 | 0 |
| standings (league_season_id, team_id, view) | 18789 | 18789 | 0 |
| team_aliases (form, value) | 2719 | 2719 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1359 | 1359 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `94411`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 94411 | 0.0% |
| kickoff_time | 0 | 94411 | 0.0% |
| home_team_id | 0 | 94411 | 0.0% |
| away_team_id | 0 | 94411 | 0.0% |
| home_score | 0 | 94411 | 0.0% |
| away_score | 0 | 94411 | 0.0% |
| home_ht | 447 | 93964 | 0.5% |
| away_ht | 447 | 93964 | 0.5% |
| first_goal_time | 7580 | 86831 | 8.0% |
| first_goal_time_extra | 7580 | 86831 | 8.0% |
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
| Home | 1257 | 43.4% |
| Draw | 715 | 24.7% |
| Away | 925 | 31.9% |
| Total | 2897 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 8221 |
| Average goals per match | 2.838 |
| Home goals | 4518 (avg 1.56) |
| Away goals | 3703 (avg 1.278) |
| Home goal share | 55.0% |
| Goalless matches | 164 (5.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2021-2022 | 506 | 44.1% | 22.9% | 33.0% | 1386 | 2.739 | 754 | 632 | 36 (7.1%) |
| 2022-2023 | 552 | 44.2% | 25.7% | 30.1% | 1540 | 2.79 | 850 | 690 | 27 (4.9%) |
| 2023-2024 | 552 | 42.2% | 25.5% | 32.2% | 1623 | 2.94 | 899 | 724 | 33 (6.0%) |
| 2024-2025 | 552 | 42.2% | 28.4% | 29.3% | 1488 | 2.696 | 826 | 662 | 37 (6.7%) |
| 2025-2026 | 557 | 43.4% | 23.0% | 33.6% | 1626 | 2.919 | 883 | 743 | 28 (5.0%) |
| 2026-2027 | 178 | 46.1% | 17.4% | 36.5% | 558 | 3.135 | 306 | 252 | 3 (1.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2731` of `2897` (94.3%)
| metric | value |
|---|---|
| First goals recorded | 2731 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 30.57 |
| Median (p50) | 25.0 |
| p25 | 12.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 913 |
| 16-30 | 676 |
| 31-45 | 454 |
| 46-60 | 347 |
| 61-75 | 198 |
| 76-90 | 107 |
| 91-120 | 36 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `429`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2021-2022 | classic | 23 | 1..23 | 23 |
| 2021-2022 | goals | 23 | 1..23 | 23 |
| 2021-2022 | luck | 23 | 1..23 | 23 |
| 2022-2023 | classic | 24 | 1..24 | 24 |
| 2022-2023 | goals | 24 | 1..24 | 24 |
| 2022-2023 | luck | 24 | 1..24 | 24 |
| 2023-2024 | classic | 24 | 1..24 | 24 |
| 2023-2024 | goals | 24 | 1..24 | 24 |
| 2023-2024 | luck | 24 | 1..24 | 24 |
| 2024-2025 | classic | 24 | 1..24 | 24 |
| 2024-2025 | goals | 24 | 1..24 | 24 |
| 2024-2025 | luck | 24 | 1..24 | 24 |
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 361 |
| 1-0 | 265 |
| 2-1 | 248 |
| 1-2 | 216 |
| 0-1 | 211 |
| 2-0 | 191 |
| 0-0 | 164 |
| 0-2 | 162 |
| 2-2 | 150 |
| 3-1 | 114 |
| 3-0 | 107 |
| 3-2 | 97 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-5 | 12 | 1 |
| 6-5 | 11 | 1 |
| 7-3 | 10 | 1 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 1 |
| 3-6 | 9 | 1 |
| 7-1 | 8 | 4 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 7 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 44 | 1.5% |
| Mon | 173 | 6.0% |
| Tue | 683 | 23.6% |
| Wed | 99 | 3.4% |
| Thu | 15 | 0.5% |
| Fri | 100 | 3.5% |
| Sat | 1783 | 61.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 506 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 23 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 552 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 24 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 552 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 24 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 552 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 24 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 557 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 178 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 13 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.7% vs overall 5.7% (deviation 4.0 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 17.4% vs overall 24.7% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 36.5% vs overall 31.9% |
| 17 | HIGH_SCORING_MATCHES | 25 match(es) with >= 8 total goals (extreme scorelines) |
| 18 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 19 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=390, fgte=390 rows) |
| 20 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=23 positions=1..23 teams=23 |
| 21 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=23 positions=1..23 teams=23 |
| 22 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=23 positions=1..23 teams=23 |
| 23 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 24 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 25 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 26 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 27 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 28 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 29 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 30 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 31 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 32 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 33 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 34 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 35 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 506, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 23, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 552, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 24, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 552, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 24, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 552, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 24, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 557, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 178, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `13.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.7, "overall_goalless_pct": 5.7, "deviation_pp": 4.0}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 17.4, "overall_share": 24.7}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 36.5, "overall_share": 31.9}`
- `17.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 25, "threshold": 8, "examples": [{"scoreline": "7-5", "total_goals": 12, "count": 1}, {"scoreline": "6-5", "total_goals": 11, "count": 1}, {"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 4}, {"scoreline": "6-2", "total_goals": 8, "count": 2}]}`
- `18.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 94411, "distinct": 94397, "duplicates": 14}`
- `19.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 94411, "fgt_inconsistent": 390, "fgte_inconsistent": 390, "n_with_fgt": 86831}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
