# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:59:58+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `greece1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 63 |
| teams | 681 |
| team_aliases | 1362 |
| team_seasons | 1155 |
| matches | 11227 |
| standings | 3291 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `30`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `greece1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 246 | 15 | 2025-08-23 | 2026-05-21 |
| 2026-2027 | True | in_progress | 35 | 14 | 2026-08-22 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 11227 | 11227 | 0 |
| matches (league_season_id, game_index) | 11227 | 11227 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 11227 | 11217 | 10 |
| team_seasons (league_season_id, team_id) | 1155 | 1155 | 0 |
| team_seasons api_name within a season | 1155 | 1155 | 0 |
| team_seasons api_slug within a season | 1155 | 1155 | 0 |
| standings (league_season_id, team_id, view) | 3291 | 3291 | 0 |
| team_aliases (form, value) | 1362 | 1362 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 681 | 681 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `11227`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 11227 | 0.0% |
| kickoff_time | 0 | 11227 | 0.0% |
| home_team_id | 0 | 11227 | 0.0% |
| away_team_id | 0 | 11227 | 0.0% |
| home_score | 0 | 11227 | 0.0% |
| away_score | 0 | 11227 | 0.0% |
| home_ht | 34 | 11193 | 0.3% |
| away_ht | 34 | 11193 | 0.3% |
| first_goal_time | 790 | 10437 | 7.0% |
| first_goal_time_extra | 790 | 10437 | 7.0% |
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
| Home | 116 | 41.3% |
| Draw | 77 | 27.4% |
| Away | 88 | 31.3% |
| Total | 281 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 712 |
| Average goals per match | 2.534 |
| Home goals | 399 (avg 1.42) |
| Away goals | 313 (avg 1.114) |
| Home goal share | 56.0% |
| Goalless matches | 24 (8.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 246 | 41.5% | 27.6% | 30.9% | 624 | 2.537 | 346 | 278 | 22 (8.9%) |
| 2026-2027 | 35 | 40.0% | 25.7% | 34.3% | 88 | 2.514 | 53 | 35 | 2 (5.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `257` of `281` (91.5%)
| metric | value |
|---|---|
| First goals recorded | 257 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 31.1 |
| Median (p50) | 27.0 |
| p25 | 14.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 75 |
| 16-30 | 66 |
| 31-45 | 51 |
| 46-60 | 31 |
| 61-75 | 23 |
| 76-90 | 7 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `87`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 15 | 1..15 | 15 |
| 2025-2026 | goals | 15 | 1..15 | 15 |
| 2025-2026 | luck | 15 | 1..15 | 15 |
| 2026-2027 | classic | 14 | 1..14 | 14 |
| 2026-2027 | goals | 14 | 1..14 | 14 |
| 2026-2027 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 41 |
| 0-0 | 24 |
| 0-1 | 24 |
| 1-0 | 23 |
| 1-2 | 20 |
| 3-0 | 19 |
| 0-2 | 18 |
| 2-1 | 18 |
| 2-0 | 18 |
| 3-1 | 13 |
| 2-2 | 11 |
| 3-2 | 8 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 153 | 54.4% |
| Mon | 13 | 4.6% |
| Tue | 3 | 1.1% |
| Wed | 13 | 4.6% |
| Thu | 4 | 1.4% |
| Sat | 95 | 33.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 246 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 15 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 35 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 14 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 5.7% vs overall 8.5% (deviation 2.8 pp) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=15 positions=1..15 teams=15 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=15 positions=1..15 teams=15 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=15 positions=1..15 teams=15 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=14 positions=1..14 teams=14 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=14 positions=1..14 teams=14 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 246, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 15, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 35, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 14, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 5.7, "overall_goalless_pct": 8.5, "deviation_pp": 2.8}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 11227, "distinct": 11217, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 11227, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 10437}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 15, "min_pos": 1, "max_pos": 15, "distinct_teams": 15}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
