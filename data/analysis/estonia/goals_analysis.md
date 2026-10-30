# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-30T03:50:19+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 57 | 4.9% |
| 1 | 181 | 15.5% |
| 2 | 241 | 20.6% |
| 3 | 281 | 24.0% |
| 4 | 205 | 17.5% |
| 5 | 107 | 9.1% |
| 6 | 52 | 4.4% |
| 7 | 22 | 1.9% |
| 8 | 15 | 1.3% |
| 9 | 8 | 0.7% |
| 10 | 1 | 0.1% |
| 11 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020 | 147 | 442 | 1.422 | 1.585 | 3.007 |
| 2021 | 134 | 455 | 1.836 | 1.56 | 3.396 |
| 2022 | 180 | 549 | 1.706 | 1.344 | 3.05 |
| 2023 | 180 | 458 | 1.356 | 1.189 | 2.544 |
| 2024 | 180 | 539 | 1.528 | 1.467 | 2.994 |
| 2025 | 180 | 572 | 1.739 | 1.439 | 3.178 |
| 2026 | 170 | 525 | 1.782 | 1.306 | 3.088 |

## 3. Home vs away goal share
- Home goals: **1897** (53.6%)
- Away goals: **1643** (46.4%)
- Home/away ratio: **1.155**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020 | 209 | 233 | 442 | 47.3% | 52.7% |
| 2021 | 246 | 209 | 455 | 54.1% | 45.9% |
| 2022 | 307 | 242 | 549 | 55.9% | 44.1% |
| 2023 | 244 | 214 | 458 | 53.3% | 46.7% |
| 2024 | 275 | 264 | 539 | 51.0% | 49.0% |
| 2025 | 313 | 259 | 572 | 54.7% | 45.3% |
| 2026 | 303 | 222 | 525 | 57.7% | 42.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **606** of `1171` (51.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020 | 147 | 69 | 46.9% |
| 2021 | 134 | 76 | 56.7% |
| 2022 | 180 | 91 | 50.6% |
| 2023 | 180 | 84 | 46.7% |
| 2024 | 180 | 90 | 50.0% |
| 2025 | 180 | 99 | 55.0% |
| 2026 | 170 | 97 | 57.1% |

## 5. Clean sheets
- Home clean sheets: **334** (28.5%)
- Away clean sheets: **288** (24.6%)
- Total clean sheets recorded: **622**
- Matches with at least one clean sheet: **565** (48.2%)
- Both teams kept clean sheets (0-0): **57**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020 | 147 | 41 | 47 | 88 | 78 (53.1%) |
| 2021 | 134 | 31 | 32 | 63 | 58 (43.3%) |
| 2022 | 180 | 59 | 36 | 95 | 89 (49.4%) |
| 2023 | 180 | 60 | 53 | 113 | 96 (53.3%) |
| 2024 | 180 | 47 | 53 | 100 | 90 (50.0%) |
| 2025 | 180 | 49 | 36 | 85 | 81 (45.0%) |
| 2026 | 170 | 47 | 31 | 78 | 73 (42.9%) |

## 6. Scoring intensity
- First-half goals: **1626** (46.9%)
- Second-half goals: **1838** (53.1%)
- Avg first-half goals per match: **1.416**
- Avg second-half goals per match: **1.601**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **225** (19.2%)
- *23 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020 | 147 | 212 | 230 | 48.0% | 52.0% |
| 2021 | 134 | 201 | 254 | 44.2% | 55.8% |
| 2022 | 180 | 247 | 302 | 45.0% | 55.0% |
| 2023 | 180 | 212 | 246 | 46.3% | 53.7% |
| 2024 | 180 | 256 | 283 | 47.5% | 52.5% |
| 2025 | 180 | 243 | 253 | 49.0% | 51.0% |
| 2026 | 170 | 255 | 270 | 48.6% | 51.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1114` of `1171` (95.1%)
- Goalless matches: `57`
- Min `1` | Max `97` | Mean `28.97` | Median (p50) `23.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 391 | 33.4% | 35.1% |
| 16-30 | 295 | 25.2% | 26.5% |
| 31-45 | 183 | 15.6% | 16.4% |
| 46-60 | 118 | 10.1% | 10.6% |
| 61-75 | 72 | 6.1% | 6.5% |
| 76-90 | 40 | 3.4% | 3.6% |
| 91-120 | 15 | 1.3% | 1.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

