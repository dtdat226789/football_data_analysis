# Football Charts — Raw-to-Database Reconciliation Report

- Generated: 2026-09-19T08:53:48
- Scope: league `premier`; seasons 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026; table views classic, luck, goals
- Overall: **0 errors**, **0 warnings** | compared=registry=13, identity=120, matches=2280, standings=360

## Findings

| # | Severity | Code | Category | Season | Message |
|---|----------|------|----------|--------|---------|

## Per-check summary

| Check | Status | Compared |
|-------|--------|----------|
| registry | PASS | 13 |
| identity | PASS | 120 |
| matches | PASS | 2280 |
| standings | PASS | 360 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` and compares them field-by-field against the rows the ETL pipeline loaded into PostgreSQL. Read-only (transaction is rolled back). Any value that differs between the raw source of truth and the loaded row is reported as an ERROR. Logo drift is reported as a WARNING.