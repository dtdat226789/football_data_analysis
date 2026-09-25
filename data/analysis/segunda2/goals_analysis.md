# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:45:40+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 31 | 9.3% |
| 1 | 63 | 18.9% |
| 2 | 86 | 25.8% |
| 3 | 60 | 18.0% |
| 4 | 55 | 16.5% |
| 5 | 27 | 8.1% |
| 6 | 8 | 2.4% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 769 | 1.438 | 1.075 | 2.513 |
| 2026-2027 | 27 | 73 | 1.63 | 1.074 | 2.704 |

## 3. Home vs away goal share
- Home goals: **484** (57.5%)
- Away goals: **358** (42.5%)
- Home/away ratio: **1.352**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 440 | 329 | 769 | 57.2% | 42.8% |
| 2026-2027 | 44 | 29 | 73 | 60.3% | 39.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **172** of `333` (51.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 158 | 51.6% |
| 2026-2027 | 27 | 14 | 51.9% |

## 5. Clean sheets
- Home clean sheets: **111** (33.3%)
- Away clean sheets: **81** (24.3%)
- Total clean sheets recorded: **192**
- Matches with at least one clean sheet: **161** (48.3%)
- Both teams kept clean sheets (0-0): **31**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 102 | 74 | 176 | 148 (48.4%) |
| 2026-2027 | 27 | 9 | 7 | 16 | 13 (48.1%) |

## 6. Scoring intensity
- First-half goals: **363** (43.1%)
- Second-half goals: **479** (56.9%)
- Avg first-half goals per match: **1.09**
- Avg second-half goals per match: **1.438**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **81** (24.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 330 | 439 | 42.9% | 57.1% |
| 2026-2027 | 27 | 33 | 40 | 45.2% | 54.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `302` of `333` (90.7%)
- Goalless matches: `31`
- Min `1` | Max `94` | Mean `32.77` | Median (p50) `28.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 95 | 28.5% | 31.5% |
| 16-30 | 67 | 20.1% | 22.2% |
| 31-45 | 57 | 17.1% | 18.9% |
| 46-60 | 38 | 11.4% | 12.6% |
| 61-75 | 25 | 7.5% | 8.3% |
| 76-90 | 14 | 4.2% | 4.6% |
| 91-120 | 6 | 1.8% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda2\charts\goals_analysis_avg_per_season.png)

