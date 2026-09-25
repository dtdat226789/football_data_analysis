# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:42:26+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 41 | 9.4% |
| 1 | 89 | 20.3% |
| 2 | 112 | 25.6% |
| 3 | 93 | 21.2% |
| 4 | 54 | 12.3% |
| 5 | 31 | 7.1% |
| 6 | 12 | 2.7% |
| 7 | 5 | 1.1% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 974 | 1.392 | 1.055 | 2.447 |
| 2026-2027 | 40 | 105 | 1.5 | 1.125 | 2.625 |

## 3. Home vs away goal share
- Home goals: **614** (56.9%)
- Away goals: **465** (43.1%)
- Home/away ratio: **1.32**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 554 | 420 | 974 | 56.9% | 43.1% |
| 2026-2027 | 60 | 45 | 105 | 57.1% | 42.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **219** of `438` (50.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 398 | 196 | 49.2% |
| 2026-2027 | 40 | 23 | 57.5% |

## 5. Clean sheets
- Home clean sheets: **159** (36.3%)
- Away clean sheets: **101** (23.1%)
- Total clean sheets recorded: **260**
- Matches with at least one clean sheet: **219** (50.0%)
- Both teams kept clean sheets (0-0): **41**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 146 | 95 | 241 | 202 (50.8%) |
| 2026-2027 | 40 | 13 | 6 | 19 | 17 (42.5%) |

## 6. Scoring intensity
- First-half goals: **458** (42.4%)
- Second-half goals: **621** (57.6%)
- Avg first-half goals per match: **1.046**
- Avg second-half goals per match: **1.418**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **112** (25.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 398 | 419 | 555 | 43.0% | 57.0% |
| 2026-2027 | 40 | 39 | 66 | 37.1% | 62.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `397` of `438` (90.6%)
- Goalless matches: `41`
- Min `1` | Max `99` | Mean `34.09` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 109 | 24.9% | 27.5% |
| 16-30 | 97 | 22.1% | 24.4% |
| 31-45 | 71 | 16.2% | 17.9% |
| 46-60 | 52 | 11.9% | 13.1% |
| 61-75 | 39 | 8.9% | 9.8% |
| 76-90 | 20 | 4.6% | 5.0% |
| 91-120 | 9 | 2.1% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\primera1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\primera1\charts\goals_analysis_avg_per_season.png)

