# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:03:43+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `national`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 109 |
| teams | 1126 |
| team_aliases | 2252 |
| team_seasons | 1949 |
| matches | 20171 |
| standings | 5673 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `53`
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
| morocco | Botola Pro | Morocco | 2 | 488 |
| national | National League | England | 2 | 665 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `national`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 557 | 24 | 2025-08-09 | 2026-05-10 |
| 2026-2027 | True | in_progress | 108 | 24 | 2026-08-08 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 20171 | 20171 | 0 |
| matches (league_season_id, game_index) | 20171 | 20171 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 20171 | 20157 | 14 |
| team_seasons (league_season_id, team_id) | 1949 | 1949 | 0 |
| team_seasons api_name within a season | 1949 | 1949 | 0 |
| team_seasons api_slug within a season | 1949 | 1949 | 0 |
| standings (league_season_id, team_id, view) | 5673 | 5673 | 0 |
| team_aliases (form, value) | 2252 | 2252 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1126 | 1126 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `20171`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 20171 | 0.0% |
| kickoff_time | 0 | 20171 | 0.0% |
| home_team_id | 0 | 20171 | 0.0% |
| away_team_id | 0 | 20171 | 0.0% |
| home_score | 0 | 20171 | 0.0% |
| away_score | 0 | 20171 | 0.0% |
| home_ht | 41 | 20130 | 0.2% |
| away_ht | 41 | 20130 | 0.2% |
| first_goal_time | 1438 | 18733 | 7.1% |
| first_goal_time_extra | 1438 | 18733 | 7.1% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 293 | 44.1% |
| Draw | 149 | 22.4% |
| Away | 223 | 33.5% |
| Total | 665 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1951 |
| Average goals per match | 2.934 |
| Home goals | 1057 (avg 1.589) |
| Away goals | 894 (avg 1.344) |
| Home goal share | 54.2% |
| Goalless matches | 29 (4.4%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 557 | 43.4% | 23.0% | 33.6% | 1626 | 2.919 | 883 | 743 | 28 (5.0%) |
| 2026-2027 | 108 | 47.2% | 19.4% | 33.3% | 325 | 3.009 | 174 | 151 | 1 (0.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `635` of `665` (95.5%)
| metric | value |
|---|---|
| First goals recorded | 635 |
| Min minute | 1 |
| Max minute | 108 |
| Mean minute | 31.63 |
| Median (p50) | 24.0 |
| p25 | 12.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 205 |
| 16-30 | 162 |
| 31-45 | 92 |
| 46-60 | 87 |
| 61-75 | 46 |
| 76-90 | 27 |
| 91-120 | 16 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `144`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 24 | 1..24 | 24 |
| 2025-2026 | goals | 24 | 1..24 | 24 |
| 2025-2026 | luck | 24 | 1..24 | 24 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 77 |
| 1-0 | 65 |
| 2-1 | 64 |
| 1-2 | 56 |
| 0-2 | 40 |
| 0-1 | 38 |
| 2-0 | 35 |
| 2-2 | 32 |
| 0-0 | 29 |
| 3-2 | 25 |
| 3-0 | 24 |
| 1-3 | 24 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 3-6 | 9 | 1 |
| 7-1 | 8 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 2 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 9 | 1.4% |
| Mon | 35 | 5.3% |
| Tue | 112 | 16.8% |
| Wed | 56 | 8.4% |
| Thu | 1 | 0.2% |
| Fri | 39 | 5.9% |
| Sat | 413 | 62.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 557 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 24 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 108 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 0.9% vs overall 4.4% (deviation 3.5 pp) |
| 7 | HIGH_SCORING_MATCHES | 7 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=19, fgte=19 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=24 positions=1..24 teams=24 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=24 positions=1..24 teams=24 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=24 positions=1..24 teams=24 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 557, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 24, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 108, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 0.9, "overall_goalless_pct": 4.4, "deviation_pp": 3.5}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 7, "threshold": 8, "examples": [{"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 20171, "distinct": 20157, "duplicates": 14}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 20171, "fgt_inconsistent": 19, "fgte_inconsistent": 19, "n_with_fgt": 18733}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
