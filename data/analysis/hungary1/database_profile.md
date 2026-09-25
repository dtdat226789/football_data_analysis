# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:00:53+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `hungary1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 73 |
| teams | 782 |
| team_aliases | 1564 |
| team_seasons | 1341 |
| matches | 12987 |
| standings | 3849 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `35`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `hungary1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 198 | 12 | 2025-07-25 | 2026-05-16 |
| 2026-2027 | True | in_progress | 47 | 12 | 2026-07-24 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 12987 | 12987 | 0 |
| matches (league_season_id, game_index) | 12987 | 12987 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 12987 | 12977 | 10 |
| team_seasons (league_season_id, team_id) | 1341 | 1341 | 0 |
| team_seasons api_name within a season | 1341 | 1341 | 0 |
| team_seasons api_slug within a season | 1341 | 1341 | 0 |
| standings (league_season_id, team_id, view) | 3849 | 3849 | 0 |
| team_aliases (form, value) | 1564 | 1564 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 782 | 782 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `12987`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 12987 | 0.0% |
| kickoff_time | 0 | 12987 | 0.0% |
| home_team_id | 0 | 12987 | 0.0% |
| away_team_id | 0 | 12987 | 0.0% |
| home_score | 0 | 12987 | 0.0% |
| away_score | 0 | 12987 | 0.0% |
| home_ht | 35 | 12952 | 0.3% |
| away_ht | 35 | 12952 | 0.3% |
| first_goal_time | 861 | 12126 | 6.6% |
| first_goal_time_extra | 861 | 12126 | 6.6% |
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
| Home | 98 | 40.0% |
| Draw | 62 | 25.3% |
| Away | 85 | 34.7% |
| Total | 245 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 747 |
| Average goals per match | 3.049 |
| Home goals | 393 (avg 1.604) |
| Away goals | 354 (avg 1.445) |
| Home goal share | 52.6% |
| Goalless matches | 10 (4.1%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 198 | 39.4% | 24.7% | 35.9% | 594 | 3.0 | 308 | 286 | 8 (4.0%) |
| 2026-2027 | 47 | 42.6% | 27.7% | 29.8% | 153 | 3.255 | 85 | 68 | 2 (4.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `235` of `245` (95.9%)
| metric | value |
|---|---|
| First goals recorded | 235 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 30.78 |
| Median (p50) | 23.0 |
| p25 | 12.5 |
| p75 | 48.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 74 |
| 16-30 | 63 |
| 31-45 | 31 |
| 46-60 | 45 |
| 61-75 | 11 |
| 76-90 | 10 |
| 91-120 | 1 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `72`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 12 | 1..12 | 12 |
| 2025-2026 | goals | 12 | 1..12 | 12 |
| 2025-2026 | luck | 12 | 1..12 | 12 |
| 2026-2027 | classic | 12 | 1..12 | 12 |
| 2026-2027 | goals | 12 | 1..12 | 12 |
| 2026-2027 | luck | 12 | 1..12 | 12 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 31 |
| 2-1 | 24 |
| 0-1 | 21 |
| 2-2 | 17 |
| 1-2 | 17 |
| 1-0 | 15 |
| 1-3 | 14 |
| 3-0 | 11 |
| 3-1 | 11 |
| 2-0 | 11 |
| 0-0 | 10 |
| 0-2 | 9 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 7-2 | 9 | 1 |
| 2-7 | 9 | 1 |
| 5-3 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 93 | 38.0% |
| Mon | 5 | 2.0% |
| Tue | 1 | 0.4% |
| Wed | 1 | 0.4% |
| Thu | 2 | 0.8% |
| Fri | 35 | 14.3% |
| Sat | 108 | 44.1% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 198 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 12 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 47 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 12 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 29.8% vs overall 34.7% |
| 7 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 8 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 9 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows) |
| 10 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=12 positions=1..12 teams=12 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=12 positions=1..12 teams=12 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=12 positions=1..12 teams=12 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=12 positions=1..12 teams=12 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=12 positions=1..12 teams=12 |
| 15 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=12 positions=1..12 teams=12 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 198, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 12, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 47, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 12, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 29.8, "overall_share": 34.7}`
- `7.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}]}`
- `8.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 12987, "distinct": 12977, "duplicates": 10}`
- `9.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 12987, "fgt_inconsistent": 7, "fgte_inconsistent": 7, "n_with_fgt": 12126}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 12, "min_pos": 1, "max_pos": 12, "distinct_teams": 12}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
