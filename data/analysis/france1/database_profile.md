# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:51:12+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `france1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 167 |
| teams | 595 |
| team_aliases | 1190 |
| team_seasons | 2725 |
| matches | 40854 |
| standings | 8175 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `25`
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
| eng1 | League One | England | 7 | 3460 |
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1171 |
| finland1 | Veikkausliiga | Finland | 7 | 946 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2134 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `france1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-08-21 | 2021-05-23 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-06 | 2022-05-21 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-05 | 2023-06-03 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-11 | 2024-05-19 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-16 | 2025-05-17 |
| 2025-2026 | True | complete | 310 | 21 | 2025-08-15 | 2026-05-29 |
| 2026-2027 | True | in_progress | 72 | 18 | 2026-08-21 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 40854 | 40854 | 0 |
| matches (league_season_id, game_index) | 40854 | 40854 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 40854 | 40849 | 5 |
| team_seasons (league_season_id, team_id) | 2725 | 2725 | 0 |
| team_seasons api_name within a season | 2725 | 2725 | 0 |
| team_seasons api_slug within a season | 2725 | 2725 | 0 |
| standings (league_season_id, team_id, view) | 8175 | 8175 | 0 |
| team_aliases (form, value) | 1190 | 1190 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 595 | 595 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `40854`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 40854 | 0.0% |
| kickoff_time | 0 | 40854 | 0.0% |
| home_team_id | 0 | 40854 | 0.0% |
| away_team_id | 0 | 40854 | 0.0% |
| home_score | 0 | 40854 | 0.0% |
| away_score | 0 | 40854 | 0.0% |
| home_ht | 367 | 40487 | 0.9% |
| away_ht | 367 | 40487 | 0.9% |
| first_goal_time | 3449 | 37405 | 8.4% |
| first_goal_time_extra | 3449 | 37405 | 8.4% |
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
| Home | 905 | 42.4% |
| Draw | 527 | 24.7% |
| Away | 702 | 32.9% |
| Total | 2134 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6008 |
| Average goals per match | 2.815 |
| Home goals | 3241 (avg 1.519) |
| Away goals | 2767 (avg 1.297) |
| Home goal share | 53.9% |
| Goalless matches | 148 (6.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.4% | 25.0% | 37.6% | 1049 | 2.761 | 531 | 518 | 26 (6.8%) |
| 2021-2022 | 380 | 42.6% | 26.8% | 30.5% | 1067 | 2.808 | 601 | 466 | 24 (6.3%) |
| 2022-2023 | 380 | 42.9% | 24.2% | 32.9% | 1067 | 2.808 | 566 | 501 | 26 (6.8%) |
| 2023-2024 | 306 | 39.2% | 26.5% | 34.3% | 826 | 2.699 | 443 | 383 | 27 (8.8%) |
| 2024-2025 | 306 | 46.7% | 20.3% | 33.0% | 911 | 2.977 | 492 | 419 | 14 (4.6%) |
| 2025-2026 | 310 | 46.1% | 24.5% | 29.4% | 874 | 2.819 | 491 | 383 | 25 (8.1%) |
| 2026-2027 | 72 | 44.4% | 26.4% | 29.2% | 214 | 2.972 | 117 | 97 | 6 (8.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1986` of `2134` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 1986 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 30.05 |
| Median (p50) | 24.5 |
| p25 | 12.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 668 |
| 16-30 | 510 |
| 31-45 | 323 |
| 46-60 | 257 |
| 61-75 | 124 |
| 76-90 | 84 |
| 91-120 | 20 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `405`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 20 | 1..20 | 20 |
| 2022-2023 | goals | 20 | 1..20 | 20 |
| 2022-2023 | luck | 20 | 1..20 | 20 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 1..18 | 18 |
| 2024-2025 | luck | 18 | 1..18 | 18 |
| 2025-2026 | classic | 21 | 1..21 | 21 |
| 2025-2026 | goals | 21 | 1..21 | 21 |
| 2025-2026 | luck | 21 | 1..21 | 21 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 249 |
| 2-1 | 186 |
| 1-0 | 181 |
| 1-2 | 157 |
| 0-1 | 154 |
| 0-0 | 148 |
| 2-0 | 139 |
| 0-2 | 113 |
| 2-2 | 107 |
| 3-1 | 106 |
| 3-0 | 77 |
| 1-3 | 73 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 2 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1198 | 56.1% |
| Mon | 7 | 0.3% |
| Tue | 7 | 0.3% |
| Wed | 170 | 8.0% |
| Thu | 8 | 0.4% |
| Fri | 200 | 9.4% |
| Sat | 544 | 25.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 310 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 72 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 9 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.4% vs overall 42.4% |
| 11 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 37.6% vs overall 32.9% |
| 12 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 8.8% vs overall 6.9% (deviation 1.9 pp) |
| 13 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 4.6% vs overall 6.9% (deviation 2.3 pp) |
| 14 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 46.7% vs overall 42.4% |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 20.3% vs overall 24.7% |
| 16 | HIGH_SCORING_MATCHES | 18 match(es) with >= 8 total goals (extreme scorelines) |
| 17 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 18 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows) |
| 19 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 20 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 21 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
| 22 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 23 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=1..18 teams=18 |
| 24 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..18 teams=18 |
| 25 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 26 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 27 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
| 28 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 310, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 72, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `9.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.4, "overall_share": 42.4}`
- `11.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 37.6, "overall_share": 32.9}`
- `12.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 8.8, "overall_goalless_pct": 6.9, "deviation_pp": 1.9}`
- `13.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 4.6, "overall_goalless_pct": 6.9, "deviation_pp": 2.3}`
- `14.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 46.7, "overall_share": 42.4}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 20.3, "overall_share": 24.7}`
- `16.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 18, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `17.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 40854, "distinct": 40849, "duplicates": 5}`
- `18.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 40854, "fgt_inconsistent": 313, "fgte_inconsistent": 313, "n_with_fgt": 37405}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
