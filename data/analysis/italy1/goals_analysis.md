# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:56:29+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 36 | 8.4% |
| 1 | 87 | 20.2% |
| 2 | 106 | 24.7% |
| 3 | 103 | 24.0% |
| 4 | 52 | 12.1% |
| 5 | 32 | 7.4% |
| 6 | 9 | 2.1% |
| 7 | 3 | 0.7% |
| 8 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 922 | 1.276 | 1.15 | 2.426 |
| 2026-2027 | 50 | 145 | 1.48 | 1.42 | 2.9 |

## 3. Home vs away goal share
- Home goals: **559** (52.4%)
- Away goals: **508** (47.6%)
- Home/away ratio: **1.1**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 485 | 437 | 922 | 52.6% | 47.4% |
| 2026-2027 | 74 | 71 | 145 | 51.0% | 49.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **201** of `430` (46.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 172 | 45.3% |
| 2026-2027 | 50 | 29 | 58.0% |

## 5. Clean sheets
- Home clean sheets: **135** (31.4%)
- Away clean sheets: **130** (30.2%)
- Total clean sheets recorded: **265**
- Matches with at least one clean sheet: **229** (53.3%)
- Both teams kept clean sheets (0-0): **36**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 125 | 119 | 244 | 208 (54.7%) |
| 2026-2027 | 50 | 10 | 11 | 21 | 21 (42.0%) |

## 6. Scoring intensity
- First-half goals: **454** (42.5%)
- Second-half goals: **613** (57.5%)
- Avg first-half goals per match: **1.056**
- Avg second-half goals per match: **1.426**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **113** (26.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 396 | 526 | 43.0% | 57.0% |
| 2026-2027 | 50 | 58 | 87 | 40.0% | 60.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `394` of `430` (91.6%)
- Goalless matches: `36`
- Min `1` | Max `96` | Mean `32.47` | Median (p50) `26.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 128 | 29.8% | 32.5% |
| 16-30 | 88 | 20.5% | 22.3% |
| 31-45 | 58 | 13.5% | 14.7% |
| 46-60 | 55 | 12.8% | 14.0% |
| 61-75 | 39 | 9.1% | 9.9% |
| 76-90 | 21 | 4.9% | 5.3% |
| 91-120 | 5 | 1.2% | 1.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy1\charts\goals_analysis_avg_per_season.png)

