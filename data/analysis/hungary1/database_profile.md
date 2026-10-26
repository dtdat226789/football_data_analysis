# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:35:55+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `hungary1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 251 |
| teams | 950 |
| team_aliases | 1900 |
| team_seasons | 4307 |
| matches | 62928 |
| standings | 12921 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `37`
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
| finland1 | Veikkausliiga | Finland | 7 | 944 |
| finland2 | Ykkosliiga | Finland | 7 | 933 |
| france1 | Ligue 1 | France | 7 | 2127 |
| france2 | Ligue 2 | France | 7 | 2224 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1696 |
| germany1 | Bundesliga | Germany | 7 | 1688 |
| germany2 | 2. Bundesliga | Germany | 7 | 1918 |
| germany3 | 3. Liga | Germany | 7 | 2380 |
| greece1 | Super League | Greece | 7 | 1207 |
| greece2 | Super League 2 | Greece | 7 | 1832 |
| holland1 | Eredivisie | Netherlands | 7 | 1936 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1250 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `hungary1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 198 | 12 | 2020-08-14 | 2021-05-09 |
| 2021-2022 | False | complete | 198 | 12 | 2021-07-30 | 2022-05-15 |
| 2022-2023 | False | complete | 198 | 12 | 2022-07-29 | 2023-05-28 |
| 2023-2024 | False | complete | 198 | 12 | 2023-07-28 | 2024-05-19 |
| 2024-2025 | False | complete | 198 | 12 | 2024-07-26 | 2025-05-25 |
| 2025-2026 | True | complete | 198 | 12 | 2025-07-25 | 2026-05-16 |
| 2026-2027 | True | in_progress | 62 | 12 | 2026-07-24 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 62928 | 62928 | 0 |
| matches (league_season_id, game_index) | 62928 | 62928 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 62928 | 62918 | 10 |
| team_seasons (league_season_id, team_id) | 4307 | 4307 | 0 |
| team_seasons api_name within a season | 4307 | 4307 | 0 |
| team_seasons api_slug within a season | 4307 | 4307 | 0 |
| standings (league_season_id, team_id, view) | 12921 | 12921 | 0 |
| team_aliases (form, value) | 1900 | 1900 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 950 | 950 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `62928`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 62928 | 0.0% |
| kickoff_time | 0 | 62928 | 0.0% |
| home_team_id | 0 | 62928 | 0.0% |
| away_team_id | 0 | 62928 | 0.0% |
| home_score | 0 | 62928 | 0.0% |
| away_score | 0 | 62928 | 0.0% |
| home_ht | 395 | 62533 | 0.6% |
| away_ht | 395 | 62533 | 0.6% |
| first_goal_time | 4959 | 57969 | 7.9% |
| first_goal_time_extra | 4959 | 57969 | 7.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 110 |
| home_ht | 0 | 7 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 534 | 42.7% |
| Draw | 322 | 25.8% |
| Away | 394 | 31.5% |
| Total | 1250 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3624 |
| Average goals per match | 2.899 |
| Home goals | 1985 (avg 1.588) |
| Away goals | 1639 (avg 1.311) |
| Home goal share | 54.8% |
| Goalless matches | 89 (7.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 198 | 42.9% | 23.2% | 33.8% | 597 | 3.015 | 326 | 271 | 14 (7.1%) |
| 2021-2022 | 198 | 39.9% | 26.8% | 33.3% | 562 | 2.838 | 295 | 267 | 18 (9.1%) |
| 2022-2023 | 198 | 43.4% | 29.8% | 26.8% | 530 | 2.677 | 299 | 231 | 16 (8.1%) |
| 2023-2024 | 198 | 48.5% | 19.7% | 31.8% | 603 | 3.045 | 344 | 259 | 11 (5.6%) |
| 2024-2025 | 198 | 42.9% | 29.3% | 27.8% | 553 | 2.793 | 309 | 244 | 20 (10.1%) |
| 2025-2026 | 198 | 39.4% | 24.7% | 35.9% | 594 | 3.0 | 308 | 286 | 8 (4.0%) |
| 2026-2027 | 62 | 40.3% | 29.0% | 30.6% | 185 | 2.984 | 104 | 81 | 2 (3.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1160` of `1250` (92.8%)
| metric | value |
|---|---|
| First goals recorded | 1160 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 30.44 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 390 |
| 16-30 | 280 |
| 31-45 | 196 |
| 46-60 | 152 |
| 61-75 | 73 |
| 76-90 | 55 |
| 91-120 | 14 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `252`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 12 | 1..13 | 12 |
| 2020-2021 | goals | 12 | 3..20 | 12 |
| 2020-2021 | luck | 12 | 1..24 | 12 |
| 2021-2022 | classic | 12 | 1..12 | 12 |
| 2021-2022 | goals | 12 | 2..18 | 12 |
| 2021-2022 | luck | 12 | 1..24 | 12 |
| 2022-2023 | classic | 12 | 1..13 | 12 |
| 2022-2023 | goals | 12 | 5..19 | 12 |
| 2022-2023 | luck | 12 | 1..24 | 12 |
| 2023-2024 | classic | 12 | 1..12 | 12 |
| 2023-2024 | goals | 12 | 4..20 | 12 |
| 2023-2024 | luck | 12 | 1..24 | 12 |
| 2024-2025 | classic | 12 | 1..12 | 12 |
| 2024-2025 | goals | 12 | 1..12 | 12 |
| 2024-2025 | luck | 12 | 1..12 | 12 |
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 143 |
| 2-1 | 118 |
| 1-2 | 103 |
| 1-0 | 98 |
| 0-0 | 89 |
| 0-1 | 85 |
| 2-2 | 72 |
| 2-0 | 70 |
| 3-1 | 64 |
| 3-0 | 55 |
| 0-2 | 51 |
| 1-3 | 46 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-9 | 11 | 1 |
| 7-2 | 9 | 1 |
| 5-4 | 9 | 2 |
| 2-7 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 6 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 458 | 36.6% |
| Mon | 16 | 1.3% |
| Tue | 20 | 1.6% |
| Wed | 42 | 3.4% |
| Thu | 11 | 0.9% |
| Fri | 162 | 13.0% |
| Sat | 541 | 43.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 198 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 198 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 12 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 198 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 12 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 198 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 198 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 12 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 198 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 62 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 9.1% vs overall 7.1% (deviation 2.0 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 26.8% vs overall 31.5% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 48.5% vs overall 42.7% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 draw outcome share 19.7% vs overall 25.8% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 10.1% vs overall 7.1% (deviation 3.0 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 4.0% vs overall 7.1% (deviation 3.1 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 away outcome share 35.9% vs overall 31.5% |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.2% vs overall 7.1% (deviation 3.9 pp) |
| 24 | HIGH_SCORING_MATCHES | 15 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=340, fgte=340 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=12 positions=1..13 teams=12 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=12 positions=3..20 teams=12 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=12 positions=1..24 teams=12 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=12 positions=1..12 teams=12 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=12 positions=2..18 teams=12 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=12 positions=1..24 teams=12 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=12 positions=1..13 teams=12 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=12 positions=5..19 teams=12 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=12 positions=1..24 teams=12 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=12 positions=1..12 teams=12 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=12 positions=4..20 teams=12 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=12 positions=1..24 teams=12 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=12 positions=1..12 teams=12 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 198, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 198, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 12, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 198, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 12, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 198, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 198, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 12, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 198, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 62, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 9.1, "overall_goalless_pct": 7.1, "deviation_pp": 2.0}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 26.8, "overall_share": 31.5}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 48.5, "overall_share": 42.7}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "draw", "season_share": 19.7, "overall_share": 25.8}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 10.1, "overall_goalless_pct": 7.1, "deviation_pp": 3.0}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 4.0, "overall_goalless_pct": 7.1, "deviation_pp": 3.1}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "away", "season_share": 35.9, "overall_share": 31.5}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.2, "overall_goalless_pct": 7.1, "deviation_pp": 3.9}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 15, "threshold": 8, "examples": [{"scoreline": "2-9", "total_goals": 11, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 6}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 62928, "distinct": 62918, "duplicates": 10}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 62928, "fgt_inconsistent": 340, "fgte_inconsistent": 340, "n_with_fgt": 57969}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 12, "min_pos": 3, "max_pos": 20, "distinct_teams": 12}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 12, "min_pos": 2, "max_pos": 18, "distinct_teams": 12}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 12, "min_pos": 5, "max_pos": 19, "distinct_teams": 12}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 12, "min_pos": 4, "max_pos": 20, "distinct_teams": 12}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 24, "distinct_teams": 12}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
