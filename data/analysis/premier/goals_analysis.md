# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-27T02:25:45+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 135 | 5.7% |
| 1 | 369 | 15.6% |
| 2 | 551 | 23.3% |
| 3 | 529 | 22.4% |
| 4 | 385 | 16.3% |
| 5 | 229 | 9.7% |
| 6 | 95 | 4.0% |
| 7 | 49 | 2.1% |
| 8 | 11 | 0.5% |
| 9 | 7 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 380 | 1024 | 1.353 | 1.342 | 2.695 |
| 2021-2022 | 380 | 1071 | 1.513 | 1.305 | 2.818 |
| 2022-2023 | 380 | 1084 | 1.634 | 1.218 | 2.853 |
| 2023-2024 | 380 | 1246 | 1.8 | 1.479 | 3.279 |
| 2024-2025 | 380 | 1115 | 1.513 | 1.421 | 2.934 |
| 2025-2026 | 380 | 1045 | 1.526 | 1.224 | 2.75 |
| 2026-2027 | 80 | 222 | 1.512 | 1.262 | 2.775 |

## 3. Home vs away goal share
- Home goals: **3670** (53.9%)
- Away goals: **3137** (46.1%)
- Home/away ratio: **1.17**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 514 | 510 | 1024 | 50.2% | 49.8% |
| 2021-2022 | 575 | 496 | 1071 | 53.7% | 46.3% |
| 2022-2023 | 621 | 463 | 1084 | 57.3% | 42.7% |
| 2023-2024 | 684 | 562 | 1246 | 54.9% | 45.1% |
| 2024-2025 | 575 | 540 | 1115 | 51.6% | 48.4% |
| 2025-2026 | 580 | 465 | 1045 | 55.5% | 44.5% |
| 2026-2027 | 121 | 101 | 222 | 54.5% | 45.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **1277** of `2360` (54.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 380 | 186 | 48.9% |
| 2021-2022 | 380 | 190 | 50.0% |
| 2022-2023 | 380 | 196 | 51.6% |
| 2023-2024 | 380 | 234 | 61.6% |
| 2024-2025 | 380 | 218 | 57.4% |
| 2025-2026 | 380 | 213 | 56.1% |
| 2026-2027 | 80 | 40 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **662** (28.1%)
- Away clean sheets: **556** (23.6%)
- Total clean sheets recorded: **1218**
- Matches with at least one clean sheet: **1083** (45.9%)
- Both teams kept clean sheets (0-0): **135**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 380 | 113 | 111 | 224 | 194 (51.1%) |
| 2021-2022 | 380 | 119 | 93 | 212 | 190 (50.0%) |
| 2022-2023 | 380 | 125 | 82 | 207 | 184 (48.4%) |
| 2023-2024 | 380 | 89 | 68 | 157 | 146 (38.4%) |
| 2024-2025 | 380 | 87 | 91 | 178 | 162 (42.6%) |
| 2025-2026 | 380 | 108 | 86 | 194 | 167 (43.9%) |
| 2026-2027 | 80 | 21 | 25 | 46 | 40 (50.0%) |

## 6. Scoring intensity
- First-half goals: **3048** (44.8%)
- Second-half goals: **3759** (55.2%)
- Avg first-half goals per match: **1.292**
- Avg second-half goals per match: **1.593**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **504** (21.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 380 | 483 | 541 | 47.2% | 52.8% |
| 2021-2022 | 380 | 484 | 587 | 45.2% | 54.8% |
| 2022-2023 | 380 | 502 | 582 | 46.3% | 53.7% |
| 2023-2024 | 380 | 517 | 729 | 41.5% | 58.5% |
| 2024-2025 | 380 | 518 | 597 | 46.5% | 53.5% |
| 2025-2026 | 380 | 452 | 593 | 43.3% | 56.7% |
| 2026-2027 | 80 | 92 | 130 | 41.4% | 58.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `2225` of `2360` (94.3%)
- Goalless matches: `135`
- Min `1` | Max `99` | Mean `29.99` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 763 | 32.3% | 34.3% |
| 16-30 | 545 | 23.1% | 24.5% |
| 31-45 | 357 | 15.1% | 16.0% |
| 46-60 | 300 | 12.7% | 13.5% |
| 61-75 | 148 | 6.3% | 6.7% |
| 76-90 | 91 | 3.9% | 4.1% |
| 91-120 | 21 | 0.9% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

