# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:49:28+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `finland1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 45 |
| teams | 475 |
| team_aliases | 950 |
| team_seasons | 801 |
| matches | 8416 |
| standings | 2334 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `22`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `finland1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 132 | 12 | 2025-04-05 | 2025-08-31 |
| 2026 | True | in_progress | 141 | 12 | 2026-04-04 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 8416 | 8416 | 0 |
| matches (league_season_id, game_index) | 8416 | 8416 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 8416 | 8411 | 5 |
| team_seasons (league_season_id, team_id) | 801 | 801 | 0 |
| team_seasons api_name within a season | 801 | 801 | 0 |
| team_seasons api_slug within a season | 801 | 801 | 0 |
| standings (league_season_id, team_id, view) | 2334 | 2334 | 0 |
| team_aliases (form, value) | 950 | 950 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 475 | 475 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `8416`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 8416 | 0.0% |
| kickoff_time | 0 | 8416 | 0.0% |
| home_team_id | 0 | 8416 | 0.0% |
| away_team_id | 0 | 8416 | 0.0% |
| home_score | 0 | 8416 | 0.0% |
| away_score | 0 | 8416 | 0.0% |
| home_ht | 31 | 8385 | 0.4% |
| away_ht | 31 | 8385 | 0.4% |
| first_goal_time | 592 | 7824 | 7.0% |
| first_goal_time_extra | 592 | 7824 | 7.0% |
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
| Home | 119 | 43.6% |
| Draw | 67 | 24.5% |
| Away | 87 | 31.9% |
| Total | 273 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 789 |
| Average goals per match | 2.89 |
| Home goals | 421 (avg 1.542) |
| Away goals | 368 (avg 1.348) |
| Home goal share | 53.4% |
| Goalless matches | 18 (6.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 132 | 42.4% | 22.0% | 35.6% | 433 | 3.28 | 222 | 211 | 8 (6.1%) |
| 2026 | 141 | 44.7% | 27.0% | 28.4% | 356 | 2.525 | 199 | 157 | 10 (7.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `255` of `273` (93.4%)
| metric | value |
|---|---|
| First goals recorded | 255 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 29.95 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 85 |
| 16-30 | 62 |
| 31-45 | 43 |
| 46-60 | 37 |
| 61-75 | 15 |
| 76-90 | 11 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `72`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 12 | 1..12 | 12 |
| 2025 | goals | 12 | 1..12 | 12 |
| 2025 | luck | 12 | 1..12 | 12 |
| 2026 | classic | 12 | 1..12 | 12 |
| 2026 | goals | 12 | 1..12 | 12 |
| 2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 32 |
| 1-0 | 26 |
| 2-1 | 23 |
| 0-1 | 22 |
| 0-0 | 18 |
| 3-2 | 17 |
| 2-2 | 16 |
| 3-0 | 14 |
| 1-2 | 13 |
| 2-0 | 12 |
| 0-2 | 12 |
| 3-1 | 10 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-2 | 10 | 1 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 47 | 17.2% |
| Mon | 25 | 9.2% |
| Tue | 12 | 4.4% |
| Wed | 22 | 8.1% |
| Thu | 2 | 0.7% |
| Fri | 36 | 13.2% |
| Sat | 129 | 47.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 132 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 141 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2025 avg goals 3.28 vs overall 2.89 (deviation 0.390) |
| 7 | SEASON_AVG_GOALS_OUTLIER | Season 2026 avg goals 2.525 vs overall 2.89 (deviation 0.365) |
| 8 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=12 positions=1..12 teams=12 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=12 positions=1..12 teams=12 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=12 positions=1..12 teams=12 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 132, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 141, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2025", "season_avg_goals": 3.28, "overall_avg_goals": 2.89, "deviation": 0.39}`
- `7.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026", "season_avg_goals": 2.525, "overall_avg_goals": 2.89, "deviation": 0.365}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "8-2", "total_goals": 10, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 8416, "distinct": 8411, "duplicates": 5}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 8416, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 7824}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
