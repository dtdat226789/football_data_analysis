# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:50:16+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 34 | 7.3% |
| 1 | 65 | 14.0% |
| 2 | 123 | 26.5% |
| 3 | 94 | 20.2% |
| 4 | 67 | 14.4% |
| 5 | 47 | 10.1% |
| 6 | 17 | 3.7% |
| 7 | 14 | 3.0% |
| 8 | 0 | 0.0% |
| 9 | 4 | 0.9% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 385 | 1125 | 1.673 | 1.249 | 2.922 |
| 2026-2027 | 80 | 207 | 1.462 | 1.125 | 2.587 |

## 3. Home vs away goal share
- Home goals: **761** (57.1%)
- Away goals: **571** (42.9%)
- Home/away ratio: **1.333**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 644 | 481 | 1125 | 57.2% | 42.8% |
| 2026-2027 | 117 | 90 | 207 | 56.5% | 43.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **235** of `465` (50.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 385 | 193 | 50.1% |
| 2026-2027 | 80 | 42 | 52.5% |

## 5. Clean sheets
- Home clean sheets: **159** (34.2%)
- Away clean sheets: **105** (22.6%)
- Total clean sheets recorded: **264**
- Matches with at least one clean sheet: **230** (49.5%)
- Both teams kept clean sheets (0-0): **34**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 385 | 135 | 85 | 220 | 192 (49.9%) |
| 2026-2027 | 80 | 24 | 20 | 44 | 38 (47.5%) |

## 6. Scoring intensity
- First-half goals: **593** (44.6%)
- Second-half goals: **736** (55.4%)
- Avg first-half goals per match: **1.278**
- Avg second-half goals per match: **1.586**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **98** (21.1%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 385 | 491 | 631 | 43.8% | 56.2% |
| 2026-2027 | 80 | 102 | 105 | 49.3% | 50.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `430` of `465` (92.5%)
- Goalless matches: `35`
- Min `1` | Max `94` | Mean `30.48` | Median (p50) `26.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 140 | 30.1% | 32.6% |
| 16-30 | 104 | 22.4% | 24.2% |
| 31-45 | 74 | 15.9% | 17.2% |
| 46-60 | 64 | 13.8% | 14.9% |
| 61-75 | 29 | 6.2% | 6.7% |
| 76-90 | 17 | 3.7% | 4.0% |
| 91-120 | 2 | 0.4% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\turkey2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\turkey2\charts\goals_analysis_avg_per_season.png)

