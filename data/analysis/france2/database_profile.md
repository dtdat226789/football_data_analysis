# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:51:31+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `france2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 174 |
| teams | 615 |
| team_aliases | 1230 |
| team_seasons | 2861 |
| matches | 43080 |
| standings | 8583 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `26`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `france2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-08-22 | 2021-05-15 |
| 2021-2022 | False | complete | 380 | 20 | 2021-07-24 | 2022-05-14 |
| 2022-2023 | False | complete | 380 | 20 | 2022-07-30 | 2023-06-02 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-05 | 2024-05-17 |
| 2024-2025 | False | complete | 306 | 19 | 2024-08-16 | 2025-05-10 |
| 2025-2026 | True | complete | 310 | 19 | 2025-08-09 | 2026-05-24 |
| 2026-2027 | True | in_progress | 90 | 18 | 2026-08-08 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 43080 | 43080 | 0 |
| matches (league_season_id, game_index) | 43080 | 43080 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 43080 | 43075 | 5 |
| team_seasons (league_season_id, team_id) | 2861 | 2861 | 0 |
| team_seasons api_name within a season | 2861 | 2861 | 0 |
| team_seasons api_slug within a season | 2861 | 2861 | 0 |
| standings (league_season_id, team_id, view) | 8583 | 8583 | 0 |
| team_aliases (form, value) | 1230 | 1230 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 615 | 615 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `43080`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 43080 | 0.0% |
| kickoff_time | 0 | 43080 | 0.0% |
| home_team_id | 0 | 43080 | 0.0% |
| away_team_id | 0 | 43080 | 0.0% |
| home_score | 0 | 43080 | 0.0% |
| away_score | 0 | 43080 | 0.0% |
| home_ht | 372 | 42708 | 0.9% |
| away_ht | 372 | 42708 | 0.9% |
| first_goal_time | 3669 | 39411 | 8.5% |
| first_goal_time_extra | 3669 | 39411 | 8.5% |
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
| Home | 934 | 42.0% |
| Draw | 640 | 28.8% |
| Away | 652 | 29.3% |
| Total | 2226 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5441 |
| Average goals per match | 2.444 |
| Home goals | 2986 (avg 1.341) |
| Away goals | 2455 (avg 1.103) |
| Home goal share | 54.9% |
| Goalless matches | 216 (9.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 41.8% | 33.4% | 24.7% | 910 | 2.395 | 511 | 399 | 37 (9.7%) |
| 2021-2022 | 380 | 41.3% | 27.9% | 30.8% | 868 | 2.284 | 478 | 390 | 38 (10.0%) |
| 2022-2023 | 380 | 43.9% | 27.1% | 28.9% | 916 | 2.411 | 502 | 414 | 36 (9.5%) |
| 2023-2024 | 380 | 40.3% | 28.7% | 31.1% | 933 | 2.455 | 504 | 429 | 45 (11.8%) |
| 2024-2025 | 306 | 48.7% | 23.5% | 27.8% | 789 | 2.578 | 461 | 328 | 19 (6.2%) |
| 2025-2026 | 310 | 37.7% | 30.6% | 31.6% | 784 | 2.529 | 407 | 377 | 33 (10.6%) |
| 2026-2027 | 90 | 35.6% | 31.1% | 33.3% | 241 | 2.678 | 123 | 118 | 8 (8.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2006` of `2226` (90.1%)
| metric | value |
|---|---|
| First goals recorded | 2006 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 32.55 |
| Median (p50) | 27.0 |
| p25 | 12.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 644 |
| 16-30 | 456 |
| 31-45 | 309 |
| 46-60 | 307 |
| 61-75 | 150 |
| 76-90 | 114 |
| 91-120 | 26 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `408`
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
| 2024-2025 | classic | 19 | 1..19 | 19 |
| 2024-2025 | goals | 19 | 1..19 | 19 |
| 2024-2025 | luck | 19 | 1..19 | 19 |
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 282 |
| 1-1 | 277 |
| 0-0 | 216 |
| 0-1 | 204 |
| 2-1 | 187 |
| 2-0 | 158 |
| 1-2 | 141 |
| 2-2 | 120 |
| 0-2 | 97 |
| 3-1 | 79 |
| 3-0 | 73 |
| 0-3 | 58 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 2 |
| 3-6 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 2 | 0.1% |
| Mon | 152 | 6.8% |
| Tue | 235 | 10.6% |
| Wed | 13 | 0.6% |
| Fri | 520 | 23.4% |
| Sat | 1304 | 58.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 19 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 310 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 90 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 7 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 33.4% vs overall 28.8% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 24.7% vs overall 29.3% |
| 10 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 11.8% vs overall 9.7% (deviation 2.1 pp) |
| 11 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 6.2% vs overall 9.7% (deviation 3.5 pp) |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 48.7% vs overall 42.0% |
| 13 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 draw outcome share 23.5% vs overall 28.8% |
| 14 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 37.7% vs overall 42.0% |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 35.6% vs overall 42.0% |
| 16 | HIGH_SCORING_MATCHES | 12 match(es) with >= 8 total goals (extreme scorelines) |
| 17 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 18 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=317, fgte=317 rows) |
| 19 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=19 positions=1..19 teams=19 |
| 20 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=19 positions=1..19 teams=19 |
| 21 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=19 positions=1..19 teams=19 |
| 22 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 23 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 24 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 25 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 19, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 310, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 90, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `7.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 33.4, "overall_share": 28.8}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 24.7, "overall_share": 29.3}`
- `10.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 11.8, "overall_goalless_pct": 9.7, "deviation_pp": 2.1}`
- `11.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 6.2, "overall_goalless_pct": 9.7, "deviation_pp": 3.5}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 48.7, "overall_share": 42.0}`
- `13.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "draw", "season_share": 23.5, "overall_share": 28.8}`
- `14.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 37.7, "overall_share": 42.0}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 35.6, "overall_share": 42.0}`
- `16.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 12, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 3}]}`
- `17.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 43080, "distinct": 43075, "duplicates": 5}`
- `18.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 43080, "fgt_inconsistent": 317, "fgte_inconsistent": 317, "n_with_fgt": 39411}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
