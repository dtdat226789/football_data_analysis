# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-23T11:01:13+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `india1`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 5 |
| league_seasons | 77 |
| teams | 813 |
| team_aliases | 1626 |
| team_seasons | 1400 |
| matches | 13535 |
| standings | 4026 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `37`
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
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `india1`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2024-2025 | True | complete | 156 | 13 | 2024-09-13 | 2025-03-12 |
| 2025-2026 | True | complete | 91 | 14 | 2026-02-14 | 2026-05-21 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 13535 | 13535 | 0 |
| matches (league_season_id, game_index) | 13535 | 13535 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 13535 | 13525 | 10 |
| team_seasons (league_season_id, team_id) | 1400 | 1400 | 0 |
| team_seasons api_name within a season | 1400 | 1400 | 0 |
| team_seasons api_slug within a season | 1400 | 1400 | 0 |
| standings (league_season_id, team_id, view) | 4026 | 4026 | 0 |
| team_aliases (form, value) | 1626 | 1626 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 5 | 5 | 0 |
| teams.canonical_name | 813 | 813 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `13535`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 13535 | 0.0% |
| kickoff_time | 0 | 13535 | 0.0% |
| home_team_id | 0 | 13535 | 0.0% |
| away_team_id | 0 | 13535 | 0.0% |
| home_score | 0 | 13535 | 0.0% |
| away_score | 0 | 13535 | 0.0% |
| home_ht | 35 | 13500 | 0.3% |
| away_ht | 35 | 13500 | 0.3% |
| first_goal_time | 899 | 12636 | 6.6% |
| first_goal_time_extra | 899 | 12636 | 6.6% |
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
| Home | 101 | 40.9% |
| Draw | 67 | 27.1% |
| Away | 79 | 32.0% |
| Total | 247 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 669 |
| Average goals per match | 2.709 |
| Home goals | 356 (avg 1.441) |
| Away goals | 313 (avg 1.267) |
| Home goal share | 53.2% |
| Goalless matches | 21 (8.5%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2024-2025 | 156 | 42.3% | 24.4% | 33.3% | 448 | 2.872 | 232 | 216 | 11 (7.1%) |
| 2025-2026 | 91 | 38.5% | 31.9% | 29.7% | 221 | 2.429 | 124 | 97 | 10 (11.0%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `226` of `247` (91.5%)
| metric | value |
|---|---|
| First goals recorded | 226 |
| Min minute | 1 |
| Max minute | 94 |
| Mean minute | 31.38 |
| Median (p50) | 27.0 |
| p25 | 11.0 |
| p75 | 47.75 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 82 |
| 16-30 | 43 |
| 31-45 | 34 |
| 46-60 | 38 |
| 61-75 | 18 |
| 76-90 | 9 |
| 91-120 | 2 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `81`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2024-2025 | classic | 13 | 1..13 | 13 |
| 2024-2025 | goals | 13 | 1..13 | 13 |
| 2024-2025 | luck | 13 | 1..13 | 13 |
| 2025-2026 | classic | 14 | 1..14 | 14 |
| 2025-2026 | goals | 14 | 1..14 | 14 |
| 2025-2026 | luck | 14 | 1..14 | 14 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 32 |
| 1-0 | 24 |
| 0-0 | 21 |
| 1-2 | 19 |
| 2-1 | 17 |
| 2-0 | 16 |
| 0-2 | 15 |
| 3-0 | 14 |
| 0-1 | 12 |
| 2-2 | 12 |
| 3-2 | 10 |
| 1-3 | 10 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 45 | 18.2% |
| Mon | 24 | 9.7% |
| Tue | 18 | 7.3% |
| Wed | 19 | 7.7% |
| Thu | 32 | 13.0% |
| Fri | 38 | 15.4% |
| Sat | 71 | 28.7% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2024-2025 has 156 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2024-2025 has 13 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2025-2026 has 91 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2025-2026 has 14 teams, expected 20 |
| 5 | GOALLESS_SHARE_OUTLIER | Season 2025-2026 goalless share 11.0% vs overall 8.5% (deviation 2.5 pp) |
| 6 | OUTCOME_SHARE_OUTLIER | Season 2025-2026 draw outcome share 31.9% vs overall 27.1% |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (10 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=7, fgte=7 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2024-2025/classic rows=13 positions=1..13 teams=13 |
| 10 | STANDINGS_INCOMPLETE | Standings 2024-2025/goals rows=13 positions=1..13 teams=13 |
| 11 | STANDINGS_INCOMPLETE | Standings 2024-2025/luck rows=13 positions=1..13 teams=13 |
| 12 | STANDINGS_INCOMPLETE | Standings 2025-2026/classic rows=14 positions=1..14 teams=14 |
| 13 | STANDINGS_INCOMPLETE | Standings 2025-2026/goals rows=14 positions=1..14 teams=14 |
| 14 | STANDINGS_INCOMPLETE | Standings 2025-2026/luck rows=14 positions=1..14 teams=14 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_matches": 156, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2024-2025", "n_teams": 13, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_matches": 91, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025-2026", "n_teams": 14, "expected": 20}`
- `5.` `GOALLESS_SHARE_OUTLIER` details: `{"season": "2025-2026", "season_goalless_pct": 11.0, "overall_goalless_pct": 8.5, "deviation_pp": 2.5}`
- `6.` `OUTCOME_SHARE_OUTLIER` details: `{"season": "2025-2026", "outcome": "draw", "season_share": 31.9, "overall_share": 27.1}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 13535, "distinct": 13525, "duplicates": 10}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 13535, "fgt_inconsistent": 7, "fgte_inconsistent": 7, "n_with_fgt": 12636}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "classic", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "goals", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2024-2025", "view": "luck", "n_rows": 13, "min_pos": 1, "max_pos": 13, "distinct_teams": 13}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "classic", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "goals", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2025-2026", "view": "luck", "n_rows": 14, "min_pos": 1, "max_pos": 14, "distinct_teams": 14}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
