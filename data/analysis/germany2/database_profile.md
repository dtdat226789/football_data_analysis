# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:51:07+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 59 |
| teams | 645 |
| team_aliases | 1290 |
| team_seasons | 1087 |
| matches | 10571 |
| standings | 3087 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `28`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 310 | 20 | 2025-08-01 | 2026-05-26 |
| 2026-2027 | True | in_progress | 54 | 18 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 10571 | 10571 | 0 |
| matches (league_season_id, game_index) | 10571 | 10571 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 10571 | 10561 | 10 |
| team_seasons (league_season_id, team_id) | 1087 | 1087 | 0 |
| team_seasons api_name within a season | 1087 | 1087 | 0 |
| team_seasons api_slug within a season | 1087 | 1087 | 0 |
| standings (league_season_id, team_id, view) | 3087 | 3087 | 0 |
| team_aliases (form, value) | 1290 | 1290 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 645 | 645 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `10571`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 10571 | 0.0% |
| kickoff_time | 0 | 10571 | 0.0% |
| home_team_id | 0 | 10571 | 0.0% |
| away_team_id | 0 | 10571 | 0.0% |
| home_score | 0 | 10571 | 0.0% |
| away_score | 0 | 10571 | 0.0% |
| home_ht | 34 | 10537 | 0.3% |
| away_ht | 34 | 10537 | 0.3% |
| first_goal_time | 746 | 9825 | 7.1% |
| first_goal_time_extra | 746 | 9825 | 7.1% |
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
| Home | 165 | 45.3% |
| Draw | 90 | 24.7% |
| Away | 109 | 29.9% |
| Total | 364 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1082 |
| Average goals per match | 2.973 |
| Home goals | 598 (avg 1.643) |
| Away goals | 484 (avg 1.33) |
| Home goal share | 55.3% |
| Goalless matches | 19 (5.2%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 46.5% | 24.2% | 29.4% | 903 | 2.913 | 504 | 399 | 17 (5.5%) |
| 2026-2027 | 54 | 38.9% | 27.8% | 33.3% | 179 | 3.315 | 94 | 85 | 2 (3.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `345` of `364` (94.8%)
| metric | value |
|---|---|
| First goals recorded | 345 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 30.92 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 47.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 121 |
| 16-30 | 73 |
| 31-45 | 59 |
| 46-60 | 42 |
| 61-75 | 32 |
| 76-90 | 14 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `114`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |
| 2026-2027 | classic | 18 | 1..18 | 18 |
| 2026-2027 | goals | 18 | 1..18 | 18 |
| 2026-2027 | luck | 18 | 1..18 | 18 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-1 | 41 |
| 1-1 | 36 |
| 1-0 | 35 |
| 1-2 | 29 |
| 2-2 | 26 |
| 2-0 | 23 |
| 0-1 | 21 |
| 0-0 | 19 |
| 0-2 | 17 |
| 3-1 | 16 |
| 3-0 | 15 |
| 2-3 | 12 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-5 | 9 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 130 | 35.7% |
| Mon | 1 | 0.3% |
| Tue | 1 | 0.3% |
| Thu | 1 | 0.3% |
| Fri | 73 | 20.1% |
| Sat | 158 | 43.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 310 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 54 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 38.9% vs overall 45.3% |
| 6 | HIGH_SCORING_MATCHES | 6 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 10 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 11 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 310, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 54, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 38.9, "overall_share": 45.3}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 6, "threshold": 8, "examples": [{"scoreline": "4-5", "total_goals": 9, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 10571, "distinct": 10561, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 10571, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 9825}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
