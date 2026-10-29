# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:11:14+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `primera2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 431 |
| teams | 1618 |
| team_aliases | 3237 |
| team_seasons | 7337 |
| matches | 111522 |
| standings | 22011 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `64`
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
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2894 |
| north | National League North | England | 7 | 3004 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1966 |
| portugal1 | Liga Portugal | Portugal | 2 | 389 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1912 |
| premier | Premier League | England | 7 | 2360 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1990 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `primera2`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2021-2022 | False | complete | 380 | 20 | 2021-08-27 | 2022-05-28 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-27 | 2023-05-27 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-26 | 2024-05-25 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-24 | 2025-05-24 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-29 | 2026-05-24 |
| 2026-2027 | True | in_progress | 90 | 20 | 2026-08-29 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 111522 | 111522 | 0 |
| matches (league_season_id, game_index) | 111522 | 111522 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 111522 | 111508 | 14 |
| team_seasons (league_season_id, team_id) | 7337 | 7337 | 0 |
| team_seasons api_name within a season | 7337 | 7337 | 0 |
| team_seasons api_slug within a season | 7337 | 7337 | 0 |
| standings (league_season_id, team_id, view) | 22011 | 22011 | 0 |
| team_aliases (form, value) | 3237 | 3237 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1618 | 1618 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `111522`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 111522 | 0.0% |
| kickoff_time | 0 | 111522 | 0.0% |
| home_team_id | 0 | 111522 | 0.0% |
| away_team_id | 0 | 111522 | 0.0% |
| home_score | 0 | 111522 | 0.0% |
| away_score | 0 | 111522 | 0.0% |
| home_ht | 471 | 111051 | 0.4% |
| away_ht | 471 | 111051 | 0.4% |
| first_goal_time | 8912 | 102610 | 8.0% |
| first_goal_time_extra | 8912 | 102610 | 8.0% |
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
| Home | 885 | 44.5% |
| Draw | 595 | 29.9% |
| Away | 510 | 25.6% |
| Total | 1990 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4589 |
| Average goals per match | 2.306 |
| Home goals | 2666 (avg 1.34) |
| Away goals | 1923 (avg 0.966) |
| Home goal share | 58.1% |
| Goalless matches | 228 (11.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2021-2022 | 380 | 48.4% | 25.3% | 26.3% | 916 | 2.411 | 547 | 369 | 37 (9.7%) |
| 2022-2023 | 380 | 40.8% | 33.9% | 25.3% | 809 | 2.129 | 462 | 347 | 53 (13.9%) |
| 2023-2024 | 380 | 46.1% | 25.5% | 28.4% | 862 | 2.268 | 503 | 359 | 43 (11.3%) |
| 2024-2025 | 380 | 40.8% | 34.7% | 24.5% | 903 | 2.376 | 508 | 395 | 43 (11.3%) |
| 2025-2026 | 380 | 45.5% | 29.7% | 24.7% | 856 | 2.253 | 500 | 356 | 46 (12.1%) |
| 2026-2027 | 90 | 47.8% | 31.1% | 21.1% | 243 | 2.7 | 146 | 97 | 6 (6.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1762` of `1990` (88.5%)
| metric | value |
|---|---|
| First goals recorded | 1762 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 33.83 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 523 |
| 16-30 | 398 |
| 31-45 | 303 |
| 46-60 | 257 |
| 61-75 | 153 |
| 76-90 | 92 |
| 91-120 | 36 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `360`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
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
| 1-0 | 277 |
| 1-1 | 260 |
| 0-0 | 228 |
| 0-1 | 175 |
| 2-1 | 162 |
| 2-0 | 158 |
| 1-2 | 116 |
| 2-2 | 90 |
| 3-0 | 83 |
| 0-2 | 75 |
| 3-1 | 65 |
| 1-3 | 46 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1050 | 52.8% |
| Mon | 7 | 0.4% |
| Tue | 9 | 0.5% |
| Wed | 48 | 2.4% |
| Thu | 9 | 0.5% |
| Fri | 124 | 6.2% |
| Sat | 743 | 37.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 90 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 9.7% vs overall 11.5% (deviation 1.8 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 25.3% vs overall 29.9% |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 13.9% vs overall 11.5% (deviation 2.4 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 draw outcome share 25.5% vs overall 29.9% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 34.7% vs overall 29.9% |
| 8 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.7 vs overall 2.306 (deviation 0.394) |
| 9 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.7% vs overall 11.5% (deviation 4.8 pp) |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 21.1% vs overall 25.6% |
| 11 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 12 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 13 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=413, fgte=413 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 90, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 9.7, "overall_goalless_pct": 11.5, "deviation_pp": 1.8}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 25.3, "overall_share": 29.9}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 13.9, "overall_goalless_pct": 11.5, "deviation_pp": 2.4}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "draw", "season_share": 25.5, "overall_share": 29.9}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 34.7, "overall_share": 29.9}`
- `8.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.7, "overall_avg_goals": 2.306, "deviation": 0.394}`
- `9.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.7, "overall_goalless_pct": 11.5, "deviation_pp": 4.8}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 21.1, "overall_share": 25.6}`
- `11.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `12.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 111522, "distinct": 111508, "duplicates": 14}`
- `13.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 111522, "fgt_inconsistent": 413, "fgte_inconsistent": 413, "n_with_fgt": 102610}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
