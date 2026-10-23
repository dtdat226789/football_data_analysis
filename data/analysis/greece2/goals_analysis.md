# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:52:02+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 24 | 8.1% |
| 1 | 80 | 26.9% |
| 2 | 77 | 25.9% |
| 3 | 61 | 20.5% |
| 4 | 29 | 9.8% |
| 5 | 16 | 5.4% |
| 6 | 7 | 2.4% |
| 7 | 3 | 1.0% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 607 | 1.313 | 0.977 | 2.291 |
| 2026-2027 | 32 | 69 | 1.375 | 0.781 | 2.156 |

## 3. Home vs away goal share
- Home goals: **392** (58.0%)
- Away goals: **284** (42.0%)
- Home/away ratio: **1.38**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 348 | 259 | 607 | 57.3% | 42.7% |
| 2026-2027 | 44 | 25 | 69 | 63.8% | 36.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **119** of `297` (40.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 265 | 106 | 40.0% |
| 2026-2027 | 32 | 13 | 40.6% |

## 5. Clean sheets
- Home clean sheets: **123** (41.4%)
- Away clean sheets: **79** (26.6%)
- Total clean sheets recorded: **202**
- Matches with at least one clean sheet: **178** (59.9%)
- Both teams kept clean sheets (0-0): **24**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 105 | 75 | 180 | 159 (60.0%) |
| 2026-2027 | 32 | 18 | 4 | 22 | 19 (59.4%) |

## 6. Scoring intensity
- First-half goals: **301** (44.5%)
- Second-half goals: **375** (55.5%)
- Avg first-half goals per match: **1.013**
- Avg second-half goals per match: **1.263**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **84** (28.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 265 | 276 | 331 | 45.5% | 54.5% |
| 2026-2027 | 32 | 25 | 44 | 36.2% | 63.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `273` of `297` (91.9%)
- Goalless matches: `24`
- Min `1` | Max `95` | Mean `34.59` | Median (p50) `31`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 84 | 28.3% | 30.8% |
| 16-30 | 52 | 17.5% | 19.0% |
| 31-45 | 46 | 15.5% | 16.8% |
| 46-60 | 41 | 13.8% | 15.0% |
| 61-75 | 32 | 10.8% | 11.7% |
| 76-90 | 13 | 4.4% | 4.8% |
| 91-120 | 5 | 1.7% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\greece2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\greece2\charts\goals_analysis_avg_per_season.png)

