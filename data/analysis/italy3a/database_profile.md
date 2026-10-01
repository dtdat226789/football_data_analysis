# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:57:55+00:00
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
| teams | 924 |
| team_aliases | 1848 |
| team_seasons | 1601 |
| matches | 16070 |
| standings | 4629 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `43`
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
| germany2 | 2. Bundesliga | Germany | 2 | 364 |
| germany3 | 3. Liga | Germany | 2 | 450 |
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 297 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 474 |
| holland3 | Tweede Divisie | Netherlands | 2 | 385 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 339 |
| ireland2 | Division 1 | Ireland | 2 | 344 |
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |
| italy3a | Serie C - Group A | Italy | 2 | 450 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `italy3a`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 380 | 20 | 2025-08-23 | 2026-04-25 |
| 2026-2027 | True | in_progress | 70 | 20 | 2026-08-21 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 16070 | 16070 | 0 |
| matches (league_season_id, game_index) | 16070 | 16070 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 16070 | 16060 | 10 |
| team_seasons (league_season_id, team_id) | 1601 | 1601 | 0 |
| team_seasons api_name within a season | 1601 | 1601 | 0 |
| team_seasons api_slug within a season | 1601 | 1601 | 0 |
| standings (league_season_id, team_id, view) | 4629 | 4629 | 0 |
| team_aliases (form, value) | 1848 | 1848 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 924 | 924 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `16070`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 16070 | 0.0% |
| kickoff_time | 0 | 16070 | 0.0% |
| home_team_id | 0 | 16070 | 0.0% |
| away_team_id | 0 | 16070 | 0.0% |
| home_score | 0 | 16070 | 0.0% |
| away_score | 0 | 16070 | 0.0% |
| home_ht | 39 | 16031 | 0.2% |
| away_ht | 39 | 16031 | 0.2% |
| first_goal_time | 1112 | 14958 | 6.9% |
| first_goal_time_extra | 1112 | 14958 | 6.9% |
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
| Home | 165 | 36.7% |
| Draw | 143 | 31.8% |
| Away | 142 | 31.6% |
| Total | 450 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1044 |
| Average goals per match | 2.32 |
| Home goals | 554 (avg 1.231) |
| Away goals | 490 (avg 1.089) |
| Home goal share | 53.1% |
| Goalless matches | 50 (11.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 37.9% | 30.3% | 31.8% | 889 | 2.339 | 474 | 415 | 37 (9.7%) |
| 2026-2027 | 70 | 30.0% | 40.0% | 30.0% | 155 | 2.214 | 80 | 75 | 13 (18.6%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `400` of `450` (88.9%)
| metric | value |
|---|---|
| First goals recorded | 400 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 33.83 |
| Median (p50) | 27.5 |
| p25 | 14.0 |
| p75 | 50.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 113 |
| 16-30 | 100 |
| 31-45 | 67 |
| 46-60 | 51 |
| 61-75 | 40 |
| 76-90 | 22 |
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
| 1-1 | 60 |
| 1-0 | 51 |
| 0-0 | 50 |
| 0-1 | 49 |
| 2-1 | 37 |
| 1-2 | 36 |
| 2-2 | 29 |
| 2-0 | 26 |
| 0-2 | 20 |
| 3-1 | 19 |
| 3-0 | 12 |
| 1-3 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 189 | 42.0% |
| Mon | 48 | 10.7% |
| Tue | 11 | 2.4% |
| Wed | 13 | 2.9% |
| Thu | 20 | 4.4% |
| Fri | 25 | 5.6% |
| Sat | 144 | 32.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 70 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 18.6% vs overall 11.1% (deviation 7.5 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 30.0% vs overall 36.7% |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 40.0% vs overall 31.8% |
| 6 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 70, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 18.6, "overall_goalless_pct": 11.1, "deviation_pp": 7.5}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 30.0, "overall_share": 36.7}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 40.0, "overall_share": 31.8}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 16070, "distinct": 16060, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 16070, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 14958}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
