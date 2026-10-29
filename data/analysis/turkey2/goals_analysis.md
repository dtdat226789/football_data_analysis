# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-29T02:19:00+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 161 | 7.4% |
| 1 | 386 | 17.7% |
| 2 | 535 | 24.5% |
| 3 | 506 | 23.2% |
| 4 | 283 | 13.0% |
| 5 | 178 | 8.2% |
| 6 | 76 | 3.5% |
| 7 | 40 | 1.8% |
| 8 | 8 | 0.4% |
| 9 | 6 | 0.3% |
| 10 | 0 | 0.0% |
| 11 | 1 | 0.0% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 854 | 1.467 | 1.324 | 2.791 |
| 2021-2022 | 342 | 901 | 1.453 | 1.181 | 2.635 |
| 2022-2023 | 341 | 915 | 1.422 | 1.261 | 2.683 |
| 2023-2024 | 306 | 725 | 1.275 | 1.095 | 2.369 |
| 2024-2025 | 380 | 1011 | 1.505 | 1.155 | 2.661 |
| 2025-2026 | 385 | 1125 | 1.673 | 1.249 | 2.922 |
| 2026-2027 | 120 | 330 | 1.45 | 1.3 | 2.75 |

## 3. Home vs away goal share
- Home goals: **3211** (54.8%)
- Away goals: **2650** (45.2%)
- Home/away ratio: **1.212**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 449 | 405 | 854 | 52.6% | 47.4% |
| 2021-2022 | 497 | 404 | 901 | 55.2% | 44.8% |
| 2022-2023 | 485 | 430 | 915 | 53.0% | 47.0% |
| 2023-2024 | 390 | 335 | 725 | 53.8% | 46.2% |
| 2024-2025 | 572 | 439 | 1011 | 56.6% | 43.4% |
| 2025-2026 | 644 | 481 | 1125 | 57.2% | 42.8% |
| 2026-2027 | 174 | 156 | 330 | 52.7% | 47.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **1067** of `2180` (48.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 306 | 153 | 50.0% |
| 2021-2022 | 342 | 183 | 53.5% |
| 2022-2023 | 341 | 172 | 50.4% |
| 2023-2024 | 306 | 133 | 43.5% |
| 2024-2025 | 380 | 168 | 44.2% |
| 2025-2026 | 385 | 193 | 50.1% |
| 2026-2027 | 120 | 65 | 54.2% |

## 5. Clean sheets
- Home clean sheets: **702** (32.2%)
- Away clean sheets: **572** (26.2%)
- Total clean sheets recorded: **1274**
- Matches with at least one clean sheet: **1113** (51.1%)
- Both teams kept clean sheets (0-0): **161**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 89 | 86 | 175 | 153 (50.0%) |
| 2021-2022 | 342 | 107 | 76 | 183 | 159 (46.5%) |
| 2022-2023 | 341 | 96 | 97 | 193 | 169 (49.6%) |
| 2023-2024 | 306 | 103 | 98 | 201 | 173 (56.5%) |
| 2024-2025 | 380 | 142 | 98 | 240 | 212 (55.8%) |
| 2025-2026 | 385 | 135 | 85 | 220 | 192 (49.9%) |
| 2026-2027 | 120 | 30 | 32 | 62 | 55 (45.8%) |

## 6. Scoring intensity
- First-half goals: **2562** (44.4%)
- Second-half goals: **3205** (55.6%)
- Avg first-half goals per match: **1.193**
- Avg second-half goals per match: **1.492**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **500** (22.9%)
- *32 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 306 | 368 | 483 | 43.2% | 56.8% |
| 2021-2022 | 342 | 395 | 506 | 43.8% | 56.2% |
| 2022-2023 | 341 | 368 | 463 | 44.3% | 55.7% |
| 2023-2024 | 306 | 314 | 411 | 43.3% | 56.7% |
| 2024-2025 | 380 | 476 | 532 | 47.2% | 52.8% |
| 2025-2026 | 385 | 491 | 631 | 43.8% | 56.2% |
| 2026-2027 | 120 | 150 | 179 | 45.6% | 54.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1987` of `2180` (91.1%)
- Goalless matches: `193`
- Min `1` | Max `98` | Mean `31.95` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 610 | 28.0% | 30.7% |
| 16-30 | 481 | 22.1% | 24.2% |
| 31-45 | 332 | 15.2% | 16.7% |
| 46-60 | 300 | 13.8% | 15.1% |
| 61-75 | 147 | 6.7% | 7.4% |
| 76-90 | 94 | 4.3% | 4.7% |
| 91-120 | 23 | 1.1% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

