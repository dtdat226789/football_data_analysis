# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:54:31+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 17 | 5.6% |
| 1 | 62 | 20.6% |
| 2 | 82 | 27.2% |
| 3 | 69 | 22.9% |
| 4 | 38 | 12.6% |
| 5 | 17 | 5.6% |
| 6 | 9 | 3.0% |
| 7 | 6 | 2.0% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 602 | 1.342 | 1.167 | 2.508 |
| 2026-2027 | 61 | 172 | 1.705 | 1.115 | 2.82 |

## 3. Home vs away goal share
- Home goals: **426** (55.0%)
- Away goals: **348** (45.0%)
- Home/away ratio: **1.224**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 280 | 602 | 53.5% | 46.5% |
| 2026-2027 | 104 | 68 | 172 | 60.5% | 39.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **149** of `301` (49.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 240 | 116 | 48.3% |
| 2026-2027 | 61 | 33 | 54.1% |

## 5. Clean sheets
- Home clean sheets: **92** (30.6%)
- Away clean sheets: **77** (25.6%)
- Total clean sheets recorded: **169**
- Matches with at least one clean sheet: **152** (50.5%)
- Both teams kept clean sheets (0-0): **17**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 72 | 67 | 139 | 124 (51.7%) |
| 2026-2027 | 61 | 20 | 10 | 30 | 28 (45.9%) |

## 6. Scoring intensity
- First-half goals: **347** (44.8%)
- Second-half goals: **427** (55.2%)
- Avg first-half goals per match: **1.153**
- Avg second-half goals per match: **1.419**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **72** (23.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 267 | 335 | 44.4% | 55.6% |
| 2026-2027 | 61 | 80 | 92 | 46.5% | 53.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `284` of `301` (94.4%)
- Goalless matches: `17`
- Min `1` | Max `93` | Mean `31.85` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 95 | 31.6% | 33.5% |
| 16-30 | 62 | 20.6% | 21.8% |
| 31-45 | 53 | 17.6% | 18.7% |
| 46-60 | 34 | 11.3% | 12.0% |
| 61-75 | 17 | 5.6% | 6.0% |
| 76-90 | 21 | 7.0% | 7.4% |
| 91-120 | 2 | 0.7% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\hungary2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\hungary2\charts\goals_analysis_avg_per_season.png)

