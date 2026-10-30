# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-30T03:49:00+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `develop21`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 118 |
| teams | 409 |
| team_aliases | 818 |
| team_seasons | 1856 |
| matches | 26971 |
| standings | 5568 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `18`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1697 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 915 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1023 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1799 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |
| brazil2 | Serie B | Brazil | 7 | 2623 |
| bulgaria1 | efbet League | Bulgaria | 7 | 1461 |
| cha | Championship | England | 7 | 3463 |
| china | Super League | China | 7 | 1482 |
| czech1 | Chance Liga | Czech Republic | 7 | 1640 |
| czech2 | ChNL | Czech Republic | 7 | 1478 |
| czech3a | 3. CFL - Group A | Czech Republic | 5 | 1089 |
| czech3b | 3. CFL - Group B | Czech Republic | 7 | 1423 |
| denmark1 | Superliga | Denmark | 7 | 926 |
| denmark2 | 1st Division | Denmark | 7 | 848 |
| develop21 | Professional Development League | England | 1 | 68 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `develop21`: `1`
- With match data: `1`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2026-2027 | True | in_progress | 68 | 17 | 2026-08-14 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 26971 | 26971 | 0 |
| matches (league_season_id, game_index) | 26971 | 26971 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 26971 | 26966 | 5 |
| team_seasons (league_season_id, team_id) | 1856 | 1856 | 0 |
| team_seasons api_name within a season | 1856 | 1856 | 0 |
| team_seasons api_slug within a season | 1856 | 1856 | 0 |
| standings (league_season_id, team_id, view) | 5568 | 5568 | 0 |
| team_aliases (form, value) | 818 | 818 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 409 | 409 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `26971`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 26971 | 0.0% |
| kickoff_time | 0 | 26971 | 0.0% |
| home_team_id | 0 | 26971 | 0.0% |
| away_team_id | 0 | 26971 | 0.0% |
| home_score | 0 | 26971 | 0.0% |
| away_score | 0 | 26971 | 0.0% |
| home_ht | 340 | 26631 | 1.3% |
| away_ht | 340 | 26631 | 1.3% |
| first_goal_time | 2352 | 24619 | 8.7% |
| first_goal_time_extra | 2352 | 24619 | 8.7% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 9 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 28 | 41.2% |
| Draw | 15 | 22.1% |
| Away | 25 | 36.8% |
| Total | 68 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 274 |
| Average goals per match | 4.029 |
| Home goals | 143 (avg 2.103) |
| Away goals | 131 (avg 1.926) |
| Home goal share | 52.2% |
| Goalless matches | 1 (1.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2026-2027 | 68 | 41.2% | 22.1% | 36.8% | 274 | 4.029 | 143 | 131 | 1 (1.5%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `67` of `68` (98.5%)
| metric | value |
|---|---|
| First goals recorded | 67 |
| Min minute | 1 |
| Max minute | 70 |
| Mean minute | 23.69 |
| Median (p50) | 20.0 |
| p25 | 11.5 |
| p75 | 34.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 23 |
| 16-30 | 24 |
| 31-45 | 14 |
| 46-60 | 3 |
| 61-75 | 3 |
| 76-90 | 0 |
| 91-120 | 0 |

### 2.5 Standings coverage
- (season, view) pairs present: `3` of `3` expected
- Standings rows total: `51`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2026-2027 | classic | 17 | 1..17 | 17 |
| 2026-2027 | goals | 17 | 1..17 | 17 |
| 2026-2027 | luck | 17 | 1..17 | 17 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 2-2 | 9 |
| 3-1 | 7 |
| 2-0 | 4 |
| 1-2 | 4 |
| 0-2 | 4 |
| 4-1 | 4 |
| 2-1 | 3 |
| 0-1 | 3 |
| 1-0 | 3 |
| 1-1 | 3 |
| 0-4 | 2 |
| 1-3 | 2 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-4 | 10 | 1 |
| 3-6 | 9 | 1 |
| 5-3 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 4 | 5.9% |
| Mon | 10 | 14.7% |
| Tue | 43 | 63.2% |
| Wed | 1 | 1.5% |
| Fri | 9 | 13.2% |
| Sat | 1 | 1.5% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 68 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 17 teams, expected 20 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 4 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 5 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (5 extra rows) |
| 6 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=310, fgte=310 rows) |
| 7 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=17 positions=1..17 teams=17 |
| 8 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=17 positions=1..17 teams=17 |
| 9 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=17 positions=1..17 teams=17 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 68, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 17, "expected": 20}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `4.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "6-4", "total_goals": 10, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `5.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 26971, "distinct": 26966, "duplicates": 5}`
- `6.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 26971, "fgt_inconsistent": 310, "fgte_inconsistent": 310, "n_with_fgt": 24619}`
- `7.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `8.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 17, "min_pos": 1, "max_pos": 17, "distinct_teams": 17}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
