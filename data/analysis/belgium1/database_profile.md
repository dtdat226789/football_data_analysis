# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T10:55:13+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `belgium1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 3 |
| league_seasons | 12 |
| teams | 98 |
| team_aliases | 196 |
| team_seasons | 176 |
| matches | 1728 |
| standings | 528 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `6`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 262 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |
| azer | Premier League | Azerbaijan | 2 | 234 |
| belgium1 | Jupiler Pro League | Belgium | 2 | 384 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `belgium1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 321 | 20 | 2025-07-25 | 2026-05-31 |
| 2026-2027 | True | in_progress | 63 | 18 | 2026-08-07 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 1728 | 1728 | 0 |
| matches (league_season_id, game_index) | 1728 | 1728 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 1728 | 1726 | 2 |
| team_seasons (league_season_id, team_id) | 176 | 176 | 0 |
| team_seasons api_name within a season | 176 | 176 | 0 |
| team_seasons api_slug within a season | 176 | 176 | 0 |
| standings (league_season_id, team_id, view) | 528 | 528 | 0 |
| team_aliases (form, value) | 196 | 196 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 3 | 3 | 0 |
| teams.canonical_name | 98 | 98 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `1728`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 1728 | 0.0% |
| kickoff_time | 0 | 1728 | 0.0% |
| home_team_id | 0 | 1728 | 0.0% |
| away_team_id | 0 | 1728 | 0.0% |
| home_score | 0 | 1728 | 0.0% |
| away_score | 0 | 1728 | 0.0% |
| home_ht | 3 | 1725 | 0.2% |
| away_ht | 3 | 1725 | 0.2% |
| first_goal_time | 121 | 1607 | 7.0% |
| first_goal_time_extra | 121 | 1607 | 7.0% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 6 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 5 |
| away_ht | 0 | 4 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 164 | 42.7% |
| Draw | 93 | 24.2% |
| Away | 127 | 33.1% |
| Total | 384 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 1049 |
| Average goals per match | 2.732 |
| Home goals | 572 (avg 1.49) |
| Away goals | 477 (avg 1.242) |
| Home goal share | 54.5% |
| Goalless matches | 28 (7.3%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 321 | 41.1% | 25.2% | 33.6% | 864 | 2.692 | 465 | 399 | 25 (7.8%) |
| 2026-2027 | 63 | 50.8% | 19.0% | 30.2% | 185 | 2.937 | 107 | 78 | 3 (4.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `356` of `384` (92.7%)
| metric | value |
|---|---|
| First goals recorded | 356 |
| Min minute | 1 |
| Max minute | 93 |
| Mean minute | 30.46 |
| Median (p50) | 24.0 |
| p25 | 11.75 |
| p75 | 44.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 123 |
| 16-30 | 84 |
| 31-45 | 64 |
| 46-60 | 37 |
| 61-75 | 27 |
| 76-90 | 17 |
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
| 1-1 | 42 |
| 2-1 | 35 |
| 1-0 | 34 |
| 1-2 | 32 |
| 2-0 | 31 |
| 0-0 | 28 |
| 0-1 | 27 |
| 0-2 | 23 |
| 2-2 | 17 |
| 3-0 | 17 |
| 3-1 | 14 |
| 1-3 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 5-5 | 10 | 2 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 174 | 45.3% |
| Mon | 6 | 1.6% |
| Tue | 7 | 1.8% |
| Wed | 5 | 1.3% |
| Thu | 8 | 2.1% |
| Fri | 43 | 11.2% |
| Sat | 141 | 36.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 321 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 63 matches, expected 380 |
| 3 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 18 teams, expected 20 |
| 4 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 4.8% vs overall 7.3% (deviation 2.5 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 50.8% vs overall 42.7% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 19.0% vs overall 24.2% |
| 8 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 9 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 10 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=2, fgte=2 rows) |
| 11 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=18 positions=1..18 teams=18 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=18 positions=1..18 teams=18 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=18 positions=1..18 teams=18 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 321, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 63, "expected": 380}`
- `3.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 18, "expected": 20}`
- `4.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 4.8, "overall_goalless_pct": 7.3, "deviation_pp": 2.5}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 50.8, "overall_share": 42.7}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 19.0, "overall_share": 24.2}`
- `8.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "5-5", "total_goals": 10, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}]}`
- `9.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 1728, "distinct": 1726, "duplicates": 2}`
- `10.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 1728, "fgt_inconsistent": 2, "fgte_inconsistent": 2, "n_with_fgt": 1607}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 18, "min_pos": 1, "max_pos": 18, "distinct_teams": 18}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
