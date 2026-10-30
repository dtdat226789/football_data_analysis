# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:49:16+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `egypt`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 125 |
| teams | 474 |
| team_aliases | 948 |
| team_seasons | 2022 |
| matches | 28742 |
| standings | 6066 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `19`
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
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1089 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1423 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1771 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `egypt`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 306 | 53 | 2020-12-11 | 2021-08-28 |
| 2021-2022 | False | complete | 306 | 18 | 2021-10-25 | 2022-08-30 |
| 2022-2023 | False | complete | 306 | 18 | 2022-10-18 | 2023-07-26 |
| 2023-2024 | False | complete | 306 | 18 | 2023-09-18 | 2024-08-18 |
| 2024-2025 | False | complete | 153 | 18 | 2024-10-30 | 2025-03-05 |
| 2025-2026 | True | complete | 322 | 21 | 2025-08-08 | 2026-05-29 |
| 2026-2027 | True | in_progress | 72 | 20 | 2026-08-21 | 2026-10-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 28742 | 28742 | 0 |
| matches (league_season_id, game_index) | 28742 | 28742 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 28742 | 28737 | 5 |
| team_seasons (league_season_id, team_id) | 2022 | 2022 | 0 |
| team_seasons api_name within a season | 2022 | 2022 | 0 |
| team_seasons api_slug within a season | 2022 | 2022 | 0 |
| standings (league_season_id, team_id, view) | 6066 | 6066 | 0 |
| team_aliases (form, value) | 948 | 948 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 474 | 474 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `28742`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 28742 | 0.0% |
| kickoff_time | 0 | 28742 | 0.0% |
| home_team_id | 0 | 28742 | 0.0% |
| away_team_id | 0 | 28742 | 0.0% |
| home_score | 0 | 28742 | 0.0% |
| away_score | 0 | 28742 | 0.0% |
| home_ht | 342 | 28400 | 1.2% |
| away_ht | 342 | 28400 | 1.2% |
| first_goal_time | 2593 | 26149 | 9.0% |
| first_goal_time_extra | 2593 | 26149 | 9.0% |
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
| Home | 635 | 35.9% |
| Draw | 597 | 33.7% |
| Away | 539 | 30.4% |
| Total | 1771 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3960 |
| Average goals per match | 2.236 |
| Home goals | 2065 (avg 1.166) |
| Away goals | 1895 (avg 1.07) |
| Home goal share | 52.1% |
| Goalless matches | 239 (13.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 306 | 31.0% | 36.6% | 32.4% | 765 | 2.5 | 383 | 382 | 32 (10.5%) |
| 2021-2022 | 306 | 36.9% | 34.3% | 28.8% | 673 | 2.199 | 356 | 317 | 42 (13.7%) |
| 2022-2023 | 306 | 38.6% | 33.3% | 28.1% | 657 | 2.147 | 353 | 304 | 52 (17.0%) |
| 2023-2024 | 306 | 37.6% | 30.1% | 32.4% | 730 | 2.386 | 389 | 341 | 33 (10.8%) |
| 2024-2025 | 153 | 37.3% | 30.7% | 32.0% | 315 | 2.059 | 166 | 149 | 24 (15.7%) |
| 2025-2026 | 322 | 33.9% | 37.9% | 28.3% | 651 | 2.022 | 336 | 315 | 51 (15.8%) |
| 2026-2027 | 72 | 38.9% | 23.6% | 37.5% | 169 | 2.347 | 82 | 87 | 5 (6.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1530` of `1771` (86.4%)
| metric | value |
|---|---|
| First goals recorded | 1530 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 35.18 |
| Median (p50) | 31.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 413 |
| 16-30 | 345 |
| 31-45 | 277 |
| 46-60 | 225 |
| 61-75 | 146 |
| 76-90 | 91 |
| 91-120 | 33 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `498`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 53 | 1..53 | 53 |
| 2020-2021 | goals | 53 | 1..53 | 53 |
| 2020-2021 | luck | 53 | 1..53 | 53 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 1..18 | 18 |
| 2024-2025 | luck | 18 | 1..18 | 18 |
| 2025-2026 | classic | 21 | 1..21 | 21 |
| 2025-2026 | goals | 21 | 1..21 | 21 |
| 2025-2026 | luck | 21 | 1..21 | 21 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 258 |
| 0-0 | 239 |
| 1-0 | 213 |
| 0-1 | 168 |
| 2-1 | 133 |
| 1-2 | 131 |
| 0-2 | 102 |
| 2-0 | 92 |
| 2-2 | 91 |
| 3-0 | 49 |
| 3-2 | 45 |
| 3-1 | 40 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-4 | 8 | 2 |
| 3-5 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 235 | 13.3% |
| Mon | 255 | 14.4% |
| Tue | 269 | 15.2% |
| Wed | 261 | 14.7% |
| Thu | 248 | 14.0% |
| Fri | 269 | 15.2% |
| Sat | 234 | 13.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 53 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 153 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 322 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 72 matches, expected 380 |
| 14 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 10.5% vs overall 13.5% (deviation 3.0 pp) |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 31.0% vs overall 35.9% |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 17.0% vs overall 13.5% (deviation 3.5 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 10.8% vs overall 13.5% (deviation 2.7 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 15.7% vs overall 13.5% (deviation 2.2 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 15.8% vs overall 13.5% (deviation 2.3 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 37.9% vs overall 33.7% |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.9% vs overall 13.5% (deviation 6.6 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 23.6% vs overall 33.7% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 37.5% vs overall 30.4% |
| 25 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 26 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 27 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=312, fgte=312 rows) |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=53 positions=1..53 teams=53 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=53 positions=1..53 teams=53 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=53 positions=1..53 teams=53 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 53, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 153, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 322, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 72, "expected": 380}`
- `14.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 10.5, "overall_goalless_pct": 13.5, "deviation_pp": 3.0}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 31.0, "overall_share": 35.9}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 17.0, "overall_goalless_pct": 13.5, "deviation_pp": 3.5}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 10.8, "overall_goalless_pct": 13.5, "deviation_pp": 2.7}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 15.7, "overall_goalless_pct": 13.5, "deviation_pp": 2.2}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 15.8, "overall_goalless_pct": 13.5, "deviation_pp": 2.3}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 37.9, "overall_share": 33.7}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.9, "overall_goalless_pct": 13.5, "deviation_pp": 6.6}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 23.6, "overall_share": 33.7}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 37.5, "overall_share": 30.4}`
- `25.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 3}]}`
- `26.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 28742, "distinct": 28737, "duplicates": 5}`
- `27.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 28742, "fgt_inconsistent": 312, "fgte_inconsistent": 312, "n_with_fgt": 26149}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 53, "min_pos": 1, "max_pos": 53, "distinct_teams": 53}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 53, "min_pos": 1, "max_pos": 53, "distinct_teams": 53}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 53, "min_pos": 1, "max_pos": 53, "distinct_teams": 53}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
