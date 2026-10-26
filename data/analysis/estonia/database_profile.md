# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:31:25+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `estonia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 146 |
| teams | 532 |
| team_aliases | 1064 |
| team_seasons | 2428 |
| matches | 36786 |
| standings | 7284 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `22`
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
| develop21 | Professional Development League | England | 1 | 61 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3455 |
| eng2 | League Two | England | 7 | 3466 |
| estonia | Meistriliiga | Estonia | 7 | 1166 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `estonia`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 147 | 10 | 2020-03-06 | 2020-12-06 |
| 2021 | False | complete | 134 | 10 | 2021-03-13 | 2021-12-01 |
| 2022 | False | complete | 180 | 10 | 2022-03-01 | 2022-11-12 |
| 2023 | False | complete | 180 | 10 | 2023-03-03 | 2023-11-11 |
| 2024 | False | complete | 180 | 10 | 2024-03-01 | 2024-11-09 |
| 2025 | True | complete | 180 | 10 | 2025-02-28 | 2025-11-08 |
| 2026 | True | in_progress | 165 | 10 | 2026-03-07 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 36786 | 36786 | 0 |
| matches (league_season_id, game_index) | 36786 | 36786 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 36786 | 36781 | 5 |
| team_seasons (league_season_id, team_id) | 2428 | 2428 | 0 |
| team_seasons api_name within a season | 2428 | 2428 | 0 |
| team_seasons api_slug within a season | 2428 | 2428 | 0 |
| standings (league_season_id, team_id, view) | 7284 | 7284 | 0 |
| team_aliases (form, value) | 1064 | 1064 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 532 | 532 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `36786`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 36786 | 0.0% |
| kickoff_time | 0 | 36786 | 0.0% |
| home_team_id | 0 | 36786 | 0.0% |
| away_team_id | 0 | 36786 | 0.0% |
| home_score | 0 | 36786 | 0.0% |
| away_score | 0 | 36786 | 0.0% |
| home_ht | 365 | 36421 | 1.0% |
| away_ht | 365 | 36421 | 1.0% |
| first_goal_time | 3177 | 33609 | 8.6% |
| first_goal_time_extra | 3177 | 33609 | 8.6% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 10 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 505 | 43.3% |
| Draw | 219 | 18.8% |
| Away | 442 | 37.9% |
| Total | 1166 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3529 |
| Average goals per match | 3.027 |
| Home goals | 1892 (avg 1.623) |
| Away goals | 1637 (avg 1.404) |
| Home goal share | 53.6% |
| Goalless matches | 57 (4.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 147 | 38.1% | 19.0% | 42.9% | 442 | 3.007 | 209 | 233 | 10 (6.8%) |
| 2021 | 134 | 45.5% | 16.4% | 38.1% | 455 | 3.396 | 246 | 209 | 5 (3.7%) |
| 2022 | 180 | 45.6% | 19.4% | 35.0% | 549 | 3.05 | 307 | 242 | 6 (3.3%) |
| 2023 | 180 | 37.2% | 27.8% | 35.0% | 458 | 2.544 | 244 | 214 | 17 (9.4%) |
| 2024 | 180 | 41.7% | 22.2% | 36.1% | 539 | 2.994 | 275 | 264 | 10 (5.6%) |
| 2025 | 180 | 46.7% | 13.3% | 40.0% | 572 | 3.178 | 313 | 259 | 4 (2.2%) |
| 2026 | 165 | 48.5% | 12.1% | 39.4% | 514 | 3.115 | 298 | 216 | 5 (3.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1109` of `1166` (95.1%)
| metric | value |
|---|---|
| First goals recorded | 1109 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 29.03 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 41.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 387 |
| 16-30 | 295 |
| 31-45 | 182 |
| 46-60 | 118 |
| 61-75 | 72 |
| 76-90 | 40 |
| 91-120 | 15 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `210`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 10 | 1..10 | 10 |
| 2020 | goals | 10 | 1..10 | 10 |
| 2020 | luck | 10 | 1..10 | 10 |
| 2021 | classic | 10 | 1..10 | 10 |
| 2021 | goals | 10 | 1..10 | 10 |
| 2021 | luck | 10 | 1..10 | 10 |
| 2022 | classic | 10 | 1..10 | 10 |
| 2022 | goals | 10 | 1..10 | 10 |
| 2022 | luck | 10 | 1..10 | 10 |
| 2023 | classic | 10 | 1..10 | 10 |
| 2023 | goals | 10 | 1..10 | 10 |
| 2023 | luck | 10 | 1..10 | 10 |
| 2024 | classic | 10 | 1..10 | 10 |
| 2024 | goals | 10 | 1..10 | 10 |
| 2024 | luck | 10 | 1..10 | 10 |
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 102 |
| 1-2 | 98 |
| 1-0 | 94 |
| 0-1 | 86 |
| 2-1 | 84 |
| 2-0 | 70 |
| 0-2 | 67 |
| 3-0 | 57 |
| 0-0 | 57 |
| 2-2 | 52 |
| 3-1 | 51 |
| 1-3 | 48 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-4 | 11 | 1 |
| 10-0 | 10 | 1 |
| 9-0 | 9 | 1 |
| 8-1 | 9 | 1 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 2-7 | 9 | 2 |
| 1-8 | 9 | 1 |
| 0-9 | 9 | 1 |
| 7-1 | 8 | 4 |
| 6-2 | 8 | 4 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |
| 1-7 | 8 | 3 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 367 | 31.5% |
| Mon | 5 | 0.4% |
| Tue | 85 | 7.3% |
| Wed | 147 | 12.6% |
| Thu | 13 | 1.1% |
| Fri | 117 | 10.0% |
| Sat | 432 | 37.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 147 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 134 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 180 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 180 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 180 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 165 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020 goalless share 6.8% vs overall 4.9% (deviation 1.9 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 home outcome share 38.1% vs overall 43.3% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 42.9% vs overall 37.9% |
| 19 | SEASON_AVG_GOALS_OUTLIER | Season 2021 avg goals 3.396 vs overall 3.027 (deviation 0.369) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 3.3% vs overall 4.9% (deviation 1.6 pp) |
| 21 | SEASON_AVG_GOALS_OUTLIER | Season 2023 avg goals 2.544 vs overall 3.027 (deviation 0.483) |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2023 goalless share 9.4% vs overall 4.9% (deviation 4.5 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2023 home outcome share 37.2% vs overall 43.3% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2023 draw outcome share 27.8% vs overall 18.8% |
| 25 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 2.2% vs overall 4.9% (deviation 2.7 pp) |
| 26 | OUTCOME_SHARE_OUTLIER | Season 2025 draw outcome share 13.3% vs overall 18.8% |
| 27 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 3.0% vs overall 4.9% (deviation 1.9 pp) |
| 28 | OUTCOME_SHARE_OUTLIER | Season 2026 home outcome share 48.5% vs overall 43.3% |
| 29 | OUTCOME_SHARE_OUTLIER | Season 2026 draw outcome share 12.1% vs overall 18.8% |
| 30 | HIGH_SCORING_MATCHES | 25 match(es) with >= 8 total goals (extreme scorelines) |
| 31 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 32 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows) |
| 33 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=10 positions=1..10 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=10 positions=1..10 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=10 positions=1..10 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=10 positions=1..10 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=10 positions=1..10 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=10 positions=1..10 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=10 positions=1..10 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=10 positions=1..10 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=10 positions=1..10 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=10 positions=1..10 teams=10 |
| 45 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=10 positions=1..10 teams=10 |
| 46 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=10 positions=1..10 teams=10 |
| 47 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=10 positions=1..10 teams=10 |
| 48 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 49 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 50 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 51 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 52 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 53 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 147, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 134, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 180, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 180, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 180, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 165, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020", "season_goalless_pct": 6.8, "overall_goalless_pct": 4.9, "deviation_pp": 1.9}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "home", "season_share": 38.1, "overall_share": 43.3}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 42.9, "overall_share": 37.9}`
- `19.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2021", "season_avg_goals": 3.396, "overall_avg_goals": 3.027, "deviation": 0.369}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 3.3, "overall_goalless_pct": 4.9, "deviation_pp": 1.6}`
- `21.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023", "season_avg_goals": 2.544, "overall_avg_goals": 3.027, "deviation": 0.483}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023", "season_goalless_pct": 9.4, "overall_goalless_pct": 4.9, "deviation_pp": 4.5}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "home", "season_share": 37.2, "overall_share": 43.3}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "draw", "season_share": 27.8, "overall_share": 18.8}`
- `25.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 2.2, "overall_goalless_pct": 4.9, "deviation_pp": 2.7}`
- `26.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025", "outcome": "draw", "season_share": 13.3, "overall_share": 18.8}`
- `27.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 3.0, "overall_goalless_pct": 4.9, "deviation_pp": 1.9}`
- `28.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "home", "season_share": 48.5, "overall_share": 43.3}`
- `29.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "draw", "season_share": 12.1, "overall_share": 18.8}`
- `30.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 25, "threshold": 8, "examples": [{"scoreline": "7-4", "total_goals": 11, "count": 1}, {"scoreline": "10-0", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 2}, {"scoreline": "1-8", "total_goals": 9, "count": 1}]}`
- `31.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 36786, "distinct": 36781, "duplicates": 5}`
- `32.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 36786, "fgt_inconsistent": 312, "fgte_inconsistent": 312, "n_with_fgt": 33609}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `50.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `51.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `52.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `53.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
