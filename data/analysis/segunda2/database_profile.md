# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:45:37+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `segunda2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 152 |
| teams | 1491 |
| team_aliases | 2982 |
| team_seasons | 2708 |
| matches | 28690 |
| standings | 7842 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `71`
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
| saudi2 | Division 1 | Saudi Arabia | 2 | 362 |
| scot-champ | Championship | Scotland | 2 | 227 |
| scot-premier | Premiership | Scotland | 2 | 276 |
| scot1 | League One | Scotland | 2 | 230 |
| scot2 | League Two | Scotland | 2 | 228 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 2 | 333 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 2 | 333 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `segunda2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 306 | 18 | 2025-09-06 | 2026-05-03 |
| 2026-2027 | True | in_progress | 27 | 18 | 2026-09-06 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 28690 | 28690 | 0 |
| matches (league_season_id, game_index) | 28690 | 28690 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 28690 | 28670 | 20 |
| team_seasons (league_season_id, team_id) | 2708 | 2708 | 0 |
| team_seasons api_name within a season | 2708 | 2708 | 0 |
| team_seasons api_slug within a season | 2708 | 2708 | 0 |
| standings (league_season_id, team_id, view) | 7842 | 7842 | 0 |
| team_aliases (form, value) | 2982 | 2982 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1491 | 1491 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `28690`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 28690 | 0.0% |
| kickoff_time | 0 | 28690 | 0.0% |
| home_team_id | 0 | 28690 | 0.0% |
| away_team_id | 0 | 28690 | 0.0% |
| home_score | 0 | 28690 | 0.0% |
| away_score | 0 | 28690 | 0.0% |
| home_ht | 50 | 28640 | 0.2% |
| away_ht | 50 | 28640 | 0.2% |
| first_goal_time | 2034 | 26656 | 7.1% |
| first_goal_time_extra | 2034 | 26656 | 7.1% |
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
| Home | 142 | 42.6% |
| Draw | 96 | 28.8% |
| Away | 95 | 28.5% |
| Total | 333 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 842 |
| Average goals per match | 2.529 |
| Home goals | 484 (avg 1.453) |
| Away goals | 358 (avg 1.075) |
| Home goal share | 57.5% |
| Goalless matches | 31 (9.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 42.5% | 29.1% | 28.4% | 769 | 2.513 | 440 | 329 | 28 (9.2%) |
| 2026-2027 | 27 | 44.4% | 25.9% | 29.6% | 73 | 2.704 | 44 | 29 | 3 (11.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `302` of `333` (90.7%)
| metric | value |
|---|---|
| First goals recorded | 302 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 32.77 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 47.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 95 |
| 16-30 | 67 |
| 31-45 | 57 |
| 46-60 | 38 |
| 61-75 | 25 |
| 76-90 | 14 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `108`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 18 | 1..18 | 18 |
| 2025-2026 | goals | 18 | 1..18 | 18 |
| 2025-2026 | luck | 18 | 1..18 | 18 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 49 |
| 1-0 | 32 |
| 0-0 | 31 |
| 0-1 | 31 |
| 2-0 | 26 |
| 1-2 | 26 |
| 2-1 | 21 |
| 3-1 | 17 |
| 2-2 | 14 |
| 3-2 | 11 |
| 0-2 | 11 |
| 1-3 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 210 | 63.1% |
| Thu | 2 | 0.6% |
| Fri | 3 | 0.9% |
| Sat | 118 | 35.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 27 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 11.1% vs overall 9.3% (deviation 1.8 pp) |
| 7 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=27, fgte=27 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 27, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 11.1, "overall_goalless_pct": 9.3, "deviation_pp": 1.8}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 28690, "distinct": 28670, "duplicates": 20}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 28690, "fgt_inconsistent": 27, "fgte_inconsistent": 27, "n_with_fgt": 26656}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
