# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T01:54:08+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `belgium1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 7 |
| league_seasons | 42 |
| teams | 123 |
| team_aliases | 246 |
| team_seasons | 583 |
| matches | 7899 |
| standings | 1749 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `6`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1697 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `belgium1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 18 | 2020-08-08 | 2021-04-18 |
| 2021-2022 | False | complete | 306 | 18 | 2021-07-23 | 2022-04-10 |
| 2022-2023 | False | complete | 306 | 18 | 2022-07-22 | 2023-04-23 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-28 | 2024-03-17 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-26 | 2025-03-16 |
| 2025-2026 | True | complete | 321 | 20 | 2025-07-25 | 2026-05-31 |
| 2026-2027 | True | in_progress | 80 | 18 | 2026-08-07 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 7899 | 7899 | 0 |
| matches (league_season_id, game_index) | 7899 | 7899 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 7899 | 7897 | 2 |
| team_seasons (league_season_id, team_id) | 583 | 583 | 0 |
| team_seasons api_name within a season | 583 | 583 | 0 |
| team_seasons api_slug within a season | 583 | 583 | 0 |
| standings (league_season_id, team_id, view) | 1749 | 1749 | 0 |
| team_aliases (form, value) | 246 | 246 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 123 | 123 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `7899`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 7899 | 0.0% |
| kickoff_time | 0 | 7899 | 0.0% |
| home_team_id | 0 | 7899 | 0.0% |
| away_team_id | 0 | 7899 | 0.0% |
| home_score | 0 | 7899 | 0.0% |
| away_score | 0 | 7899 | 0.0% |
| home_ht | 19 | 7880 | 0.2% |
| away_ht | 19 | 7880 | 0.2% |
| first_goal_time | 602 | 7297 | 7.6% |
| first_goal_time_extra | 602 | 7297 | 7.6% |
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
| Home | 777 | 43.2% |
| Draw | 436 | 24.2% |
| Away | 586 | 32.6% |
| Total | 1799 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5179 |
| Average goals per match | 2.879 |
| Home goals | 2836 (avg 1.576) |
| Away goals | 2343 (avg 1.302) |
| Home goal share | 54.8% |
| Goalless matches | 103 (5.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 40.2% | 22.9% | 36.9% | 914 | 2.987 | 472 | 442 | 14 (4.6%) |
| 2021-2022 | 306 | 41.8% | 22.2% | 35.9% | 900 | 2.941 | 479 | 421 | 12 (3.9%) |
| 2022-2023 | 306 | 44.1% | 22.2% | 33.7% | 929 | 3.036 | 505 | 424 | 15 (4.9%) |
| 2023-2024 | 240 | 45.0% | 27.1% | 27.9% | 672 | 2.8 | 383 | 289 | 12 (5.0%) |
| 2024-2025 | 240 | 45.8% | 28.8% | 25.4% | 645 | 2.688 | 383 | 262 | 22 (9.2%) |
| 2025-2026 | 321 | 41.1% | 25.2% | 33.6% | 864 | 2.692 | 465 | 399 | 25 (7.8%) |
| 2026-2027 | 80 | 51.2% | 18.8% | 30.0% | 255 | 3.188 | 149 | 106 | 3 (3.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1690` of `1799` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 1690 |
| Min minute | 1 |
| Max minute | 100 |
| Mean minute | 30.49 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 568 |
| 16-30 | 392 |
| 31-45 | 317 |
| 46-60 | 209 |
| 61-75 | 104 |
| 76-90 | 86 |
| 91-120 | 14 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `372`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 18 | 1..18 | 18 |
| 2020-2021 | goals | 18 | 1..18 | 18 |
| 2020-2021 | luck | 18 | 1..18 | 18 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 212 |
| 2-1 | 155 |
| 1-0 | 138 |
| 0-1 | 135 |
| 2-0 | 129 |
| 1-2 | 129 |
| 0-0 | 103 |
| 2-2 | 99 |
| 0-2 | 89 |
| 3-0 | 86 |
| 1-3 | 67 |
| 3-1 | 66 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 4 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 1 |
| 2-7 | 9 | 1 |
| 7-1 | 8 | 1 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 791 | 44.0% |
| Mon | 37 | 2.1% |
| Tue | 46 | 2.6% |
| Wed | 59 | 3.3% |
| Thu | 34 | 1.9% |
| Fri | 186 | 10.3% |
| Sat | 646 | 35.9% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 321 matches, expected 380 |
| 12 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 80 matches, expected 380 |
| 13 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 14 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 36.9% vs overall 32.6% |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 3.9% vs overall 5.7% (deviation 1.8 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 27.9% vs overall 32.6% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 9.2% vs overall 5.7% (deviation 3.5 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 28.8% vs overall 24.2% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 25.4% vs overall 32.6% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 7.8% vs overall 5.7% (deviation 2.1 pp) |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.8% vs overall 5.7% (deviation 1.9 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 51.2% vs overall 43.2% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 18.8% vs overall 24.2% |
| 25 | HIGH_SCORING_MATCHES | 16 match(es) with >= 8 total goals (extreme scorelines) |
| 26 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 27 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=15, fgte=15 rows) |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 321, "expected": 380}`
- `12.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 80, "expected": 380}`
- `13.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `14.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 36.9, "overall_share": 32.6}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 3.9, "overall_goalless_pct": 5.7, "deviation_pp": 1.8}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 27.9, "overall_share": 32.6}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 9.2, "overall_goalless_pct": 5.7, "deviation_pp": 3.5}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 28.8, "overall_share": 24.2}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 25.4, "overall_share": 32.6}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 7.8, "overall_goalless_pct": 5.7, "deviation_pp": 2.1}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.8, "overall_goalless_pct": 5.7, "deviation_pp": 1.9}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 51.2, "overall_share": 43.2}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 18.8, "overall_share": 24.2}`
- `25.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 16, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 4}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 3}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `26.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 7899, "distinct": 7897, "duplicates": 2}`
- `27.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 7899, "fgt_inconsistent": 15, "fgte_inconsistent": 15, "n_with_fgt": 7297}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
