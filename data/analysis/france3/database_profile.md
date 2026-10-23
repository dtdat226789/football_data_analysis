# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:50:25+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `france3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 53 |
| teams | 584 |
| team_aliases | 1168 |
| team_seasons | 976 |
| matches | 9792 |
| standings | 2859 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `26`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `france3`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 303 | 50 | 2025-08-08 | 2026-05-15 |
| 2026-2027 | True | in_progress | 85 | 19 | 2026-08-07 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 9792 | 9792 | 0 |
| matches (league_season_id, game_index) | 9792 | 9792 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 9792 | 9782 | 10 |
| team_seasons (league_season_id, team_id) | 976 | 976 | 0 |
| team_seasons api_name within a season | 976 | 976 | 0 |
| team_seasons api_slug within a season | 976 | 976 | 0 |
| standings (league_season_id, team_id, view) | 2859 | 2859 | 0 |
| team_aliases (form, value) | 1168 | 1168 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 584 | 584 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `9792`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 9792 | 0.0% |
| kickoff_time | 0 | 9792 | 0.0% |
| home_team_id | 0 | 9792 | 0.0% |
| away_team_id | 0 | 9792 | 0.0% |
| home_score | 0 | 9792 | 0.0% |
| away_score | 0 | 9792 | 0.0% |
| home_ht | 34 | 9758 | 0.3% |
| away_ht | 34 | 9758 | 0.3% |
| first_goal_time | 718 | 9074 | 7.3% |
| first_goal_time_extra | 718 | 9074 | 7.3% |
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
| Home | 140 | 36.1% |
| Draw | 126 | 32.5% |
| Away | 122 | 31.4% |
| Total | 388 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 943 |
| Average goals per match | 2.43 |
| Home goals | 491 (avg 1.265) |
| Away goals | 452 (avg 1.165) |
| Home goal share | 52.1% |
| Goalless matches | 42 (10.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 303 | 36.0% | 33.0% | 31.0% | 738 | 2.436 | 384 | 354 | 32 (10.6%) |
| 2026-2027 | 85 | 36.5% | 30.6% | 32.9% | 205 | 2.412 | 107 | 98 | 10 (11.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `345` of `388` (88.9%)
| metric | value |
|---|---|
| First goals recorded | 345 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 29.41 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 121 |
| 16-30 | 88 |
| 31-45 | 53 |
| 46-60 | 42 |
| 61-75 | 27 |
| 76-90 | 9 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `207`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 50 | 1..50 | 50 |
| 2025-2026 | goals | 50 | 1..50 | 50 |
| 2025-2026 | luck | 50 | 1..50 | 50 |
| 2026-2027 | classic | 19 | 1..19 | 19 |
| 2026-2027 | goals | 19 | 1..19 | 19 |
| 2026-2027 | luck | 19 | 1..19 | 19 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 61 |
| 0-0 | 42 |
| 1-2 | 35 |
| 1-0 | 34 |
| 2-1 | 32 |
| 0-1 | 26 |
| 2-0 | 24 |
| 2-2 | 21 |
| 0-3 | 19 |
| 0-2 | 18 |
| 3-0 | 16 |
| 3-1 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Tue | 11 | 2.8% |
| Thu | 20 | 5.2% |
| Fri | 286 | 73.7% |
| Sat | 71 | 18.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 303 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 50 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 85 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 19 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=50 positions=1..50 teams=50 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=50 positions=1..50 teams=50 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=50 positions=1..50 teams=50 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=19 positions=1..19 teams=19 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=19 positions=1..19 teams=19 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=19 positions=1..19 teams=19 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 303, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 50, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 85, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 19, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 9792, "distinct": 9782, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 9792, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 9074}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 50, "min_pos": 1, "max_pos": 50, "distinct_teams": 50}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
