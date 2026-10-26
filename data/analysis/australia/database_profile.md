# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:25:59+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `australia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 7 |
| league_seasons | 14 |
| teams | 44 |
| team_aliases | 88 |
| team_seasons | 191 |
| matches | 2658 |
| standings | 573 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `2`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `australia`: `7`
- With match data: `6`
- Registered but no data: `['2026-2027']`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 156 | 12 | 2020-12-28 | 2021-06-10 |
| 2021-2022 | False | complete | 156 | 12 | 2021-11-19 | 2022-05-10 |
| 2022-2023 | False | complete | 156 | 12 | 2022-10-07 | 2023-04-29 |
| 2023-2024 | False | complete | 162 | 12 | 2023-10-20 | 2024-05-01 |
| 2024-2025 | False | complete | 169 | 13 | 2024-10-18 | 2025-05-04 |
| 2025-2026 | True | complete | 163 | 12 | 2025-10-17 | 2026-05-23 |
| 2026-2027 | True | unknown | 0 | 0 | - | - |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 2658 | 2658 | 0 |
| matches (league_season_id, game_index) | 2658 | 2658 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 2658 | 2656 | 2 |
| team_seasons (league_season_id, team_id) | 191 | 191 | 0 |
| team_seasons api_name within a season | 191 | 191 | 0 |
| team_seasons api_slug within a season | 191 | 191 | 0 |
| standings (league_season_id, team_id, view) | 573 | 573 | 0 |
| team_aliases (form, value) | 88 | 88 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 44 | 44 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `2658`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 2658 | 0.0% |
| kickoff_time | 0 | 2658 | 0.0% |
| home_team_id | 0 | 2658 | 0.0% |
| away_team_id | 0 | 2658 | 0.0% |
| home_score | 0 | 2658 | 0.0% |
| away_score | 0 | 2658 | 0.0% |
| home_ht | 8 | 2650 | 0.3% |
| away_ht | 8 | 2650 | 0.3% |
| first_goal_time | 255 | 2403 | 9.6% |
| first_goal_time_extra | 255 | 2403 | 9.6% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 8 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 402 | 41.8% |
| Draw | 241 | 25.1% |
| Away | 319 | 33.2% |
| Total | 962 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2949 |
| Average goals per match | 3.065 |
| Home goals | 1597 (avg 1.66) |
| Away goals | 1352 (avg 1.405) |
| Home goal share | 54.2% |
| Goalless matches | 43 (4.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 156 | 42.9% | 23.7% | 33.3% | 457 | 2.929 | 246 | 211 | 9 (5.8%) |
| 2021-2022 | 156 | 46.8% | 24.4% | 28.8% | 457 | 2.929 | 255 | 202 | 6 (3.8%) |
| 2022-2023 | 156 | 45.5% | 25.0% | 29.5% | 477 | 3.058 | 269 | 208 | 4 (2.6%) |
| 2023-2024 | 162 | 43.2% | 24.7% | 32.1% | 540 | 3.333 | 303 | 237 | 7 (4.3%) |
| 2024-2025 | 169 | 34.9% | 26.0% | 39.1% | 556 | 3.29 | 280 | 276 | 8 (4.7%) |
| 2025-2026 | 163 | 38.0% | 26.4% | 35.6% | 462 | 2.834 | 244 | 218 | 9 (5.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `917` of `962` (95.3%)
| metric | value |
|---|---|
| First goals recorded | 917 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.4 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 319 |
| 16-30 | 232 |
| 31-45 | 145 |
| 46-60 | 119 |
| 61-75 | 59 |
| 76-90 | 31 |
| 91-120 | 12 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `219`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 12 | 1..12 | 12 |
| 2020-2021 | goals | 12 | 1..12 | 12 |
| 2020-2021 | luck | 12 | 1..12 | 12 |
| 2021-2022 | classic | 12 | 1..12 | 12 |
| 2021-2022 | goals | 12 | 1..12 | 12 |
| 2021-2022 | luck | 12 | 1..12 | 12 |
| 2022-2023 | classic | 12 | 1..12 | 12 |
| 2022-2023 | goals | 12 | 1..12 | 12 |
| 2022-2023 | luck | 12 | 1..12 | 12 |
| 2023-2024 | classic | 12 | 1..12 | 12 |
| 2023-2024 | goals | 12 | 1..12 | 12 |
| 2023-2024 | luck | 12 | 1..12 | 12 |
| 2024-2025 | classic | 13 | 1..13 | 13 |
| 2024-2025 | goals | 13 | 1..13 | 13 |
| 2024-2025 | luck | 13 | 1..13 | 13 |
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 104 |
| 2-1 | 85 |
| 1-2 | 83 |
| 2-2 | 77 |
| 1-0 | 74 |
| 0-1 | 69 |
| 2-0 | 57 |
| 0-0 | 43 |
| 0-2 | 40 |
| 1-3 | 34 |
| 3-2 | 34 |
| 3-0 | 32 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-1 | 9 | 1 |
| 5-4 | 9 | 2 |
| 4-5 | 9 | 2 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 4 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 228 | 23.7% |
| Mon | 30 | 3.1% |
| Tue | 43 | 4.5% |
| Wed | 59 | 6.1% |
| Thu | 26 | 2.7% |
| Fri | 169 | 17.6% |
| Sat | 407 | 42.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 156 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 156 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 156 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 162 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 169 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 13 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 163 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 13 | SEASON_REGISTERED_NO_DATA | Season 2026-2027 is registered but has no match data (declared_by_api=True, state=unknown) |
| 14 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 0 matches, expected 380 |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 46.8% vs overall 41.8% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 28.8% vs overall 33.2% |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 2.6% vs overall 4.5% (deviation 1.9 pp) |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 34.9% vs overall 41.8% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 39.1% vs overall 33.2% |
| 20 | HIGH_SCORING_MATCHES | 16 match(es) with >= 8 total goals (extreme scorelines) |
| 21 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 22 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=12 positions=1..12 teams=12 |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=12 positions=1..12 teams=12 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=12 positions=1..12 teams=12 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=12 positions=1..12 teams=12 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=12 positions=1..12 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=12 positions=1..12 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=12 positions=1..12 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=13 positions=1..13 teams=13 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=13 positions=1..13 teams=13 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=13 positions=1..13 teams=13 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 156, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 156, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 156, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 162, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 169, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 13, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 163, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `13.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2026-2027"}`
- `14.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 0, "expected": 380}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 46.8, "overall_share": 41.8}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 28.8, "overall_share": 33.2}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 2.6, "overall_goalless_pct": 4.5, "deviation_pp": 1.9}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 34.9, "overall_share": 41.8}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 39.1, "overall_share": 33.2}`
- `20.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 16, "threshold": 8, "examples": [{"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 4}]}`
- `21.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 2658, "distinct": 2656, "duplicates": 2}`
- `22.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 2658, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 2403}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
