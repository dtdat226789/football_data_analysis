# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:36:29+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `india1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 265 |
| teams | 988 |
| team_aliases | 1976 |
| team_seasons | 4518 |
| matches | 65663 |
| standings | 13554 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `39`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `india1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 110 | 11 | 2020-11-20 | 2021-02-28 |
| 2021-2022 | False | complete | 110 | 11 | 2021-11-19 | 2022-03-07 |
| 2022-2023 | False | complete | 110 | 11 | 2022-10-07 | 2023-02-26 |
| 2023-2024 | False | complete | 132 | 12 | 2023-09-21 | 2024-04-15 |
| 2024-2025 | False | complete | 156 | 13 | 2024-09-13 | 2025-03-12 |
| 2025-2026 | True | complete | 91 | 14 | 2026-02-14 | 2026-05-21 |
| 2026-2027 | True | in_progress | 14 | 13 | 2026-10-10 | 2026-10-24 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 65663 | 65663 | 0 |
| matches (league_season_id, game_index) | 65663 | 65663 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 65663 | 65653 | 10 |
| team_seasons (league_season_id, team_id) | 4518 | 4518 | 0 |
| team_seasons api_name within a season | 4518 | 4518 | 0 |
| team_seasons api_slug within a season | 4518 | 4518 | 0 |
| standings (league_season_id, team_id, view) | 13554 | 13554 | 0 |
| team_aliases (form, value) | 1976 | 1976 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 988 | 988 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `65663`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 65663 | 0.0% |
| kickoff_time | 0 | 65663 | 0.0% |
| home_team_id | 0 | 65663 | 0.0% |
| away_team_id | 0 | 65663 | 0.0% |
| home_score | 0 | 65663 | 0.0% |
| away_score | 0 | 65663 | 0.0% |
| home_ht | 400 | 65263 | 0.6% |
| away_ht | 400 | 65263 | 0.6% |
| first_goal_time | 5162 | 60501 | 7.9% |
| first_goal_time_extra | 5162 | 60501 | 7.9% |
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
| Home | 295 | 40.8% |
| Draw | 192 | 26.6% |
| Away | 236 | 32.6% |
| Total | 723 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2036 |
| Average goals per match | 2.816 |
| Home goals | 1061 (avg 1.467) |
| Away goals | 975 (avg 1.349) |
| Home goal share | 52.1% |
| Goalless matches | 52 (7.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 110 | 29.1% | 38.2% | 32.7% | 286 | 2.6 | 144 | 142 | 13 (11.8%) |
| 2021-2022 | 110 | 40.0% | 28.2% | 31.8% | 344 | 3.127 | 174 | 170 | 5 (4.5%) |
| 2022-2023 | 110 | 47.3% | 14.5% | 38.2% | 334 | 3.036 | 174 | 160 | 3 (2.7%) |
| 2023-2024 | 132 | 45.5% | 24.2% | 30.3% | 363 | 2.75 | 194 | 169 | 9 (6.8%) |
| 2024-2025 | 156 | 42.3% | 24.4% | 33.3% | 448 | 2.872 | 232 | 216 | 11 (7.1%) |
| 2025-2026 | 91 | 38.5% | 31.9% | 29.7% | 221 | 2.429 | 124 | 97 | 10 (11.0%) |
| 2026-2027 | 14 | 42.9% | 28.6% | 28.6% | 40 | 2.857 | 19 | 21 | 1 (7.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `670` of `723` (92.7%)
| metric | value |
|---|---|
| First goals recorded | 670 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 30.91 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 243 |
| 16-30 | 142 |
| 31-45 | 103 |
| 46-60 | 91 |
| 61-75 | 49 |
| 76-90 | 35 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `255`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 11 | 1..11 | 11 |
| 2020-2021 | goals | 11 | 1..11 | 11 |
| 2020-2021 | luck | 11 | 1..11 | 11 |
| 2021-2022 | classic | 11 | 1..11 | 11 |
| 2021-2022 | goals | 11 | 1..11 | 11 |
| 2021-2022 | luck | 11 | 1..11 | 11 |
| 2022-2023 | classic | 11 | 1..11 | 11 |
| 2022-2023 | goals | 11 | 1..11 | 11 |
| 2022-2023 | luck | 11 | 1..11 | 11 |
| 2023-2024 | classic | 12 | 1..12 | 12 |
| 2023-2024 | goals | 12 | 1..12 | 12 |
| 2023-2024 | luck | 12 | 1..12 | 12 |
| 2024-2025 | classic | 13 | 1..13 | 13 |
| 2024-2025 | goals | 13 | 1..13 | 13 |
| 2024-2025 | luck | 13 | 1..13 | 13 |
| 2025-2026 | classic | 14 | 1..14 | 14 |
| 2025-2026 | goals | 14 | 1..14 | 14 |
| 2025-2026 | luck | 14 | 1..14 | 14 |
| 2026-2027 | classic | 13 | 1..13 | 13 |
| 2026-2027 | goals | 13 | 1..13 | 13 |
| 2026-2027 | luck | 13 | 1..13 | 13 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 90 |
| 1-0 | 69 |
| 2-1 | 64 |
| 0-0 | 52 |
| 0-1 | 51 |
| 1-2 | 47 |
| 2-0 | 40 |
| 2-2 | 38 |
| 0-2 | 36 |
| 3-1 | 29 |
| 3-0 | 28 |
| 1-3 | 25 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-5 | 11 | 1 |
| 6-4 | 10 | 1 |
| 3-7 | 10 | 1 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 133 | 18.4% |
| Mon | 74 | 10.2% |
| Tue | 61 | 8.4% |
| Wed | 74 | 10.2% |
| Thu | 96 | 13.3% |
| Fri | 106 | 14.7% |
| Sat | 179 | 24.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2020-2021 has 110 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2020-2021 has 11 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2021-2022 has 110 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2021-2022 has 11 teams, expected 20 |
| 5 | MATCH_COUNT_UNEXPECTED | Season 2022-2023 has 110 matches, expected 380 |
| 6 | TEAM_COUNT_UNEXPECTED | Season 2022-2023 has 11 teams, expected 20 |
| 7 | MATCH_COUNT_UNEXPECTED | Season 2023-2024 has 132 matches, expected 380 |
| 8 | TEAM_COUNT_UNEXPECTED | Season 2023-2024 has 12 teams, expected 20 |
| 9 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 156 matches, expected 380 |
| 10 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 13 teams, expected 20 |
| 11 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 91 matches, expected 380 |
| 12 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 14 teams, expected 20 |
| 13 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 14 matches, expected 380 |
| 14 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 13 teams, expected 20 |
| 15 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 16 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 11.8% vs overall 7.2% (deviation 4.6 pp) |
| 17 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 29.1% vs overall 40.8% |
| 18 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 draw outcome share 38.2% vs overall 26.6% |
| 19 | GOALLESS_SHARE_OUTLIER | Season 2021-2022 goalless share 4.5% vs overall 7.2% (deviation 2.7 pp) |
| 20 | GOALLESS_SHARE_OUTLIER | Season 2022-2023 goalless share 2.7% vs overall 7.2% (deviation 4.5 pp) |
| 21 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 47.3% vs overall 40.8% |
| 22 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 draw outcome share 14.5% vs overall 26.6% |
| 23 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 38.2% vs overall 32.6% |
| 24 | OUTCOME_SHARE_OUTLIER | Season 2023-2024 home outcome share 45.5% vs overall 40.8% |
| 25 | SEASON_AVG_GOALS_OUTLIER | Season 2025-2026 avg goals 2.429 vs overall 2.816 (deviation 0.387) |
| 26 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 11.0% vs overall 7.2% (deviation 3.8 pp) |
| 27 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 31.9% vs overall 26.6% |
| 28 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 29 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 30 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=345, fgte=345 rows) |
| 31 | STANDINGS_INCOMPLETE | Standings 2020-2021/classic rows=11 positions=1..11 teams=11 |
| 32 | STANDINGS_INCOMPLETE | Standings 2020-2021/goals rows=11 positions=1..11 teams=11 |
| 33 | STANDINGS_INCOMPLETE | Standings 2020-2021/luck rows=11 positions=1..11 teams=11 |
| 34 | STANDINGS_INCOMPLETE | Standings 2021-2022/classic rows=11 positions=1..11 teams=11 |
| 35 | STANDINGS_INCOMPLETE | Standings 2021-2022/goals rows=11 positions=1..11 teams=11 |
| 36 | STANDINGS_INCOMPLETE | Standings 2021-2022/luck rows=11 positions=1..11 teams=11 |
| 37 | STANDINGS_INCOMPLETE | Standings 2022-2023/classic rows=11 positions=1..11 teams=11 |
| 38 | STANDINGS_INCOMPLETE | Standings 2022-2023/goals rows=11 positions=1..11 teams=11 |
| 39 | STANDINGS_INCOMPLETE | Standings 2022-2023/luck rows=11 positions=1..11 teams=11 |
| 40 | STANDINGS_INCOMPLETE | Standings 2023-2024/classic rows=12 positions=1..12 teams=12 |
| 41 | STANDINGS_INCOMPLETE | Standings 2023-2024/goals rows=12 positions=1..12 teams=12 |
| 42 | STANDINGS_INCOMPLETE | Standings 2023-2024/luck rows=12 positions=1..12 teams=12 |
| 43 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=13 positions=1..13 teams=13 |
| 44 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=13 positions=1..13 teams=13 |
| 45 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=13 positions=1..13 teams=13 |
| 46 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=14 positions=1..14 teams=14 |
| 47 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=14 positions=1..14 teams=14 |
| 48 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=14 positions=1..14 teams=14 |
| 49 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=13 positions=1..13 teams=13 |
| 50 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=13 positions=1..13 teams=13 |
| 51 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=13 positions=1..13 teams=13 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_matches": 110, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2020-2021", "n_teams": 11, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_matches": 110, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2021-2022", "n_teams": 11, "expected": 20}`
- `5.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_matches": 110, "expected": 380}`
- `6.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2022-2023", "n_teams": 11, "expected": 20}`
- `7.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_matches": 132, "expected": 380}`
- `8.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2023-2024", "n_teams": 12, "expected": 20}`
- `9.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 156, "expected": 380}`
- `10.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 13, "expected": 20}`
- `11.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 91, "expected": 380}`
- `12.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 14, "expected": 20}`
- `13.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 14, "expected": 380}`
- `14.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 13, "expected": 20}`
- `15.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `16.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 11.8, "overall_goalless_pct": 7.2, "deviation_pp": 4.6}`
- `17.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 29.1, "overall_share": 40.8}`
- `18.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "draw", "season_share": 38.2, "overall_share": 26.6}`
- `19.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021-2022", "season_goalless_pct": 4.5, "overall_goalless_pct": 7.2, "deviation_pp": 2.7}`
- `20.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022-2023", "season_goalless_pct": 2.7, "overall_goalless_pct": 7.2, "deviation_pp": 4.5}`
- `21.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 47.3, "overall_share": 40.8}`
- `22.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "draw", "season_share": 14.5, "overall_share": 26.6}`
- `23.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 38.2, "overall_share": 32.6}`
- `24.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2023-2024", "outcome": "home", "season_share": 45.5, "overall_share": 40.8}`
- `25.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025-2026", "season_avg_goals": 2.429, "overall_avg_goals": 2.816, "deviation": 0.387}`
- `26.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 11.0, "overall_goalless_pct": 7.2, "deviation_pp": 3.8}`
- `27.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 31.9, "overall_share": 26.6}`
- `28.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "6-5", "total_goals": 11, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "3-7", "total_goals": 10, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `29.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 65663, "distinct": 65653, "duplicates": 10}`
- `30.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 65663, "fgt_inconsistent": 345, "fgte_inconsistent": 345, "n_with_fgt": 60501}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `32.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `33.` `STANDINGS_INCOMPLETE` details: `{"season": "2020-2021", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `34.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `35.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `36.` `STANDINGS_INCOMPLETE` details: `{"season": "2021-2022", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `37.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `38.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `39.` `STANDINGS_INCOMPLETE` details: `{"season": "2022-2023", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `40.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `41.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `42.` `STANDINGS_INCOMPLETE` details: `{"season": "2023-2024", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `43.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `44.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `45.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `46.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `47.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `48.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `49.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `50.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `51.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
