# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:09:01+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `spain2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 169 |
| teams | 1694 |
| team_aliases | 3388 |
| team_seasons | 3050 |
| matches | 32279 |
| standings | 8868 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `79`
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
| south | National League South | England | 2 | 728 |
| spain1 | LaLiga | Spain | 2 | 449 |
| spain2 | LaLiga2 | Spain | 2 | 586 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `spain2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 509 | 23 | 2025-08-15 | 2026-06-20 |
| 2026-2027 | True | in_progress | 77 | 22 | 2026-08-14 | 2026-09-28 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 32279 | 32279 | 0 |
| matches (league_season_id, game_index) | 32279 | 32279 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 32279 | 32234 | 45 |
| team_seasons (league_season_id, team_id) | 3050 | 3050 | 0 |
| team_seasons api_name within a season | 3050 | 3050 | 0 |
| team_seasons api_slug within a season | 3050 | 3050 | 0 |
| standings (league_season_id, team_id, view) | 8868 | 8868 | 0 |
| team_aliases (form, value) | 3388 | 3388 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1694 | 1694 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `32279`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 32279 | 0.0% |
| kickoff_time | 0 | 32279 | 0.0% |
| home_team_id | 0 | 32279 | 0.0% |
| away_team_id | 0 | 32279 | 0.0% |
| home_score | 0 | 32279 | 0.0% |
| away_score | 0 | 32279 | 0.0% |
| home_ht | 52 | 32227 | 0.2% |
| away_ht | 52 | 32227 | 0.2% |
| first_goal_time | 2316 | 29963 | 7.2% |
| first_goal_time_extra | 2316 | 29963 | 7.2% |
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
| Home | 256 | 43.7% |
| Draw | 145 | 24.7% |
| Away | 185 | 31.6% |
| Total | 586 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1528 |
| Average goals per match | 2.608 |
| Home goals | 835 (avg 1.425) |
| Away goals | 693 (avg 1.183) |
| Home goal share | 54.6% |
| Goalless matches | 47 (8.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 509 | 43.8% | 25.3% | 30.8% | 1335 | 2.623 | 729 | 606 | 40 (7.9%) |
| 2026-2027 | 77 | 42.9% | 20.8% | 36.4% | 193 | 2.506 | 106 | 87 | 7 (9.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `539` of `586` (92.0%)
| metric | value |
|---|---|
| First goals recorded | 539 |
| Min minute | 1 |
| Max minute | 98 |
| Mean minute | 31.12 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 186 |
| 16-30 | 125 |
| 31-45 | 83 |
| 46-60 | 75 |
| 61-75 | 35 |
| 76-90 | 25 |
| 91-120 | 10 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `135`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 23 | 1..23 | 23 |
| 2025-2026 | goals | 23 | 1..23 | 23 |
| 2025-2026 | luck | 23 | 1..23 | 23 |
| 2026-2027 | classic | 22 | 1..22 | 22 |
| 2026-2027 | goals | 22 | 1..22 | 22 |
| 2026-2027 | luck | 22 | 1..22 | 22 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 74 |
| 1-0 | 63 |
| 2-1 | 59 |
| 0-1 | 54 |
| 0-0 | 47 |
| 1-2 | 45 |
| 2-0 | 35 |
| 1-3 | 26 |
| 0-2 | 24 |
| 3-1 | 24 |
| 3-0 | 21 |
| 3-2 | 19 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 6-2 | 8 | 1 |
| 5-3 | 8 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 248 | 42.3% |
| Mon | 52 | 8.9% |
| Tue | 5 | 0.9% |
| Wed | 8 | 1.4% |
| Thu | 4 | 0.7% |
| Fri | 56 | 9.6% |
| Sat | 213 | 36.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 509 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 23 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 77 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 22 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 36.4% vs overall 31.6% |
| 7 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=23 positions=1..23 teams=23 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=23 positions=1..23 teams=23 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=23 positions=1..23 teams=23 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=22 positions=1..22 teams=22 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=22 positions=1..22 teams=22 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=22 positions=1..22 teams=22 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 509, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 23, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 77, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 22, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 36.4, "overall_share": 31.6}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 32279, "distinct": 32234, "duplicates": 45}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 32279, "fgt_inconsistent": 29, "fgte_inconsistent": 29, "n_with_fgt": 29963}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 23, "min_pos": 1, "max_pos": 23, "distinct_teams": 23}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 22, "min_pos": 1, "max_pos": 22, "distinct_teams": 22}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
