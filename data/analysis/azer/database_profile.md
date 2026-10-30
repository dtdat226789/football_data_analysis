# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:45:01+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `azer`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 7 |
| league_seasons | 35 |
| teams | 96 |
| team_aliases | 192 |
| team_seasons | 459 |
| matches | 6100 |
| standings | 1377 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `5`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1697 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `azer`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 112 | 8 | 2020-08-21 | 2021-05-19 |
| 2021-2022 | False | complete | 112 | 8 | 2021-08-14 | 2022-05-21 |
| 2022-2023 | False | complete | 180 | 10 | 2022-08-05 | 2023-05-28 |
| 2023-2024 | False | complete | 180 | 10 | 2023-08-04 | 2024-05-26 |
| 2024-2025 | False | complete | 180 | 10 | 2024-08-02 | 2025-05-25 |
| 2025-2026 | True | complete | 200 | 13 | 2025-08-15 | 2026-05-28 |
| 2026-2027 | True | in_progress | 59 | 13 | 2026-08-14 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 6100 | 6100 | 0 |
| matches (league_season_id, game_index) | 6100 | 6100 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 6100 | 6098 | 2 |
| team_seasons (league_season_id, team_id) | 459 | 459 | 0 |
| team_seasons api_name within a season | 459 | 459 | 0 |
| team_seasons api_slug within a season | 459 | 459 | 0 |
| standings (league_season_id, team_id, view) | 1377 | 1377 | 0 |
| team_aliases (form, value) | 192 | 192 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 96 | 96 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `6100`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 6100 | 0.0% |
| kickoff_time | 0 | 6100 | 0.0% |
| home_team_id | 0 | 6100 | 0.0% |
| away_team_id | 0 | 6100 | 0.0% |
| home_score | 0 | 6100 | 0.0% |
| away_score | 0 | 6100 | 0.0% |
| home_ht | 13 | 6087 | 0.2% |
| away_ht | 13 | 6087 | 0.2% |
| first_goal_time | 493 | 5607 | 8.1% |
| first_goal_time_extra | 493 | 5607 | 8.1% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 8 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 415 | 40.6% |
| Draw | 263 | 25.7% |
| Away | 345 | 33.7% |
| Total | 1023 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2603 |
| Average goals per match | 2.544 |
| Home goals | 1386 (avg 1.355) |
| Away goals | 1217 (avg 1.19) |
| Home goal share | 53.2% |
| Goalless matches | 87 (8.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 112 | 38.4% | 33.9% | 27.7% | 266 | 2.375 | 144 | 122 | 14 (12.5%) |
| 2021-2022 | 112 | 41.1% | 22.3% | 36.6% | 291 | 2.598 | 164 | 127 | 8 (7.1%) |
| 2022-2023 | 180 | 40.0% | 25.6% | 34.4% | 475 | 2.639 | 242 | 233 | 15 (8.3%) |
| 2023-2024 | 180 | 43.9% | 22.8% | 33.3% | 471 | 2.617 | 259 | 212 | 11 (6.1%) |
| 2024-2025 | 180 | 40.6% | 27.8% | 31.7% | 432 | 2.4 | 232 | 200 | 15 (8.3%) |
| 2025-2026 | 200 | 37.5% | 24.5% | 38.0% | 515 | 2.575 | 261 | 254 | 18 (9.0%) |
| 2026-2027 | 59 | 45.8% | 23.7% | 30.5% | 153 | 2.593 | 84 | 69 | 6 (10.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `935` of `1023` (91.4%)
| metric | value |
|---|---|
| First goals recorded | 935 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.54 |
| Median (p50) | 30.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 259 |
| 16-30 | 212 |
| 31-45 | 159 |
| 46-60 | 155 |
| 61-75 | 81 |
| 76-90 | 48 |
| 91-120 | 21 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `216`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 8 | 1..8 | 8 |
| 2020-2021 | goals | 8 | 1..8 | 8 |
| 2020-2021 | luck | 8 | 1..8 | 8 |
| 2021-2022 | classic | 8 | 1..8 | 8 |
| 2021-2022 | goals | 8 | 1..8 | 8 |
| 2021-2022 | luck | 8 | 1..8 | 8 |
| 2022-2023 | classic | 10 | 1..10 | 10 |
| 2022-2023 | goals | 10 | 1..10 | 10 |
| 2022-2023 | luck | 10 | 1..10 | 10 |
| 2023-2024 | classic | 10 | 1..10 | 10 |
| 2023-2024 | goals | 10 | 1..10 | 10 |
| 2023-2024 | luck | 10 | 1..10 | 10 |
| 2024-2025 | classic | 10 | 1..10 | 10 |
| 2024-2025 | goals | 10 | 1..10 | 10 |
| 2024-2025 | luck | 10 | 1..10 | 10 |
| 2025-2026 | classic | 13 | 1..13 | 13 |
| 2025-2026 | goals | 13 | 1..13 | 13 |
| 2025-2026 | luck | 13 | 1..13 | 13 |
| 2026-2027 | classic | 13 | 1..13 | 13 |
| 2026-2027 | goals | 13 | 1..13 | 13 |
| 2026-2027 | luck | 13 | 1..13 | 13 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 120 |
| 1-0 | 106 |
| 0-1 | 99 |
| 0-0 | 87 |
| 2-1 | 73 |
| 2-0 | 70 |
| 0-2 | 60 |
| 1-2 | 60 |
| 2-2 | 49 |
| 0-3 | 40 |
| 3-1 | 40 |
| 3-0 | 39 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-0 | 8 | 1 |
| 7-1 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 340 | 33.2% |
| Mon | 78 | 7.6% |
| Tue | 37 | 3.6% |
| Wed | 25 | 2.4% |
| Thu | 30 | 2.9% |
| Fri | 173 | 16.9% |
| Sat | 340 | 33.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 112 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 8 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 112 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 8 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 200 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 13 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 59 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 13 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 12.5% vs overall 8.5% (deviation 4.0 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 33.9% vs overall 25.7% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 27.7% vs overall 33.7% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 6.1% vs overall 8.5% (deviation 2.4 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 away outcome share 38.0% vs overall 33.7% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.2% vs overall 8.5% (deviation 1.7 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 45.8% vs overall 40.6% |
| 23 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=9, fgte=9 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=8 positions=1..8 teams=8 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=8 positions=1..8 teams=8 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=8 positions=1..8 teams=8 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=8 positions=1..8 teams=8 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=8 positions=1..8 teams=8 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=8 positions=1..8 teams=8 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=10 positions=1..10 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=13 positions=1..13 teams=13 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=13 positions=1..13 teams=13 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=13 positions=1..13 teams=13 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=13 positions=1..13 teams=13 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=13 positions=1..13 teams=13 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=13 positions=1..13 teams=13 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 112, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 8, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 112, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 8, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 200, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 13, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 59, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 13, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 12.5, "overall_goalless_pct": 8.5, "deviation_pp": 4.0}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 33.9, "overall_share": 25.7}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 27.7, "overall_share": 33.7}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 6.1, "overall_goalless_pct": 8.5, "deviation_pp": 2.4}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "away", "season_share": 38.0, "overall_share": 33.7}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.2, "overall_goalless_pct": 8.5, "deviation_pp": 1.7}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 45.8, "overall_share": 40.6}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 6100, "distinct": 6098, "duplicates": 2}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 6100, "fgt_inconsistent": 9, "fgte_inconsistent": 9, "n_with_fgt": 5607}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 8, "min_pos": 1, "max_pos": 8, "distinct_teams": 8}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
