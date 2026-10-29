# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-29T02:13:09+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 83 | 6.5% |
| 1 | 229 | 17.8% |
| 2 | 310 | 24.1% |
| 3 | 297 | 23.1% |
| 4 | 196 | 15.3% |
| 5 | 97 | 7.6% |
| 6 | 51 | 4.0% |
| 7 | 14 | 1.1% |
| 8 | 5 | 0.4% |
| 9 | 2 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 198 | 475 | 1.242 | 1.157 | 2.399 |
| 2021-2022 | 198 | 491 | 1.394 | 1.086 | 2.48 |
| 2022-2023 | 198 | 583 | 1.702 | 1.242 | 2.944 |
| 2023-2024 | 198 | 526 | 1.465 | 1.192 | 2.657 |
| 2024-2025 | 198 | 584 | 1.707 | 1.242 | 2.949 |
| 2025-2026 | 234 | 643 | 1.573 | 1.175 | 2.748 |
| 2026-2027 | 60 | 169 | 1.5 | 1.317 | 2.817 |

## 3. Home vs away goal share
- Home goals: **1945** (56.0%)
- Away goals: **1526** (44.0%)
- Home/away ratio: **1.275**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 246 | 229 | 475 | 51.8% | 48.2% |
| 2021-2022 | 276 | 215 | 491 | 56.2% | 43.8% |
| 2022-2023 | 337 | 246 | 583 | 57.8% | 42.2% |
| 2023-2024 | 290 | 236 | 526 | 55.1% | 44.9% |
| 2024-2025 | 338 | 246 | 584 | 57.9% | 42.1% |
| 2025-2026 | 368 | 275 | 643 | 57.2% | 42.8% |
| 2026-2027 | 90 | 79 | 169 | 53.3% | 46.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **628** of `1284` (48.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 198 | 80 | 40.4% |
| 2021-2022 | 198 | 96 | 48.5% |
| 2022-2023 | 198 | 99 | 50.0% |
| 2023-2024 | 198 | 95 | 48.0% |
| 2024-2025 | 198 | 104 | 52.5% |
| 2025-2026 | 234 | 121 | 51.7% |
| 2026-2027 | 60 | 33 | 55.0% |

## 5. Clean sheets
- Home clean sheets: **438** (34.1%)
- Away clean sheets: **301** (23.4%)
- Total clean sheets recorded: **739**
- Matches with at least one clean sheet: **656** (51.1%)
- Both teams kept clean sheets (0-0): **83**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 198 | 71 | 64 | 135 | 118 (59.6%) |
| 2021-2022 | 198 | 74 | 45 | 119 | 102 (51.5%) |
| 2022-2023 | 198 | 66 | 39 | 105 | 99 (50.0%) |
| 2023-2024 | 198 | 65 | 52 | 117 | 103 (52.0%) |
| 2024-2025 | 198 | 65 | 39 | 104 | 94 (47.5%) |
| 2025-2026 | 234 | 83 | 47 | 130 | 113 (48.3%) |
| 2026-2027 | 60 | 14 | 15 | 29 | 27 (45.0%) |

## 6. Scoring intensity
- First-half goals: **1592** (45.9%)
- Second-half goals: **1879** (54.1%)
- Avg first-half goals per match: **1.24**
- Avg second-half goals per match: **1.463**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **260** (20.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 198 | 225 | 250 | 47.4% | 52.6% |
| 2021-2022 | 198 | 240 | 251 | 48.9% | 51.1% |
| 2022-2023 | 198 | 264 | 319 | 45.3% | 54.7% |
| 2023-2024 | 198 | 216 | 310 | 41.1% | 58.9% |
| 2024-2025 | 198 | 264 | 320 | 45.2% | 54.8% |
| 2025-2026 | 234 | 291 | 352 | 45.3% | 54.7% |
| 2026-2027 | 60 | 92 | 77 | 54.4% | 45.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1201` of `1284` (93.5%)
- Goalless matches: `83`
- Min `1` | Max `98` | Mean `29.88` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 400 | 31.2% | 33.3% |
| 16-30 | 323 | 25.2% | 26.9% |
| 31-45 | 196 | 15.3% | 16.3% |
| 46-60 | 138 | 10.7% | 11.5% |
| 61-75 | 79 | 6.2% | 6.6% |
| 76-90 | 50 | 3.9% | 4.2% |
| 91-120 | 15 | 1.2% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

