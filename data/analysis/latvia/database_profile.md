# Football Charts Database Profile
- Report: `database_profile`
- Generated: 2026-09-29T16:01:08+00:00
- Script: `backend/scripts/profile_database.py` v1.0.0
- Database: `football_charts` (PostgreSQL 18.6 (Ubuntu 18.6-0ubuntu0.26.04.1))
- Scope: league `latvia`

## 1. Observed data

### 1.1 Table row counts
| table | rows |
|---|---|
| leagues | 93 |
| seasons | 6 |
| league_seasons | 103 |
| teams | 1069 |
| team_aliases | 2138 |
| team_seasons | 1849 |
| matches | 18820 |
| standings | 5373 |

### 1.2 Leagues with data
- Catalog leagues: `93`
- Leagues with match data: `50`
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
| greece1 | Super League | Greece | 2 | 281 |
| greece2 | Super League 2 | Greece | 2 | 297 |
| holland1 | Eredivisie | Netherlands | 2 | 384 |
| holland2 | Eerste Divisie | Netherlands | 2 | 474 |
| holland3 | Tweede Divisie | Netherlands | 2 | 385 |
| hungary1 | NB I. | Hungary | 2 | 245 |
| hungary2 | NB II. | Hungary | 2 | 301 |
| india1 | ISL | India | 2 | 247 |
| ireland1 | Premier Division | Ireland | 2 | 339 |
| ireland2 | Division 1 | Ireland | 2 | 344 |
| italy1 | Serie A | Italy | 2 | 430 |
| italy19 | Primavera 1 | Italy | 2 | 432 |
| italy2 | Serie B | Italy | 2 | 440 |
| italy3a | Serie C - Group A | Italy | 2 | 450 |
| italy3b | Serie C - Group B | Italy | 2 | 426 |
| japan1 | J1 League | Japan | 2 | 241 |
| japan2 | J2 League | Japan | 2 | 760 |
| korea1 | K League 1 | South Korea | 2 | 378 |
| korea2 | K League 2 | South Korea | 2 | 493 |
| kuwait | Premier League | Kuwait | 2 | 116 |
| latvia | Virsliga | Latvia | 2 | 336 |

### 1.3 Registered seasons vs seasons with data
- Registered league_seasons for `latvia`: `2`
- With match data: `2`
- Registered but no data: `none`

| season | declared_by_api | state | matches | teams | first match | last match |
|---|---|---|---|---|---|---|
| 2025 | True | complete | 182 | 11 | 2025-03-05 | 2025-11-23 |
| 2026 | True | in_progress | 154 | 10 | 2026-03-06 | 2026-09-20 |

### 1.4 Duplicate checks
| check | rows | distinct | duplicates |
|---|---|---|---|
| matches.api_id (natural PK) | 18820 | 18820 | 0 |
| matches (league_season_id, game_index) | 18820 | 18820 | 0 |
| matches same fixture on same date (league_season, home, away, match_date) | 18820 | 18806 | 14 |
| team_seasons (league_season_id, team_id) | 1849 | 1849 | 0 |
| team_seasons api_name within a season | 1849 | 1849 | 0 |
| team_seasons api_slug within a season | 1849 | 1849 | 0 |
| standings (league_season_id, team_id, view) | 5373 | 5373 | 0 |
| team_aliases (form, value) | 2138 | 2138 | 0 |
| leagues.api_key | 93 | 93 | 0 |
| seasons.name | 6 | 6 | 0 |
| teams.canonical_name | 1069 | 1069 | 0 |
  > **WARNING:** duplicates found, see section 3.

### 1.5 NULL counts (matches, important fields)
- Total matches: `18820`

| field | n_null | n_not_null | null_pct |
|---|---|---|---|
| match_date | 0 | 18820 | 0.0% |
| kickoff_time | 0 | 18820 | 0.0% |
| home_team_id | 0 | 18820 | 0.0% |
| away_team_id | 0 | 18820 | 0.0% |
| home_score | 0 | 18820 | 0.0% |
| away_score | 0 | 18820 | 0.0% |
| home_ht | 39 | 18781 | 0.2% |
| away_ht | 39 | 18781 | 0.2% |
| first_goal_time | 1337 | 17483 | 7.1% |
| first_goal_time_extra | 1337 | 17483 | 7.1% |
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
| Home | 147 | 43.8% |
| Draw | 80 | 23.8% |
| Away | 109 | 32.4% |
| Total | 336 | 100.0% |

### 2.2 Goals
| metric | value |
|---|---|
| Total goals | 973 |
| Average goals per match | 2.896 |
| Home goals | 548 (avg 1.631) |
| Away goals | 425 (avg 1.265) |
| Home goal share | 56.3% |
| Goalless matches | 19 (5.7%) |

### 2.3 Per-season breakdown
| season | matches | H% | D% | A% | total goals | avg goals | home goals | away goals | goalless |
|---|---|---|---|---|---|---|---|---|---|
| 2025 | 182 | 45.6% | 23.6% | 30.8% | 535 | 2.94 | 302 | 233 | 11 (6.0%) |
| 2026 | 154 | 41.6% | 24.0% | 34.4% | 438 | 2.844 | 246 | 192 | 8 (5.2%) |

### 2.4 First-goal timing
- Matches with a recorded first-goal time: `317` of `336` (94.3%)
| metric | value |
|---|---|
| First goals recorded | 317 |
| Min minute | 1 |
| Max minute | 97 |
| Mean minute | 30.7 |
| Median (p50) | 26.0 |
| p25 | 12.0 |
| p75 | 46.0 |

First-goal minute buckets (count):
| bucket | count |
|---|---|
| 1-15 | 104 |
| 16-30 | 85 |
| 31-45 | 45 |
| 46-60 | 43 |
| 61-75 | 17 |
| 76-90 | 19 |
| 91-120 | 4 |

### 2.5 Standings coverage
- (season, view) pairs present: `6` of `6` expected
- Standings rows total: `63`
- Coverage complete: `True`

| season | view | rows | positions | distinct teams |
|---|---|---|---|---|
| 2025 | classic | 11 | 1..11 | 11 |
| 2025 | goals | 11 | 1..11 | 11 |
| 2025 | luck | 11 | 1..11 | 11 |
| 2026 | classic | 10 | 1..10 | 10 |
| 2026 | goals | 10 | 1..10 | 10 |
| 2026 | luck | 10 | 1..10 | 10 |

### 2.6 Scorelines
Most common full-time scorelines:
| scoreline | count |
|---|---|
| 1-1 | 40 |
| 0-1 | 36 |
| 1-0 | 28 |
| 2-0 | 27 |
| 2-1 | 23 |
| 1-2 | 22 |
| 0-0 | 19 |
| 2-2 | 17 |
| 3-1 | 12 |
| 4-1 | 12 |
| 3-0 | 11 |
| 3-2 | 11 |

Extreme scorelines (>= 8 total goals):
| scoreline | total goals | count |
|---|---|---|
| 6-2 | 8 | 1 |
| 2-6 | 8 | 1 |
| 1-7 | 8 | 1 |
| 0-8 | 8 | 1 |

### 2.7 Match weekday distribution
| weekday | count | pct |
|---|---|---|
| Sun | 89 | 26.5% |
| Mon | 35 | 10.4% |
| Tue | 31 | 9.2% |
| Wed | 28 | 8.3% |
| Thu | 27 | 8.0% |
| Fri | 49 | 14.6% |
| Sat | 77 | 22.9% |

## 3. Warnings & anomalies
| # | code | message |
|---|---|---|
| 1 | MATCH_COUNT_UNEXPECTED | Season 2025 has 182 matches, expected 380 |
| 2 | TEAM_COUNT_UNEXPECTED | Season 2025 has 11 teams, expected 20 |
| 3 | MATCH_COUNT_UNEXPECTED | Season 2026 has 154 matches, expected 380 |
| 4 | TEAM_COUNT_UNEXPECTED | Season 2026 has 10 teams, expected 20 |
| 5 | SEASON_STATE_NOT_COMPLETE | Season 2026 has data but state is 'in_progress' |
| 6 | HIGH_SCORING_MATCHES | 4 match(es) with >= 8 total goals (extreme scorelines) |
| 7 | DUPLICATE_ROWS | Duplicate rows detected in matches same fixture on same date (league_season, home, away, match_date) (14 extra rows) |
| 8 | FIRST_GOAL_NULL_INCONSISTENCY | first_goal_time/first_goal_time_extra NULL semantics broken (fgt=17, fgte=17 rows) |
| 9 | STANDINGS_INCOMPLETE | Standings 2025/classic rows=11 positions=1..11 teams=11 |
| 10 | STANDINGS_INCOMPLETE | Standings 2025/goals rows=11 positions=1..11 teams=11 |
| 11 | STANDINGS_INCOMPLETE | Standings 2025/luck rows=11 positions=1..11 teams=11 |
| 12 | STANDINGS_INCOMPLETE | Standings 2026/classic rows=10 positions=1..10 teams=10 |
| 13 | STANDINGS_INCOMPLETE | Standings 2026/goals rows=10 positions=1..10 teams=10 |
| 14 | STANDINGS_INCOMPLETE | Standings 2026/luck rows=10 positions=1..10 teams=10 |
- `1.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2025", "n_matches": 182, "expected": 380}`
- `2.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2025", "n_teams": 11, "expected": 20}`
- `3.` `MATCH_COUNT_UNEXPECTED` details: `{"season": "2026", "n_matches": 154, "expected": 380}`
- `4.` `TEAM_COUNT_UNEXPECTED` details: `{"season": "2026", "n_teams": 10, "expected": 20}`
- `5.` `SEASON_STATE_NOT_COMPLETE` details: `{"season": "2026", "season_state": "in_progress"}`
- `6.` `HIGH_SCORING_MATCHES` details: `{"n_matches": 4, "threshold": 8, "examples": [{"scoreline": "6-2", "total_goals": 8, "count": 1}, {"scoreline": "2-6", "total_goals": 8, "count": 1}, {"scoreline": "1-7", "total_goals": 8, "count": 1}, {"scoreline": "0-8", "total_goals": 8, "count": 1}]}`
- `7.` `DUPLICATE_ROWS` details: `{"check": "matches same fixture on same date (league_season, home, away, match_date)", "rows": 18820, "distinct": 18806, "duplicates": 14}`
- `8.` `FIRST_GOAL_NULL_INCONSISTENCY` details: `{"total": 18820, "fgt_inconsistent": 17, "fgte_inconsistent": 17, "n_with_fgt": 17483}`
- `9.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "classic", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `10.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "goals", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `11.` `STANDINGS_INCOMPLETE` details: `{"season": "2025", "view": "luck", "n_rows": 11, "min_pos": 1, "max_pos": 11, "distinct_teams": 11}`
- `12.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "classic", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `13.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "goals", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`
- `14.` `STANDINGS_INCOMPLETE` details: `{"season": "2026", "view": "luck", "n_rows": 10, "min_pos": 1, "max_pos": 10, "distinct_teams": 10}`

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/profile_database.py` to regenerate.*
