# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:45:58+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 35 | 10.4% |
| 1 | 80 | 23.7% |
| 2 | 77 | 22.8% |
| 3 | 67 | 19.9% |
| 4 | 41 | 12.2% |
| 5 | 19 | 5.6% |
| 6 | 15 | 4.5% |
| 7 | 0 | 0.0% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 742 | 1.418 | 1.007 | 2.425 |
| 2026-2027 | 31 | 68 | 1.226 | 0.968 | 2.194 |

## 3. Home vs away goal share
- Home goals: **472** (58.3%)
- Away goals: **338** (41.7%)
- Home/away ratio: **1.396**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 434 | 308 | 742 | 58.5% | 41.5% |
| 2026-2027 | 38 | 30 | 68 | 55.9% | 44.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **176** of `337` (52.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 159 | 52.0% |
| 2026-2027 | 31 | 17 | 54.8% |

## 5. Clean sheets
- Home clean sheets: **126** (37.4%)
- Away clean sheets: **70** (20.8%)
- Total clean sheets recorded: **196**
- Matches with at least one clean sheet: **161** (47.8%)
- Both teams kept clean sheets (0-0): **35**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 114 | 66 | 180 | 147 (48.0%) |
| 2026-2027 | 31 | 12 | 4 | 16 | 14 (45.2%) |

## 6. Scoring intensity
- First-half goals: **348** (43.0%)
- Second-half goals: **462** (57.0%)
- Avg first-half goals per match: **1.033**
- Avg second-half goals per match: **1.371**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **97** (28.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 320 | 422 | 43.1% | 56.9% |
| 2026-2027 | 31 | 28 | 40 | 41.2% | 58.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `302` of `337` (89.6%)
- Goalless matches: `35`
- Min `1` | Max `99` | Mean `34.56` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 96 | 28.5% | 31.8% |
| 16-30 | 68 | 20.2% | 22.5% |
| 31-45 | 36 | 10.7% | 11.9% |
| 46-60 | 40 | 11.9% | 13.2% |
| 61-75 | 34 | 10.1% | 11.3% |
| 76-90 | 23 | 6.8% | 7.6% |
| 91-120 | 5 | 1.5% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda3\charts\goals_analysis_avg_per_season.png)

