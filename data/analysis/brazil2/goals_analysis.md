# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:45:38+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 59 | 8.7% |
| 1 | 159 | 23.4% |
| 2 | 180 | 26.5% |
| 3 | 162 | 23.9% |
| 4 | 79 | 11.6% |
| 5 | 22 | 3.2% |
| 6 | 14 | 2.1% |
| 7 | 3 | 0.4% |
| 8 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 380 | 843 | 1.292 | 0.926 | 2.218 |
| 2026 | 299 | 701 | 1.341 | 1.003 | 2.344 |

## 3. Home vs away goal share
- Home goals: **892** (57.8%)
- Away goals: **652** (42.2%)
- Home/away ratio: **1.368**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 491 | 352 | 843 | 58.2% | 41.8% |
| 2026 | 401 | 300 | 701 | 57.2% | 42.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **331** of `679` (48.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 380 | 188 | 49.5% |
| 2026 | 299 | 143 | 47.8% |

## 5. Clean sheets
- Home clean sheets: **255** (37.6%)
- Away clean sheets: **152** (22.4%)
- Total clean sheets recorded: **407**
- Matches with at least one clean sheet: **348** (51.3%)
- Both teams kept clean sheets (0-0): **59**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 380 | 146 | 79 | 225 | 192 (50.5%) |
| 2026 | 299 | 109 | 73 | 182 | 156 (52.2%) |

## 6. Scoring intensity
- First-half goals: **689** (44.6%)
- Second-half goals: **855** (55.4%)
- Avg first-half goals per match: **1.015**
- Avg second-half goals per match: **1.259**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **174** (25.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 380 | 379 | 464 | 45.0% | 55.0% |
| 2026 | 299 | 310 | 391 | 44.2% | 55.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `620` of `679` (91.3%)
- Goalless matches: `59`
- Min `1` | Max `101` | Mean `34.81` | Median (p50) `29.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 170 | 25.0% | 27.4% |
| 16-30 | 151 | 22.2% | 24.4% |
| 31-45 | 101 | 14.9% | 16.3% |
| 46-60 | 85 | 12.5% | 13.7% |
| 61-75 | 61 | 9.0% | 9.8% |
| 76-90 | 34 | 5.0% | 5.5% |
| 91-120 | 18 | 2.7% | 2.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\brazil2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\brazil2\charts\goals_analysis_avg_per_season.png)

