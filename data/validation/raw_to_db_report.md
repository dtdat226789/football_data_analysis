# Football Charts — Raw-to-Database Reconciliation Report

- Generated: 2026-09-23T20:51:24
- Scope: league `wsweden`; seasons 2025, 2026; table views classic, luck, goals
- Overall: **0 errors**, **0 warnings** | compared=registry=4, identity=28, matches=315, standings=84

## Findings

| # | Severity | Code | Category | Season | Message |
|---|----------|------|----------|--------|---------|

## Per-check summary

| Check | Status | Compared |
|-------|--------|----------|
| registry | PASS | 4 |
| identity | PASS | 28 |
| matches | PASS | 315 |
| standings | PASS | 84 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` and compares them field-by-field against the rows the ETL pipeline loaded into PostgreSQL. Read-only (transaction is rolled back). Any value that differs between the raw source of truth and the loaded row is reported as an ERROR. Logo drift is reported as a WARNING.