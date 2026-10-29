# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:04:40+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 286 |
| teams | 1038 |
| team_aliases | 2076 |
| team_seasons | 4797 |
| matches | 70364 |
| standings | 14391 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `42`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-19 | 2021-05-23 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-21 | 2022-05-22 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-13 | 2023-06-04 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-19 | 2024-06-02 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-17 | 2025-05-25 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-23 | 2026-05-24 |
| 2026-2027 | True | in_progress | 83 | 20 | 2026-08-22 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 70364 | 70364 | 0 |
| matches (league_season_id, game_index) | 70364 | 70364 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 70364 | 70354 | 10 |
| team_seasons (league_season_id, team_id) | 4797 | 4797 | 0 |
| team_seasons api_name within a season | 4797 | 4797 | 0 |
| team_seasons api_slug within a season | 4797 | 4797 | 0 |
| standings (league_season_id, team_id, view) | 14391 | 14391 | 0 |
| team_aliases (form, value) | 2076 | 2076 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1038 | 1038 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `70364`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 70364 | 0.0% |
| kickoff_time | 0 | 70364 | 0.0% |
| home_team_id | 0 | 70364 | 0.0% |
| away_team_id | 0 | 70364 | 0.0% |
| home_score | 0 | 70364 | 0.0% |
| away_score | 0 | 70364 | 0.0% |
| home_ht | 404 | 69960 | 0.6% |
| away_ht | 404 | 69960 | 0.6% |
| first_goal_time | 5490 | 64874 | 7.8% |
| first_goal_time_extra | 5490 | 64874 | 7.8% |
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
| Home | 962 | 40.7% |
| Draw | 627 | 26.5% |
| Away | 774 | 32.8% |
| Total | 2363 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6372 |
| Average goals per match | 2.697 |
| Home goals | 3401 (avg 1.439) |
| Away goals | 2971 (avg 1.257) |
| Home goal share | 53.4% |
| Goalless matches | 156 (6.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 41.1% | 25.3% | 33.7% | 1163 | 3.061 | 621 | 542 | 19 (5.0%) |
| 2021-2022 | 380 | 38.9% | 25.8% | 35.3% | 1089 | 2.866 | 571 | 518 | 22 (5.8%) |
| 2022-2023 | 380 | 42.4% | 26.3% | 31.3% | 974 | 2.563 | 537 | 437 | 20 (5.3%) |
| 2023-2024 | 380 | 41.8% | 29.5% | 28.7% | 992 | 2.611 | 545 | 447 | 30 (7.9%) |
| 2024-2025 | 380 | 39.7% | 28.4% | 31.8% | 973 | 2.561 | 509 | 464 | 28 (7.4%) |
| 2025-2026 | 380 | 38.9% | 26.1% | 35.0% | 922 | 2.426 | 485 | 437 | 36 (9.5%) |
| 2026-2027 | 83 | 47.0% | 16.9% | 36.1% | 259 | 3.12 | 133 | 126 | 1 (1.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2206` of `2363` (93.4%)
| metric | value |
|---|---|
| First goals recorded | 2206 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 31.04 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 727 |
| 16-30 | 529 |
| 31-45 | 366 |
| 46-60 | 300 |
| 61-75 | 165 |
| 76-90 | 90 |
| 91-120 | 29 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `420`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 20 | 1..20 | 20 |
| 2022-2023 | goals | 20 | 1..20 | 20 |
| 2022-2023 | luck | 20 | 1..20 | 20 |
| 2023-2024 | classic | 20 | 1..20 | 20 |
| 2023-2024 | goals | 20 | 1..20 | 20 |
| 2023-2024 | luck | 20 | 1..20 | 20 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 297 |
| 1-0 | 228 |
| 2-1 | 193 |
| 1-2 | 186 |
| 0-1 | 179 |
| 2-0 | 167 |
| 0-0 | 156 |
| 2-2 | 146 |
| 0-2 | 141 |
| 3-0 | 87 |
| 3-1 | 77 |
| 3-2 | 65 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 4 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1029 | 43.5% |
| Mon | 235 | 9.9% |
| Tue | 48 | 2.0% |
| Wed | 140 | 5.9% |
| Thu | 42 | 1.8% |
| Fri | 168 | 7.1% |
| Sat | 701 | 29.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 83 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | SEASON_AVG_GOALS_OUTLIER | Season 2020-2021 avg goals 3.061 vs overall 2.697 (deviation 0.364) |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 5.0% vs overall 6.6% (deviation 1.6 pp) |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 28.7% vs overall 32.8% |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 9.5% vs overall 6.6% (deviation 2.9 pp) |
| 7 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.12 vs overall 2.697 (deviation 0.423) |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.2% vs overall 6.6% (deviation 5.4 pp) |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 47.0% vs overall 40.7% |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 16.9% vs overall 26.5% |
| 11 | HIGH_SCORING_MATCHES | 11 match(es) with >= 8 total goals (extreme scorelines) |
| 12 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 13 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=349, fgte=349 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 83, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2020-2021", "season_avg_goals": 3.061, "overall_avg_goals": 2.697, "deviation": 0.364}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 5.0, "overall_goalless_pct": 6.6, "deviation_pp": 1.6}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 28.7, "overall_share": 32.8}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 9.5, "overall_goalless_pct": 6.6, "deviation_pp": 2.9}`
- `7.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.12, "overall_avg_goals": 2.697, "deviation": 0.423}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.2, "overall_goalless_pct": 6.6, "deviation_pp": 5.4}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 47.0, "overall_share": 40.7}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 16.9, "overall_share": 26.5}`
- `11.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 11, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 4}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `12.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 70364, "distinct": 70354, "duplicates": 10}`
- `13.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 70364, "fgt_inconsistent": 349, "fgte_inconsistent": 349, "n_with_fgt": 64874}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
