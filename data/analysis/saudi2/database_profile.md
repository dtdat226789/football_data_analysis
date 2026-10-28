# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:27:39+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `saudi2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 459 |
| teams | 1721 |
| team_aliases | 3446 |
| team_seasons | 7817 |
| matches | 118446 |
| standings | 23451 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `68`
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
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1023 |
| lithuania | TOPLYGA | Lithuania | 7 | 1112 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2885 |
| north | National League North | England | 7 | 2994 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1965 |
| portugal1 | Liga Portugal | Portugal | 2 | 388 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1911 |
| premier | Premier League | England | 7 | 2360 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1990 |
| romania1 | Superliga | Romania | 7 | 1653 |
| russia | Premier League | Russia | 7 | 1544 |
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |
| saudi2 | Division 1 | Saudi Arabia | 7 | 2054 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `saudi2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-10-20 | 2021-05-31 |
| 2021-2022 | False | complete | 380 | 20 | 2021-09-06 | 2022-05-28 |
| 2022-2023 | False | complete | 306 | 18 | 2022-08-22 | 2023-05-29 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-14 | 2024-05-28 |
| 2024-2025 | False | complete | 306 | 18 | 2024-08-19 | 2025-05-18 |
| 2025-2026 | True | complete | 309 | 18 | 2025-09-11 | 2026-05-23 |
| 2026-2027 | True | in_progress | 67 | 18 | 2026-08-21 | 2026-10-21 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 118446 | 118446 | 0 |
| matches (league_season_id, game_index) | 118446 | 118446 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 118446 | 118428 | 18 |
| team_seasons (league_season_id, team_id) | 7817 | 7817 | 0 |
| team_seasons api_name within a season | 7817 | 7817 | 0 |
| team_seasons api_slug within a season | 7817 | 7817 | 0 |
| standings (league_season_id, team_id, view) | 23451 | 23451 | 0 |
| team_aliases (form, value) | 3446 | 3446 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1721 | 1721 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `118446`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 118446 | 0.0% |
| kickoff_time | 0 | 118446 | 0.0% |
| home_team_id | 0 | 118446 | 0.0% |
| away_team_id | 0 | 118446 | 0.0% |
| home_score | 0 | 118446 | 0.0% |
| away_score | 0 | 118446 | 0.0% |
| home_ht | 486 | 117960 | 0.4% |
| away_ht | 486 | 117960 | 0.4% |
| first_goal_time | 9483 | 108963 | 8.0% |
| first_goal_time_extra | 9483 | 108963 | 8.0% |
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
| Home | 817 | 39.8% |
| Draw | 584 | 28.4% |
| Away | 653 | 31.8% |
| Total | 2054 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5108 |
| Average goals per match | 2.487 |
| Home goals | 2725 (avg 1.327) |
| Away goals | 2383 (avg 1.16) |
| Home goal share | 53.3% |
| Goalless matches | 192 (9.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.9% | 28.4% | 33.7% | 892 | 2.347 | 475 | 417 | 42 (11.1%) |
| 2021-2022 | 380 | 37.9% | 33.7% | 28.4% | 825 | 2.171 | 447 | 378 | 51 (13.4%) |
| 2022-2023 | 306 | 40.8% | 27.1% | 32.0% | 709 | 2.317 | 369 | 340 | 26 (8.5%) |
| 2023-2024 | 306 | 43.1% | 27.1% | 29.7% | 816 | 2.667 | 439 | 377 | 23 (7.5%) |
| 2024-2025 | 306 | 40.5% | 26.8% | 32.7% | 794 | 2.595 | 424 | 370 | 23 (7.5%) |
| 2025-2026 | 309 | 41.4% | 23.3% | 35.3% | 917 | 2.968 | 487 | 430 | 16 (5.2%) |
| 2026-2027 | 67 | 29.9% | 41.8% | 28.4% | 155 | 2.313 | 84 | 71 | 11 (16.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1855` of `2054` (90.3%)
| metric | value |
|---|---|
| First goals recorded | 1855 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 34.36 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 530 |
| 16-30 | 422 |
| 31-45 | 318 |
| 46-60 | 282 |
| 61-75 | 168 |
| 76-90 | 105 |
| 91-120 | 30 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `390`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 2..21 | 20 |
| 2020-2021 | goals | 20 | 12..59 | 20 |
| 2020-2021 | luck | 20 | 1..85 | 20 |
| 2021-2022 | classic | 20 | 2..21 | 20 |
| 2021-2022 | goals | 20 | 25..66 | 20 |
| 2021-2022 | luck | 20 | 1..85 | 20 |
| 2022-2023 | classic | 18 | 1..19 | 18 |
| 2022-2023 | goals | 18 | 33..63 | 18 |
| 2022-2023 | luck | 18 | 1..74 | 18 |
| 2023-2024 | classic | 18 | 1..19 | 18 |
| 2023-2024 | goals | 18 | 13..39 | 18 |
| 2023-2024 | luck | 18 | 1..51 | 18 |
| 2024-2025 | classic | 18 | 1..18 | 18 |
| 2024-2025 | goals | 18 | 5..26 | 18 |
| 2024-2025 | luck | 18 | 1..36 | 18 |
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 18 | 2..19 | 18 |
| 2026-2027 | goals | 18 | 1..19 | 18 |
| 2026-2027 | luck | 18 | 2..19 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 271 |
| 1-0 | 221 |
| 0-0 | 192 |
| 0-1 | 191 |
| 2-1 | 183 |
| 1-2 | 167 |
| 2-0 | 120 |
| 2-2 | 106 |
| 0-2 | 99 |
| 3-1 | 86 |
| 3-0 | 65 |
| 1-3 | 58 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 6-3 | 9 | 1 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 1 |
| 8-0 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 180 | 8.8% |
| Mon | 458 | 22.3% |
| Tue | 548 | 26.7% |
| Wed | 488 | 23.8% |
| Thu | 98 | 4.8% |
| Fri | 144 | 7.0% |
| Sat | 138 | 6.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 309 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 67 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 11 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 12 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 11.1% vs overall 9.3% (deviation 1.8 pp) |
| 13 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 13.4% vs overall 9.3% (deviation 4.1 pp) |
| 14 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 draw outcome share 33.7% vs overall 28.4% |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 7.5% vs overall 9.3% (deviation 1.8 pp) |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 7.5% vs overall 9.3% (deviation 1.8 pp) |
| 17 | SEASON_AVG_GOALS_OUTLIER | Season 2025-2026 avg goals 2.968 vs overall 2.487 (deviation 0.481) |
| 18 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 5.2% vs overall 9.3% (deviation 4.1 pp) |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 23.3% vs overall 28.4% |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 16.4% vs overall 9.3% (deviation 7.1 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 29.9% vs overall 39.8% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 41.8% vs overall 28.4% |
| 23 | HIGH_SCORING_MATCHES | 7 match(es) with >= 8 total goals (extreme scorelines) |
| 24 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows) |
| 25 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=425, fgte=425 rows) |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=20 positions=2..21 teams=20 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=20 positions=12..59 teams=20 |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=20 positions=1..85 teams=20 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=20 positions=2..21 teams=20 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=20 positions=25..66 teams=20 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=20 positions=1..85 teams=20 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..19 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=33..63 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..74 teams=18 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..19 teams=18 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=13..39 teams=18 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..51 teams=18 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=18 positions=1..18 teams=18 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=18 positions=5..26 teams=18 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=18 positions=1..36 teams=18 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=2..19 teams=18 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..19 teams=18 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=2..19 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 309, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 67, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `11.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `12.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 11.1, "overall_goalless_pct": 9.3, "deviation_pp": 1.8}`
- `13.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 13.4, "overall_goalless_pct": 9.3, "deviation_pp": 4.1}`
- `14.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "draw", "season_share": 33.7, "overall_share": 28.4}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 7.5, "overall_goalless_pct": 9.3, "deviation_pp": 1.8}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 7.5, "overall_goalless_pct": 9.3, "deviation_pp": 1.8}`
- `17.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025-2026", "season_avg_goals": 2.968, "overall_avg_goals": 2.487, "deviation": 0.481}`
- `18.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 5.2, "overall_goalless_pct": 9.3, "deviation_pp": 4.1}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 23.3, "overall_share": 28.4}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 16.4, "overall_goalless_pct": 9.3, "deviation_pp": 7.1}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 29.9, "overall_share": 39.8}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 41.8, "overall_share": 28.4}`
- `23.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 7, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `24.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 118446, "distinct": 118428, "duplicates": 18}`
- `25.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 118446, "fgt_inconsistent": 425, "fgte_inconsistent": 425, "n_with_fgt": 108963}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 20, "min_pos": 2, "max_pos": 21, "distinct_teams": 20}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 20, "min_pos": 12, "max_pos": 59, "distinct_teams": 20}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 85, "distinct_teams": 20}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 20, "min_pos": 2, "max_pos": 21, "distinct_teams": 20}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 20, "min_pos": 25, "max_pos": 66, "distinct_teams": 20}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 85, "distinct_teams": 20}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 33, "max_pos": 63, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 74, "distinct_teams": 18}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 13, "max_pos": 39, "distinct_teams": 18}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 51, "distinct_teams": 18}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 18, "min_pos": 5, "max_pos": 26, "distinct_teams": 18}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 36, "distinct_teams": 18}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 2, "max_pos": 19, "distinct_teams": 18}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 2, "max_pos": 19, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
