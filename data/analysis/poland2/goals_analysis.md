# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-30T04:04:30+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 146 | 7.4% |
| 1 | 353 | 18.0% |
| 2 | 482 | 24.5% |
| 3 | 450 | 22.9% |
| 4 | 279 | 14.2% |
| 5 | 151 | 7.7% |
| 6 | 72 | 3.7% |
| 7 | 27 | 1.4% |
| 8 | 5 | 0.3% |
| 9 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 713 | 1.294 | 1.036 | 2.33 |
| 2021-2022 | 306 | 760 | 1.324 | 1.16 | 2.484 |
| 2022-2023 | 306 | 808 | 1.435 | 1.206 | 2.641 |
| 2023-2024 | 306 | 814 | 1.48 | 1.18 | 2.66 |
| 2024-2025 | 306 | 831 | 1.422 | 1.294 | 2.716 |
| 2025-2026 | 328 | 991 | 1.619 | 1.402 | 3.021 |
| 2026-2027 | 108 | 291 | 1.5 | 1.194 | 2.694 |

## 3. Home vs away goal share
- Home goals: **2821** (54.2%)
- Away goals: **2387** (45.8%)
- Home/away ratio: **1.182**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 396 | 317 | 713 | 55.5% | 44.5% |
| 2021-2022 | 405 | 355 | 760 | 53.3% | 46.7% |
| 2022-2023 | 439 | 369 | 808 | 54.3% | 45.7% |
| 2023-2024 | 453 | 361 | 814 | 55.7% | 44.3% |
| 2024-2025 | 435 | 396 | 831 | 52.3% | 47.7% |
| 2025-2026 | 531 | 460 | 991 | 53.6% | 46.4% |
| 2026-2027 | 162 | 129 | 291 | 55.7% | 44.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **1035** of `1966` (52.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 306 | 127 | 41.5% |
| 2021-2022 | 306 | 148 | 48.4% |
| 2022-2023 | 306 | 166 | 54.2% |
| 2023-2024 | 306 | 159 | 52.0% |
| 2024-2025 | 306 | 164 | 53.6% |
| 2025-2026 | 328 | 213 | 64.9% |
| 2026-2027 | 108 | 58 | 53.7% |

## 5. Clean sheets
- Home clean sheets: **591** (30.1%)
- Away clean sheets: **486** (24.7%)
- Total clean sheets recorded: **1077**
- Matches with at least one clean sheet: **931** (47.4%)
- Both teams kept clean sheets (0-0): **146**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 121 | 87 | 208 | 179 (58.5%) |
| 2021-2022 | 306 | 98 | 90 | 188 | 158 (51.6%) |
| 2022-2023 | 306 | 89 | 71 | 160 | 140 (45.8%) |
| 2023-2024 | 306 | 97 | 73 | 170 | 147 (48.0%) |
| 2024-2025 | 306 | 84 | 82 | 166 | 142 (46.4%) |
| 2025-2026 | 328 | 71 | 59 | 130 | 115 (35.1%) |
| 2026-2027 | 108 | 31 | 24 | 55 | 50 (46.3%) |

## 6. Scoring intensity
- First-half goals: **2351** (45.2%)
- Second-half goals: **2851** (54.8%)
- Avg first-half goals per match: **1.197**
- Avg second-half goals per match: **1.452**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **438** (22.3%)
- *2 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 303 | 410 | 42.5% | 57.5% |
| 2021-2022 | 306 | 348 | 412 | 45.8% | 54.2% |
| 2022-2023 | 306 | 377 | 431 | 46.7% | 53.3% |
| 2023-2024 | 306 | 354 | 460 | 43.5% | 56.5% |
| 2024-2025 | 306 | 387 | 441 | 46.7% | 53.3% |
| 2025-2026 | 328 | 452 | 536 | 45.7% | 54.3% |
| 2026-2027 | 108 | 130 | 161 | 44.7% | 55.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1818` of `1966` (92.5%)
- Goalless matches: `148`
- Min `1` | Max `98` | Mean `31.72` | Median (p50) `26.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 584 | 29.7% | 32.1% |
| 16-30 | 427 | 21.7% | 23.5% |
| 31-45 | 319 | 16.2% | 17.5% |
| 46-60 | 233 | 11.9% | 12.8% |
| 61-75 | 129 | 6.6% | 7.1% |
| 76-90 | 100 | 5.1% | 5.5% |
| 91-120 | 26 | 1.3% | 1.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

