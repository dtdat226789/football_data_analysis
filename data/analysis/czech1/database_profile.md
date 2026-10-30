# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:47:14+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 84 |
| teams | 299 |
| team_aliases | 598 |
| team_seasons | 1368 |
| matches | 21139 |
| standings | 4104 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `12`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 18 | 2020-08-21 | 2021-05-29 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-24 | 2022-04-20 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-30 | 2023-04-30 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-22 | 2024-04-28 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-19 | 2025-04-19 |
| 2025-2026 | True | complete | 280 | 18 | 2025-07-18 | 2026-05-31 |
| 2026-2027 | True | in_progress | 94 | 16 | 2026-07-25 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 21139 | 21139 | 0 |
| matches (league_season_id, game_index) | 21139 | 21139 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 21139 | 21137 | 2 |
| team_seasons (league_season_id, team_id) | 1368 | 1368 | 0 |
| team_seasons api_name within a season | 1368 | 1368 | 0 |
| team_seasons api_slug within a season | 1368 | 1368 | 0 |
| standings (league_season_id, team_id, view) | 4104 | 4104 | 0 |
| team_aliases (form, value) | 598 | 598 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 299 | 299 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `21139`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 21139 | 0.0% |
| kickoff_time | 0 | 21139 | 0.0% |
| home_team_id | 0 | 21139 | 0.0% |
| away_team_id | 0 | 21139 | 0.0% |
| home_score | 0 | 21139 | 0.0% |
| away_score | 0 | 21139 | 0.0% |
| home_ht | 328 | 20811 | 1.6% |
| away_ht | 328 | 20811 | 1.6% |
| first_goal_time | 2001 | 19138 | 9.5% |
| first_goal_time_extra | 2001 | 19138 | 9.5% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 717 | 43.7% |
| Draw | 407 | 24.8% |
| Away | 516 | 31.5% |
| Total | 1640 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4510 |
| Average goals per match | 2.75 |
| Home goals | 2499 (avg 1.524) |
| Away goals | 2011 (avg 1.226) |
| Home goal share | 55.4% |
| Goalless matches | 120 (7.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 41.2% | 26.5% | 32.4% | 822 | 2.686 | 450 | 372 | 27 (8.8%) |
| 2021-2022 | 240 | 48.3% | 25.4% | 26.2% | 670 | 2.792 | 390 | 280 | 14 (5.8%) |
| 2022-2023 | 240 | 43.3% | 24.6% | 32.1% | 720 | 3.0 | 400 | 320 | 10 (4.2%) |
| 2023-2024 | 240 | 44.2% | 26.2% | 29.6% | 678 | 2.825 | 384 | 294 | 17 (7.1%) |
| 2024-2025 | 240 | 44.6% | 22.5% | 32.9% | 627 | 2.612 | 345 | 282 | 22 (9.2%) |
| 2025-2026 | 280 | 42.1% | 23.9% | 33.9% | 740 | 2.643 | 393 | 347 | 23 (8.2%) |
| 2026-2027 | 94 | 42.6% | 23.4% | 34.0% | 253 | 2.691 | 137 | 116 | 7 (7.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1519` of `1640` (92.6%)
| metric | value |
|---|---|
| First goals recorded | 1519 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 29.78 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 44.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 529 |
| 16-30 | 365 |
| 31-45 | 254 |
| 46-60 | 196 |
| 61-75 | 97 |
| 76-90 | 66 |
| 91-120 | 12 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `348`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..18 | 18 |
| 2020-2021 | goals | 18 | 1..18 | 18 |
| 2020-2021 | luck | 18 | 1..18 | 18 |
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
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 184 |
| 2-1 | 153 |
| 1-0 | 141 |
| 2-0 | 125 |
| 0-1 | 124 |
| 0-0 | 120 |
| 1-2 | 111 |
| 2-2 | 85 |
| 0-2 | 81 |
| 3-0 | 76 |
| 3-1 | 65 |
| 1-3 | 62 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-9 | 14 | 1 |
| 5-5 | 10 | 1 |
| 7-2 | 9 | 2 |
| 4-5 | 9 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 701 | 42.7% |
| Mon | 5 | 0.3% |
| Tue | 34 | 2.1% |
| Wed | 80 | 4.9% |
| Thu | 3 | 0.2% |
| Fri | 38 | 2.3% |
| Sat | 779 | 47.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 280 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 94 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 8.8% vs overall 7.3% (deviation 1.5 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 48.3% vs overall 43.7% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 26.2% vs overall 31.5% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 4.2% vs overall 7.3% (deviation 3.1 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 9.2% vs overall 7.3% (deviation 1.9 pp) |
| 21 | HIGH_SCORING_MATCHES | 13 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=306, fgte=306 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..18 teams=18 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..18 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..18 teams=18 |
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
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 280, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 94, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 8.8, "overall_goalless_pct": 7.3, "deviation_pp": 1.5}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 48.3, "overall_share": 43.7}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 26.2, "overall_share": 31.5}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 4.2, "overall_goalless_pct": 7.3, "deviation_pp": 3.1}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 9.2, "overall_goalless_pct": 7.3, "deviation_pp": 1.9}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 13, "threshold": 8, "examples": [{"scoreline": "5-9", "total_goals": 14, "count": 1}, {"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 21139, "distinct": 21137, "duplicates": 2}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 21139, "fgt_inconsistent": 306, "fgte_inconsistent": 306, "n_with_fgt": 19138}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
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
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
