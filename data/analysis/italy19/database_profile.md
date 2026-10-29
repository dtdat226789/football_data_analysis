# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T02:04:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy19`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 293 |
| teams | 1087 |
| team_aliases | 2174 |
| team_seasons | 4927 |
| matches | 72364 |
| standings | 14781 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `43`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy19`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 240 | 16 | 2020-09-18 | 2021-06-16 |
| 2021-2022 | False | complete | 306 | 18 | 2021-08-27 | 2022-05-15 |
| 2022-2023 | False | complete | 306 | 18 | 2022-08-19 | 2023-05-27 |
| 2023-2024 | False | complete | 306 | 18 | 2023-08-25 | 2024-05-19 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-16 | 2025-05-18 |
| 2025-2026 | True | complete | 382 | 20 | 2025-08-16 | 2026-05-22 |
| 2026-2027 | True | in_progress | 80 | 20 | 2026-08-22 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 72364 | 72364 | 0 |
| matches (league_season_id, game_index) | 72364 | 72364 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 72364 | 72354 | 10 |
| team_seasons (league_season_id, team_id) | 4927 | 4927 | 0 |
| team_seasons api_name within a season | 4927 | 4927 | 0 |
| team_seasons api_slug within a season | 4927 | 4927 | 0 |
| standings (league_season_id, team_id, view) | 14781 | 14781 | 0 |
| team_aliases (form, value) | 2174 | 2174 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1087 | 1087 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `72364`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 72364 | 0.0% |
| kickoff_time | 0 | 72364 | 0.0% |
| home_team_id | 0 | 72364 | 0.0% |
| away_team_id | 0 | 72364 | 0.0% |
| home_score | 0 | 72364 | 0.0% |
| away_score | 0 | 72364 | 0.0% |
| home_ht | 410 | 71954 | 0.6% |
| away_ht | 410 | 71954 | 0.6% |
| first_goal_time | 5598 | 66766 | 7.7% |
| first_goal_time_extra | 5598 | 66766 | 7.7% |
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
| Home | 858 | 42.9% |
| Draw | 513 | 25.6% |
| Away | 629 | 31.4% |
| Total | 2000 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5992 |
| Average goals per match | 2.996 |
| Home goals | 3288 (avg 1.644) |
| Away goals | 2704 (avg 1.352) |
| Home goal share | 54.9% |
| Goalless matches | 97 (4.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 240 | 40.4% | 25.4% | 34.2% | 739 | 3.079 | 408 | 331 | 12 (5.0%) |
| 2021-2022 | 306 | 46.1% | 22.2% | 31.7% | 911 | 2.977 | 496 | 415 | 11 (3.6%) |
| 2022-2023 | 306 | 44.8% | 24.5% | 30.7% | 901 | 2.944 | 505 | 396 | 16 (5.2%) |
| 2023-2024 | 306 | 45.8% | 27.1% | 27.1% | 962 | 3.144 | 545 | 417 | 12 (3.9%) |
| 2024-2025 | 380 | 42.6% | 21.6% | 35.8% | 1164 | 3.063 | 621 | 543 | 15 (3.9%) |
| 2025-2026 | 382 | 39.8% | 30.6% | 29.6% | 1051 | 2.751 | 572 | 479 | 29 (7.6%) |
| 2026-2027 | 80 | 36.2% | 33.8% | 30.0% | 264 | 3.3 | 141 | 123 | 2 (2.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `1892` of `2000` (94.6%)
| metric | value |
|---|---|
| First goals recorded | 1892 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 28.49 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 708 |
| 16-30 | 469 |
| 31-45 | 280 |
| 46-60 | 221 |
| 61-75 | 118 |
| 76-90 | 82 |
| 91-120 | 14 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `390`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 16 | 1..16 | 16 |
| 2020-2021 | goals | 16 | 1..16 | 16 |
| 2020-2021 | luck | 16 | 1..16 | 16 |
| 2021-2022 | classic | 18 | 1..18 | 18 |
| 2021-2022 | goals | 18 | 1..18 | 18 |
| 2021-2022 | luck | 18 | 1..18 | 18 |
| 2022-2023 | classic | 18 | 1..18 | 18 |
| 2022-2023 | goals | 18 | 1..18 | 18 |
| 2022-2023 | luck | 18 | 1..18 | 18 |
| 2023-2024 | classic | 18 | 1..18 | 18 |
| 2023-2024 | goals | 18 | 1..18 | 18 |
| 2023-2024 | luck | 18 | 1..18 | 18 |
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
| 1-1 | 247 |
| 1-0 | 179 |
| 2-1 | 173 |
| 1-2 | 154 |
| 0-1 | 139 |
| 2-2 | 131 |
| 2-0 | 119 |
| 0-0 | 97 |
| 3-1 | 88 |
| 0-2 | 82 |
| 3-0 | 75 |
| 1-3 | 61 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-0 | 9 | 1 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 1 |
| 5-4 | 9 | 1 |
| 4-5 | 9 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 6 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 5 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 595 | 29.8% |
| Mon | 207 | 10.3% |
| Tue | 44 | 2.2% |
| Wed | 137 | 6.8% |
| Thu | 28 | 1.4% |
| Fri | 189 | 9.4% |
| Sat | 800 | 40.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 306 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 18 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 382 matches, expected 380 |
| 10 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 80 matches, expected 380 |
| 11 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 away outcome share 27.1% vs overall 31.4% |
| 13 | OUTCOME_SHARE_OUTLIER | Season 2024-2025 away outcome share 35.8% vs overall 31.4% |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 7.6% vs overall 4.8% (deviation 2.8 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 30.6% vs overall 25.6% |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.5% vs overall 4.8% (deviation 2.3 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 36.2% vs overall 42.9% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 33.8% vs overall 25.6% |
| 19 | HIGH_SCORING_MATCHES | 23 match(es) with >= 8 total goals (extreme scorelines) |
| 20 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 21 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=360, fgte=360 rows) |
| 22 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=16 positions=1..16 teams=16 |
| 23 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=16 positions=1..16 teams=16 |
| 24 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=16 positions=1..16 teams=16 |
| 25 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=18 positions=1..18 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=18 positions=1..18 teams=18 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=18 positions=1..18 teams=18 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=18 positions=1..18 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=18 positions=1..18 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 306, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 18, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 382, "expected": 380}`
- `10.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 80, "expected": 380}`
- `11.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "away", "season_share": 27.1, "overall_share": 31.4}`
- `13.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024-2025", "outcome": "away", "season_share": 35.8, "overall_share": 31.4}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 7.6, "overall_goalless_pct": 4.8, "deviation_pp": 2.8}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 30.6, "overall_share": 25.6}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.5, "overall_goalless_pct": 4.8, "deviation_pp": 2.3}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 36.2, "overall_share": 42.9}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 33.8, "overall_share": 25.6}`
- `19.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 23, "threshold": 8, "examples": [{"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 6}, {"scoreline": "4-4", "total_goals": 8, "count": 3}]}`
- `20.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 72364, "distinct": 72354, "duplicates": 10}`
- `21.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 72364, "fgt_inconsistent": 360, "fgte_inconsistent": 360, "n_with_fgt": 66766}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
