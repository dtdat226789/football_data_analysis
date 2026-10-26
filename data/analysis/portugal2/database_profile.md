# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:43:11+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `portugal2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 412 |
| teams | 1515 |
| team_aliases | 3031 |
| team_seasons | 6955 |
| matches | 104985 |
| standings | 20865 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `61`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `portugal2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 18 | 2020-09-10 | 2021-05-22 |
| 2021-2022 | False | complete | 306 | 18 | 2021-08-07 | 2022-05-15 |
| 2022-2023 | False | complete | 306 | 18 | 2022-08-06 | 2023-05-28 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-12 | 2024-05-19 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-10 | 2025-05-17 |
| 2025-2026 | True | complete | 310 | 20 | 2025-08-09 | 2026-05-30 |
| 2026-2027 | True | in_progress | 68 | 18 | 2026-08-08 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 104985 | 104985 | 0 |
| matches (league_season_id, game_index) | 104985 | 104985 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 104985 | 104971 | 14 |
| team_seasons (league_season_id, team_id) | 6955 | 6955 | 0 |
| team_seasons api_name within a season | 6955 | 6955 | 0 |
| team_seasons api_slug within a season | 6955 | 6955 | 0 |
| standings (league_season_id, team_id, view) | 20865 | 20865 | 0 |
| team_aliases (form, value) | 3031 | 3031 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1515 | 1515 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `104985`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 104985 | 0.0% |
| kickoff_time | 0 | 104985 | 0.0% |
| home_team_id | 0 | 104985 | 0.0% |
| away_team_id | 0 | 104985 | 0.0% |
| home_score | 0 | 104985 | 0.0% |
| away_score | 0 | 104985 | 0.0% |
| home_ht | 456 | 104529 | 0.4% |
| away_ht | 456 | 104529 | 0.4% |
| first_goal_time | 8337 | 96648 | 7.9% |
| first_goal_time_extra | 8337 | 96648 | 7.9% |
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
| Home | 768 | 40.3% |
| Draw | 526 | 27.6% |
| Away | 614 | 32.2% |
| Total | 1908 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4739 |
| Average goals per match | 2.484 |
| Home goals | 2516 (avg 1.319) |
| Away goals | 2223 (avg 1.165) |
| Home goal share | 53.1% |
| Goalless matches | 164 (8.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 38.9% | 30.4% | 30.7% | 741 | 2.422 | 387 | 354 | 29 (9.5%) |
| 2021-2022 | 306 | 42.2% | 26.8% | 31.0% | 760 | 2.484 | 412 | 348 | 26 (8.5%) |
| 2022-2023 | 306 | 38.9% | 28.4% | 32.7% | 807 | 2.637 | 435 | 372 | 22 (7.2%) |
| 2023-2024 | 306 | 39.5% | 27.5% | 33.0% | 749 | 2.448 | 397 | 352 | 24 (7.8%) |
| 2024-2025 | 306 | 39.2% | 29.4% | 31.4% | 769 | 2.513 | 408 | 361 | 25 (8.2%) |
| 2025-2026 | 310 | 42.3% | 24.5% | 33.2% | 751 | 2.423 | 395 | 356 | 33 (10.6%) |
| 2026-2027 | 68 | 42.6% | 20.6% | 36.8% | 162 | 2.382 | 82 | 80 | 5 (7.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1744` of `1908` (91.4%)
| metric | value |
|---|---|
| First goals recorded | 1744 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 31.76 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 545 |
| 16-30 | 428 |
| 31-45 | 288 |
| 46-60 | 244 |
| 61-75 | 137 |
| 76-90 | 72 |
| 91-120 | 30 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `384`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..18 | 18 |
| 2020-2021 | goals | 18 | 1..18 | 18 |
| 2020-2021 | luck | 18 | 1..18 | 18 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 1..18 | 18 |
| 2024-2025 | luck | 18 | 1..18 | 18 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 248 |
| 1-0 | 206 |
| 2-1 | 177 |
| 0-1 | 172 |
| 1-2 | 171 |
| 0-0 | 164 |
| 2-0 | 131 |
| 2-2 | 103 |
| 0-2 | 96 |
| 3-1 | 71 |
| 3-0 | 53 |
| 1-3 | 50 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-4 | 11 | 1 |
| 6-4 | 10 | 1 |
| 3-6 | 9 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 764 | 40.0% |
| Mon | 194 | 10.2% |
| Tue | 51 | 2.7% |
| Wed | 39 | 2.0% |
| Thu | 34 | 1.8% |
| Fri | 169 | 8.9% |
| Sat | 657 | 34.4% |

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
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 310 matches, expected 380 |
| 12 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 68 matches, expected 380 |
| 13 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 14 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 10.6% vs overall 8.6% (deviation 2.0 pp) |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 20.6% vs overall 27.6% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 36.8% vs overall 32.2% |
| 18 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 19 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 20 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows) |
| 21 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..18 teams=18 |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..18 teams=18 |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..18 teams=18 |
| 24 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 25 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
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
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 310, "expected": 380}`
- `12.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 68, "expected": 380}`
- `13.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `14.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 10.6, "overall_goalless_pct": 8.6, "deviation_pp": 2.0}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 20.6, "overall_share": 27.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 36.8, "overall_share": 32.2}`
- `18.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "7-4", "total_goals": 11, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 2}]}`
- `19.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 104985, "distinct": 104971, "duplicates": 14}`
- `20.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 104985, "fgt_inconsistent": 397, "fgte_inconsistent": 397, "n_with_fgt": 96648}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
