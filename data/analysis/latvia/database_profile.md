# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:01:36+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `latvia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 355 |
| teams | 1290 |
| team_aliases | 2581 |
| team_seasons | 5941 |
| matches | 88916 |
| standings | 17823 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `52`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `latvia`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2021 | False | complete | 126 | 9 | 2021-03-13 | 2021-11-06 |
| 2022 | False | complete | 182 | 11 | 2022-03-11 | 2022-11-27 |
| 2023 | False | complete | 182 | 11 | 2023-03-11 | 2023-11-25 |
| 2024 | False | complete | 182 | 11 | 2024-03-08 | 2024-11-23 |
| 2025 | True | complete | 182 | 11 | 2025-03-05 | 2025-11-23 |
| 2026 | True | in_progress | 170 | 10 | 2026-03-06 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 88916 | 88916 | 0 |
| matches (league_season_id, game_index) | 88916 | 88916 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 88916 | 88902 | 14 |
| team_seasons (league_season_id, team_id) | 5941 | 5941 | 0 |
| team_seasons api_name within a season | 5941 | 5941 | 0 |
| team_seasons api_slug within a season | 5941 | 5941 | 0 |
| standings (league_season_id, team_id, view) | 17823 | 17823 | 0 |
| team_aliases (form, value) | 2581 | 2581 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1290 | 1290 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `88916`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 88916 | 0.0% |
| kickoff_time | 0 | 88916 | 0.0% |
| home_team_id | 0 | 88916 | 0.0% |
| away_team_id | 0 | 88916 | 0.0% |
| home_score | 0 | 88916 | 0.0% |
| away_score | 0 | 88916 | 0.0% |
| home_ht | 442 | 88474 | 0.5% |
| away_ht | 442 | 88474 | 0.5% |
| first_goal_time | 7115 | 81801 | 8.0% |
| first_goal_time_extra | 7115 | 81801 | 8.0% |
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
| Home | 448 | 43.8% |
| Draw | 209 | 20.4% |
| Away | 367 | 35.8% |
| Total | 1024 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3040 |
| Average goals per match | 2.969 |
| Home goals | 1645 (avg 1.606) |
| Away goals | 1395 (avg 1.362) |
| Home goal share | 54.1% |
| Goalless matches | 60 (5.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | 126 | 46.8% | 15.9% | 37.3% | 375 | 2.976 | 200 | 175 | 4 (3.2%) |
| 2022 | 182 | 42.9% | 17.6% | 39.6% | 543 | 2.984 | 286 | 257 | 12 (6.6%) |
| 2023 | 182 | 43.4% | 23.6% | 33.0% | 533 | 2.929 | 275 | 258 | 12 (6.6%) |
| 2024 | 182 | 42.3% | 18.1% | 39.6% | 561 | 3.082 | 308 | 253 | 12 (6.6%) |
| 2025 | 182 | 45.6% | 23.6% | 30.8% | 535 | 2.94 | 302 | 233 | 11 (6.0%) |
| 2026 | 170 | 42.4% | 22.4% | 35.3% | 493 | 2.9 | 274 | 219 | 9 (5.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `947` of `1024` (92.5%)
| metric | value |
|---|---|
| First goals recorded | 947 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 29.37 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 333 |
| 16-30 | 241 |
| 31-45 | 152 |
| 46-60 | 107 |
| 61-75 | 61 |
| 76-90 | 47 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `189`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2021 | classic | 9 | 1..9 | 9 |
| 2021 | goals | 9 | 1..9 | 9 |
| 2021 | luck | 9 | 1..9 | 9 |
| 2022 | classic | 11 | 1..11 | 11 |
| 2022 | goals | 11 | 1..11 | 11 |
| 2022 | luck | 11 | 1..11 | 11 |
| 2023 | classic | 11 | 1..11 | 11 |
| 2023 | goals | 11 | 1..11 | 11 |
| 2023 | luck | 11 | 1..11 | 11 |
| 2024 | classic | 11 | 1..11 | 11 |
| 2024 | goals | 11 | 1..11 | 11 |
| 2024 | luck | 11 | 1..11 | 11 |
| 2025 | classic | 11 | 1..11 | 11 |
| 2025 | goals | 11 | 1..11 | 11 |
| 2025 | luck | 11 | 1..11 | 11 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 102 |
| 0-1 | 87 |
| 2-0 | 80 |
| 1-0 | 80 |
| 2-1 | 65 |
| 1-2 | 64 |
| 0-0 | 60 |
| 3-0 | 53 |
| 0-2 | 43 |
| 0-3 | 42 |
| 2-2 | 38 |
| 3-1 | 32 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 10-1 | 11 | 1 |
| 0-10 | 10 | 1 |
| 4-5 | 9 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 2 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 293 | 28.6% |
| Mon | 97 | 9.5% |
| Tue | 75 | 7.3% |
| Wed | 90 | 8.8% |
| Thu | 74 | 7.2% |
| Fri | 125 | 12.2% |
| Sat | 270 | 26.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2021 has 126 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2021 has 9 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2022 has 182 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2022 has 11 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2023 has 182 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2023 has 11 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2024 has 182 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2024 has 11 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2025 has 182 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2025 has 11 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2026 has 170 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 13 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 3.2% vs overall 5.9% (deviation 2.7 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2021 draw outcome share 15.9% vs overall 20.4% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2025 away outcome share 30.8% vs overall 35.8% |
| 17 | HIGH_SCORING_MATCHES | 11 match(es) with >= 8 total goals (extreme scorelines) |
| 18 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 19 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=385, fgte=385 rows) |
| 20 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=9 positions=1..9 teams=9 |
| 21 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=9 positions=1..9 teams=9 |
| 22 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=9 positions=1..9 teams=9 |
| 23 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=11 positions=1..11 teams=11 |
| 24 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=11 positions=1..11 teams=11 |
| 25 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=11 positions=1..11 teams=11 |
| 26 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=11 positions=1..11 teams=11 |
| 27 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=11 positions=1..11 teams=11 |
| 28 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=11 positions=1..11 teams=11 |
| 29 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=11 positions=1..11 teams=11 |
| 30 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=11 positions=1..11 teams=11 |
| 31 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=11 positions=1..11 teams=11 |
| 32 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=11 positions=1..11 teams=11 |
| 33 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=11 positions=1..11 teams=11 |
| 34 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=11 positions=1..11 teams=11 |
| 35 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 126, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 9, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 182, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 11, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 182, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 11, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 182, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 11, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 182, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 11, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 170, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `13.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 3.2, "overall_goalless_pct": 5.9, "deviation_pp": 2.7}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "draw", "season_share": 15.9, "overall_share": 20.4}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025", "outcome": "away", "season_share": 30.8, "overall_share": 35.8}`
- `17.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 11, "threshold": 8, "examples": [{"scoreline": "10-1", "total_goals": 11, "count": 1}, {"scoreline": "0-10", "total_goals": 10, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 2}, {"scoreline": "1-7", "total_goals": 8, "count": 2}]}`
- `18.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 88916, "distinct": 88902, "duplicates": 14}`
- `19.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 88916, "fgt_inconsistent": 385, "fgte_inconsistent": 385, "n_with_fgt": 81801}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
