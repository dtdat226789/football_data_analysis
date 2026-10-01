# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:53:27+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `holland3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 71 |
| teams | 769 |
| team_aliases | 1538 |
| team_seasons | 1318 |
| matches | 12842 |
| standings | 3780 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `34`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `holland3`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 322 | 25 | 2025-08-16 | 2026-06-13 |
| 2026-2027 | True | in_progress | 63 | 18 | 2026-08-15 | 2026-09-26 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 12842 | 12842 | 0 |
| matches (league_season_id, game_index) | 12842 | 12842 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 12842 | 12832 | 10 |
| team_seasons (league_season_id, team_id) | 1318 | 1318 | 0 |
| team_seasons api_name within a season | 1318 | 1318 | 0 |
| team_seasons api_slug within a season | 1318 | 1318 | 0 |
| standings (league_season_id, team_id, view) | 3780 | 3780 | 0 |
| team_aliases (form, value) | 1538 | 1538 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 769 | 769 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `12842`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 12842 | 0.0% |
| kickoff_time | 0 | 12842 | 0.0% |
| home_team_id | 0 | 12842 | 0.0% |
| away_team_id | 0 | 12842 | 0.0% |
| home_score | 0 | 12842 | 0.0% |
| away_score | 0 | 12842 | 0.0% |
| home_ht | 35 | 12807 | 0.3% |
| away_ht | 35 | 12807 | 0.3% |
| first_goal_time | 857 | 11985 | 6.7% |
| first_goal_time_extra | 857 | 11985 | 6.7% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 176 | 45.7% |
| Draw | 79 | 20.5% |
| Away | 130 | 33.8% |
| Total | 385 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1287 |
| Average goals per match | 3.343 |
| Home goals | 702 (avg 1.823) |
| Away goals | 585 (avg 1.519) |
| Home goal share | 54.5% |
| Goalless matches | 10 (2.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 322 | 47.5% | 19.6% | 32.9% | 1069 | 3.32 | 584 | 485 | 10 (3.1%) |
| 2026-2027 | 63 | 36.5% | 25.4% | 38.1% | 218 | 3.46 | 118 | 100 | 0 (0.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `374` of `385` (97.1%)
| metric | value |
|---|---|
| First goals recorded | 374 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 28.36 |
| Median (p50) | 23.0 |
| p25 | 11.25 |
| p75 | 38.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 125 |
| 16-30 | 104 |
| 31-45 | 63 |
| 46-60 | 46 |
| 61-75 | 23 |
| 76-90 | 9 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `129`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 25 | 1..25 | 25 |
| 2025-2026 | goals | 25 | 1..25 | 25 |
| 2025-2026 | luck | 25 | 1..25 | 25 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 38 |
| 2-1 | 31 |
| 1-2 | 31 |
| 1-0 | 27 |
| 2-2 | 22 |
| 3-0 | 21 |
| 1-3 | 21 |
| 2-0 | 20 |
| 0-2 | 19 |
| 3-2 | 19 |
| 0-1 | 16 |
| 3-1 | 15 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-4 | 9 | 1 |
| 3-6 | 9 | 1 |
| 8-0 | 8 | 1 |
| 6-2 | 8 | 1 |
| 4-4 | 8 | 2 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1 | 0.3% |
| Tue | 1 | 0.3% |
| Wed | 8 | 2.1% |
| Sat | 375 | 97.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 322 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 25 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 0.0% vs overall 2.6% (deviation 2.6 pp) |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 36.5% vs overall 45.7% |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 25.4% vs overall 20.5% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 38.1% vs overall 33.8% |
| 10 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=25 positions=1..25 teams=25 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=25 positions=1..25 teams=25 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=25 positions=1..25 teams=25 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 322, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 25, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 0.0, "overall_goalless_pct": 2.6, "deviation_pp": 2.6}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 36.5, "overall_share": 45.7}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 25.4, "overall_share": 20.5}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 38.1, "overall_share": 33.8}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "5-4", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "4-4", "total_goals": 8, "count": 2}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 12842, "distinct": 12832, "duplicates": 10}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 12842, "fgt_inconsistent": 7, "fgte_inconsistent": 7, "n_with_fgt": 11985}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 25, "min_pos": 1, "max_pos": 25, "distinct_teams": 25}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
