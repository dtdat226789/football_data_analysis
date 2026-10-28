# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:43:52+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech3a`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 96 |
| teams | 341 |
| team_aliases | 682 |
| team_seasons | 1560 |
| matches | 23696 |
| standings | 4680 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `14`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2620 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1457 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1640 |
| czech2 | ChNL | Czech Republic | 7 | 1478 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech3a`: `5`
- With match data: `5`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2022-2023 | False | complete | 240 | 16 | 2022-08-06 | 2023-06-11 |
| 2023-2024 | False | complete | 240 | 16 | 2023-08-04 | 2024-06-09 |
| 2024-2025 | False | complete | 240 | 17 | 2024-08-09 | 2025-06-08 |
| 2025-2026 | True | complete | 272 | 17 | 2025-08-08 | 2026-06-06 |
| 2026-2027 | True | in_progress | 95 | 16 | 2026-08-07 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 23696 | 23696 | 0 |
| matches (league_season_id, game_index) | 23696 | 23696 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 23696 | 23693 | 3 |
| team_seasons (league_season_id, team_id) | 1560 | 1560 | 0 |
| team_seasons api_name within a season | 1560 | 1560 | 0 |
| team_seasons api_slug within a season | 1560 | 1560 | 0 |
| standings (league_season_id, team_id, view) | 4680 | 4680 | 0 |
| team_aliases (form, value) | 682 | 682 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 341 | 341 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `23696`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 23696 | 0.0% |
| kickoff_time | 0 | 23696 | 0.0% |
| home_team_id | 0 | 23696 | 0.0% |
| away_team_id | 0 | 23696 | 0.0% |
| home_score | 0 | 23696 | 0.0% |
| away_score | 0 | 23696 | 0.0% |
| home_ht | 330 | 23366 | 1.4% |
| away_ht | 330 | 23366 | 1.4% |
| first_goal_time | 2164 | 21532 | 9.1% |
| first_goal_time_extra | 2164 | 21532 | 9.1% |
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
| Home | 504 | 46.4% |
| Draw | 239 | 22.0% |
| Away | 344 | 31.6% |
| Total | 1087 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3498 |
| Average goals per match | 3.218 |
| Home goals | 1939 (avg 1.784) |
| Away goals | 1559 (avg 1.434) |
| Home goal share | 55.4% |
| Goalless matches | 61 (5.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2022-2023 | 240 | 50.4% | 20.8% | 28.8% | 745 | 3.104 | 428 | 317 | 15 (6.2%) |
| 2023-2024 | 240 | 48.8% | 22.5% | 28.8% | 793 | 3.304 | 454 | 339 | 11 (4.6%) |
| 2024-2025 | 240 | 42.5% | 20.8% | 36.7% | 754 | 3.142 | 402 | 352 | 10 (4.2%) |
| 2025-2026 | 272 | 45.6% | 21.0% | 33.5% | 869 | 3.195 | 464 | 405 | 17 (6.2%) |
| 2026-2027 | 95 | 42.1% | 29.5% | 28.4% | 337 | 3.547 | 191 | 146 | 8 (8.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1025` of `1087` (94.3%)
| metric | value |
|---|---|
| First goals recorded | 1025 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 26.5 |
| Median (p50) | 20.0 |
| p25 | 10.0 |
| p75 | 38.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 429 |
| 16-30 | 244 |
| 31-45 | 162 |
| 46-60 | 98 |
| 61-75 | 48 |
| 76-90 | 40 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `15` of `15` expected
- Standings rows total: `246`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 17 | 1..17 | 17 |
| 2024-2025 | goals | 17 | 1..17 | 17 |
| 2024-2025 | luck | 17 | 1..17 | 17 |
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
| 1-1 | 95 |
| 2-1 | 88 |
| 1-0 | 77 |
| 2-0 | 70 |
| 3-1 | 69 |
| 1-2 | 69 |
| 0-0 | 61 |
| 2-2 | 61 |
| 0-1 | 56 |
| 0-2 | 54 |
| 3-0 | 44 |
| 3-2 | 43 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-1 | 10 | 1 |
| 9-0 | 9 | 1 |
| 7-2 | 9 | 4 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 1 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 2 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 5 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 373 | 34.3% |
| Mon | 1 | 0.1% |
| Tue | 3 | 0.3% |
| Wed | 59 | 5.4% |
| Thu | 3 | 0.3% |
| Fri | 121 | 11.1% |
| Sat | 527 | 48.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 17 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 272 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 17 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 95 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 11 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 36.7% vs overall 31.6% |
| 13 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 8.4% vs overall 5.6% (deviation 2.8 pp) |
| 14 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 42.1% vs overall 46.4% |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 29.5% vs overall 22.0% |
| 16 | HIGH_SCORING_MATCHES | 23 match(es) with >= 8 total goals (extreme scorelines) |
| 17 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (3 extra rows) |
| 18 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=307, fgte=307 rows) |
| 19 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 20 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 21 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 22 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 23 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=17 positions=1..17 teams=17 |
| 26 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=17 positions=1..17 teams=17 |
| 27 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=17 positions=1..17 teams=17 |
| 28 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=17 positions=1..17 teams=17 |
| 29 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=17 positions=1..17 teams=17 |
| 30 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=17 positions=1..17 teams=17 |
| 31 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 17, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 272, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 17, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 95, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `11.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 36.7, "overall_share": 31.6}`
- `13.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 8.4, "overall_goalless_pct": 5.6, "deviation_pp": 2.8}`
- `14.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 42.1, "overall_share": 46.4}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 29.5, "overall_share": 22.0}`
- `16.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 23, "threshold": 8, "examples": [{"scoreline": "9-1", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 4}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 1}]}`
- `17.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 23696, "distinct": 23693, "duplicates": 3}`
- `18.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 23696, "fgt_inconsistent": 307, "fgte_inconsistent": 307, "n_with_fgt": 21532}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
