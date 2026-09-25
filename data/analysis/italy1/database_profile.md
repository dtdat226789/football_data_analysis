# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:40+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 83 |
| teams | 855 |
| team_aliases | 1710 |
| team_seasons | 1480 |
| matches | 14642 |
| standings | 4266 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `40`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 380 | 20 | 2025-08-23 | 2026-05-24 |
| 2026-2027 | True | in_progress | 50 | 20 | 2026-08-22 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 14642 | 14642 | 0 |
| matches (league_season_id, game_index) | 14642 | 14642 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 14642 | 14632 | 10 |
| team_seasons (league_season_id, team_id) | 1480 | 1480 | 0 |
| team_seasons api_name within a season | 1480 | 1480 | 0 |
| team_seasons api_slug within a season | 1480 | 1480 | 0 |
| standings (league_season_id, team_id, view) | 4266 | 4266 | 0 |
| team_aliases (form, value) | 1710 | 1710 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 855 | 855 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `14642`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 14642 | 0.0% |
| kickoff_time | 0 | 14642 | 0.0% |
| home_team_id | 0 | 14642 | 0.0% |
| away_team_id | 0 | 14642 | 0.0% |
| home_score | 0 | 14642 | 0.0% |
| away_score | 0 | 14642 | 0.0% |
| home_ht | 36 | 14606 | 0.2% |
| away_ht | 36 | 14606 | 0.2% |
| first_goal_time | 985 | 13657 | 6.7% |
| first_goal_time_extra | 985 | 13657 | 6.7% |
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
| Home | 170 | 39.5% |
| Draw | 108 | 25.1% |
| Away | 152 | 35.3% |
| Total | 430 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1067 |
| Average goals per match | 2.481 |
| Home goals | 559 (avg 1.3) |
| Away goals | 508 (avg 1.181) |
| Home goal share | 52.4% |
| Goalless matches | 36 (8.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 38.9% | 26.1% | 35.0% | 922 | 2.426 | 485 | 437 | 36 (9.5%) |
| 2026-2027 | 50 | 44.0% | 18.0% | 38.0% | 145 | 2.9 | 74 | 71 | 0 (0.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `394` of `430` (91.6%)
| metric | value |
|---|---|
| First goals recorded | 394 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 32.47 |
| Median (p50) | 26.5 |
| p25 | 13.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 128 |
| 16-30 | 88 |
| 31-45 | 58 |
| 46-60 | 55 |
| 61-75 | 39 |
| 76-90 | 21 |
| 91-120 | 5 |

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
| 1-0 | 45 |
| 1-1 | 43 |
| 0-1 | 42 |
| 2-1 | 39 |
| 0-0 | 36 |
| 1-2 | 36 |
| 0-2 | 34 |
| 2-0 | 29 |
| 2-2 | 24 |
| 0-3 | 16 |
| 3-0 | 12 |
| 3-2 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 186 | 43.3% |
| Mon | 53 | 12.3% |
| Tue | 6 | 1.4% |
| Wed | 14 | 3.3% |
| Thu | 6 | 1.4% |
| Fri | 31 | 7.2% |
| Sat | 134 | 31.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 50 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.9 vs overall 2.481 (deviation 0.419) |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 0.0% vs overall 8.4% (deviation 8.4 pp) |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 44.0% vs overall 39.5% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 18.0% vs overall 25.1% |
| 7 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=8, fgte=8 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 50, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.9, "overall_avg_goals": 2.481, "deviation": 0.419}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 0.0, "overall_goalless_pct": 8.4, "deviation_pp": 8.4}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 44.0, "overall_share": 39.5}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 18.0, "overall_share": 25.1}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 14642, "distinct": 14632, "duplicates": 10}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 14642, "fgt_inconsistent": 8, "fgte_inconsistent": 8, "n_with_fgt": 13657}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
