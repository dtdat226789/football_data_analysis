# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:10:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 7 | 5.6% |
| 1 | 11 | 8.9% |
| 2 | 38 | 30.6% |
| 3 | 29 | 23.4% |
| 4 | 14 | 11.3% |
| 5 | 12 | 9.7% |
| 6 | 9 | 7.3% |
| 7 | 4 | 3.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 324 | 1.491 | 1.509 | 3.0 |
| 2026-2027 | 16 | 48 | 1.875 | 1.125 | 3.0 |

## 3. Home vs away goal share
- Home goals: **191** (51.3%)
- Away goals: **181** (48.7%)
- Home/away ratio: **1.055**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 161 | 163 | 324 | 49.7% | 50.3% |
| 2026-2027 | 30 | 18 | 48 | 62.5% | 37.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **69** of `124` (55.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 108 | 63 | 58.3% |
| 2026-2027 | 16 | 6 | 37.5% |

## 5. Clean sheets
- Home clean sheets: **36** (29.0%)
- Away clean sheets: **26** (21.0%)
- Total clean sheets recorded: **62**
- Matches with at least one clean sheet: **55** (44.4%)
- Both teams kept clean sheets (0-0): **7**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 28 | 23 | 51 | 45 (41.7%) |
| 2026-2027 | 16 | 8 | 3 | 11 | 10 (62.5%) |

## 6. Scoring intensity
- First-half goals: **171** (46.0%)
- Second-half goals: **201** (54.0%)
- Avg first-half goals per match: **1.379**
- Avg second-half goals per match: **1.621**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **25** (20.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 149 | 175 | 46.0% | 54.0% |
| 2026-2027 | 16 | 22 | 26 | 45.8% | 54.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `117` of `124` (94.4%)
- Goalless matches: `7`
- Min `1` | Max `89` | Mean `29.37` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 41 | 33.1% | 35.0% |
| 16-30 | 32 | 25.8% | 27.4% |
| 31-45 | 19 | 15.3% | 16.2% |
| 46-60 | 12 | 9.7% | 10.3% |
| 61-75 | 6 | 4.8% | 5.1% |
| 76-90 | 7 | 5.6% | 6.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wbelgium1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wbelgium1\charts\goals_analysis_avg_per_season.png)

