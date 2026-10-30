# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:06:25+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `primera1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 425 |
| teams | 1585 |
| team_aliases | 3171 |
| team_seasons | 7217 |
| matches | 109558 |
| standings | 21651 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `63`
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
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `primera1`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2021-2022 | False | complete | 380 | 20 | 2021-08-27 | 2022-05-29 |
| 2022-2023 | False | complete | 380 | 21 | 2022-08-27 | 2023-05-27 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-26 | 2024-05-25 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-24 | 2025-05-24 |
| 2025-2026 | True | complete | 398 | 21 | 2025-08-29 | 2026-05-23 |
| 2026-2027 | True | in_progress | 90 | 20 | 2026-08-28 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 109558 | 109558 | 0 |
| matches (league_season_id, game_index) | 109558 | 109558 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 109558 | 109544 | 14 |
| team_seasons (league_season_id, team_id) | 7217 | 7217 | 0 |
| team_seasons api_name within a season | 7217 | 7217 | 0 |
| team_seasons api_slug within a season | 7217 | 7217 | 0 |
| standings (league_season_id, team_id, view) | 21651 | 21651 | 0 |
| team_aliases (form, value) | 3171 | 3171 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1585 | 1585 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `109558`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 109558 | 0.0% |
| kickoff_time | 0 | 109558 | 0.0% |
| home_team_id | 0 | 109558 | 0.0% |
| away_team_id | 0 | 109558 | 0.0% |
| home_score | 0 | 109558 | 0.0% |
| away_score | 0 | 109558 | 0.0% |
| home_ht | 471 | 109087 | 0.4% |
| away_ht | 471 | 109087 | 0.4% |
| first_goal_time | 8687 | 100871 | 7.9% |
| first_goal_time_extra | 8687 | 100871 | 7.9% |
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
| Home | 900 | 44.8% |
| Draw | 566 | 28.2% |
| Away | 542 | 27.0% |
| Total | 2008 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4720 |
| Average goals per match | 2.351 |
| Home goals | 2689 (avg 1.339) |
| Away goals | 2031 (avg 1.011) |
| Home goal share | 57.0% |
| Goalless matches | 186 (9.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2021-2022 | 380 | 44.5% | 24.7% | 30.8% | 907 | 2.387 | 497 | 410 | 32 (8.4%) |
| 2022-2023 | 380 | 46.1% | 27.1% | 26.8% | 862 | 2.268 | 492 | 370 | 34 (8.9%) |
| 2023-2024 | 380 | 41.8% | 31.8% | 26.3% | 815 | 2.145 | 473 | 342 | 50 (13.2%) |
| 2024-2025 | 380 | 45.3% | 29.5% | 25.3% | 930 | 2.447 | 543 | 387 | 25 (6.6%) |
| 2025-2026 | 398 | 45.7% | 28.4% | 25.9% | 974 | 2.447 | 554 | 420 | 39 (9.8%) |
| 2026-2027 | 90 | 47.8% | 25.6% | 26.7% | 232 | 2.578 | 130 | 102 | 6 (6.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1806` of `2008` (89.9%)
| metric | value |
|---|---|
| First goals recorded | 1806 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.19 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 525 |
| 16-30 | 413 |
| 31-45 | 315 |
| 46-60 | 250 |
| 61-75 | 168 |
| 76-90 | 101 |
| 91-120 | 34 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `366`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 21 | 1..21 | 21 |
| 2022-2023 | goals | 21 | 1..21 | 21 |
| 2022-2023 | luck | 21 | 1..21 | 21 |
| 2023-2024 | classic | 20 | 1..20 | 20 |
| 2023-2024 | goals | 20 | 1..20 | 20 |
| 2023-2024 | luck | 20 | 1..20 | 20 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
| 2025-2026 | classic | 21 | 1..21 | 21 |
| 2025-2026 | goals | 21 | 1..21 | 21 |
| 2025-2026 | luck | 21 | 1..21 | 21 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 282 |
| 1-0 | 275 |
| 2-1 | 190 |
| 0-0 | 186 |
| 0-1 | 167 |
| 2-0 | 157 |
| 1-2 | 135 |
| 0-2 | 101 |
| 3-0 | 88 |
| 2-2 | 85 |
| 3-1 | 64 |
| 1-3 | 42 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 2-7 | 9 | 1 |
| 5-3 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1009 | 50.2% |
| Mon | 4 | 0.2% |
| Tue | 10 | 0.5% |
| Wed | 32 | 1.6% |
| Thu | 7 | 0.3% |
| Fri | 108 | 5.4% |
| Sat | 838 | 41.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 21 teams, expected 20 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 398 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 4 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 90 matches, expected 380 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 13.2% vs overall 9.3% (deviation 3.9 pp) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 6.6% vs overall 9.3% (deviation 2.7 pp) |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.7% vs overall 9.3% (deviation 2.6 pp) |
| 9 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=413, fgte=413 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=21 positions=1..21 teams=21 |
| 13 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=21 positions=1..21 teams=21 |
| 14 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=21 positions=1..21 teams=21 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 16 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 17 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 21, "expected": 20}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 398, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `4.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 90, "expected": 380}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 13.2, "overall_goalless_pct": 9.3, "deviation_pp": 3.9}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 6.6, "overall_goalless_pct": 9.3, "deviation_pp": 2.7}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.7, "overall_goalless_pct": 9.3, "deviation_pp": 2.6}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 109558, "distinct": 109544, "duplicates": 14}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 109558, "fgt_inconsistent": 413, "fgte_inconsistent": 413, "n_with_fgt": 100871}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
