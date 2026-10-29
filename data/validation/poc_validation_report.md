# Football Charts Raw Data — POC Validation Report

- Generated: 2026-10-29T01:52:39+00:00
- Scope: league `wsweden`; seasons 2020, 2021, 2022, 2023, 2024, 2025, 2026; table views classic, luck, goals
- Overall: **0 errors**, **16 warnings**

## Findings

| # | Severity | Code | Category | Season | File | Message |
|---|----------|------|----------|--------|------|---------|
| 1 | WARNING | `SEASON_NOT_DECLARED` | response_structure | - | wsweden/leagues.json | Historical seasons are fetched directly but not declared by /leagues/ (expected API behaviour: current + previous only) |
| 2 | WARNING | `TEAMS_COUNT` | teams | 2020 | wsweden/2020/teams.json | Team count is 12, expected 14 |
| 3 | WARNING | `TEAMS_COUNT` | teams | 2021 | wsweden/2021/teams.json | Team count is 12, expected 14 |
| 4 | WARNING | `RESULTS_COUNT_UNEXPECTED` | results | 2020 | wsweden/2020/results.json | Match count is 132, expected 182 for a complete 14-team round-robin season |
| 5 | WARNING | `RESULTS_COUNT_UNEXPECTED` | results | 2021 | wsweden/2021/results.json | Match count is 132, expected 182 for a complete 14-team round-robin season |
| 6 | WARNING | `RESULTS_COUNT_UNEXPECTED` | results | 2026 | wsweden/2026/results.json | Match count is 161, expected 182 for a complete 14-team round-robin season |
| 7 | WARNING | `RESULTS_NOT_CHRONOLOGICAL` | results | 2026 | wsweden/2026/results.json | Matches are not in chronological date order |
| 8 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2020 | wsweden/2020/table_classic.json | table_classic has 12 rows, expected 14 |
| 9 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2020 | wsweden/2020/table_luck.json | table_luck has 12 rows, expected 14 |
| 10 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2020 | wsweden/2020/table_goals.json | table_goals has 12 rows, expected 14 |
| 11 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2021 | wsweden/2021/table_classic.json | table_classic has 12 rows, expected 14 |
| 12 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2021 | wsweden/2021/table_luck.json | table_luck has 12 rows, expected 14 |
| 13 | WARNING | `TABLE_ROWS_UNEXPECTED` | table | 2021 | wsweden/2021/table_goals.json | table_goals has 12 rows, expected 14 |
| 14 | WARNING | `TABLE_ID_SEASON_SCOPED` | table | - | wsweden/2020/table_classic.json | Table row 'id' is not a stable team identifier: only 0 of 94 distinct ids appear in every collected season |
| 15 | WARNING | `TEAM_COUNT_CHANGE` | historical | - |  | Team count varies across seasons |
| 16 | WARNING | `MATCH_COUNT_CHANGE` | historical | - |  | Match count varies across seasons |

## Per-check summary

| Check | Status |
|-------|--------|
| response_structure | WARNING |
| file_completeness | PASS |
| teams | WARNING |
| results | WARNING |
| team_references | PASS |
| match_identity | PASS |
| table | WARNING |
| cross_endpoint | PASS |
| historical | WARNING |

## Check details

### response_structure
**Status:** WARNING
**leagues:** `{"status": "WARNING", "declared_seasons": ["2026", "2025"]}`
**seasonal:** `{"status": "WARNING"}`

### file_completeness
**Status:** PASS
**expected_count:** `36`
**present_count:** `36`
**missing_files:** `[]`

### teams
**Status:** WARNING
**per_season:**
- `2020`: {"teams": null, "n_teams": 12}
- `2021`: {"teams": null, "n_teams": 12}
- `2022`: {"teams": null, "n_teams": 14}
- `2023`: {"teams": null, "n_teams": 14}
- `2024`: {"teams": null, "n_teams": 14}
- `2025`: {"teams": null, "n_teams": 14}
- `2026`: {"teams": null, "n_teams": 14}
**field_sets:** `[["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"]]`

### results
**Status:** WARNING
**per_season:**
- `2020`: {"n_matches": 132}
- `2021`: {"n_matches": 132}
- `2022`: {"n_matches": 182}
- `2023`: {"n_matches": 182}
- `2024`: {"n_matches": 182}
- `2025`: {"n_matches": 182}
- `2026`: {"n_matches": 161}
**field_sets:** `[["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "kickoff_utc", "score", "stats", "time"]]`

### team_references
**Status:** PASS

### match_identity
**Status:** PASS
**per_season:**
- `2020`: {"n_matches": 132, "id_min": 62255, "id_max": 62386, "game_index_min": 1, "game_index_max": 132}
- `2021`: {"n_matches": 132, "id_min": 62123, "id_max": 62254, "game_index_min": 1, "game_index_max": 132}
- `2022`: {"n_matches": 182, "id_min": 61395, "id_max": 61576, "game_index_min": 1, "game_index_max": 182}
- `2023`: {"n_matches": 182, "id_min": 61941, "id_max": 62122, "game_index_min": 1, "game_index_max": 182}
- `2024`: {"n_matches": 182, "id_min": 61759, "id_max": 61940, "game_index_min": 1, "game_index_max": 182}
- `2025`: {"n_matches": 182, "id_min": 61577, "id_max": 61758, "game_index_min": 1, "game_index_max": 182}
- `2026`: {"n_matches": 161, "id_min": 210593, "id_max": 235602, "game_index_min": 1, "game_index_max": 161}

### table
**Status:** WARNING
**per_season:**
- `2020`: {"classic": {"rows": 12, "view": "classic"}, "luck": {"rows": 12, "view": "luck"}, "goals": {"rows": 12, "view": "goals"}}
- `2021`: {"classic": {"rows": 12, "view": "classic"}, "luck": {"rows": 12, "view": "luck"}, "goals": {"rows": 12, "view": "goals"}}
- `2022`: {"classic": {"rows": 14, "view": "classic"}, "luck": {"rows": 14, "view": "luck"}, "goals": {"rows": 14, "view": "goals"}}
- `2023`: {"classic": {"rows": 14, "view": "classic"}, "luck": {"rows": 14, "view": "luck"}, "goals": {"rows": 14, "view": "goals"}}
- `2024`: {"classic": {"rows": 14, "view": "classic"}, "luck": {"rows": 14, "view": "luck"}, "goals": {"rows": 14, "view": "goals"}}
- `2025`: {"classic": {"rows": 14, "view": "classic"}, "luck": {"rows": 14, "view": "luck"}, "goals": {"rows": 14, "view": "goals"}}
- `2026`: {"classic": {"rows": 14, "view": "classic"}, "luck": {"rows": 14, "view": "luck"}, "goals": {"rows": 14, "view": "goals"}}

### cross_endpoint
**Status:** PASS

### historical
**Status:** WARNING
**team_counts:**
```json
{
  "2020": 12,
  "2021": 12,
  "2022": 14,
  "2023": 14,
  "2024": 14,
  "2025": 14,
  "2026": 14
}
```
**match_counts:**
```json
{
  "2020": 132,
  "2021": 132,
  "2022": 182,
  "2023": 182,
  "2024": 182,
  "2025": 182,
  "2026": 161
}
```
**roster_churn:**
```json
{
  "2021": {
    "added": [
      "AIK W",
      "Hacken W",
      "Hammarby W"
    ],
    "removed": [
      "Goteborg W",
      "Umea W",
      "Uppsala W"
    ]
  },
  "2022": {
    "added": [
      "IF Brommapojkarna W",
      "Kalmar W",
      "Umea W"
    ],
    "removed": [
      "Vaxjo DFF W"
    ]
  },
  "2023": {
    "added": [
      "Norrkoping W",
      "Uppsala W",
      "Vaxjo DFF W"
    ],
    "removed": [
      "AIK W",
      "Eskilstuna Utd W",
      "Umea W"
    ]
  },
  "2024": {
    "added": [
      "AIK W",
      "Trelleborg W"
    ],
    "removed": [
      "Kalmar W",
      "Uppsala W"
    ]
  },
  "2025": {
    "added": [
      "Alingsas W",
      "Malmo FF W"
    ],
    "removed": [
      "KIF Orebro W",
      "Trelleborg W"
    ]
  },
  "2026": {
    "added": [
      "Eskilstuna Utd W",
      "Uppsala W"
    ],
    "removed": [
      "Alingsas W",
      "Linkoping W"
    ]
  }
}
```
**recurring_issues:**
```json
[
  {
    "code": "TABLE_ROWS_UNEXPECTED",
    "severity": "WARNING",
    "n": 6
  },
  {
    "code": "RESULTS_COUNT_UNEXPECTED",
    "severity": "WARNING",
    "n": 3
  },
  {
    "code": "TEAMS_COUNT",
    "severity": "WARNING",
    "n": 2
  },
  {
    "code": "SEASON_NOT_DECLARED",
    "severity": "WARNING",
    "n": 1
  },
  {
    "code": "RESULTS_NOT_CHRONOLOGICAL",
    "severity": "WARNING",
    "n": 1
  },
  {
    "code": "TABLE_ID_SEASON_SCOPED",
    "severity": "WARNING",
    "n": 1
  }
]
```

## Issues by season

| Season | Errors | Warnings |
|--------|--------|----------|
| 2020 | 0 | 5 |
| 2021 | 0 | 5 |
| 2022 | 0 | 0 |
| 2023 | 0 | 0 |
| 2024 | 0 | 0 |
| 2025 | 0 | 0 |
| 2026 | 0 | 2 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` produced by `scripts/collect_raw_data.py`. Each league/season/endpoint is validated for file presence, top-level schema, required fields, value formats, uniqueness constraints, and cross-endpoint consistency. Findings are classified PASS / WARNING / ERROR; nothing is modified.