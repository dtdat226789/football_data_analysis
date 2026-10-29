# Football Charts — Raw-to-Database Reconciliation Report

- Generated: 2026-10-29T16:26:05+00:00
- Scope: league `premier`; seasons 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026, 2026-2027; table views classic, luck, goals
- Overall: **0 errors**, **0 warnings** | compared=registry=14, identity=140, matches=2360, standings=420

## Findings

| # | Severity | Code | Category | Season | Message |
|---|----------|------|----------|--------|---------|

## Per-check summary

| Check | Status | Compared |
|-------|--------|----------|
| registry | PASS | 14 |
| identity | PASS | 140 |
| matches | PASS | 2360 |
| standings | PASS | 420 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` and compares them field-by-field against the rows the ETL pipeline loaded into PostgreSQL. Read-only (transaction is rolled back). Any value that differs between the raw source of truth and the loaded row is reported as an ERROR. Logo drift and raw rows etl_03 skipped for a team-membership gap are reported as WARNINGs.
Phantom roster rows (teams.json entries that never play a match in results.json and that etl_02 therefore skipped) surface as PHANTOM_TEAM_IN_RAW WARNINGs, and their table rows as TEAM_MEMBERSHIP_MISSING WARNINGs.