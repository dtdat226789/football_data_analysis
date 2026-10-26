# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-26T01:45:01+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 112 | 7.3% |
| 1 | 266 | 17.3% |
| 2 | 381 | 24.7% |
| 3 | 324 | 21.0% |
| 4 | 234 | 15.2% |
| 5 | 134 | 8.7% |
| 6 | 66 | 4.3% |
| 7 | 18 | 1.2% |
| 8 | 5 | 0.3% |
| 9 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 637 | 1.558 | 1.096 | 2.654 |
| 2021-2022 | 240 | 639 | 1.496 | 1.167 | 2.663 |
| 2022-2023 | 240 | 730 | 1.712 | 1.329 | 3.042 |
| 2023-2024 | 240 | 637 | 1.496 | 1.158 | 2.654 |
| 2024-2025 | 240 | 648 | 1.517 | 1.183 | 2.7 |
| 2025-2026 | 244 | 615 | 1.434 | 1.086 | 2.52 |
| 2026-2027 | 97 | 271 | 1.433 | 1.361 | 2.794 |

## 3. Home vs away goal share
- Home goals: **2356** (56.4%)
- Away goals: **1821** (43.6%)
- Home/away ratio: **1.294**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 374 | 263 | 637 | 58.7% | 41.3% |
| 2021-2022 | 359 | 280 | 639 | 56.2% | 43.8% |
| 2022-2023 | 411 | 319 | 730 | 56.3% | 43.7% |
| 2023-2024 | 359 | 278 | 637 | 56.4% | 43.6% |
| 2024-2025 | 364 | 284 | 648 | 56.2% | 43.8% |
| 2025-2026 | 350 | 265 | 615 | 56.9% | 43.1% |
| 2026-2027 | 139 | 132 | 271 | 51.3% | 48.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **820** of `1541` (53.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 240 | 111 | 46.2% |
| 2021-2022 | 240 | 138 | 57.5% |
| 2022-2023 | 240 | 136 | 56.7% |
| 2023-2024 | 240 | 128 | 53.3% |
| 2024-2025 | 240 | 123 | 51.2% |
| 2025-2026 | 244 | 125 | 51.2% |
| 2026-2027 | 97 | 59 | 60.8% |

## 5. Clean sheets
- Home clean sheets: **489** (31.7%)
- Away clean sheets: **344** (22.3%)
- Total clean sheets recorded: **833**
- Matches with at least one clean sheet: **721** (46.8%)
- Both teams kept clean sheets (0-0): **112**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 86 | 60 | 146 | 129 (53.8%) |
| 2021-2022 | 240 | 70 | 50 | 120 | 102 (42.5%) |
| 2022-2023 | 240 | 68 | 50 | 118 | 104 (43.3%) |
| 2023-2024 | 240 | 82 | 50 | 132 | 112 (46.7%) |
| 2024-2025 | 240 | 79 | 58 | 137 | 117 (48.8%) |
| 2025-2026 | 244 | 81 | 53 | 134 | 119 (48.8%) |
| 2026-2027 | 97 | 23 | 23 | 46 | 38 (39.2%) |

## 6. Scoring intensity
- First-half goals: **1823** (43.7%)
- Second-half goals: **2345** (56.3%)
- Avg first-half goals per match: **1.185**
- Avg second-half goals per match: **1.525**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **358** (23.2%)
- *3 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 260 | 371 | 41.2% | 58.8% |
| 2021-2022 | 240 | 289 | 350 | 45.2% | 54.8% |
| 2022-2023 | 240 | 316 | 411 | 43.5% | 56.5% |
| 2023-2024 | 240 | 278 | 359 | 43.6% | 56.4% |
| 2024-2025 | 240 | 287 | 361 | 44.3% | 55.7% |
| 2025-2026 | 244 | 285 | 330 | 46.3% | 53.7% |
| 2026-2027 | 97 | 108 | 163 | 39.9% | 60.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1426` of `1541` (92.5%)
- Goalless matches: `115`
- Min `1` | Max `99` | Mean `32.55` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 433 | 28.1% | 30.4% |
| 16-30 | 345 | 22.4% | 24.2% |
| 31-45 | 249 | 16.2% | 17.5% |
| 46-60 | 193 | 12.5% | 13.5% |
| 61-75 | 108 | 7.0% | 7.6% |
| 76-90 | 77 | 5.0% | 5.4% |
| 91-120 | 21 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

