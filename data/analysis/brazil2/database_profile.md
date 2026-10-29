# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-10-29T01:54:48+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `brazil2`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 98 |
| seasons | 14 |
| league_seasons | 56 |
| teams | 179 |
| team_aliases | 358 |
| team_seasons | 863 |
| matches | 13093 |
| standings | 2589 |

### 1.2 Leagues with data
- Catalog leagues: `98`
- Leagues with match data: `8`
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

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `brazil2`: `7`
- With match data: `7`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020 | False | complete | 380 | 20 | 2020-08-08 | 2021-01-30 |
| 2021 | False | complete | 380 | 20 | 2021-05-28 | 2021-11-28 |
| 2022 | False | complete | 380 | 20 | 2022-04-09 | 2022-11-06 |
| 2023 | False | complete | 380 | 20 | 2023-04-15 | 2023-11-25 |
| 2024 | False | complete | 373 | 20 | 2024-04-20 | 2024-11-24 |
| 2025 | True | complete | 380 | 20 | 2025-04-05 | 2025-11-23 |
| 2026 | True | in_progress | 350 | 20 | 2026-03-21 | 2026-10-27 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 13093 | 13093 | 0 |
| matches (league_season_id, game_index) | 13093 | 13093 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 13093 | 13091 | 2 |
| team_seasons (league_season_id, team_id) | 863 | 863 | 0 |
| team_seasons api_name within a season | 863 | 863 | 0 |
| team_seasons api_slug within a season | 863 | 863 | 0 |
| standings (league_season_id, team_id, view) | 2589 | 2589 | 0 |
| team_aliases (form, value) | 358 | 358 | 0 |
| leagues.api_key | 98 | 98 | 0 |
| seasons.name | 14 | 14 | 0 |
| teams.canonical_name | 179 | 179 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `13093`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 13093 | 0.0% |
| kickoff_time | 0 | 13093 | 0.0% |
| home_team_id | 0 | 13093 | 0.0% |
| away_team_id | 0 | 13093 | 0.0% |
| home_score | 0 | 13093 | 0.0% |
| away_score | 0 | 13093 | 0.0% |
| home_ht | 315 | 12778 | 2.4% |
| away_ht | 315 | 12778 | 2.4% |
| first_goal_time | 1365 | 11728 | 10.4% |
| first_goal_time_extra | 1365 | 11728 | 10.4% |
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
| Home | 1229 | 46.9% |
| Draw | 758 | 28.9% |
| Away | 636 | 24.2% |
| Total | 2623 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 5687 |
| Average goals per match | 2.168 |
| Home goals | 3371 (avg 1.285) |
| Away goals | 2316 (avg 0.883) |
| Home goal share | 59.3% |
| Goalless matches | 282 (10.8%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020 | 380 | 46.1% | 28.2% | 25.8% | 824 | 2.168 | 485 | 339 | 43 (11.3%) |
| 2021 | 380 | 43.4% | 30.3% | 26.3% | 826 | 2.174 | 474 | 352 | 47 (12.4%) |
| 2022 | 380 | 49.7% | 31.8% | 18.4% | 766 | 2.016 | 487 | 279 | 49 (12.9%) |
| 2023 | 380 | 46.1% | 29.2% | 24.7% | 796 | 2.095 | 477 | 319 | 44 (11.6%) |
| 2024 | 373 | 52.3% | 25.2% | 22.5% | 815 | 2.185 | 492 | 323 | 37 (9.9%) |
| 2025 | 380 | 45.8% | 30.5% | 23.7% | 843 | 2.218 | 491 | 352 | 33 (8.7%) |
| 2026 | 350 | 44.6% | 26.9% | 28.6% | 817 | 2.334 | 465 | 352 | 29 (8.3%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2341` of `2623` (89.2%)
| metric | value |
|---|---|
| First goals recorded | 2341 |
| Min minute | 1 |
| Max minute | 101 |
| Mean minute | 35.18 |
| Median (p50) | 30.0 |
| p25 | 14.0 |
| p75 | 52.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 647 |
| 16-30 | 527 |
| 31-45 | 391 |
| 46-60 | 355 |
| 61-75 | 214 |
| 76-90 | 150 |
| 91-120 | 57 |

### 2.5 Standings coverage
- (season, view) pairs present: `21` of `21` expected
- Standings rows total: `420`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020 | classic | 20 | 1..22 | 20 |
| 2020 | goals | 20 | 11..40 | 20 |
| 2020 | luck | 20 | 1..58 | 20 |
| 2021 | classic | 20 | 1..21 | 20 |
| 2021 | goals | 20 | 10..34 | 20 |
| 2021 | luck | 20 | 1..40 | 20 |
| 2022 | classic | 20 | 1..22 | 20 |
| 2022 | goals | 20 | 15..42 | 20 |
| 2022 | luck | 20 | 1..58 | 20 |
| 2023 | classic | 20 | 1..21 | 20 |
| 2023 | goals | 20 | 5..32 | 20 |
| 2023 | luck | 20 | 1..40 | 20 |
| 2024 | classic | 20 | 1..22 | 20 |
| 2024 | goals | 20 | 13..43 | 20 |
| 2024 | luck | 20 | 1..56 | 20 |
| 2025 | classic | 20 | 1..23 | 20 |
| 2025 | goals | 20 | 13..48 | 20 |
| 2025 | luck | 20 | 1..57 | 20 |
| 2026 | classic | 20 | 1..20 | 20 |
| 2026 | goals | 20 | 1..20 | 20 |
| 2026 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-0 | 404 |
| 1-1 | 359 |
| 2-1 | 282 |
| 0-0 | 282 |
| 0-1 | 255 |
| 2-0 | 228 |
| 1-2 | 160 |
| 3-0 | 105 |
| 2-2 | 100 |
| 0-2 | 93 |
| 3-1 | 85 |
| 3-2 | 41 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 2-7 | 9 | 1 |
| 3-5 | 8 | 1 |
| 2-6 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 594 | 22.6% |
| Mon | 120 | 4.6% |
| Tue | 242 | 9.2% |
| Wed | 359 | 13.7% |
| Thu | 203 | 7.7% |
| Fri | 221 | 8.4% |
| Sat | 884 | 33.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2024 has 373 matches, expected 380 |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026 has 350 matches, expected 380 |
| 3 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 4 | GOALLESS_SHARE_OUTLIER | Season 2021 goalless share 12.4% vs overall 10.8% (deviation 1.6 pp) |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2022 goalless share 12.9% vs overall 10.8% (deviation 2.1 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2022 away outcome share 18.4% vs overall 24.2% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2024 home outcome share 52.3% vs overall 46.9% |
| 8 | GOALLESS_SHARE_OUTLIER | Season 2025 goalless share 8.7% vs overall 10.8% (deviation 2.1 pp) |
| 9 | GOALLESS_SHARE_OUTLIER | Season 2026 goalless share 8.3% vs overall 10.8% (deviation 2.5 pp) |
| 10 | OUTCOME_SHARE_OUTLIER | Season 2026 away outcome share 28.6% vs overall 24.2% |
| 11 | HIGH_SCORING_MATCHES | 3 match(es) with >= 8 total goals (extreme scorelines) |
| 12 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (2 extra rows) |
| 13 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=294, fgte=294 rows) |
| 14 | STANDINGS_INCOMPLETE | Standings 2020/classic rows=20 positions=1..22 teams=20 |
| 15 | STANDINGS_INCOMPLETE | Standings 2020/goals rows=20 positions=11..40 teams=20 |
| 16 | STANDINGS_INCOMPLETE | Standings 2020/luck rows=20 positions=1..58 teams=20 |
| 17 | STANDINGS_INCOMPLETE | Standings 2021/classic rows=20 positions=1..21 teams=20 |
| 18 | STANDINGS_INCOMPLETE | Standings 2021/goals rows=20 positions=10..34 teams=20 |
| 19 | STANDINGS_INCOMPLETE | Standings 2021/luck rows=20 positions=1..40 teams=20 |
| 20 | STANDINGS_INCOMPLETE | Standings 2022/classic rows=20 positions=1..22 teams=20 |
| 21 | STANDINGS_INCOMPLETE | Standings 2022/goals rows=20 positions=15..42 teams=20 |
| 22 | STANDINGS_INCOMPLETE | Standings 2022/luck rows=20 positions=1..58 teams=20 |
| 23 | STANDINGS_INCOMPLETE | Standings 2023/classic rows=20 positions=1..21 teams=20 |
| 24 | STANDINGS_INCOMPLETE | Standings 2023/goals rows=20 positions=5..32 teams=20 |
| 25 | STANDINGS_INCOMPLETE | Standings 2023/luck rows=20 positions=1..40 teams=20 |
| 26 | STANDINGS_INCOMPLETE | Standings 2024/classic rows=20 positions=1..22 teams=20 |
| 27 | STANDINGS_INCOMPLETE | Standings 2024/goals rows=20 positions=13..43 teams=20 |
| 28 | STANDINGS_INCOMPLETE | Standings 2024/luck rows=20 positions=1..56 teams=20 |
| 29 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=20 positions=1..23 teams=20 |
| 30 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=20 positions=13..48 teams=20 |
| 31 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=20 positions=1..57 teams=20 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024", "n_matches": 373, "expected": 380}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 350, "expected": 380}`
- `3.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `4.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2021", "season_goalless_pct": 12.4, "overall_goalless_pct": 10.8, "deviation_pp": 1.6}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2022", "season_goalless_pct": 12.9, "overall_goalless_pct": 10.8, "deviation_pp": 2.1}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022", "outcome": "away", "season_share": 18.4, "overall_share": 24.2}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2024", "outcome": "home", "season_share": 52.3, "overall_share": 46.9}`
- `8.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025", "season_goalless_pct": 8.7, "overall_goalless_pct": 10.8, "deviation_pp": 2.1}`
- `9.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2026", "season_goalless_pct": 8.3, "overall_goalless_pct": 10.8, "deviation_pp": 2.5}`
- `10.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2026", "outcome": "away", "season_share": 28.6, "overall_share": 24.2}`
- `11.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 3, "threshold": 8, "examples": [{"scoreline": "2-7", "total_goals": 9, "count": 1}, {"scoreline": "3-5", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}]}`
- `12.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 13093, "distinct": 13091, "duplicates": 2}`
- `13.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 13093, "fgt_inconsistent": 294, "fgte_inconsistent": 294, "n_with_fgt": 11728}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `15.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "goals", "n_rows": 20, "min_pos": 11, "max_pos": 40, "distinct_teams": 20}`
- `16.` `STANDINGS_INCOMPLETE` details: `{"season": "2020", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `17.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 21, "distinct_teams": 20}`
- `18.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "goals", "n_rows": 20, "min_pos": 10, "max_pos": 34, "distinct_teams": 20}`
- `19.` `STANDINGS_INCOMPLETE` details: `{"season": "2021", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 40, "distinct_teams": 20}`
- `20.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `21.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "goals", "n_rows": 20, "min_pos": 15, "max_pos": 42, "distinct_teams": 20}`
- `22.` `STANDINGS_INCOMPLETE` details: `{"season": "2022", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 58, "distinct_teams": 20}`
- `23.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 21, "distinct_teams": 20}`
- `24.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "goals", "n_rows": 20, "min_pos": 5, "max_pos": 32, "distinct_teams": 20}`
- `25.` `STANDINGS_INCOMPLETE` details: `{"season": "2023", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 40, "distinct_teams": 20}`
- `26.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 22, "distinct_teams": 20}`
- `27.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "goals", "n_rows": 20, "min_pos": 13, "max_pos": 43, "distinct_teams": 20}`
- `28.` `STANDINGS_INCOMPLETE` details: `{"season": "2024", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 56, "distinct_teams": 20}`
- `29.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 20, "min_pos": 1, "max_pos": 23, "distinct_teams": 20}`
- `30.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 20, "min_pos": 13, "max_pos": 48, "distinct_teams": 20}`
- `31.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 20, "min_pos": 1, "max_pos": 57, "distinct_teams": 20}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
