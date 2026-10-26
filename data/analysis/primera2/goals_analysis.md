# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-26T01:44:20+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 228 | 11.5% |
| 1 | 452 | 22.8% |
| 2 | 491 | 24.7% |
| 3 | 400 | 20.2% |
| 4 | 228 | 11.5% |
| 5 | 123 | 6.2% |
| 6 | 41 | 2.1% |
| 7 | 16 | 0.8% |
| 8 | 5 | 0.3% |
| 9 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2021-2022 | 380 | 916 | 1.439 | 0.971 | 2.411 |
| 2022-2023 | 380 | 809 | 1.216 | 0.913 | 2.129 |
| 2023-2024 | 380 | 862 | 1.324 | 0.945 | 2.268 |
| 2024-2025 | 380 | 903 | 1.337 | 1.039 | 2.376 |
| 2025-2026 | 380 | 856 | 1.316 | 0.937 | 2.253 |
| 2026-2027 | 85 | 222 | 1.553 | 1.059 | 2.612 |

## 3. Home vs away goal share
- Home goals: **2652** (58.1%)
- Away goals: **1916** (41.9%)
- Home/away ratio: **1.384**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2021-2022 | 547 | 369 | 916 | 59.7% | 40.3% |
| 2022-2023 | 462 | 347 | 809 | 57.1% | 42.9% |
| 2023-2024 | 503 | 359 | 862 | 58.4% | 41.6% |
| 2024-2025 | 508 | 395 | 903 | 56.3% | 43.7% |
| 2025-2026 | 500 | 356 | 856 | 58.4% | 41.6% |
| 2026-2027 | 132 | 90 | 222 | 59.5% | 40.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **911** of `1985` (45.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2021-2022 | 380 | 167 | 43.9% |
| 2022-2023 | 380 | 172 | 45.3% |
| 2023-2024 | 380 | 162 | 42.6% |
| 2024-2025 | 380 | 199 | 52.4% |
| 2025-2026 | 380 | 167 | 43.9% |
| 2026-2027 | 85 | 44 | 51.8% |

## 5. Clean sheets
- Home clean sheets: **780** (39.3%)
- Away clean sheets: **522** (26.3%)
- Total clean sheets recorded: **1302**
- Matches with at least one clean sheet: **1074** (54.1%)
- Both teams kept clean sheets (0-0): **228**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2021-2022 | 380 | 157 | 93 | 250 | 213 (56.1%) |
| 2022-2023 | 380 | 155 | 106 | 261 | 208 (54.7%) |
| 2023-2024 | 380 | 152 | 109 | 261 | 218 (57.4%) |
| 2024-2025 | 380 | 128 | 96 | 224 | 181 (47.6%) |
| 2025-2026 | 380 | 156 | 103 | 259 | 213 (56.1%) |
| 2026-2027 | 85 | 32 | 15 | 47 | 41 (48.2%) |

## 6. Scoring intensity
- First-half goals: **1993** (43.6%)
- Second-half goals: **2575** (56.4%)
- Avg first-half goals per match: **1.004**
- Avg second-half goals per match: **1.297**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **515** (25.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2021-2022 | 380 | 409 | 507 | 44.7% | 55.3% |
| 2022-2023 | 380 | 350 | 459 | 43.3% | 56.7% |
| 2023-2024 | 380 | 373 | 489 | 43.3% | 56.7% |
| 2024-2025 | 380 | 367 | 536 | 40.6% | 59.4% |
| 2025-2026 | 380 | 398 | 458 | 46.5% | 53.5% |
| 2026-2027 | 85 | 96 | 126 | 43.2% | 56.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1757` of `1985` (88.5%)
- Goalless matches: `228`
- Min `1` | Max `99` | Mean `33.88` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 521 | 26.2% | 29.7% |
| 16-30 | 396 | 19.9% | 22.5% |
| 31-45 | 302 | 15.2% | 17.2% |
| 46-60 | 257 | 12.9% | 14.6% |
| 61-75 | 153 | 7.7% | 8.7% |
| 76-90 | 92 | 4.6% | 5.2% |
| 91-120 | 36 | 1.8% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

