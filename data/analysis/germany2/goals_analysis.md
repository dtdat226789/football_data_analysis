# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:59:35+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.2% |
| 1 | 56 | 15.4% |
| 2 | 76 | 20.9% |
| 3 | 96 | 26.4% |
| 4 | 53 | 14.6% |
| 5 | 33 | 9.1% |
| 6 | 16 | 4.4% |
| 7 | 9 | 2.5% |
| 8 | 4 | 1.1% |
| 9 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 903 | 1.626 | 1.287 | 2.913 |
| 2026-2027 | 54 | 179 | 1.741 | 1.574 | 3.315 |

## 3. Home vs away goal share
- Home goals: **598** (55.3%)
- Away goals: **484** (44.7%)
- Home/away ratio: **1.236**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 504 | 399 | 903 | 55.8% | 44.2% |
| 2026-2027 | 94 | 85 | 179 | 52.5% | 47.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **217** of `364` (59.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 310 | 183 | 59.0% |
| 2026-2027 | 54 | 34 | 63.0% |

## 5. Clean sheets
- Home clean sheets: **96** (26.4%)
- Away clean sheets: **70** (19.2%)
- Total clean sheets recorded: **166**
- Matches with at least one clean sheet: **147** (40.4%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 85 | 59 | 144 | 127 (41.0%) |
| 2026-2027 | 54 | 11 | 11 | 22 | 20 (37.0%) |

## 6. Scoring intensity
- First-half goals: **494** (45.7%)
- Second-half goals: **588** (54.3%)
- Avg first-half goals per match: **1.357**
- Avg second-half goals per match: **1.615**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **83** (22.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 403 | 500 | 44.6% | 55.4% |
| 2026-2027 | 54 | 91 | 88 | 50.8% | 49.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `345` of `364` (94.8%)
- Goalless matches: `19`
- Min `1` | Max `96` | Mean `30.92` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 121 | 33.2% | 35.1% |
| 16-30 | 73 | 20.1% | 21.2% |
| 31-45 | 59 | 16.2% | 17.1% |
| 46-60 | 42 | 11.5% | 12.2% |
| 61-75 | 32 | 8.8% | 9.3% |
| 76-90 | 14 | 3.8% | 4.1% |
| 91-120 | 4 | 1.1% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\germany2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\germany2\charts\goals_analysis_avg_per_season.png)

