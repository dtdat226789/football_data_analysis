# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:56:47+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 12 | 3.7% |
| 1 | 37 | 11.3% |
| 2 | 75 | 23.0% |
| 3 | 69 | 21.2% |
| 4 | 52 | 16.0% |
| 5 | 42 | 12.9% |
| 6 | 20 | 6.1% |
| 7 | 10 | 3.1% |
| 8 | 6 | 1.8% |
| 9 | 2 | 0.6% |
| 10 | 0 | 0.0% |
| 11 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 912 | 1.82 | 1.533 | 3.353 |
| 2026-2027 | 54 | 167 | 1.722 | 1.37 | 3.093 |

## 3. Home vs away goal share
- Home goals: **588** (54.5%)
- Away goals: **491** (45.5%)
- Home/away ratio: **1.198**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 495 | 417 | 912 | 54.3% | 45.7% |
| 2026-2027 | 93 | 74 | 167 | 55.7% | 44.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **186** of `326` (57.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 272 | 158 | 58.1% |
| 2026-2027 | 54 | 28 | 51.9% |

## 5. Clean sheets
- Home clean sheets: **89** (27.3%)
- Away clean sheets: **63** (19.3%)
- Total clean sheets recorded: **152**
- Matches with at least one clean sheet: **140** (42.9%)
- Both teams kept clean sheets (0-0): **12**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 73 | 48 | 121 | 114 (41.9%) |
| 2026-2027 | 54 | 16 | 15 | 31 | 26 (48.1%) |

## 6. Scoring intensity
- First-half goals: **511** (47.4%)
- Second-half goals: **568** (52.6%)
- Avg first-half goals per match: **1.567**
- Avg second-half goals per match: **1.742**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **49** (15.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 434 | 478 | 47.6% | 52.4% |
| 2026-2027 | 54 | 77 | 90 | 46.1% | 53.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `314` of `326` (96.3%)
- Goalless matches: `12`
- Min `1` | Max `91` | Mean `25.77` | Median (p50) `21.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 121 | 37.1% | 38.5% |
| 16-30 | 86 | 26.4% | 27.4% |
| 31-45 | 56 | 17.2% | 17.8% |
| 46-60 | 33 | 10.1% | 10.5% |
| 61-75 | 8 | 2.5% | 2.5% |
| 76-90 | 9 | 2.8% | 2.9% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech3b\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech3b\charts\goals_analysis_avg_per_season.png)

