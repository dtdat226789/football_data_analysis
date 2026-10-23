# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:04:29+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `primera2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 133 |
| teams | 1323 |
| team_aliases | 2646 |
| team_seasons | 2399 |
| matches | 25745 |
| standings | 6915 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `61`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `primera2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 380 | 20 | 2025-08-29 | 2026-05-24 |
| 2026-2027 | True | in_progress | 49 | 20 | 2026-08-29 | 2026-09-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 25745 | 25745 | 0 |
| matches (league_season_id, game_index) | 25745 | 25745 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 25745 | 25731 | 14 |
| team_seasons (league_season_id, team_id) | 2399 | 2399 | 0 |
| team_seasons api_name within a season | 2399 | 2399 | 0 |
| team_seasons api_slug within a season | 2399 | 2399 | 0 |
| standings (league_season_id, team_id, view) | 6915 | 6915 | 0 |
| team_aliases (form, value) | 2646 | 2646 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1323 | 1323 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `25745`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 25745 | 0.0% |
| kickoff_time | 0 | 25745 | 0.0% |
| home_team_id | 0 | 25745 | 0.0% |
| away_team_id | 0 | 25745 | 0.0% |
| home_score | 0 | 25745 | 0.0% |
| away_score | 0 | 25745 | 0.0% |
| home_ht | 47 | 25698 | 0.2% |
| away_ht | 47 | 25698 | 0.2% |
| first_goal_time | 1805 | 23940 | 7.0% |
| first_goal_time_extra | 1805 | 23940 | 7.0% |
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
| Home | 194 | 45.2% |
| Draw | 126 | 29.4% |
| Away | 109 | 25.4% |
| Total | 429 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 979 |
| Average goals per match | 2.282 |
| Home goals | 568 (avg 1.324) |
| Away goals | 411 (avg 0.958) |
| Home goal share | 58.0% |
| Goalless matches | 50 (11.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 45.5% | 29.7% | 24.7% | 856 | 2.253 | 500 | 356 | 46 (12.1%) |
| 2026-2027 | 49 | 42.9% | 26.5% | 30.6% | 123 | 2.51 | 68 | 55 | 4 (8.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `379` of `429` (88.3%)
| metric | value |
|---|---|
| First goals recorded | 379 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 32.98 |
| Median (p50) | 28.0 |
| p25 | 13.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 114 |
| 16-30 | 87 |
| 31-45 | 68 |
| 46-60 | 52 |
| 61-75 | 34 |
| 76-90 | 17 |
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
| 1-0 | 58 |
| 0-0 | 50 |
| 1-1 | 48 |
| 2-0 | 43 |
| 0-1 | 39 |
| 2-1 | 37 |
| 2-2 | 25 |
| 1-2 | 24 |
| 3-0 | 17 |
| 0-2 | 17 |
| 3-1 | 14 |
| 1-3 | 9 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 198 | 46.2% |
| Mon | 6 | 1.4% |
| Wed | 9 | 2.1% |
| Fri | 43 | 10.0% |
| Sat | 173 | 40.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 49 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 8.2% vs overall 11.7% (deviation 3.5 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 30.6% vs overall 25.4% |
| 5 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 6 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 7 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=24, fgte=24 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 49, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 8.2, "overall_goalless_pct": 11.7, "deviation_pp": 3.5}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 30.6, "overall_share": 25.4}`
- `5.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `6.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 25745, "distinct": 25731, "duplicates": 14}`
- `7.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 25745, "fgt_inconsistent": 24, "fgte_inconsistent": 24, "n_with_fgt": 23940}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
