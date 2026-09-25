# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:49:41+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 18 | 6.8% |
| 1 | 47 | 17.8% |
| 2 | 74 | 28.0% |
| 3 | 52 | 19.7% |
| 4 | 35 | 13.3% |
| 5 | 26 | 9.8% |
| 6 | 5 | 1.9% |
| 7 | 4 | 1.5% |
| 8 | 2 | 0.8% |
| 9 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 642 | 1.583 | 1.092 | 2.675 |
| 2026-2027 | 24 | 62 | 1.208 | 1.375 | 2.583 |

## 3. Home vs away goal share
- Home goals: **409** (58.1%)
- Away goals: **295** (41.9%)
- Home/away ratio: **1.386**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 262 | 642 | 59.2% | 40.8% |
| 2026-2027 | 29 | 33 | 62 | 46.8% | 53.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **148** of `264` (56.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 240 | 133 | 55.4% |
| 2026-2027 | 24 | 15 | 62.5% |

## 5. Clean sheets
- Home clean sheets: **83** (31.4%)
- Away clean sheets: **51** (19.3%)
- Total clean sheets recorded: **134**
- Matches with at least one clean sheet: **116** (43.9%)
- Both teams kept clean sheets (0-0): **18**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 78 | 46 | 124 | 107 (44.6%) |
| 2026-2027 | 24 | 5 | 5 | 10 | 9 (37.5%) |

## 6. Scoring intensity
- First-half goals: **302** (42.9%)
- Second-half goals: **402** (57.1%)
- Avg first-half goals per match: **1.144**
- Avg second-half goals per match: **1.523**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **64** (24.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 264 | 378 | 41.1% | 58.9% |
| 2026-2027 | 24 | 38 | 24 | 61.3% | 38.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `246` of `264` (93.2%)
- Goalless matches: `18`
- Min `1` | Max `107` | Mean `32.55` | Median (p50) `27.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 81 | 30.7% | 32.9% |
| 16-30 | 51 | 19.3% | 20.7% |
| 31-45 | 42 | 15.9% | 17.1% |
| 46-60 | 34 | 12.9% | 13.8% |
| 61-75 | 18 | 6.8% | 7.3% |
| 76-90 | 15 | 5.7% | 6.1% |
| 91-120 | 5 | 1.9% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\thai1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\thai1\charts\goals_analysis_avg_per_season.png)

