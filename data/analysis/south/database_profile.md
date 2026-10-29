# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:16:13+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `south`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 543 |
| teams | 2044 |
| team_aliases | 4092 |
| team_seasons | 9162 |
| matches | 137856 |
| standings | 27486 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `80`
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
| france1 | Ligue 1 | France | 7 | 2134 |
| france2 | Ligue 2 | France | 7 | 2226 |
| france3 | Ligue 3 | France | 7 | 1902 |
| germany-north | Regionalliga North | Germany | 7 | 1699 |
| germany1 | Bundesliga | Germany | 7 | 1690 |
| germany2 | 2. Bundesliga | Germany | 7 | 1921 |
| germany3 | 3. Liga | Germany | 7 | 2383 |
| greece1 | Super League | Greece | 7 | 1211 |
| greece2 | Super League 2 | Greece | 7 | 1836 |
| holland1 | Eredivisie | Netherlands | 7 | 1941 |
| holland2 | Eerste Divisie | Netherlands | 7 | 2412 |
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1253 |
| hungary2 | NB II. | Hungary | 7 | 2013 |
| india1 | ISL | India | 7 | 726 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2363 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2377 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2367 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 593 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1483 |
| national | National League | England | 6 | 2894 |
| north | National League North | England | 7 | 3004 |
| norway | Eliteserien | Norway | 7 | 1632 |
| poland1 | Ekstraklasa | Poland | 7 | 1876 |
| poland2 | Division 1 | Poland | 7 | 1966 |
| portugal1 | Liga Portugal | Portugal | 2 | 389 |
| portugal2 | Liga Portugal 2 | Portugal | 7 | 1912 |
| premier | Premier League | England | 7 | 2360 |
| primera1 | Primera RFEF - Group 1 | Spain | 6 | 2008 |
| primera2 | Primera RFEF - Group 2 | Spain | 6 | 1990 |
| romania1 | Superliga | Romania | 7 | 1654 |
| russia | Premier League | Russia | 7 | 1544 |
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |
| saudi2 | Division 1 | Saudi Arabia | 7 | 2058 |
| scot-champ | Championship | Scotland | 7 | 1106 |
| scot-premier | Premiership | Scotland | 7 | 1284 |
| scot1 | League One | Scotland | 7 | 1061 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1782 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1801 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1801 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1799 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1789 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1726 |
| slovenia1 | Prva liga | Slovenia | 7 | 1128 |
| south | National League South | England | 7 | 3011 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `south`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 165 | 21 | 2020-10-06 | 2021-02-16 |
| 2021-2022 | False | complete | 420 | 21 | 2021-08-14 | 2022-05-07 |
| 2022-2023 | False | complete | 552 | 24 | 2022-08-06 | 2023-04-29 |
| 2023-2024 | False | complete | 550 | 24 | 2023-08-05 | 2024-04-20 |
| 2024-2025 | False | complete | 549 | 24 | 2024-08-10 | 2025-04-26 |
| 2025-2026 | True | complete | 605 | 72 | 2025-08-09 | 2026-05-09 |
| 2026-2027 | True | in_progress | 170 | 24 | 2026-08-08 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 137856 | 137856 | 0 |
| matches (league_season_id, game_index) | 137856 | 137856 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 137856 | 137811 | 45 |
| team_seasons (league_season_id, team_id) | 9162 | 9162 | 0 |
| team_seasons api_name within a season | 9162 | 9162 | 0 |
| team_seasons api_slug within a season | 9162 | 9162 | 0 |
| standings (league_season_id, team_id, view) | 27486 | 27486 | 0 |
| team_aliases (form, value) | 4092 | 4092 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2044 | 2044 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `137856`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 137856 | 0.0% |
| kickoff_time | 0 | 137856 | 0.0% |
| home_team_id | 0 | 137856 | 0.0% |
| away_team_id | 0 | 137856 | 0.0% |
| home_score | 0 | 137856 | 0.0% |
| away_score | 0 | 137856 | 0.0% |
| home_ht | 497 | 137359 | 0.4% |
| away_ht | 497 | 137359 | 0.4% |
| first_goal_time | 11231 | 126625 | 8.1% |
| first_goal_time_extra | 11231 | 126625 | 8.1% |
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
| Home | 1303 | 43.3% |
| Draw | 717 | 23.8% |
| Away | 991 | 32.9% |
| Total | 3011 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 8555 |
| Average goals per match | 2.841 |
| Home goals | 4642 (avg 1.542) |
| Away goals | 3913 (avg 1.3) |
| Home goal share | 54.3% |
| Goalless matches | 182 (6.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 165 | 37.6% | 21.8% | 40.6% | 489 | 2.964 | 241 | 248 | 9 (5.5%) |
| 2021-2022 | 420 | 43.3% | 23.3% | 33.3% | 1242 | 2.957 | 668 | 574 | 24 (5.7%) |
| 2022-2023 | 552 | 43.5% | 22.8% | 33.7% | 1550 | 2.808 | 848 | 702 | 36 (6.5%) |
| 2023-2024 | 550 | 42.4% | 24.9% | 32.7% | 1566 | 2.847 | 851 | 715 | 32 (5.8%) |
| 2024-2025 | 549 | 42.8% | 25.5% | 31.7% | 1498 | 2.729 | 809 | 689 | 35 (6.4%) |
| 2025-2026 | 605 | 47.8% | 22.3% | 29.9% | 1709 | 2.825 | 968 | 741 | 39 (6.4%) |
| 2026-2027 | 170 | 36.5% | 26.5% | 37.1% | 501 | 2.947 | 257 | 244 | 7 (4.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2828` of `3011` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 2828 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 30.73 |
| Median (p50) | 25.0 |
| p25 | 12.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 941 |
| 16-30 | 709 |
| 31-45 | 476 |
| 46-60 | 336 |
| 61-75 | 192 |
| 76-90 | 146 |
| 91-120 | 28 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `630`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 21 | 1..21 | 21 |
| 2020-2021 | goals | 21 | 1..21 | 21 |
| 2020-2021 | luck | 21 | 1..21 | 21 |
| 2021-2022 | classic | 21 | 1..21 | 21 |
| 2021-2022 | goals | 21 | 1..21 | 21 |
| 2021-2022 | luck | 21 | 1..21 | 21 |
| 2022-2023 | classic | 24 | 1..24 | 24 |
| 2022-2023 | goals | 24 | 1..24 | 24 |
| 2022-2023 | luck | 24 | 1..24 | 24 |
| 2023-2024 | classic | 24 | 1..24 | 24 |
| 2023-2024 | goals | 24 | 1..24 | 24 |
| 2023-2024 | luck | 24 | 1..24 | 24 |
| 2024-2025 | classic | 24 | 1..24 | 24 |
| 2024-2025 | goals | 24 | 1..24 | 24 |
| 2024-2025 | luck | 24 | 1..24 | 24 |
| 2025-2026 | classic | 72 | 1..72 | 72 |
| 2025-2026 | goals | 72 | 1..72 | 72 |
| 2025-2026 | luck | 72 | 1..72 | 72 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 347 |
| 1-0 | 296 |
| 1-2 | 253 |
| 2-1 | 252 |
| 0-1 | 234 |
| 2-0 | 193 |
| 0-0 | 182 |
| 2-2 | 152 |
| 0-2 | 127 |
| 3-1 | 124 |
| 3-0 | 117 |
| 1-3 | 98 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 2-8 | 10 | 1 |
| 7-2 | 9 | 3 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 2 |
| 4-5 | 9 | 1 |
| 2-7 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 4 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 2 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 28 | 0.9% |
| Mon | 207 | 6.9% |
| Tue | 715 | 23.7% |
| Wed | 41 | 1.4% |
| Thu | 23 | 0.8% |
| Fri | 74 | 2.5% |
| Sat | 1923 | 63.9% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 165 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 420 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 21 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 552 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 24 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 550 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 24 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 549 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 24 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 605 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 72 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 170 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.6% vs overall 43.3% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 40.6% vs overall 32.9% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 home outcome share 47.8% vs overall 43.3% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.1% vs overall 6.0% (deviation 1.9 pp) |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 36.5% vs overall 43.3% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 37.1% vs overall 32.9% |
| 22 | HIGH_SCORING_MATCHES | 25 match(es) with >= 8 total goals (extreme scorelines) |
| 23 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 24 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=439, fgte=439 rows) |
| 25 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=21 positions=1..21 teams=21 |
| 26 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=21 positions=1..21 teams=21 |
| 27 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=21 positions=1..21 teams=21 |
| 28 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=21 positions=1..21 teams=21 |
| 29 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=21 positions=1..21 teams=21 |
| 30 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=21 positions=1..21 teams=21 |
| 31 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=24 positions=1..24 teams=24 |
| 32 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=24 positions=1..24 teams=24 |
| 33 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=24 positions=1..24 teams=24 |
| 34 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=24 positions=1..24 teams=24 |
| 35 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=24 positions=1..24 teams=24 |
| 36 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=24 positions=1..24 teams=24 |
| 37 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=24 positions=1..24 teams=24 |
| 38 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=24 positions=1..24 teams=24 |
| 39 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=24 positions=1..24 teams=24 |
| 40 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=72 positions=1..72 teams=72 |
| 41 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=72 positions=1..72 teams=72 |
| 42 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=72 positions=1..72 teams=72 |
| 43 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 44 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 45 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 165, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 420, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 21, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 552, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 24, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 550, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 24, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 549, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 24, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 605, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 72, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 170, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.6, "overall_share": 43.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 40.6, "overall_share": 32.9}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "home", "season_share": 47.8, "overall_share": 43.3}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.1, "overall_goalless_pct": 6.0, "deviation_pp": 1.9}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 36.5, "overall_share": 43.3}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 37.1, "overall_share": 32.9}`
- `22.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 25, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "2-8", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 3}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}]}`
- `23.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 137856, "distinct": 137811, "duplicates": 45}`
- `24.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 137856, "fgt_inconsistent": 439, "fgte_inconsistent": 439, "n_with_fgt": 126625}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
