# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-19T08:55:00+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `premier`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 7 |
| league_seasons | 7 |
| teams | 28 |
| team_aliases | 56 |
| team_seasons | 120 |
| matches | 2280 |
| standings | 360 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `1`
| api_key | name | country | registered_seasons | matches |
|---|---|---|---|---|
| premier | Premier League | England | 7 | 2280 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `premier`: `7`
- With match data: `6`
- Registered but no data: `['2026-2027']`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2020-2021 | False | complete | 380 | 20 | 2020-09-12 | 2021-05-23 |
| 2021-2022 | False | complete | 380 | 20 | 2021-08-13 | 2022-05-22 |
| 2022-2023 | False | complete | 380 | 20 | 2022-08-05 | 2023-05-28 |
| 2023-2024 | False | complete | 380 | 20 | 2023-08-11 | 2024-05-19 |
| 2024-2025 | False | complete | 380 | 20 | 2024-08-16 | 2025-05-25 |
| 2025-2026 | True | complete | 380 | 20 | 2025-08-15 | 2026-05-24 |
| 2026-2027 | True | unknown | 0 | 0 | - | - |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 2280 | 2280 | 0 |
| matches (league_season_id, game_index) | 2280 | 2280 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 2280 | 2280 | 0 |
| team_seasons (league_season_id, team_id) | 120 | 120 | 0 |
| team_seasons api_name within a season | 120 | 120 | 0 |
| team_seasons api_slug within a season | 120 | 120 | 0 |
| standings (league_season_id, team_id, view) | 360 | 360 | 0 |
| team_aliases (form, value) | 56 | 56 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 7 | 7 | 0 |
| teams.canonical_name | 28 | 28 | 0 |

### 1.5 NULL counts (matches, important fields)
- Total matches: `2280`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 2280 | 0.0% |
| kickoff_time | 0 | 2280 | 0.0% |
| home_team_id | 0 | 2280 | 0.0% |
| away_team_id | 0 | 2280 | 0.0% |
| home_score | 0 | 2280 | 0.0% |
| away_score | 0 | 2280 | 0.0% |
| home_ht | 0 | 2280 | 0.0% |
| away_ht | 0 | 2280 | 0.0% |
| first_goal_time | 129 | 2151 | 5.7% |
| first_goal_time_extra | 129 | 2151 | 5.7% |
  > Semantics: `home_ht`/`away_ht` NULL together; `first_goal_time`/`first_goal_time_extra` NULL iff goalless.

### 1.6 Value ranges
| metric | min | max |
|---|---|---|
| home_score | 0 | 9 |
| away_score | 0 | 8 |
| first_goal_time | 1 | 99 |
| home_ht | 0 | 5 |
| away_ht | 0 | 5 |
- first_goal_time NULL semantics consistent: `True`

## 2. Calculated statistics

### 2.1 Outcome distribution (overall)
| outcome | count | pct |
|---|---|---|
| Home | 983 | 43.1% |
| Draw | 537 | 23.6% |
| Away | 760 | 33.3% |
| Total | 2280 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 6585 |
| Average goals per match | 2.888 |
| Home goals | 3549 (avg 1.557) |
| Away goals | 3036 (avg 1.332) |
| Home goal share | 53.9% |
| Goalless matches | 129 (5.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2020-2021 | 380 | 37.9% | 21.8% | 40.3% | 1024 | 2.695 | 514 | 510 | 30 (7.9%) |
| 2021-2022 | 380 | 42.9% | 23.2% | 33.9% | 1071 | 2.818 | 575 | 496 | 22 (5.8%) |
| 2022-2023 | 380 | 48.4% | 22.9% | 28.7% | 1084 | 2.853 | 621 | 463 | 23 (6.1%) |
| 2023-2024 | 380 | 46.1% | 21.6% | 32.4% | 1246 | 3.279 | 684 | 562 | 11 (2.9%) |
| 2024-2025 | 380 | 40.8% | 24.5% | 34.7% | 1115 | 2.934 | 575 | 540 | 16 (4.2%) |
| 2025-2026 | 380 | 42.6% | 27.4% | 30.0% | 1045 | 2.75 | 580 | 465 | 27 (7.1%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `2151` of `2280` (94.3%)
| metric | value |
|---|---|
| First goals recorded | 2151 |
| Min minute | 1 |
| Max minute | 99 |
| Mean minute | 29.88 |
| Median (p50) | 25.0 |
| p25 | 11.0 |
| p75 | 45.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 737 |
| 16-30 | 535 |
| 31-45 | 345 |
| 46-60 | 285 |
| 61-75 | 142 |
| 76-90 | 86 |
| 91-120 | 21 |

### 2.5 Standings coverage
- (season, view) pairs present: `18` of `18` expected
- Standings rows total: `360`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2020-2021 | classic | 20 | 1..20 | 20 |
| 2020-2021 | goals | 20 | 1..20 | 20 |
| 2020-2021 | luck | 20 | 1..20 | 20 |
| 2021-2022 | classic | 20 | 1..20 | 20 |
| 2021-2022 | goals | 20 | 1..20 | 20 |
| 2021-2022 | luck | 20 | 1..20 | 20 |
| 2022-2023 | classic | 20 | 1..20 | 20 |
| 2022-2023 | goals | 20 | 1..20 | 20 |
| 2022-2023 | luck | 20 | 1..20 | 20 |
| 2023-2024 | classic | 20 | 1..20 | 20 |
| 2023-2024 | goals | 20 | 1..20 | 20 |
| 2023-2024 | luck | 20 | 1..20 | 20 |
| 2024-2025 | classic | 20 | 1..20 | 20 |
| 2024-2025 | goals | 20 | 1..20 | 20 |
| 2024-2025 | luck | 20 | 1..20 | 20 |
| 2025-2026 | classic | 20 | 1..20 | 20 |
| 2025-2026 | goals | 20 | 1..20 | 20 |
| 2025-2026 | luck | 20 | 1..20 | 20 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 250 |
| 1-0 | 189 |
| 2-1 | 187 |
| 0-1 | 167 |
| 1-2 | 159 |
| 2-0 | 154 |
| 2-2 | 131 |
| 0-0 | 129 |
| 0-2 | 126 |
| 3-1 | 111 |
| 3-0 | 103 |
| 1-3 | 71 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 9-0 | 9 | 2 |
| 7-2 | 9 | 1 |
| 6-3 | 9 | 2 |
| 4-5 | 9 | 1 |
| 3-6 | 9 | 1 |
| 6-2 | 8 | 2 |
| 5-3 | 8 | 2 |
| 4-4 | 8 | 4 |
| 2-6 | 8 | 1 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 665 | 29.2% |
| Mon | 136 | 6.0% |
| Tue | 126 | 5.5% |
| Wed | 176 | 7.7% |
| Thu | 77 | 3.4% |
| Fri | 69 | 3.0% |
| Sat | 1031 | 45.2% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | SEASON_REGISTERED_NO_DATA | Season 2026-2027 is registered but has no match data (declared_by_api=True, state=unknown) |
| 2 | MATCH_COUNT_UNEXPECTED | Season 2026-2027 has 0 matches, expected 380 |
| 3 | GOALLESS_SHARE_OUTLIER | Season 2020-2021 goalless share 7.9% vs overall 5.7% (deviation 2.2 pp) |
| 4 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 home outcome share 37.9% vs overall 43.1% |
| 5 | OUTCOME_SHARE_OUTLIER | Season 2020-2021 away outcome share 40.3% vs overall 33.3% |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 home outcome share 48.4% vs overall 43.1% |
| 7 | OUTCOME_SHARE_OUTLIER | Season 2022-2023 away outcome share 28.7% vs overall 33.3% |
| 8 | SEASON_AVG_GOALS_OUTLIER | Season 2023-2024 avg goals 3.279 vs overall 2.888 (deviation 0.391) |
| 9 | GOALLESS_SHARE_OUTLIER | Season 2023-2024 goalless share 2.9% vs overall 5.7% (deviation 2.8 pp) |
| 10 | HIGH_SCORING_MATCHES | 17 match(es) with >= 8 total goals (extreme scorelines) |
- `1.` `SEASON_REGISTERED_NO_DATA` details: `{"season": "2026-2027"}`
- `2.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026-2027", "n_matches": 0, "expected": 380}`
- `3.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2020-2021", "season_goalless_pct": 7.9, "overall_goalless_pct": 5.7, "deviation_pp": 2.2}`
- `4.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "home", "season_share": 37.9, "overall_share": 43.1}`
- `5.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2020-2021", "outcome": "away", "season_share": 40.3, "overall_share": 33.3}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "home", "season_share": 48.4, "overall_share": 43.1}`
- `7.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2022-2023", "outcome": "away", "season_share": 28.7, "overall_share": 33.3}`
- `8.` `SEASON_AVG_GOALS_OUTLIER` details: `{"season": "2023-2024", "season_avg_goals": 3.279, "overall_avg_goals": 2.888, "deviation": 0.391}`
- `9.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2023-2024", "season_goalless_pct": 2.9, "overall_goalless_pct": 5.7, "deviation_pp": 2.8}`
- `10.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 17, "threshold": 8, "examples": [{"scoreline": "9-0", "total_goals": 9, "count": 2}, {"scoreline": "7-2", "total_goals": 9, "count": 1}, {"scoreline": "6-3", "total_goals": 9, "count": 2}, {"scoreline": "4-5", "total_goals": 9, "count": 1}, {"scoreline": "3-6", "total_goals": 9, "count": 1}, {"scoreline": "6-2", "total_goals": 8, "count": 2}, {"scoreline": "5-3", "total_goals": 8, "count": 2}, {"scoreline": "4-4", "total_goals": 8, "count": 4}]}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
