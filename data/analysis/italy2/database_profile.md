# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:59+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 87 |
| teams | 899 |
| team_aliases | 1798 |
| team_seasons | 1560 |
| matches | 15514 |
| standings | 4506 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `42`
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
| holland2 | Eerste Divisie | Netherlands | 2 | 466 |
| holland3 | Tweede Divisie | Netherlands | 2 | 376 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 338 |
| ireland2 | Division 1 | Ireland | 2 | 339 |
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 390 | 20 | 2025-08-22 | 2026-05-29 |
| 2026-2027 | True | in_progress | 50 | 20 | 2026-08-21 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 15514 | 15514 | 0 |
| matches (league_season_id, game_index) | 15514 | 15514 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 15514 | 15504 | 10 |
| team_seasons (league_season_id, team_id) | 1560 | 1560 | 0 |
| team_seasons api_name within a season | 1560 | 1560 | 0 |
| team_seasons api_slug within a season | 1560 | 1560 | 0 |
| standings (league_season_id, team_id, view) | 4506 | 4506 | 0 |
| team_aliases (form, value) | 1798 | 1798 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 899 | 899 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `15514`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 15514 | 0.0% |
| kickoff_time | 0 | 15514 | 0.0% |
| home_team_id | 0 | 15514 | 0.0% |
| away_team_id | 0 | 15514 | 0.0% |
| home_score | 0 | 15514 | 0.0% |
| away_score | 0 | 15514 | 0.0% |
| home_ht | 39 | 15475 | 0.3% |
| away_ht | 39 | 15475 | 0.3% |
| first_goal_time | 1056 | 14458 | 6.8% |
| first_goal_time_extra | 1056 | 14458 | 6.8% |
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
| Home | 196 | 44.5% |
| Draw | 134 | 30.5% |
| Away | 110 | 25.0% |
| Total | 440 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1125 |
| Average goals per match | 2.557 |
| Home goals | 648 (avg 1.473) |
| Away goals | 477 (avg 1.084) |
| Home goal share | 57.6% |
| Goalless matches | 31 (7.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 390 | 44.9% | 31.0% | 24.1% | 993 | 2.546 | 577 | 416 | 30 (7.7%) |
| 2026-2027 | 50 | 42.0% | 26.0% | 32.0% | 132 | 2.64 | 71 | 61 | 1 (2.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `409` of `440` (93.0%)
| metric | value |
|---|---|
| First goals recorded | 409 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 32.59 |
| Median (p50) | 29.0 |
| p25 | 14.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 113 |
| 16-30 | 101 |
| 31-45 | 79 |
| 46-60 | 65 |
| 61-75 | 23 |
| 76-90 | 25 |
| 91-120 | 3 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `120`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 69 |
| 1-0 | 49 |
| 2-1 | 39 |
| 2-0 | 32 |
| 1-2 | 32 |
| 0-0 | 31 |
| 2-2 | 30 |
| 0-1 | 28 |
| 3-1 | 24 |
| 3-0 | 23 |
| 0-2 | 16 |
| 1-3 | 12 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 104 | 23.6% |
| Mon | 19 | 4.3% |
| Tue | 32 | 7.3% |
| Wed | 21 | 4.8% |
| Thu | 1 | 0.2% |
| Fri | 55 | 12.5% |
| Sat | 208 | 47.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 390 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 50 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.0% vs overall 7.0% (deviation 5.0 pp) |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 26.0% vs overall 30.5% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 32.0% vs overall 25.0% |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 390, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 50, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.0, "overall_goalless_pct": 7.0, "deviation_pp": 5.0}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 26.0, "overall_share": 30.5}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 32.0, "overall_share": 25.0}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 15514, "distinct": 15504, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 15514, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 14458}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
