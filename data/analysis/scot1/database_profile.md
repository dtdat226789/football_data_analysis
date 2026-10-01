# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:06:14+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `scot1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 147 |
| teams | 1436 |
| team_aliases | 2872 |
| team_seasons | 2615 |
| matches | 27970 |
| standings | 7563 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `68`
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
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |
| lithuania | TOPLYGA | Lithuania | 2 | 324 |
| morocco | Botola Pro | Morocco | 3 | 488 |
| national | National League | England | 2 | 677 |
| north | National League North | England | 2 | 680 |
| norway | Eliteserien | Norway | 2 | 408 |
| poland2 | Division 1 | Poland | 2 | 408 |
| portugal1 | Liga Portugal | Portugal | 2 | 370 |
| portugal2 | Liga Portugal 2 | Portugal | 2 | 363 |
| premier | Premier League | England | 7 | 2330 |
| primera1 | Primera RFEF - Group 1 | Spain | 2 | 448 |
| primera2 | Primera RFEF - Group 2 | Spain | 2 | 429 |
| romania1 | Superliga | Romania | 2 | 429 |
| russia | Premier League | Russia | 2 | 320 |
| saudi1 | Saudi Professional League | Saudi Arabia | 2 | 377 |
| saudi2 | Division 1 | Saudi Arabia | 2 | 362 |
| scot-champ | Championship | Scotland | 2 | 231 |
| scot-premier | Premiership | Scotland | 2 | 276 |
| scot1 | League One | Scotland | 2 | 230 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `scot1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 191 | 14 | 2025-08-02 | 2026-05-15 |
| 2026-2027 | True | in_progress | 39 | 10 | 2026-08-01 | 2026-09-19 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 27970 | 27970 | 0 |
| matches (league_season_id, game_index) | 27970 | 27970 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 27970 | 27950 | 20 |
| team_seasons (league_season_id, team_id) | 2615 | 2615 | 0 |
| team_seasons api_name within a season | 2615 | 2615 | 0 |
| team_seasons api_slug within a season | 2615 | 2615 | 0 |
| standings (league_season_id, team_id, view) | 7563 | 7563 | 0 |
| team_aliases (form, value) | 2872 | 2872 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1436 | 1436 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `27970`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 27970 | 0.0% |
| kickoff_time | 0 | 27970 | 0.0% |
| home_team_id | 0 | 27970 | 0.0% |
| away_team_id | 0 | 27970 | 0.0% |
| home_score | 0 | 27970 | 0.0% |
| away_score | 0 | 27970 | 0.0% |
| home_ht | 49 | 27921 | 0.2% |
| away_ht | 49 | 27921 | 0.2% |
| first_goal_time | 1975 | 25995 | 7.1% |
| first_goal_time_extra | 1975 | 25995 | 7.1% |
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
| Home | 99 | 43.0% |
| Draw | 61 | 26.5% |
| Away | 70 | 30.4% |
| Total | 230 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 614 |
| Average goals per match | 2.67 |
| Home goals | 338 (avg 1.47) |
| Away goals | 276 (avg 1.2) |
| Home goal share | 55.0% |
| Goalless matches | 14 (6.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 191 | 41.9% | 27.2% | 30.9% | 511 | 2.675 | 273 | 238 | 10 (5.2%) |
| 2026-2027 | 39 | 48.7% | 23.1% | 28.2% | 103 | 2.641 | 65 | 38 | 4 (10.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `216` of `230` (93.9%)
| metric | value |
|---|---|
| First goals recorded | 216 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 30.02 |
| Median (p50) | 24.5 |
| p25 | 11.0 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 74 |
| 16-30 | 51 |
| 31-45 | 41 |
| 46-60 | 24 |
| 61-75 | 17 |
| 76-90 | 8 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `72`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 14 | 1..14 | 14 |
| 2025-2026 | goals | 14 | 1..14 | 14 |
| 2025-2026 | luck | 14 | 1..14 | 14 |
| 2026-2027 | classic | 10 | 1..10 | 10 |
| 2026-2027 | goals | 10 | 1..10 | 10 |
| 2026-2027 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 34 |
| 2-1 | 21 |
| 1-0 | 20 |
| 0-2 | 17 |
| 0-1 | 16 |
| 3-1 | 15 |
| 0-0 | 14 |
| 1-2 | 14 |
| 3-0 | 12 |
| 2-0 | 12 |
| 2-2 | 12 |
| 0-3 | 6 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 8-0 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Tue | 19 | 8.3% |
| Wed | 1 | 0.4% |
| Fri | 3 | 1.3% |
| Sat | 207 | 90.0% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 191 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 14 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 39 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 10.3% vs overall 6.1% (deviation 4.2 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 48.7% vs overall 43.0% |
| 8 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=14 positions=1..14 teams=14 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=14 positions=1..14 teams=14 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=14 positions=1..14 teams=14 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=10 positions=1..10 teams=10 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=10 positions=1..10 teams=10 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 191, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 14, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 39, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 10.3, "overall_goalless_pct": 6.1, "deviation_pp": 4.2}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 48.7, "overall_share": 43.0}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 27970, "distinct": 27950, "duplicates": 20}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 27970, "fgt_inconsistent": 26, "fgte_inconsistent": 26, "n_with_fgt": 25995}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
