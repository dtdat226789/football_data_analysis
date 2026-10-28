# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:00:18+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `korea2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 342 |
| teams | 1258 |
| team_aliases | 2516 |
| team_seasons | 5801 |
| matches | 87238 |
| standings | 17403 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `50`
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
| germany1 | Bundesliga | Germany | 7 | 1690 |
| germany2 | 2. Bundesliga | Germany | 7 | 1921 |
| germany3 | 3. Liga | Germany | 7 | 2383 |
| greece1 | Super League | Greece | 7 | 1211 |
| greece2 | Super League 2 | Greece | 7 | 1835 |
| holland1 | Eredivisie | Netherlands | 7 | 1941 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1253 |
| hungary2 | NB II. | Hungary | 7 | 2013 |
| india1 | ISL | India | 7 | 725 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2360 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2370 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `korea2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 135 | 10 | 2020-05-09 | 2020-11-21 |
| 2021 | False | complete | 173 | 10 | 2021-02-27 | 2021-10-31 |
| 2022 | False | complete | 220 | 11 | 2022-02-19 | 2022-10-15 |
| 2023 | False | complete | 234 | 13 | 2023-03-01 | 2023-11-26 |
| 2024 | False | complete | 234 | 13 | 2024-03-01 | 2024-11-09 |
| 2025 | True | complete | 273 | 14 | 2025-02-22 | 2025-11-23 |
| 2026 | True | in_progress | 244 | 17 | 2026-02-28 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 87238 | 87238 | 0 |
| matches (league_season_id, game_index) | 87238 | 87238 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 87238 | 87224 | 14 |
| team_seasons (league_season_id, team_id) | 5801 | 5801 | 0 |
| team_seasons api_name within a season | 5801 | 5801 | 0 |
| team_seasons api_slug within a season | 5801 | 5801 | 0 |
| standings (league_season_id, team_id, view) | 17403 | 17403 | 0 |
| team_aliases (form, value) | 2516 | 2516 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1258 | 1258 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `87238`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 87238 | 0.0% |
| kickoff_time | 0 | 87238 | 0.0% |
| home_team_id | 0 | 87238 | 0.0% |
| away_team_id | 0 | 87238 | 0.0% |
| home_score | 0 | 87238 | 0.0% |
| away_score | 0 | 87238 | 0.0% |
| home_ht | 420 | 86818 | 0.5% |
| away_ht | 420 | 86818 | 0.5% |
| first_goal_time | 6995 | 80243 | 8.0% |
| first_goal_time_extra | 6995 | 80243 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 112 |
| home_ht | 0 | 7 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 556 | 36.7% |
| Draw | 433 | 28.6% |
| Away | 524 | 34.6% |
| Total | 1513 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3866 |
| Average goals per match | 2.555 |
| Home goals | 1998 (avg 1.321) |
| Away goals | 1868 (avg 1.235) |
| Home goal share | 51.7% |
| Goalless matches | 136 (9.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 135 | 31.9% | 25.9% | 42.2% | 326 | 2.415 | 156 | 170 | 11 (8.1%) |
| 2021 | 173 | 34.1% | 28.3% | 37.6% | 418 | 2.416 | 214 | 204 | 19 (11.0%) |
| 2022 | 220 | 42.3% | 29.5% | 28.2% | 556 | 2.527 | 303 | 253 | 20 (9.1%) |
| 2023 | 234 | 42.3% | 24.4% | 33.3% | 601 | 2.568 | 319 | 282 | 24 (10.3%) |
| 2024 | 234 | 32.9% | 29.9% | 37.2% | 616 | 2.632 | 302 | 314 | 19 (8.1%) |
| 2025 | 273 | 35.2% | 29.3% | 35.5% | 686 | 2.513 | 360 | 326 | 26 (9.5%) |
| 2026 | 244 | 36.5% | 31.6% | 32.0% | 663 | 2.717 | 344 | 319 | 17 (7.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1377` of `1513` (91.0%)
| metric | value |
|---|---|
| First goals recorded | 1377 |
| Min minute | 1 |
| Max minute | 112 |
| Mean minute | 35.61 |
| Median (p50) | 32.0 |
| p25 | 15.0 |
| p75 | 52.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 364 |
| 16-30 | 303 |
| 31-45 | 263 |
| 46-60 | 201 |
| 61-75 | 130 |
| 76-90 | 85 |
| 91-120 | 31 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `264`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 10 | 1..10 | 10 |
| 2020 | goals | 10 | 1..10 | 10 |
| 2020 | luck | 10 | 1..10 | 10 |
| 2021 | classic | 10 | 1..11 | 10 |
| 2021 | goals | 10 | 2..19 | 10 |
| 2021 | luck | 10 | 1..19 | 10 |
| 2022 | classic | 11 | 1..12 | 11 |
| 2022 | goals | 11 | 4..21 | 11 |
| 2022 | luck | 11 | 1..22 | 11 |
| 2023 | classic | 13 | 1..13 | 13 |
| 2023 | goals | 13 | 5..22 | 13 |
| 2023 | luck | 13 | 1..26 | 13 |
| 2024 | classic | 13 | 1..14 | 13 |
| 2024 | goals | 13 | 4..22 | 13 |
| 2024 | luck | 13 | 1..26 | 13 |
| 2025 | classic | 14 | 1..15 | 14 |
| 2025 | goals | 14 | 6..22 | 14 |
| 2025 | luck | 14 | 1..28 | 14 |
| 2026 | classic | 17 | 1..17 | 17 |
| 2026 | goals | 17 | 1..17 | 17 |
| 2026 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 197 |
| 0-1 | 149 |
| 1-0 | 143 |
| 0-0 | 136 |
| 1-2 | 128 |
| 2-1 | 126 |
| 2-2 | 86 |
| 2-0 | 84 |
| 0-2 | 77 |
| 3-1 | 54 |
| 2-3 | 47 |
| 3-0 | 46 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-7 | 10 | 1 |
| 4-5 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 587 | 38.8% |
| Mon | 84 | 5.6% |
| Tue | 59 | 3.9% |
| Wed | 96 | 6.3% |
| Thu | 1 | 0.1% |
| Fri | 29 | 1.9% |
| Sat | 657 | 43.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 135 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021 has 173 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022 has 220 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022 has 11 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023 has 234 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023 has 13 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024 has 234 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024 has 13 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025 has 273 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025 has 14 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026 has 244 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026 has 17 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020 home outcome share 31.9% vs overall 36.7% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 42.2% vs overall 34.6% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 11.0% vs overall 9.0% (deviation 2.0 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2022 home outcome share 42.3% vs overall 36.7% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2022 away outcome share 28.2% vs overall 34.6% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2023 home outcome share 42.3% vs overall 36.7% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2023 draw outcome share 24.4% vs overall 28.6% |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 7.0% vs overall 9.0% (deviation 2.0 pp) |
| 24 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 25 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 26 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=367, fgte=367 rows) |
| 27 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=10 positions=1..10 teams=10 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=10 positions=1..10 teams=10 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=10 positions=1..10 teams=10 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=10 positions=1..11 teams=10 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=10 positions=2..19 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=10 positions=1..19 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=11 positions=1..12 teams=11 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=11 positions=4..21 teams=11 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=11 positions=1..22 teams=11 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=13 positions=1..13 teams=13 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=13 positions=5..22 teams=13 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=13 positions=1..26 teams=13 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=13 positions=1..14 teams=13 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=13 positions=4..22 teams=13 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=13 positions=1..26 teams=13 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=14 positions=1..15 teams=14 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=14 positions=6..22 teams=14 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=14 positions=1..28 teams=14 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=17 positions=1..17 teams=17 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=17 positions=1..17 teams=17 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 135, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021", "n_matches": 173, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 220, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 11, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 234, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 13, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 234, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024", "n_teams": 13, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 273, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 14, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 244, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 17, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "home", "season_share": 31.9, "overall_share": 36.7}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 42.2, "overall_share": 34.6}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 11.0, "overall_goalless_pct": 9.0, "deviation_pp": 2.0}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "home", "season_share": 42.3, "overall_share": 36.7}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "away", "season_share": 28.2, "overall_share": 34.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "home", "season_share": 42.3, "overall_share": 36.7}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023", "outcome": "draw", "season_share": 24.4, "overall_share": 28.6}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 7.0, "overall_goalless_pct": 9.0, "deviation_pp": 2.0}`
- `24.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "3-7", "total_goals": 10, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `25.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 87238, "distinct": 87224, "duplicates": 14}`
- `26.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 87238, "fgt_inconsistent": 367, "fgte_inconsistent": 367, "n_with_fgt": 80243}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 10, "min_pos": 2, "max_pos": 19, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 19, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 12, "distinct_teams": 11}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 11, "min_pos": 4, "max_pos": 21, "distinct_teams": 11}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 22, "distinct_teams": 11}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 13, "min_pos": 5, "max_pos": 22, "distinct_teams": 13}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 26, "distinct_teams": 13}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 14, "distinct_teams": 13}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 13, "min_pos": 4, "max_pos": 22, "distinct_teams": 13}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 26, "distinct_teams": 13}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 15, "distinct_teams": 14}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 14, "min_pos": 6, "max_pos": 22, "distinct_teams": 14}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 28, "distinct_teams": 14}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
