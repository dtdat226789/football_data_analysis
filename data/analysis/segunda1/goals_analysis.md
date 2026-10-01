# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:06:46+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.5% |
| 1 | 74 | 21.6% |
| 2 | 72 | 21.1% |
| 3 | 83 | 24.3% |
| 4 | 43 | 12.6% |
| 5 | 21 | 6.1% |
| 6 | 10 | 2.9% |
| 7 | 8 | 2.3% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 776 | 1.392 | 1.144 | 2.536 |
| 2026-2027 | 36 | 101 | 1.389 | 1.417 | 2.806 |

## 3. Home vs away goal share
- Home goals: **476** (54.3%)
- Away goals: **401** (45.7%)
- Home/away ratio: **1.187**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 426 | 350 | 776 | 54.9% | 45.1% |
| 2026-2027 | 50 | 51 | 101 | 49.5% | 50.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **173** of `342` (50.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 156 | 51.0% |
| 2026-2027 | 36 | 17 | 47.2% |

## 5. Clean sheets
- Home clean sheets: **109** (31.9%)
- Away clean sheets: **89** (26.0%)
- Total clean sheets recorded: **198**
- Matches with at least one clean sheet: **169** (49.4%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 100 | 78 | 178 | 150 (49.0%) |
| 2026-2027 | 36 | 9 | 11 | 20 | 19 (52.8%) |

## 6. Scoring intensity
- First-half goals: **386** (44.2%)
- Second-half goals: **488** (55.8%)
- Avg first-half goals per match: **1.132**
- Avg second-half goals per match: **1.431**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **83** (24.3%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 340 | 433 | 44.0% | 56.0% |
| 2026-2027 | 36 | 46 | 55 | 45.5% | 54.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `312` of `342` (91.2%)
- Goalless matches: `30`
- Min `1` | Max `96` | Mean `32.2` | Median (p50) `28.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 111 | 32.5% | 35.6% |
| 16-30 | 60 | 17.5% | 19.2% |
| 31-45 | 57 | 16.7% | 18.3% |
| 46-60 | 38 | 11.1% | 12.2% |
| 61-75 | 24 | 7.0% | 7.7% |
| 76-90 | 13 | 3.8% | 4.2% |
| 91-120 | 9 | 2.6% | 2.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda1\charts\goals_analysis_avg_per_season.png)

