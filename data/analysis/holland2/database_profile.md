# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:52:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `holland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 69 |
| teams | 742 |
| team_aliases | 1484 |
| team_seasons | 1275 |
| matches | 12457 |
| standings | 3651 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `33`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |
| brazil1 | Serie A Betano | Brazil | 2 | 657 |
| brazil2 | Serie B | Brazil | 2 | 679 |
| bulgaria1 | efbet League | Bulgaria | 2 | 363 |
| cha | Championship | England | 2 | 654 |
| china | Super League | China | 2 | 448 |
| czech1 | Chance Liga | Czech Republic | 2 | 351 |
| czech2 | ChNL | Czech Republic | 2 | 312 |
| czech3a | 3. CFL - Group A | Czech Republic | 2 | 337 |
| czech3b | 3. CFL - Group B | Czech Republic | 2 | 333 |
| denmark1 | Superliga | Denmark | 2 | 248 |
| develop21 | Professional Development League | England | 1 | 40 |
| egypt | Premier League | Egypt | 2 | 372 |
| eng1 | League One | England | 2 | 644 |
| eng2 | League Two | England | 2 | 651 |
| estonia | Meistriliiga | Estonia | 2 | 325 |
| finland1 | Veikkausliiga | Finland | 2 | 273 |
| finland2 | Ykkosliiga | Finland | 2 | 260 |
| france1 | Ligue 1 | France | 2 | 355 |
| france2 | Ligue 2 | France | 2 | 373 |
| france3 | Ligue 3 | France | 2 | 388 |
| germany-north | Regionalliga North | Germany | 2 | 415 |
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 450 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 297 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 474 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `holland2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 392 | 21 | 2025-08-08 | 2026-05-23 |
| 2026-2027 | True | in_progress | 82 | 20 | 2026-08-07 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 12457 | 12457 | 0 |
| matches (league_season_id, game_index) | 12457 | 12457 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 12457 | 12447 | 10 |
| team_seasons (league_season_id, team_id) | 1275 | 1275 | 0 |
| team_seasons api_name within a season | 1275 | 1275 | 0 |
| team_seasons api_slug within a season | 1275 | 1275 | 0 |
| standings (league_season_id, team_id, view) | 3651 | 3651 | 0 |
| team_aliases (form, value) | 1484 | 1484 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 742 | 742 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `12457`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 12457 | 0.0% |
| kickoff_time | 0 | 12457 | 0.0% |
| home_team_id | 0 | 12457 | 0.0% |
| away_team_id | 0 | 12457 | 0.0% |
| home_score | 0 | 12457 | 0.0% |
| away_score | 0 | 12457 | 0.0% |
| home_ht | 34 | 12423 | 0.3% |
| away_ht | 34 | 12423 | 0.3% |
| first_goal_time | 846 | 11611 | 6.8% |
| first_goal_time_extra | 846 | 11611 | 6.8% |
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
| Home | 214 | 45.1% |
| Draw | 97 | 20.5% |
| Away | 163 | 34.4% |
| Total | 474 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1551 |
| Average goals per match | 3.272 |
| Home goals | 851 (avg 1.795) |
| Away goals | 700 (avg 1.477) |
| Home goal share | 54.9% |
| Goalless matches | 16 (3.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 392 | 42.6% | 21.7% | 35.7% | 1248 | 3.184 | 678 | 570 | 14 (3.6%) |
| 2026-2027 | 82 | 57.3% | 14.6% | 28.0% | 303 | 3.695 | 173 | 130 | 2 (2.4%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `458` of `474` (96.6%)
| metric | value |
|---|---|
| First goals recorded | 458 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 27.48 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 40.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 170 |
| 16-30 | 125 |
| 31-45 | 64 |
| 46-60 | 55 |
| 61-75 | 24 |
| 76-90 | 17 |
| 91-120 | 3 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `123`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 21 | 1..21 | 21 |
| 2025-2026 | goals | 21 | 1..21 | 21 |
| 2025-2026 | luck | 21 | 1..21 | 21 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 43 |
| 2-1 | 41 |
| 1-2 | 38 |
| 1-0 | 36 |
| 2-2 | 31 |
| 0-1 | 30 |
| 2-0 | 29 |
| 3-1 | 23 |
| 3-2 | 22 |
| 1-3 | 20 |
| 2-3 | 17 |
| 0-0 | 16 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 3-6 | 9 | 1 |
| 5-3 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 39 | 8.2% |
| Mon | 88 | 18.6% |
| Tue | 28 | 5.9% |
| Wed | 5 | 1.1% |
| Thu | 2 | 0.4% |
| Fri | 262 | 55.3% |
| Sat | 50 | 10.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 392 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 21 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 82 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.695 vs overall 3.272 (deviation 0.423) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 57.3% vs overall 45.1% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 14.6% vs overall 20.5% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 28.0% vs overall 34.4% |
| 9 | HIGH_SCORING_MATCHES | 5 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=21 positions=1..21 teams=21 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=21 positions=1..21 teams=21 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=21 positions=1..21 teams=21 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 392, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 21, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 82, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.695, "overall_avg_goals": 3.272, "deviation": 0.423}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 57.3, "overall_share": 45.1}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 14.6, "overall_share": 20.5}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 28.0, "overall_share": 34.4}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 5, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 12457, "distinct": 12447, "duplicates": 10}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 12457, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 11611}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 21, "min_pos": 1, "max_pos": 21, "distinct_teams": 21}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
