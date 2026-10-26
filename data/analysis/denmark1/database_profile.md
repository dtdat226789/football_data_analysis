# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:29:49+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `denmark1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 110 |
| teams | 376 |
| team_aliases | 752 |
| team_seasons | 1758 |
| matches | 26021 |
| standings | 5274 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `16`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `denmark1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 132 | 12 | 2020-09-11 | 2021-03-21 |
| 2021-2022 | False | complete | 132 | 12 | 2021-07-16 | 2022-03-20 |
| 2022-2023 | False | complete | 132 | 12 | 2022-07-15 | 2023-03-19 |
| 2023-2024 | False | complete | 132 | 12 | 2023-07-21 | 2024-03-17 |
| 2024-2025 | False | complete | 132 | 12 | 2024-07-19 | 2025-03-16 |
| 2025-2026 | True | complete | 193 | 12 | 2025-07-18 | 2026-05-21 |
| 2026-2027 | True | in_progress | 68 | 12 | 2026-07-24 | 2026-10-23 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 26021 | 26021 | 0 |
| matches (league_season_id, game_index) | 26021 | 26021 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 26021 | 26016 | 5 |
| team_seasons (league_season_id, team_id) | 1758 | 1758 | 0 |
| team_seasons api_name within a season | 1758 | 1758 | 0 |
| team_seasons api_slug within a season | 1758 | 1758 | 0 |
| standings (league_season_id, team_id, view) | 5274 | 5274 | 0 |
| team_aliases (form, value) | 752 | 752 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 376 | 376 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `26021`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 26021 | 0.0% |
| kickoff_time | 0 | 26021 | 0.0% |
| home_team_id | 0 | 26021 | 0.0% |
| away_team_id | 0 | 26021 | 0.0% |
| home_score | 0 | 26021 | 0.0% |
| away_score | 0 | 26021 | 0.0% |
| home_ht | 340 | 25681 | 1.3% |
| away_ht | 340 | 25681 | 1.3% |
| first_goal_time | 2296 | 23725 | 8.8% |
| first_goal_time_extra | 2296 | 23725 | 8.8% |
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
| Home | 380 | 41.3% |
| Draw | 252 | 27.4% |
| Away | 289 | 31.4% |
| Total | 921 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2640 |
| Average goals per match | 2.866 |
| Home goals | 1402 (avg 1.522) |
| Away goals | 1238 (avg 1.344) |
| Home goal share | 53.1% |
| Goalless matches | 56 (6.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 132 | 41.7% | 25.8% | 32.6% | 359 | 2.72 | 191 | 168 | 10 (7.6%) |
| 2021-2022 | 132 | 38.6% | 30.3% | 31.1% | 354 | 2.682 | 190 | 164 | 8 (6.1%) |
| 2022-2023 | 132 | 40.2% | 28.8% | 31.1% | 359 | 2.72 | 184 | 175 | 10 (7.6%) |
| 2023-2024 | 132 | 40.2% | 25.0% | 34.8% | 356 | 2.697 | 189 | 167 | 8 (6.1%) |
| 2024-2025 | 132 | 44.7% | 31.1% | 24.2% | 406 | 3.076 | 219 | 187 | 6 (4.5%) |
| 2025-2026 | 193 | 41.5% | 23.3% | 35.2% | 599 | 3.104 | 320 | 279 | 11 (5.7%) |
| 2026-2027 | 68 | 42.6% | 30.9% | 26.5% | 207 | 3.044 | 109 | 98 | 3 (4.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `865` of `921` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 865 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.54 |
| Median (p50) | 25.0 |
| p25 | 10.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 315 |
| 16-30 | 194 |
| 31-45 | 148 |
| 46-60 | 111 |
| 61-75 | 49 |
| 76-90 | 38 |
| 91-120 | 10 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `252`
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
| 2024-2025 | classic | 12 | 1..12 | 12 |
| 2024-2025 | goals | 12 | 1..12 | 12 |
| 2024-2025 | luck | 12 | 1..12 | 12 |
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 117 |
| 1-0 | 84 |
| 2-1 | 82 |
| 1-2 | 69 |
| 0-2 | 63 |
| 2-2 | 58 |
| 2-0 | 56 |
| 0-0 | 56 |
| 0-1 | 45 |
| 3-1 | 37 |
| 3-2 | 31 |
| 1-3 | 25 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 593 | 64.4% |
| Mon | 126 | 13.7% |
| Tue | 3 | 0.3% |
| Wed | 10 | 1.1% |
| Thu | 10 | 1.1% |
| Fri | 130 | 14.1% |
| Sat | 49 | 5.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 132 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 132 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 132 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 132 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 12 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 193 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 68 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 24.2% vs overall 31.4% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 23.3% vs overall 27.4% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.4% vs overall 6.1% (deviation 1.7 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 26.5% vs overall 31.4% |
| 21 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=12 positions=1..12 teams=12 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=12 positions=1..12 teams=12 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=12 positions=1..12 teams=12 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=12 positions=1..12 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=12 positions=1..12 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=12 positions=1..12 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=12 positions=1..12 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=12 positions=1..12 teams=12 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=12 positions=1..12 teams=12 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 132, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 132, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 132, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 132, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 12, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 193, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 68, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 4.5, "overall_goalless_pct": 6.1, "deviation_pp": 1.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 24.2, "overall_share": 31.4}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 23.3, "overall_share": 27.4}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.4, "overall_goalless_pct": 6.1, "deviation_pp": 1.7}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 26.5, "overall_share": 31.4}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 2}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 26021, "distinct": 26016, "duplicates": 5}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 26021, "fgt_inconsistent": 310, "fgte_inconsistent": 310, "n_with_fgt": 23725}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
