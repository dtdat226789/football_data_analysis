# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:57:19+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 1 | 2.9% |
| 1 | 2 | 5.9% |
| 2 | 6 | 17.6% |
| 3 | 4 | 11.8% |
| 4 | 9 | 26.5% |
| 5 | 3 | 8.8% |
| 6 | 4 | 11.8% |
| 7 | 3 | 8.8% |
| 8 | 1 | 2.9% |
| 9 | 0 | 0.0% |
| 10 | 1 | 2.9% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2026-2027 | 34 | 140 | 2.294 | 1.824 | 4.118 |

## 3. Home vs away goal share
- Home goals: **78** (55.7%)
- Away goals: **62** (44.3%)
- Home/away ratio: **1.258**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2026-2027 | 78 | 62 | 140 | 55.7% | 44.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **23** of `34` (67.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2026-2027 | 34 | 23 | 67.6% |

## 5. Clean sheets
- Home clean sheets: **6** (17.6%)
- Away clean sheets: **6** (17.6%)
- Total clean sheets recorded: **12**
- Matches with at least one clean sheet: **11** (32.4%)
- Both teams kept clean sheets (0-0): **1**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2026-2027 | 34 | 6 | 6 | 12 | 11 (32.4%) |

## 6. Scoring intensity
- First-half goals: **72** (51.4%)
- Second-half goals: **68** (48.6%)
- Avg first-half goals per match: **2.118**
- Avg second-half goals per match: **2.0**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **3** (8.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2026-2027 | 34 | 72 | 68 | 51.4% | 48.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `33` of `34` (97.1%)
- Goalless matches: `1`
- Min `1` | Max `67` | Mean `22.7` | Median (p50) `19`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 12 | 35.3% | 36.4% |
| 16-30 | 13 | 38.2% | 39.4% |
| 31-45 | 5 | 14.7% | 15.2% |
| 46-60 | 1 | 2.9% | 3.0% |
| 61-75 | 2 | 5.9% | 6.1% |
| 76-90 | 0 | 0.0% | 0.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\develop21\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\develop21\charts\goals_analysis_avg_per_season.png)

