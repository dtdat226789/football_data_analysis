# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:30:05+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `denmark2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 117 |
| teams | 392 |
| team_aliases | 784 |
| team_seasons | 1839 |
| matches | 26869 |
| standings | 5517 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `17`
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
| denmark2 | 1st Division | Denmark | 7 | 848 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `denmark2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 132 | 12 | 2020-09-10 | 2021-03-19 |
| 2021-2022 | False | complete | 132 | 12 | 2021-07-23 | 2022-03-18 |
| 2022-2023 | False | complete | 132 | 12 | 2022-07-22 | 2023-03-18 |
| 2023-2024 | False | complete | 110 | 11 | 2023-07-21 | 2024-03-16 |
| 2024-2025 | False | complete | 110 | 11 | 2024-07-19 | 2025-03-14 |
| 2025-2026 | True | complete | 160 | 11 | 2025-07-18 | 2026-05-31 |
| 2026-2027 | True | in_progress | 72 | 12 | 2026-07-24 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 26869 | 26869 | 0 |
| matches (league_season_id, game_index) | 26869 | 26869 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 26869 | 26864 | 5 |
| team_seasons (league_season_id, team_id) | 1839 | 1839 | 0 |
| team_seasons api_name within a season | 1839 | 1839 | 0 |
| team_seasons api_slug within a season | 1839 | 1839 | 0 |
| standings (league_season_id, team_id, view) | 5517 | 5517 | 0 |
| team_aliases (form, value) | 784 | 784 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 392 | 392 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `26869`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 26869 | 0.0% |
| kickoff_time | 0 | 26869 | 0.0% |
| home_team_id | 0 | 26869 | 0.0% |
| away_team_id | 0 | 26869 | 0.0% |
| home_score | 0 | 26869 | 0.0% |
| away_score | 0 | 26869 | 0.0% |
| home_ht | 340 | 26529 | 1.3% |
| away_ht | 340 | 26529 | 1.3% |
| first_goal_time | 2348 | 24521 | 8.7% |
| first_goal_time_extra | 2348 | 24521 | 8.7% |
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
| Home | 349 | 41.2% |
| Draw | 205 | 24.2% |
| Away | 294 | 34.7% |
| Total | 848 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2427 |
| Average goals per match | 2.862 |
| Home goals | 1278 (avg 1.507) |
| Away goals | 1149 (avg 1.355) |
| Home goal share | 52.7% |
| Goalless matches | 52 (6.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 132 | 41.7% | 19.7% | 38.6% | 364 | 2.758 | 191 | 173 | 6 (4.5%) |
| 2021-2022 | 132 | 43.9% | 24.2% | 31.8% | 395 | 2.992 | 210 | 185 | 5 (3.8%) |
| 2022-2023 | 132 | 46.2% | 18.9% | 34.8% | 395 | 2.992 | 221 | 174 | 8 (6.1%) |
| 2023-2024 | 110 | 36.4% | 25.5% | 38.2% | 336 | 3.055 | 169 | 167 | 6 (5.5%) |
| 2024-2025 | 110 | 40.0% | 20.0% | 40.0% | 306 | 2.782 | 148 | 158 | 7 (6.4%) |
| 2025-2026 | 160 | 41.2% | 28.1% | 30.6% | 436 | 2.725 | 238 | 198 | 12 (7.5%) |
| 2026-2027 | 72 | 34.7% | 37.5% | 27.8% | 195 | 2.708 | 101 | 94 | 8 (11.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `796` of `848` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 796 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 28.4 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 307 |
| 16-30 | 189 |
| 31-45 | 110 |
| 46-60 | 100 |
| 61-75 | 50 |
| 76-90 | 31 |
| 91-120 | 9 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `243`
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
| 2023-2024 | classic | 11 | 1..11 | 11 |
| 2023-2024 | goals | 11 | 1..11 | 11 |
| 2023-2024 | luck | 11 | 1..11 | 11 |
| 2024-2025 | classic | 11 | 1..11 | 11 |
| 2024-2025 | goals | 11 | 1..11 | 11 |
| 2024-2025 | luck | 11 | 1..11 | 11 |
| 2025-2026 | classic | 11 | 1..11 | 11 |
| 2025-2026 | goals | 11 | 1..11 | 11 |
| 2025-2026 | luck | 11 | 1..11 | 11 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 93 |
| 1-0 | 70 |
| 2-1 | 67 |
| 1-2 | 66 |
| 0-1 | 64 |
| 2-0 | 54 |
| 0-0 | 52 |
| 2-2 | 45 |
| 0-2 | 43 |
| 3-1 | 42 |
| 3-0 | 34 |
| 0-3 | 30 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 4-4 | 8 | 2 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 208 | 24.5% |
| Mon | 29 | 3.4% |
| Tue | 23 | 2.7% |
| Wed | 26 | 3.1% |
| Thu | 28 | 3.3% |
| Fri | 266 | 31.4% |
| Sat | 268 | 31.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 132 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 132 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 110 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 11 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 110 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 11 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 160 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 11 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 72 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 19.7% vs overall 24.2% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 46.2% vs overall 41.2% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 18.9% vs overall 24.2% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 36.4% vs overall 41.2% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 20.0% vs overall 24.2% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 40.0% vs overall 34.7% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 away outcome share 30.6% vs overall 34.7% |
| 25 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 11.1% vs overall 6.1% (deviation 5.0 pp) |
| 26 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 34.7% vs overall 41.2% |
| 27 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 37.5% vs overall 24.2% |
| 28 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 27.8% vs overall 34.7% |
| 29 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 30 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 31 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows) |
| 32 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=12 positions=1..12 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=12 positions=1..12 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=12 positions=1..12 teams=12 |
| 37 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=12 positions=1..12 teams=12 |
| 38 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=11 positions=1..11 teams=11 |
| 42 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=11 positions=1..11 teams=11 |
| 43 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=11 positions=1..11 teams=11 |
| 44 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=11 positions=1..11 teams=11 |
| 45 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=11 positions=1..11 teams=11 |
| 46 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=11 positions=1..11 teams=11 |
| 47 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=11 positions=1..11 teams=11 |
| 48 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=11 positions=1..11 teams=11 |
| 49 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=11 positions=1..11 teams=11 |
| 50 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 51 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 52 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 132, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 132, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 110, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 11, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 110, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 11, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 160, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 11, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 72, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 4.5, "overall_goalless_pct": 6.1, "deviation_pp": 1.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 19.7, "overall_share": 24.2}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 3.8, "overall_goalless_pct": 6.1, "deviation_pp": 2.3}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 46.2, "overall_share": 41.2}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 18.9, "overall_share": 24.2}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 36.4, "overall_share": 41.2}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 20.0, "overall_share": 24.2}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 40.0, "overall_share": 34.7}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "away", "season_share": 30.6, "overall_share": 34.7}`
- `25.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 11.1, "overall_goalless_pct": 6.1, "deviation_pp": 5.0}`
- `26.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 34.7, "overall_share": 41.2}`
- `27.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 37.5, "overall_share": 24.2}`
- `28.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 27.8, "overall_share": 34.7}`
- `29.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `30.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 26869, "distinct": 26864, "duplicates": 5}`
- `31.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 26869, "fgt_inconsistent": 310, "fgte_inconsistent": 310, "n_with_fgt": 24521}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `50.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `51.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `52.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
