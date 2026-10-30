# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T04:13:21+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `spain1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 550 |
| teams | 2072 |
| team_aliases | 4148 |
| team_seasons | 9302 |
| matches | 140276 |
| standings | 27906 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `81`
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
| holland3 | Tweede Divisie | Netherlands | 7 | 1693 |
| hungary1 | NB I. | Hungary | 7 | 1253 |
| hungary2 | NB II. | Hungary | 7 | 2013 |
| india1 | ISL | India | 7 | 727 |
| ireland1 | Premier Division | Ireland | 7 | 1164 |
| ireland2 | Division 1 | Ireland | 7 | 1086 |
| italy1 | Serie A | Italy | 7 | 2368 |
| italy19 | Primavera 1 | Italy | 7 | 2000 |
| italy2 | Serie B | Italy | 7 | 2380 |
| italy3a | Serie C - Group A | Italy | 7 | 2390 |
| italy3b | Serie C - Group B | Italy | 7 | 2368 |
| japan1 | J1 League | Japan | 8 | 2339 |
| japan2 | J2 League | Japan | 6 | 2608 |
| korea1 | K League 1 | South Korea | 7 | 1320 |
| korea2 | K League 2 | South Korea | 7 | 1513 |
| kuwait | Premier League | Kuwait | 7 | 594 |
| latvia | Virsliga | Latvia | 6 | 1024 |
| lithuania | TOPLYGA | Lithuania | 7 | 1113 |
| morocco | Botola Pro | Morocco | 7 | 1485 |
| national | National League | England | 6 | 2897 |
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
| saudi2 | Division 1 | Saudi Arabia | 7 | 2061 |
| scot-champ | Championship | Scotland | 7 | 1106 |
| scot-premier | Premiership | Scotland | 7 | 1290 |
| scot1 | League One | Scotland | 7 | 1061 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1782 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1801 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1801 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1799 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1789 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1728 |
| slovenia1 | Prva liga | Slovenia | 7 | 1130 |
| south | National League South | England | 7 | 3012 |
| spain1 | LaLiga | Spain | 7 | 2380 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `spain1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-12 | 2021-05-23 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-13 | 2022-05-22 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-12 | 2023-06-04 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-11 | 2024-05-26 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-15 | 2025-05-25 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-15 | 2026-05-24 |
| 2026-2027 | True | in_progress | 100 | 20 | 2026-08-15 | 2026-10-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 140276 | 140276 | 0 |
| matches (league_season_id, game_index) | 140276 | 140276 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 140276 | 140231 | 45 |
| team_seasons (league_season_id, team_id) | 9302 | 9302 | 0 |
| team_seasons api_name within a season | 9302 | 9302 | 0 |
| team_seasons api_slug within a season | 9302 | 9302 | 0 |
| standings (league_season_id, team_id, view) | 27906 | 27906 | 0 |
| team_aliases (form, value) | 4148 | 4148 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2072 | 2072 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `140276`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 140276 | 0.0% |
| kickoff_time | 0 | 140276 | 0.0% |
| home_team_id | 0 | 140276 | 0.0% |
| away_team_id | 0 | 140276 | 0.0% |
| home_score | 0 | 140276 | 0.0% |
| away_score | 0 | 140276 | 0.0% |
| home_ht | 498 | 139778 | 0.4% |
| away_ht | 498 | 139778 | 0.4% |
| first_goal_time | 11411 | 128865 | 8.1% |
| first_goal_time_extra | 11411 | 128865 | 8.1% |
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
| Home | 1071 | 45.0% |
| Draw | 634 | 26.6% |
| Away | 675 | 28.4% |
| Total | 2380 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6181 |
| Average goals per match | 2.597 |
| Home goals | 3495 (avg 1.468) |
| Away goals | 2686 (avg 1.129) |
| Home goal share | 56.5% |
| Goalless matches | 176 (7.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 41.6% | 28.7% | 29.7% | 953 | 2.508 | 520 | 433 | 30 (7.9%) |
| 2021-2022 | 380 | 43.4% | 29.2% | 27.4% | 951 | 2.503 | 540 | 411 | 43 (11.3%) |
| 2022-2023 | 380 | 47.9% | 23.4% | 28.7% | 955 | 2.513 | 553 | 402 | 26 (6.8%) |
| 2023-2024 | 380 | 43.9% | 28.2% | 27.9% | 1005 | 2.645 | 564 | 441 | 31 (8.2%) |
| 2024-2025 | 380 | 44.5% | 25.5% | 30.0% | 995 | 2.618 | 552 | 443 | 21 (5.5%) |
| 2025-2026 | 380 | 48.9% | 24.5% | 26.6% | 1024 | 2.695 | 598 | 426 | 15 (3.9%) |
| 2026-2027 | 100 | 44.0% | 28.0% | 28.0% | 298 | 2.98 | 168 | 130 | 10 (10.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2204` of `2380` (92.6%)
| metric | value |
|---|---|
| First goals recorded | 2204 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 33.08 |
| Median (p50) | 28.0 |
| p25 | 12.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 695 |
| 16-30 | 485 |
| 31-45 | 375 |
| 46-60 | 299 |
| 61-75 | 183 |
| 76-90 | 132 |
| 91-120 | 35 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `420`
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
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 327 |
| 1-0 | 290 |
| 2-1 | 220 |
| 0-1 | 184 |
| 0-0 | 176 |
| 1-2 | 160 |
| 2-0 | 159 |
| 0-2 | 121 |
| 2-2 | 109 |
| 3-0 | 90 |
| 3-1 | 82 |
| 3-2 | 60 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 3 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 888 | 37.3% |
| Mon | 176 | 7.4% |
| Tue | 94 | 3.9% |
| Wed | 133 | 5.6% |
| Thu | 94 | 3.9% |
| Fri | 201 | 8.4% |
| Sat | 794 | 33.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 100 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 11.3% vs overall 7.4% (deviation 3.9 pp) |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 5.5% vs overall 7.4% (deviation 1.9 pp) |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 3.9% vs overall 7.4% (deviation 3.5 pp) |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.98 vs overall 2.597 (deviation 0.383) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.0% vs overall 7.4% (deviation 2.6 pp) |
| 8 | HIGH_SCORING_MATCHES | 12 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=439, fgte=439 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 100, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 11.3, "overall_goalless_pct": 7.4, "deviation_pp": 3.9}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 5.5, "overall_goalless_pct": 7.4, "deviation_pp": 1.9}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 3.9, "overall_goalless_pct": 7.4, "deviation_pp": 3.5}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.98, "overall_avg_goals": 2.597, "deviation": 0.383}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.0, "overall_goalless_pct": 7.4, "deviation_pp": 2.6}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 12, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 3}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 140276, "distinct": 140231, "duplicates": 45}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 140276, "fgt_inconsistent": 439, "fgte_inconsistent": 439, "n_with_fgt": 128865}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
