# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:01:23+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 30 | 8.9% |
| 1 | 61 | 18.0% |
| 2 | 83 | 24.6% |
| 3 | 75 | 22.2% |
| 4 | 45 | 13.3% |
| 5 | 30 | 8.9% |
| 6 | 8 | 2.4% |
| 7 | 4 | 1.2% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 180 | 437 | 1.378 | 1.05 | 2.428 |
| 2026 | 158 | 438 | 1.487 | 1.285 | 2.772 |

## 3. Home vs away goal share
- Home goals: **483** (55.2%)
- Away goals: **392** (44.8%)
- Home/away ratio: **1.232**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 248 | 189 | 437 | 56.8% | 43.2% |
| 2026 | 235 | 203 | 438 | 53.7% | 46.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **190** of `338` (56.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 180 | 96 | 53.3% |
| 2026 | 158 | 94 | 59.5% |

## 5. Clean sheets
- Home clean sheets: **106** (31.4%)
- Away clean sheets: **72** (21.3%)
- Total clean sheets recorded: **178**
- Matches with at least one clean sheet: **148** (43.8%)
- Both teams kept clean sheets (0-0): **30**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 180 | 60 | 39 | 99 | 84 (46.7%) |
| 2026 | 158 | 46 | 33 | 79 | 64 (40.5%) |

## 6. Scoring intensity
- First-half goals: **408** (46.6%)
- Second-half goals: **467** (53.4%)
- Avg first-half goals per match: **1.207**
- Avg second-half goals per match: **1.382**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **63** (18.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 180 | 211 | 226 | 48.3% | 51.7% |
| 2026 | 158 | 197 | 241 | 45.0% | 55.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `308` of `338` (91.1%)
- Goalless matches: `30`
- Min `1` | Max `94` | Mean `30.01` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 99 | 29.3% | 32.1% |
| 16-30 | 82 | 24.3% | 26.6% |
| 31-45 | 57 | 16.9% | 18.5% |
| 46-60 | 35 | 10.4% | 11.4% |
| 61-75 | 14 | 4.1% | 4.5% |
| 76-90 | 15 | 4.4% | 4.9% |
| 91-120 | 6 | 1.8% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\ireland1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\ireland1\charts\goals_analysis_avg_per_season.png)

