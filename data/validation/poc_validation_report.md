# Football Charts Raw Data — POC Validation Report

- Generated: 2026-09-22T13:14:30
- Scope: league `japan1`; seasons 2020-2021, 2021-2022, 2022-2023, 2023-2024, 2024-2025, 2025-2026; table views classic, luck, goals
- Overall: **144 errors**, **1 warnings**

## Findings

| # | Severity | Code | Category | Season | File | Message |
|---|----------|------|----------|--------|------|---------|
| 1 | ERROR | `FILE_MISSING` | file_completeness | 2020-2021 | japan1/2020-2021/teams.json | Expected file is missing: teams.json |
| 2 | ERROR | `FILE_MISSING` | file_completeness | 2020-2021 | japan1/2020-2021/results.json | Expected file is missing: results.json |
| 3 | ERROR | `FILE_MISSING` | file_completeness | 2020-2021 | japan1/2020-2021/table_classic.json | Expected file is missing: table_classic.json |
| 4 | ERROR | `FILE_MISSING` | file_completeness | 2020-2021 | japan1/2020-2021/table_luck.json | Expected file is missing: table_luck.json |
| 5 | ERROR | `FILE_MISSING` | file_completeness | 2020-2021 | japan1/2020-2021/table_goals.json | Expected file is missing: table_goals.json |
| 6 | ERROR | `FILE_MISSING` | file_completeness | 2021-2022 | japan1/2021-2022/teams.json | Expected file is missing: teams.json |
| 7 | ERROR | `FILE_MISSING` | file_completeness | 2021-2022 | japan1/2021-2022/results.json | Expected file is missing: results.json |
| 8 | ERROR | `FILE_MISSING` | file_completeness | 2021-2022 | japan1/2021-2022/table_classic.json | Expected file is missing: table_classic.json |
| 9 | ERROR | `FILE_MISSING` | file_completeness | 2021-2022 | japan1/2021-2022/table_luck.json | Expected file is missing: table_luck.json |
| 10 | ERROR | `FILE_MISSING` | file_completeness | 2021-2022 | japan1/2021-2022/table_goals.json | Expected file is missing: table_goals.json |
| 11 | ERROR | `FILE_MISSING` | file_completeness | 2022-2023 | japan1/2022-2023/teams.json | Expected file is missing: teams.json |
| 12 | ERROR | `FILE_MISSING` | file_completeness | 2022-2023 | japan1/2022-2023/results.json | Expected file is missing: results.json |
| 13 | ERROR | `FILE_MISSING` | file_completeness | 2022-2023 | japan1/2022-2023/table_classic.json | Expected file is missing: table_classic.json |
| 14 | ERROR | `FILE_MISSING` | file_completeness | 2022-2023 | japan1/2022-2023/table_luck.json | Expected file is missing: table_luck.json |
| 15 | ERROR | `FILE_MISSING` | file_completeness | 2022-2023 | japan1/2022-2023/table_goals.json | Expected file is missing: table_goals.json |
| 16 | ERROR | `FILE_MISSING` | file_completeness | 2023-2024 | japan1/2023-2024/teams.json | Expected file is missing: teams.json |
| 17 | ERROR | `FILE_MISSING` | file_completeness | 2023-2024 | japan1/2023-2024/results.json | Expected file is missing: results.json |
| 18 | ERROR | `FILE_MISSING` | file_completeness | 2023-2024 | japan1/2023-2024/table_classic.json | Expected file is missing: table_classic.json |
| 19 | ERROR | `FILE_MISSING` | file_completeness | 2023-2024 | japan1/2023-2024/table_luck.json | Expected file is missing: table_luck.json |
| 20 | ERROR | `FILE_MISSING` | file_completeness | 2023-2024 | japan1/2023-2024/table_goals.json | Expected file is missing: table_goals.json |
| 21 | ERROR | `FILE_MISSING` | file_completeness | 2024-2025 | japan1/2024-2025/teams.json | Expected file is missing: teams.json |
| 22 | ERROR | `FILE_MISSING` | file_completeness | 2024-2025 | japan1/2024-2025/results.json | Expected file is missing: results.json |
| 23 | ERROR | `FILE_MISSING` | file_completeness | 2024-2025 | japan1/2024-2025/table_classic.json | Expected file is missing: table_classic.json |
| 24 | ERROR | `FILE_MISSING` | file_completeness | 2024-2025 | japan1/2024-2025/table_luck.json | Expected file is missing: table_luck.json |
| 25 | ERROR | `FILE_MISSING` | file_completeness | 2024-2025 | japan1/2024-2025/table_goals.json | Expected file is missing: table_goals.json |
| 26 | ERROR | `FILE_MISSING` | file_completeness | 2025-2026 | japan1/2025-2026/teams.json | Expected file is missing: teams.json |
| 27 | ERROR | `FILE_MISSING` | file_completeness | 2025-2026 | japan1/2025-2026/results.json | Expected file is missing: results.json |
| 28 | ERROR | `FILE_MISSING` | file_completeness | 2025-2026 | japan1/2025-2026/table_classic.json | Expected file is missing: table_classic.json |
| 29 | ERROR | `FILE_MISSING` | file_completeness | 2025-2026 | japan1/2025-2026/table_luck.json | Expected file is missing: table_luck.json |
| 30 | ERROR | `FILE_MISSING` | file_completeness | 2025-2026 | japan1/2025-2026/table_goals.json | Expected file is missing: table_goals.json |
| 31 | WARNING | `SEASON_NOT_DECLARED` | response_structure | - | japan1/leagues.json | Historical seasons are fetched directly but not declared by /leagues/ (expected API behaviour: current + previous only) |
| 32 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 33 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 34 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_classic.json' |
| 35 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_luck.json' |
| 36 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_goals.json' |
| 37 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 38 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 39 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_classic.json' |
| 40 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_luck.json' |
| 41 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_goals.json' |
| 42 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 43 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 44 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_classic.json' |
| 45 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_luck.json' |
| 46 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_goals.json' |
| 47 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 48 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 49 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_classic.json' |
| 50 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_luck.json' |
| 51 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_goals.json' |
| 52 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 53 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 54 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_classic.json' |
| 55 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_luck.json' |
| 56 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_goals.json' |
| 57 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 58 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |
| 59 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_classic.json' |
| 60 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_luck.json' |
| 61 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_goals.json' |
| 62 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 63 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 64 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 65 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 66 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 67 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 68 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 69 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 70 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 71 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 72 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 73 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |
| 74 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 75 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 76 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 77 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 78 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 79 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 80 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 81 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 82 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 83 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 84 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 85 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |
| 86 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 87 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 88 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 89 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 90 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 91 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |
| 92 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 93 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_classic.json' |
| 94 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_luck.json' |
| 95 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_goals.json' |
| 96 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 97 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_classic.json' |
| 98 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_luck.json' |
| 99 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_goals.json' |
| 100 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 101 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_classic.json' |
| 102 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_luck.json' |
| 103 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_goals.json' |
| 104 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 105 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_classic.json' |
| 106 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_luck.json' |
| 107 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_goals.json' |
| 108 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 109 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_classic.json' |
| 110 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_luck.json' |
| 111 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_goals.json' |
| 112 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 113 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_classic.json' |
| 114 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_luck.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_luck.json' |
| 115 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_goals.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_goals.json' |
| 116 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 117 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 118 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/table_classic.json' |
| 119 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 120 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 121 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/table_classic.json' |
| 122 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 123 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 124 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/table_classic.json' |
| 125 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 126 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 127 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/table_classic.json' |
| 128 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 129 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 130 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/table_classic.json' |
| 131 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 132 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |
| 133 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/table_classic.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/table_classic.json' |
| 134 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/teams.json' |
| 135 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2020-2021/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2020-2021/results.json' |
| 136 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/teams.json' |
| 137 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2021-2022/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2021-2022/results.json' |
| 138 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/teams.json' |
| 139 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2022-2023/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2022-2023/results.json' |
| 140 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/teams.json' |
| 141 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2023-2024/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2023-2024/results.json' |
| 142 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/teams.json' |
| 143 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2024-2025/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2024-2025/results.json' |
| 144 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/teams.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/teams.json' |
| 145 | ERROR | `FILE_UNREADABLE` | response_structure | - | japan1/2025-2026/results.json | File exists but is not valid JSON: [Errno 2] No such file or directory: '/mnt/e/football_data_analysis/data/raw/japan1/2025-2026/results.json' |

## Per-check summary

| Check | Status |
|-------|--------|
| response_structure | ERROR |
| file_completeness | ERROR |
| teams | PASS |
| results | PASS |
| team_references | PASS |
| match_identity | PASS |
| table | PASS |
| cross_endpoint | PASS |
| historical | PASS |

## Check details

### response_structure
**Status:** ERROR
**leagues:** `{"status": "WARNING", "declared_seasons": ["2026-2027", "2026"]}`
**seasonal:** `{"status": "ERROR"}`

### file_completeness
**Status:** ERROR
**expected_count:** `31`
**present_count:** `1`
**missing_files:** `["data/raw/japan1/2020-2021/teams.json", "data/raw/japan1/2020-2021/results.json", "data/raw/japan1/2020-2021/table_classic.json", "data/raw/japan1/2020-2021/table_luck.json", "data/raw/japan1/2020-2021/table_goals.json", "data/raw/japan1/2021-2022/teams.json", "data/raw/japan1/2021-2022/results.json", "data/raw/japan1/2021-2022/table_classic.json", "data/raw/japan1/2021-2022/table_luck.json", "data/raw/japan1/2021-2022/table_goals.json", "data/raw/japan1/2022-2023/teams.json", "data/raw/japan1/2022-2023/results.json", "data/raw/japan1/2022-2023/table_classic.json", "data/raw/japan1/2022-2023/table_luck.json", "data/raw/japan1/2022-2023/table_goals.json", "data/raw/japan1/2023-2024/teams.json", "data/raw/japan1/2023-2024/results.json", "data/raw/japan1/2023-2024/table_classic.json", "data/raw/japan1/2023-2024/table_luck.json", "data/raw/japan1/2023-2024/table_goals.json", "data/raw/japan1/2024-2025/teams.json", "data/raw/japan1/2024-2025/results.json", "data/raw/japan1/2024-2025/table_classic.json", "data/raw/japan1/2024-2025/table_luck.json", "data/raw/japan1/2024-2025/table_goals.json", "data/raw/japan1/2025-2026/teams.json", "data/raw/japan1/2025-2026/results.json", "data/raw/japan1/2025-2026/table_classic.json", "data/raw/japan1/2025-2026/table_luck.json", "data/raw/japan1/2025-2026/table_goals.json"]`

### teams
**Status:** PASS
**per_season:**
- `2020-2021`: {"teams": null}
- `2021-2022`: {"teams": null}
- `2022-2023`: {"teams": null}
- `2023-2024`: {"teams": null}
- `2024-2025`: {"teams": null}
- `2025-2026`: {"teams": null}
**field_sets:** `[]`

### results
**Status:** PASS
**per_season:**
- `2020-2021`: {"n_matches": null}
- `2021-2022`: {"n_matches": null}
- `2022-2023`: {"n_matches": null}
- `2023-2024`: {"n_matches": null}
- `2024-2025`: {"n_matches": null}
- `2025-2026`: {"n_matches": null}
**field_sets:** `[]`

### team_references
**Status:** PASS

### match_identity
**Status:** PASS
**per_season:**
- `2020-2021`: {"n_matches": null}
- `2021-2022`: {"n_matches": null}
- `2022-2023`: {"n_matches": null}
- `2023-2024`: {"n_matches": null}
- `2024-2025`: {"n_matches": null}
- `2025-2026`: {"n_matches": null}

### table
**Status:** PASS
**per_season:**
- `2020-2021`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}
- `2021-2022`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}
- `2022-2023`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}
- `2023-2024`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}
- `2024-2025`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}
- `2025-2026`: {"classic": {"rows": null, "view": "classic"}, "luck": {"rows": null, "view": "luck"}, "goals": {"rows": null, "view": "goals"}}

### cross_endpoint
**Status:** PASS

### historical
**Status:** PASS
**team_counts:**
```json
{}
```
**match_counts:**
```json
{}
```
**roster_churn:**
```json
{}
```
**recurring_issues:**
```json
[
  {
    "code": "FILE_UNREADABLE",
    "severity": "ERROR",
    "n": 114
  },
  {
    "code": "FILE_MISSING",
    "severity": "ERROR",
    "n": 30
  },
  {
    "code": "SEASON_NOT_DECLARED",
    "severity": "WARNING",
    "n": 1
  }
]
```

## Issues by season

| Season | Errors | Warnings |
|--------|--------|----------|
| 2020-2021 | 5 | 0 |
| 2021-2022 | 5 | 0 |
| 2022-2023 | 5 | 0 |
| 2023-2024 | 5 | 0 |
| 2024-2025 | 5 | 0 |
| 2025-2026 | 5 | 0 |

## Methodology

Reads the byte-preserved raw JSON files under `data/raw/` produced by `scripts/collect_raw_data.py`. Each league/season/endpoint is validated for file presence, top-level schema, required fields, value formats, uniqueness constraints, and cross-endpoint consistency. Findings are classified PASS / WARNING / ERROR; nothing is modified.