# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:01:41+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `greece1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 216 |
| teams | 812 |
| team_aliases | 1624 |
| team_seasons | 3660 |
| matches | 53877 |
| standings | 10980 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `32`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `greece1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 182 | 14 | 2020-09-11 | 2021-03-14 |
| 2021-2022 | False | complete | 182 | 14 | 2021-09-11 | 2022-03-06 |
| 2022-2023 | False | complete | 182 | 14 | 2022-08-19 | 2023-03-12 |
| 2023-2024 | False | complete | 182 | 14 | 2023-08-18 | 2024-03-03 |
| 2024-2025 | False | complete | 182 | 14 | 2024-08-17 | 2025-03-09 |
| 2025-2026 | True | complete | 246 | 15 | 2025-08-23 | 2026-05-21 |
| 2026-2027 | True | in_progress | 55 | 14 | 2026-08-22 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 53877 | 53877 | 0 |
| matches (league_season_id, game_index) | 53877 | 53877 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 53877 | 53867 | 10 |
| team_seasons (league_season_id, team_id) | 3660 | 3660 | 0 |
| team_seasons api_name within a season | 3660 | 3660 | 0 |
| team_seasons api_slug within a season | 3660 | 3660 | 0 |
| standings (league_season_id, team_id, view) | 10980 | 10980 | 0 |
| team_aliases (form, value) | 1624 | 1624 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 812 | 812 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `53877`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 53877 | 0.0% |
| kickoff_time | 0 | 53877 | 0.0% |
| home_team_id | 0 | 53877 | 0.0% |
| away_team_id | 0 | 53877 | 0.0% |
| home_score | 0 | 53877 | 0.0% |
| away_score | 0 | 53877 | 0.0% |
| home_ht | 385 | 53492 | 0.7% |
| away_ht | 385 | 53492 | 0.7% |
| first_goal_time | 4396 | 49481 | 8.2% |
| first_goal_time_extra | 4396 | 49481 | 8.2% |
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
| Home | 518 | 42.8% |
| Draw | 312 | 25.8% |
| Away | 381 | 31.5% |
| Total | 1211 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3021 |
| Average goals per match | 2.495 |
| Home goals | 1670 (avg 1.379) |
| Away goals | 1351 (avg 1.116) |
| Home goal share | 55.3% |
| Goalless matches | 108 (8.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 182 | 40.1% | 26.4% | 33.5% | 411 | 2.258 | 219 | 192 | 17 (9.3%) |
| 2021-2022 | 182 | 45.6% | 22.5% | 31.9% | 439 | 2.412 | 243 | 196 | 21 (11.5%) |
| 2022-2023 | 182 | 42.3% | 29.1% | 28.6% | 414 | 2.275 | 227 | 187 | 22 (12.1%) |
| 2023-2024 | 182 | 45.6% | 26.9% | 27.5% | 545 | 2.995 | 309 | 236 | 8 (4.4%) |
| 2024-2025 | 182 | 40.1% | 23.1% | 36.8% | 436 | 2.396 | 230 | 206 | 14 (7.7%) |
| 2025-2026 | 246 | 41.5% | 27.6% | 30.9% | 624 | 2.537 | 346 | 278 | 22 (8.9%) |
| 2026-2027 | 55 | 49.1% | 20.0% | 30.9% | 152 | 2.764 | 96 | 56 | 4 (7.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1101` of `1211` (90.9%)
| metric | value |
|---|---|
| First goals recorded | 1101 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 31.74 |
| Median (p50) | 27.0 |
| p25 | 13.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 329 |
| 16-30 | 266 |
| 31-45 | 216 |
| 46-60 | 151 |
| 61-75 | 75 |
| 76-90 | 47 |
| 91-120 | 17 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `297`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 14 | 1..14 | 14 |
| 2020-2021 | goals | 14 | 1..14 | 14 |
| 2020-2021 | luck | 14 | 1..14 | 14 |
| 2021-2022 | classic | 14 | 1..14 | 14 |
| 2021-2022 | goals | 14 | 1..14 | 14 |
| 2021-2022 | luck | 14 | 1..14 | 14 |
| 2022-2023 | classic | 14 | 1..14 | 14 |
| 2022-2023 | goals | 14 | 1..14 | 14 |
| 2022-2023 | luck | 14 | 1..14 | 14 |
| 2023-2024 | classic | 14 | 1..14 | 14 |
| 2023-2024 | goals | 14 | 1..14 | 14 |
| 2023-2024 | luck | 14 | 1..14 | 14 |
| 2024-2025 | classic | 14 | 1..14 | 14 |
| 2024-2025 | goals | 14 | 1..14 | 14 |
| 2024-2025 | luck | 14 | 1..14 | 14 |
| 2025-2026 | classic | 15 | 1..15 | 15 |
| 2025-2026 | goals | 15 | 1..15 | 15 |
| 2025-2026 | luck | 15 | 1..15 | 15 |
| 2026-2027 | classic | 14 | 1..14 | 14 |
| 2026-2027 | goals | 14 | 1..14 | 14 |
| 2026-2027 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 138 |
| 1-0 | 121 |
| 0-0 | 108 |
| 2-1 | 105 |
| 0-1 | 100 |
| 2-0 | 98 |
| 1-2 | 83 |
| 0-2 | 76 |
| 3-0 | 69 |
| 2-2 | 57 |
| 0-3 | 32 |
| 3-1 | 31 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |
| 4-4 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 615 | 50.8% |
| Mon | 103 | 8.5% |
| Tue | 14 | 1.2% |
| Wed | 95 | 7.8% |
| Thu | 33 | 2.7% |
| Fri | 16 | 1.3% |
| Sat | 335 | 27.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 182 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 14 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 182 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 14 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 182 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 14 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 182 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 14 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 182 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 14 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 246 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 15 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 55 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 14 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 11.5% vs overall 8.9% (deviation 2.6 pp) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 12.1% vs overall 8.9% (deviation 3.2 pp) |
| 18 | SEASON_AVG_GOALS_OUTLIER | Season 2023-2024 avg goals 2.995 vs overall 2.495 (deviation 0.500) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 4.4% vs overall 8.9% (deviation 4.5 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 36.8% vs overall 31.5% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.3% vs overall 8.9% (deviation 1.6 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 49.1% vs overall 42.8% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 20.0% vs overall 25.8% |
| 24 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=330, fgte=330 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=14 positions=1..14 teams=14 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=14 positions=1..14 teams=14 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=14 positions=1..14 teams=14 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=14 positions=1..14 teams=14 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=14 positions=1..14 teams=14 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=14 positions=1..14 teams=14 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=14 positions=1..14 teams=14 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=14 positions=1..14 teams=14 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=14 positions=1..14 teams=14 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=14 positions=1..14 teams=14 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=14 positions=1..14 teams=14 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=14 positions=1..14 teams=14 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=14 positions=1..14 teams=14 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=14 positions=1..14 teams=14 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=14 positions=1..14 teams=14 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=15 positions=1..15 teams=15 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=15 positions=1..15 teams=15 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=15 positions=1..15 teams=15 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=14 positions=1..14 teams=14 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=14 positions=1..14 teams=14 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 182, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 14, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 182, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 14, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 182, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 14, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 182, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 14, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 182, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 14, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 246, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 15, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 55, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 14, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 11.5, "overall_goalless_pct": 8.9, "deviation_pp": 2.6}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 12.1, "overall_goalless_pct": 8.9, "deviation_pp": 3.2}`
- `18.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023-2024", "season_avg_goals": 2.995, "overall_avg_goals": 2.495, "deviation": 0.5}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 4.4, "overall_goalless_pct": 8.9, "deviation_pp": 4.5}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 36.8, "overall_share": 31.5}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.3, "overall_goalless_pct": 8.9, "deviation_pp": 1.6}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 49.1, "overall_share": 42.8}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 20.0, "overall_share": 25.8}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 53877, "distinct": 53867, "duplicates": 10}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 53877, "fgt_inconsistent": 330, "fgte_inconsistent": 330, "n_with_fgt": 49481}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
