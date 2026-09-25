# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T13:49:56+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `turkey1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 10 |
| league_seasons | 180 |
| teams | 1792 |
| team_aliases | 3584 |
| team_seasons | 3227 |
| matches | 34032 |
| standings | 9399 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `85`
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
| swiss1 | Super League | Switzerland | 2 | 284 |
| swiss2 | Challenge League | Switzerland | 2 | 231 |
| thai1 | Thai League 1 | Thailand | 2 | 264 |
| turkey1 | Super Lig | Turkey | 2 | 360 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `turkey1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 306 | 18 | 2025-08-08 | 2026-05-17 |
| 2026-2027 | True | in_progress | 54 | 18 | 2026-08-14 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 34032 | 34032 | 0 |
| matches (league_season_id, game_index) | 34032 | 34032 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 34032 | 33987 | 45 |
| team_seasons (league_season_id, team_id) | 3227 | 3227 | 0 |
| team_seasons api_name within a season | 3227 | 3227 | 0 |
| team_seasons api_slug within a season | 3227 | 3227 | 0 |
| standings (league_season_id, team_id, view) | 9399 | 9399 | 0 |
| team_aliases (form, value) | 3584 | 3584 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 10 | 10 | 0 |
| teams.canonical_name | 1792 | 1792 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `34032`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 34032 | 0.0% |
| kickoff_time | 0 | 34032 | 0.0% |
| home_team_id | 0 | 34032 | 0.0% |
| away_team_id | 0 | 34032 | 0.0% |
| home_score | 0 | 34032 | 0.0% |
| away_score | 0 | 34032 | 0.0% |
| home_ht | 53 | 33979 | 0.2% |
| away_ht | 53 | 33979 | 0.2% |
| first_goal_time | 2427 | 31605 | 7.1% |
| first_goal_time_extra | 2427 | 31605 | 7.1% |
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
| Home | 155 | 43.1% |
| Draw | 100 | 27.8% |
| Away | 105 | 29.2% |
| Total | 360 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 973 |
| Average goals per match | 2.703 |
| Home goals | 539 (avg 1.497) |
| Away goals | 434 (avg 1.206) |
| Home goal share | 55.4% |
| Goalless matches | 30 (8.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 42.2% | 29.1% | 28.8% | 812 | 2.654 | 442 | 370 | 28 (9.2%) |
| 2026-2027 | 54 | 48.1% | 20.4% | 31.5% | 161 | 2.981 | 97 | 64 | 2 (3.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `330` of `360` (91.7%)
| metric | value |
|---|---|
| First goals recorded | 330 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 31.82 |
| Median (p50) | 24.5 |
| p25 | 12.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 108 |
| 16-30 | 76 |
| 31-45 | 49 |
| 46-60 | 49 |
| 61-75 | 28 |
| 76-90 | 12 |
| 91-120 | 8 |

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
| 1-1 | 47 |
| 1-0 | 37 |
| 2-1 | 33 |
| 0-0 | 30 |
| 1-2 | 28 |
| 3-0 | 19 |
| 2-0 | 19 |
| 0-1 | 19 |
| 2-2 | 19 |
| 0-2 | 16 |
| 3-1 | 13 |
| 3-2 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 8-0 | 8 | 1 |
| 6-2 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 131 | 36.4% |
| Mon | 48 | 13.3% |
| Tue | 1 | 0.3% |
| Wed | 10 | 2.8% |
| Thu | 4 | 1.1% |
| Fri | 38 | 10.6% |
| Sat | 128 | 35.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 306 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 18 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 54 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 3.7% vs overall 8.3% (deviation 4.6 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 48.1% vs overall 43.1% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 20.4% vs overall 27.8% |
| 9 | HIGH_SCORING_MATCHES | 2 match(es) with >= 8 total goals (extreme scorelines) |
| 10 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (45 extra rows) |
| 11 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=30, fgte=30 rows) |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=18 positions=1..18 teams=18 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=18 positions=1..18 teams=18 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=18 positions=1..18 teams=18 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 306, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 18, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 54, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 3.7, "overall_goalless_pct": 8.3, "deviation_pp": 4.6}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 48.1, "overall_share": 43.1}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 20.4, "overall_share": 27.8}`
- `9.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 2, "threshold": 8, "examples": [{"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}]}`
- `10.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 34032, "distinct": 33987, "duplicates": 45}`
- `11.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 34032, "fgt_inconsistent": 30, "fgte_inconsistent": 30, "n_with_fgt": 31605}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
