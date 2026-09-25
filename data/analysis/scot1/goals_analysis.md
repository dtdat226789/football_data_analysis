# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:44:50+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.1% |
| 1 | 36 | 15.7% |
| 2 | 63 | 27.4% |
| 3 | 53 | 23.0% |
| 4 | 41 | 17.8% |
| 5 | 16 | 7.0% |
| 6 | 3 | 1.3% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.4% |
| 9 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 191 | 511 | 1.429 | 1.246 | 2.675 |
| 2026-2027 | 39 | 103 | 1.667 | 0.974 | 2.641 |

## 3. Home vs away goal share
- Home goals: **338** (55.0%)
- Away goals: **276** (45.0%)
- Home/away ratio: **1.225**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 273 | 238 | 511 | 53.4% | 46.6% |
| 2026-2027 | 65 | 38 | 103 | 63.1% | 36.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **120** of `230` (52.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 191 | 103 | 53.9% |
| 2026-2027 | 39 | 17 | 43.6% |

## 5. Clean sheets
- Home clean sheets: **66** (28.7%)
- Away clean sheets: **58** (25.2%)
- Total clean sheets recorded: **124**
- Matches with at least one clean sheet: **110** (47.8%)
- Both teams kept clean sheets (0-0): **14**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 191 | 51 | 47 | 98 | 88 (46.1%) |
| 2026-2027 | 39 | 15 | 11 | 26 | 22 (56.4%) |

## 6. Scoring intensity
- First-half goals: **264** (43.0%)
- Second-half goals: **350** (57.0%)
- Avg first-half goals per match: **1.148**
- Avg second-half goals per match: **1.522**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **46** (20.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 191 | 225 | 286 | 44.0% | 56.0% |
| 2026-2027 | 39 | 39 | 64 | 37.9% | 62.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `216` of `230` (93.9%)
- Goalless matches: `14`
- Min `1` | Max `93` | Mean `30.02` | Median (p50) `24.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 74 | 32.2% | 34.3% |
| 16-30 | 51 | 22.2% | 23.6% |
| 31-45 | 41 | 17.8% | 19.0% |
| 46-60 | 24 | 10.4% | 11.1% |
| 61-75 | 17 | 7.4% | 7.9% |
| 76-90 | 8 | 3.5% | 3.7% |
| 91-120 | 1 | 0.4% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\scot1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\scot1\charts\goals_analysis_avg_per_season.png)

