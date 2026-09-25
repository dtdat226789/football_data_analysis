# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:55:36+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 58 | 8.7% |
| 1 | 157 | 23.5% |
| 2 | 178 | 26.6% |
| 3 | 160 | 23.9% |
| 4 | 76 | 11.4% |
| 5 | 22 | 3.3% |
| 6 | 14 | 2.1% |
| 7 | 3 | 0.4% |
| 8 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 380 | 843 | 1.292 | 0.926 | 2.218 |
| 2026 | 289 | 677 | 1.336 | 1.007 | 2.343 |

## 3. Home vs away goal share
- Home goals: **877** (57.7%)
- Away goals: **643** (42.3%)
- Home/away ratio: **1.364**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 491 | 352 | 843 | 58.2% | 41.8% |
| 2026 | 386 | 291 | 677 | 57.0% | 43.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **328** of `669` (49.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 380 | 188 | 49.5% |
| 2026 | 289 | 140 | 48.4% |

## 5. Clean sheets
- Home clean sheets: **251** (37.5%)
- Away clean sheets: **148** (22.1%)
- Total clean sheets recorded: **399**
- Matches with at least one clean sheet: **341** (51.0%)
- Both teams kept clean sheets (0-0): **58**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 380 | 146 | 79 | 225 | 192 (50.5%) |
| 2026 | 289 | 105 | 69 | 174 | 149 (51.6%) |

## 6. Scoring intensity
- First-half goals: **681** (44.8%)
- Second-half goals: **839** (55.2%)
- Avg first-half goals per match: **1.018**
- Avg second-half goals per match: **1.254**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **172** (25.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 380 | 379 | 464 | 45.0% | 55.0% |
| 2026 | 289 | 302 | 375 | 44.6% | 55.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `611` of `669` (91.3%)
- Goalless matches: `58`
- Min `1` | Max `101` | Mean `34.78` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 168 | 25.1% | 27.5% |
| 16-30 | 151 | 22.6% | 24.7% |
| 31-45 | 98 | 14.6% | 16.0% |
| 46-60 | 82 | 12.3% | 13.4% |
| 61-75 | 60 | 9.0% | 9.8% |
| 76-90 | 34 | 5.1% | 5.6% |
| 91-120 | 18 | 2.7% | 2.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\brazil2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\brazil2\charts\goals_analysis_avg_per_season.png)

