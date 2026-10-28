# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:47:02+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `finland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 153 |
| teams | 550 |
| team_aliases | 1100 |
| team_seasons | 2512 |
| matches | 37753 |
| standings | 7536 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `23`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `finland1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 132 | 12 | 2020-07-01 | 2020-11-04 |
| 2021 | False | complete | 132 | 12 | 2021-04-24 | 2021-09-30 |
| 2022 | False | complete | 132 | 12 | 2022-04-02 | 2022-09-11 |
| 2023 | False | complete | 132 | 12 | 2023-04-05 | 2023-09-03 |
| 2024 | False | complete | 132 | 12 | 2024-04-06 | 2024-09-01 |
| 2025 | True | complete | 132 | 12 | 2025-04-05 | 2025-08-31 |
| 2026 | True | in_progress | 153 | 12 | 2026-04-04 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 37753 | 37753 | 0 |
| matches (league_season_id, game_index) | 37753 | 37753 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 37753 | 37748 | 5 |
| team_seasons (league_season_id, team_id) | 2512 | 2512 | 0 |
| team_seasons api_name within a season | 2512 | 2512 | 0 |
| team_seasons api_slug within a season | 2512 | 2512 | 0 |
| standings (league_season_id, team_id, view) | 7536 | 7536 | 0 |
| team_aliases (form, value) | 1100 | 1100 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 550 | 550 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `37753`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 37753 | 0.0% |
| kickoff_time | 0 | 37753 | 0.0% |
| home_team_id | 0 | 37753 | 0.0% |
| away_team_id | 0 | 37753 | 0.0% |
| home_score | 0 | 37753 | 0.0% |
| away_score | 0 | 37753 | 0.0% |
| home_ht | 366 | 37387 | 1.0% |
| away_ht | 366 | 37387 | 1.0% |
| first_goal_time | 3241 | 34512 | 8.6% |
| first_goal_time_extra | 3241 | 34512 | 8.6% |
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
| Home | 404 | 42.8% |
| Draw | 225 | 23.8% |
| Away | 316 | 33.4% |
| Total | 945 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2616 |
| Average goals per match | 2.768 |
| Home goals | 1388 (avg 1.469) |
| Away goals | 1228 (avg 1.299) |
| Home goal share | 53.1% |
| Goalless matches | 62 (6.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 132 | 40.2% | 25.0% | 34.8% | 372 | 2.818 | 192 | 180 | 10 (7.6%) |
| 2021 | 132 | 43.2% | 18.9% | 37.9% | 310 | 2.348 | 163 | 147 | 9 (6.8%) |
| 2022 | 132 | 40.9% | 23.5% | 35.6% | 384 | 2.909 | 192 | 192 | 6 (4.5%) |
| 2023 | 132 | 40.9% | 25.8% | 33.3% | 329 | 2.492 | 173 | 156 | 11 (8.3%) |
| 2024 | 132 | 47.0% | 25.0% | 28.0% | 395 | 2.992 | 224 | 171 | 7 (5.3%) |
| 2025 | 132 | 42.4% | 22.0% | 35.6% | 433 | 3.28 | 222 | 211 | 8 (6.1%) |
| 2026 | 153 | 44.4% | 26.1% | 29.4% | 393 | 2.569 | 222 | 171 | 11 (7.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `882` of `945` (93.3%)
| metric | value |
|---|---|
| First goals recorded | 882 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 30.08 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 292 |
| 16-30 | 225 |
| 31-45 | 138 |
| 46-60 | 124 |
| 61-75 | 59 |
| 76-90 | 37 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `252`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 12 | 1..12 | 12 |
| 2020 | goals | 12 | 1..12 | 12 |
| 2020 | luck | 12 | 1..12 | 12 |
| 2021 | classic | 12 | 1..12 | 12 |
| 2021 | goals | 12 | 1..12 | 12 |
| 2021 | luck | 12 | 1..12 | 12 |
| 2022 | classic | 12 | 1..12 | 12 |
| 2022 | goals | 12 | 1..12 | 12 |
| 2022 | luck | 12 | 1..12 | 12 |
| 2023 | classic | 12 | 1..12 | 12 |
| 2023 | goals | 12 | 1..12 | 12 |
| 2023 | luck | 12 | 1..12 | 12 |
| 2024 | classic | 12 | 1..12 | 12 |
| 2024 | goals | 12 | 1..12 | 12 |
| 2024 | luck | 12 | 1..12 | 12 |
| 2025 | classic | 12 | 1..12 | 12 |
| 2025 | goals | 12 | 1..12 | 12 |
| 2025 | luck | 12 | 1..12 | 12 |
| 2026 | classic | 12 | 1..12 | 12 |
| 2026 | goals | 12 | 1..12 | 12 |
| 2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 107 |
| 1-0 | 86 |
| 2-1 | 85 |
| 0-1 | 79 |
| 0-0 | 62 |
| 0-2 | 61 |
| 1-2 | 60 |
| 2-0 | 49 |
| 2-2 | 48 |
| 3-2 | 45 |
| 3-0 | 43 |
| 3-1 | 36 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 5-5 | 10 | 1 |
| 4-6 | 10 | 1 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 214 | 22.6% |
| Mon | 89 | 9.4% |
| Tue | 42 | 4.4% |
| Wed | 113 | 12.0% |
| Thu | 39 | 4.1% |
| Fri | 127 | 13.4% |
| Sat | 321 | 34.0% |

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
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 132 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 12 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 132 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 12 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 153 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | SEASON_AVG_GOALS_OUTLIER | Season 2021 avg goals 2.348 vs overall 2.768 (deviation 0.420) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2021 draw outcome share 18.9% vs overall 23.8% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2021 away outcome share 37.9% vs overall 33.4% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 4.5% vs overall 6.6% (deviation 2.1 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2023 goalless share 8.3% vs overall 6.6% (deviation 1.7 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2024 home outcome share 47.0% vs overall 42.8% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2024 away outcome share 28.0% vs overall 33.4% |
| 23 | SEASON_AVG_GOALS_OUTLIER | Season 2025 avg goals 3.28 vs overall 2.768 (deviation 0.512) |
| 24 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=313, fgte=313 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=12 positions=1..12 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=12 positions=1..12 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=12 positions=1..12 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=12 positions=1..12 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=12 positions=1..12 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=12 positions=1..12 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=12 positions=1..12 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=12 positions=1..12 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=12 positions=1..12 teams=12 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=12 positions=1..12 teams=12 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=12 positions=1..12 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=12 positions=1..12 teams=12 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=12 positions=1..12 teams=12 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=12 positions=1..12 teams=12 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=12 positions=1..12 teams=12 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 132, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 132, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 132, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 132, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 12, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 132, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 12, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 153, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2021", "season_avg_goals": 2.348, "overall_avg_goals": 2.768, "deviation": 0.42}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "draw", "season_share": 18.9, "overall_share": 23.8}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021", "outcome": "away", "season_share": 37.9, "overall_share": 33.4}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 4.5, "overall_goalless_pct": 6.6, "deviation_pp": 2.1}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023", "season_goalless_pct": 8.3, "overall_goalless_pct": 6.6, "deviation_pp": 1.7}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "home", "season_share": 47.0, "overall_share": 42.8}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "away", "season_share": 28.0, "overall_share": 33.4}`
- `23.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025", "season_avg_goals": 3.28, "overall_avg_goals": 2.768, "deviation": 0.512}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "5-5", "total_goals": 10, "count": 1}, {"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 37753, "distinct": 37748, "duplicates": 5}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 37753, "fgt_inconsistent": 313, "fgte_inconsistent": 313, "n_with_fgt": 34512}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
