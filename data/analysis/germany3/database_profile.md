# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:33:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 209 |
| teams | 790 |
| team_aliases | 1580 |
| team_seasons | 3561 |
| matches | 52598 |
| standings | 10683 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `31`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany3`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-18 | 2021-05-22 |
| 2021-2022 | False | complete | 373 | 20 | 2021-07-24 | 2022-05-14 |
| 2022-2023 | False | complete | 380 | 20 | 2022-07-22 | 2023-05-27 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-04 | 2024-05-18 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-02 | 2025-05-17 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-01 | 2026-05-16 |
| 2026-2027 | True | in_progress | 107 | 20 | 2026-08-07 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 52598 | 52598 | 0 |
| matches (league_season_id, game_index) | 52598 | 52598 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 52598 | 52588 | 10 |
| team_seasons (league_season_id, team_id) | 3561 | 3561 | 0 |
| team_seasons api_name within a season | 3561 | 3561 | 0 |
| team_seasons api_slug within a season | 3561 | 3561 | 0 |
| standings (league_season_id, team_id, view) | 10683 | 10683 | 0 |
| team_aliases (form, value) | 1580 | 1580 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 790 | 790 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `52598`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 52598 | 0.0% |
| kickoff_time | 0 | 52598 | 0.0% |
| home_team_id | 0 | 52598 | 0.0% |
| away_team_id | 0 | 52598 | 0.0% |
| home_score | 0 | 52598 | 0.0% |
| away_score | 0 | 52598 | 0.0% |
| home_ht | 383 | 52215 | 0.7% |
| away_ht | 383 | 52215 | 0.7% |
| first_goal_time | 4282 | 48316 | 8.1% |
| first_goal_time_extra | 4282 | 48316 | 8.1% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 10 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 1029 | 43.2% |
| Draw | 603 | 25.3% |
| Away | 748 | 31.4% |
| Total | 2380 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6894 |
| Average goals per match | 2.897 |
| Home goals | 3724 (avg 1.565) |
| Away goals | 3170 (avg 1.332) |
| Home goal share | 54.0% |
| Goalless matches | 142 (6.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.6% | 28.4% | 33.9% | 1015 | 2.671 | 519 | 496 | 25 (6.6%) |
| 2021-2022 | 373 | 40.8% | 25.7% | 33.5% | 1028 | 2.756 | 548 | 480 | 29 (7.8%) |
| 2022-2023 | 380 | 44.7% | 23.4% | 31.8% | 1108 | 2.916 | 607 | 501 | 16 (4.2%) |
| 2023-2024 | 380 | 45.5% | 26.3% | 28.2% | 1066 | 2.805 | 599 | 467 | 26 (6.8%) |
| 2024-2025 | 380 | 45.3% | 25.3% | 29.5% | 1103 | 2.903 | 597 | 506 | 19 (5.0%) |
| 2025-2026 | 380 | 46.1% | 23.4% | 30.5% | 1219 | 3.208 | 668 | 551 | 23 (6.1%) |
| 2026-2027 | 107 | 41.1% | 23.4% | 35.5% | 355 | 3.318 | 186 | 169 | 4 (3.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2237` of `2380` (94.0%)
| metric | value |
|---|---|
| First goals recorded | 2237 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 29.39 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 788 |
| 16-30 | 555 |
| 31-45 | 382 |
| 46-60 | 253 |
| 61-75 | 144 |
| 76-90 | 93 |
| 91-120 | 22 |

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
| 1-1 | 300 |
| 2-1 | 218 |
| 1-0 | 209 |
| 2-0 | 161 |
| 1-2 | 156 |
| 0-1 | 154 |
| 0-0 | 142 |
| 2-2 | 133 |
| 3-1 | 116 |
| 0-2 | 110 |
| 1-3 | 81 |
| 3-0 | 75 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 2 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 6 |
| 4-4 | 8 | 4 |
| 3-5 | 8 | 6 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 521 | 21.9% |
| Mon | 84 | 3.5% |
| Tue | 144 | 6.1% |
| Wed | 160 | 6.7% |
| Fri | 195 | 8.2% |
| Sat | 1276 | 53.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 373 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 107 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.6% vs overall 43.2% |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 7.8% vs overall 6.0% (deviation 1.8 pp) |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 4.2% vs overall 6.0% (deviation 1.8 pp) |
| 7 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.318 vs overall 2.897 (deviation 0.421) |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.7% vs overall 6.0% (deviation 2.3 pp) |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 35.5% vs overall 31.4% |
| 10 | HIGH_SCORING_MATCHES | 28 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=328, fgte=328 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 373, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 107, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.6, "overall_share": 43.2}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 7.8, "overall_goalless_pct": 6.0, "deviation_pp": 1.8}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 4.2, "overall_goalless_pct": 6.0, "deviation_pp": 1.8}`
- `7.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.318, "overall_avg_goals": 2.897, "deviation": 0.421}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.7, "overall_goalless_pct": 6.0, "deviation_pp": 2.3}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 35.5, "overall_share": 31.4}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 28, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 6}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 52598, "distinct": 52588, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 52598, "fgt_inconsistent": 328, "fgte_inconsistent": 328, "n_with_fgt": 48316}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
