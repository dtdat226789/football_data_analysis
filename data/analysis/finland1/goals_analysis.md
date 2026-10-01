# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:49:30+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 18 | 6.6% |
| 1 | 48 | 17.6% |
| 2 | 56 | 20.5% |
| 3 | 54 | 19.8% |
| 4 | 43 | 15.8% |
| 5 | 39 | 14.3% |
| 6 | 9 | 3.3% |
| 7 | 4 | 1.5% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 132 | 433 | 1.682 | 1.598 | 3.28 |
| 2026 | 141 | 356 | 1.411 | 1.113 | 2.525 |

## 3. Home vs away goal share
- Home goals: **421** (53.4%)
- Away goals: **368** (46.6%)
- Home/away ratio: **1.144**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 222 | 211 | 433 | 51.3% | 48.7% |
| 2026 | 199 | 157 | 356 | 55.9% | 44.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **152** of `273` (55.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 132 | 83 | 62.9% |
| 2026 | 141 | 69 | 48.9% |

## 5. Clean sheets
- Home clean sheets: **75** (27.5%)
- Away clean sheets: **64** (23.4%)
- Total clean sheets recorded: **139**
- Matches with at least one clean sheet: **121** (44.3%)
- Both teams kept clean sheets (0-0): **18**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 132 | 24 | 33 | 57 | 49 (37.1%) |
| 2026 | 141 | 51 | 31 | 82 | 72 (51.1%) |

## 6. Scoring intensity
- First-half goals: **342** (43.3%)
- Second-half goals: **447** (56.7%)
- Avg first-half goals per match: **1.253**
- Avg second-half goals per match: **1.637**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **58** (21.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 132 | 165 | 268 | 38.1% | 61.9% |
| 2026 | 141 | 177 | 179 | 49.7% | 50.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `255` of `273` (93.4%)
- Goalless matches: `18`
- Min `1` | Max `94` | Mean `29.95` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 85 | 31.1% | 33.3% |
| 16-30 | 62 | 22.7% | 24.3% |
| 31-45 | 43 | 15.8% | 16.9% |
| 46-60 | 37 | 13.6% | 14.5% |
| 61-75 | 15 | 5.5% | 5.9% |
| 76-90 | 11 | 4.0% | 4.3% |
| 91-120 | 2 | 0.7% | 0.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\finland1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\finland1\charts\goals_analysis_avg_per_season.png)

