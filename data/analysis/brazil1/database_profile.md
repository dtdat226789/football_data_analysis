# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-26T01:27:19+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `brazil1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 49 |
| teams | 153 |
| team_aliases | 306 |
| team_seasons | 723 |
| matches | 10461 |
| standings | 2169 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `7`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| algir1 | Ligue 1 | Algeria | 7 | 1696 |
| australia | A-League | Australia | 7 | 962 |
| austria1 | Bundesliga | Austria | 7 | 913 |
| austria2 | 2. Liga | Austria | 7 | 1503 |
| azer | Premier League | Azerbaijan | 7 | 1021 |
| belgium1 | Jupiler Pro League | Belgium | 7 | 1795 |
| brazil1 | Serie A Betano | Brazil | 7 | 2571 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `brazil1`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 380 | 20 | 2020-08-09 | 2021-02-26 |
| 2021 | False | complete | 380 | 20 | 2021-05-30 | 2021-12-10 |
| 2022 | False | complete | 380 | 20 | 2022-04-09 | 2022-11-13 |
| 2023 | False | complete | 375 | 20 | 2023-04-15 | 2023-12-07 |
| 2024 | False | complete | 380 | 20 | 2024-04-13 | 2024-12-08 |
| 2025 | True | complete | 380 | 20 | 2025-03-29 | 2025-12-07 |
| 2026 | True | in_progress | 296 | 20 | 2026-01-28 | 2026-10-11 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 10461 | 10461 | 0 |
| matches (league_season_id, game_index) | 10461 | 10461 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 10461 | 10459 | 2 |
| team_seasons (league_season_id, team_id) | 723 | 723 | 0 |
| team_seasons api_name within a season | 723 | 723 | 0 |
| team_seasons api_slug within a season | 723 | 723 | 0 |
| standings (league_season_id, team_id, view) | 2169 | 2169 | 0 |
| team_aliases (form, value) | 306 | 306 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 153 | 153 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `10461`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 10461 | 0.0% |
| kickoff_time | 0 | 10461 | 0.0% |
| home_team_id | 0 | 10461 | 0.0% |
| away_team_id | 0 | 10461 | 0.0% |
| home_score | 0 | 10461 | 0.0% |
| away_score | 0 | 10461 | 0.0% |
| home_ht | 315 | 10146 | 3.0% |
| away_ht | 315 | 10146 | 3.0% |
| first_goal_time | 1082 | 9379 | 10.3% |
| first_goal_time_extra | 1082 | 9379 | 10.3% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 8 |
| away_score | 0 | 8 |
| first_goal_time | 1 | 108 |
| home_ht | 0 | 7 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `False`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 1201 | 46.7% |
| Draw | 709 | 27.6% |
| Away | 661 | 25.7% |
| Total | 2571 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6296 |
| Average goals per match | 2.449 |
| Home goals | 3654 (avg 1.421) |
| Away goals | 2642 (avg 1.028) |
| Home goal share | 58.0% |
| Goalless matches | 202 (7.9%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 380 | 45.0% | 28.4% | 26.6% | 944 | 2.484 | 536 | 408 | 32 (8.4%) |
| 2021 | 380 | 45.8% | 29.7% | 24.5% | 842 | 2.216 | 483 | 359 | 44 (11.6%) |
| 2022 | 380 | 44.2% | 28.4% | 27.4% | 905 | 2.382 | 534 | 371 | 26 (6.8%) |
| 2023 | 375 | 46.9% | 25.9% | 27.2% | 930 | 2.48 | 531 | 399 | 30 (8.0%) |
| 2024 | 380 | 47.4% | 26.6% | 26.1% | 929 | 2.445 | 536 | 393 | 26 (6.8%) |
| 2025 | 380 | 50.3% | 26.1% | 23.7% | 959 | 2.524 | 580 | 379 | 27 (7.1%) |
| 2026 | 296 | 47.6% | 28.0% | 24.3% | 787 | 2.659 | 454 | 333 | 17 (5.7%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2090` of `2571` (81.3%)
| metric | value |
|---|---|
| First goals recorded | 2090 |
| Min minute | 1 |
| Max minute | 106 |
| Mean minute | 33.79 |
| Median (p50) | 29.0 |
| p25 | 13.0 |
| p75 | 49.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 616 |
| 16-30 | 477 |
| 31-45 | 365 |
| 46-60 | 314 |
| 61-75 | 159 |
| 76-90 | 107 |
| 91-120 | 52 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `420`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 20 | 1..22 | 20 |
| 2020 | goals | 20 | 7..37 | 20 |
| 2020 | luck | 20 | 1..58 | 20 |
| 2021 | classic | 20 | 1..22 | 20 |
| 2021 | goals | 20 | 30..59 | 20 |
| 2021 | luck | 20 | 2..74 | 20 |
| 2022 | classic | 20 | 1..22 | 20 |
| 2022 | goals | 20 | 15..47 | 20 |
| 2022 | luck | 20 | 1..58 | 20 |
| 2023 | classic | 20 | 1..22 | 20 |
| 2023 | goals | 20 | 8..50 | 20 |
| 2023 | luck | 20 | 1..58 | 20 |
| 2024 | classic | 20 | 1..22 | 20 |
| 2024 | goals | 20 | 20..54 | 20 |
| 2024 | luck | 20 | 1..58 | 20 |
| 2025 | classic | 20 | 1..21 | 20 |
| 2025 | goals | 20 | 10..34 | 20 |
| 2025 | luck | 20 | 1..40 | 20 |
| 2026 | classic | 20 | 1..20 | 20 |
| 2026 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 352 |
| 1-0 | 331 |
| 2-1 | 278 |
| 2-0 | 209 |
| 0-1 | 204 |
| 0-0 | 202 |
| 1-2 | 181 |
| 2-2 | 132 |
| 3-0 | 112 |
| 0-2 | 107 |
| 3-1 | 96 |
| 3-2 | 50 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 4-6 | 10 | 1 |
| 8-0 | 8 | 1 |
| 7-1 | 8 | 1 |
| 5-3 | 8 | 3 |
| 4-4 | 8 | 1 |
| 3-5 | 8 | 3 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 1129 | 43.9% |
| Mon | 177 | 6.9% |
| Tue | 124 | 4.8% |
| Wed | 145 | 5.6% |
| Thu | 401 | 15.6% |
| Fri | 175 | 6.8% |
| Sat | 420 | 16.3% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2023 has 375 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026 has 296 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 11.6% vs overall 7.9% (deviation 3.7 pp) |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 5.7% vs overall 7.9% (deviation 2.2 pp) |
| 6 | HIGH_SCORING_MATCHES | 10 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=294, fgte=294 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=20 positions=1..22 teams=20 |
| 10 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=20 positions=7..37 teams=20 |
| 11 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=20 positions=1..58 teams=20 |
| 12 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=20 positions=1..22 teams=20 |
| 13 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=20 positions=30..59 teams=20 |
| 14 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=20 positions=2..74 teams=20 |
| 15 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=20 positions=1..22 teams=20 |
| 16 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=20 positions=15..47 teams=20 |
| 17 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=20 positions=1..58 teams=20 |
| 18 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=20 positions=1..22 teams=20 |
| 19 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=20 positions=8..50 teams=20 |
| 20 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=20 positions=1..58 teams=20 |
| 21 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=20 positions=1..22 teams=20 |
| 22 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=20 positions=20..54 teams=20 |
| 23 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=20 positions=1..58 teams=20 |
| 24 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=20 positions=1..21 teams=20 |
| 25 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=20 positions=10..34 teams=20 |
| 26 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=20 positions=1..40 teams=20 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2023", "n_matches": 375, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 296, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 11.6, "overall_goalless_pct": 7.9, "deviation_pp": 3.7}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 5.7, "overall_goalless_pct": 7.9, "deviation_pp": 2.2}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 10, "threshold": 8, "examples": [{"scoreline": "4-6", "total_goals": 10, "count": 1}, {"scoreline": "8-0", "total_goals": 8, "count": 1}, {"scoreline": "7-1", "total_goals": 8, "count": 1}, {"scoreline": "5-3", "total_goals": 8, "count": 3}, {"scoreline": "4-4", "total_goals": 8, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 3}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 10461, "distinct": 10459, "duplicates": 2}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 10461, "fgt_inconsistent": 294, "fgte_inconsistent": 294, "n_with_fgt": 9379}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 20, "min_pos": 7, "max_pos": 37, "distinct_teams": 20}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 20, "min_pos": 30, "max_pos": 59, "distinct_teams": 20}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 20, "min_pos": 2, "max_pos": 74, "distinct_teams": 20}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 20, "min_pos": 15, "max_pos": 47, "distinct_teams": 20}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 20, "min_pos": 8, "max_pos": 50, "distinct_teams": 20}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 20, "min_pos": 20, "max_pos": 54, "distinct_teams": 20}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 21, "distinct_teams": 20}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 20, "min_pos": 10, "max_pos": 34, "distinct_teams": 20}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 40, "distinct_teams": 20}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
