# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:56:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.2% |
| 1 | 73 | 16.9% |
| 2 | 103 | 23.8% |
| 3 | 94 | 21.8% |
| 4 | 64 | 14.8% |
| 5 | 30 | 6.9% |
| 6 | 23 | 5.3% |
| 7 | 7 | 1.6% |
| 8 | 5 | 1.2% |
| 9 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 382 | 1051 | 1.497 | 1.254 | 2.751 |
| 2026-2027 | 50 | 161 | 1.62 | 1.6 | 3.22 |

## 3. Home vs away goal share
- Home goals: **653** (53.9%)
- Away goals: **559** (46.1%)
- Home/away ratio: **1.168**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 572 | 479 | 1051 | 54.4% | 45.6% |
| 2026-2027 | 81 | 80 | 161 | 50.3% | 49.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **257** of `432` (59.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 382 | 224 | 58.6% |
| 2026-2027 | 50 | 33 | 66.0% |

## 5. Clean sheets
- Home clean sheets: **108** (25.0%)
- Away clean sheets: **98** (22.7%)
- Total clean sheets recorded: **206**
- Matches with at least one clean sheet: **175** (40.5%)
- Both teams kept clean sheets (0-0): **31**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 382 | 102 | 85 | 187 | 158 (41.4%) |
| 2026-2027 | 50 | 6 | 13 | 19 | 17 (34.0%) |

## 6. Scoring intensity
- First-half goals: **549** (45.6%)
- Second-half goals: **655** (54.4%)
- Avg first-half goals per match: **1.28**
- Avg second-half goals per match: **1.527**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **96** (22.2%)
- *3 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 382 | 463 | 580 | 44.4% | 55.6% |
| 2026-2027 | 50 | 86 | 75 | 53.4% | 46.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `392` of `432` (90.7%)
- Goalless matches: `40`
- Min `1` | Max `91` | Mean `28.06` | Median (p50) `21.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 158 | 36.6% | 40.3% |
| 16-30 | 81 | 18.8% | 20.7% |
| 31-45 | 65 | 15.0% | 16.6% |
| 46-60 | 40 | 9.3% | 10.2% |
| 61-75 | 23 | 5.3% | 5.9% |
| 76-90 | 21 | 4.9% | 5.4% |
| 91-120 | 4 | 0.9% | 1.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy19\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy19\charts\goals_analysis_avg_per_season.png)

