# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:52:31+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 195 |
| teams | 748 |
| team_aliases | 1496 |
| team_seasons | 3293 |
| matches | 48372 |
| standings | 9879 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `29`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 272 | 17 | 2020-09-18 | 2021-05-22 |
| 2021-2022 | False | complete | 272 | 17 | 2021-08-14 | 2022-05-14 |
| 2022-2023 | False | complete | 272 | 17 | 2022-08-05 | 2023-05-27 |
| 2023-2024 | False | complete | 272 | 17 | 2023-08-18 | 2024-05-18 |
| 2024-2025 | False | complete | 272 | 17 | 2024-08-24 | 2025-05-17 |
| 2025-2026 | True | complete | 274 | 18 | 2025-08-22 | 2026-05-25 |
| 2026-2027 | True | in_progress | 56 | 17 | 2026-08-28 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 48372 | 48372 | 0 |
| matches (league_season_id, game_index) | 48372 | 48372 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 48372 | 48362 | 10 |
| team_seasons (league_season_id, team_id) | 3293 | 3293 | 0 |
| team_seasons api_name within a season | 3293 | 3293 | 0 |
| team_seasons api_slug within a season | 3293 | 3293 | 0 |
| standings (league_season_id, team_id, view) | 9879 | 9879 | 0 |
| team_aliases (form, value) | 1496 | 1496 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 748 | 748 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `48372`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 48372 | 0.0% |
| kickoff_time | 0 | 48372 | 0.0% |
| home_team_id | 0 | 48372 | 0.0% |
| away_team_id | 0 | 48372 | 0.0% |
| home_score | 0 | 48372 | 0.0% |
| away_score | 0 | 48372 | 0.0% |
| home_ht | 382 | 47990 | 0.8% |
| away_ht | 382 | 47990 | 0.8% |
| first_goal_time | 4036 | 44336 | 8.3% |
| first_goal_time_extra | 4036 | 44336 | 8.3% |
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
| Home | 741 | 43.8% |
| Draw | 417 | 24.7% |
| Away | 532 | 31.5% |
| Total | 1690 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5309 |
| Average goals per match | 3.141 |
| Home goals | 2950 (avg 1.746) |
| Away goals | 2359 (avg 1.396) |
| Home goal share | 55.6% |
| Goalless matches | 88 (5.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 272 | 42.3% | 26.1% | 31.6% | 808 | 2.971 | 444 | 364 | 17 (6.2%) |
| 2021-2022 | 272 | 46.7% | 23.5% | 29.8% | 839 | 3.085 | 472 | 367 | 16 (5.9%) |
| 2022-2023 | 272 | 46.3% | 23.9% | 29.8% | 864 | 3.176 | 498 | 366 | 11 (4.0%) |
| 2023-2024 | 272 | 44.5% | 25.0% | 30.5% | 862 | 3.169 | 485 | 377 | 10 (3.7%) |
| 2024-2025 | 272 | 37.9% | 26.1% | 36.0% | 847 | 3.114 | 439 | 408 | 21 (7.7%) |
| 2025-2026 | 274 | 43.8% | 23.7% | 32.5% | 898 | 3.277 | 493 | 405 | 8 (2.9%) |
| 2026-2027 | 56 | 51.8% | 23.2% | 25.0% | 191 | 3.411 | 119 | 72 | 5 (8.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1601` of `1690` (94.7%)
| metric | value |
|---|---|
| First goals recorded | 1601 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 28.31 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 42.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 577 |
| 16-30 | 407 |
| 31-45 | 272 |
| 46-60 | 190 |
| 61-75 | 94 |
| 76-90 | 54 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `360`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 17 | 1..17 | 17 |
| 2020-2021 | goals | 17 | 1..17 | 17 |
| 2020-2021 | luck | 17 | 1..17 | 17 |
| 2021-2022 | classic | 17 | 1..17 | 17 |
| 2021-2022 | goals | 17 | 1..17 | 17 |
| 2021-2022 | luck | 17 | 1..17 | 17 |
| 2022-2023 | classic | 17 | 1..17 | 17 |
| 2022-2023 | goals | 17 | 1..17 | 17 |
| 2022-2023 | luck | 17 | 1..17 | 17 |
| 2023-2024 | classic | 17 | 1..17 | 17 |
| 2023-2024 | goals | 17 | 1..17 | 17 |
| 2023-2024 | luck | 17 | 1..17 | 17 |
| 2024-2025 | classic | 17 | 1..17 | 17 |
| 2024-2025 | goals | 17 | 1..17 | 17 |
| 2024-2025 | luck | 17 | 1..17 | 17 |
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 17 | 1..17 | 17 |
| 2026-2027 | goals | 17 | 1..17 | 17 |
| 2026-2027 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 199 |
| 2-1 | 144 |
| 2-0 | 107 |
| 1-0 | 102 |
| 2-2 | 102 |
| 1-2 | 101 |
| 0-1 | 96 |
| 0-0 | 88 |
| 3-1 | 87 |
| 0-2 | 77 |
| 3-0 | 65 |
| 1-3 | 64 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-1 | 9 | 2 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 412 | 24.4% |
| Mon | 8 | 0.5% |
| Tue | 32 | 1.9% |
| Wed | 46 | 2.7% |
| Thu | 3 | 0.2% |
| Fri | 157 | 9.3% |
| Sat | 1032 | 61.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 272 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 17 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 272 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 17 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 272 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 17 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 272 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 17 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 272 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 17 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 274 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 56 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 17 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 7.7% vs overall 5.2% (deviation 2.5 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 37.9% vs overall 43.8% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 36.0% vs overall 31.5% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 2.9% vs overall 5.2% (deviation 2.3 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 8.9% vs overall 5.2% (deviation 3.7 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 51.8% vs overall 43.8% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 25.0% vs overall 31.5% |
| 23 | HIGH_SCORING_MATCHES | 14 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=327, fgte=327 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=17 positions=1..17 teams=17 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=17 positions=1..17 teams=17 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=17 positions=1..17 teams=17 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=17 positions=1..17 teams=17 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=17 positions=1..17 teams=17 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=17 positions=1..17 teams=17 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=17 positions=1..17 teams=17 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=17 positions=1..17 teams=17 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=17 positions=1..17 teams=17 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=17 positions=1..17 teams=17 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=17 positions=1..17 teams=17 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=17 positions=1..17 teams=17 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=17 positions=1..17 teams=17 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=17 positions=1..17 teams=17 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=17 positions=1..17 teams=17 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=17 positions=1..17 teams=17 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=17 positions=1..17 teams=17 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 272, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 17, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 272, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 17, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 272, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 17, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 272, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 17, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 272, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 17, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 274, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 56, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 17, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 7.7, "overall_goalless_pct": 5.2, "deviation_pp": 2.5}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 37.9, "overall_share": 43.8}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 36.0, "overall_share": 31.5}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 2.9, "overall_goalless_pct": 5.2, "deviation_pp": 2.3}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 8.9, "overall_goalless_pct": 5.2, "deviation_pp": 3.7}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 51.8, "overall_share": 43.8}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 25.0, "overall_share": 31.5}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 14, "threshold": 8, "examples": [{"scoreline": "8-1", "total_goals": 9, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 48372, "distinct": 48362, "duplicates": 10}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 48372, "fgt_inconsistent": 327, "fgte_inconsistent": 327, "n_with_fgt": 44336}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
