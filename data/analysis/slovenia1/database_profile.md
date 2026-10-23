# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:08:15+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `slovenia1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 163 |
| teams | 1581 |
| team_aliases | 3162 |
| team_seasons | 2869 |
| matches | 30516 |
| standings | 8325 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `76`
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
| scot2 | League Two | Scotland | 2 | 228 |
| segunda1 | Segunda RFEF - Group 1 | Spain | 2 | 342 |
| segunda2 | Segunda RFEF - Group 2 | Spain | 2 | 342 |
| segunda3 | Segunda RFEF - Group 3 | Spain | 2 | 346 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 2 | 359 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 2 | 348 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 2 | 365 |
| slovenia1 | Prva liga | Slovenia | 2 | 216 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `slovenia1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 164 | 11 | 2025-07-18 | 2026-05-31 |
| 2026-2027 | True | in_progress | 52 | 10 | 2026-07-17 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 30516 | 30516 | 0 |
| matches (league_season_id, game_index) | 30516 | 30516 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 30516 | 30482 | 34 |
| team_seasons (league_season_id, team_id) | 2869 | 2869 | 0 |
| team_seasons api_name within a season | 2869 | 2869 | 0 |
| team_seasons api_slug within a season | 2869 | 2869 | 0 |
| standings (league_season_id, team_id, view) | 8325 | 8325 | 0 |
| team_aliases (form, value) | 3162 | 3162 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1581 | 1581 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `30516`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 30516 | 0.0% |
| kickoff_time | 0 | 30516 | 0.0% |
| home_team_id | 0 | 30516 | 0.0% |
| away_team_id | 0 | 30516 | 0.0% |
| home_score | 0 | 30516 | 0.0% |
| away_score | 0 | 30516 | 0.0% |
| home_ht | 52 | 30464 | 0.2% |
| away_ht | 52 | 30464 | 0.2% |
| first_goal_time | 2204 | 28312 | 7.2% |
| first_goal_time_extra | 2204 | 28312 | 7.2% |
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
| Home | 99 | 45.8% |
| Draw | 46 | 21.3% |
| Away | 71 | 32.9% |
| Total | 216 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 635 |
| Average goals per match | 2.94 |
| Home goals | 340 (avg 1.574) |
| Away goals | 295 (avg 1.366) |
| Home goal share | 53.5% |
| Goalless matches | 14 (6.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 164 | 49.4% | 18.3% | 32.3% | 501 | 3.055 | 273 | 228 | 8 (4.9%) |
| 2026-2027 | 52 | 34.6% | 30.8% | 34.6% | 134 | 2.577 | 67 | 67 | 6 (11.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `201` of `216` (93.1%)
| metric | value |
|---|---|
| First goals recorded | 201 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 25.33 |
| Median (p50) | 21.0 |
| p25 | 10.0 |
| p75 | 35.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 77 |
| 16-30 | 63 |
| 31-45 | 32 |
| 46-60 | 15 |
| 61-75 | 8 |
| 76-90 | 2 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `63`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 11 | 1..11 | 11 |
| 2025-2026 | goals | 11 | 1..11 | 11 |
| 2025-2026 | luck | 11 | 1..11 | 11 |
| 2026-2027 | classic | 10 | 1..10 | 10 |
| 2026-2027 | goals | 10 | 1..10 | 10 |
| 2026-2027 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-1 | 25 |
| 1-1 | 19 |
| 1-0 | 18 |
| 1-2 | 17 |
| 0-0 | 14 |
| 2-0 | 14 |
| 3-0 | 13 |
| 0-2 | 13 |
| 1-3 | 11 |
| 3-1 | 9 |
| 2-3 | 8 |
| 2-2 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 86 | 39.8% |
| Mon | 6 | 2.8% |
| Tue | 3 | 1.4% |
| Wed | 5 | 2.3% |
| Thu | 3 | 1.4% |
| Fri | 27 | 12.5% |
| Sat | 86 | 39.8% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 164 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 11 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 52 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 4.9% vs overall 6.5% (deviation 1.6 pp) |
| 7 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 2.577 vs overall 2.94 (deviation 0.363) |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 11.5% vs overall 6.5% (deviation 5.0 pp) |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 34.6% vs overall 45.8% |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 30.8% vs overall 21.3% |
| 11 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 12 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (34 extra rows) |
| 13 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows) |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=11 positions=1..11 teams=11 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=11 positions=1..11 teams=11 |
| 16 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=11 positions=1..11 teams=11 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=10 positions=1..10 teams=10 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=10 positions=1..10 teams=10 |
| 19 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 164, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 11, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 52, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 4.9, "overall_goalless_pct": 6.5, "deviation_pp": 1.6}`
- `7.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 2.577, "overall_avg_goals": 2.94, "deviation": 0.363}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 11.5, "overall_goalless_pct": 6.5, "deviation_pp": 5.0}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 34.6, "overall_share": 45.8}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 30.8, "overall_share": 21.3}`
- `11.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `12.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 30516, "distinct": 30482, "duplicates": 34}`
- `13.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 30516, "fgt_inconsistent": 29, "fgte_inconsistent": 29, "n_with_fgt": 28312}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
