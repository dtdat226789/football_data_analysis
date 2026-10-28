# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:39:12+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `algir1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 7 |
| league_seasons | 7 |
| teams | 31 |
| team_aliases | 62 |
| team_seasons | 118 |
| matches | 1696 |
| standings | 354 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `1`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `algir1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 379 | 20 | 2020-11-27 | 2021-08-28 |
| 2021-2022 | False | complete | 306 | 18 | 2021-10-22 | 2022-06-17 |
| 2022-2023 | False | complete | 240 | 16 | 2022-08-26 | 2023-07-15 |
| 2023-2024 | False | complete | 240 | 16 | 2023-09-15 | 2024-06-14 |
| 2024-2025 | False | complete | 240 | 16 | 2024-09-19 | 2025-06-21 |
| 2025-2026 | True | complete | 240 | 16 | 2025-08-21 | 2026-06-06 |
| 2026-2027 | True | in_progress | 51 | 16 | 2026-09-03 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 1696 | 1696 | 0 |
| matches (league_season_id, game_index) | 1696 | 1696 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 1696 | 1694 | 2 |
| team_seasons (league_season_id, team_id) | 118 | 118 | 0 |
| team_seasons api_name within a season | 118 | 118 | 0 |
| team_seasons api_slug within a season | 118 | 118 | 0 |
| standings (league_season_id, team_id, view) | 354 | 354 | 0 |
| team_aliases (form, value) | 62 | 62 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 31 | 31 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `1696`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 1696 | 0.0% |
| kickoff_time | 0 | 1696 | 0.0% |
| home_team_id | 0 | 1696 | 0.0% |
| away_team_id | 0 | 1696 | 0.0% |
| home_score | 0 | 1696 | 0.0% |
| away_score | 0 | 1696 | 0.0% |
| home_ht | 6 | 1690 | 0.4% |
| away_ht | 6 | 1690 | 0.4% |
| first_goal_time | 210 | 1486 | 12.4% |
| first_goal_time_extra | 210 | 1486 | 12.4% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 8 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 4 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 859 | 50.6% |
| Draw | 478 | 28.2% |
| Away | 359 | 21.2% |
| Total | 1696 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3794 |
| Average goals per match | 2.237 |
| Home goals | 2318 (avg 1.367) |
| Away goals | 1476 (avg 0.87) |
| Home goal share | 61.1% |
| Goalless matches | 207 (12.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 379 | 51.2% | 27.4% | 21.4% | 902 | 2.38 | 538 | 364 | 37 (9.8%) |
| 2021-2022 | 306 | 48.0% | 28.1% | 23.9% | 693 | 2.265 | 421 | 272 | 43 (14.1%) |
| 2022-2023 | 240 | 57.1% | 26.7% | 16.2% | 516 | 2.15 | 343 | 173 | 31 (12.9%) |
| 2023-2024 | 240 | 51.2% | 25.4% | 23.3% | 556 | 2.317 | 334 | 222 | 28 (11.7%) |
| 2024-2025 | 240 | 48.3% | 31.2% | 20.4% | 467 | 1.946 | 286 | 181 | 42 (17.5%) |
| 2025-2026 | 240 | 50.0% | 29.2% | 20.8% | 544 | 2.267 | 325 | 219 | 20 (8.3%) |
| 2026-2027 | 51 | 43.1% | 35.3% | 21.6% | 116 | 2.275 | 71 | 45 | 6 (11.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1486` of `1696` (87.6%)
| metric | value |
|---|---|
| First goals recorded | 1486 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 35.96 |
| Median (p50) | 31.0 |
| p25 | 14.0 |
| p75 | 52.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 406 |
| 16-30 | 318 |
| 31-45 | 255 |
| 46-60 | 224 |
| 61-75 | 133 |
| 76-90 | 118 |
| 91-120 | 32 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `354`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 295 |
| 0-0 | 207 |
| 1-1 | 203 |
| 2-1 | 183 |
| 2-0 | 154 |
| 0-1 | 131 |
| 1-2 | 71 |
| 2-2 | 61 |
| 3-1 | 56 |
| 3-0 | 54 |
| 0-2 | 47 |
| 3-2 | 34 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 2 |
| 4-5 | 9 | 2 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 3 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 197 | 11.6% |
| Mon | 75 | 4.4% |
| Tue | 212 | 12.5% |
| Wed | 126 | 7.4% |
| Thu | 117 | 6.9% |
| Fri | 485 | 28.6% |
| Sat | 484 | 28.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 379 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 4 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 5 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 6 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 7 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 8 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 9 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 10 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 11 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 12 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 51 matches, expected 380 |
| 13 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 14 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 9.8% vs overall 12.2% (deviation 2.4 pp) |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 14.1% vs overall 12.2% (deviation 1.9 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 57.1% vs overall 50.6% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 16.2% vs overall 21.2% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 17.5% vs overall 12.2% (deviation 5.3 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 8.3% vs overall 12.2% (deviation 3.9 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 43.1% vs overall 50.6% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 35.3% vs overall 28.2% |
| 23 | HIGH_SCORING_MATCHES | 15 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=3, fgte=3 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 379, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `4.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `5.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `6.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `7.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `8.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `9.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `10.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `11.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `12.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 51, "expected": 380}`
- `13.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `14.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 9.8, "overall_goalless_pct": 12.2, "deviation_pp": 2.4}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 14.1, "overall_goalless_pct": 12.2, "deviation_pp": 1.9}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 57.1, "overall_share": 50.6}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 16.2, "overall_share": 21.2}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 17.5, "overall_goalless_pct": 12.2, "deviation_pp": 5.3}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 8.3, "overall_goalless_pct": 12.2, "deviation_pp": 3.9}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 43.1, "overall_share": 50.6}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 35.3, "overall_share": 28.2}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 15, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 1696, "distinct": 1694, "duplicates": 2}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 1696, "fgt_inconsistent": 3, "fgte_inconsistent": 3, "n_with_fgt": 1486}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
