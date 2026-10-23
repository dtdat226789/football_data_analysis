# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:04:31+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.7% |
| 1 | 97 | 22.6% |
| 2 | 108 | 25.2% |
| 3 | 85 | 19.8% |
| 4 | 54 | 12.6% |
| 5 | 23 | 5.4% |
| 6 | 7 | 1.6% |
| 7 | 3 | 0.7% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 856 | 1.316 | 0.937 | 2.253 |
| 2026-2027 | 49 | 123 | 1.388 | 1.122 | 2.51 |

## 3. Home vs away goal share
- Home goals: **568** (58.0%)
- Away goals: **411** (42.0%)
- Home/away ratio: **1.382**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 500 | 356 | 856 | 58.4% | 41.6% |
| 2026-2027 | 68 | 55 | 123 | 55.3% | 44.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **191** of `429` (44.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 167 | 43.9% |
| 2026-2027 | 49 | 24 | 49.0% |

## 5. Clean sheets
- Home clean sheets: **175** (40.8%)
- Away clean sheets: **113** (26.3%)
- Total clean sheets recorded: **288**
- Matches with at least one clean sheet: **238** (55.5%)
- Both teams kept clean sheets (0-0): **50**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 156 | 103 | 259 | 213 (56.1%) |
| 2026-2027 | 49 | 19 | 10 | 29 | 25 (51.0%) |

## 6. Scoring intensity
- First-half goals: **454** (46.4%)
- Second-half goals: **525** (53.6%)
- Avg first-half goals per match: **1.058**
- Avg second-half goals per match: **1.224**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **100** (23.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 398 | 458 | 46.5% | 53.5% |
| 2026-2027 | 49 | 56 | 67 | 45.5% | 54.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `379` of `429` (88.3%)
- Goalless matches: `50`
- Min `1` | Max `97` | Mean `32.98` | Median (p50) `28`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 114 | 26.6% | 30.1% |
| 16-30 | 87 | 20.3% | 23.0% |
| 31-45 | 68 | 15.9% | 17.9% |
| 46-60 | 52 | 12.1% | 13.7% |
| 61-75 | 34 | 7.9% | 9.0% |
| 76-90 | 17 | 4.0% | 4.5% |
| 91-120 | 7 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\primera2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\primera2\charts\goals_analysis_avg_per_season.png)

