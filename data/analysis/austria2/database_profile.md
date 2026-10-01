# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T15:44:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `austria2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 3 |
| league_seasons | 8 |
| teams | 62 |
| team_aliases | 124 |
| team_seasons | 113 |
| matches | 1111 |
| standings | 339 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `4`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 2 | 263 |
| australia | A-League | Australia | 2 | 332 |
| austria1 | Bundesliga | Austria | 2 | 237 |
| austria2 | 2. Liga | Austria | 2 | 279 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `austria2`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025-2026 | True | complete | 223 | 16 | 2025-08-01 | 2026-05-14 |
| 2026-2027 | True | in_progress | 56 | 16 | 2026-07-31 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 1111 | 1111 | 0 |
| matches (league_season_id, game_index) | 1111 | 1111 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 1111 | 1109 | 2 |
| team_seasons (league_season_id, team_id) | 113 | 113 | 0 |
| team_seasons api_name within a season | 113 | 113 | 0 |
| team_seasons api_slug within a season | 113 | 113 | 0 |
| standings (league_season_id, team_id, view) | 339 | 339 | 0 |
| team_aliases (form, value) | 124 | 124 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 3 | 3 | 0 |
| teams.canonical_name | 62 | 62 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `1111`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 1111 | 0.0% |
| kickoff_time | 0 | 1111 | 0.0% |
| home_team_id | 0 | 1111 | 0.0% |
| away_team_id | 0 | 1111 | 0.0% |
| home_score | 0 | 1111 | 0.0% |
| away_score | 0 | 1111 | 0.0% |
| home_ht | 1 | 1110 | 0.1% |
| away_ht | 1 | 1110 | 0.1% |
| first_goal_time | 72 | 1039 | 6.5% |
| first_goal_time_extra | 72 | 1039 | 6.5% |
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
| Home | 121 | 43.4% |
| Draw | 66 | 23.7% |
| Away | 92 | 33.0% |
| Total | 279 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 784 |
| Average goals per match | 2.81 |
| Home goals | 425 (avg 1.523) |
| Away goals | 359 (avg 1.287) |
| Home goal share | 54.2% |
| Goalless matches | 19 (6.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 223 | 41.3% | 26.0% | 32.7% | 599 | 2.686 | 317 | 282 | 18 (8.1%) |
| 2026-2027 | 56 | 51.8% | 14.3% | 33.9% | 185 | 3.304 | 108 | 77 | 1 (1.8%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `259` of `279` (92.8%)
| metric | value |
|---|---|
| First goals recorded | 259 |
| Min minute | 1 |
| Max minute | 96 |
| Mean minute | 28.59 |
| Median (p50) | 22.0 |
| p25 | 10.0 |
| p75 | 41.5 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 95 |
| 16-30 | 68 |
| 31-45 | 41 |
| 46-60 | 26 |
| 61-75 | 13 |
| 76-90 | 11 |
| 91-120 | 5 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `96`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025-2026 | classic | 16 | 1..16 | 16 |
| 2025-2026 | goals | 16 | 1..16 | 16 |
| 2025-2026 | luck | 16 | 1..16 | 16 |
| 2026-2027 | classic | 16 | 1..16 | 16 |
| 2026-2027 | goals | 16 | 1..16 | 16 |
| 2026-2027 | luck | 16 | 1..16 | 16 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 28 |
| 2-1 | 25 |
| 0-2 | 23 |
| 1-0 | 23 |
| 0-1 | 20 |
| 0-0 | 19 |
| 2-0 | 17 |
| 1-2 | 16 |
| 2-2 | 14 |
| 3-1 | 13 |
| 3-0 | 12 |
| 0-3 | 8 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-4 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 33 | 11.8% |
| Mon | 7 | 2.5% |
| Tue | 4 | 1.4% |
| Thu | 7 | 2.5% |
| Fri | 151 | 54.1% |
| Sat | 77 | 27.6% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 223 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 16 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 56 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026-2027 has 16 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026-2027 has data but state is 'in_progress' |
| 6 | SEASON_AVG_GOALS_OUTLIER | Season 2026-2027 avg goals 3.304 vs overall 2.81 (deviation 0.494) |
| 7 | GOALLESS_SHARE_OUTLIER | Season 2026-2027 goalless share 1.8% vs overall 6.8% (deviation 5.0 pp) |
| 8 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 home outcome share 51.8% vs overall 43.4% |
| 9 | OUTCOME_SHARE_OUTLIER | Season 2026-2027 draw outcome share 14.3% vs overall 23.7% |
| 10 | HIGH_SCORING_MATCHES | 1 match(es) with >= 8 total goals (extreme scorelines) |
| 11 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 12 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=1, fgte=1 rows) |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=16 positions=1..16 teams=16 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=16 positions=1..16 teams=16 |
| 15 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=16 positions=1..16 teams=16 |
| 16 | STANDINGS_INCOMPLETE | Standings 2026-2027/classic rows=16 positions=1..16 teams=16 |
| 17 | STANDINGS_INCOMPLETE | Standings 2026-2027/goals rows=16 positions=1..16 teams=16 |
| 18 | STANDINGS_INCOMPLETE | Standings 2026-2027/luck rows=16 positions=1..16 teams=16 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 223, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 16, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 56, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_teams": 16, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026-2027", "season_state": "in_progress"}`
- `6.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2026-2027", "season_avg_goals": 3.304, "overall_avg_goals": 2.81, "deviation": 0.494}`
- `7.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026-2027", "season_goalless_pct": 1.8, "overall_goalless_pct": 6.8, "deviation_pp": 5.0}`
- `8.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "home", "season_share": 51.8, "overall_share": 43.4}`
- `9.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026-2027", "outcome": "draw", "season_share": 14.3, "overall_share": 23.7}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 1, "threshold": 8, "examples": [{"scoreline": "4-4", "total_goals": 8, "count": 1}]}`
- `11.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 1111, "distinct": 1109, "duplicates": 2}`
- `12.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 1111, "fgt_inconsistent": 1, "fgte_inconsistent": 1, "n_with_fgt": 1039}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "classic", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "goals", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2026-2027", "view": "luck", "n_rows": 16, "min_pos": 1, "max_pos": 16, "distinct_teams": 16}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
