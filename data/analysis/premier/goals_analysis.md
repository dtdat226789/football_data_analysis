# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:42:07+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (England)
- Scope: league `premier`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 134 | 5.8% |
| 1 | 365 | 15.7% |
| 2 | 540 | 23.2% |
| 3 | 523 | 22.4% |
| 4 | 381 | 16.4% |
| 5 | 226 | 9.7% |
| 6 | 94 | 4.0% |
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
| 2026-2027 | 50 | 141 | 1.52 | 1.3 | 2.82 |

## 3. Home vs away goal share
- Home goals: **3625** (53.9%)
- Away goals: **3101** (46.1%)
- Home/away ratio: **1.169**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 514 | 510 | 1024 | 50.2% | 49.8% |
| 2021-2022 | 575 | 496 | 1071 | 53.7% | 46.3% |
| 2022-2023 | 621 | 463 | 1084 | 57.3% | 42.7% |
| 2023-2024 | 684 | 562 | 1246 | 54.9% | 45.1% |
| 2024-2025 | 575 | 540 | 1115 | 51.6% | 48.4% |
| 2025-2026 | 580 | 465 | 1045 | 55.5% | 44.5% |
| 2026-2027 | 76 | 65 | 141 | 53.9% | 46.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **1262** of `2330` (54.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 380 | 186 | 48.9% |
| 2021-2022 | 380 | 190 | 50.0% |
| 2022-2023 | 380 | 196 | 51.6% |
| 2023-2024 | 380 | 234 | 61.6% |
| 2024-2025 | 380 | 218 | 57.4% |
| 2025-2026 | 380 | 213 | 56.1% |
| 2026-2027 | 50 | 25 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **656** (28.2%)
- Away clean sheets: **546** (23.4%)
- Total clean sheets recorded: **1202**
- Matches with at least one clean sheet: **1068** (45.8%)
- Both teams kept clean sheets (0-0): **134**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 380 | 113 | 111 | 224 | 194 (51.1%) |
| 2021-2022 | 380 | 119 | 93 | 212 | 190 (50.0%) |
| 2022-2023 | 380 | 125 | 82 | 207 | 184 (48.4%) |
| 2023-2024 | 380 | 89 | 68 | 157 | 146 (38.4%) |
| 2024-2025 | 380 | 87 | 91 | 178 | 162 (42.6%) |
| 2025-2026 | 380 | 108 | 86 | 194 | 167 (43.9%) |
| 2026-2027 | 50 | 15 | 15 | 30 | 25 (50.0%) |

## 6. Scoring intensity
- First-half goals: **3019** (44.9%)
- Second-half goals: **3707** (55.1%)
- Avg first-half goals per match: **1.296**
- Avg second-half goals per match: **1.591**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **493** (21.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 380 | 483 | 541 | 47.2% | 52.8% |
| 2021-2022 | 380 | 484 | 587 | 45.2% | 54.8% |
| 2022-2023 | 380 | 502 | 582 | 46.3% | 53.7% |
| 2023-2024 | 380 | 517 | 729 | 41.5% | 58.5% |
| 2024-2025 | 380 | 518 | 597 | 46.5% | 53.5% |
| 2025-2026 | 380 | 452 | 593 | 43.3% | 56.7% |
| 2026-2027 | 50 | 63 | 78 | 44.7% | 55.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `2196` of `2330` (94.2%)
- Goalless matches: `134`
- Min `1` | Max `99` | Mean `29.93` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 753 | 32.3% | 34.3% |
| 16-30 | 542 | 23.3% | 24.7% |
| 31-45 | 352 | 15.1% | 16.0% |
| 46-60 | 294 | 12.6% | 13.4% |
| 61-75 | 146 | 6.3% | 6.6% |
| 76-90 | 88 | 3.8% | 4.0% |
| 91-120 | 21 | 0.9% | 1.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\premier\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\premier\charts\goals_analysis_avg_per_season.png)

