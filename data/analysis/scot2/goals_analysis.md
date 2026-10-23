# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:06:31+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 9 | 3.9% |
| 1 | 27 | 11.8% |
| 2 | 60 | 26.3% |
| 3 | 50 | 21.9% |
| 4 | 43 | 18.9% |
| 5 | 20 | 8.8% |
| 6 | 14 | 6.1% |
| 7 | 4 | 1.8% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 188 | 552 | 1.537 | 1.399 | 2.936 |
| 2026-2027 | 40 | 139 | 2.075 | 1.4 | 3.475 |

## 3. Home vs away goal share
- Home goals: **372** (53.8%)
- Away goals: **319** (46.2%)
- Home/away ratio: **1.166**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 289 | 263 | 552 | 52.4% | 47.6% |
| 2026-2027 | 83 | 56 | 139 | 59.7% | 40.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **138** of `228` (60.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 188 | 116 | 61.7% |
| 2026-2027 | 40 | 22 | 55.0% |

## 5. Clean sheets
- Home clean sheets: **62** (27.2%)
- Away clean sheets: **37** (16.2%)
- Total clean sheets recorded: **99**
- Matches with at least one clean sheet: **90** (39.5%)
- Both teams kept clean sheets (0-0): **9**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 188 | 49 | 32 | 81 | 72 (38.3%) |
| 2026-2027 | 40 | 13 | 5 | 18 | 18 (45.0%) |

## 6. Scoring intensity
- First-half goals: **335** (48.5%)
- Second-half goals: **356** (51.5%)
- Avg first-half goals per match: **1.469**
- Avg second-half goals per match: **1.561**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **44** (19.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 188 | 271 | 281 | 49.1% | 50.9% |
| 2026-2027 | 40 | 64 | 75 | 46.0% | 54.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `219` of `228` (96.1%)
- Goalless matches: `9`
- Min `1` | Max `89` | Mean `29.22` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 70 | 30.7% | 32.0% |
| 16-30 | 60 | 26.3% | 27.4% |
| 31-45 | 41 | 18.0% | 18.7% |
| 46-60 | 24 | 10.5% | 11.0% |
| 61-75 | 17 | 7.5% | 7.8% |
| 76-90 | 7 | 3.1% | 3.2% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\scot2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\scot2\charts\goals_analysis_avg_per_season.png)

