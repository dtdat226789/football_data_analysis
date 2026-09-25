# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:48:11+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 47 | 8.2% |
| 1 | 115 | 20.0% |
| 2 | 128 | 22.3% |
| 3 | 133 | 23.1% |
| 4 | 78 | 13.6% |
| 5 | 42 | 7.3% |
| 6 | 23 | 4.0% |
| 7 | 5 | 0.9% |
| 8 | 3 | 0.5% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 1335 | 1.432 | 1.191 | 2.623 |
| 2026-2027 | 66 | 163 | 1.333 | 1.136 | 2.47 |

## 3. Home vs away goal share
- Home goals: **817** (54.5%)
- Away goals: **681** (45.5%)
- Home/away ratio: **1.2**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 729 | 606 | 1335 | 54.6% | 45.4% |
| 2026-2027 | 88 | 75 | 163 | 54.0% | 46.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **315** of `575` (54.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 509 | 286 | 56.2% |
| 2026-2027 | 66 | 29 | 43.9% |

## 5. Clean sheets
- Home clean sheets: **170** (29.6%)
- Away clean sheets: **137** (23.8%)
- Total clean sheets recorded: **307**
- Matches with at least one clean sheet: **260** (45.2%)
- Both teams kept clean sheets (0-0): **47**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 147 | 116 | 263 | 223 (43.8%) |
| 2026-2027 | 66 | 23 | 21 | 44 | 37 (56.1%) |

## 6. Scoring intensity
- First-half goals: **666** (44.5%)
- Second-half goals: **832** (55.5%)
- Avg first-half goals per match: **1.158**
- Avg second-half goals per match: **1.447**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **138** (24.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 509 | 593 | 742 | 44.4% | 55.6% |
| 2026-2027 | 66 | 73 | 90 | 44.8% | 55.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `528` of `575` (91.8%)
- Goalless matches: `47`
- Min `1` | Max `98` | Mean `31.36` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 180 | 31.3% | 34.1% |
| 16-30 | 123 | 21.4% | 23.3% |
| 31-45 | 81 | 14.1% | 15.3% |
| 46-60 | 74 | 12.9% | 14.0% |
| 61-75 | 35 | 6.1% | 6.6% |
| 76-90 | 25 | 4.3% | 4.7% |
| 91-120 | 10 | 1.7% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\spain2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\spain2\charts\goals_analysis_avg_per_season.png)

