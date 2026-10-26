# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:28:26+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `china`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 77 |
| teams | 277 |
| team_aliases | 554 |
| team_seasons | 1252 |
| matches | 19483 |
| standings | 3756 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `11`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `china`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 112 | 16 | 2020-07-25 | 2020-09-28 |
| 2021 | False | complete | 112 | 16 | 2021-04-20 | 2021-08-15 |
| 2022 | False | complete | 306 | 18 | 2022-06-03 | 2022-12-31 |
| 2023 | False | complete | 240 | 16 | 2023-04-15 | 2023-11-04 |
| 2024 | False | complete | 240 | 16 | 2024-03-01 | 2024-11-02 |
| 2025 | True | complete | 240 | 16 | 2025-02-22 | 2025-11-22 |
| 2026 | True | in_progress | 232 | 16 | 2026-03-06 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 19483 | 19483 | 0 |
| matches (league_season_id, game_index) | 19483 | 19483 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 19483 | 19481 | 2 |
| team_seasons (league_season_id, team_id) | 1252 | 1252 | 0 |
| team_seasons api_name within a season | 1252 | 1252 | 0 |
| team_seasons api_slug within a season | 1252 | 1252 | 0 |
| standings (league_season_id, team_id, view) | 3756 | 3756 | 0 |
| team_aliases (form, value) | 554 | 554 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 277 | 277 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `19483`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 19483 | 0.0% |
| kickoff_time | 0 | 19483 | 0.0% |
| home_team_id | 0 | 19483 | 0.0% |
| away_team_id | 0 | 19483 | 0.0% |
| home_score | 0 | 19483 | 0.0% |
| away_score | 0 | 19483 | 0.0% |
| home_ht | 327 | 19156 | 1.7% |
| away_ht | 327 | 19156 | 1.7% |
| first_goal_time | 1878 | 17605 | 9.6% |
| first_goal_time_extra | 1878 | 17605 | 9.6% |
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
| Home | 660 | 44.5% |
| Draw | 364 | 24.6% |
| Away | 458 | 30.9% |
| Total | 1482 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 4414 |
| Average goals per match | 2.978 |
| Home goals | 2446 (avg 1.65) |
| Away goals | 1968 (avg 1.328) |
| Home goal share | 55.4% |
| Goalless matches | 89 (6.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 112 | 40.2% | 24.1% | 35.7% | 321 | 2.866 | 167 | 154 | 7 (6.2%) |
| 2021 | 112 | 48.2% | 26.8% | 25.0% | 301 | 2.688 | 163 | 138 | 13 (11.6%) |
| 2022 | 306 | 42.5% | 20.3% | 37.3% | 875 | 2.859 | 470 | 405 | 20 (6.5%) |
| 2023 | 240 | 44.2% | 27.9% | 27.9% | 666 | 2.775 | 372 | 294 | 14 (5.8%) |
| 2024 | 240 | 46.2% | 22.9% | 30.8% | 750 | 3.125 | 431 | 319 | 16 (6.7%) |
| 2025 | 240 | 46.7% | 25.8% | 27.5% | 771 | 3.212 | 432 | 339 | 9 (3.8%) |
| 2026 | 232 | 44.0% | 26.3% | 29.7% | 730 | 3.147 | 411 | 319 | 10 (4.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1384` of `1482` (93.4%)
| metric | value |
|---|---|
| First goals recorded | 1384 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.62 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 481 |
| 16-30 | 352 |
| 31-45 | 227 |
| 46-60 | 166 |
| 61-75 | 88 |
| 76-90 | 48 |
| 91-120 | 22 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `342`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 16 | 1..16 | 16 |
| 2020 | goals | 16 | 1..16 | 16 |
| 2020 | luck | 16 | 1..16 | 16 |
| 2021 | classic | 16 | 1..16 | 16 |
| 2021 | goals | 16 | 1..16 | 16 |
| 2021 | luck | 16 | 1..16 | 16 |
| 2022 | classic | 18 | 1..18 | 18 |
| 2022 | goals | 18 | 1..18 | 18 |
| 2022 | luck | 18 | 1..18 | 18 |
| 2023 | classic | 16 | 1..16 | 16 |
| 2023 | goals | 16 | 1..16 | 16 |
| 2023 | luck | 16 | 1..16 | 16 |
| 2024 | classic | 16 | 1..16 | 16 |
| 2024 | goals | 16 | 1..16 | 16 |
| 2024 | luck | 16 | 1..16 | 16 |
| 2025 | classic | 16 | 1..16 | 16 |
| 2025 | goals | 16 | 1..16 | 16 |
| 2025 | luck | 16 | 1..16 | 16 |
| 2026 | classic | 16 | 1..16 | 16 |
| 2026 | goals | 16 | 1..16 | 16 |
| 2026 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 173 |
| 2-1 | 133 |
| 1-0 | 124 |
| 0-1 | 104 |
| 1-2 | 96 |
| 2-0 | 94 |
| 0-0 | 89 |
| 2-2 | 79 |
| 3-1 | 68 |
| 3-0 | 58 |
| 0-2 | 55 |
| 1-3 | 45 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-1 | 9 | 2 |
| 7-2 | 9 | 1 |
| 4-5 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 332 | 22.4% |
| Mon | 101 | 6.8% |
| Tue | 136 | 9.2% |
| Wed | 144 | 9.7% |
| Thu | 87 | 5.9% |
| Fri | 260 | 17.5% |
| Sat | 422 | 28.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 112 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 112 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 240 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 16 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 232 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020 home outcome share 40.2% vs overall 44.5% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 35.7% vs overall 30.9% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 11.6% vs overall 6.0% (deviation 5.6 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021 away outcome share 25.0% vs overall 30.9% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2022 draw outcome share 20.3% vs overall 24.6% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2022 away outcome share 37.3% vs overall 30.9% |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 3.8% vs overall 6.0% (deviation 2.2 pp) |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 4.3% vs overall 6.0% (deviation 1.7 pp) |
| 24 | HIGH_SCORING_MATCHES | 15 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=305, fgte=305 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 112, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 112, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 240, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 16, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 232, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "home", "season_share": 40.2, "overall_share": 44.5}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 35.7, "overall_share": 30.9}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 11.6, "overall_goalless_pct": 6.0, "deviation_pp": 5.6}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "away", "season_share": 25.0, "overall_share": 30.9}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "draw", "season_share": 20.3, "overall_share": 24.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "away", "season_share": 37.3, "overall_share": 30.9}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 3.8, "overall_goalless_pct": 6.0, "deviation_pp": 2.2}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 4.3, "overall_goalless_pct": 6.0, "deviation_pp": 1.7}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 15, "threshold": 8, "examples": [{"scoreline": "8-1", "total_goals": 9, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 3}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 19483, "distinct": 19481, "duplicates": 2}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 19483, "fgt_inconsistent": 305, "fgte_inconsistent": 305, "n_with_fgt": 17605}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
