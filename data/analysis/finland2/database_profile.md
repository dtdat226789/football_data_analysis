# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T01:59:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `finland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 160 |
| teams | 565 |
| team_aliases | 1130 |
| team_seasons | 2590 |
| matches | 38711 |
| standings | 7770 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `24`
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
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1087 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1421 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |
| egypt | Premier League | Egypt | 7 | 1769 |
| eng1 | League One | England | 7 | 3460 |
| eng2 | League Two | England | 7 | 3468 |
| estonia | Meistriliiga | Estonia | 7 | 1169 |
| finland1 | Veikkausliiga | Finland | 7 | 945 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `finland2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 132 | 12 | 2020-06-27 | 2020-11-08 |
| 2021 | False | complete | 132 | 12 | 2021-05-05 | 2021-09-19 |
| 2022 | False | complete | 132 | 12 | 2022-04-18 | 2022-09-03 |
| 2023 | False | complete | 132 | 12 | 2023-04-14 | 2023-09-02 |
| 2024 | False | complete | 135 | 10 | 2024-04-13 | 2024-10-19 |
| 2025 | True | complete | 135 | 10 | 2025-04-21 | 2025-10-18 |
| 2026 | True | in_progress | 135 | 10 | 2026-04-03 | 2026-10-17 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 38711 | 38711 | 0 |
| matches (league_season_id, game_index) | 38711 | 38711 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 38711 | 38706 | 5 |
| team_seasons (league_season_id, team_id) | 2590 | 2590 | 0 |
| team_seasons api_name within a season | 2590 | 2590 | 0 |
| team_seasons api_slug within a season | 2590 | 2590 | 0 |
| standings (league_season_id, team_id, view) | 7770 | 7770 | 0 |
| team_aliases (form, value) | 1130 | 1130 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 565 | 565 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `38711`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 38711 | 0.0% |
| kickoff_time | 0 | 38711 | 0.0% |
| home_team_id | 0 | 38711 | 0.0% |
| away_team_id | 0 | 38711 | 0.0% |
| home_score | 0 | 38711 | 0.0% |
| away_score | 0 | 38711 | 0.0% |
| home_ht | 366 | 38345 | 0.9% |
| away_ht | 366 | 38345 | 0.9% |
| first_goal_time | 3299 | 35412 | 8.5% |
| first_goal_time_extra | 3299 | 35412 | 8.5% |
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
| Home | 398 | 42.7% |
| Draw | 233 | 25.0% |
| Away | 302 | 32.4% |
| Total | 933 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2783 |
| Average goals per match | 2.983 |
| Home goals | 1528 (avg 1.638) |
| Away goals | 1255 (avg 1.345) |
| Home goal share | 54.9% |
| Goalless matches | 57 (6.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 132 | 41.7% | 22.0% | 36.4% | 442 | 3.348 | 250 | 192 | 6 (4.5%) |
| 2021 | 132 | 40.2% | 26.5% | 33.3% | 355 | 2.689 | 191 | 164 | 10 (7.6%) |
| 2022 | 132 | 44.7% | 25.8% | 29.5% | 395 | 2.992 | 229 | 166 | 5 (3.8%) |
| 2023 | 132 | 44.7% | 26.5% | 28.8% | 368 | 2.788 | 209 | 159 | 11 (8.3%) |
| 2024 | 135 | 41.5% | 25.2% | 33.3% | 420 | 3.111 | 224 | 196 | 10 (7.4%) |
| 2025 | 135 | 43.0% | 25.9% | 31.1% | 443 | 3.281 | 235 | 208 | 5 (3.7%) |
| 2026 | 135 | 43.0% | 23.0% | 34.1% | 360 | 2.667 | 190 | 170 | 10 (7.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `876` of `933` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 876 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 29.56 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 44.25 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 313 |
| 16-30 | 222 |
| 31-45 | 132 |
| 46-60 | 101 |
| 61-75 | 69 |
| 76-90 | 31 |
| 91-120 | 8 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `234`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 12 | 1..12 | 12 |
| 2020 | goals | 12 | 1..12 | 12 |
| 2020 | luck | 12 | 1..12 | 12 |
| 2021 | classic | 12 | 1..13 | 12 |
| 2021 | goals | 12 | 6..21 | 12 |
| 2021 | luck | 12 | 1..24 | 12 |
| 2022 | classic | 12 | 1..13 | 12 |
| 2022 | goals | 12 | 6..20 | 12 |
| 2022 | luck | 12 | 1..24 | 12 |
| 2023 | classic | 12 | 1..12 | 12 |
| 2023 | goals | 12 | 1..12 | 12 |
| 2023 | luck | 12 | 1..12 | 12 |
| 2024 | classic | 10 | 1..11 | 10 |
| 2024 | goals | 10 | 2..14 | 10 |
| 2024 | luck | 10 | 1..20 | 10 |
| 2025 | classic | 10 | 1..11 | 10 |
| 2025 | goals | 10 | 2..15 | 10 |
| 2025 | luck | 10 | 1..20 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 108 |
| 2-1 | 78 |
| 1-0 | 72 |
| 1-2 | 65 |
| 0-1 | 64 |
| 0-0 | 57 |
| 2-2 | 55 |
| 2-0 | 54 |
| 0-2 | 51 |
| 3-0 | 38 |
| 3-1 | 38 |
| 0-3 | 30 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 10-2 | 12 | 1 |
| 10-1 | 11 | 1 |
| 8-2 | 10 | 1 |
| 4-6 | 10 | 1 |
| 7-2 | 9 | 1 |
| 3-6 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 5 |
| 4-4 | 8 | 2 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 206 | 22.1% |
| Mon | 50 | 5.4% |
| Tue | 24 | 2.6% |
| Wed | 113 | 12.1% |
| Thu | 41 | 4.4% |
| Fri | 143 | 15.3% |
| Sat | 356 | 38.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 132 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 132 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 132 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 135 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 135 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 135 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | SEASON_AVG_GOALS_OUTLIER | Season 2020 avg goals 3.348 vs overall 2.983 (deviation 0.365) |
| 17 | GOALLESS_SHARE_OUTLIER | Season 2020 goalless share 4.5% vs overall 6.1% (deviation 1.6 pp) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 3.8% vs overall 6.1% (deviation 2.3 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2023 goalless share 8.3% vs overall 6.1% (deviation 2.2 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 3.7% vs overall 6.1% (deviation 2.4 pp) |
| 21 | HIGH_SCORING_MATCHES | 19 match(es) with >= 8 total goals (extreme scorelines) |
| 22 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 23 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows) |
| 24 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=12 positions=1..12 teams=12 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=12 positions=1..12 teams=12 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=12 positions=1..12 teams=12 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=12 positions=1..13 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=12 positions=6..21 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=12 positions=1..24 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=12 positions=1..13 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=12 positions=6..20 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=12 positions=1..24 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=12 positions=1..12 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=10 positions=1..11 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=10 positions=2..14 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=10 positions=1..20 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..11 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=2..15 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..20 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 132, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 132, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 132, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 135, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 135, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 135, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2020", "season_avg_goals": 3.348, "overall_avg_goals": 2.983, "deviation": 0.365}`
- `17.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020", "season_goalless_pct": 4.5, "overall_goalless_pct": 6.1, "deviation_pp": 1.6}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 3.8, "overall_goalless_pct": 6.1, "deviation_pp": 2.3}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023", "season_goalless_pct": 8.3, "overall_goalless_pct": 6.1, "deviation_pp": 2.2}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 3.7, "overall_goalless_pct": 6.1, "deviation_pp": 2.4}`
- `21.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 19, "threshold": 8, "examples": [{"scoreline": "10-2", "total_goals": 12, "count": 1}, {"scoreline": "10-1", "total_goals": 11, "count": 1}, {"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 5}]}`
- `22.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 38711, "distinct": 38706, "duplicates": 5}`
- `23.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 38711, "fgt_inconsistent": 313, "fgte_inconsistent": 313, "n_with_fgt": 35412}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 12, "min_pos": 6, "max_pos": 21, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 12, "min_pos": 6, "max_pos": 20, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 10, "min_pos": 2, "max_pos": 14, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 20, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 2, "max_pos": 15, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 20, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
