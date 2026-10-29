# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T01:56:49+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech3b`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 103 |
| teams | 360 |
| team_aliases | 720 |
| team_seasons | 1674 |
| matches | 25125 |
| standings | 5022 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `15`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech3b`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 63 | 16 | 2020-08-22 | 2020-10-11 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-31 | 2022-06-18 |
| 2022-2023 | False | complete | 240 | 16 | 2022-08-06 | 2023-06-10 |
| 2023-2024 | False | complete | 240 | 16 | 2023-08-05 | 2024-06-08 |
| 2024-2025 | False | complete | 272 | 17 | 2024-08-10 | 2025-06-07 |
| 2025-2026 | True | complete | 272 | 17 | 2025-08-09 | 2026-06-07 |
| 2026-2027 | True | in_progress | 94 | 16 | 2026-08-07 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 25125 | 25125 | 0 |
| matches (league_season_id, game_index) | 25125 | 25125 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 25125 | 25121 | 4 |
| team_seasons (league_season_id, team_id) | 1674 | 1674 | 0 |
| team_seasons api_name within a season | 1674 | 1674 | 0 |
| team_seasons api_slug within a season | 1674 | 1674 | 0 |
| standings (league_season_id, team_id, view) | 5022 | 5022 | 0 |
| team_aliases (form, value) | 720 | 720 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 360 | 360 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `25125`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 25125 | 0.0% |
| kickoff_time | 0 | 25125 | 0.0% |
| home_team_id | 0 | 25125 | 0.0% |
| away_team_id | 0 | 25125 | 0.0% |
| home_score | 0 | 25125 | 0.0% |
| away_score | 0 | 25125 | 0.0% |
| home_ht | 340 | 24785 | 1.4% |
| away_ht | 340 | 24785 | 1.4% |
| first_goal_time | 2242 | 22883 | 8.9% |
| first_goal_time_extra | 2242 | 22883 | 8.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 666 | 46.9% |
| Draw | 313 | 22.0% |
| Away | 442 | 31.1% |
| Total | 1421 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4388 |
| Average goals per match | 3.088 |
| Home goals | 2487 (avg 1.75) |
| Away goals | 1901 (avg 1.338) |
| Home goal share | 56.7% |
| Goalless matches | 74 (5.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 63 | 68.3% | 0.0% | 31.7% | 213 | 3.381 | 131 | 82 | 0 (0.0%) |
| 2021-2022 | 240 | 48.3% | 20.8% | 30.8% | 732 | 3.05 | 422 | 310 | 12 (5.0%) |
| 2022-2023 | 240 | 44.2% | 24.2% | 31.7% | 713 | 2.971 | 395 | 318 | 15 (6.2%) |
| 2023-2024 | 240 | 49.2% | 23.3% | 27.5% | 720 | 3.0 | 410 | 310 | 14 (5.8%) |
| 2024-2025 | 272 | 46.0% | 24.3% | 29.8% | 796 | 2.926 | 465 | 331 | 19 (7.0%) |
| 2025-2026 | 272 | 44.1% | 22.1% | 33.8% | 912 | 3.353 | 495 | 417 | 7 (2.6%) |
| 2026-2027 | 94 | 40.4% | 24.5% | 35.1% | 302 | 3.213 | 169 | 133 | 7 (7.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1344` of `1421` (94.6%)
| metric | value |
|---|---|
| First goals recorded | 1344 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 27.45 |
| Median (p50) | 21.0 |
| p25 | 11.0 |
| p75 | 40.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 484 |
| 16-30 | 370 |
| 31-45 | 228 |
| 46-60 | 143 |
| 61-75 | 63 |
| 76-90 | 48 |
| 91-120 | 8 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `342`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 16 | 1..16 | 16 |
| 2021-2022 | goals | 16 | 1..16 | 16 |
| 2021-2022 | luck | 16 | 1..16 | 16 |
| 2022-2023 | classic | 16 | 1..17 | 16 |
| 2022-2023 | goals | 16 | 4..24 | 16 |
| 2022-2023 | luck | 16 | 1..32 | 16 |
| 2023-2024 | classic | 16 | 1..17 | 16 |
| 2023-2024 | goals | 16 | 6..26 | 16 |
| 2023-2024 | luck | 16 | 1..32 | 16 |
| 2024-2025 | classic | 17 | 1..18 | 17 |
| 2024-2025 | goals | 17 | 4..25 | 17 |
| 2024-2025 | luck | 17 | 1..34 | 17 |
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 135 |
| 1-0 | 112 |
| 2-1 | 111 |
| 2-0 | 110 |
| 0-1 | 90 |
| 1-2 | 87 |
| 0-0 | 74 |
| 2-2 | 74 |
| 3-0 | 71 |
| 3-1 | 65 |
| 0-2 | 61 |
| 2-3 | 46 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-9 | 11 | 1 |
| 7-3 | 10 | 1 |
| 6-4 | 10 | 1 |
| 8-1 | 9 | 1 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 1 |
| 3-6 | 9 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 593 | 41.7% |
| Mon | 5 | 0.4% |
| Tue | 10 | 0.7% |
| Wed | 97 | 6.8% |
| Thu | 7 | 0.5% |
| Fri | 64 | 4.5% |
| Sat | 645 | 45.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 63 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 272 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 17 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 272 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 94 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 0.0% vs overall 5.2% (deviation 5.2 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 68.3% vs overall 46.9% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 0.0% vs overall 22.0% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 7.0% vs overall 5.2% (deviation 1.8 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 2.6% vs overall 5.2% (deviation 2.6 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 7.4% vs overall 5.2% (deviation 2.2 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 40.4% vs overall 46.9% |
| 23 | HIGH_SCORING_MATCHES | 17 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (4 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..17 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=4..24 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..32 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..17 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=6..26 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..32 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=17 positions=1..18 teams=17 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=17 positions=4..25 teams=17 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=17 positions=1..34 teams=17 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 63, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 272, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 17, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 272, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 94, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 0.0, "overall_goalless_pct": 5.2, "deviation_pp": 5.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 68.3, "overall_share": 46.9}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 0.0, "overall_share": 22.0}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 7.0, "overall_goalless_pct": 5.2, "deviation_pp": 1.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 2.6, "overall_goalless_pct": 5.2, "deviation_pp": 2.6}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 7.4, "overall_goalless_pct": 5.2, "deviation_pp": 2.2}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 40.4, "overall_share": 46.9}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 17, "threshold": 8, "examples": [{"scoreline": "2-9", "total_goals": 11, "count": 1}, {"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 25125, "distinct": 25121, "duplicates": 4}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 25125, "fgt_inconsistent": 310, "fgte_inconsistent": 310, "n_with_fgt": 22883}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 17, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 4, "max_pos": 24, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 32, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 17, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 6, "max_pos": 26, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 32, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 18, "distinct_teams": 17}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 17, "min_pos": 4, "max_pos": 25, "distinct_teams": 17}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 34, "distinct_teams": 17}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
