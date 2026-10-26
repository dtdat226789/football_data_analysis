# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:36:44+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `ireland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 272 |
| teams | 1001 |
| team_aliases | 2002 |
| team_seasons | 4588 |
| matches | 66827 |
| standings | 13764 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `40`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `ireland1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 90 | 10 | 2020-02-14 | 2020-11-09 |
| 2021 | False | complete | 180 | 10 | 2021-03-19 | 2021-11-19 |
| 2022 | False | complete | 179 | 10 | 2022-02-18 | 2022-11-06 |
| 2023 | False | complete | 180 | 10 | 2023-02-17 | 2023-11-03 |
| 2024 | False | complete | 180 | 10 | 2024-02-16 | 2024-11-01 |
| 2025 | True | complete | 180 | 10 | 2025-02-14 | 2025-11-01 |
| 2026 | True | in_progress | 175 | 10 | 2026-02-06 | 2026-10-23 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 66827 | 66827 | 0 |
| matches (league_season_id, game_index) | 66827 | 66827 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 66827 | 66817 | 10 |
| team_seasons (league_season_id, team_id) | 4588 | 4588 | 0 |
| team_seasons api_name within a season | 4588 | 4588 | 0 |
| team_seasons api_slug within a season | 4588 | 4588 | 0 |
| standings (league_season_id, team_id, view) | 13764 | 13764 | 0 |
| team_aliases (form, value) | 2002 | 2002 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1001 | 1001 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `66827`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 66827 | 0.0% |
| kickoff_time | 0 | 66827 | 0.0% |
| home_team_id | 0 | 66827 | 0.0% |
| away_team_id | 0 | 66827 | 0.0% |
| home_score | 0 | 66827 | 0.0% |
| away_score | 0 | 66827 | 0.0% |
| home_ht | 401 | 66426 | 0.6% |
| away_ht | 401 | 66426 | 0.6% |
| first_goal_time | 5258 | 61569 | 7.9% |
| first_goal_time_extra | 5258 | 61569 | 7.9% |
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
| Home | 499 | 42.9% |
| Draw | 316 | 27.1% |
| Away | 349 | 30.0% |
| Total | 1164 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2904 |
| Average goals per match | 2.495 |
| Home goals | 1628 (avg 1.399) |
| Away goals | 1276 (avg 1.096) |
| Home goal share | 56.1% |
| Goalless matches | 95 (8.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 90 | 44.4% | 21.1% | 34.4% | 198 | 2.2 | 110 | 88 | 10 (11.1%) |
| 2021 | 180 | 42.2% | 24.4% | 33.3% | 458 | 2.544 | 250 | 208 | 4 (2.2%) |
| 2022 | 179 | 44.1% | 26.8% | 29.1% | 448 | 2.503 | 253 | 195 | 13 (7.3%) |
| 2023 | 180 | 45.0% | 25.0% | 30.0% | 469 | 2.606 | 270 | 199 | 15 (8.3%) |
| 2024 | 180 | 41.7% | 30.0% | 28.3% | 408 | 2.267 | 229 | 179 | 22 (12.2%) |
| 2025 | 180 | 42.8% | 28.9% | 28.3% | 437 | 2.428 | 248 | 189 | 15 (8.3%) |
| 2026 | 175 | 40.6% | 30.9% | 28.6% | 486 | 2.777 | 268 | 218 | 16 (9.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1068` of `1164` (91.8%)
| metric | value |
|---|---|
| First goals recorded | 1068 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 31.76 |
| Median (p50) | 26.0 |
| p25 | 13.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 322 |
| 16-30 | 271 |
| 31-45 | 190 |
| 46-60 | 149 |
| 61-75 | 63 |
| 76-90 | 57 |
| 91-120 | 16 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `210`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 10 | 1..10 | 10 |
| 2020 | goals | 10 | 1..10 | 10 |
| 2020 | luck | 10 | 1..10 | 10 |
| 2021 | classic | 10 | 1..10 | 10 |
| 2021 | goals | 10 | 1..10 | 10 |
| 2021 | luck | 10 | 1..10 | 10 |
| 2022 | classic | 10 | 1..10 | 10 |
| 2022 | goals | 10 | 1..10 | 10 |
| 2022 | luck | 10 | 1..10 | 10 |
| 2023 | classic | 10 | 1..10 | 10 |
| 2023 | goals | 10 | 1..10 | 10 |
| 2023 | luck | 10 | 1..10 | 10 |
| 2024 | classic | 10 | 1..10 | 10 |
| 2024 | goals | 10 | 1..10 | 10 |
| 2024 | luck | 10 | 1..10 | 10 |
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 153 |
| 1-0 | 129 |
| 2-1 | 109 |
| 0-1 | 104 |
| 0-0 | 95 |
| 1-2 | 87 |
| 2-0 | 78 |
| 0-2 | 65 |
| 2-2 | 61 |
| 3-0 | 49 |
| 3-1 | 44 |
| 3-2 | 25 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 7-1 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 68 | 5.8% |
| Mon | 189 | 16.2% |
| Tue | 15 | 1.3% |
| Wed | 4 | 0.3% |
| Thu | 19 | 1.6% |
| Fri | 741 | 63.7% |
| Sat | 128 | 11.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 90 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 179 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 175 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020 goalless share 11.1% vs overall 8.2% (deviation 2.9 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 draw outcome share 21.1% vs overall 27.1% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 34.4% vs overall 30.0% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 2.2% vs overall 8.2% (deviation 6.0 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2024 goalless share 12.2% vs overall 8.2% (deviation 4.0 pp) |
| 21 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=346, fgte=346 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=10 positions=1..10 teams=10 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=10 positions=1..10 teams=10 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=10 positions=1..10 teams=10 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=10 positions=1..10 teams=10 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=10 positions=1..10 teams=10 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 90, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 179, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 175, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020", "season_goalless_pct": 11.1, "overall_goalless_pct": 8.2, "deviation_pp": 2.9}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "draw", "season_share": 21.1, "overall_share": 27.1}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 34.4, "overall_share": 30.0}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 2.2, "overall_goalless_pct": 8.2, "deviation_pp": 6.0}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024", "season_goalless_pct": 12.2, "overall_goalless_pct": 8.2, "deviation_pp": 4.0}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 66827, "distinct": 66817, "duplicates": 10}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 66827, "fgt_inconsistent": 346, "fgte_inconsistent": 346, "n_with_fgt": 61569}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
