# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:46:17+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 31 | 8.9% |
| 1 | 87 | 24.9% |
| 2 | 83 | 23.7% |
| 3 | 83 | 23.7% |
| 4 | 37 | 10.6% |
| 5 | 21 | 6.0% |
| 6 | 7 | 2.0% |
| 7 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 738 | 1.344 | 0.941 | 2.285 |
| 2026-2027 | 27 | 66 | 1.333 | 1.111 | 2.444 |

## 3. Home vs away goal share
- Home goals: **470** (58.5%)
- Away goals: **334** (41.5%)
- Home/away ratio: **1.407**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 434 | 304 | 738 | 58.8% | 41.2% |
| 2026-2027 | 36 | 30 | 66 | 54.5% | 45.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **177** of `350` (50.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 323 | 163 | 50.5% |
| 2026-2027 | 27 | 14 | 51.9% |

## 5. Clean sheets
- Home clean sheets: **130** (37.1%)
- Away clean sheets: **74** (21.1%)
- Total clean sheets recorded: **204**
- Matches with at least one clean sheet: **173** (49.4%)
- Both teams kept clean sheets (0-0): **31**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 122 | 66 | 188 | 160 (49.5%) |
| 2026-2027 | 27 | 8 | 8 | 16 | 13 (48.1%) |

## 6. Scoring intensity
- First-half goals: **338** (42.0%)
- Second-half goals: **466** (58.0%)
- Avg first-half goals per match: **0.966**
- Avg second-half goals per match: **1.331**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **97** (27.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 323 | 308 | 430 | 41.7% | 58.3% |
| 2026-2027 | 27 | 30 | 36 | 45.5% | 54.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `319` of `350` (91.1%)
- Goalless matches: `31`
- Min `1` | Max `97` | Mean `34.94` | Median (p50) `30`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 86 | 24.6% | 27.0% |
| 16-30 | 78 | 22.3% | 24.5% |
| 31-45 | 55 | 15.7% | 17.2% |
| 46-60 | 47 | 13.4% | 14.7% |
| 61-75 | 22 | 6.3% | 6.9% |
| 76-90 | 24 | 6.9% | 7.5% |
| 91-120 | 7 | 2.0% | 2.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda4\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda4\charts\goals_analysis_avg_per_season.png)

