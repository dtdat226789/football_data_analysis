# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:02:36+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `japan2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 95 |
| teams | 1001 |
| team_aliases | 2002 |
| team_seasons | 1736 |
| matches | 17372 |
| standings | 5034 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `46`
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
| italy3b | Serie C - Group B | Italy | 2 | 417 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `japan2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2024 | True | complete | 380 | 20 | 2024-02-24 | 2024-11-10 |
| 2025 | True | complete | 380 | 20 | 2025-02-15 | 2025-11-29 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 17372 | 17372 | 0 |
| matches (league_season_id, game_index) | 17372 | 17372 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 17372 | 17362 | 10 |
| team_seasons (league_season_id, team_id) | 1736 | 1736 | 0 |
| team_seasons api_name within a season | 1736 | 1736 | 0 |
| team_seasons api_slug within a season | 1736 | 1736 | 0 |
| standings (league_season_id, team_id, view) | 5034 | 5034 | 0 |
| team_aliases (form, value) | 2002 | 2002 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1001 | 1001 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `17372`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 17372 | 0.0% |
| kickoff_time | 0 | 17372 | 0.0% |
| home_team_id | 0 | 17372 | 0.0% |
| away_team_id | 0 | 17372 | 0.0% |
| home_score | 0 | 17372 | 0.0% |
| away_score | 0 | 17372 | 0.0% |
| home_ht | 39 | 17333 | 0.2% |
| away_ht | 39 | 17333 | 0.2% |
| first_goal_time | 1222 | 16150 | 7.0% |
| first_goal_time_extra | 1222 | 16150 | 7.0% |
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
| Home | 298 | 39.2% |
| Draw | 197 | 25.9% |
| Away | 265 | 34.9% |
| Total | 760 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1880 |
| Average goals per match | 2.474 |
| Home goals | 1007 (avg 1.325) |
| Away goals | 873 (avg 1.149) |
| Home goal share | 53.6% |
| Goalless matches | 75 (9.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2024 | 380 | 40.8% | 23.4% | 35.8% | 946 | 2.489 | 520 | 426 | 37 (9.7%) |
| 2025 | 380 | 37.6% | 28.4% | 33.9% | 934 | 2.458 | 487 | 447 | 38 (10.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `685` of `760` (90.1%)
| metric | value |
|---|---|
| First goals recorded | 685 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 32.32 |
| Median (p50) | 27.0 |
| p25 | 13.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 206 |
| 16-30 | 167 |
| 31-45 | 132 |
| 46-60 | 85 |
| 61-75 | 48 |
| 76-90 | 34 |
| 91-120 | 13 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `120`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2024 | classic | 20 | 1..20 | 20 |
| 2024 | goals | 20 | 1..20 | 20 |
| 2024 | luck | 20 | 1..20 | 20 |
| 2025 | classic | 20 | 1..20 | 20 |
| 2025 | goals | 20 | 1..20 | 20 |
| 2025 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 89 |
| 1-1 | 79 |
| 0-1 | 77 |
| 1-2 | 76 |
| 0-0 | 75 |
| 2-1 | 58 |
| 2-0 | 50 |
| 2-2 | 38 |
| 0-2 | 36 |
| 1-3 | 22 |
| 3-1 | 22 |
| 3-0 | 22 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 334 | 43.9% |
| Mon | 13 | 1.7% |
| Tue | 20 | 2.6% |
| Wed | 23 | 3.0% |
| Fri | 18 | 2.4% |
| Sat | 352 | 46.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 2 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 3 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
- `1.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}]}`
- `2.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 17372, "distinct": 17362, "duplicates": 10}`
- `3.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 17372, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 16150}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
