# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:00:11+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 23 | 8.0% |
| 1 | 77 | 26.6% |
| 2 | 75 | 26.0% |
| 3 | 60 | 20.8% |
| 4 | 29 | 10.0% |
| 5 | 15 | 5.2% |
| 6 | 7 | 2.4% |
| 7 | 3 | 1.0% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 607 | 1.313 | 0.977 | 2.291 |
| 2026-2027 | 24 | 54 | 1.292 | 0.958 | 2.25 |

## 3. Home vs away goal share
- Home goals: **379** (57.3%)
- Away goals: **282** (42.7%)
- Home/away ratio: **1.344**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 348 | 259 | 607 | 57.3% | 42.7% |
| 2026-2027 | 31 | 23 | 54 | 57.4% | 42.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **117** of `289` (40.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 265 | 106 | 40.0% |
| 2026-2027 | 24 | 11 | 45.8% |

## 5. Clean sheets
- Home clean sheets: **117** (40.5%)
- Away clean sheets: **78** (27.0%)
- Total clean sheets recorded: **195**
- Matches with at least one clean sheet: **172** (59.5%)
- Both teams kept clean sheets (0-0): **23**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 105 | 75 | 180 | 159 (60.0%) |
| 2026-2027 | 24 | 12 | 3 | 15 | 13 (54.2%) |

## 6. Scoring intensity
- First-half goals: **296** (44.8%)
- Second-half goals: **365** (55.2%)
- Avg first-half goals per match: **1.024**
- Avg second-half goals per match: **1.263**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **81** (28.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 276 | 331 | 45.5% | 54.5% |
| 2026-2027 | 24 | 20 | 34 | 37.0% | 63.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `266` of `289` (92.0%)
- Goalless matches: `23`
- Min `1` | Max `95` | Mean `34.61` | Median (p50) `31.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 81 | 28.0% | 30.5% |
| 16-30 | 51 | 17.6% | 19.2% |
| 31-45 | 46 | 15.9% | 17.3% |
| 46-60 | 40 | 13.8% | 15.0% |
| 61-75 | 31 | 10.7% | 11.7% |
| 76-90 | 12 | 4.2% | 4.5% |
| 91-120 | 5 | 1.7% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\greece2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\greece2\charts\goals_analysis_avg_per_season.png)

