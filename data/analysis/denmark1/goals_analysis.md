# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:56:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 12 | 4.8% |
| 1 | 31 | 12.5% |
| 2 | 58 | 23.4% |
| 3 | 58 | 23.4% |
| 4 | 35 | 14.1% |
| 5 | 30 | 12.1% |
| 6 | 18 | 7.3% |
| 7 | 4 | 1.6% |
| 8 | 2 | 0.8% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 193 | 599 | 1.658 | 1.446 | 3.104 |
| 2026-2027 | 55 | 164 | 1.527 | 1.455 | 2.982 |

## 3. Home vs away goal share
- Home goals: **404** (52.9%)
- Away goals: **359** (47.1%)
- Home/away ratio: **1.125**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 320 | 279 | 599 | 53.4% | 46.6% |
| 2026-2027 | 84 | 80 | 164 | 51.2% | 48.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **148** of `248` (59.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 193 | 115 | 59.6% |
| 2026-2027 | 55 | 33 | 60.0% |

## 5. Clean sheets
- Home clean sheets: **62** (25.0%)
- Away clean sheets: **50** (20.2%)
- Total clean sheets recorded: **112**
- Matches with at least one clean sheet: **100** (40.3%)
- Both teams kept clean sheets (0-0): **12**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 193 | 49 | 40 | 89 | 78 (40.4%) |
| 2026-2027 | 55 | 13 | 10 | 23 | 22 (40.0%) |

## 6. Scoring intensity
- First-half goals: **360** (47.2%)
- Second-half goals: **403** (52.8%)
- Avg first-half goals per match: **1.452**
- Avg second-half goals per match: **1.625**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **53** (21.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 193 | 282 | 317 | 47.1% | 52.9% |
| 2026-2027 | 55 | 78 | 86 | 47.6% | 52.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `236` of `248` (95.2%)
- Goalless matches: `12`
- Min `1` | Max `99` | Mean `28.05` | Median (p50) `21.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 96 | 38.7% | 40.7% |
| 16-30 | 54 | 21.8% | 22.9% |
| 31-45 | 31 | 12.5% | 13.1% |
| 46-60 | 30 | 12.1% | 12.7% |
| 61-75 | 8 | 3.2% | 3.4% |
| 76-90 | 13 | 5.2% | 5.5% |
| 91-120 | 4 | 1.6% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\denmark1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\denmark1\charts\goals_analysis_avg_per_season.png)

