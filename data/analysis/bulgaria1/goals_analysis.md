# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-30T03:46:20+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 145 | 9.9% |
| 1 | 324 | 22.2% |
| 2 | 353 | 24.2% |
| 3 | 308 | 21.1% |
| 4 | 180 | 12.3% |
| 5 | 94 | 6.4% |
| 6 | 43 | 2.9% |
| 7 | 10 | 0.7% |
| 8 | 2 | 0.1% |
| 9 | 2 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 182 | 439 | 1.396 | 1.016 | 2.412 |
| 2021-2022 | 182 | 445 | 1.429 | 1.016 | 2.445 |
| 2022-2023 | 240 | 560 | 1.288 | 1.046 | 2.333 |
| 2023-2024 | 240 | 582 | 1.396 | 1.029 | 2.425 |
| 2024-2025 | 240 | 584 | 1.3 | 1.133 | 2.433 |
| 2025-2026 | 294 | 677 | 1.255 | 1.048 | 2.303 |
| 2026-2027 | 83 | 219 | 1.506 | 1.133 | 2.639 |

## 3. Home vs away goal share
- Home goals: **1964** (56.0%)
- Away goals: **1542** (44.0%)
- Home/away ratio: **1.274**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 254 | 185 | 439 | 57.9% | 42.1% |
| 2021-2022 | 260 | 185 | 445 | 58.4% | 41.6% |
| 2022-2023 | 309 | 251 | 560 | 55.2% | 44.8% |
| 2023-2024 | 335 | 247 | 582 | 57.6% | 42.4% |
| 2024-2025 | 312 | 272 | 584 | 53.4% | 46.6% |
| 2025-2026 | 369 | 308 | 677 | 54.5% | 45.5% |
| 2026-2027 | 125 | 94 | 219 | 57.1% | 42.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **628** of `1461` (43.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 182 | 78 | 42.9% |
| 2021-2022 | 182 | 84 | 46.2% |
| 2022-2023 | 240 | 98 | 40.8% |
| 2023-2024 | 240 | 95 | 39.6% |
| 2024-2025 | 240 | 103 | 42.9% |
| 2025-2026 | 294 | 126 | 42.9% |
| 2026-2027 | 83 | 44 | 53.0% |

## 5. Clean sheets
- Home clean sheets: **573** (39.2%)
- Away clean sheets: **405** (27.7%)
- Total clean sheets recorded: **978**
- Matches with at least one clean sheet: **833** (57.0%)
- Both teams kept clean sheets (0-0): **145**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 182 | 75 | 51 | 126 | 104 (57.1%) |
| 2021-2022 | 182 | 77 | 40 | 117 | 98 (53.8%) |
| 2022-2023 | 240 | 92 | 75 | 167 | 142 (59.2%) |
| 2023-2024 | 240 | 104 | 63 | 167 | 145 (60.4%) |
| 2024-2025 | 240 | 83 | 71 | 154 | 137 (57.1%) |
| 2025-2026 | 294 | 116 | 88 | 204 | 168 (57.1%) |
| 2026-2027 | 83 | 26 | 17 | 43 | 39 (47.0%) |

## 6. Scoring intensity
- First-half goals: **1559** (44.5%)
- Second-half goals: **1943** (55.5%)
- Avg first-half goals per match: **1.068**
- Avg second-half goals per match: **1.331**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **356** (24.4%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 182 | 203 | 236 | 46.2% | 53.8% |
| 2021-2022 | 182 | 195 | 250 | 43.8% | 56.2% |
| 2022-2023 | 240 | 243 | 317 | 43.4% | 56.6% |
| 2023-2024 | 240 | 266 | 316 | 45.7% | 54.3% |
| 2024-2025 | 240 | 269 | 315 | 46.1% | 53.9% |
| 2025-2026 | 294 | 291 | 382 | 43.2% | 56.8% |
| 2026-2027 | 83 | 92 | 127 | 42.0% | 58.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1315` of `1461` (90.0%)
- Goalless matches: `146`
- Min `1` | Max `108` | Mean `33.34` | Median (p50) `28`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 380 | 26.0% | 28.9% |
| 16-30 | 316 | 21.6% | 24.0% |
| 31-45 | 226 | 15.5% | 17.2% |
| 46-60 | 190 | 13.0% | 14.4% |
| 61-75 | 111 | 7.6% | 8.4% |
| 76-90 | 72 | 4.9% | 5.5% |
| 91-120 | 20 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

