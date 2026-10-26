# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:41:46+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `north`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 382 |
| teams | 1394 |
| team_aliases | 2789 |
| team_seasons | 6427 |
| matches | 97232 |
| standings | 19281 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `56`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `north`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 165 | 22 | 2020-10-05 | 2021-02-16 |
| 2021-2022 | False | complete | 462 | 22 | 2021-08-14 | 2022-05-07 |
| 2022-2023 | False | complete | 552 | 24 | 2022-08-06 | 2023-04-29 |
| 2023-2024 | False | complete | 552 | 24 | 2023-08-05 | 2024-04-20 |
| 2024-2025 | False | complete | 552 | 24 | 2024-08-10 | 2025-04-26 |
| 2025-2026 | True | complete | 560 | 24 | 2025-08-09 | 2026-05-09 |
| 2026-2027 | True | in_progress | 151 | 24 | 2026-08-08 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 97232 | 97232 | 0 |
| matches (league_season_id, game_index) | 97232 | 97232 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 97232 | 97218 | 14 |
| team_seasons (league_season_id, team_id) | 6427 | 6427 | 0 |
| team_seasons api_name within a season | 6427 | 6427 | 0 |
| team_seasons api_slug within a season | 6427 | 6427 | 0 |
| standings (league_season_id, team_id, view) | 19281 | 19281 | 0 |
| team_aliases (form, value) | 2789 | 2789 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1394 | 1394 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `97232`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 97232 | 0.0% |
| kickoff_time | 0 | 97232 | 0.0% |
| home_team_id | 0 | 97232 | 0.0% |
| away_team_id | 0 | 97232 | 0.0% |
| home_score | 0 | 97232 | 0.0% |
| away_score | 0 | 97232 | 0.0% |
| home_ht | 452 | 96780 | 0.5% |
| away_ht | 452 | 96780 | 0.5% |
| first_goal_time | 7781 | 89451 | 8.0% |
| first_goal_time_extra | 7781 | 89451 | 8.0% |
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
| Home | 1302 | 43.5% |
| Draw | 739 | 24.7% |
| Away | 953 | 31.8% |
| Total | 2994 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 8084 |
| Average goals per match | 2.7 |
| Home goals | 4474 (avg 1.494) |
| Away goals | 3610 (avg 1.206) |
| Home goal share | 55.3% |
| Goalless matches | 211 (7.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 165 | 39.4% | 30.3% | 30.3% | 458 | 2.776 | 243 | 215 | 8 (4.8%) |
| 2021-2022 | 462 | 46.3% | 26.2% | 27.5% | 1220 | 2.641 | 702 | 518 | 40 (8.7%) |
| 2022-2023 | 552 | 40.9% | 29.2% | 29.9% | 1390 | 2.518 | 773 | 617 | 52 (9.4%) |
| 2023-2024 | 552 | 44.2% | 21.9% | 33.9% | 1474 | 2.67 | 810 | 664 | 40 (7.2%) |
| 2024-2025 | 552 | 43.7% | 23.0% | 33.3% | 1420 | 2.572 | 787 | 633 | 42 (7.6%) |
| 2025-2026 | 560 | 42.7% | 22.5% | 34.8% | 1707 | 3.048 | 920 | 787 | 23 (4.1%) |
| 2026-2027 | 151 | 48.3% | 21.9% | 29.8% | 415 | 2.748 | 239 | 176 | 6 (4.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2780` of `2994` (92.9%)
| metric | value |
|---|---|
| First goals recorded | 2780 |
| Min minute | 1 |
| Max minute | 102 |
| Mean minute | 30.54 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 937 |
| 16-30 | 658 |
| 31-45 | 472 |
| 46-60 | 374 |
| 61-75 | 178 |
| 76-90 | 129 |
| 91-120 | 32 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `492`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 22 | 1..22 | 22 |
| 2020-2021 | goals | 22 | 1..22 | 22 |
| 2020-2021 | luck | 22 | 1..22 | 22 |
| 2021-2022 | classic | 22 | 1..22 | 22 |
| 2021-2022 | goals | 22 | 1..22 | 22 |
| 2021-2022 | luck | 22 | 1..22 | 22 |
| 2022-2023 | classic | 24 | 1..24 | 24 |
| 2022-2023 | goals | 24 | 1..24 | 24 |
| 2022-2023 | luck | 24 | 1..24 | 24 |
| 2023-2024 | classic | 24 | 1..24 | 24 |
| 2023-2024 | goals | 24 | 1..24 | 24 |
| 2023-2024 | luck | 24 | 1..24 | 24 |
| 2024-2025 | classic | 24 | 1..24 | 24 |
| 2024-2025 | goals | 24 | 1..24 | 24 |
| 2024-2025 | luck | 24 | 1..24 | 24 |
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 339 |
| 1-0 | 281 |
| 2-1 | 262 |
| 0-1 | 248 |
| 1-2 | 221 |
| 0-0 | 211 |
| 2-0 | 205 |
| 0-2 | 162 |
| 2-2 | 156 |
| 3-0 | 143 |
| 3-1 | 126 |
| 1-3 | 77 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 3-7 | 10 | 1 |
| 9-0 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 2 |
| 2-6 | 8 | 1 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 21 | 0.7% |
| Mon | 180 | 6.0% |
| Tue | 813 | 27.2% |
| Wed | 24 | 0.8% |
| Thu | 13 | 0.4% |
| Fri | 79 | 2.6% |
| Sat | 1864 | 62.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 165 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 22 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 462 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 22 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 552 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 24 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 552 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 24 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 552 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 24 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 560 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 151 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 4.8% vs overall 7.0% (deviation 2.2 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 39.4% vs overall 43.5% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 30.3% vs overall 24.7% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 8.7% vs overall 7.0% (deviation 1.7 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 away outcome share 27.5% vs overall 31.8% |
| 21 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 9.4% vs overall 7.0% (deviation 2.4 pp) |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 29.2% vs overall 24.7% |
| 23 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 4.1% vs overall 7.0% (deviation 2.9 pp) |
| 24 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.0% vs overall 7.0% (deviation 3.0 pp) |
| 25 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 48.3% vs overall 43.5% |
| 26 | HIGH_SCORING_MATCHES | 14 match(es) with >= 8 total goals (extreme scorelines) |
| 27 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 28 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=393, fgte=393 rows) |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=22 positions=1..22 teams=22 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=22 positions=1..22 teams=22 |
| 31 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=22 positions=1..22 teams=22 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=22 positions=1..22 teams=22 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=22 positions=1..22 teams=22 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=22 positions=1..22 teams=22 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 165, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 22, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 462, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 22, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 552, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 24, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 552, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 24, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 552, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 24, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 560, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 151, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 4.8, "overall_goalless_pct": 7.0, "deviation_pp": 2.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 39.4, "overall_share": 43.5}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 30.3, "overall_share": 24.7}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 8.7, "overall_goalless_pct": 7.0, "deviation_pp": 1.7}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "away", "season_share": 27.5, "overall_share": 31.8}`
- `21.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 9.4, "overall_goalless_pct": 7.0, "deviation_pp": 2.4}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 29.2, "overall_share": 24.7}`
- `23.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 4.1, "overall_goalless_pct": 7.0, "deviation_pp": 2.9}`
- `24.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.0, "overall_goalless_pct": 7.0, "deviation_pp": 3.0}`
- `25.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 48.3, "overall_share": 43.5}`
- `26.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 14, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "3-7", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `27.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 97232, "distinct": 97218, "duplicates": 14}`
- `28.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 97232, "fgt_inconsistent": 393, "fgte_inconsistent": 393, "n_with_fgt": 89451}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
