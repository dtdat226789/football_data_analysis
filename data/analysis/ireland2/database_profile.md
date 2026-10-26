# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:37:00+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `ireland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 279 |
| teams | 1009 |
| team_aliases | 2018 |
| team_seasons | 4657 |
| matches | 67913 |
| standings | 13971 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `41`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `ireland2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 88 | 10 | 2020-02-21 | 2020-10-27 |
| 2021 | False | complete | 135 | 10 | 2021-03-26 | 2021-10-29 |
| 2022 | False | complete | 144 | 9 | 2022-02-18 | 2022-10-21 |
| 2023 | False | complete | 180 | 10 | 2023-02-17 | 2023-10-20 |
| 2024 | False | complete | 180 | 10 | 2024-02-16 | 2024-10-18 |
| 2025 | True | complete | 179 | 10 | 2025-02-14 | 2025-10-17 |
| 2026 | True | in_progress | 180 | 10 | 2026-02-13 | 2026-10-16 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 67913 | 67913 | 0 |
| matches (league_season_id, game_index) | 67913 | 67913 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 67913 | 67903 | 10 |
| team_seasons (league_season_id, team_id) | 4657 | 4657 | 0 |
| team_seasons api_name within a season | 4657 | 4657 | 0 |
| team_seasons api_slug within a season | 4657 | 4657 | 0 |
| standings (league_season_id, team_id, view) | 13971 | 13971 | 0 |
| team_aliases (form, value) | 2018 | 2018 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1009 | 1009 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `67913`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 67913 | 0.0% |
| kickoff_time | 0 | 67913 | 0.0% |
| home_team_id | 0 | 67913 | 0.0% |
| away_team_id | 0 | 67913 | 0.0% |
| home_score | 0 | 67913 | 0.0% |
| away_score | 0 | 67913 | 0.0% |
| home_ht | 403 | 67510 | 0.6% |
| away_ht | 403 | 67510 | 0.6% |
| first_goal_time | 5328 | 62585 | 7.8% |
| first_goal_time_extra | 5328 | 62585 | 7.8% |
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
| Home | 456 | 42.0% |
| Draw | 263 | 24.2% |
| Away | 367 | 33.8% |
| Total | 1086 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3082 |
| Average goals per match | 2.838 |
| Home goals | 1640 (avg 1.51) |
| Away goals | 1442 (avg 1.328) |
| Home goal share | 53.2% |
| Goalless matches | 68 (6.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 88 | 35.2% | 17.0% | 47.7% | 258 | 2.932 | 116 | 142 | 6 (6.8%) |
| 2021 | 135 | 42.2% | 23.7% | 34.1% | 364 | 2.696 | 194 | 170 | 13 (9.6%) |
| 2022 | 144 | 36.8% | 24.3% | 38.9% | 431 | 2.993 | 204 | 227 | 12 (8.3%) |
| 2023 | 180 | 40.0% | 23.9% | 36.1% | 550 | 3.056 | 291 | 259 | 9 (5.0%) |
| 2024 | 180 | 40.6% | 30.0% | 29.4% | 473 | 2.628 | 264 | 209 | 9 (5.0%) |
| 2025 | 179 | 45.3% | 23.5% | 31.3% | 502 | 2.804 | 279 | 223 | 10 (5.6%) |
| 2026 | 180 | 49.4% | 23.3% | 27.2% | 504 | 2.8 | 292 | 212 | 9 (5.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1016` of `1086` (93.6%)
| metric | value |
|---|---|
| First goals recorded | 1016 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 30.08 |
| Median (p50) | 24.0 |
| p25 | 10.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 352 |
| 16-30 | 246 |
| 31-45 | 160 |
| 46-60 | 129 |
| 61-75 | 79 |
| 76-90 | 40 |
| 91-120 | 10 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `207`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 10 | 1..10 | 10 |
| 2020 | goals | 10 | 1..10 | 10 |
| 2020 | luck | 10 | 1..10 | 10 |
| 2021 | classic | 10 | 1..10 | 10 |
| 2021 | goals | 10 | 1..10 | 10 |
| 2021 | luck | 10 | 1..10 | 10 |
| 2022 | classic | 9 | 1..9 | 9 |
| 2022 | goals | 9 | 1..9 | 9 |
| 2022 | luck | 9 | 1..9 | 9 |
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
| 1-1 | 110 |
| 1-0 | 96 |
| 2-1 | 95 |
| 0-1 | 90 |
| 2-0 | 80 |
| 1-2 | 77 |
| 2-2 | 70 |
| 0-0 | 68 |
| 0-2 | 50 |
| 3-1 | 44 |
| 3-0 | 34 |
| 0-3 | 33 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-1 | 10 | 1 |
| 5-4 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 4-4 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 6 | 0.6% |
| Mon | 110 | 10.1% |
| Tue | 13 | 1.2% |
| Thu | 10 | 0.9% |
| Fri | 847 | 78.0% |
| Sat | 100 | 9.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 88 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 135 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 144 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 9 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 179 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 180 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020 home outcome share 35.2% vs overall 42.0% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 draw outcome share 17.0% vs overall 24.2% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 47.7% vs overall 33.8% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 9.6% vs overall 6.3% (deviation 3.3 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 8.3% vs overall 6.3% (deviation 2.0 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2022 home outcome share 36.8% vs overall 42.0% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2022 away outcome share 38.9% vs overall 33.8% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2024 draw outcome share 30.0% vs overall 24.2% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2024 away outcome share 29.4% vs overall 33.8% |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2026 home outcome share 49.4% vs overall 42.0% |
| 26 | OUTCOME_SHARE_OUTLIER | Season 2026 away outcome share 27.2% vs overall 33.8% |
| 27 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 28 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 29 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=348, fgte=348 rows) |
| 30 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=10 positions=1..10 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=10 positions=1..10 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=9 positions=1..9 teams=9 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=9 positions=1..9 teams=9 |
| 38 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=9 positions=1..9 teams=9 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=10 positions=1..10 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=10 positions=1..10 teams=10 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 47 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 50 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 88, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 135, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 144, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 9, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 179, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 180, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "home", "season_share": 35.2, "overall_share": 42.0}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "draw", "season_share": 17.0, "overall_share": 24.2}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 47.7, "overall_share": 33.8}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 9.6, "overall_goalless_pct": 6.3, "deviation_pp": 3.3}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 8.3, "overall_goalless_pct": 6.3, "deviation_pp": 2.0}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "home", "season_share": 36.8, "overall_share": 42.0}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "away", "season_share": 38.9, "overall_share": 33.8}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "draw", "season_share": 30.0, "overall_share": 24.2}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "away", "season_share": 29.4, "overall_share": 33.8}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "home", "season_share": 49.4, "overall_share": 42.0}`
- `26.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "away", "season_share": 27.2, "overall_share": 33.8}`
- `27.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "9-1", "total_goals": 10, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `28.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 67913, "distinct": 67903, "duplicates": 10}`
- `29.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 67913, "fgt_inconsistent": 348, "fgte_inconsistent": 348, "n_with_fgt": 62585}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 9, "min_pos": 1, "max_pos": 9, "distinct_teams": 9}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `50.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
