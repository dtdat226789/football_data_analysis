# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:05:53+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `premier`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 419 |
| teams | 1526 |
| team_aliases | 3053 |
| team_seasons | 7095 |
| matches | 107550 |
| standings | 21285 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `62`
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
| north | National League North | England | 7 | 3004 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1966 |
| portugal1 | Liga Portugal | Portugal | 2 | 389 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1912 |
| premier | Premier League | England | 7 | 2360 |

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
| 2026-2027 | True | in_progress | 80 | 20 | 2026-08-21 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 107550 | 107550 | 0 |
| matches (league_season_id, game_index) | 107550 | 107550 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 107550 | 107536 | 14 |
| team_seasons (league_season_id, team_id) | 7095 | 7095 | 0 |
| team_seasons api_name within a season | 7095 | 7095 | 0 |
| team_seasons api_slug within a season | 7095 | 7095 | 0 |
| standings (league_season_id, team_id, view) | 21285 | 21285 | 0 |
| team_aliases (form, value) | 3053 | 3053 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1526 | 1526 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `107550`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 107550 | 0.0% |
| kickoff_time | 0 | 107550 | 0.0% |
| home_team_id | 0 | 107550 | 0.0% |
| away_team_id | 0 | 107550 | 0.0% |
| home_score | 0 | 107550 | 0.0% |
| away_score | 0 | 107550 | 0.0% |
| home_ht | 455 | 107095 | 0.4% |
| away_ht | 455 | 107095 | 0.4% |
| first_goal_time | 8485 | 99065 | 7.9% |
| first_goal_time_extra | 8485 | 99065 | 7.9% |
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
| Home | 1014 | 43.0% |
| Draw | 560 | 23.7% |
| Away | 786 | 33.3% |
| Total | 2360 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6807 |
| Average goals per match | 2.884 |
| Home goals | 3670 (avg 1.555) |
| Away goals | 3137 (avg 1.329) |
| Home goal share | 53.9% |
| Goalless matches | 135 (5.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.9% | 21.8% | 40.3% | 1024 | 2.695 | 514 | 510 | 30 (7.9%) |
| 2021-2022 | 380 | 42.9% | 23.2% | 33.9% | 1071 | 2.818 | 575 | 496 | 22 (5.8%) |
| 2022-2023 | 380 | 48.4% | 22.9% | 28.7% | 1084 | 2.853 | 621 | 463 | 23 (6.1%) |
| 2023-2024 | 380 | 46.1% | 21.6% | 32.4% | 1246 | 3.279 | 684 | 562 | 11 (2.9%) |
| 2024-2025 | 380 | 40.8% | 24.5% | 34.7% | 1115 | 2.934 | 575 | 540 | 16 (4.2%) |
| 2025-2026 | 380 | 42.6% | 27.4% | 30.0% | 1045 | 2.75 | 580 | 465 | 27 (7.1%) |
| 2026-2027 | 80 | 38.8% | 28.8% | 32.5% | 222 | 2.775 | 121 | 101 | 6 (7.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2225` of `2360` (94.3%)
| metric | value |
|---|---|
| First goals recorded | 2225 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.99 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 763 |
| 16-30 | 545 |
| 31-45 | 357 |
| 46-60 | 300 |
| 61-75 | 148 |
| 76-90 | 91 |
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
| 1-1 | 259 |
| 2-1 | 194 |
| 1-0 | 193 |
| 0-1 | 176 |
| 1-2 | 161 |
| 2-0 | 159 |
| 2-2 | 139 |
| 0-0 | 135 |
| 0-2 | 133 |
| 3-1 | 113 |
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
| Sun | 692 | 29.3% |
| Mon | 141 | 6.0% |
| Tue | 126 | 5.3% |
| Wed | 176 | 7.5% |
| Thu | 77 | 3.3% |
| Fri | 74 | 3.1% |
| Sat | 1074 | 45.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 80 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 7.9% vs overall 5.7% (deviation 2.2 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.9% vs overall 43.0% |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 40.3% vs overall 33.3% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 48.4% vs overall 43.0% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 28.7% vs overall 33.3% |
| 8 | SEASON_AVG_GOALS_OUTLIER | Season 2023-2024 avg goals 3.279 vs overall 2.884 (deviation 0.395) |
| 9 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 2.9% vs overall 5.7% (deviation 2.8 pp) |
| 10 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.5% vs overall 5.7% (deviation 1.8 pp) |
| 11 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 38.8% vs overall 43.0% |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 28.8% vs overall 23.7% |
| 13 | HIGH_SCORING_MATCHES | 18 match(es) with >= 8 total goals (extreme scorelines) |
| 14 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 15 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=397, fgte=397 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 80, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 7.9, "overall_goalless_pct": 5.7, "deviation_pp": 2.2}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.9, "overall_share": 43.0}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 40.3, "overall_share": 33.3}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 48.4, "overall_share": 43.0}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 28.7, "overall_share": 33.3}`
- `8.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023-2024", "season_avg_goals": 3.279, "overall_avg_goals": 2.884, "deviation": 0.395}`
- `9.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 2.9, "overall_goalless_pct": 5.7, "deviation_pp": 2.8}`
- `10.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.5, "overall_goalless_pct": 5.7, "deviation_pp": 1.8}`
- `11.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 38.8, "overall_share": 43.0}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 28.8, "overall_share": 23.7}`
- `13.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 18, "threshold": 8, "examples": [{"scoreline": "9-0", "total_goals": 9, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 4}]}`
- `14.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 107550, "distinct": 107536, "duplicates": 14}`
- `15.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 107550, "fgt_inconsistent": 397, "fgte_inconsistent": 397, "n_with_fgt": 99065}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
