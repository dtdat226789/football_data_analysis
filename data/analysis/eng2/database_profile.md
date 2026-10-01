# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:48:59+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `eng2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 41 |
| teams | 450 |
| team_aliases | 900 |
| team_seasons | 757 |
| matches | 7818 |
| standings | 2202 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `20`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `eng2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 557 | 24 | 2025-08-02 | 2026-05-25 |
| 2026-2027 | True | in_progress | 94 | 24 | 2026-08-15 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 7818 | 7818 | 0 |
| matches (league_season_id, game_index) | 7818 | 7818 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 7818 | 7813 | 5 |
| team_seasons (league_season_id, team_id) | 757 | 757 | 0 |
| team_seasons api_name within a season | 757 | 757 | 0 |
| team_seasons api_slug within a season | 757 | 757 | 0 |
| standings (league_season_id, team_id, view) | 2202 | 2202 | 0 |
| team_aliases (form, value) | 900 | 900 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 450 | 450 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `7818`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 7818 | 0.0% |
| kickoff_time | 0 | 7818 | 0.0% |
| home_team_id | 0 | 7818 | 0.0% |
| away_team_id | 0 | 7818 | 0.0% |
| home_score | 0 | 7818 | 0.0% |
| away_score | 0 | 7818 | 0.0% |
| home_ht | 8 | 7810 | 0.1% |
| away_ht | 8 | 7810 | 0.1% |
| first_goal_time | 565 | 7253 | 7.2% |
| first_goal_time_extra | 565 | 7253 | 7.2% |
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
| Home | 280 | 43.0% |
| Draw | 173 | 26.6% |
| Away | 198 | 30.4% |
| Total | 651 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1674 |
| Average goals per match | 2.571 |
| Home goals | 912 (avg 1.401) |
| Away goals | 762 (avg 1.171) |
| Home goal share | 54.5% |
| Goalless matches | 45 (6.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 41.8% | 25.0% | 33.2% | 1434 | 2.575 | 764 | 670 | 37 (6.6%) |
| 2026-2027 | 94 | 50.0% | 36.2% | 13.8% | 240 | 2.553 | 148 | 92 | 8 (8.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `606` of `651` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 606 |
| Min minute | 1 |
| Max minute | 103 |
| Mean minute | 33.25 |
| Median (p50) | 28.0 |
| p25 | 12.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 193 |
| 16-30 | 128 |
| 31-45 | 99 |
| 46-60 | 83 |
| 61-75 | 62 |
| 76-90 | 27 |
| 91-120 | 14 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `144`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 81 |
| 1-0 | 78 |
| 2-1 | 55 |
| 0-1 | 52 |
| 1-2 | 49 |
| 2-0 | 48 |
| 0-0 | 45 |
| 2-2 | 39 |
| 0-2 | 35 |
| 3-1 | 31 |
| 1-3 | 22 |
| 3-2 | 19 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-1 | 8 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 4 | 0.6% |
| Mon | 27 | 4.1% |
| Tue | 90 | 13.8% |
| Wed | 7 | 1.1% |
| Thu | 17 | 2.6% |
| Fri | 33 | 5.1% |
| Sat | 473 | 72.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 557 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 94 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 8.5% vs overall 6.9% (deviation 1.6 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 50.0% vs overall 43.0% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 36.2% vs overall 26.6% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 13.8% vs overall 30.4% |
| 10 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=5, fgte=5 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 557, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 94, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 8.5, "overall_goalless_pct": 6.9, "deviation_pp": 1.6}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 50.0, "overall_share": 43.0}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 36.2, "overall_share": 26.6}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 13.8, "overall_share": 30.4}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 7818, "distinct": 7813, "duplicates": 5}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 7818, "fgt_inconsistent": 5, "fgte_inconsistent": 5, "n_with_fgt": 7253}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
