# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:03:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `premier`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 129 |
| teams | 1268 |
| team_aliases | 2536 |
| team_seasons | 2318 |
| matches | 24868 |
| standings | 6672 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `59`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 679 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 337 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 333 |
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 40 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 644 |
| eng2 | League Two | England | 2 | 651 |
| estonia | Meistriliiga | Estonia | 2 | 325 |
| finland1 | Veikkausliiga | Finland | 2 | 273 |
| finland2 | Ykkosliiga | Finland | 2 | 260 |
| france1 | Ligue 1 | France | 2 | 355 |
| france2 | Ligue 2 | France | 2 | 373 |
| france3 | Ligue 3 | France | 2 | 388 |
| germany-north | Regionalliga North | Germany | 2 | 415 |
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 450 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 297 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 474 |
| holland3 | Tweede Divisie | Netherlands | 2 | 385 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 339 |
| ireland2 | Division 1 | Ireland | 2 | 344 |
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |
| italy3a | Serie C - Group A | Italy | 2 | 450 |
| italy3b | Serie C - Group B | Italy | 2 | 426 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |
| korea1 | K League 1 | South Korea | 2 | 378 |
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |
| lithuania | TOPLYGA | Lithuania | 2 | 324 |
| morocco | Botola Pro | Morocco | 3 | 488 |
| national | National League | England | 2 | 677 |
| north | National League North | England | 2 | 680 |
| norway | Eliteserien | Norway | 2 | 408 |
| poland2 | Division 1 | Poland | 2 | 408 |
| portugal1 | Liga Portugal | Portugal | 2 | 370 |
| portugal2 | Liga Portugal 2 | Portugal | 2 | 363 |
| premier | Premier League | England | 7 | 2330 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `premier`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-12 | 2021-05-23 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-13 | 2022-05-22 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-05 | 2023-05-28 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-11 | 2024-05-19 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-16 | 2025-05-25 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-15 | 2026-05-24 |
| 2026-2027 | True | in_progress | 50 | 20 | 2026-08-21 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 24868 | 24868 | 0 |
| matches (league_season_id, game_index) | 24868 | 24868 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 24868 | 24854 | 14 |
| team_seasons (league_season_id, team_id) | 2318 | 2318 | 0 |
| team_seasons api_name within a season | 2318 | 2318 | 0 |
| team_seasons api_slug within a season | 2318 | 2318 | 0 |
| standings (league_season_id, team_id, view) | 6672 | 6672 | 0 |
| team_aliases (form, value) | 2536 | 2536 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1268 | 1268 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `24868`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 24868 | 0.0% |
| kickoff_time | 0 | 24868 | 0.0% |
| home_team_id | 0 | 24868 | 0.0% |
| away_team_id | 0 | 24868 | 0.0% |
| home_score | 0 | 24868 | 0.0% |
| away_score | 0 | 24868 | 0.0% |
| home_ht | 47 | 24821 | 0.2% |
| away_ht | 47 | 24821 | 0.2% |
| first_goal_time | 1713 | 23155 | 6.9% |
| first_goal_time_extra | 1713 | 23155 | 6.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 6 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 1001 | 43.0% |
| Draw | 553 | 23.7% |
| Away | 776 | 33.3% |
| Total | 2330 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6726 |
| Average goals per match | 2.887 |
| Home goals | 3625 (avg 1.556) |
| Away goals | 3101 (avg 1.331) |
| Home goal share | 53.9% |
| Goalless matches | 134 (5.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.9% | 21.8% | 40.3% | 1024 | 2.695 | 514 | 510 | 30 (7.9%) |
| 2021-2022 | 380 | 42.9% | 23.2% | 33.9% | 1071 | 2.818 | 575 | 496 | 22 (5.8%) |
| 2022-2023 | 380 | 48.4% | 22.9% | 28.7% | 1084 | 2.853 | 621 | 463 | 23 (6.1%) |
| 2023-2024 | 380 | 46.1% | 21.6% | 32.4% | 1246 | 3.279 | 684 | 562 | 11 (2.9%) |
| 2024-2025 | 380 | 40.8% | 24.5% | 34.7% | 1115 | 2.934 | 575 | 540 | 16 (4.2%) |
| 2025-2026 | 380 | 42.6% | 27.4% | 30.0% | 1045 | 2.75 | 580 | 465 | 27 (7.1%) |
| 2026-2027 | 50 | 36.0% | 32.0% | 32.0% | 141 | 2.82 | 76 | 65 | 5 (10.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2196` of `2330` (94.2%)
| metric | value |
|---|---|
| First goals recorded | 2196 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.93 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 45.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 753 |
| 16-30 | 542 |
| 31-45 | 352 |
| 46-60 | 294 |
| 61-75 | 146 |
| 76-90 | 88 |
| 91-120 | 21 |

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
| 1-1 | 255 |
| 1-0 | 192 |
| 2-1 | 191 |
| 0-1 | 173 |
| 1-2 | 160 |
| 2-0 | 156 |
| 2-2 | 137 |
| 0-0 | 134 |
| 0-2 | 129 |
| 3-1 | 111 |
| 3-0 | 107 |
| 1-3 | 71 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-0 | 9 | 2 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 2 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 4 |
| 2-6 | 8 | 1 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 680 | 29.2% |
| Mon | 139 | 6.0% |
| Tue | 126 | 5.4% |
| Wed | 176 | 7.6% |
| Thu | 77 | 3.3% |
| Fri | 73 | 3.1% |
| Sat | 1059 | 45.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 50 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 7.9% vs overall 5.8% (deviation 2.1 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.9% vs overall 43.0% |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 40.3% vs overall 33.3% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 48.4% vs overall 43.0% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 28.7% vs overall 33.3% |
| 8 | SEASON_AVG_GOALS_OUTLIER | Season 2023-2024 avg goals 3.279 vs overall 2.887 (deviation 0.392) |
| 9 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 2.9% vs overall 5.8% (deviation 2.9 pp) |
| 10 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 4.2% vs overall 5.8% (deviation 1.6 pp) |
| 11 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.0% vs overall 5.8% (deviation 4.2 pp) |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 36.0% vs overall 43.0% |
| 13 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 32.0% vs overall 23.7% |
| 14 | HIGH_SCORING_MATCHES | 18 match(es) with >= 8 total goals (extreme scorelines) |
| 15 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 16 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 50, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 7.9, "overall_goalless_pct": 5.8, "deviation_pp": 2.1}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.9, "overall_share": 43.0}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 40.3, "overall_share": 33.3}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 48.4, "overall_share": 43.0}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 28.7, "overall_share": 33.3}`
- `8.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023-2024", "season_avg_goals": 3.279, "overall_avg_goals": 2.887, "deviation": 0.392}`
- `9.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 2.9, "overall_goalless_pct": 5.8, "deviation_pp": 2.9}`
- `10.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 4.2, "overall_goalless_pct": 5.8, "deviation_pp": 1.6}`
- `11.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.0, "overall_goalless_pct": 5.8, "deviation_pp": 4.2}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 36.0, "overall_share": 43.0}`
- `13.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 32.0, "overall_share": 23.7}`
- `14.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 18, "threshold": 8, "examples": [{"scoreline": "9-0", "total_goals": 9, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 4}]}`
- `15.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 24868, "distinct": 24854, "duplicates": 14}`
- `16.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 24868, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 23155}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
