# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:46:35+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.4% |
| 1 | 55 | 16.2% |
| 2 | 79 | 23.3% |
| 3 | 89 | 26.3% |
| 4 | 45 | 13.3% |
| 5 | 28 | 8.3% |
| 6 | 5 | 1.5% |
| 7 | 6 | 1.8% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 783 | 1.458 | 1.101 | 2.559 |
| 2026-2027 | 33 | 89 | 1.515 | 1.182 | 2.697 |

## 3. Home vs away goal share
- Home goals: **496** (56.9%)
- Away goals: **376** (43.1%)
- Home/away ratio: **1.319**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 446 | 337 | 783 | 57.0% | 43.0% |
| 2026-2027 | 50 | 39 | 89 | 56.2% | 43.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **171** of `339` (50.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 155 | 50.7% |
| 2026-2027 | 33 | 16 | 48.5% |

## 5. Clean sheets
- Home clean sheets: **116** (34.2%)
- Away clean sheets: **84** (24.8%)
- Total clean sheets recorded: **200**
- Matches with at least one clean sheet: **168** (49.6%)
- Both teams kept clean sheets (0-0): **32**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 103 | 75 | 178 | 151 (49.3%) |
| 2026-2027 | 33 | 13 | 9 | 22 | 17 (51.5%) |

## 6. Scoring intensity
- First-half goals: **370** (42.4%)
- Second-half goals: **502** (57.6%)
- Avg first-half goals per match: **1.091**
- Avg second-half goals per match: **1.481**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **79** (23.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 338 | 445 | 43.2% | 56.8% |
| 2026-2027 | 33 | 32 | 57 | 36.0% | 64.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `307` of `339` (90.6%)
- Goalless matches: `32`
- Min `1` | Max `93` | Mean `31.38` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 98 | 28.9% | 31.9% |
| 16-30 | 78 | 23.0% | 25.4% |
| 31-45 | 51 | 15.0% | 16.6% |
| 46-60 | 34 | 10.0% | 11.1% |
| 61-75 | 26 | 7.7% | 8.5% |
| 76-90 | 17 | 5.0% | 5.5% |
| 91-120 | 3 | 0.9% | 1.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda5\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda5\charts\goals_analysis_avg_per_season.png)

