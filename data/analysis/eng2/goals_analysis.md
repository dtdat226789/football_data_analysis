# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:57:51+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 45 | 7.0% |
| 1 | 129 | 20.1% |
| 2 | 161 | 25.1% |
| 3 | 132 | 20.6% |
| 4 | 105 | 16.4% |
| 5 | 47 | 7.3% |
| 6 | 14 | 2.2% |
| 7 | 4 | 0.6% |
| 8 | 4 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1434 | 1.372 | 1.203 | 2.575 |
| 2026-2027 | 84 | 212 | 1.583 | 0.94 | 2.524 |

## 3. Home vs away goal share
- Home goals: **897** (54.5%)
- Away goals: **749** (45.5%)
- Home/away ratio: **1.198**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 764 | 670 | 1434 | 53.3% | 46.7% |
| 2026-2027 | 133 | 79 | 212 | 62.7% | 37.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **335** of `641` (52.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 292 | 52.4% |
| 2026-2027 | 84 | 43 | 51.2% |

## 5. Clean sheets
- Home clean sheets: **200** (31.2%)
- Away clean sheets: **151** (23.6%)
- Total clean sheets recorded: **351**
- Matches with at least one clean sheet: **306** (47.7%)
- Both teams kept clean sheets (0-0): **45**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 165 | 137 | 302 | 265 (47.6%) |
| 2026-2027 | 84 | 35 | 14 | 49 | 41 (48.8%) |

## 6. Scoring intensity
- First-half goals: **728** (44.2%)
- Second-half goals: **918** (55.8%)
- Avg first-half goals per match: **1.136**
- Avg second-half goals per match: **1.432**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **164** (25.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 635 | 799 | 44.3% | 55.7% |
| 2026-2027 | 84 | 93 | 119 | 43.9% | 56.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `596` of `641` (93.0%)
- Goalless matches: `45`
- Min `1` | Max `103` | Mean `33.36` | Median (p50) `28.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 189 | 29.5% | 31.7% |
| 16-30 | 125 | 19.5% | 21.0% |
| 31-45 | 99 | 15.4% | 16.6% |
| 46-60 | 82 | 12.8% | 13.8% |
| 61-75 | 60 | 9.4% | 10.1% |
| 76-90 | 27 | 4.2% | 4.5% |
| 91-120 | 14 | 2.2% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\eng2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\eng2\charts\goals_analysis_avg_per_season.png)

