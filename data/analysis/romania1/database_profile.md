# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:44:37+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `romania1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 438 |
| teams | 1647 |
| team_aliases | 3295 |
| team_seasons | 7452 |
| matches | 112983 |
| standings | 22356 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `65`
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
| hungary2 | NB II. | Hungary | 7 | 2012 |
| india1 | ISL | India | 7 | 723 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2355 |
| italy19 | Primavera 1 | Italy | 7 | 1997 |
| italy2 | Serie B | Italy | 7 | 2368 |
| italy3a | Serie C - Group A | Italy | 7 | 2383 |
| italy3b | Serie C - Group B | Italy | 7 | 2364 |
| japan1 | J1 League | Japan | 8 | 2334 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1507 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1020 |
| lithuania | TOPLYGA | Lithuania | 7 | 1110 |
| morocco | Botola Pro | Morocco | 7 | 1481 |
| national | National League | England | 6 | 2885 |
| north | National League North | England | 7 | 2994 |
| norway | Eliteserien | Norway | 7 | 1626 |
| poland1 | Ekstraklasa | Poland | 7 | 1873 |
| poland2 | Division 1 | Poland | 7 | 1962 |
| portugal1 | Liga Portugal | Portugal | 2 | 384 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1908 |
| premier | Premier League | England | 7 | 2355 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2007 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1985 |
| romania1 | Superliga | Romania | 7 | 1651 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `romania1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-08-21 | 2021-04-12 |
| 2021-2022 | False | complete | 240 | 16 | 2021-07-15 | 2022-03-07 |
| 2022-2023 | False | complete | 240 | 16 | 2022-07-15 | 2023-03-16 |
| 2023-2024 | False | complete | 240 | 16 | 2023-07-14 | 2024-03-11 |
| 2024-2025 | False | complete | 240 | 16 | 2024-07-12 | 2025-03-10 |
| 2025-2026 | True | complete | 350 | 19 | 2025-07-11 | 2026-06-01 |
| 2026-2027 | True | in_progress | 101 | 16 | 2026-07-17 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 112983 | 112983 | 0 |
| matches (league_season_id, game_index) | 112983 | 112983 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 112983 | 112969 | 14 |
| team_seasons (league_season_id, team_id) | 7452 | 7452 | 0 |
| team_seasons api_name within a season | 7452 | 7452 | 0 |
| team_seasons api_slug within a season | 7452 | 7452 | 0 |
| standings (league_season_id, team_id, view) | 22356 | 22356 | 0 |
| team_aliases (form, value) | 3295 | 3295 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1647 | 1647 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `112983`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 112983 | 0.0% |
| kickoff_time | 0 | 112983 | 0.0% |
| home_team_id | 0 | 112983 | 0.0% |
| away_team_id | 0 | 112983 | 0.0% |
| home_score | 0 | 112983 | 0.0% |
| away_score | 0 | 112983 | 0.0% |
| home_ht | 473 | 112510 | 0.4% |
| away_ht | 473 | 112510 | 0.4% |
| first_goal_time | 9059 | 103924 | 8.0% |
| first_goal_time_extra | 9059 | 103924 | 8.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 13 |
| away_score | 0 | 13 |
| first_goal_time | 1 | 112 |
| home_ht | 0 | 7 |
| away_ht | 0 | 7 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 698 | 42.3% |
| Draw | 483 | 29.3% |
| Away | 470 | 28.5% |
| Total | 1651 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3956 |
| Average goals per match | 2.396 |
| Home goals | 2232 (avg 1.352) |
| Away goals | 1724 (avg 1.044) |
| Home goal share | 56.4% |
| Goalless matches | 158 (9.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 34.6% | 30.8% | 34.6% | 549 | 2.288 | 283 | 266 | 25 (10.4%) |
| 2021-2022 | 240 | 42.9% | 28.3% | 28.8% | 521 | 2.171 | 289 | 232 | 28 (11.7%) |
| 2022-2023 | 240 | 44.6% | 26.2% | 29.2% | 562 | 2.342 | 329 | 233 | 17 (7.1%) |
| 2023-2024 | 240 | 40.0% | 33.3% | 26.7% | 615 | 2.562 | 339 | 276 | 30 (12.5%) |
| 2024-2025 | 240 | 41.7% | 32.5% | 25.8% | 553 | 2.304 | 315 | 238 | 26 (10.8%) |
| 2025-2026 | 350 | 44.3% | 27.4% | 28.3% | 887 | 2.534 | 504 | 383 | 25 (7.1%) |
| 2026-2027 | 101 | 53.5% | 23.8% | 22.8% | 269 | 2.663 | 173 | 96 | 7 (6.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1492` of `1651` (90.4%)
| metric | value |
|---|---|
| First goals recorded | 1492 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 33.15 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 450 |
| 16-30 | 357 |
| 31-45 | 241 |
| 46-60 | 207 |
| 61-75 | 137 |
| 76-90 | 72 |
| 91-120 | 28 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `345`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 16 | 1..16 | 16 |
| 2021-2022 | goals | 16 | 1..16 | 16 |
| 2021-2022 | luck | 16 | 1..16 | 16 |
| 2022-2023 | classic | 16 | 1..16 | 16 |
| 2022-2023 | goals | 16 | 1..16 | 16 |
| 2022-2023 | luck | 16 | 1..16 | 16 |
| 2023-2024 | classic | 16 | 1..16 | 16 |
| 2023-2024 | goals | 16 | 1..16 | 16 |
| 2023-2024 | luck | 16 | 1..16 | 16 |
| 2024-2025 | classic | 16 | 1..16 | 16 |
| 2024-2025 | goals | 16 | 1..16 | 16 |
| 2024-2025 | luck | 16 | 1..16 | 16 |
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 234 |
| 1-0 | 203 |
| 0-1 | 167 |
| 0-0 | 158 |
| 2-1 | 151 |
| 2-0 | 100 |
| 0-2 | 95 |
| 1-2 | 88 |
| 2-2 | 78 |
| 3-1 | 58 |
| 3-0 | 43 |
| 3-2 | 39 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-8 | 10 | 1 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 434 | 26.3% |
| Mon | 333 | 20.2% |
| Tue | 41 | 2.5% |
| Wed | 39 | 2.4% |
| Thu | 46 | 2.8% |
| Fri | 328 | 19.9% |
| Sat | 430 | 26.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 350 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 101 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 34.6% vs overall 42.3% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 34.6% vs overall 28.5% |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 11.7% vs overall 9.6% (deviation 2.1 pp) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 7.1% vs overall 9.6% (deviation 2.5 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 12.5% vs overall 9.6% (deviation 2.9 pp) |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 7.1% vs overall 9.6% (deviation 2.5 pp) |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 6.9% vs overall 9.6% (deviation 2.7 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 53.5% vs overall 42.3% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 23.8% vs overall 29.3% |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 22.8% vs overall 28.5% |
| 26 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 27 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 28 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=414, fgte=414 rows) |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 350, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 101, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 34.6, "overall_share": 42.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 34.6, "overall_share": 28.5}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 11.7, "overall_goalless_pct": 9.6, "deviation_pp": 2.1}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 7.1, "overall_goalless_pct": 9.6, "deviation_pp": 2.5}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 12.5, "overall_goalless_pct": 9.6, "deviation_pp": 2.9}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 7.1, "overall_goalless_pct": 9.6, "deviation_pp": 2.5}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 6.9, "overall_goalless_pct": 9.6, "deviation_pp": 2.7}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 53.5, "overall_share": 42.3}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 23.8, "overall_share": 29.3}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 22.8, "overall_share": 28.5}`
- `26.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "2-8", "total_goals": 10, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `27.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 112983, "distinct": 112969, "duplicates": 14}`
- `28.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 112983, "fgt_inconsistent": 414, "fgte_inconsistent": 414, "n_with_fgt": 103924}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
