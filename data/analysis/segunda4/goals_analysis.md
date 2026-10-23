# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:07:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 33 | 9.2% |
| 1 | 89 | 24.8% |
| 2 | 84 | 23.4% |
| 3 | 85 | 23.7% |
| 4 | 38 | 10.6% |
| 5 | 21 | 5.8% |
| 6 | 7 | 1.9% |
| 7 | 1 | 0.3% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 738 | 1.344 | 0.941 | 2.285 |
| 2026-2027 | 36 | 88 | 1.444 | 1.0 | 2.444 |

## 3. Home vs away goal share
- Home goals: **486** (58.8%)
- Away goals: **340** (41.2%)
- Home/away ratio: **1.429**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 434 | 304 | 738 | 58.8% | 41.2% |
| 2026-2027 | 52 | 36 | 88 | 59.1% | 40.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **179** of `359` (49.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 323 | 163 | 50.5% |
| 2026-2027 | 36 | 16 | 44.4% |

## 5. Clean sheets
- Home clean sheets: **136** (37.9%)
- Away clean sheets: **77** (21.4%)
- Total clean sheets recorded: **213**
- Matches with at least one clean sheet: **180** (50.1%)
- Both teams kept clean sheets (0-0): **33**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 122 | 66 | 188 | 160 (49.5%) |
| 2026-2027 | 36 | 14 | 11 | 25 | 20 (55.6%) |

## 6. Scoring intensity
- First-half goals: **352** (42.6%)
- Second-half goals: **474** (57.4%)
- Avg first-half goals per match: **0.981**
- Avg second-half goals per match: **1.32**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **98** (27.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 308 | 430 | 41.7% | 58.3% |
| 2026-2027 | 36 | 44 | 44 | 50.0% | 50.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `326` of `359` (90.8%)
- Goalless matches: `33`
- Min `1` | Max `97` | Mean `34.79` | Median (p50) `30.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 91 | 25.3% | 27.9% |
| 16-30 | 79 | 22.0% | 24.2% |
| 31-45 | 54 | 15.0% | 16.6% |
| 46-60 | 47 | 13.1% | 14.4% |
| 61-75 | 23 | 6.4% | 7.1% |
| 76-90 | 24 | 6.7% | 7.4% |
| 91-120 | 8 | 2.2% | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda4\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda4\charts\goals_analysis_avg_per_season.png)

