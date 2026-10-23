# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:49:42+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `finland2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 47 |
| teams | 494 |
| team_aliases | 988 |
| team_seasons | 831 |
| matches | 8676 |
| standings | 2424 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `23`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `finland2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 135 | 20 | 2025-04-21 | 2025-10-18 |
| 2026 | True | in_progress | 125 | 10 | 2026-04-03 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 8676 | 8676 | 0 |
| matches (league_season_id, game_index) | 8676 | 8676 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 8676 | 8671 | 5 |
| team_seasons (league_season_id, team_id) | 831 | 831 | 0 |
| team_seasons api_name within a season | 831 | 831 | 0 |
| team_seasons api_slug within a season | 831 | 831 | 0 |
| standings (league_season_id, team_id, view) | 2424 | 2424 | 0 |
| team_aliases (form, value) | 988 | 988 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 494 | 494 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `8676`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 8676 | 0.0% |
| kickoff_time | 0 | 8676 | 0.0% |
| home_team_id | 0 | 8676 | 0.0% |
| away_team_id | 0 | 8676 | 0.0% |
| home_score | 0 | 8676 | 0.0% |
| away_score | 0 | 8676 | 0.0% |
| home_ht | 31 | 8645 | 0.4% |
| away_ht | 31 | 8645 | 0.4% |
| first_goal_time | 606 | 8070 | 7.0% |
| first_goal_time_extra | 606 | 8070 | 7.0% |
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
| Home | 110 | 42.3% |
| Draw | 64 | 24.6% |
| Away | 86 | 33.1% |
| Total | 260 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 764 |
| Average goals per match | 2.938 |
| Home goals | 401 (avg 1.542) |
| Away goals | 363 (avg 1.396) |
| Home goal share | 52.5% |
| Goalless matches | 14 (5.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 135 | 43.0% | 25.9% | 31.1% | 443 | 3.281 | 235 | 208 | 5 (3.7%) |
| 2026 | 125 | 41.6% | 23.2% | 35.2% | 321 | 2.568 | 166 | 155 | 9 (7.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `246` of `260` (94.6%)
| metric | value |
|---|---|
| First goals recorded | 246 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 29.53 |
| Median (p50) | 20.5 |
| p25 | 11.0 |
| p75 | 45.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 93 |
| 16-30 | 59 |
| 31-45 | 32 |
| 46-60 | 32 |
| 61-75 | 19 |
| 76-90 | 7 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `90`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 20 | 1..20 | 20 |
| 2025 | goals | 20 | 1..20 | 20 |
| 2025 | luck | 20 | 1..20 | 20 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 30 |
| 2-1 | 23 |
| 1-0 | 23 |
| 0-1 | 22 |
| 3-1 | 18 |
| 2-2 | 16 |
| 0-2 | 16 |
| 1-2 | 16 |
| 0-0 | 14 |
| 2-0 | 11 |
| 0-3 | 9 |
| 3-0 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 5-3 | 8 | 2 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 40 | 15.4% |
| Mon | 16 | 6.2% |
| Tue | 8 | 3.1% |
| Wed | 20 | 7.7% |
| Thu | 9 | 3.5% |
| Fri | 75 | 28.8% |
| Sat | 92 | 35.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 135 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026 has 125 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 3.7% vs overall 5.4% (deviation 1.7 pp) |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2026 avg goals 2.568 vs overall 2.938 (deviation 0.370) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 7.2% vs overall 5.4% (deviation 1.8 pp) |
| 8 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 135, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 125, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 3.7, "overall_goalless_pct": 5.4, "deviation_pp": 1.7}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026", "season_avg_goals": 2.568, "overall_avg_goals": 2.938, "deviation": 0.37}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 7.2, "overall_goalless_pct": 5.4, "deviation_pp": 1.8}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 8676, "distinct": 8671, "duplicates": 5}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 8676, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 8070}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
