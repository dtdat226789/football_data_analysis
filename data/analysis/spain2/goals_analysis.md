# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:09:04+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 47 | 8.0% |
| 1 | 117 | 20.0% |
| 2 | 133 | 22.7% |
| 3 | 133 | 22.7% |
| 4 | 80 | 13.7% |
| 5 | 44 | 7.5% |
| 6 | 23 | 3.9% |
| 7 | 5 | 0.9% |
| 8 | 3 | 0.5% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 1335 | 1.432 | 1.191 | 2.623 |
| 2026-2027 | 77 | 193 | 1.377 | 1.13 | 2.506 |

## 3. Home vs away goal share
- Home goals: **835** (54.6%)
- Away goals: **693** (45.4%)
- Home/away ratio: **1.205**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 729 | 606 | 1335 | 54.6% | 45.4% |
| 2026-2027 | 106 | 87 | 193 | 54.9% | 45.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **321** of `586` (54.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 509 | 286 | 56.2% |
| 2026-2027 | 77 | 35 | 45.5% |

## 5. Clean sheets
- Home clean sheets: **173** (29.5%)
- Away clean sheets: **139** (23.7%)
- Total clean sheets recorded: **312**
- Matches with at least one clean sheet: **265** (45.2%)
- Both teams kept clean sheets (0-0): **47**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 147 | 116 | 263 | 223 (43.8%) |
| 2026-2027 | 77 | 26 | 23 | 49 | 42 (54.5%) |

## 6. Scoring intensity
- First-half goals: **682** (44.6%)
- Second-half goals: **846** (55.4%)
- Avg first-half goals per match: **1.164**
- Avg second-half goals per match: **1.444**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **139** (23.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 593 | 742 | 44.4% | 55.6% |
| 2026-2027 | 77 | 89 | 104 | 46.1% | 53.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `539` of `586` (92.0%)
- Goalless matches: `47`
- Min `1` | Max `98` | Mean `31.12` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 186 | 31.7% | 34.5% |
| 16-30 | 125 | 21.3% | 23.2% |
| 31-45 | 83 | 14.2% | 15.4% |
| 46-60 | 75 | 12.8% | 13.9% |
| 61-75 | 35 | 6.0% | 6.5% |
| 76-90 | 25 | 4.3% | 4.6% |
| 91-120 | 10 | 1.7% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\spain2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\spain2\charts\goals_analysis_avg_per_season.png)

