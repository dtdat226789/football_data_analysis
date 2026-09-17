# Football Charts Raw Data — POC Validation Report

- Generated: 2026-09-16T10:39:26
- Scope: league `premier`; seasons 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026; table views classic, luck, goals
- Overall: **0 errors**, **2 warnings**

## Findings

| # | Severity | Code | Category | Season | File | Message |
|---|----------|------|----------|--------|------|---------|
| 1 | WARNING | `SEASON_NOT_DECLARED` | response_structure | - | premier/leagues.json | Historical seasons are fetched directly but not declared by /leagues/ (expected API behaviour: current + previous only) |
| 2 | WARNING | `TABLE_ID_SEASON_SCOPED` | table | - | premier/2020-2021/table_classic.json | Table row 'id' is not a stable team identifier: only 0 of 120 distinct ids appear in every collected season |

## Per-check summary

| Check | Status |
|-------|--------|
| response_structure | WARNING |
| file_completeness | PASS |
| teams | PASS |
| results | PASS |
| team_references | PASS |
| match_identity | PASS |
| table | WARNING |
| cross_endpoint | PASS |
| historical | PASS |

## Check details

### response_structure
**Status:** WARNING
**leagues:** `{"status": "WARNING", "declared_seasons": ["2026-2027", "2025-2026"]}`
**seasonal:** `{"status": "WARNING"}`

### file_completeness
**Status:** PASS
**expected_count:** `31`
**present_count:** `31`
**missing_files:** `[]`

### teams
**Status:** PASS
**per_season:**
- `2020-2021`: {"teams": null, "n_teams": 20}
- `2021-2022`: {"teams": null, "n_teams": 20}
- `2022-2023`: {"teams": null, "n_teams": 20}
- `2023-2024`: {"teams": null, "n_teams": 20}
- `2024-2025`: {"teams": null, "n_teams": 20}
- `2025-2026`: {"teams": null, "n_teams": 20}
**field_sets:** `[["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"], ["logo_url", "played", "points", "position", "slug", "team"]]`

### results
**Status:** PASS
**per_season:**
- `2020-2021`: {"n_matches": 380}
- `2021-2022`: {"n_matches": 380}
- `2022-2023`: {"n_matches": 380}
- `2023-2024`: {"n_matches": 380}
- `2024-2025`: {"n_matches": 380}
- `2025-2026`: {"n_matches": 380}
**field_sets:** `[["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"], ["awayTeam", "date", "first_goal_time", "first_goal_time_extra", "game_index", "goalless", "homeTeam", "ht_result", "id", "score", "time"]]`

### team_references
**Status:** PASS

### match_identity
**Status:** PASS
**per_season:**
- `2020-2021`: {"n_matches": 380, "id_min": 161341, "id_max": 161720, "game_index_min": 1, "game_index_max": 380}
- `2021-2022`: {"n_matches": 380, "id_min": 160201, "id_max": 160580, "game_index_min": 1, "game_index_max": 380}
- `2022-2023`: {"n_matches": 380, "id_min": 160581, "id_max": 160960, "game_index_min": 1, "game_index_max": 380}
- `2023-2024`: {"n_matches": 380, "id_min": 160961, "id_max": 161340, "game_index_min": 1, "game_index_max": 380}
- `2024-2025`: {"n_matches": 380, "id_min": 161721, "id_max": 162100, "game_index_min": 1, "game_index_max": 380}
- `2025-2026`: {"n_matches": 380, "id_min": 160082, "id_max": 212123, "game_index_min": 1, "game_index_max": 380}

### table
**Status:** WARNING
**per_season:**
- `2020-2021`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}
- `2021-2022`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}
- `2022-2023`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}
- `2023-2024`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}
- `2024-2025`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}
- `2025-2026`: {"classic": {"rows": 20, "view": "classic"}, "luck": {"rows": 20, "view": "luck"}, "goals": {"rows": 20, "view": "goals"}}

### cross_endpoint
**Status:** PASS

### historical
**Status:** PASS
**team_counts:**
```json
{
  "2020-2021": 20,
  "2021-2022": 20,
  "2022-2023": 20,
  "2023-2024": 20,
  "2024-2025": 20,
  "2025-2026": 20
}
```
**match_counts:**
```json
{
  "2020-2021": 380,
  "2021-2022": 380,
  "2022-2023": 380,
  "2023-2024": 380,
  "2024-2025": 380,
  "2025-2026": 380
}
```
**roster_churn:**
```json
{
  "2021-2022": {
    "added": [
      "Brentford",
      "Norwich",
      "Watford"
    ],
    "removed": [
      "Fulham",
      "Sheffield Utd",
      "West Brom"
    ]
  },
  "2022-2023": {
    "added": [
      "Bournemouth",
      "Fulham",
      "Nottingham"
    ],
    "removed": [
      "Burnley",
      "Norwich",
      "Watford"
    ]
  },
  "2023-2024": {
    "added": [
      "Burnley",
      "Luton",
      "Sheffield Utd"
    ],
    "removed": [
      "Leeds",
      "Leicester",
      "Southampton"
    ]
  },
  "2024-2025": {
    "added": [
      "Ipswich",
      "Leicester",
      "Southampton"
    ],
    "removed": [
      "Burnley",
      "Luton",
      "Sheffield Utd"
    ]
  },
  "2025-2026": {
    "added": [
      "Burnley",
      "Leeds",
      "Sunderland"
    ],
    "removed": [
      "Ipswich",
      "Leicester",
      "Southampton"
    ]
  }
}
```
**recurring_issues:**
```json
[
  {
    "code": "SEASON_NOT_DECLARED",
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
| 2020-2021 | 0 | 0 |
| 2021-2022 | 0 | 0 |
| 2022-2023 | 0 | 0 |
| 2023-2024 | 0 | 0 |
| 2024-2025 | 0 | 0 |
| 2025-2026 | 0 | 0 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` produced by `scripts/collect_raw_data.py`. Each league/season/endpoint is validated for file presence, top-level schema, required fields, value formats, uniqueness constraints, and cross-endpoint consistency. Findings are classified PASS / WARNING / ERROR; nothing is modified.