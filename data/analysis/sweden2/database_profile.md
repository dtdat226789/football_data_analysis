# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:48:42+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `sweden2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 172 |
| teams | 1728 |
| team_aliases | 3456 |
| team_seasons | 3113 |
| matches | 32893 |
| standings | 9057 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `81`
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
| segunda3 | Segunda RFEF - Group 3 | Spain | 2 | 337 |
| segunda4 | Segunda RFEF - Group 4 | Spain | 2 | 350 |
| segunda5 | Segunda RFEF - Group 5 | Spain | 2 | 339 |
| serbia1 | Mozzart Bet Super Liga | Serbia | 2 | 365 |
| slovenia1 | Prva liga | Slovenia | 2 | 216 |
| south | National League South | England | 2 | 716 |
| spain1 | LaLiga | Spain | 2 | 449 |
| spain2 | LaLiga2 | Spain | 2 | 575 |
| sweden1 | Allsvenskan | Sweden | 2 | 416 |
| sweden2 | Superettan | Sweden | 2 | 440 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `sweden2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 240 | 16 | 2025-03-29 | 2025-11-08 |
| 2026 | True | in_progress | 200 | 16 | 2026-04-03 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 32893 | 32893 | 0 |
| matches (league_season_id, game_index) | 32893 | 32893 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 32893 | 32848 | 45 |
| team_seasons (league_season_id, team_id) | 3113 | 3113 | 0 |
| team_seasons api_name within a season | 3113 | 3113 | 0 |
| team_seasons api_slug within a season | 3113 | 3113 | 0 |
| standings (league_season_id, team_id, view) | 9057 | 9057 | 0 |
| team_aliases (form, value) | 3456 | 3456 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1728 | 1728 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `32893`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 32893 | 0.0% |
| kickoff_time | 0 | 32893 | 0.0% |
| home_team_id | 0 | 32893 | 0.0% |
| away_team_id | 0 | 32893 | 0.0% |
| home_score | 0 | 32893 | 0.0% |
| away_score | 0 | 32893 | 0.0% |
| home_ht | 53 | 32840 | 0.2% |
| away_ht | 53 | 32840 | 0.2% |
| first_goal_time | 2354 | 30539 | 7.2% |
| first_goal_time_extra | 2354 | 30539 | 7.2% |
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
| Home | 178 | 40.5% |
| Draw | 119 | 27.0% |
| Away | 143 | 32.5% |
| Total | 440 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1266 |
| Average goals per match | 2.877 |
| Home goals | 683 (avg 1.552) |
| Away goals | 583 (avg 1.325) |
| Home goal share | 53.9% |
| Goalless matches | 31 (7.0%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 240 | 42.1% | 27.1% | 30.8% | 686 | 2.858 | 384 | 302 | 18 (7.5%) |
| 2026 | 200 | 38.5% | 27.0% | 34.5% | 580 | 2.9 | 299 | 281 | 13 (6.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `408` of `440` (92.7%)
| metric | value |
|---|---|
| First goals recorded | 408 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 29.18 |
| Median (p50) | 23.0 |
| p25 | 10.75 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 154 |
| 16-30 | 85 |
| 31-45 | 72 |
| 46-60 | 48 |
| 61-75 | 26 |
| 76-90 | 17 |
| 91-120 | 6 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 16 | 1..16 | 16 |
| 2025 | goals | 16 | 1..16 | 16 |
| 2025 | luck | 16 | 1..16 | 16 |
| 2026 | classic | 16 | 1..16 | 16 |
| 2026 | goals | 16 | 1..16 | 16 |
| 2026 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 45 |
| 2-1 | 37 |
| 2-2 | 35 |
| 1-0 | 34 |
| 1-2 | 33 |
| 0-1 | 33 |
| 0-0 | 31 |
| 0-2 | 27 |
| 2-0 | 24 |
| 1-3 | 18 |
| 3-2 | 16 |
| 3-1 | 16 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 1 |
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 109 | 24.8% |
| Mon | 60 | 13.6% |
| Tue | 40 | 9.1% |
| Wed | 19 | 4.3% |
| Thu | 14 | 3.2% |
| Fri | 26 | 5.9% |
| Sat | 172 | 39.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 240 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 200 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=16 positions=1..16 teams=16 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=16 positions=1..16 teams=16 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=16 positions=1..16 teams=16 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=16 positions=1..16 teams=16 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 240, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 200, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 32893, "distinct": 32848, "duplicates": 45}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 32893, "fgt_inconsistent": 30, "fgte_inconsistent": 30, "n_with_fgt": 30539}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
