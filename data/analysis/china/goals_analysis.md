# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:46:30+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 4.2% |
| 1 | 62 | 13.8% |
| 2 | 98 | 21.9% |
| 3 | 86 | 19.2% |
| 4 | 88 | 19.6% |
| 5 | 47 | 10.5% |
| 6 | 31 | 6.9% |
| 7 | 12 | 2.7% |
| 8 | 4 | 0.9% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 240 | 771 | 1.8 | 1.413 | 3.212 |
| 2026 | 208 | 643 | 1.779 | 1.312 | 3.091 |

## 3. Home vs away goal share
- Home goals: **802** (56.7%)
- Away goals: **612** (43.3%)
- Home/away ratio: **1.31**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 432 | 339 | 771 | 56.0% | 44.0% |
| 2026 | 370 | 273 | 643 | 57.5% | 42.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **284** of `448` (63.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 240 | 151 | 62.9% |
| 2026 | 208 | 133 | 63.9% |

## 5. Clean sheets
- Home clean sheets: **122** (27.2%)
- Away clean sheets: **61** (13.6%)
- Total clean sheets recorded: **183**
- Matches with at least one clean sheet: **164** (36.6%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 240 | 68 | 30 | 98 | 89 (37.1%) |
| 2026 | 208 | 54 | 31 | 85 | 75 (36.1%) |

## 6. Scoring intensity
- First-half goals: **625** (44.2%)
- Second-half goals: **789** (55.8%)
- Avg first-half goals per match: **1.395**
- Avg second-half goals per match: **1.761**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **84** (18.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 240 | 355 | 416 | 46.0% | 54.0% |
| 2026 | 208 | 270 | 373 | 42.0% | 58.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `429` of `448` (95.8%)
- Goalless matches: `19`
- Min `1` | Max `94` | Mean `28.95` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 149 | 33.3% | 34.7% |
| 16-30 | 105 | 23.4% | 24.5% |
| 31-45 | 84 | 18.8% | 19.6% |
| 46-60 | 50 | 11.2% | 11.7% |
| 61-75 | 21 | 4.7% | 4.9% |
| 76-90 | 18 | 4.0% | 4.2% |
| 91-120 | 2 | 0.4% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\china\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\china\charts\goals_analysis_avg_per_season.png)

