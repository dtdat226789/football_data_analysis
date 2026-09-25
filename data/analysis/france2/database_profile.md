# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:58:47+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `france2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 51 |
| teams | 533 |
| team_aliases | 1066 |
| team_seasons | 907 |
| matches | 9354 |
| standings | 2652 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `25`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `france2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 310 | 19 | 2025-08-09 | 2026-05-24 |
| 2026-2027 | True | in_progress | 63 | 18 | 2026-08-08 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 9354 | 9354 | 0 |
| matches (league_season_id, game_index) | 9354 | 9354 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 9354 | 9349 | 5 |
| team_seasons (league_season_id, team_id) | 907 | 907 | 0 |
| team_seasons api_name within a season | 907 | 907 | 0 |
| team_seasons api_slug within a season | 907 | 907 | 0 |
| standings (league_season_id, team_id, view) | 2652 | 2652 | 0 |
| team_aliases (form, value) | 1066 | 1066 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 533 | 533 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `9354`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 9354 | 0.0% |
| kickoff_time | 0 | 9354 | 0.0% |
| home_team_id | 0 | 9354 | 0.0% |
| away_team_id | 0 | 9354 | 0.0% |
| home_score | 0 | 9354 | 0.0% |
| away_score | 0 | 9354 | 0.0% |
| home_ht | 33 | 9321 | 0.4% |
| away_ht | 33 | 9321 | 0.4% |
| first_goal_time | 672 | 8682 | 7.2% |
| first_goal_time_extra | 672 | 8682 | 7.2% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 138 | 37.0% |
| Draw | 118 | 31.6% |
| Away | 117 | 31.4% |
| Total | 373 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 946 |
| Average goals per match | 2.536 |
| Home goals | 491 (avg 1.316) |
| Away goals | 455 (avg 1.22) |
| Home goal share | 51.9% |
| Goalless matches | 40 (10.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 37.7% | 30.6% | 31.6% | 784 | 2.529 | 407 | 377 | 33 (10.6%) |
| 2026-2027 | 63 | 33.3% | 36.5% | 30.2% | 162 | 2.571 | 84 | 78 | 7 (11.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `333` of `373` (89.3%)
| metric | value |
|---|---|
| First goals recorded | 333 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 31.13 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 106 |
| 16-30 | 88 |
| 31-45 | 46 |
| 46-60 | 47 |
| 61-75 | 26 |
| 76-90 | 17 |
| 91-120 | 3 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `111`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 49 |
| 1-0 | 48 |
| 0-0 | 40 |
| 0-1 | 33 |
| 2-1 | 30 |
| 1-2 | 28 |
| 2-2 | 24 |
| 2-0 | 15 |
| 0-3 | 13 |
| 0-2 | 13 |
| 1-3 | 12 |
| 3-1 | 10 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 2-6 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1 | 0.3% |
| Mon | 27 | 7.2% |
| Tue | 22 | 5.9% |
| Fri | 182 | 48.8% |
| Sat | 141 | 37.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 310 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 36.5% vs overall 31.6% |
| 7 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 310, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 36.5, "overall_share": 31.6}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 2}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 9354, "distinct": 9349, "duplicates": 5}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 9354, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 8682}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
