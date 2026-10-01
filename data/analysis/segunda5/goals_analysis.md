# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:07:48+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.2% |
| 1 | 58 | 16.7% |
| 2 | 81 | 23.3% |
| 3 | 91 | 26.1% |
| 4 | 47 | 13.5% |
| 5 | 28 | 8.0% |
| 6 | 5 | 1.4% |
| 7 | 6 | 1.7% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 783 | 1.458 | 1.101 | 2.559 |
| 2026-2027 | 42 | 110 | 1.548 | 1.071 | 2.619 |

## 3. Home vs away goal share
- Home goals: **511** (57.2%)
- Away goals: **382** (42.8%)
- Home/away ratio: **1.338**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 446 | 337 | 783 | 57.0% | 43.0% |
| 2026-2027 | 65 | 45 | 110 | 59.1% | 40.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **174** of `348` (50.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 155 | 50.7% |
| 2026-2027 | 42 | 19 | 45.2% |

## 5. Clean sheets
- Home clean sheets: **122** (35.1%)
- Away clean sheets: **84** (24.1%)
- Total clean sheets recorded: **206**
- Matches with at least one clean sheet: **174** (50.0%)
- Both teams kept clean sheets (0-0): **32**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 103 | 75 | 178 | 151 (49.3%) |
| 2026-2027 | 42 | 19 | 9 | 28 | 23 (54.8%) |

## 6. Scoring intensity
- First-half goals: **377** (42.2%)
- Second-half goals: **516** (57.8%)
- Avg first-half goals per match: **1.083**
- Avg second-half goals per match: **1.483**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **83** (23.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 338 | 445 | 43.2% | 56.8% |
| 2026-2027 | 42 | 39 | 71 | 35.5% | 64.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `316` of `348` (90.8%)
- Goalless matches: `32`
- Min `1` | Max `93` | Mean `31.78` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 99 | 28.4% | 31.3% |
| 16-30 | 79 | 22.7% | 25.0% |
| 31-45 | 54 | 15.5% | 17.1% |
| 46-60 | 35 | 10.1% | 11.1% |
| 61-75 | 29 | 8.3% | 9.2% |
| 76-90 | 17 | 4.9% | 5.4% |
| 91-120 | 3 | 0.9% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda5\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda5\charts\goals_analysis_avg_per_season.png)

