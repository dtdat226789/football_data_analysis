# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:48:42+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany-north`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 188 |
| teams | 722 |
| team_aliases | 1444 |
| team_seasons | 3173 |
| matches | 46644 |
| standings | 9519 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `28`
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
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 925 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 61 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3455 |
| eng2 | League Two | England | 7 | 3466 |
| estonia | Meistriliiga | Estonia | 7 | 1167 |
| finland1 | Veikkausliiga | Finland | 7 | 945 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2133 |
| france2 | Ligue 2 | France | 7 | 2224 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1699 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany-north`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 98 | 22 | 2020-09-04 | 2020-11-01 |
| 2021-2022 | False | complete | 200 | 21 | 2021-08-13 | 2022-02-27 |
| 2022-2023 | False | complete | 342 | 19 | 2022-07-30 | 2023-05-27 |
| 2023-2024 | False | complete | 306 | 18 | 2023-07-28 | 2024-05-19 |
| 2024-2025 | False | complete | 306 | 18 | 2024-07-26 | 2025-05-18 |
| 2025-2026 | True | complete | 317 | 19 | 2025-07-25 | 2026-05-16 |
| 2026-2027 | True | in_progress | 130 | 19 | 2026-07-31 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 46644 | 46644 | 0 |
| matches (league_season_id, game_index) | 46644 | 46644 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 46644 | 46634 | 10 |
| team_seasons (league_season_id, team_id) | 3173 | 3173 | 0 |
| team_seasons api_name within a season | 3173 | 3173 | 0 |
| team_seasons api_slug within a season | 3173 | 3173 | 0 |
| standings (league_season_id, team_id, view) | 9519 | 9519 | 0 |
| team_aliases (form, value) | 1444 | 1444 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 722 | 722 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `46644`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 46644 | 0.0% |
| kickoff_time | 0 | 46644 | 0.0% |
| home_team_id | 0 | 46644 | 0.0% |
| away_team_id | 0 | 46644 | 0.0% |
| home_score | 0 | 46644 | 0.0% |
| away_score | 0 | 46644 | 0.0% |
| home_ht | 381 | 46263 | 0.8% |
| away_ht | 381 | 46263 | 0.8% |
| first_goal_time | 3944 | 42700 | 8.5% |
| first_goal_time_extra | 3944 | 42700 | 8.5% |
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
| Home | 726 | 42.7% |
| Draw | 383 | 22.5% |
| Away | 590 | 34.7% |
| Total | 1699 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5641 |
| Average goals per match | 3.32 |
| Home goals | 3013 (avg 1.773) |
| Away goals | 2628 (avg 1.547) |
| Home goal share | 53.4% |
| Goalless matches | 78 (4.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 98 | 44.9% | 13.3% | 41.8% | 279 | 2.847 | 145 | 134 | 2 (2.0%) |
| 2021-2022 | 200 | 42.0% | 25.5% | 32.5% | 605 | 3.025 | 329 | 276 | 13 (6.5%) |
| 2022-2023 | 342 | 44.4% | 22.8% | 32.7% | 1101 | 3.219 | 595 | 506 | 21 (6.1%) |
| 2023-2024 | 306 | 41.8% | 24.5% | 33.7% | 1014 | 3.314 | 545 | 469 | 18 (5.9%) |
| 2024-2025 | 306 | 41.5% | 22.9% | 35.6% | 984 | 3.216 | 514 | 470 | 13 (4.2%) |
| 2025-2026 | 317 | 42.6% | 21.8% | 35.6% | 1152 | 3.634 | 611 | 541 | 8 (2.5%) |
| 2026-2027 | 130 | 43.1% | 20.8% | 36.2% | 506 | 3.892 | 274 | 232 | 3 (2.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1618` of `1699` (95.2%)
| metric | value |
|---|---|
| First goals recorded | 1618 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 27.43 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 41.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 626 |
| 16-30 | 391 |
| 31-45 | 272 |
| 46-60 | 187 |
| 61-75 | 71 |
| 76-90 | 60 |
| 91-120 | 11 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `408`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 22 | 1..24 | 22 |
| 2020-2021 | goals | 22 | 3..26 | 22 |
| 2020-2021 | luck | 22 | 1..27 | 22 |
| 2021-2022 | classic | 21 | 1..22 | 21 |
| 2021-2022 | goals | 21 | 5..29 | 21 |
| 2021-2022 | luck | 21 | 1..32 | 21 |
| 2022-2023 | classic | 19 | 1..20 | 19 |
| 2022-2023 | goals | 19 | 7..31 | 19 |
| 2022-2023 | luck | 19 | 1..38 | 19 |
| 2023-2024 | classic | 18 | 1..39 | 18 |
| 2023-2024 | goals | 18 | 19..43 | 18 |
| 2023-2024 | luck | 18 | 1..51 | 18 |
| 2024-2025 | classic | 18 | 1..19 | 18 |
| 2024-2025 | goals | 18 | 7..29 | 18 |
| 2024-2025 | luck | 18 | 1..36 | 18 |
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 19 | 1..19 | 19 |
| 2026-2027 | goals | 19 | 1..19 | 19 |
| 2026-2027 | luck | 19 | 1..19 | 19 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 175 |
| 2-1 | 118 |
| 2-0 | 102 |
| 1-0 | 99 |
| 2-2 | 99 |
| 0-1 | 97 |
| 1-2 | 97 |
| 3-1 | 86 |
| 0-0 | 78 |
| 1-3 | 75 |
| 0-2 | 71 |
| 0-3 | 66 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-2 | 11 | 1 |
| 6-5 | 11 | 1 |
| 5-6 | 11 | 1 |
| 8-2 | 10 | 1 |
| 7-3 | 10 | 1 |
| 6-4 | 10 | 1 |
| 1-9 | 10 | 1 |
| 9-0 | 9 | 1 |
| 8-1 | 9 | 2 |
| 7-2 | 9 | 4 |
| 5-4 | 9 | 1 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 2 |
| 7-1 | 8 | 3 |
| 6-2 | 8 | 6 |
| 5-3 | 8 | 5 |
| 4-4 | 8 | 7 |
| 3-5 | 8 | 5 |
| 2-6 | 8 | 3 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 617 | 36.3% |
| Mon | 13 | 0.8% |
| Tue | 27 | 1.6% |
| Wed | 193 | 11.4% |
| Thu | 23 | 1.4% |
| Fri | 236 | 13.9% |
| Sat | 590 | 34.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 98 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 22 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 200 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 21 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 342 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 19 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 317 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 130 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 19 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | SEASON_AVG_GOALS_OUTLIER | Season 2020-2021 avg goals 2.847 vs overall 3.32 (deviation 0.473) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 2.0% vs overall 4.6% (deviation 2.6 pp) |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 13.3% vs overall 22.5% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 41.8% vs overall 34.7% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 6.5% vs overall 4.6% (deviation 1.9 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 2.5% vs overall 4.6% (deviation 2.1 pp) |
| 22 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.892 vs overall 3.32 (deviation 0.572) |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.3% vs overall 4.6% (deviation 2.3 pp) |
| 24 | HIGH_SCORING_MATCHES | 49 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=326, fgte=326 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=22 positions=1..24 teams=22 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=22 positions=3..26 teams=22 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=22 positions=1..27 teams=22 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=21 positions=1..22 teams=21 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=21 positions=5..29 teams=21 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=21 positions=1..32 teams=21 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=19 positions=1..20 teams=19 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=19 positions=7..31 teams=19 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=19 positions=1..38 teams=19 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..39 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=19..43 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..51 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..19 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=7..29 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..36 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=19 positions=1..19 teams=19 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=19 positions=1..19 teams=19 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=19 positions=1..19 teams=19 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 98, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 22, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 200, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 21, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 342, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 19, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 317, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 130, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 19, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2020-2021", "season_avg_goals": 2.847, "overall_avg_goals": 3.32, "deviation": 0.473}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 2.0, "overall_goalless_pct": 4.6, "deviation_pp": 2.6}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 13.3, "overall_share": 22.5}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 41.8, "overall_share": 34.7}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 6.5, "overall_goalless_pct": 4.6, "deviation_pp": 1.9}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 2.5, "overall_goalless_pct": 4.6, "deviation_pp": 2.1}`
- `22.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.892, "overall_avg_goals": 3.32, "deviation": 0.572}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.3, "overall_goalless_pct": 4.6, "deviation_pp": 2.3}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 49, "threshold": 8, "examples": [{"scoreline": "9-2", "total_goals": 11, "count": 1}, {"scoreline": "6-5", "total_goals": 11, "count": 1}, {"scoreline": "5-6", "total_goals": 11, "count": 1}, {"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "1-9", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 46644, "distinct": 46634, "duplicates": 10}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 46644, "fgt_inconsistent": 326, "fgte_inconsistent": 326, "n_with_fgt": 42700}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 24, "distinct_teams": 22}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 22, "min_pos": 3, "max_pos": 26, "distinct_teams": 22}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 27, "distinct_teams": 22}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 22, "distinct_teams": 21}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 21, "min_pos": 5, "max_pos": 29, "distinct_teams": 21}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 32, "distinct_teams": 21}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 20, "distinct_teams": 19}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 19, "min_pos": 7, "max_pos": 31, "distinct_teams": 19}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 38, "distinct_teams": 19}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 39, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 19, "max_pos": 43, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 51, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 7, "max_pos": 29, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 36, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
