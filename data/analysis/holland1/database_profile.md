# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:00:21+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `holland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 67 |
| teams | 729 |
| team_aliases | 1458 |
| team_seasons | 1233 |
| matches | 11900 |
| standings | 3525 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `32`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 669 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 330 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 326 |
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 34 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 640 |
| eng2 | League Two | England | 2 | 641 |
| estonia | Meistriliiga | Estonia | 2 | 325 |
| finland1 | Veikkausliiga | Finland | 2 | 273 |
| finland2 | Ykkosliiga | Finland | 2 | 255 |
| france1 | Ligue 1 | France | 2 | 355 |
| france2 | Ligue 2 | France | 2 | 373 |
| france3 | Ligue 3 | France | 2 | 371 |
| germany-north | Regionalliga North | Germany | 2 | 408 |
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 449 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 289 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `holland1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 321 | 24 | 2025-08-08 | 2026-05-24 |
| 2026-2027 | True | in_progress | 63 | 18 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 11900 | 11900 | 0 |
| matches (league_season_id, game_index) | 11900 | 11900 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 11900 | 11890 | 10 |
| team_seasons (league_season_id, team_id) | 1233 | 1233 | 0 |
| team_seasons api_name within a season | 1233 | 1233 | 0 |
| team_seasons api_slug within a season | 1233 | 1233 | 0 |
| standings (league_season_id, team_id, view) | 3525 | 3525 | 0 |
| team_aliases (form, value) | 1458 | 1458 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 729 | 729 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `11900`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 11900 | 0.0% |
| kickoff_time | 0 | 11900 | 0.0% |
| home_team_id | 0 | 11900 | 0.0% |
| away_team_id | 0 | 11900 | 0.0% |
| home_score | 0 | 11900 | 0.0% |
| away_score | 0 | 11900 | 0.0% |
| home_ht | 34 | 11866 | 0.3% |
| away_ht | 34 | 11866 | 0.3% |
| first_goal_time | 824 | 11076 | 6.9% |
| first_goal_time_extra | 824 | 11076 | 6.9% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 162 | 42.2% |
| Draw | 100 | 26.0% |
| Away | 122 | 31.8% |
| Total | 384 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1256 |
| Average goals per match | 3.271 |
| Home goals | 684 (avg 1.781) |
| Away goals | 572 (avg 1.49) |
| Home goal share | 54.5% |
| Goalless matches | 11 (2.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 44.5% | 25.9% | 29.6% | 1016 | 3.165 | 576 | 440 | 10 (3.1%) |
| 2026-2027 | 63 | 30.2% | 27.0% | 42.9% | 240 | 3.81 | 108 | 132 | 1 (1.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `373` of `384` (97.1%)
| metric | value |
|---|---|
| First goals recorded | 373 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 27.94 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 41.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 139 |
| 16-30 | 91 |
| 31-45 | 63 |
| 46-60 | 45 |
| 61-75 | 16 |
| 76-90 | 17 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `126`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-2 | 41 |
| 1-1 | 40 |
| 2-1 | 35 |
| 1-2 | 29 |
| 2-0 | 26 |
| 0-2 | 23 |
| 1-0 | 21 |
| 0-1 | 17 |
| 3-0 | 16 |
| 3-1 | 15 |
| 2-3 | 13 |
| 0-0 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 179 | 46.6% |
| Mon | 1 | 0.3% |
| Tue | 7 | 1.8% |
| Wed | 11 | 2.9% |
| Thu | 4 | 1.0% |
| Fri | 27 | 7.0% |
| Sat | 155 | 40.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 321 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.81 vs overall 3.271 (deviation 0.539) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 30.2% vs overall 42.2% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 42.9% vs overall 31.8% |
| 9 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 321, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.81, "overall_avg_goals": 3.271, "deviation": 0.539}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 30.2, "overall_share": 42.2}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 42.9, "overall_share": 31.8}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 11900, "distinct": 11890, "duplicates": 10}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 11900, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 11076}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
