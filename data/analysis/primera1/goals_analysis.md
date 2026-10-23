# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:04:16+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 42 | 9.4% |
| 1 | 92 | 20.5% |
| 2 | 114 | 25.4% |
| 3 | 94 | 21.0% |
| 4 | 55 | 12.3% |
| 5 | 31 | 6.9% |
| 6 | 13 | 2.9% |
| 7 | 5 | 1.1% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 974 | 1.392 | 1.055 | 2.447 |
| 2026-2027 | 50 | 133 | 1.46 | 1.2 | 2.66 |

## 3. Home vs away goal share
- Home goals: **627** (56.6%)
- Away goals: **480** (43.4%)
- Home/away ratio: **1.306**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 554 | 420 | 974 | 56.9% | 43.1% |
| 2026-2027 | 73 | 60 | 133 | 54.9% | 45.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **223** of `448` (49.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 398 | 196 | 49.2% |
| 2026-2027 | 50 | 27 | 54.0% |

## 5. Clean sheets
- Home clean sheets: **163** (36.4%)
- Away clean sheets: **104** (23.2%)
- Total clean sheets recorded: **267**
- Matches with at least one clean sheet: **225** (50.2%)
- Both teams kept clean sheets (0-0): **42**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 146 | 95 | 241 | 202 (50.8%) |
| 2026-2027 | 50 | 17 | 9 | 26 | 23 (46.0%) |

## 6. Scoring intensity
- First-half goals: **469** (42.4%)
- Second-half goals: **638** (57.6%)
- Avg first-half goals per match: **1.047**
- Avg second-half goals per match: **1.424**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **114** (25.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 419 | 555 | 43.0% | 57.0% |
| 2026-2027 | 50 | 50 | 83 | 37.6% | 62.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `406` of `448` (90.6%)
- Goalless matches: `42`
- Min `1` | Max `99` | Mean `34.13` | Median (p50) `29.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 110 | 24.6% | 27.1% |
| 16-30 | 101 | 22.5% | 24.9% |
| 31-45 | 73 | 16.3% | 18.0% |
| 46-60 | 52 | 11.6% | 12.8% |
| 61-75 | 40 | 8.9% | 9.9% |
| 76-90 | 21 | 4.7% | 5.2% |
| 91-120 | 9 | 2.0% | 2.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\primera1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\primera1\charts\goals_analysis_avg_per_season.png)

