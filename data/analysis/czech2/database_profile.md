# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:47:33+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `czech2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 91 |
| teams | 317 |
| team_aliases | 634 |
| team_seasons | 1478 |
| matches | 22617 |
| standings | 4434 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `13`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `czech2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 182 | 14 | 2020-08-21 | 2021-05-30 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-23 | 2022-05-14 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-29 | 2023-05-28 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-21 | 2024-05-25 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-19 | 2025-05-25 |
| 2025-2026 | True | complete | 240 | 16 | 2025-07-18 | 2026-05-23 |
| 2026-2027 | True | in_progress | 96 | 16 | 2026-07-24 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 22617 | 22617 | 0 |
| matches (league_season_id, game_index) | 22617 | 22617 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 22617 | 22615 | 2 |
| team_seasons (league_season_id, team_id) | 1478 | 1478 | 0 |
| team_seasons api_name within a season | 1478 | 1478 | 0 |
| team_seasons api_slug within a season | 1478 | 1478 | 0 |
| standings (league_season_id, team_id, view) | 4434 | 4434 | 0 |
| team_aliases (form, value) | 634 | 634 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 317 | 317 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `22617`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 22617 | 0.0% |
| kickoff_time | 0 | 22617 | 0.0% |
| home_team_id | 0 | 22617 | 0.0% |
| away_team_id | 0 | 22617 | 0.0% |
| home_score | 0 | 22617 | 0.0% |
| away_score | 0 | 22617 | 0.0% |
| home_ht | 328 | 22289 | 1.5% |
| away_ht | 328 | 22289 | 1.5% |
| first_goal_time | 2103 | 20514 | 9.3% |
| first_goal_time_extra | 2103 | 20514 | 9.3% |
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
| Home | 653 | 44.2% |
| Draw | 390 | 26.4% |
| Away | 435 | 29.4% |
| Total | 1478 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4022 |
| Average goals per match | 2.721 |
| Home goals | 2267 (avg 1.534) |
| Away goals | 1755 (avg 1.187) |
| Home goal share | 56.4% |
| Goalless matches | 102 (6.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 182 | 37.4% | 25.8% | 36.8% | 473 | 2.599 | 244 | 229 | 12 (6.6%) |
| 2021-2022 | 240 | 47.9% | 25.4% | 26.7% | 651 | 2.712 | 378 | 273 | 19 (7.9%) |
| 2022-2023 | 240 | 47.1% | 27.1% | 25.8% | 666 | 2.775 | 398 | 268 | 13 (5.4%) |
| 2023-2024 | 240 | 46.2% | 25.4% | 28.3% | 687 | 2.862 | 390 | 297 | 17 (7.1%) |
| 2024-2025 | 240 | 40.4% | 31.2% | 28.3% | 605 | 2.521 | 333 | 272 | 23 (9.6%) |
| 2025-2026 | 240 | 46.2% | 20.8% | 32.9% | 643 | 2.679 | 364 | 279 | 14 (5.8%) |
| 2026-2027 | 96 | 39.6% | 32.3% | 28.1% | 297 | 3.094 | 160 | 137 | 4 (4.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1376` of `1478` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 1376 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 30.22 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 446 |
| 16-30 | 362 |
| 31-45 | 229 |
| 46-60 | 169 |
| 61-75 | 92 |
| 76-90 | 66 |
| 91-120 | 12 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `330`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 14 | 1..14 | 14 |
| 2020-2021 | goals | 14 | 1..14 | 14 |
| 2020-2021 | luck | 14 | 1..14 | 14 |
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
| 1-1 | 174 |
| 1-0 | 155 |
| 2-1 | 135 |
| 0-1 | 117 |
| 1-2 | 109 |
| 0-0 | 102 |
| 2-0 | 95 |
| 2-2 | 94 |
| 0-2 | 72 |
| 3-1 | 66 |
| 3-0 | 55 |
| 1-3 | 38 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 3 |
| 6-3 | 9 | 2 |
| 4-5 | 9 | 1 |
| 2-7 | 9 | 1 |
| 6-2 | 8 | 3 |
| 5-3 | 8 | 2 |
| 3-5 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 413 | 27.9% |
| Mon | 41 | 2.8% |
| Tue | 20 | 1.4% |
| Wed | 171 | 11.6% |
| Thu | 6 | 0.4% |
| Fri | 279 | 18.9% |
| Sat | 548 | 37.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 182 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 14 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 96 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.4% vs overall 44.2% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 36.8% vs overall 29.4% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 9.6% vs overall 6.9% (deviation 2.7 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 31.2% vs overall 26.4% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 20.8% vs overall 26.4% |
| 21 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.094 vs overall 2.721 (deviation 0.373) |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.2% vs overall 6.9% (deviation 2.7 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 39.6% vs overall 44.2% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 32.3% vs overall 26.4% |
| 25 | HIGH_SCORING_MATCHES | 14 match(es) with >= 8 total goals (extreme scorelines) |
| 26 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 27 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=306, fgte=306 rows) |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=14 positions=1..14 teams=14 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=14 positions=1..14 teams=14 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=14 positions=1..14 teams=14 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 182, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 14, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 96, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.4, "overall_share": 44.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 36.8, "overall_share": 29.4}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 9.6, "overall_goalless_pct": 6.9, "deviation_pp": 2.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 31.2, "overall_share": 26.4}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 20.8, "overall_share": 26.4}`
- `21.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.094, "overall_avg_goals": 2.721, "deviation": 0.373}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.2, "overall_goalless_pct": 6.9, "deviation_pp": 2.7}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 39.6, "overall_share": 44.2}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 32.3, "overall_share": 26.4}`
- `25.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 14, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 3}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 3}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 2}]}`
- `26.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 22617, "distinct": 22615, "duplicates": 2}`
- `27.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 22617, "fgt_inconsistent": 306, "fgte_inconsistent": 306, "n_with_fgt": 20514}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
