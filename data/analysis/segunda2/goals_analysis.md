# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:07:02+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.4% |
| 1 | 66 | 19.3% |
| 2 | 87 | 25.4% |
| 3 | 61 | 17.8% |
| 4 | 56 | 16.4% |
| 5 | 29 | 8.5% |
| 6 | 8 | 2.3% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 769 | 1.438 | 1.075 | 2.513 |
| 2026-2027 | 36 | 95 | 1.583 | 1.056 | 2.639 |

## 3. Home vs away goal share
- Home goals: **497** (57.5%)
- Away goals: **367** (42.5%)
- Home/away ratio: **1.354**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 440 | 329 | 769 | 57.2% | 42.8% |
| 2026-2027 | 57 | 38 | 95 | 60.0% | 40.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **173** of `342` (50.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 158 | 51.6% |
| 2026-2027 | 36 | 15 | 41.7% |

## 5. Clean sheets
- Home clean sheets: **115** (33.6%)
- Away clean sheets: **86** (25.1%)
- Total clean sheets recorded: **201**
- Matches with at least one clean sheet: **169** (49.4%)
- Both teams kept clean sheets (0-0): **32**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 102 | 74 | 176 | 148 (48.4%) |
| 2026-2027 | 36 | 13 | 12 | 25 | 21 (58.3%) |

## 6. Scoring intensity
- First-half goals: **374** (43.3%)
- Second-half goals: **490** (56.7%)
- Avg first-half goals per match: **1.094**
- Avg second-half goals per match: **1.433**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **83** (24.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 330 | 439 | 42.9% | 57.1% |
| 2026-2027 | 36 | 44 | 51 | 46.3% | 53.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `310` of `342` (90.6%)
- Goalless matches: `32`
- Min `1` | Max `96` | Mean `32.67` | Median (p50) `27.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 98 | 28.7% | 31.6% |
| 16-30 | 70 | 20.5% | 22.6% |
| 31-45 | 57 | 16.7% | 18.4% |
| 46-60 | 38 | 11.1% | 12.3% |
| 61-75 | 26 | 7.6% | 8.4% |
| 76-90 | 14 | 4.1% | 4.5% |
| 91-120 | 7 | 2.0% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda2\charts\goals_analysis_avg_per_season.png)

