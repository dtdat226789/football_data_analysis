# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:59:14+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `japan2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 328 |
| teams | 1229 |
| team_aliases | 2458 |
| team_seasons | 5629 |
| matches | 84405 |
| standings | 16887 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `48`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `japan2`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 462 | 22 | 2020-02-23 | 2020-12-20 |
| 2021 | False | complete | 462 | 22 | 2021-02-27 | 2021-12-05 |
| 2022 | False | complete | 462 | 22 | 2022-02-19 | 2022-10-23 |
| 2023 | False | complete | 462 | 22 | 2023-02-18 | 2023-11-12 |
| 2024 | True | complete | 380 | 20 | 2024-02-24 | 2024-11-10 |
| 2025 | True | complete | 380 | 20 | 2025-02-15 | 2025-11-29 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 84405 | 84405 | 0 |
| matches (league_season_id, game_index) | 84405 | 84405 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 84405 | 84395 | 10 |
| team_seasons (league_season_id, team_id) | 5629 | 5629 | 0 |
| team_seasons api_name within a season | 5629 | 5629 | 0 |
| team_seasons api_slug within a season | 5629 | 5629 | 0 |
| standings (league_season_id, team_id, view) | 16887 | 16887 | 0 |
| team_aliases (form, value) | 2458 | 2458 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1229 | 1229 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `84405`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 84405 | 0.0% |
| kickoff_time | 0 | 84405 | 0.0% |
| home_team_id | 0 | 84405 | 0.0% |
| away_team_id | 0 | 84405 | 0.0% |
| home_score | 0 | 84405 | 0.0% |
| away_score | 0 | 84405 | 0.0% |
| home_ht | 419 | 83986 | 0.5% |
| away_ht | 419 | 83986 | 0.5% |
| first_goal_time | 6744 | 77661 | 8.0% |
| first_goal_time_extra | 6744 | 77661 | 8.0% |
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
| Home | 994 | 38.1% |
| Draw | 721 | 27.6% |
| Away | 893 | 34.2% |
| Total | 2608 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6416 |
| Average goals per match | 2.46 |
| Home goals | 3373 (avg 1.293) |
| Away goals | 3043 (avg 1.167) |
| Home goal share | 52.6% |
| Goalless matches | 242 (9.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 462 | 39.8% | 26.6% | 33.5% | 1119 | 2.422 | 594 | 525 | 42 (9.1%) |
| 2021 | 462 | 35.1% | 29.7% | 35.3% | 1102 | 2.385 | 563 | 539 | 47 (10.2%) |
| 2022 | 462 | 36.6% | 29.0% | 34.4% | 1136 | 2.459 | 593 | 543 | 38 (8.2%) |
| 2023 | 462 | 39.2% | 28.1% | 32.7% | 1179 | 2.552 | 616 | 563 | 40 (8.7%) |
| 2024 | 380 | 40.8% | 23.4% | 35.8% | 946 | 2.489 | 520 | 426 | 37 (9.7%) |
| 2025 | 380 | 37.6% | 28.4% | 33.9% | 934 | 2.458 | 487 | 447 | 38 (10.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2366` of `2608` (90.7%)
| metric | value |
|---|---|
| First goals recorded | 2366 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 33.05 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 710 |
| 16-30 | 555 |
| 31-45 | 416 |
| 46-60 | 331 |
| 61-75 | 172 |
| 76-90 | 141 |
| 91-120 | 41 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `384`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 22 | 1..22 | 22 |
| 2020 | goals | 22 | 1..22 | 22 |
| 2020 | luck | 22 | 1..22 | 22 |
| 2021 | classic | 22 | 1..22 | 22 |
| 2021 | goals | 22 | 1..22 | 22 |
| 2021 | luck | 22 | 1..22 | 22 |
| 2022 | classic | 22 | 1..22 | 22 |
| 2022 | goals | 22 | 1..22 | 22 |
| 2022 | luck | 22 | 1..22 | 22 |
| 2023 | classic | 22 | 1..22 | 22 |
| 2023 | goals | 22 | 1..22 | 22 |
| 2023 | luck | 22 | 1..22 | 22 |
| 2024 | classic | 20 | 1..20 | 20 |
| 2024 | goals | 20 | 1..20 | 20 |
| 2024 | luck | 20 | 1..20 | 20 |
| 2025 | classic | 20 | 1..20 | 20 |
| 2025 | goals | 20 | 1..20 | 20 |
| 2025 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 319 |
| 1-0 | 294 |
| 0-1 | 290 |
| 0-0 | 242 |
| 1-2 | 212 |
| 2-1 | 211 |
| 2-0 | 158 |
| 2-2 | 133 |
| 0-2 | 130 |
| 3-0 | 76 |
| 1-3 | 73 |
| 3-1 | 73 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-1 | 10 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1150 | 44.1% |
| Mon | 27 | 1.0% |
| Tue | 27 | 1.0% |
| Wed | 357 | 13.7% |
| Thu | 1 | 0.0% |
| Fri | 25 | 1.0% |
| Sat | 1021 | 39.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 462 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 22 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 462 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 22 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 462 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 22 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 462 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 22 teams, expected 20 |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2024 draw outcome share 23.4% vs overall 27.6% |
| 10 | HIGH_SCORING_MATCHES | 8 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=366, fgte=366 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=22 positions=1..22 teams=22 |
| 14 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=22 positions=1..22 teams=22 |
| 15 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=22 positions=1..22 teams=22 |
| 16 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=22 positions=1..22 teams=22 |
| 17 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=22 positions=1..22 teams=22 |
| 18 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=22 positions=1..22 teams=22 |
| 19 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=22 positions=1..22 teams=22 |
| 20 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=22 positions=1..22 teams=22 |
| 21 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=22 positions=1..22 teams=22 |
| 22 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=22 positions=1..22 teams=22 |
| 23 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=22 positions=1..22 teams=22 |
| 24 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=22 positions=1..22 teams=22 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 462, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 22, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 462, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 22, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 462, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 22, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 462, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 22, "expected": 20}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "draw", "season_share": 23.4, "overall_share": 27.6}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 8, "threshold": 8, "examples": [{"scoreline": "9-1", "total_goals": 10, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 84405, "distinct": 84395, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 84405, "fgt_inconsistent": 366, "fgte_inconsistent": 366, "n_with_fgt": 77661}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
