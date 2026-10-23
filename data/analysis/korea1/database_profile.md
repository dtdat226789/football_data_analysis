# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:59:57+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `korea1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 97 |
| teams | 1016 |
| team_aliases | 2032 |
| team_seasons | 1761 |
| matches | 17875 |
| standings | 5109 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `47`
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
| italy3b | Serie C - Group B | Italy | 2 | 426 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |
| korea1 | K League 1 | South Korea | 2 | 378 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `korea1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 198 | 12 | 2025-02-15 | 2025-10-18 |
| 2026 | True | in_progress | 180 | 12 | 2026-02-28 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 17875 | 17875 | 0 |
| matches (league_season_id, game_index) | 17875 | 17875 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 17875 | 17865 | 10 |
| team_seasons (league_season_id, team_id) | 1761 | 1761 | 0 |
| team_seasons api_name within a season | 1761 | 1761 | 0 |
| team_seasons api_slug within a season | 1761 | 1761 | 0 |
| standings (league_season_id, team_id, view) | 5109 | 5109 | 0 |
| team_aliases (form, value) | 2032 | 2032 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1016 | 1016 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `17875`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 17875 | 0.0% |
| kickoff_time | 0 | 17875 | 0.0% |
| home_team_id | 0 | 17875 | 0.0% |
| away_team_id | 0 | 17875 | 0.0% |
| home_score | 0 | 17875 | 0.0% |
| away_score | 0 | 17875 | 0.0% |
| home_ht | 39 | 17836 | 0.2% |
| away_ht | 39 | 17836 | 0.2% |
| first_goal_time | 1268 | 16607 | 7.1% |
| first_goal_time_extra | 1268 | 16607 | 7.1% |
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
| Home | 137 | 36.2% |
| Draw | 113 | 29.9% |
| Away | 128 | 33.9% |
| Total | 378 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 952 |
| Average goals per match | 2.519 |
| Home goals | 484 (avg 1.28) |
| Away goals | 468 (avg 1.238) |
| Home goal share | 50.8% |
| Goalless matches | 37 (9.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 198 | 41.9% | 26.3% | 31.8% | 512 | 2.586 | 275 | 237 | 16 (8.1%) |
| 2026 | 180 | 30.0% | 33.9% | 36.1% | 440 | 2.444 | 209 | 231 | 21 (11.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `341` of `378` (90.2%)
| metric | value |
|---|---|
| First goals recorded | 341 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 35.26 |
| Median (p50) | 32.0 |
| p25 | 14.0 |
| p75 | 51.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 92 |
| 16-30 | 75 |
| 31-45 | 67 |
| 46-60 | 46 |
| 61-75 | 33 |
| 76-90 | 21 |
| 91-120 | 7 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `72`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 12 | 1..12 | 12 |
| 2025 | goals | 12 | 1..12 | 12 |
| 2025 | luck | 12 | 1..12 | 12 |
| 2026 | classic | 12 | 1..12 | 12 |
| 2026 | goals | 12 | 1..12 | 12 |
| 2026 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 54 |
| 0-1 | 38 |
| 0-0 | 37 |
| 1-0 | 33 |
| 1-2 | 32 |
| 2-1 | 32 |
| 2-0 | 22 |
| 2-2 | 21 |
| 3-2 | 16 |
| 0-2 | 14 |
| 3-1 | 14 |
| 1-3 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 127 | 33.6% |
| Mon | 4 | 1.1% |
| Tue | 35 | 9.3% |
| Wed | 32 | 8.5% |
| Fri | 15 | 4.0% |
| Sat | 165 | 43.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 198 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 180 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 8.1% vs overall 9.8% (deviation 1.7 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2025 home outcome share 41.9% vs overall 36.2% |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 11.7% vs overall 9.8% (deviation 1.9 pp) |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026 home outcome share 30.0% vs overall 36.2% |
| 10 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=12 positions=1..12 teams=12 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=12 positions=1..12 teams=12 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=12 positions=1..12 teams=12 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 198, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 180, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 8.1, "overall_goalless_pct": 9.8, "deviation_pp": 1.7}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025", "outcome": "home", "season_share": 41.9, "overall_share": 36.2}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 11.7, "overall_goalless_pct": 9.8, "deviation_pp": 1.9}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "home", "season_share": 30.0, "overall_share": 36.2}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 17875, "distinct": 17865, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 17875, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 16607}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
