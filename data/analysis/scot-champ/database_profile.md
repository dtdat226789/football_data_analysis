# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:05:44+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `scot-champ`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 143 |
| teams | 1415 |
| team_aliases | 2830 |
| team_seasons | 2564 |
| matches | 27464 |
| standings | 7410 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `66`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `scot-champ`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 190 | 13 | 2025-08-01 | 2026-05-16 |
| 2026-2027 | True | in_progress | 41 | 10 | 2026-08-01 | 2026-09-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 27464 | 27464 | 0 |
| matches (league_season_id, game_index) | 27464 | 27464 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 27464 | 27444 | 20 |
| team_seasons (league_season_id, team_id) | 2564 | 2564 | 0 |
| team_seasons api_name within a season | 2564 | 2564 | 0 |
| team_seasons api_slug within a season | 2564 | 2564 | 0 |
| standings (league_season_id, team_id, view) | 7410 | 7410 | 0 |
| team_aliases (form, value) | 2830 | 2830 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1415 | 1415 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `27464`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 27464 | 0.0% |
| kickoff_time | 0 | 27464 | 0.0% |
| home_team_id | 0 | 27464 | 0.0% |
| away_team_id | 0 | 27464 | 0.0% |
| home_score | 0 | 27464 | 0.0% |
| away_score | 0 | 27464 | 0.0% |
| home_ht | 49 | 27415 | 0.2% |
| away_ht | 49 | 27415 | 0.2% |
| first_goal_time | 1942 | 25522 | 7.1% |
| first_goal_time_extra | 1942 | 25522 | 7.1% |
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
| Home | 93 | 40.3% |
| Draw | 74 | 32.0% |
| Away | 64 | 27.7% |
| Total | 231 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 540 |
| Average goals per match | 2.338 |
| Home goals | 298 (avg 1.29) |
| Away goals | 242 (avg 1.048) |
| Home goal share | 55.2% |
| Goalless matches | 29 (12.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 190 | 38.9% | 33.7% | 27.4% | 460 | 2.421 | 252 | 208 | 25 (13.2%) |
| 2026-2027 | 41 | 46.3% | 24.4% | 29.3% | 80 | 1.951 | 46 | 34 | 4 (9.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `202` of `231` (87.4%)
| metric | value |
|---|---|
| First goals recorded | 202 |
| Min minute | 1 |
| Max minute | 88 |
| Mean minute | 29.51 |
| Median (p50) | 25.0 |
| p25 | 13.25 |
| p75 | 43.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 60 |
| 16-30 | 56 |
| 31-45 | 41 |
| 46-60 | 27 |
| 61-75 | 10 |
| 76-90 | 8 |
| 91-120 | 0 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `69`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 13 | 1..13 | 13 |
| 2025-2026 | goals | 13 | 1..13 | 13 |
| 2025-2026 | luck | 13 | 1..13 | 13 |
| 2026-2027 | classic | 10 | 1..10 | 10 |
| 2026-2027 | goals | 10 | 1..10 | 10 |
| 2026-2027 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 33 |
| 0-0 | 29 |
| 1-0 | 22 |
| 2-1 | 20 |
| 0-1 | 20 |
| 2-0 | 18 |
| 0-2 | 14 |
| 1-2 | 13 |
| 2-2 | 11 |
| 3-2 | 7 |
| 3-1 | 7 |
| 3-0 | 7 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Tue | 23 | 10.0% |
| Wed | 1 | 0.4% |
| Fri | 38 | 16.5% |
| Sat | 169 | 73.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 190 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 13 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 41 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 1.951 vs overall 2.338 (deviation 0.387) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 9.8% vs overall 12.6% (deviation 2.8 pp) |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 46.3% vs overall 40.3% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 24.4% vs overall 32.0% |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (20 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=26, fgte=26 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=13 positions=1..13 teams=13 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=13 positions=1..13 teams=13 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=13 positions=1..13 teams=13 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=10 positions=1..10 teams=10 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=10 positions=1..10 teams=10 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 190, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 13, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 41, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 1.951, "overall_avg_goals": 2.338, "deviation": 0.387}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 9.8, "overall_goalless_pct": 12.6, "deviation_pp": 2.8}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 46.3, "overall_share": 40.3}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 24.4, "overall_share": 32.0}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 27464, "distinct": 27444, "duplicates": 20}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 27464, "fgt_inconsistent": 26, "fgte_inconsistent": 26, "n_with_fgt": 25522}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
