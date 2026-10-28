# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-27T01:58:40+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `japan1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 322 |
| teams | 1209 |
| team_aliases | 2418 |
| team_seasons | 5501 |
| matches | 81797 |
| standings | 16503 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `47`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `japan1`: `8`
- With match data: `8`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 306 | 18 | 2020-02-21 | 2020-12-19 |
| 2021 | False | complete | 380 | 20 | 2021-02-26 | 2021-12-04 |
| 2022 | False | complete | 306 | 18 | 2022-02-18 | 2022-11-05 |
| 2023 | False | complete | 306 | 18 | 2023-02-17 | 2023-12-03 |
| 2024 | False | complete | 380 | 20 | 2024-02-23 | 2024-12-08 |
| 2025 | False | complete | 380 | 20 | 2025-02-14 | 2025-12-06 |
| 2026 | True | complete | 161 | 20 | 2026-02-06 | 2026-05-13 |
| 2026-2027 | True | in_progress | 120 | 20 | 2026-08-07 | 2026-10-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 81797 | 81797 | 0 |
| matches (league_season_id, game_index) | 81797 | 81797 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 81797 | 81787 | 10 |
| team_seasons (league_season_id, team_id) | 5501 | 5501 | 0 |
| team_seasons api_name within a season | 5501 | 5501 | 0 |
| team_seasons api_slug within a season | 5501 | 5501 | 0 |
| standings (league_season_id, team_id, view) | 16503 | 16503 | 0 |
| team_aliases (form, value) | 2418 | 2418 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 1209 | 1209 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `81797`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 81797 | 0.0% |
| kickoff_time | 0 | 81797 | 0.0% |
| home_team_id | 0 | 81797 | 0.0% |
| away_team_id | 0 | 81797 | 0.0% |
| home_score | 0 | 81797 | 0.0% |
| away_score | 0 | 81797 | 0.0% |
| home_ht | 419 | 81378 | 0.5% |
| away_ht | 419 | 81378 | 0.5% |
| first_goal_time | 6502 | 75295 | 7.9% |
| first_goal_time_extra | 6502 | 75295 | 7.9% |
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
| Home | 990 | 42.3% |
| Draw | 567 | 24.2% |
| Away | 782 | 33.4% |
| Total | 2339 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6077 |
| Average goals per match | 2.598 |
| Home goals | 3264 (avg 1.395) |
| Away goals | 2813 (avg 1.203) |
| Home goal share | 53.7% |
| Goalless matches | 186 (8.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 306 | 38.6% | 22.2% | 39.2% | 866 | 2.83 | 445 | 421 | 20 (6.5%) |
| 2021 | 380 | 42.1% | 24.7% | 33.2% | 920 | 2.421 | 494 | 426 | 34 (8.9%) |
| 2022 | 306 | 39.9% | 31.7% | 28.4% | 771 | 2.52 | 424 | 347 | 36 (11.8%) |
| 2023 | 306 | 42.2% | 25.5% | 32.4% | 777 | 2.539 | 418 | 359 | 24 (7.8%) |
| 2024 | 380 | 38.4% | 27.4% | 34.2% | 1013 | 2.666 | 541 | 472 | 32 (8.4%) |
| 2025 | 380 | 44.2% | 25.5% | 30.3% | 911 | 2.397 | 500 | 411 | 33 (8.7%) |
| 2026 | 161 | 58.4% | 0.0% | 41.6% | 462 | 2.87 | 248 | 214 | 0 (0.0%) |
| 2026-2027 | 120 | 44.2% | 24.2% | 31.7% | 357 | 2.975 | 194 | 163 | 7 (5.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2152` of `2339` (92.0%)
| metric | value |
|---|---|
| First goals recorded | 2152 |
| Min minute | 1 |
| Max minute | 103 |
| Mean minute | 33.63 |
| Median (p50) | 29.0 |
| p25 | 12.75 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 653 |
| 16-30 | 470 |
| 31-45 | 356 |
| 46-60 | 322 |
| 61-75 | 206 |
| 76-90 | 111 |
| 91-120 | 34 |

### 2.5 Standings coverage
- (season, view) pairs present: `24` of `24` expected
- Standings rows total: `462`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 18 | 1..19 | 18 |
| 2020 | goals | 18 | 12..34 | 18 |
| 2020 | luck | 18 | 1..36 | 18 |
| 2021 | classic | 20 | 1..20 | 20 |
| 2021 | goals | 20 | 5..35 | 20 |
| 2021 | luck | 20 | 1..40 | 20 |
| 2022 | classic | 18 | 1..18 | 18 |
| 2022 | goals | 18 | 6..33 | 18 |
| 2022 | luck | 18 | 1..35 | 18 |
| 2023 | classic | 18 | 1..18 | 18 |
| 2023 | goals | 18 | 1..18 | 18 |
| 2023 | luck | 18 | 1..18 | 18 |
| 2024 | classic | 20 | 1..20 | 20 |
| 2024 | goals | 20 | 1..20 | 20 |
| 2024 | luck | 20 | 1..20 | 20 |
| 2025 | classic | 20 | 1..21 | 20 |
| 2025 | goals | 20 | 6..37 | 20 |
| 2025 | luck | 20 | 1..40 | 20 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026 | classic | 20 | 1..22 | 20 |
| 2026 | goals | 20 | 3..27 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 20 | 1..36 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 257 |
| 1-0 | 248 |
| 2-1 | 229 |
| 0-1 | 225 |
| 0-0 | 186 |
| 1-2 | 179 |
| 2-0 | 162 |
| 0-2 | 113 |
| 2-2 | 101 |
| 3-1 | 88 |
| 3-0 | 81 |
| 1-3 | 66 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 4 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 3 |
| 5-3 | 8 | 7 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 615 | 26.3% |
| Mon | 24 | 1.0% |
| Tue | 43 | 1.8% |
| Wed | 366 | 15.6% |
| Thu | 5 | 0.2% |
| Fri | 115 | 4.9% |
| Sat | 1171 | 50.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2022 has 306 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2022 has 18 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2023 has 306 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2023 has 18 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2026 has 161 matches, expected 380 |
| 8 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 120 matches, expected 380 |
| 9 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2020 away outcome share 39.2% vs overall 33.4% |
| 11 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 11.8% vs overall 8.0% (deviation 3.8 pp) |
| 12 | OUTCOME_SHARE_OUTLIER | Season 2022 draw outcome share 31.7% vs overall 24.2% |
| 13 | OUTCOME_SHARE_OUTLIER | Season 2022 away outcome share 28.4% vs overall 33.4% |
| 14 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 0.0% vs overall 8.0% (deviation 8.0 pp) |
| 15 | OUTCOME_SHARE_OUTLIER | Season 2026 home outcome share 58.4% vs overall 42.3% |
| 16 | OUTCOME_SHARE_OUTLIER | Season 2026 draw outcome share 0.0% vs overall 24.2% |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2026 away outcome share 41.6% vs overall 33.4% |
| 18 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.975 vs overall 2.598 (deviation 0.377) |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 5.8% vs overall 8.0% (deviation 2.2 pp) |
| 20 | HIGH_SCORING_MATCHES | 21 match(es) with >= 8 total goals (extreme scorelines) |
| 21 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 22 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=366, fgte=366 rows) |
| 23 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=18 positions=1..19 teams=18 |
| 24 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=18 positions=12..34 teams=18 |
| 25 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=18 positions=1..36 teams=18 |
| 26 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=20 positions=5..35 teams=20 |
| 27 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=20 positions=1..40 teams=20 |
| 28 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=18 positions=1..18 teams=18 |
| 29 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=18 positions=6..33 teams=18 |
| 30 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=18 positions=1..35 teams=18 |
| 31 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=18 positions=1..18 teams=18 |
| 32 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=18 positions=1..18 teams=18 |
| 33 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=18 positions=1..18 teams=18 |
| 34 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=20 positions=1..21 teams=20 |
| 35 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=20 positions=6..37 teams=20 |
| 36 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=20 positions=1..40 teams=20 |
| 37 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=20 positions=1..22 teams=20 |
| 38 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=20 positions=3..27 teams=20 |
| 39 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=20 positions=1..36 teams=20 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022", "n_matches": 306, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022", "n_teams": 18, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 306, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023", "n_teams": 18, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 161, "expected": 380}`
- `8.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 120, "expected": 380}`
- `9.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020", "outcome": "away", "season_share": 39.2, "overall_share": 33.4}`
- `11.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 11.8, "overall_goalless_pct": 8.0, "deviation_pp": 3.8}`
- `12.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "draw", "season_share": 31.7, "overall_share": 24.2}`
- `13.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "away", "season_share": 28.4, "overall_share": 33.4}`
- `14.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 0.0, "overall_goalless_pct": 8.0, "deviation_pp": 8.0}`
- `15.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "home", "season_share": 58.4, "overall_share": 42.3}`
- `16.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "draw", "season_share": 0.0, "overall_share": 24.2}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "away", "season_share": 41.6, "overall_share": 33.4}`
- `18.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.975, "overall_avg_goals": 2.598, "deviation": 0.377}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 5.8, "overall_goalless_pct": 8.0, "deviation_pp": 2.2}`
- `20.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 21, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 4}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 3}, {"scoreline": "5-3", "total_goals": 8, "count": 7}, {"scoreline": "4-4", "total_goals": 8, "count": 3}, {"scoreline": "3-5", "total_goals": 8, "count": 2}]}`
- `21.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 81797, "distinct": 81787, "duplicates": 10}`
- `22.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 81797, "fgt_inconsistent": 366, "fgte_inconsistent": 366, "n_with_fgt": 75295}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 19, "distinct_teams": 18}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 18, "min_pos": 12, "max_pos": 34, "distinct_teams": 18}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 36, "distinct_teams": 18}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 20, "min_pos": 5, "max_pos": 35, "distinct_teams": 20}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 40, "distinct_teams": 20}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 18, "min_pos": 6, "max_pos": 33, "distinct_teams": 18}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 35, "distinct_teams": 18}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 21, "distinct_teams": 20}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 20, "min_pos": 6, "max_pos": 37, "distinct_teams": 20}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 40, "distinct_teams": 20}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 20, "min_pos": 3, "max_pos": 27, "distinct_teams": 20}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 36, "distinct_teams": 20}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
