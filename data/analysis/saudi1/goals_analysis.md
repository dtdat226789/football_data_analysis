# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:43:42+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Saudi Professional League (Saudi Arabia)
- Scope: league `saudi1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 26 | 6.9% |
| 1 | 54 | 14.3% |
| 2 | 86 | 22.8% |
| 3 | 73 | 19.4% |
| 4 | 63 | 16.7% |
| 5 | 43 | 11.4% |
| 6 | 21 | 5.6% |
| 7 | 9 | 2.4% |
| 8 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 314 | 943 | 1.592 | 1.411 | 3.003 |
| 2026-2027 | 63 | 174 | 1.397 | 1.365 | 2.762 |

## 3. Home vs away goal share
- Home goals: **588** (52.6%)
- Away goals: **529** (47.4%)
- Home/away ratio: **1.112**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 500 | 443 | 943 | 53.0% | 47.0% |
| 2026-2027 | 88 | 86 | 174 | 50.6% | 49.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **213** of `377` (56.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 314 | 182 | 58.0% |
| 2026-2027 | 63 | 31 | 49.2% |

## 5. Clean sheets
- Home clean sheets: **105** (27.9%)
- Away clean sheets: **85** (22.5%)
- Total clean sheets recorded: **190**
- Matches with at least one clean sheet: **164** (43.5%)
- Both teams kept clean sheets (0-0): **26**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 314 | 87 | 61 | 148 | 132 (42.0%) |
| 2026-2027 | 63 | 18 | 24 | 42 | 32 (50.8%) |

## 6. Scoring intensity
- First-half goals: **511** (45.7%)
- Second-half goals: **606** (54.3%)
- Avg first-half goals per match: **1.355**
- Avg second-half goals per match: **1.607**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **71** (18.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 314 | 416 | 527 | 44.1% | 55.9% |
| 2026-2027 | 63 | 95 | 79 | 54.6% | 45.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `351` of `377` (93.1%)
- Goalless matches: `26`
- Min `1` | Max `96` | Mean `28.23` | Median (p50) `22`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 132 | 35.0% | 37.6% |
| 16-30 | 85 | 22.5% | 24.2% |
| 31-45 | 55 | 14.6% | 15.7% |
| 46-60 | 48 | 12.7% | 13.7% |
| 61-75 | 14 | 3.7% | 4.0% |
| 76-90 | 12 | 3.2% | 3.4% |
| 91-120 | 5 | 1.3% | 1.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\saudi1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\saudi1\charts\goals_analysis_avg_per_season.png)

