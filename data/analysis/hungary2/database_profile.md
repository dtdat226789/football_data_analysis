# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:03+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `hungary2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 75 |
| teams | 798 |
| team_aliases | 1596 |
| team_seasons | 1373 |
| matches | 13288 |
| standings | 3945 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `36`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `hungary2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 240 | 16 | 2025-07-27 | 2026-05-17 |
| 2026-2027 | True | in_progress | 61 | 16 | 2026-07-25 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 13288 | 13288 | 0 |
| matches (league_season_id, game_index) | 13288 | 13288 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 13288 | 13278 | 10 |
| team_seasons (league_season_id, team_id) | 1373 | 1373 | 0 |
| team_seasons api_name within a season | 1373 | 1373 | 0 |
| team_seasons api_slug within a season | 1373 | 1373 | 0 |
| standings (league_season_id, team_id, view) | 3945 | 3945 | 0 |
| team_aliases (form, value) | 1596 | 1596 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 798 | 798 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `13288`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 13288 | 0.0% |
| kickoff_time | 0 | 13288 | 0.0% |
| home_team_id | 0 | 13288 | 0.0% |
| away_team_id | 0 | 13288 | 0.0% |
| home_score | 0 | 13288 | 0.0% |
| away_score | 0 | 13288 | 0.0% |
| home_ht | 35 | 13253 | 0.3% |
| away_ht | 35 | 13253 | 0.3% |
| first_goal_time | 878 | 12410 | 6.6% |
| first_goal_time_extra | 878 | 12410 | 6.6% |
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
| Home | 137 | 45.5% |
| Draw | 74 | 24.6% |
| Away | 90 | 29.9% |
| Total | 301 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 774 |
| Average goals per match | 2.571 |
| Home goals | 426 (avg 1.415) |
| Away goals | 348 (avg 1.156) |
| Home goal share | 55.0% |
| Goalless matches | 17 (5.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 43.8% | 25.0% | 31.2% | 602 | 2.508 | 322 | 280 | 15 (6.2%) |
| 2026-2027 | 61 | 52.5% | 23.0% | 24.6% | 172 | 2.82 | 104 | 68 | 2 (3.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `284` of `301` (94.4%)
| metric | value |
|---|---|
| First goals recorded | 284 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 31.63 |
| Median (p50) | 27.0 |
| p25 | 12.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 95 |
| 16-30 | 62 |
| 31-45 | 55 |
| 46-60 | 34 |
| 61-75 | 16 |
| 76-90 | 20 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 39 |
| 1-0 | 35 |
| 2-1 | 32 |
| 0-1 | 27 |
| 2-0 | 24 |
| 0-2 | 19 |
| 1-2 | 18 |
| 0-0 | 17 |
| 2-2 | 16 |
| 3-1 | 11 |
| 0-3 | 11 |
| 3-0 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 215 | 71.4% |
| Mon | 20 | 6.6% |
| Wed | 1 | 0.3% |
| Fri | 1 | 0.3% |
| Sat | 64 | 21.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 61 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.3% vs overall 5.6% (deviation 2.3 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 52.5% vs overall 45.5% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 24.6% vs overall 29.9% |
| 9 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 61, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.3, "overall_goalless_pct": 5.6, "deviation_pp": 2.3}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 52.5, "overall_share": 45.5}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 24.6, "overall_share": 29.9}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 13288, "distinct": 13278, "duplicates": 10}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 13288, "fgt_inconsistent": 7, "fgte_inconsistent": 7, "n_with_fgt": 12410}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
