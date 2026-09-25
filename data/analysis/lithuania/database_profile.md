# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:03:24+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `lithuania`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 105 |
| teams | 1080 |
| team_aliases | 2160 |
| team_seasons | 1868 |
| matches | 19018 |
| standings | 5430 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `51`
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
| korea1 | K League 1 | South Korea | 2 | 377 |
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |
| lithuania | TOPLYGA | Lithuania | 2 | 324 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `lithuania`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 180 | 10 | 2025-02-28 | 2025-11-08 |
| 2026 | True | in_progress | 144 | 10 | 2026-02-21 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 19018 | 19018 | 0 |
| matches (league_season_id, game_index) | 19018 | 19018 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 19018 | 19004 | 14 |
| team_seasons (league_season_id, team_id) | 1868 | 1868 | 0 |
| team_seasons api_name within a season | 1868 | 1868 | 0 |
| team_seasons api_slug within a season | 1868 | 1868 | 0 |
| standings (league_season_id, team_id, view) | 5430 | 5430 | 0 |
| team_aliases (form, value) | 2160 | 2160 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1080 | 1080 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `19018`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 19018 | 0.0% |
| kickoff_time | 0 | 19018 | 0.0% |
| home_team_id | 0 | 19018 | 0.0% |
| away_team_id | 0 | 19018 | 0.0% |
| home_score | 0 | 19018 | 0.0% |
| away_score | 0 | 19018 | 0.0% |
| home_ht | 40 | 18978 | 0.2% |
| away_ht | 40 | 18978 | 0.2% |
| first_goal_time | 1357 | 17661 | 7.1% |
| first_goal_time_extra | 1357 | 17661 | 7.1% |
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
| Home | 130 | 40.1% |
| Draw | 84 | 25.9% |
| Away | 110 | 34.0% |
| Total | 324 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 860 |
| Average goals per match | 2.654 |
| Home goals | 464 (avg 1.432) |
| Away goals | 396 (avg 1.222) |
| Home goal share | 54.0% |
| Goalless matches | 29 (9.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 40.6% | 24.4% | 35.0% | 479 | 2.661 | 258 | 221 | 13 (7.2%) |
| 2026 | 144 | 39.6% | 27.8% | 32.6% | 381 | 2.646 | 206 | 175 | 16 (11.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `294` of `324` (90.7%)
| metric | value |
|---|---|
| First goals recorded | 294 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 32.58 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 87 |
| 16-30 | 67 |
| 31-45 | 60 |
| 46-60 | 39 |
| 61-75 | 23 |
| 76-90 | 12 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `60`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 10 | 1..10 | 10 |
| 2025 | goals | 10 | 1..10 | 10 |
| 2025 | luck | 10 | 1..10 | 10 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 34 |
| 0-0 | 29 |
| 2-1 | 27 |
| 0-1 | 27 |
| 1-0 | 25 |
| 1-2 | 22 |
| 2-0 | 20 |
| 0-2 | 19 |
| 2-2 | 19 |
| 3-0 | 16 |
| 1-3 | 14 |
| 3-1 | 13 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 115 | 35.5% |
| Mon | 32 | 9.9% |
| Tue | 9 | 2.8% |
| Wed | 28 | 8.6% |
| Thu | 9 | 2.8% |
| Fri | 43 | 13.3% |
| Sat | 88 | 27.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 180 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 10 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 144 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 7.2% vs overall 9.0% (deviation 1.8 pp) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 11.1% vs overall 9.0% (deviation 2.1 pp) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=18, fgte=18 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=10 positions=1..10 teams=10 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=10 positions=1..10 teams=10 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 180, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 10, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 144, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 7.2, "overall_goalless_pct": 9.0, "deviation_pp": 1.8}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 11.1, "overall_goalless_pct": 9.0, "deviation_pp": 2.1}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 19018, "distinct": 19004, "duplicates": 14}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 19018, "fgt_inconsistent": 18, "fgte_inconsistent": 18, "n_with_fgt": 17661}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
