# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:58:46+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 300 |
| teams | 1116 |
| team_aliases | 2232 |
| team_seasons | 5067 |
| matches | 74760 |
| standings | 15201 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `44`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-25 | 2021-05-10 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-20 | 2022-05-06 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-12 | 2023-05-19 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-18 | 2024-05-10 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-16 | 2025-05-13 |
| 2025-2026 | True | complete | 390 | 20 | 2025-08-22 | 2026-05-29 |
| 2026-2027 | True | in_progress | 90 | 20 | 2026-08-21 | 2026-10-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 74760 | 74760 | 0 |
| matches (league_season_id, game_index) | 74760 | 74760 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 74760 | 74750 | 10 |
| team_seasons (league_season_id, team_id) | 5067 | 5067 | 0 |
| team_seasons api_name within a season | 5067 | 5067 | 0 |
| team_seasons api_slug within a season | 5067 | 5067 | 0 |
| standings (league_season_id, team_id, view) | 15201 | 15201 | 0 |
| team_aliases (form, value) | 2232 | 2232 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1116 | 1116 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `74760`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 74760 | 0.0% |
| kickoff_time | 0 | 74760 | 0.0% |
| home_team_id | 0 | 74760 | 0.0% |
| away_team_id | 0 | 74760 | 0.0% |
| home_score | 0 | 74760 | 0.0% |
| away_score | 0 | 74760 | 0.0% |
| home_ht | 412 | 74348 | 0.6% |
| away_ht | 412 | 74348 | 0.6% |
| first_goal_time | 5820 | 68940 | 7.8% |
| first_goal_time_extra | 5820 | 68940 | 7.8% |
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
| Home | 949 | 39.9% |
| Draw | 766 | 32.2% |
| Away | 665 | 27.9% |
| Total | 2380 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5876 |
| Average goals per match | 2.469 |
| Home goals | 3233 (avg 1.358) |
| Away goals | 2643 (avg 1.111) |
| Home goal share | 55.0% |
| Goalless matches | 217 (9.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.6% | 34.5% | 27.9% | 913 | 2.403 | 495 | 418 | 38 (10.0%) |
| 2021-2022 | 380 | 40.0% | 30.8% | 29.2% | 942 | 2.479 | 524 | 418 | 27 (7.1%) |
| 2022-2023 | 380 | 40.5% | 32.1% | 27.4% | 891 | 2.345 | 492 | 399 | 42 (11.1%) |
| 2023-2024 | 380 | 36.6% | 32.1% | 31.3% | 958 | 2.521 | 509 | 449 | 37 (9.7%) |
| 2024-2025 | 380 | 40.3% | 33.7% | 26.1% | 937 | 2.466 | 514 | 423 | 40 (10.5%) |
| 2025-2026 | 390 | 44.9% | 31.0% | 24.1% | 993 | 2.546 | 577 | 416 | 30 (7.7%) |
| 2026-2027 | 90 | 36.7% | 27.8% | 35.6% | 242 | 2.689 | 122 | 120 | 3 (3.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2161` of `2380` (90.8%)
| metric | value |
|---|---|
| First goals recorded | 2161 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 31.53 |
| Median (p50) | 27.0 |
| p25 | 13.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 652 |
| 16-30 | 561 |
| 31-45 | 375 |
| 46-60 | 299 |
| 61-75 | 140 |
| 76-90 | 110 |
| 91-120 | 24 |

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
| 1-1 | 370 |
| 1-0 | 251 |
| 0-0 | 217 |
| 2-1 | 205 |
| 0-1 | 189 |
| 1-2 | 172 |
| 2-0 | 162 |
| 2-2 | 151 |
| 0-2 | 115 |
| 3-0 | 93 |
| 3-1 | 87 |
| 1-3 | 59 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 4 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 549 | 23.1% |
| Mon | 146 | 6.1% |
| Tue | 208 | 8.7% |
| Wed | 106 | 4.5% |
| Thu | 40 | 1.7% |
| Fri | 242 | 10.2% |
| Sat | 1089 | 45.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 390 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 90 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 7.1% vs overall 9.1% (deviation 2.0 pp) |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 11.1% vs overall 9.1% (deviation 2.0 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 44.9% vs overall 39.9% |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.3% vs overall 9.1% (deviation 5.8 pp) |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 27.8% vs overall 32.2% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 35.6% vs overall 27.9% |
| 10 | HIGH_SCORING_MATCHES | 9 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=362, fgte=362 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 390, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 90, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 7.1, "overall_goalless_pct": 9.1, "deviation_pp": 2.0}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 11.1, "overall_goalless_pct": 9.1, "deviation_pp": 2.0}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 44.9, "overall_share": 39.9}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.3, "overall_goalless_pct": 9.1, "deviation_pp": 5.8}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 27.8, "overall_share": 32.2}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 35.6, "overall_share": 27.9}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 9, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 4}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 74760, "distinct": 74750, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 74760, "fgt_inconsistent": 362, "fgte_inconsistent": 362, "n_with_fgt": 68940}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
