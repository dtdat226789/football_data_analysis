# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:27:52+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `bulgaria1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 63 |
| teams | 202 |
| team_aliases | 404 |
| team_seasons | 970 |
| matches | 14538 |
| standings | 2910 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `9`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `bulgaria1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 182 | 14 | 2020-08-07 | 2021-04-26 |
| 2021-2022 | False | complete | 182 | 14 | 2021-07-23 | 2022-04-11 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-08 | 2023-05-08 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-14 | 2024-04-21 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-19 | 2025-04-21 |
| 2025-2026 | True | complete | 294 | 17 | 2025-07-18 | 2026-05-29 |
| 2026-2027 | True | in_progress | 79 | 14 | 2026-07-17 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 14538 | 14538 | 0 |
| matches (league_season_id, game_index) | 14538 | 14538 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 14538 | 14536 | 2 |
| team_seasons (league_season_id, team_id) | 970 | 970 | 0 |
| team_seasons api_name within a season | 970 | 970 | 0 |
| team_seasons api_slug within a season | 970 | 970 | 0 |
| standings (league_season_id, team_id, view) | 2910 | 2910 | 0 |
| team_aliases (form, value) | 404 | 404 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 202 | 202 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `14538`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 14538 | 0.0% |
| kickoff_time | 0 | 14538 | 0.0% |
| home_team_id | 0 | 14538 | 0.0% |
| away_team_id | 0 | 14538 | 0.0% |
| home_score | 0 | 14538 | 0.0% |
| away_score | 0 | 14538 | 0.0% |
| home_ht | 316 | 14222 | 2.2% |
| away_ht | 316 | 14222 | 2.2% |
| first_goal_time | 1509 | 13029 | 10.4% |
| first_goal_time_extra | 1509 | 13029 | 10.4% |
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
| Home | 660 | 45.3% |
| Draw | 358 | 24.6% |
| Away | 439 | 30.1% |
| Total | 1457 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3500 |
| Average goals per match | 2.402 |
| Home goals | 1959 (avg 1.345) |
| Away goals | 1541 (avg 1.058) |
| Home goal share | 56.0% |
| Goalless matches | 144 (9.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 182 | 46.2% | 27.5% | 26.4% | 439 | 2.412 | 254 | 185 | 22 (12.1%) |
| 2021-2022 | 182 | 50.5% | 25.3% | 24.2% | 445 | 2.445 | 260 | 185 | 19 (10.4%) |
| 2022-2023 | 240 | 45.4% | 22.9% | 31.7% | 560 | 2.333 | 309 | 251 | 25 (10.4%) |
| 2023-2024 | 240 | 46.2% | 21.2% | 32.5% | 582 | 2.425 | 335 | 247 | 22 (9.2%) |
| 2024-2025 | 240 | 43.3% | 22.9% | 33.8% | 584 | 2.433 | 312 | 272 | 17 (7.1%) |
| 2025-2026 | 294 | 42.5% | 27.9% | 29.6% | 677 | 2.303 | 369 | 308 | 36 (12.2%) |
| 2026-2027 | 79 | 44.3% | 24.1% | 31.6% | 213 | 2.696 | 120 | 93 | 3 (3.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1312` of `1457` (90.0%)
| metric | value |
|---|---|
| First goals recorded | 1312 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 33.37 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 379 |
| 16-30 | 314 |
| 31-45 | 226 |
| 46-60 | 190 |
| 61-75 | 111 |
| 76-90 | 72 |
| 91-120 | 20 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `321`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 14 | 1..14 | 14 |
| 2020-2021 | goals | 14 | 1..14 | 14 |
| 2020-2021 | luck | 14 | 1..14 | 14 |
| 2021-2022 | classic | 14 | 1..14 | 14 |
| 2021-2022 | goals | 14 | 1..14 | 14 |
| 2021-2022 | luck | 14 | 1..14 | 14 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 17 | 1..17 | 17 |
| 2025-2026 | goals | 17 | 1..17 | 17 |
| 2025-2026 | luck | 17 | 1..17 | 17 |
| 2026-2027 | classic | 14 | 1..14 | 14 |
| 2026-2027 | goals | 14 | 1..14 | 14 |
| 2026-2027 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 204 |
| 1-1 | 156 |
| 0-0 | 144 |
| 2-1 | 131 |
| 0-1 | 120 |
| 2-0 | 116 |
| 1-2 | 84 |
| 0-2 | 78 |
| 3-0 | 55 |
| 2-2 | 52 |
| 3-1 | 44 |
| 1-3 | 41 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-1 | 9 | 1 |
| 5-4 | 9 | 1 |
| 3-5 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 392 | 26.9% |
| Mon | 222 | 15.2% |
| Tue | 43 | 3.0% |
| Wed | 49 | 3.4% |
| Thu | 58 | 4.0% |
| Fri | 279 | 19.1% |
| Sat | 414 | 28.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 182 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 14 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 182 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 14 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 294 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 79 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 14 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 12.1% vs overall 9.9% (deviation 2.2 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 50.5% vs overall 45.3% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 24.2% vs overall 30.1% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 7.1% vs overall 9.9% (deviation 2.8 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 12.2% vs overall 9.9% (deviation 2.3 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.8% vs overall 9.9% (deviation 6.1 pp) |
| 22 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=295, fgte=295 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=14 positions=1..14 teams=14 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=14 positions=1..14 teams=14 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=14 positions=1..14 teams=14 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=14 positions=1..14 teams=14 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=14 positions=1..14 teams=14 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=14 positions=1..14 teams=14 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=14 positions=1..14 teams=14 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=14 positions=1..14 teams=14 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 182, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 14, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 182, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 14, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 294, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 79, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 14, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 12.1, "overall_goalless_pct": 9.9, "deviation_pp": 2.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 50.5, "overall_share": 45.3}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 24.2, "overall_share": 30.1}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 7.1, "overall_goalless_pct": 9.9, "deviation_pp": 2.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 12.2, "overall_goalless_pct": 9.9, "deviation_pp": 2.3}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.8, "overall_goalless_pct": 9.9, "deviation_pp": 6.1}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 14538, "distinct": 14536, "duplicates": 2}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 14538, "fgt_inconsistent": 295, "fgte_inconsistent": 295, "n_with_fgt": 13029}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
