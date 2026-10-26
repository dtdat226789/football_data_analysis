# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:51:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `thai1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 591 |
| teams | 2170 |
| team_aliases | 4344 |
| team_seasons | 9928 |
| matches | 149836 |
| standings | 29784 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `87`
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
| russia | Premier League | Russia | 7 | 1541 |
| saudi1 | Saudi Professional League | Saudi Arabia | 7 | 1737 |
| saudi2 | Division 1 | Saudi Arabia | 7 | 2054 |
| scot-champ | Championship | Scotland | 7 | 1105 |
| scot-premier | Premiership | Scotland | 7 | 1282 |
| scot1 | League One | Scotland | 7 | 1060 |
| scot2 | League Two | Scotland | 7 | 1053 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 7 | 1779 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 7 | 1797 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 7 | 1795 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 7 | 1794 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 7 | 1784 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 7 | 1725 |
| slovenia1 | Prva liga | Slovenia | 7 | 1126 |
| south | National League South | England | 7 | 3000 |
| spain1 | LaLiga | Spain | 7 | 2375 |
| spain2 | LaLiga2 | Spain | 7 | 2935 |
| sweden1 | Allsvenskan | Sweden | 7 | 1638 |
| sweden2 | Superettan | Sweden | 7 | 1660 |
| swiss1 | Super League | Switzerland | 7 | 1229 |
| swiss2 | Challenge League | Switzerland | 7 | 1140 |
| thai1 | Thai League 1 | Thailand | 6 | 1244 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `thai1`: `6`
- With match data: `6`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2021-2022 | False | complete | 240 | 16 | 2021-09-03 | 2022-05-04 |
| 2022-2023 | False | complete | 240 | 16 | 2022-08-12 | 2023-05-12 |
| 2023-2024 | False | complete | 240 | 16 | 2023-08-11 | 2024-05-26 |
| 2024-2025 | False | complete | 240 | 16 | 2024-08-09 | 2025-04-30 |
| 2025-2026 | True | complete | 240 | 16 | 2025-08-15 | 2026-05-10 |
| 2026-2027 | True | in_progress | 44 | 16 | 2026-09-04 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 149836 | 149836 | 0 |
| matches (league_season_id, game_index) | 149836 | 149836 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 149836 | 149791 | 45 |
| team_seasons (league_season_id, team_id) | 9928 | 9928 | 0 |
| team_seasons api_name within a season | 9928 | 9928 | 0 |
| team_seasons api_slug within a season | 9928 | 9928 | 0 |
| standings (league_season_id, team_id, view) | 29784 | 29784 | 0 |
| team_aliases (form, value) | 4344 | 4344 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 2170 | 2170 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `149836`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 149836 | 0.0% |
| kickoff_time | 0 | 149836 | 0.0% |
| home_team_id | 0 | 149836 | 0.0% |
| away_team_id | 0 | 149836 | 0.0% |
| home_score | 0 | 149836 | 0.0% |
| away_score | 0 | 149836 | 0.0% |
| home_ht | 503 | 149333 | 0.3% |
| away_ht | 503 | 149333 | 0.3% |
| first_goal_time | 12126 | 137710 | 8.1% |
| first_goal_time_extra | 12126 | 137710 | 8.1% |
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
| Home | 579 | 46.5% |
| Draw | 336 | 27.0% |
| Away | 329 | 26.4% |
| Total | 1244 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 3502 |
| Average goals per match | 2.815 |
| Home goals | 2035 (avg 1.636) |
| Away goals | 1467 (avg 1.179) |
| Home goal share | 58.1% |
| Goalless matches | 85 (6.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2021-2022 | 240 | 45.4% | 26.7% | 27.9% | 615 | 2.562 | 339 | 276 | 19 (7.9%) |
| 2022-2023 | 240 | 48.8% | 26.2% | 25.0% | 647 | 2.696 | 372 | 275 | 15 (6.2%) |
| 2023-2024 | 240 | 46.7% | 27.5% | 25.8% | 736 | 3.067 | 444 | 292 | 17 (7.1%) |
| 2024-2025 | 240 | 49.2% | 25.4% | 25.4% | 732 | 3.05 | 432 | 300 | 16 (6.7%) |
| 2025-2026 | 240 | 43.3% | 31.2% | 25.4% | 642 | 2.675 | 380 | 262 | 17 (7.1%) |
| 2026-2027 | 44 | 43.2% | 15.9% | 40.9% | 130 | 2.955 | 68 | 62 | 1 (2.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1159` of `1244` (93.2%)
| metric | value |
|---|---|
| First goals recorded | 1159 |
| Min minute | 1 |
| Max minute | 107 |
| Mean minute | 31.34 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 379 |
| 16-30 | 271 |
| 31-45 | 198 |
| 46-60 | 159 |
| 61-75 | 84 |
| 76-90 | 51 |
| 91-120 | 17 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `288`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
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
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 168 |
| 1-0 | 129 |
| 2-1 | 116 |
| 2-0 | 89 |
| 1-2 | 87 |
| 0-0 | 85 |
| 0-1 | 76 |
| 2-2 | 72 |
| 3-1 | 58 |
| 3-0 | 43 |
| 0-2 | 42 |
| 1-3 | 35 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-7 | 11 | 1 |
| 8-2 | 10 | 1 |
| 9-0 | 9 | 1 |
| 8-1 | 9 | 1 |
| 7-2 | 9 | 1 |
| 8-0 | 8 | 2 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 501 | 40.3% |
| Mon | 28 | 2.3% |
| Tue | 18 | 1.4% |
| Wed | 68 | 5.5% |
| Thu | 19 | 1.5% |
| Fri | 106 | 8.5% |
| Sat | 504 | 40.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 240 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 16 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 240 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 16 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 240 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 16 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 44 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 13 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 14 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 31.2% vs overall 27.0% |
| 15 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.3% vs overall 6.8% (deviation 4.5 pp) |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 15.9% vs overall 27.0% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 40.9% vs overall 26.4% |
| 18 | HIGH_SCORING_MATCHES | 14 match(es) with >= 8 total goals (extreme scorelines) |
| 19 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 20 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=443, fgte=443 rows) |
| 21 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=16 positions=1..16 teams=16 |
| 22 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=16 positions=1..16 teams=16 |
| 23 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=16 positions=1..16 teams=16 |
| 26 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=16 positions=1..16 teams=16 |
| 27 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=16 positions=1..16 teams=16 |
| 28 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=16 positions=1..16 teams=16 |
| 29 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=16 positions=1..16 teams=16 |
| 30 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=16 positions=1..16 teams=16 |
| 31 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=16 positions=1..16 teams=16 |
| 32 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=16 positions=1..16 teams=16 |
| 33 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 34 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 35 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 36 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 240, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 16, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 240, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 16, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 240, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 16, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 44, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `13.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `14.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 31.2, "overall_share": 27.0}`
- `15.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.3, "overall_goalless_pct": 6.8, "deviation_pp": 4.5}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 15.9, "overall_share": 27.0}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 40.9, "overall_share": 26.4}`
- `18.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 14, "threshold": 8, "examples": [{"scoreline": "4-7", "total_goals": 11, "count": 1}, {"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "8-1", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 2}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `19.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 149836, "distinct": 149791, "duplicates": 45}`
- `20.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 149836, "fgt_inconsistent": 443, "fgte_inconsistent": 443, "n_with_fgt": 137710}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
