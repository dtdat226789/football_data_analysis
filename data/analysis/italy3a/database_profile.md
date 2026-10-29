# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:05:35+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy3a`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 307 |
| teams | 1152 |
| team_aliases | 2304 |
| team_seasons | 5207 |
| matches | 77131 |
| standings | 15621 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `45`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy3a`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-26 | 2021-05-02 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-28 | 2022-04-24 |
| 2022-2023 | False | complete | 380 | 20 | 2022-09-03 | 2023-04-22 |
| 2023-2024 | False | complete | 380 | 20 | 2023-09-03 | 2024-04-28 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-23 | 2025-04-25 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-23 | 2026-04-25 |
| 2026-2027 | True | in_progress | 110 | 20 | 2026-08-21 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 77131 | 77131 | 0 |
| matches (league_season_id, game_index) | 77131 | 77131 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 77131 | 77121 | 10 |
| team_seasons (league_season_id, team_id) | 5207 | 5207 | 0 |
| team_seasons api_name within a season | 5207 | 5207 | 0 |
| team_seasons api_slug within a season | 5207 | 5207 | 0 |
| standings (league_season_id, team_id, view) | 15621 | 15621 | 0 |
| team_aliases (form, value) | 2304 | 2304 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1152 | 1152 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `77131`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 77131 | 0.0% |
| kickoff_time | 0 | 77131 | 0.0% |
| home_team_id | 0 | 77131 | 0.0% |
| away_team_id | 0 | 77131 | 0.0% |
| home_score | 0 | 77131 | 0.0% |
| away_score | 0 | 77131 | 0.0% |
| home_ht | 412 | 76719 | 0.5% |
| away_ht | 412 | 76719 | 0.5% |
| first_goal_time | 6059 | 71072 | 7.9% |
| first_goal_time_extra | 6059 | 71072 | 7.9% |
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
| Home | 935 | 39.1% |
| Draw | 710 | 29.7% |
| Away | 745 | 31.2% |
| Total | 2390 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5459 |
| Average goals per match | 2.284 |
| Home goals | 2942 (avg 1.231) |
| Away goals | 2517 (avg 1.053) |
| Home goal share | 53.9% |
| Goalless matches | 242 (10.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 39.5% | 30.0% | 30.5% | 866 | 2.279 | 473 | 393 | 43 (11.3%) |
| 2021-2022 | 380 | 38.2% | 31.6% | 30.3% | 833 | 2.192 | 447 | 386 | 38 (10.0%) |
| 2022-2023 | 380 | 39.5% | 28.4% | 32.1% | 884 | 2.326 | 474 | 410 | 34 (8.9%) |
| 2023-2024 | 380 | 37.1% | 29.5% | 33.4% | 847 | 2.229 | 445 | 402 | 42 (11.1%) |
| 2024-2025 | 380 | 43.7% | 26.8% | 29.5% | 873 | 2.297 | 490 | 383 | 32 (8.4%) |
| 2025-2026 | 380 | 37.9% | 30.3% | 31.8% | 889 | 2.339 | 474 | 415 | 37 (9.7%) |
| 2026-2027 | 110 | 35.5% | 35.5% | 29.1% | 267 | 2.427 | 139 | 128 | 16 (14.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2148` of `2390` (89.9%)
| metric | value |
|---|---|
| First goals recorded | 2148 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 33.34 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 641 |
| 16-30 | 509 |
| 31-45 | 367 |
| 46-60 | 285 |
| 61-75 | 189 |
| 76-90 | 118 |
| 91-120 | 39 |

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
| 1-1 | 342 |
| 1-0 | 291 |
| 0-1 | 242 |
| 0-0 | 242 |
| 2-1 | 211 |
| 1-2 | 183 |
| 2-0 | 162 |
| 0-2 | 138 |
| 2-2 | 111 |
| 3-1 | 82 |
| 3-0 | 67 |
| 0-3 | 51 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1048 | 43.8% |
| Mon | 119 | 5.0% |
| Tue | 86 | 3.6% |
| Wed | 220 | 9.2% |
| Thu | 54 | 2.3% |
| Fri | 136 | 5.7% |
| Sat | 727 | 30.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 110 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 8.4% vs overall 10.1% (deviation 1.7 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 43.7% vs overall 39.1% |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 14.5% vs overall 10.1% (deviation 4.4 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 35.5% vs overall 29.7% |
| 7 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=362, fgte=362 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 110, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 8.4, "overall_goalless_pct": 10.1, "deviation_pp": 1.7}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 43.7, "overall_share": 39.1}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 14.5, "overall_goalless_pct": 10.1, "deviation_pp": 4.4}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 35.5, "overall_share": 29.7}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 77131, "distinct": 77121, "duplicates": 10}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 77131, "fgt_inconsistent": 362, "fgte_inconsistent": 362, "n_with_fgt": 71072}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
