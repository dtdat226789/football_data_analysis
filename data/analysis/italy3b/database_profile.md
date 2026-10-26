# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:38:39+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy3b`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 314 |
| teams | 1180 |
| team_aliases | 2360 |
| team_seasons | 5347 |
| matches | 79380 |
| standings | 16041 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `46`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy3b`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-26 | 2021-05-02 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-28 | 2022-04-23 |
| 2022-2023 | False | complete | 380 | 20 | 2022-09-04 | 2023-04-23 |
| 2023-2024 | False | complete | 380 | 20 | 2023-09-01 | 2024-04-28 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-23 | 2025-04-27 |
| 2025-2026 | True | complete | 357 | 20 | 2025-08-22 | 2026-04-26 |
| 2026-2027 | True | in_progress | 107 | 20 | 2026-08-21 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 79380 | 79380 | 0 |
| matches (league_season_id, game_index) | 79380 | 79380 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 79380 | 79370 | 10 |
| team_seasons (league_season_id, team_id) | 5347 | 5347 | 0 |
| team_seasons api_name within a season | 5347 | 5347 | 0 |
| team_seasons api_slug within a season | 5347 | 5347 | 0 |
| standings (league_season_id, team_id, view) | 16041 | 16041 | 0 |
| team_aliases (form, value) | 2360 | 2360 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1180 | 1180 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `79380`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 79380 | 0.0% |
| kickoff_time | 0 | 79380 | 0.0% |
| home_team_id | 0 | 79380 | 0.0% |
| away_team_id | 0 | 79380 | 0.0% |
| home_score | 0 | 79380 | 0.0% |
| away_score | 0 | 79380 | 0.0% |
| home_ht | 416 | 78964 | 0.5% |
| away_ht | 416 | 78964 | 0.5% |
| first_goal_time | 6309 | 73071 | 7.9% |
| first_goal_time_extra | 6309 | 73071 | 7.9% |
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
| Home | 955 | 40.4% |
| Draw | 722 | 30.5% |
| Away | 687 | 29.1% |
| Total | 2364 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5596 |
| Average goals per match | 2.367 |
| Home goals | 3094 (avg 1.309) |
| Away goals | 2502 (avg 1.058) |
| Home goal share | 55.3% |
| Goalless matches | 253 (10.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 41.1% | 30.5% | 28.4% | 924 | 2.432 | 517 | 407 | 40 (10.5%) |
| 2021-2022 | 380 | 42.9% | 32.4% | 24.7% | 925 | 2.434 | 534 | 391 | 49 (12.9%) |
| 2022-2023 | 380 | 35.5% | 31.6% | 32.9% | 859 | 2.261 | 458 | 401 | 43 (11.3%) |
| 2023-2024 | 380 | 45.3% | 27.9% | 26.8% | 915 | 2.408 | 532 | 383 | 36 (9.5%) |
| 2024-2025 | 380 | 38.7% | 30.0% | 31.3% | 897 | 2.361 | 488 | 409 | 42 (11.1%) |
| 2025-2026 | 357 | 37.5% | 31.7% | 30.8% | 802 | 2.246 | 416 | 386 | 35 (9.8%) |
| 2026-2027 | 107 | 44.9% | 28.0% | 27.1% | 274 | 2.561 | 149 | 125 | 8 (7.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2108` of `2364` (89.2%)
| metric | value |
|---|---|
| First goals recorded | 2108 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 32.86 |
| Median (p50) | 28.0 |
| p25 | 12.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 636 |
| 16-30 | 510 |
| 31-45 | 349 |
| 46-60 | 289 |
| 61-75 | 184 |
| 76-90 | 102 |
| 91-120 | 38 |

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
| 1-1 | 341 |
| 1-0 | 258 |
| 0-0 | 253 |
| 0-1 | 217 |
| 2-1 | 197 |
| 2-0 | 170 |
| 1-2 | 166 |
| 2-2 | 112 |
| 0-2 | 106 |
| 3-0 | 87 |
| 3-1 | 80 |
| 1-3 | 59 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-3 | 9 | 1 |
| 5-4 | 9 | 1 |
| 4-5 | 9 | 1 |
| 8-0 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1052 | 44.5% |
| Mon | 127 | 5.4% |
| Tue | 115 | 4.9% |
| Wed | 206 | 8.7% |
| Thu | 61 | 2.6% |
| Fri | 126 | 5.3% |
| Sat | 677 | 28.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 357 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 107 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 12.9% vs overall 10.7% (deviation 2.2 pp) |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 24.7% vs overall 29.1% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 35.5% vs overall 40.4% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 45.3% vs overall 40.4% |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.5% vs overall 10.7% (deviation 3.2 pp) |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 44.9% vs overall 40.4% |
| 10 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=365, fgte=365 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 357, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 107, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 12.9, "overall_goalless_pct": 10.7, "deviation_pp": 2.2}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 24.7, "overall_share": 29.1}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 35.5, "overall_share": 40.4}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 45.3, "overall_share": 40.4}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.5, "overall_goalless_pct": 10.7, "deviation_pp": 3.2}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 44.9, "overall_share": 40.4}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 79380, "distinct": 79370, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 79380, "fgt_inconsistent": 365, "fgte_inconsistent": 365, "n_with_fgt": 73071}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
