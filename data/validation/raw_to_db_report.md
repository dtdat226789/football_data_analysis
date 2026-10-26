# Football Charts — Raw-to-Database Reconciliation Report

- Generated: 2026-10-26T01:53:26+00:00
- Scope: league `wsweden`; seasons 2020, 2021, 2022, 2023, 2024, 2025, 2026; table views classic, luck, goals
- Overall: **0 errors**, **0 warnings** | compared=registry=14, identity=94, matches=1151, standings=282

## Findings

| # | Severity | Code | Category | Season | Message |
|---|----------|------|----------|--------|---------|

## Per-check summary

| Check | Status | Compared |
|-------|--------|----------|
| registry | PASS | 14 |
| identity | PASS | 94 |
| matches | PASS | 1151 |
| standings | PASS | 282 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` and compares them field-by-field against the rows the ETL pipeline loaded into PostgreSQL. Read-only (transaction is rolled back). Any value that differs between the raw source of truth and the loaded row is reported as an ERROR. Logo drift and raw rows etl_03 skipped for a team-membership gap are reported as WARNINGs.
Phantom roster rows (teams.json entries that never play a match in results.json and that etl_02 therefore skipped) surface as PHANTOM_TEAM_IN_RAW WARNINGs, and their table rows as TEAM_MEMBERSHIP_MISSING WARNINGs.