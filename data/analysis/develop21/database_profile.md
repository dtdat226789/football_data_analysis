# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:48:13+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `develop21`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 35 |
| teams | 378 |
| team_aliases | 756 |
| team_seasons | 620 |
| matches | 6151 |
| standings | 1791 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `17`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `develop21`: `1`
- With match data: `1`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2026-2027 | True | in_progress | 40 | 17 | 2026-08-14 | 2026-09-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 6151 | 6151 | 0 |
| matches (league_season_id, game_index) | 6151 | 6151 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 6151 | 6146 | 5 |
| team_seasons (league_season_id, team_id) | 620 | 620 | 0 |
| team_seasons api_name within a season | 620 | 620 | 0 |
| team_seasons api_slug within a season | 620 | 620 | 0 |
| standings (league_season_id, team_id, view) | 1791 | 1791 | 0 |
| team_aliases (form, value) | 756 | 756 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 378 | 378 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `6151`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 6151 | 0.0% |
| kickoff_time | 0 | 6151 | 0.0% |
| home_team_id | 0 | 6151 | 0.0% |
| away_team_id | 0 | 6151 | 0.0% |
| home_score | 0 | 6151 | 0.0% |
| away_score | 0 | 6151 | 0.0% |
| home_ht | 8 | 6143 | 0.1% |
| away_ht | 8 | 6143 | 0.1% |
| first_goal_time | 423 | 5728 | 6.9% |
| first_goal_time_extra | 423 | 5728 | 6.9% |
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
| Home | 18 | 45.0% |
| Draw | 10 | 25.0% |
| Away | 12 | 30.0% |
| Total | 40 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 164 |
| Average goals per match | 4.1 |
| Home goals | 93 (avg 2.325) |
| Away goals | 71 (avg 1.775) |
| Home goal share | 56.7% |
| Goalless matches | 1 (2.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2026-2027 | 40 | 45.0% | 25.0% | 30.0% | 164 | 4.1 | 93 | 71 | 1 (2.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `39` of `40` (97.5%)
| metric | value |
|---|---|
| First goals recorded | 39 |
| Min minute | 1 |
| Max minute | 67 |
| Mean minute | 23.56 |
| Median (p50) | 20.0 |
| p25 | 13.5 |
| p75 | 33.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 12 |
| 16-30 | 16 |
| 31-45 | 8 |
| 46-60 | 1 |
| 61-75 | 2 |
| 76-90 | 0 |
| 91-120 | 0 |

### 2.5 Standings coverage
- (season, view) pairs present: `3` of `3` expected
- Standings rows total: `51`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2026-2027 | classic | 17 | 1..17 | 17 |
| 2026-2027 | goals | 17 | 1..17 | 17 |
| 2026-2027 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-2 | 5 |
| 3-1 | 5 |
| 0-2 | 3 |
| 4-1 | 3 |
| 2-1 | 2 |
| 1-1 | 2 |
| 2-0 | 2 |
| 3-3 | 2 |
| 1-2 | 2 |
| 5-3 | 1 |
| 2-5 | 1 |
| 0-1 | 1 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 3 | 7.5% |
| Mon | 6 | 15.0% |
| Tue | 24 | 60.0% |
| Fri | 6 | 15.0% |
| Sat | 1 | 2.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 40 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 17 teams, expected 20 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 5 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 6 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=17 positions=1..17 teams=17 |
| 8 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=17 positions=1..17 teams=17 |
| 9 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 40, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 17, "expected": 20}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `5.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 6151, "distinct": 6146, "duplicates": 5}`
- `6.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 6151, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 5728}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
