# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:02:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `japan1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 93 |
| teams | 980 |
| team_aliases | 1960 |
| team_seasons | 1696 |
| matches | 16612 |
| standings | 4914 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `45`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `japan1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2026 | True | complete | 161 | 36 | 2026-02-06 | 2026-05-13 |
| 2026-2027 | True | in_progress | 80 | 20 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 16612 | 16612 | 0 |
| matches (league_season_id, game_index) | 16612 | 16612 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 16612 | 16602 | 10 |
| team_seasons (league_season_id, team_id) | 1696 | 1696 | 0 |
| team_seasons api_name within a season | 1696 | 1696 | 0 |
| team_seasons api_slug within a season | 1696 | 1696 | 0 |
| standings (league_season_id, team_id, view) | 4914 | 4914 | 0 |
| team_aliases (form, value) | 1960 | 1960 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 980 | 980 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `16612`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 16612 | 0.0% |
| kickoff_time | 0 | 16612 | 0.0% |
| home_team_id | 0 | 16612 | 0.0% |
| away_team_id | 0 | 16612 | 0.0% |
| home_score | 0 | 16612 | 0.0% |
| away_score | 0 | 16612 | 0.0% |
| home_ht | 39 | 16573 | 0.2% |
| away_ht | 39 | 16573 | 0.2% |
| first_goal_time | 1147 | 15465 | 6.9% |
| first_goal_time_extra | 1147 | 15465 | 6.9% |
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
| Home | 131 | 54.4% |
| Draw | 17 | 7.1% |
| Away | 93 | 38.6% |
| Total | 241 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 699 |
| Average goals per match | 2.9 |
| Home goals | 375 (avg 1.556) |
| Away goals | 324 (avg 1.344) |
| Home goal share | 53.6% |
| Goalless matches | 3 (1.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | 161 | 58.4% | 0.0% | 41.6% | 462 | 2.87 | 248 | 214 | 0 (0.0%) |
| 2026-2027 | 80 | 46.2% | 21.2% | 32.5% | 237 | 2.962 | 127 | 110 | 3 (3.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `238` of `241` (98.8%)
| metric | value |
|---|---|
| First goals recorded | 238 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 34.22 |
| Median (p50) | 31.0 |
| p25 | 13.0 |
| p75 | 51.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 66 |
| 16-30 | 51 |
| 31-45 | 46 |
| 46-60 | 41 |
| 61-75 | 19 |
| 76-90 | 14 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `168`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2026 | classic | 36 | 1..36 | 36 |
| 2026-2027 | classic | 20 | 1..20 | 20 |
| 2026 | goals | 36 | 1..36 | 36 |
| 2026-2027 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 36 | 1..36 | 36 |
| 2026-2027 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-1 | 39 |
| 1-2 | 30 |
| 1-0 | 27 |
| 2-0 | 22 |
| 0-1 | 20 |
| 3-2 | 17 |
| 0-2 | 12 |
| 3-0 | 10 |
| 1-1 | 10 |
| 2-3 | 8 |
| 1-3 | 7 |
| 3-1 | 7 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 64 | 26.6% |
| Wed | 45 | 18.7% |
| Fri | 17 | 7.1% |
| Sat | 115 | 47.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026 has 161 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2026 has 36 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 80 matches, expected 380 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026 draw outcome share 0.0% vs overall 7.1% |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.8% vs overall 1.2% (deviation 2.6 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 46.2% vs overall 54.4% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 21.2% vs overall 7.1% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 32.5% vs overall 38.6% |
| 10 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=36 positions=1..36 teams=36 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=36 positions=1..36 teams=36 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=36 positions=1..36 teams=36 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 161, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 36, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 80, "expected": 380}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "draw", "season_share": 0.0, "overall_share": 7.1}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.8, "overall_goalless_pct": 1.2, "deviation_pp": 2.6}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 46.2, "overall_share": 54.4}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 21.2, "overall_share": 7.1}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 32.5, "overall_share": 38.6}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 16612, "distinct": 16602, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 16612, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 15465}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 36, "min_pos": 1, "max_pos": 36, "distinct_teams": 36}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
