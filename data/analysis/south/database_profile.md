# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:08:31+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `south`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 165 |
| teams | 1655 |
| team_aliases | 3310 |
| team_seasons | 2965 |
| matches | 31244 |
| standings | 8613 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `77`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `south`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 605 | 72 | 2025-08-09 | 2026-05-09 |
| 2026-2027 | True | in_progress | 123 | 24 | 2026-08-08 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 31244 | 31244 | 0 |
| matches (league_season_id, game_index) | 31244 | 31244 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 31244 | 31199 | 45 |
| team_seasons (league_season_id, team_id) | 2965 | 2965 | 0 |
| team_seasons api_name within a season | 2965 | 2965 | 0 |
| team_seasons api_slug within a season | 2965 | 2965 | 0 |
| standings (league_season_id, team_id, view) | 8613 | 8613 | 0 |
| team_aliases (form, value) | 3310 | 3310 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1655 | 1655 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `31244`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 31244 | 0.0% |
| kickoff_time | 0 | 31244 | 0.0% |
| home_team_id | 0 | 31244 | 0.0% |
| away_team_id | 0 | 31244 | 0.0% |
| home_score | 0 | 31244 | 0.0% |
| away_score | 0 | 31244 | 0.0% |
| home_ht | 52 | 31192 | 0.2% |
| away_ht | 52 | 31192 | 0.2% |
| first_goal_time | 2249 | 28995 | 7.2% |
| first_goal_time_extra | 2249 | 28995 | 7.2% |
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
| Home | 333 | 45.7% |
| Draw | 168 | 23.1% |
| Away | 227 | 31.2% |
| Total | 728 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 2063 |
| Average goals per match | 2.834 |
| Home goals | 1143 (avg 1.57) |
| Away goals | 920 (avg 1.264) |
| Home goal share | 55.4% |
| Goalless matches | 45 (6.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 605 | 47.8% | 22.3% | 29.9% | 1709 | 2.825 | 968 | 741 | 39 (6.4%) |
| 2026-2027 | 123 | 35.8% | 26.8% | 37.4% | 354 | 2.878 | 175 | 179 | 6 (4.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `683` of `728` (93.8%)
| metric | value |
|---|---|
| First goals recorded | 683 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 30.58 |
| Median (p50) | 24.0 |
| p25 | 11.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 244 |
| 16-30 | 171 |
| 31-45 | 96 |
| 46-60 | 87 |
| 61-75 | 36 |
| 76-90 | 32 |
| 91-120 | 17 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `288`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 72 | 1..72 | 72 |
| 2025-2026 | goals | 72 | 1..72 | 72 |
| 2025-2026 | luck | 72 | 1..72 | 72 |
| 2026-2027 | classic | 24 | 1..24 | 24 |
| 2026-2027 | goals | 24 | 1..24 | 24 |
| 2026-2027 | luck | 24 | 1..24 | 24 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 85 |
| 1-1 | 77 |
| 1-2 | 74 |
| 2-0 | 56 |
| 2-1 | 54 |
| 0-1 | 47 |
| 0-0 | 45 |
| 2-2 | 35 |
| 3-0 | 31 |
| 3-2 | 28 |
| 3-1 | 26 |
| 0-2 | 22 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 5-4 | 9 | 2 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 5-3 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1 | 0.1% |
| Mon | 44 | 6.0% |
| Tue | 182 | 25.0% |
| Wed | 6 | 0.8% |
| Fri | 27 | 3.7% |
| Sat | 468 | 64.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 605 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 72 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 123 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 24 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 35.8% vs overall 45.7% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 37.4% vs overall 31.2% |
| 8 | HIGH_SCORING_MATCHES | 8 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=29, fgte=29 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=72 positions=1..72 teams=72 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=72 positions=1..72 teams=72 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=72 positions=1..72 teams=72 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=24 positions=1..24 teams=24 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=24 positions=1..24 teams=24 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=24 positions=1..24 teams=24 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 605, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 72, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 123, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 24, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 35.8, "overall_share": 45.7}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 37.4, "overall_share": 31.2}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 8, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "5-4", "total_goals": 9, "count": 2}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 31244, "distinct": 31199, "duplicates": 45}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 31244, "fgt_inconsistent": 29, "fgte_inconsistent": 29, "n_with_fgt": 28995}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 72, "min_pos": 1, "max_pos": 72, "distinct_teams": 72}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 24, "min_pos": 1, "max_pos": 24, "distinct_teams": 24}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
