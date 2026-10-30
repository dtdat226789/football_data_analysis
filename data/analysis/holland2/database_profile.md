# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:54:35+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `holland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 237 |
| teams | 898 |
| team_aliases | 1796 |
| team_seasons | 4090 |
| matches | 60076 |
| standings | 12270 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `35`
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
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1700 |
| germany1 | Bundesliga | Germany | 7 | 1690 |
| germany2 | 2. Bundesliga | Germany | 7 | 1921 |
| germany3 | 3. Liga | Germany | 7 | 2383 |
| greece1 | Super League | Greece | 7 | 1211 |
| greece2 | Super League 2 | Greece | 7 | 1836 |
| holland1 | Eredivisie | Netherlands | 7 | 1941 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `holland2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-08-28 | 2021-05-12 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-06 | 2022-05-06 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-05 | 2023-05-19 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-11 | 2024-05-10 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-09 | 2025-05-09 |
| 2025-2026 | True | complete | 392 | 21 | 2025-08-08 | 2026-05-23 |
| 2026-2027 | True | in_progress | 120 | 20 | 2026-08-07 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 60076 | 60076 | 0 |
| matches (league_season_id, game_index) | 60076 | 60076 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 60076 | 60066 | 10 |
| team_seasons (league_season_id, team_id) | 4090 | 4090 | 0 |
| team_seasons api_name within a season | 4090 | 4090 | 0 |
| team_seasons api_slug within a season | 4090 | 4090 | 0 |
| standings (league_season_id, team_id, view) | 12270 | 12270 | 0 |
| team_aliases (form, value) | 1796 | 1796 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 898 | 898 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `60076`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 60076 | 0.0% |
| kickoff_time | 0 | 60076 | 0.0% |
| home_team_id | 0 | 60076 | 0.0% |
| away_team_id | 0 | 60076 | 0.0% |
| home_score | 0 | 60076 | 0.0% |
| away_score | 0 | 60076 | 0.0% |
| home_ht | 393 | 59683 | 0.7% |
| away_ht | 393 | 59683 | 0.7% |
| first_goal_time | 4816 | 55260 | 8.0% |
| first_goal_time_extra | 4816 | 55260 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 1079 | 44.7% |
| Draw | 530 | 22.0% |
| Away | 803 | 33.3% |
| Total | 2412 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 7543 |
| Average goals per match | 3.127 |
| Home goals | 4160 (avg 1.725) |
| Away goals | 3383 (avg 1.403) |
| Home goal share | 55.2% |
| Goalless matches | 112 (4.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 43.2% | 20.5% | 36.3% | 1228 | 3.232 | 667 | 561 | 19 (5.0%) |
| 2021-2022 | 380 | 42.9% | 21.6% | 35.5% | 1165 | 3.066 | 619 | 546 | 19 (5.0%) |
| 2022-2023 | 380 | 46.6% | 20.8% | 32.6% | 1166 | 3.068 | 668 | 498 | 13 (3.4%) |
| 2023-2024 | 380 | 45.5% | 24.7% | 29.7% | 1159 | 3.05 | 644 | 515 | 22 (5.8%) |
| 2024-2025 | 380 | 45.8% | 23.2% | 31.1% | 1146 | 3.016 | 645 | 501 | 23 (6.1%) |
| 2025-2026 | 392 | 42.6% | 21.7% | 35.7% | 1248 | 3.184 | 678 | 570 | 14 (3.6%) |
| 2026-2027 | 120 | 50.8% | 20.0% | 29.2% | 431 | 3.592 | 239 | 192 | 2 (1.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2300` of `2412` (95.4%)
| metric | value |
|---|---|
| First goals recorded | 2300 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 28.26 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 41.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 856 |
| 16-30 | 592 |
| 31-45 | 352 |
| 46-60 | 262 |
| 61-75 | 123 |
| 76-90 | 84 |
| 91-120 | 31 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `423`
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
| 2023-2024 | classic | 20 | 1..20 | 20 |
| 2023-2024 | goals | 20 | 1..20 | 20 |
| 2023-2024 | luck | 20 | 1..20 | 20 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
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
| 1-1 | 232 |
| 2-1 | 196 |
| 1-2 | 180 |
| 0-1 | 172 |
| 1-0 | 170 |
| 2-0 | 169 |
| 2-2 | 146 |
| 3-0 | 117 |
| 0-0 | 112 |
| 3-1 | 105 |
| 3-2 | 88 |
| 0-2 | 87 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 13-0 | 13 | 1 |
| 7-3 | 10 | 1 |
| 6-4 | 10 | 1 |
| 4-6 | 10 | 2 |
| 8-1 | 9 | 1 |
| 7-2 | 9 | 2 |
| 6-3 | 9 | 2 |
| 5-4 | 9 | 2 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 1 |
| 1-8 | 9 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 8 |
| 4-4 | 8 | 5 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 4 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 208 | 8.6% |
| Mon | 443 | 18.4% |
| Tue | 75 | 3.1% |
| Wed | 18 | 0.7% |
| Thu | 10 | 0.4% |
| Fri | 1460 | 60.5% |
| Sat | 198 | 8.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 392 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 120 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.592 vs overall 3.127 (deviation 0.465) |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.7% vs overall 4.6% (deviation 2.9 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 50.8% vs overall 44.7% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 29.2% vs overall 33.3% |
| 9 | HIGH_SCORING_MATCHES | 39 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=338, fgte=338 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 392, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 120, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.592, "overall_avg_goals": 3.127, "deviation": 0.465}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.7, "overall_goalless_pct": 4.6, "deviation_pp": 2.9}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 50.8, "overall_share": 44.7}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 29.2, "overall_share": 33.3}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 39, "threshold": 8, "examples": [{"scoreline": "13-0", "total_goals": 13, "count": 1}, {"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "4-6", "total_goals": 10, "count": 2}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 2}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "5-4", "total_goals": 9, "count": 2}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 60076, "distinct": 60066, "duplicates": 10}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 60076, "fgt_inconsistent": 338, "fgte_inconsistent": 338, "n_with_fgt": 55260}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
