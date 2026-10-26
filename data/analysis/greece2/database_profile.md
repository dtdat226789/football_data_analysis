# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:34:41+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `greece2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 223 |
| teams | 860 |
| team_aliases | 1720 |
| team_seasons | 3817 |
| matches | 55637 |
| standings | 11451 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `33`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `greece2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 132 | 12 | 2021-01-16 | 2021-04-21 |
| 2021-2022 | False | complete | 544 | 34 | 2021-11-06 | 2022-05-01 |
| 2022-2023 | False | complete | 387 | 30 | 2022-11-04 | 2023-06-20 |
| 2023-2024 | False | complete | 264 | 25 | 2023-09-23 | 2024-03-11 |
| 2024-2025 | False | complete | 180 | 20 | 2024-09-20 | 2025-02-02 |
| 2025-2026 | True | complete | 265 | 20 | 2025-09-13 | 2026-04-26 |
| 2026-2027 | True | in_progress | 60 | 16 | 2026-09-05 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 55637 | 55637 | 0 |
| matches (league_season_id, game_index) | 55637 | 55637 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 55637 | 55627 | 10 |
| team_seasons (league_season_id, team_id) | 3817 | 3817 | 0 |
| team_seasons api_name within a season | 3817 | 3817 | 0 |
| team_seasons api_slug within a season | 3817 | 3817 | 0 |
| standings (league_season_id, team_id, view) | 11451 | 11451 | 0 |
| team_aliases (form, value) | 1720 | 1720 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 860 | 860 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `55637`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 55637 | 0.0% |
| kickoff_time | 0 | 55637 | 0.0% |
| home_team_id | 0 | 55637 | 0.0% |
| away_team_id | 0 | 55637 | 0.0% |
| home_score | 0 | 55637 | 0.0% |
| away_score | 0 | 55637 | 0.0% |
| home_ht | 393 | 55244 | 0.7% |
| away_ht | 393 | 55244 | 0.7% |
| first_goal_time | 4604 | 51033 | 8.3% |
| first_goal_time_extra | 4604 | 51033 | 8.3% |
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
| Home | 820 | 44.8% |
| Draw | 480 | 26.2% |
| Away | 532 | 29.0% |
| Total | 1832 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4113 |
| Average goals per match | 2.245 |
| Home goals | 2390 (avg 1.305) |
| Away goals | 1723 (avg 0.941) |
| Home goal share | 58.1% |
| Goalless matches | 204 (11.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 132 | 40.2% | 29.5% | 30.3% | 252 | 1.909 | 137 | 115 | 17 (12.9%) |
| 2021-2022 | 544 | 46.9% | 27.4% | 25.7% | 1234 | 2.268 | 757 | 477 | 67 (12.3%) |
| 2022-2023 | 387 | 40.6% | 25.6% | 33.9% | 900 | 2.326 | 495 | 405 | 46 (11.9%) |
| 2023-2024 | 264 | 49.2% | 23.9% | 26.9% | 584 | 2.212 | 347 | 237 | 26 (9.8%) |
| 2024-2025 | 180 | 42.8% | 27.8% | 29.4% | 412 | 2.289 | 230 | 182 | 20 (11.1%) |
| 2025-2026 | 265 | 44.2% | 23.0% | 32.8% | 607 | 2.291 | 348 | 259 | 21 (7.9%) |
| 2026-2027 | 60 | 51.7% | 31.7% | 16.7% | 124 | 2.067 | 76 | 48 | 7 (11.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1620` of `1832` (88.4%)
| metric | value |
|---|---|
| First goals recorded | 1620 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 33.58 |
| Median (p50) | 28.0 |
| p25 | 14.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 468 |
| 16-30 | 393 |
| 31-45 | 259 |
| 46-60 | 229 |
| 61-75 | 161 |
| 76-90 | 82 |
| 91-120 | 28 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `471`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 12 | 1..12 | 12 |
| 2020-2021 | goals | 12 | 1..12 | 12 |
| 2020-2021 | luck | 12 | 1..12 | 12 |
| 2021-2022 | classic | 34 | 1..34 | 34 |
| 2021-2022 | goals | 34 | 1..34 | 34 |
| 2021-2022 | luck | 34 | 1..34 | 34 |
| 2022-2023 | classic | 30 | 1..30 | 30 |
| 2022-2023 | goals | 30 | 1..30 | 30 |
| 2022-2023 | luck | 30 | 1..30 | 30 |
| 2023-2024 | classic | 25 | 1..25 | 25 |
| 2023-2024 | goals | 25 | 1..25 | 25 |
| 2023-2024 | luck | 25 | 1..25 | 25 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 267 |
| 0-0 | 204 |
| 1-1 | 204 |
| 0-1 | 189 |
| 2-0 | 153 |
| 2-1 | 121 |
| 1-2 | 107 |
| 3-0 | 89 |
| 0-2 | 89 |
| 2-2 | 63 |
| 3-1 | 62 |
| 0-3 | 53 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 800 | 43.7% |
| Mon | 154 | 8.4% |
| Tue | 16 | 0.9% |
| Wed | 320 | 17.5% |
| Thu | 38 | 2.1% |
| Fri | 59 | 3.2% |
| Sat | 445 | 24.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 544 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 34 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 387 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 30 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 264 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 25 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 180 matches, expected 380 |
| 10 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 265 matches, expected 380 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 60 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 13 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 12.9% vs overall 11.1% (deviation 1.8 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 40.2% vs overall 44.8% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 40.6% vs overall 44.8% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 33.9% vs overall 29.0% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 49.2% vs overall 44.8% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 7.9% vs overall 11.1% (deviation 3.2 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 51.7% vs overall 44.8% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 31.7% vs overall 26.2% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 16.7% vs overall 29.0% |
| 23 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=338, fgte=338 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=12 positions=1..12 teams=12 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=34 positions=1..34 teams=34 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=34 positions=1..34 teams=34 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=34 positions=1..34 teams=34 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=30 positions=1..30 teams=30 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=30 positions=1..30 teams=30 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=30 positions=1..30 teams=30 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=25 positions=1..25 teams=25 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=25 positions=1..25 teams=25 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=25 positions=1..25 teams=25 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 544, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 34, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 387, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 30, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 264, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 25, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 180, "expected": 380}`
- `10.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 265, "expected": 380}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 60, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `13.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 12.9, "overall_goalless_pct": 11.1, "deviation_pp": 1.8}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 40.2, "overall_share": 44.8}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 40.6, "overall_share": 44.8}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 33.9, "overall_share": 29.0}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 49.2, "overall_share": 44.8}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 7.9, "overall_goalless_pct": 11.1, "deviation_pp": 3.2}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 51.7, "overall_share": 44.8}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 31.7, "overall_share": 26.2}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 16.7, "overall_share": 29.0}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 55637, "distinct": 55627, "duplicates": 10}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 55637, "fgt_inconsistent": 338, "fgte_inconsistent": 338, "n_with_fgt": 51033}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 34, "min_pos": 1, "max_pos": 34, "distinct_teams": 34}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 34, "min_pos": 1, "max_pos": 34, "distinct_teams": 34}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 34, "min_pos": 1, "max_pos": 34, "distinct_teams": 34}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 30, "min_pos": 1, "max_pos": 30, "distinct_teams": 30}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 30, "min_pos": 1, "max_pos": 30, "distinct_teams": 30}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 30, "min_pos": 1, "max_pos": 30, "distinct_teams": 30}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
