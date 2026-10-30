# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-30T04:02:23+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 194 | 13.1% |
| 1 | 312 | 21.0% |
| 2 | 389 | 26.2% |
| 3 | 329 | 22.2% |
| 4 | 146 | 9.8% |
| 5 | 81 | 5.5% |
| 6 | 18 | 1.2% |
| 7 | 13 | 0.9% |
| 8 | 2 | 0.1% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 540 | 1.229 | 1.021 | 2.25 |
| 2021-2022 | 240 | 519 | 1.183 | 0.979 | 2.163 |
| 2022-2023 | 240 | 512 | 1.188 | 0.946 | 2.133 |
| 2023-2024 | 240 | 534 | 1.217 | 1.008 | 2.225 |
| 2024-2025 | 240 | 555 | 1.242 | 1.071 | 2.312 |
| 2025-2026 | 248 | 539 | 1.149 | 1.024 | 2.173 |
| 2026-2027 | 37 | 92 | 1.027 | 1.459 | 2.486 |

## 3. Home vs away goal share
- Home goals: **1777** (54.0%)
- Away goals: **1514** (46.0%)
- Home/away ratio: **1.174**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 295 | 245 | 540 | 54.6% | 45.4% |
| 2021-2022 | 284 | 235 | 519 | 54.7% | 45.3% |
| 2022-2023 | 285 | 227 | 512 | 55.7% | 44.3% |
| 2023-2024 | 292 | 242 | 534 | 54.7% | 45.3% |
| 2024-2025 | 298 | 257 | 555 | 53.7% | 46.3% |
| 2025-2026 | 285 | 254 | 539 | 52.9% | 47.1% |
| 2026-2027 | 38 | 54 | 92 | 41.3% | 58.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **710** of `1485` (47.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 240 | 116 | 48.3% |
| 2021-2022 | 240 | 111 | 46.2% |
| 2022-2023 | 240 | 112 | 46.7% |
| 2023-2024 | 240 | 115 | 47.9% |
| 2024-2025 | 240 | 107 | 44.6% |
| 2025-2026 | 248 | 129 | 52.0% |
| 2026-2027 | 37 | 20 | 54.1% |

## 5. Clean sheets
- Home clean sheets: **531** (35.8%)
- Away clean sheets: **438** (29.5%)
- Total clean sheets recorded: **969**
- Matches with at least one clean sheet: **775** (52.2%)
- Both teams kept clean sheets (0-0): **194**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 84 | 74 | 158 | 124 (51.7%) |
| 2021-2022 | 240 | 92 | 77 | 169 | 129 (53.8%) |
| 2022-2023 | 240 | 87 | 75 | 162 | 128 (53.3%) |
| 2023-2024 | 240 | 84 | 71 | 155 | 125 (52.1%) |
| 2024-2025 | 240 | 89 | 66 | 155 | 133 (55.4%) |
| 2025-2026 | 248 | 86 | 62 | 148 | 119 (48.0%) |
| 2026-2027 | 37 | 9 | 13 | 22 | 17 (45.9%) |

## 6. Scoring intensity
- First-half goals: **1446** (43.9%)
- Second-half goals: **1845** (56.1%)
- Avg first-half goals per match: **0.974**
- Avg second-half goals per match: **1.242**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **379** (25.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 240 | 250 | 290 | 46.3% | 53.7% |
| 2021-2022 | 240 | 225 | 294 | 43.4% | 56.6% |
| 2022-2023 | 240 | 226 | 286 | 44.1% | 55.9% |
| 2023-2024 | 240 | 227 | 307 | 42.5% | 57.5% |
| 2024-2025 | 240 | 228 | 327 | 41.1% | 58.9% |
| 2025-2026 | 248 | 250 | 289 | 46.4% | 53.6% |
| 2026-2027 | 37 | 40 | 52 | 43.5% | 56.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1291` of `1485` (86.9%)
- Goalless matches: `194`
- Min `1` | Max `104` | Mean `34.99` | Median (p50) `31`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 357 | 24.0% | 27.7% |
| 16-30 | 285 | 19.2% | 22.1% |
| 31-45 | 220 | 14.8% | 17.0% |
| 46-60 | 216 | 14.5% | 16.7% |
| 61-75 | 104 | 7.0% | 8.1% |
| 76-90 | 75 | 5.1% | 5.8% |
| 91-120 | 34 | 2.3% | 2.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

