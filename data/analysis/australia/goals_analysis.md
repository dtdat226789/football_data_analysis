# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:43:51+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: A-League (Australia)
- Scope: league `australia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 17 | 5.1% |
| 1 | 51 | 15.4% |
| 2 | 67 | 20.2% |
| 3 | 68 | 20.5% |
| 4 | 64 | 19.3% |
| 5 | 40 | 12.0% |
| 6 | 11 | 3.3% |
| 7 | 7 | 2.1% |
| 8 | 5 | 1.5% |
| 9 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2024-2025 | 169 | 556 | 1.657 | 1.633 | 3.29 |
| 2025-2026 | 163 | 462 | 1.497 | 1.337 | 2.834 |

## 3. Home vs away goal share
- Home goals: **524** (51.5%)
- Away goals: **494** (48.5%)
- Home/away ratio: **1.061**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2024-2025 | 280 | 276 | 556 | 50.4% | 49.6% |
| 2025-2026 | 244 | 218 | 462 | 52.8% | 47.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **202** of `332` (60.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2024-2025 | 169 | 105 | 62.1% |
| 2025-2026 | 163 | 97 | 59.5% |

## 5. Clean sheets
- Home clean sheets: **74** (22.3%)
- Away clean sheets: **73** (22.0%)
- Total clean sheets recorded: **147**
- Matches with at least one clean sheet: **130** (39.2%)
- Both teams kept clean sheets (0-0): **17**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2024-2025 | 169 | 37 | 35 | 72 | 64 (37.9%) |
| 2025-2026 | 163 | 37 | 38 | 75 | 66 (40.5%) |

## 6. Scoring intensity
- First-half goals: **458** (45.0%)
- Second-half goals: **560** (55.0%)
- Avg first-half goals per match: **1.38**
- Avg second-half goals per match: **1.687**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **70** (21.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2024-2025 | 169 | 254 | 302 | 45.7% | 54.3% |
| 2025-2026 | 163 | 204 | 258 | 44.2% | 55.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `315` of `332` (94.9%)
- Goalless matches: `17`
- Min `1` | Max `99` | Mean `28.58` | Median (p50) `20`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 128 | 38.6% | 40.6% |
| 16-30 | 63 | 19.0% | 20.0% |
| 31-45 | 47 | 14.2% | 14.9% |
| 46-60 | 42 | 12.7% | 13.3% |
| 61-75 | 20 | 6.0% | 6.3% |
| 76-90 | 9 | 2.7% | 2.9% |
| 91-120 | 6 | 1.8% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\australia\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\australia\charts\goals_analysis_avg_per_season.png)

