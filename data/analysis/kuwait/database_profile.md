# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T02:00:50+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `kuwait`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 349 |
| teams | 1273 |
| team_aliases | 2547 |
| team_seasons | 5878 |
| matches | 87831 |
| standings | 17634 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `51`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `kuwait`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 105 | 15 | 2020-10-15 | 2020-12-26 |
| 2021-2022 | False | complete | 90 | 10 | 2021-11-19 | 2022-04-25 |
| 2022-2023 | False | complete | 90 | 10 | 2022-08-25 | 2023-03-11 |
| 2023-2024 | False | complete | 90 | 10 | 2023-08-24 | 2024-03-08 |
| 2024-2025 | False | complete | 90 | 10 | 2024-08-08 | 2025-03-29 |
| 2025-2026 | True | complete | 98 | 10 | 2025-09-12 | 2026-06-29 |
| 2026-2027 | True | in_progress | 30 | 12 | 2026-08-25 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 87831 | 87831 | 0 |
| matches (league_season_id, game_index) | 87831 | 87831 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 87831 | 87817 | 14 |
| team_seasons (league_season_id, team_id) | 5878 | 5878 | 0 |
| team_seasons api_name within a season | 5878 | 5878 | 0 |
| team_seasons api_slug within a season | 5878 | 5878 | 0 |
| standings (league_season_id, team_id, view) | 17634 | 17634 | 0 |
| team_aliases (form, value) | 2547 | 2547 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1273 | 1273 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `87831`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 87831 | 0.0% |
| kickoff_time | 0 | 87831 | 0.0% |
| home_team_id | 0 | 87831 | 0.0% |
| away_team_id | 0 | 87831 | 0.0% |
| home_score | 0 | 87831 | 0.0% |
| away_score | 0 | 87831 | 0.0% |
| home_ht | 428 | 87403 | 0.5% |
| away_ht | 428 | 87403 | 0.5% |
| first_goal_time | 7034 | 80797 | 8.0% |
| first_goal_time_extra | 7034 | 80797 | 8.0% |
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
| Home | 239 | 40.3% |
| Draw | 140 | 23.6% |
| Away | 214 | 36.1% |
| Total | 593 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1709 |
| Average goals per match | 2.882 |
| Home goals | 890 (avg 1.501) |
| Away goals | 819 (avg 1.381) |
| Home goal share | 52.1% |
| Goalless matches | 38 (6.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 105 | 32.4% | 22.9% | 44.8% | 282 | 2.686 | 132 | 150 | 9 (8.6%) |
| 2021-2022 | 90 | 44.4% | 20.0% | 35.6% | 253 | 2.811 | 129 | 124 | 5 (5.6%) |
| 2022-2023 | 90 | 37.8% | 31.1% | 31.1% | 279 | 3.1 | 140 | 139 | 5 (5.6%) |
| 2023-2024 | 90 | 41.1% | 23.3% | 35.6% | 266 | 2.956 | 148 | 118 | 7 (7.8%) |
| 2024-2025 | 90 | 46.7% | 20.0% | 33.3% | 276 | 3.067 | 150 | 126 | 4 (4.4%) |
| 2025-2026 | 98 | 40.8% | 25.5% | 33.7% | 257 | 2.622 | 145 | 112 | 7 (7.1%) |
| 2026-2027 | 30 | 40.0% | 20.0% | 40.0% | 96 | 3.2 | 46 | 50 | 1 (3.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `554` of `593` (93.4%)
| metric | value |
|---|---|
| First goals recorded | 554 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 31.05 |
| Median (p50) | 26.5 |
| p25 | 12.0 |
| p75 | 45.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 179 |
| 16-30 | 136 |
| 31-45 | 100 |
| 46-60 | 74 |
| 61-75 | 39 |
| 76-90 | 19 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `231`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 15 | 1..16 | 15 |
| 2020-2021 | goals | 15 | 1..22 | 15 |
| 2020-2021 | luck | 15 | 1..24 | 15 |
| 2021-2022 | classic | 10 | 1..11 | 10 |
| 2021-2022 | goals | 10 | 4..15 | 10 |
| 2021-2022 | luck | 10 | 1..20 | 10 |
| 2022-2023 | classic | 10 | 1..11 | 10 |
| 2022-2023 | goals | 10 | 6..16 | 10 |
| 2022-2023 | luck | 10 | 2..20 | 10 |
| 2023-2024 | classic | 10 | 1..11 | 10 |
| 2023-2024 | goals | 10 | 4..16 | 10 |
| 2023-2024 | luck | 10 | 1..20 | 10 |
| 2024-2025 | classic | 10 | 1..11 | 10 |
| 2024-2025 | goals | 10 | 6..18 | 10 |
| 2024-2025 | luck | 10 | 1..20 | 10 |
| 2025-2026 | classic | 10 | 1..10 | 10 |
| 2025-2026 | goals | 10 | 1..10 | 10 |
| 2025-2026 | luck | 10 | 1..10 | 10 |
| 2026-2027 | classic | 12 | 1..13 | 12 |
| 2026-2027 | goals | 12 | 1..13 | 12 |
| 2026-2027 | luck | 12 | 1..13 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 72 |
| 1-0 | 53 |
| 2-1 | 48 |
| 0-1 | 44 |
| 0-0 | 38 |
| 0-2 | 36 |
| 1-2 | 36 |
| 2-0 | 31 |
| 0-3 | 24 |
| 3-1 | 24 |
| 1-3 | 23 |
| 2-2 | 22 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-1 | 10 | 1 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 3-6 | 9 | 1 |
| 7-1 | 8 | 1 |
| 4-4 | 8 | 1 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 79 | 13.3% |
| Mon | 62 | 10.5% |
| Tue | 55 | 9.3% |
| Wed | 61 | 10.3% |
| Thu | 97 | 16.4% |
| Fri | 129 | 21.8% |
| Sat | 110 | 18.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 105 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 15 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 90 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 10 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 90 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 10 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 90 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 10 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 90 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 10 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 98 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 10 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 30 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 8.6% vs overall 6.4% (deviation 2.2 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 32.4% vs overall 40.3% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 44.8% vs overall 36.1% |
| 19 | OUTCOME_SHARE_OUTLIER | Season 2021-2022 home outcome share 44.4% vs overall 40.3% |
| 20 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 31.1% vs overall 23.6% |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 31.1% vs overall 36.1% |
| 22 | GOALLESS_SHARE_OUTLIER | Season 2024-2025 goalless share 4.4% vs overall 6.4% (deviation 2.0 pp) |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 home outcome share 46.7% vs overall 40.3% |
| 24 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.3% vs overall 6.4% (deviation 3.1 pp) |
| 25 | HIGH_SCORING_MATCHES | 8 match(es) with >= 8 total goals (extreme scorelines) |
| 26 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 27 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=368, fgte=368 rows) |
| 28 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=15 positions=1..16 teams=15 |
| 29 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=15 positions=1..22 teams=15 |
| 30 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=15 positions=1..24 teams=15 |
| 31 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=10 positions=1..11 teams=10 |
| 32 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=10 positions=4..15 teams=10 |
| 33 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=10 positions=1..20 teams=10 |
| 34 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=10 positions=1..11 teams=10 |
| 35 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=10 positions=6..16 teams=10 |
| 36 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=10 positions=2..20 teams=10 |
| 37 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=10 positions=1..11 teams=10 |
| 38 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=10 positions=4..16 teams=10 |
| 39 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=10 positions=1..20 teams=10 |
| 40 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=10 positions=1..11 teams=10 |
| 41 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=10 positions=6..18 teams=10 |
| 42 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=10 positions=1..20 teams=10 |
| 43 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=10 positions=1..10 teams=10 |
| 44 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=10 positions=1..10 teams=10 |
| 45 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=10 positions=1..10 teams=10 |
| 46 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..13 teams=12 |
| 47 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..13 teams=12 |
| 48 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..13 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 105, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 15, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 90, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 10, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 90, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 10, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 90, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 10, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 90, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 10, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 98, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 10, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 30, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 8.6, "overall_goalless_pct": 6.4, "deviation_pp": 2.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 32.4, "overall_share": 40.3}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 44.8, "overall_share": 36.1}`
- `19.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2021-2022", "outcome": "home", "season_share": 44.4, "overall_share": 40.3}`
- `20.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 31.1, "overall_share": 23.6}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 31.1, "overall_share": 36.1}`
- `22.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2024-2025", "season_goalless_pct": 4.4, "overall_goalless_pct": 6.4, "deviation_pp": 2.0}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "home", "season_share": 46.7, "overall_share": 40.3}`
- `24.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.3, "overall_goalless_pct": 6.4, "deviation_pp": 3.1}`
- `25.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 8, "threshold": 8, "examples": [{"scoreline": "9-1", "total_goals": 10, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}]}`
- `26.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 87831, "distinct": 87817, "duplicates": 14}`
- `27.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 87831, "fgt_inconsistent": 368, "fgte_inconsistent": 368, "n_with_fgt": 80797}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 15, "min_pos": 1, "max_pos": 16, "distinct_teams": 15}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 15, "min_pos": 1, "max_pos": 22, "distinct_teams": 15}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 15, "min_pos": 1, "max_pos": 24, "distinct_teams": 15}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 10, "min_pos": 4, "max_pos": 15, "distinct_teams": 10}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 20, "distinct_teams": 10}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 10, "min_pos": 6, "max_pos": 16, "distinct_teams": 10}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 10, "min_pos": 2, "max_pos": 20, "distinct_teams": 10}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 10, "min_pos": 4, "max_pos": 16, "distinct_teams": 10}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 20, "distinct_teams": 10}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 11, "distinct_teams": 10}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 10, "min_pos": 6, "max_pos": 18, "distinct_teams": 10}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 20, "distinct_teams": 10}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 13, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
