# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:02:08+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `italy3a`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 89 |
| teams | 923 |
| team_aliases | 1846 |
| team_seasons | 1600 |
| matches | 15954 |
| standings | 4626 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `43`
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
| italy3a | Serie C - Group A | Italy | 2 | 440 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy3a`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 380 | 20 | 2025-08-23 | 2026-04-25 |
| 2026-2027 | True | in_progress | 60 | 20 | 2026-08-21 | 2026-09-21 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 15954 | 15954 | 0 |
| matches (league_season_id, game_index) | 15954 | 15954 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 15954 | 15944 | 10 |
| team_seasons (league_season_id, team_id) | 1600 | 1600 | 0 |
| team_seasons api_name within a season | 1600 | 1600 | 0 |
| team_seasons api_slug within a season | 1600 | 1600 | 0 |
| standings (league_season_id, team_id, view) | 4626 | 4626 | 0 |
| team_aliases (form, value) | 1846 | 1846 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 923 | 923 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `15954`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 15954 | 0.0% |
| kickoff_time | 0 | 15954 | 0.0% |
| home_team_id | 0 | 15954 | 0.0% |
| away_team_id | 0 | 15954 | 0.0% |
| home_score | 0 | 15954 | 0.0% |
| away_score | 0 | 15954 | 0.0% |
| home_ht | 39 | 15915 | 0.2% |
| away_ht | 39 | 15915 | 0.2% |
| first_goal_time | 1104 | 14850 | 6.9% |
| first_goal_time_extra | 1104 | 14850 | 6.9% |
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
| Home | 164 | 37.3% |
| Draw | 138 | 31.4% |
| Away | 138 | 31.4% |
| Total | 440 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1026 |
| Average goals per match | 2.332 |
| Home goals | 547 (avg 1.243) |
| Away goals | 479 (avg 1.089) |
| Home goal share | 53.3% |
| Goalless matches | 48 (10.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 37.9% | 30.3% | 31.8% | 889 | 2.339 | 474 | 415 | 37 (9.7%) |
| 2026-2027 | 60 | 33.3% | 38.3% | 28.3% | 137 | 2.283 | 73 | 64 | 11 (18.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `392` of `440` (89.1%)
| metric | value |
|---|---|
| First goals recorded | 392 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 33.52 |
| Median (p50) | 27.0 |
| p25 | 14.0 |
| p75 | 49.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 112 |
| 16-30 | 100 |
| 31-45 | 65 |
| 46-60 | 49 |
| 61-75 | 38 |
| 76-90 | 21 |
| 91-120 | 7 |

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
| 1-1 | 57 |
| 1-0 | 51 |
| 0-0 | 48 |
| 0-1 | 48 |
| 2-1 | 37 |
| 1-2 | 35 |
| 2-2 | 29 |
| 2-0 | 26 |
| 3-1 | 19 |
| 0-2 | 19 |
| 3-0 | 11 |
| 1-3 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 185 | 42.0% |
| Mon | 48 | 10.9% |
| Tue | 11 | 2.5% |
| Wed | 13 | 3.0% |
| Thu | 20 | 4.5% |
| Fri | 25 | 5.7% |
| Sat | 138 | 31.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 60 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 18.3% vs overall 10.9% (deviation 7.4 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 38.3% vs overall 31.4% |
| 5 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 6 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 7 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 60, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 18.3, "overall_goalless_pct": 10.9, "deviation_pp": 7.4}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 38.3, "overall_share": 31.4}`
- `5.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `6.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 15954, "distinct": 15944, "duplicates": 10}`
- `7.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 15954, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 14850}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
