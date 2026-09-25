# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:42:48+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.9% |
| 1 | 95 | 22.7% |
| 2 | 104 | 24.8% |
| 3 | 82 | 19.6% |
| 4 | 53 | 12.6% |
| 5 | 23 | 5.5% |
| 6 | 7 | 1.7% |
| 7 | 3 | 0.7% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 856 | 1.316 | 0.937 | 2.253 |
| 2026-2027 | 39 | 100 | 1.513 | 1.051 | 2.564 |

## 3. Home vs away goal share
- Home goals: **559** (58.5%)
- Away goals: **397** (41.5%)
- Home/away ratio: **1.408**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 500 | 356 | 856 | 58.4% | 41.6% |
| 2026-2027 | 59 | 41 | 100 | 59.0% | 41.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **185** of `419` (44.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 167 | 43.9% |
| 2026-2027 | 39 | 18 | 46.2% |

## 5. Clean sheets
- Home clean sheets: **173** (41.3%)
- Away clean sheets: **111** (26.5%)
- Total clean sheets recorded: **284**
- Matches with at least one clean sheet: **234** (55.8%)
- Both teams kept clean sheets (0-0): **50**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 156 | 103 | 259 | 213 (56.1%) |
| 2026-2027 | 39 | 17 | 8 | 25 | 21 (53.8%) |

## 6. Scoring intensity
- First-half goals: **445** (46.5%)
- Second-half goals: **511** (53.5%)
- Avg first-half goals per match: **1.062**
- Avg second-half goals per match: **1.22**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **95** (22.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 398 | 458 | 46.5% | 53.5% |
| 2026-2027 | 39 | 47 | 53 | 47.0% | 53.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `369` of `419` (88.1%)
- Goalless matches: `50`
- Min `1` | Max `97` | Mean `32.72` | Median (p50) `28`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 112 | 26.7% | 30.4% |
| 16-30 | 85 | 20.3% | 23.0% |
| 31-45 | 67 | 16.0% | 18.2% |
| 46-60 | 49 | 11.7% | 13.3% |
| 61-75 | 33 | 7.9% | 8.9% |
| 76-90 | 17 | 4.1% | 4.6% |
| 91-120 | 6 | 1.4% | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\primera2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\primera2\charts\goals_analysis_avg_per_season.png)

