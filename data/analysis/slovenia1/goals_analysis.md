# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-27T02:31:09+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 94 | 8.3% |
| 1 | 188 | 16.7% |
| 2 | 285 | 25.3% |
| 3 | 242 | 21.5% |
| 4 | 162 | 14.4% |
| 5 | 90 | 8.0% |
| 6 | 45 | 4.0% |
| 7 | 14 | 1.2% |
| 8 | 4 | 0.4% |
| 9 | 1 | 0.1% |
| 10 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020-2021 | 180 | 422 | 1.322 | 1.022 | 2.344 |
| 2021-2022 | 180 | 457 | 1.311 | 1.228 | 2.539 |
| 2022-2023 | 180 | 457 | 1.3 | 1.239 | 2.539 |
| 2023-2024 | 180 | 505 | 1.467 | 1.339 | 2.806 |
| 2024-2025 | 180 | 498 | 1.561 | 1.206 | 2.767 |
| 2025-2026 | 164 | 501 | 1.665 | 1.39 | 3.055 |
| 2026-2027 | 62 | 161 | 1.339 | 1.258 | 2.597 |

## 3. Home vs away goal share
- Home goals: **1609** (53.6%)
- Away goals: **1392** (46.4%)
- Home/away ratio: **1.156**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020-2021 | 238 | 184 | 422 | 56.4% | 43.6% |
| 2021-2022 | 236 | 221 | 457 | 51.6% | 48.4% |
| 2022-2023 | 234 | 223 | 457 | 51.2% | 48.8% |
| 2023-2024 | 264 | 241 | 505 | 52.3% | 47.7% |
| 2024-2025 | 281 | 217 | 498 | 56.4% | 43.6% |
| 2025-2026 | 273 | 228 | 501 | 54.5% | 45.5% |
| 2026-2027 | 83 | 78 | 161 | 51.6% | 48.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **585** of `1126` (52.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020-2021 | 180 | 85 | 47.2% |
| 2021-2022 | 180 | 89 | 49.4% |
| 2022-2023 | 180 | 88 | 48.9% |
| 2023-2024 | 180 | 105 | 58.3% |
| 2024-2025 | 180 | 92 | 51.1% |
| 2025-2026 | 164 | 95 | 57.9% |
| 2026-2027 | 62 | 31 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **339** (30.1%)
- Away clean sheets: **296** (26.3%)
- Total clean sheets recorded: **635**
- Matches with at least one clean sheet: **541** (48.0%)
- Both teams kept clean sheets (0-0): **94**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020-2021 | 180 | 66 | 53 | 119 | 95 (52.8%) |
| 2021-2022 | 180 | 54 | 52 | 106 | 91 (50.6%) |
| 2022-2023 | 180 | 50 | 58 | 108 | 92 (51.1%) |
| 2023-2024 | 180 | 45 | 40 | 85 | 75 (41.7%) |
| 2024-2025 | 180 | 58 | 43 | 101 | 88 (48.9%) |
| 2025-2026 | 164 | 45 | 32 | 77 | 69 (42.1%) |
| 2026-2027 | 62 | 21 | 18 | 39 | 31 (50.0%) |

## 6. Scoring intensity
- First-half goals: **1347** (45.1%)
- Second-half goals: **1642** (54.9%)
- Avg first-half goals per match: **1.201**
- Avg second-half goals per match: **1.463**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **209** (18.6%)
- *4 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020-2021 | 180 | 189 | 230 | 45.1% | 54.9% |
| 2021-2022 | 180 | 208 | 249 | 45.5% | 54.5% |
| 2022-2023 | 180 | 206 | 251 | 45.1% | 54.9% |
| 2023-2024 | 180 | 226 | 273 | 45.3% | 54.7% |
| 2024-2025 | 180 | 222 | 276 | 44.6% | 55.4% |
| 2025-2026 | 164 | 228 | 270 | 45.8% | 54.2% |
| 2026-2027 | 62 | 68 | 93 | 42.2% | 57.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1028` of `1126` (91.3%)
- Goalless matches: `98`
- Min `1` | Max `95` | Mean `29.61` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 353 | 31.3% | 34.3% |
| 16-30 | 260 | 23.1% | 25.3% |
| 31-45 | 192 | 17.1% | 18.7% |
| 46-60 | 109 | 9.7% | 10.6% |
| 61-75 | 62 | 5.5% | 6.0% |
| 76-90 | 34 | 3.0% | 3.3% |
| 91-120 | 18 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

