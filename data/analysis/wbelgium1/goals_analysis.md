# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:50:34+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 7 | 5.8% |
| 1 | 11 | 9.2% |
| 2 | 35 | 29.2% |
| 3 | 29 | 24.2% |
| 4 | 14 | 11.7% |
| 5 | 12 | 10.0% |
| 6 | 9 | 7.5% |
| 7 | 3 | 2.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 324 | 1.491 | 1.509 | 3.0 |
| 2026-2027 | 12 | 35 | 1.833 | 1.083 | 2.917 |

## 3. Home vs away goal share
- Home goals: **183** (51.0%)
- Away goals: **176** (49.0%)
- Home/away ratio: **1.04**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 161 | 163 | 324 | 49.7% | 50.3% |
| 2026-2027 | 22 | 13 | 35 | 62.9% | 37.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **67** of `120` (55.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 108 | 63 | 58.3% |
| 2026-2027 | 12 | 4 | 33.3% |

## 5. Clean sheets
- Home clean sheets: **34** (28.3%)
- Away clean sheets: **26** (21.7%)
- Total clean sheets recorded: **60**
- Matches with at least one clean sheet: **53** (44.2%)
- Both teams kept clean sheets (0-0): **7**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 28 | 23 | 51 | 45 (41.7%) |
| 2026-2027 | 12 | 6 | 3 | 9 | 8 (66.7%) |

## 6. Scoring intensity
- First-half goals: **168** (46.8%)
- Second-half goals: **191** (53.2%)
- Avg first-half goals per match: **1.4**
- Avg second-half goals per match: **1.592**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **22** (18.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 108 | 149 | 175 | 46.0% | 54.0% |
| 2026-2027 | 12 | 19 | 16 | 54.3% | 45.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `113` of `120` (94.2%)
- Goalless matches: `7`
- Min `1` | Max `89` | Mean `28.28` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 41 | 34.2% | 36.3% |
| 16-30 | 31 | 25.8% | 27.4% |
| 31-45 | 19 | 15.8% | 16.8% |
| 46-60 | 12 | 10.0% | 10.6% |
| 61-75 | 4 | 3.3% | 3.5% |
| 76-90 | 6 | 5.0% | 5.3% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wbelgium1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wbelgium1\charts\goals_analysis_avg_per_season.png)

