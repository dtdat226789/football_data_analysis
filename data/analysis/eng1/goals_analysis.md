# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:57:39+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 41 | 6.4% |
| 1 | 130 | 20.3% |
| 2 | 141 | 22.0% |
| 3 | 146 | 22.8% |
| 4 | 102 | 15.9% |
| 5 | 48 | 7.5% |
| 6 | 21 | 3.3% |
| 7 | 9 | 1.4% |
| 8 | 0 | 0.0% |
| 9 | 2 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1462 | 1.478 | 1.147 | 2.625 |
| 2026-2027 | 83 | 243 | 1.554 | 1.373 | 2.928 |

## 3. Home vs away goal share
- Home goals: **952** (55.8%)
- Away goals: **753** (44.2%)
- Home/away ratio: **1.264**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 823 | 639 | 1462 | 56.3% | 43.7% |
| 2026-2027 | 129 | 114 | 243 | 53.1% | 46.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **341** of `640` (53.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 291 | 52.2% |
| 2026-2027 | 83 | 50 | 60.2% |

## 5. Clean sheets
- Home clean sheets: **197** (30.8%)
- Away clean sheets: **143** (22.3%)
- Total clean sheets recorded: **340**
- Matches with at least one clean sheet: **299** (46.7%)
- Both teams kept clean sheets (0-0): **41**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 175 | 124 | 299 | 266 (47.8%) |
| 2026-2027 | 83 | 22 | 19 | 41 | 33 (39.8%) |

## 6. Scoring intensity
- First-half goals: **739** (43.3%)
- Second-half goals: **966** (56.7%)
- Avg first-half goals per match: **1.155**
- Avg second-half goals per match: **1.509**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **155** (24.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 639 | 823 | 43.7% | 56.3% |
| 2026-2027 | 83 | 100 | 143 | 41.2% | 58.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `599` of `640` (93.6%)
- Goalless matches: `41`
- Min `1` | Max `99` | Mean `31.74` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 196 | 30.6% | 32.7% |
| 16-30 | 139 | 21.7% | 23.2% |
| 31-45 | 100 | 15.6% | 16.7% |
| 46-60 | 79 | 12.3% | 13.2% |
| 61-75 | 47 | 7.3% | 7.8% |
| 76-90 | 28 | 4.4% | 4.7% |
| 91-120 | 10 | 1.6% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\eng1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\eng1\charts\goals_analysis_avg_per_season.png)

