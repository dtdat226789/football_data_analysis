# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:50:40+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany-north`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 55 |
| teams | 607 |
| team_aliases | 1214 |
| team_seasons | 1014 |
| matches | 10207 |
| standings | 2973 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `27`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany-north`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 317 | 19 | 2025-07-25 | 2026-05-16 |
| 2026-2027 | True | in_progress | 98 | 19 | 2026-07-31 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 10207 | 10207 | 0 |
| matches (league_season_id, game_index) | 10207 | 10207 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 10207 | 10197 | 10 |
| team_seasons (league_season_id, team_id) | 1014 | 1014 | 0 |
| team_seasons api_name within a season | 1014 | 1014 | 0 |
| team_seasons api_slug within a season | 1014 | 1014 | 0 |
| standings (league_season_id, team_id, view) | 2973 | 2973 | 0 |
| team_aliases (form, value) | 1214 | 1214 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 607 | 607 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `10207`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 10207 | 0.0% |
| kickoff_time | 0 | 10207 | 0.0% |
| home_team_id | 0 | 10207 | 0.0% |
| away_team_id | 0 | 10207 | 0.0% |
| home_score | 0 | 10207 | 0.0% |
| away_score | 0 | 10207 | 0.0% |
| home_ht | 34 | 10173 | 0.3% |
| away_ht | 34 | 10173 | 0.3% |
| first_goal_time | 727 | 9480 | 7.1% |
| first_goal_time_extra | 727 | 9480 | 7.1% |
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
| Home | 174 | 41.9% |
| Draw | 90 | 21.7% |
| Away | 151 | 36.4% |
| Total | 415 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1535 |
| Average goals per match | 3.699 |
| Home goals | 812 (avg 1.957) |
| Away goals | 723 (avg 1.742) |
| Home goal share | 52.9% |
| Goalless matches | 9 (2.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 317 | 42.6% | 21.8% | 35.6% | 1152 | 3.634 | 611 | 541 | 8 (2.5%) |
| 2026-2027 | 98 | 39.8% | 21.4% | 38.8% | 383 | 3.908 | 201 | 182 | 1 (1.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `406` of `415` (97.8%)
| metric | value |
|---|---|
| First goals recorded | 406 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 26.52 |
| Median (p50) | 19.5 |
| p25 | 9.0 |
| p75 | 39.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 171 |
| 16-30 | 95 |
| 31-45 | 63 |
| 46-60 | 40 |
| 61-75 | 18 |
| 76-90 | 16 |
| 91-120 | 3 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `114`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 19 | 1..19 | 19 |
| 2026-2027 | goals | 19 | 1..19 | 19 |
| 2026-2027 | luck | 19 | 1..19 | 19 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 41 |
| 2-2 | 30 |
| 0-2 | 22 |
| 2-1 | 22 |
| 3-2 | 22 |
| 2-0 | 22 |
| 0-1 | 21 |
| 1-3 | 21 |
| 3-1 | 18 |
| 1-2 | 17 |
| 1-0 | 16 |
| 4-0 | 15 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 7-3 | 10 | 1 |
| 6-4 | 10 | 1 |
| 9-0 | 9 | 1 |
| 7-2 | 9 | 1 |
| 3-6 | 9 | 1 |
| 2-7 | 9 | 1 |
| 7-1 | 8 | 2 |
| 6-2 | 8 | 4 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 3 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 111 | 26.7% |
| Mon | 2 | 0.5% |
| Tue | 6 | 1.4% |
| Wed | 64 | 15.4% |
| Thu | 5 | 1.2% |
| Fri | 55 | 13.3% |
| Sat | 172 | 41.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 317 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 98 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 19 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 20 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=19 positions=1..19 teams=19 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=19 positions=1..19 teams=19 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=19 positions=1..19 teams=19 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 317, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 98, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 19, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 20, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "7-3", "total_goals": 10, "count": 1}, {"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "9-0", "total_goals": 9, "count": 1}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 2}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 10207, "distinct": 10197, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 10207, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 9480}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
