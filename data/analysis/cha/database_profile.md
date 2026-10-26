# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:28:09+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `cha`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 70 |
| teams | 248 |
| team_aliases | 496 |
| team_seasons | 1138 |
| matches | 18001 |
| standings | 3414 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `10`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `cha`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 552 | 24 | 2020-09-11 | 2021-05-08 |
| 2021-2022 | False | complete | 552 | 24 | 2021-08-06 | 2022-05-07 |
| 2022-2023 | False | complete | 552 | 24 | 2022-07-29 | 2023-05-08 |
| 2023-2024 | False | complete | 552 | 24 | 2023-08-04 | 2024-05-04 |
| 2024-2025 | False | complete | 552 | 24 | 2024-08-09 | 2025-05-03 |
| 2025-2026 | True | complete | 559 | 24 | 2025-08-08 | 2026-05-23 |
| 2026-2027 | True | in_progress | 144 | 24 | 2026-08-14 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 18001 | 18001 | 0 |
| matches (league_season_id, game_index) | 18001 | 18001 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 18001 | 17999 | 2 |
| team_seasons (league_season_id, team_id) | 1138 | 1138 | 0 |
| team_seasons api_name within a season | 1138 | 1138 | 0 |
| team_seasons api_slug within a season | 1138 | 1138 | 0 |
| standings (league_season_id, team_id, view) | 3414 | 3414 | 0 |
| team_aliases (form, value) | 496 | 496 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 248 | 248 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `18001`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 18001 | 0.0% |
| kickoff_time | 0 | 18001 | 0.0% |
| home_team_id | 0 | 18001 | 0.0% |
| away_team_id | 0 | 18001 | 0.0% |
| home_score | 0 | 18001 | 0.0% |
| away_score | 0 | 18001 | 0.0% |
| home_ht | 318 | 17683 | 1.8% |
| away_ht | 318 | 17683 | 1.8% |
| first_goal_time | 1780 | 16221 | 9.9% |
| first_goal_time_extra | 1780 | 16221 | 9.9% |
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
| Home | 1490 | 43.0% |
| Draw | 901 | 26.0% |
| Away | 1072 | 31.0% |
| Total | 3463 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 8695 |
| Average goals per match | 2.511 |
| Home goals | 4820 (avg 1.392) |
| Away goals | 3875 (avg 1.119) |
| Home goal share | 55.4% |
| Goalless matches | 270 (7.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 552 | 41.1% | 25.2% | 33.7% | 1274 | 2.308 | 691 | 583 | 53 (9.6%) |
| 2021-2022 | 552 | 44.6% | 25.2% | 30.3% | 1385 | 2.509 | 781 | 604 | 44 (8.0%) |
| 2022-2023 | 552 | 41.1% | 27.0% | 31.9% | 1342 | 2.431 | 731 | 611 | 48 (8.7%) |
| 2023-2024 | 552 | 44.6% | 23.4% | 32.1% | 1480 | 2.681 | 818 | 662 | 35 (6.3%) |
| 2024-2025 | 552 | 45.8% | 28.3% | 25.9% | 1353 | 2.451 | 792 | 561 | 44 (8.0%) |
| 2025-2026 | 559 | 41.7% | 26.7% | 31.7% | 1445 | 2.585 | 777 | 668 | 37 (6.6%) |
| 2026-2027 | 144 | 40.3% | 27.8% | 31.9% | 416 | 2.889 | 230 | 186 | 9 (6.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `3192` of `3463` (92.2%)
| metric | value |
|---|---|
| First goals recorded | 3192 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 31.77 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 1026 |
| 16-30 | 762 |
| 31-45 | 510 |
| 46-60 | 451 |
| 61-75 | 241 |
| 76-90 | 162 |
| 91-120 | 40 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `504`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 24 | 1..24 | 24 |
| 2020-2021 | goals | 24 | 1..24 | 24 |
| 2020-2021 | luck | 24 | 1..24 | 24 |
| 2021-2022 | classic | 24 | 1..24 | 24 |
| 2021-2022 | goals | 24 | 1..24 | 24 |
| 2021-2022 | luck | 24 | 1..24 | 24 |
| 2022-2023 | classic | 24 | 1..24 | 24 |
| 2022-2023 | goals | 24 | 1..24 | 24 |
| 2022-2023 | luck | 24 | 1..24 | 24 |
| 2023-2024 | classic | 24 | 1..24 | 24 |
| 2023-2024 | goals | 24 | 1..24 | 24 |
| 2023-2024 | luck | 24 | 1..24 | 24 |
| 2024-2025 | classic | 24 | 1..24 | 24 |
| 2024-2025 | goals | 24 | 1..24 | 24 |
| 2024-2025 | luck | 24 | 1..24 | 24 |
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 444 |
| 1-0 | 379 |
| 2-1 | 335 |
| 0-1 | 316 |
| 1-2 | 274 |
| 0-0 | 270 |
| 2-0 | 250 |
| 0-2 | 176 |
| 2-2 | 159 |
| 3-0 | 136 |
| 3-1 | 131 |
| 1-3 | 93 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 4 |
| 5-3 | 8 | 4 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 154 | 4.4% |
| Mon | 170 | 4.9% |
| Tue | 527 | 15.2% |
| Wed | 368 | 10.6% |
| Thu | 40 | 1.2% |
| Fri | 258 | 7.5% |
| Sat | 1946 | 56.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 552 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 552 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 24 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 552 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 24 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 552 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 24 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 552 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 24 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 559 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 144 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 9.6% vs overall 7.8% (deviation 1.8 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 25.9% vs overall 31.0% |
| 18 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.889 vs overall 2.511 (deviation 0.378) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.2% vs overall 7.8% (deviation 1.6 pp) |
| 20 | HIGH_SCORING_MATCHES | 17 match(es) with >= 8 total goals (extreme scorelines) |
| 21 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 22 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=296, fgte=296 rows) |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=24 positions=1..24 teams=24 |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=24 positions=1..24 teams=24 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=24 positions=1..24 teams=24 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=24 positions=1..24 teams=24 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=24 positions=1..24 teams=24 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=24 positions=1..24 teams=24 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 35 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 38 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 41 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 552, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 552, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 24, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 552, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 24, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 552, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 24, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 552, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 24, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 559, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 144, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 9.6, "overall_goalless_pct": 7.8, "deviation_pp": 1.8}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 25.9, "overall_share": 31.0}`
- `18.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.889, "overall_avg_goals": 2.511, "deviation": 0.378}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.2, "overall_goalless_pct": 7.8, "deviation_pp": 1.6}`
- `20.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 17, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 4}, {"scoreline": "5-3", "total_goals": 8, "count": 4}, {"scoreline": "4-4", "total_goals": 8, "count": 3}, {"scoreline": "3-5", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `21.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 18001, "distinct": 17999, "duplicates": 2}`
- `22.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 18001, "fgt_inconsistent": 296, "fgte_inconsistent": 296, "n_with_fgt": 16221}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
