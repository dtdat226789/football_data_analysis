# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:43:40+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `saudi1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 138 |
| teams | 1382 |
| team_aliases | 2764 |
| team_seasons | 2504 |
| matches | 26701 |
| standings | 7230 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `64`
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
| north | National League North | England | 2 | 668 |
| norway | Eliteserien | Norway | 2 | 408 |
| poland2 | Division 1 | Poland | 2 | 408 |
| portugal1 | Liga Portugal | Portugal | 2 | 370 |
| portugal2 | Liga Portugal 2 | Portugal | 2 | 363 |
| premier | Premier League | England | 7 | 2330 |
| primera1 | Primera RFEF - Group 1 | Spain | 2 | 438 |
| primera2 | Primera RFEF - Group 2 | Spain | 2 | 419 |
| romania1 | Superliga | Romania | 2 | 429 |
| russia | Premier League | Russia | 2 | 320 |
| saudi1 | Saudi Professional League | Saudi Arabia | 2 | 377 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `saudi1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 314 | 19 | 2025-08-28 | 2026-05-21 |
| 2026-2027 | True | in_progress | 63 | 18 | 2026-08-13 | 2026-09-13 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 26701 | 26701 | 0 |
| matches (league_season_id, game_index) | 26701 | 26701 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 26701 | 26683 | 18 |
| team_seasons (league_season_id, team_id) | 2504 | 2504 | 0 |
| team_seasons api_name within a season | 2504 | 2504 | 0 |
| team_seasons api_slug within a season | 2504 | 2504 | 0 |
| standings (league_season_id, team_id, view) | 7230 | 7230 | 0 |
| team_aliases (form, value) | 2764 | 2764 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1382 | 1382 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `26701`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 26701 | 0.0% |
| kickoff_time | 0 | 26701 | 0.0% |
| home_team_id | 0 | 26701 | 0.0% |
| away_team_id | 0 | 26701 | 0.0% |
| home_score | 0 | 26701 | 0.0% |
| away_score | 0 | 26701 | 0.0% |
| home_ht | 47 | 26654 | 0.2% |
| away_ht | 47 | 26654 | 0.2% |
| first_goal_time | 1873 | 24828 | 7.0% |
| first_goal_time_extra | 1873 | 24828 | 7.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 6 |
| away_ht | 0 | 6 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 163 | 43.2% |
| Draw | 91 | 24.1% |
| Away | 123 | 32.6% |
| Total | 377 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1117 |
| Average goals per match | 2.963 |
| Home goals | 588 (avg 1.56) |
| Away goals | 529 (avg 1.403) |
| Home goal share | 52.6% |
| Goalless matches | 26 (6.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 314 | 44.3% | 22.9% | 32.8% | 943 | 3.003 | 500 | 443 | 16 (5.1%) |
| 2026-2027 | 63 | 38.1% | 30.2% | 31.7% | 174 | 2.762 | 88 | 86 | 10 (15.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `351` of `377` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 351 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 28.23 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 132 |
| 16-30 | 85 |
| 31-45 | 55 |
| 46-60 | 48 |
| 61-75 | 14 |
| 76-90 | 12 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `111`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 19 | 1..19 | 19 |
| 2025-2026 | goals | 19 | 1..19 | 19 |
| 2025-2026 | luck | 19 | 1..19 | 19 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 45 |
| 2-1 | 34 |
| 1-0 | 30 |
| 0-0 | 26 |
| 2-0 | 24 |
| 0-1 | 24 |
| 1-2 | 22 |
| 0-2 | 17 |
| 3-1 | 17 |
| 1-3 | 16 |
| 2-2 | 16 |
| 3-2 | 14 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 36 | 9.5% |
| Mon | 25 | 6.6% |
| Tue | 32 | 8.5% |
| Wed | 29 | 7.7% |
| Thu | 70 | 18.6% |
| Fri | 86 | 22.8% |
| Sat | 99 | 26.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 314 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 19 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 5.1% vs overall 6.9% (deviation 1.8 pp) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 15.9% vs overall 6.9% (deviation 9.0 pp) |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 38.1% vs overall 43.2% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 30.2% vs overall 24.1% |
| 10 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (18 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=19 positions=1..19 teams=19 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=19 positions=1..19 teams=19 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=19 positions=1..19 teams=19 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 314, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 19, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 5.1, "overall_goalless_pct": 6.9, "deviation_pp": 1.8}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 15.9, "overall_goalless_pct": 6.9, "deviation_pp": 9.0}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 38.1, "overall_share": 43.2}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 30.2, "overall_share": 24.1}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 26701, "distinct": 26683, "duplicates": 18}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 26701, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 24828}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 19, "min_pos": 1, "max_pos": 19, "distinct_teams": 19}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
