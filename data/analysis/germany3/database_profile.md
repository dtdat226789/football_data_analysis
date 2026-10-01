# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:51:21+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `germany3`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 61 |
| teams | 665 |
| team_aliases | 1330 |
| team_seasons | 1127 |
| matches | 11021 |
| standings | 3207 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `29`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `germany3`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 380 | 20 | 2025-08-01 | 2026-05-16 |
| 2026-2027 | True | in_progress | 70 | 20 | 2026-08-07 | 2026-09-25 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 11021 | 11021 | 0 |
| matches (league_season_id, game_index) | 11021 | 11021 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 11021 | 11011 | 10 |
| team_seasons (league_season_id, team_id) | 1127 | 1127 | 0 |
| team_seasons api_name within a season | 1127 | 1127 | 0 |
| team_seasons api_slug within a season | 1127 | 1127 | 0 |
| standings (league_season_id, team_id, view) | 3207 | 3207 | 0 |
| team_aliases (form, value) | 1330 | 1330 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 665 | 665 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `11021`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 11021 | 0.0% |
| kickoff_time | 0 | 11021 | 0.0% |
| home_team_id | 0 | 11021 | 0.0% |
| away_team_id | 0 | 11021 | 0.0% |
| home_score | 0 | 11021 | 0.0% |
| away_score | 0 | 11021 | 0.0% |
| home_ht | 34 | 10987 | 0.3% |
| away_ht | 34 | 10987 | 0.3% |
| first_goal_time | 771 | 10250 | 7.0% |
| first_goal_time_extra | 771 | 10250 | 7.0% |
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
| Home | 204 | 45.3% |
| Draw | 103 | 22.9% |
| Away | 143 | 31.8% |
| Total | 450 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1448 |
| Average goals per match | 3.218 |
| Home goals | 786 (avg 1.747) |
| Away goals | 662 (avg 1.471) |
| Home goal share | 54.3% |
| Goalless matches | 25 (5.6%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 46.1% | 23.4% | 30.5% | 1219 | 3.208 | 668 | 551 | 23 (6.1%) |
| 2026-2027 | 70 | 41.4% | 20.0% | 38.6% | 229 | 3.271 | 118 | 111 | 2 (2.9%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `425` of `450` (94.4%)
| metric | value |
|---|---|
| First goals recorded | 425 |
| Min minute | 1 |
| Max minute | 95 |
| Mean minute | 28.22 |
| Median (p50) | 23.0 |
| p25 | 11.0 |
| p75 | 40.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 143 |
| 16-30 | 126 |
| 31-45 | 72 |
| 46-60 | 45 |
| 61-75 | 15 |
| 76-90 | 19 |
| 91-120 | 5 |

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
| 2-1 | 47 |
| 1-1 | 46 |
| 1-0 | 29 |
| 1-2 | 27 |
| 2-2 | 26 |
| 3-1 | 26 |
| 2-0 | 26 |
| 0-0 | 25 |
| 0-1 | 23 |
| 1-3 | 21 |
| 3-2 | 19 |
| 3-0 | 14 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |
| 5-3 | 8 | 2 |
| 3-5 | 8 | 3 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 117 | 26.0% |
| Tue | 25 | 5.6% |
| Wed | 25 | 5.6% |
| Fri | 38 | 8.4% |
| Sat | 245 | 54.4% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 70 matches, expected 380 |
| 2 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 2.9% vs overall 5.6% (deviation 2.7 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 away outcome share 38.6% vs overall 31.8% |
| 5 | HIGH_SCORING_MATCHES | 7 match(es) with >= 8 total goals (extreme scorelines) |
| 6 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 7 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=6, fgte=6 rows) |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 70, "expected": 380}`
- `2.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 2.9, "overall_goalless_pct": 5.6, "deviation_pp": 2.7}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "away", "season_share": 38.6, "overall_share": 31.8}`
- `5.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 7, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "3-5", "total_goals": 8, "count": 3}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `6.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 11021, "distinct": 11011, "duplicates": 10}`
- `7.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 11021, "fgt_inconsistent": 6, "fgte_inconsistent": 6, "n_with_fgt": 10250}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
