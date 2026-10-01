# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:00:53+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 8 | 6.9% |
| 1 | 22 | 19.0% |
| 2 | 31 | 26.7% |
| 3 | 23 | 19.8% |
| 4 | 12 | 10.3% |
| 5 | 12 | 10.3% |
| 6 | 7 | 6.0% |
| 7 | 0 | 0.0% |
| 8 | 1 | 0.9% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 98 | 257 | 1.48 | 1.143 | 2.622 |
| 2026-2027 | 18 | 54 | 1.611 | 1.389 | 3.0 |

## 3. Home vs away goal share
- Home goals: **174** (55.9%)
- Away goals: **137** (44.1%)
- Home/away ratio: **1.27**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 145 | 112 | 257 | 56.4% | 43.6% |
| 2026-2027 | 29 | 25 | 54 | 53.7% | 46.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **58** of `116` (50.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 98 | 47 | 48.0% |
| 2026-2027 | 18 | 11 | 61.1% |

## 5. Clean sheets
- Home clean sheets: **34** (29.3%)
- Away clean sheets: **32** (27.6%)
- Total clean sheets recorded: **66**
- Matches with at least one clean sheet: **58** (50.0%)
- Both teams kept clean sheets (0-0): **8**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 98 | 29 | 29 | 58 | 51 (52.0%) |
| 2026-2027 | 18 | 5 | 3 | 8 | 7 (38.9%) |

## 6. Scoring intensity
- First-half goals: **135** (43.4%)
- Second-half goals: **176** (56.6%)
- Avg first-half goals per match: **1.164**
- Avg second-half goals per match: **1.517**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **26** (22.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 98 | 112 | 145 | 43.6% | 56.4% |
| 2026-2027 | 18 | 23 | 31 | 42.6% | 57.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `108` of `116` (93.1%)
- Goalless matches: `8`
- Min `1` | Max `96` | Mean `33.19` | Median (p50) `30.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 30 | 25.9% | 27.8% |
| 16-30 | 26 | 22.4% | 24.1% |
| 31-45 | 21 | 18.1% | 19.4% |
| 46-60 | 19 | 16.4% | 17.6% |
| 61-75 | 7 | 6.0% | 6.5% |
| 76-90 | 4 | 3.4% | 3.7% |
| 91-120 | 1 | 0.9% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\kuwait\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\kuwait\charts\goals_analysis_avg_per_season.png)

