# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:48:46+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 41 | 6.4% |
| 1 | 132 | 20.5% |
| 2 | 142 | 22.0% |
| 3 | 146 | 22.7% |
| 4 | 103 | 16.0% |
| 5 | 48 | 7.5% |
| 6 | 21 | 3.3% |
| 7 | 9 | 1.4% |
| 8 | 0 | 0.0% |
| 9 | 2 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1462 | 1.478 | 1.147 | 2.625 |
| 2026-2027 | 87 | 251 | 1.529 | 1.356 | 2.885 |

## 3. Home vs away goal share
- Home goals: **956** (55.8%)
- Away goals: **757** (44.2%)
- Home/away ratio: **1.263**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 823 | 639 | 1462 | 56.3% | 43.7% |
| 2026-2027 | 133 | 118 | 251 | 53.0% | 47.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **343** of `644` (53.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 291 | 52.2% |
| 2026-2027 | 87 | 52 | 59.8% |

## 5. Clean sheets
- Home clean sheets: **198** (30.7%)
- Away clean sheets: **144** (22.4%)
- Total clean sheets recorded: **342**
- Matches with at least one clean sheet: **301** (46.7%)
- Both teams kept clean sheets (0-0): **41**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 175 | 124 | 299 | 266 (47.8%) |
| 2026-2027 | 87 | 23 | 20 | 43 | 35 (40.2%) |

## 6. Scoring intensity
- First-half goals: **740** (43.2%)
- Second-half goals: **973** (56.8%)
- Avg first-half goals per match: **1.149**
- Avg second-half goals per match: **1.511**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **158** (24.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 639 | 823 | 43.7% | 56.3% |
| 2026-2027 | 87 | 101 | 150 | 40.2% | 59.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `603` of `644` (93.6%)
- Goalless matches: `41`
- Min `1` | Max `99` | Mean `31.85` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 196 | 30.4% | 32.5% |
| 16-30 | 140 | 21.7% | 23.2% |
| 31-45 | 100 | 15.5% | 16.6% |
| 46-60 | 81 | 12.6% | 13.4% |
| 61-75 | 48 | 7.5% | 8.0% |
| 76-90 | 28 | 4.3% | 4.6% |
| 91-120 | 10 | 1.6% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\eng1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\eng1\charts\goals_analysis_avg_per_season.png)

