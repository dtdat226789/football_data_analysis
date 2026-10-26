# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:26:31+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `austria2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 7 |
| league_seasons | 28 |
| teams | 80 |
| team_aliases | 160 |
| team_seasons | 387 |
| matches | 5074 |
| standings | 1161 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `4`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 913 |
| austria2 | 2. Liga | Austria | 7 | 1503 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `austria2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-09-11 | 2021-05-23 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-23 | 2022-05-22 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-22 | 2023-06-04 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-28 | 2024-05-25 |
| 2024-2025 | False | complete | 240 | 16 | 2024-08-02 | 2025-05-25 |
| 2025-2026 | True | complete | 223 | 16 | 2025-08-01 | 2026-05-14 |
| 2026-2027 | True | in_progress | 80 | 16 | 2026-07-31 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 5074 | 5074 | 0 |
| matches (league_season_id, game_index) | 5074 | 5074 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 5074 | 5072 | 2 |
| team_seasons (league_season_id, team_id) | 387 | 387 | 0 |
| team_seasons api_name within a season | 387 | 387 | 0 |
| team_seasons api_slug within a season | 387 | 387 | 0 |
| standings (league_season_id, team_id, view) | 1161 | 1161 | 0 |
| team_aliases (form, value) | 160 | 160 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 80 | 80 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `5074`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 5074 | 0.0% |
| kickoff_time | 0 | 5074 | 0.0% |
| home_team_id | 0 | 5074 | 0.0% |
| away_team_id | 0 | 5074 | 0.0% |
| home_score | 0 | 5074 | 0.0% |
| away_score | 0 | 5074 | 0.0% |
| home_ht | 11 | 5063 | 0.2% |
| away_ht | 11 | 5063 | 0.2% |
| first_goal_time | 405 | 4669 | 8.0% |
| first_goal_time_extra | 405 | 4669 | 8.0% |
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
| Home | 650 | 43.2% |
| Draw | 331 | 22.0% |
| Away | 522 | 34.7% |
| Total | 1503 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4438 |
| Average goals per match | 2.953 |
| Home goals | 2370 (avg 1.577) |
| Away goals | 2068 (avg 1.376) |
| Home goal share | 53.4% |
| Goalless matches | 91 (6.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 40.4% | 20.8% | 38.8% | 736 | 3.067 | 386 | 350 | 14 (5.8%) |
| 2021-2022 | 240 | 45.0% | 23.3% | 31.7% | 732 | 3.05 | 402 | 330 | 14 (5.8%) |
| 2022-2023 | 240 | 43.8% | 22.5% | 33.8% | 696 | 2.9 | 366 | 330 | 14 (5.8%) |
| 2023-2024 | 240 | 43.8% | 20.0% | 36.2% | 716 | 2.983 | 376 | 340 | 12 (5.0%) |
| 2024-2025 | 240 | 43.3% | 21.2% | 35.4% | 710 | 2.958 | 382 | 328 | 16 (6.7%) |
| 2025-2026 | 223 | 41.3% | 26.0% | 32.7% | 599 | 2.686 | 317 | 282 | 18 (8.1%) |
| 2026-2027 | 80 | 48.8% | 17.5% | 33.8% | 249 | 3.112 | 141 | 108 | 3 (3.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1409` of `1503` (93.7%)
| metric | value |
|---|---|
| First goals recorded | 1409 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 29.06 |
| Median (p50) | 23.0 |
| p25 | 10.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 514 |
| 16-30 | 347 |
| 31-45 | 224 |
| 46-60 | 160 |
| 61-75 | 92 |
| 76-90 | 56 |
| 91-120 | 16 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `336`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 16 | 1..16 | 16 |
| 2021-2022 | goals | 16 | 1..16 | 16 |
| 2021-2022 | luck | 16 | 1..16 | 16 |
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
| 1-1 | 147 |
| 2-1 | 120 |
| 1-0 | 117 |
| 0-1 | 108 |
| 1-2 | 94 |
| 2-0 | 93 |
| 0-0 | 91 |
| 0-2 | 87 |
| 3-1 | 83 |
| 2-2 | 76 |
| 3-0 | 66 |
| 1-3 | 49 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-3 | 10 | 1 |
| 6-4 | 10 | 1 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 230 | 15.3% |
| Mon | 49 | 3.3% |
| Tue | 38 | 2.5% |
| Wed | 13 | 0.9% |
| Thu | 9 | 0.6% |
| Fri | 840 | 55.9% |
| Sat | 324 | 21.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 223 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 80 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 38.8% vs overall 34.7% |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 8.1% vs overall 6.1% (deviation 2.0 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 48.8% vs overall 43.2% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 17.5% vs overall 22.0% |
| 21 | HIGH_SCORING_MATCHES | 11 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 223, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 80, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 38.8, "overall_share": 34.7}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 8.1, "overall_goalless_pct": 6.1, "deviation_pp": 2.0}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.8, "overall_goalless_pct": 6.1, "deviation_pp": 2.3}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 48.8, "overall_share": 43.2}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 17.5, "overall_share": 22.0}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 11, "threshold": 8, "examples": [{"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 5074, "distinct": 5072, "duplicates": 2}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 5074, "fgt_inconsistent": 8, "fgte_inconsistent": 8, "n_with_fgt": 4669}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
