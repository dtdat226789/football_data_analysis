# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:49:44+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 14 | 5.4% |
| 1 | 45 | 17.3% |
| 2 | 57 | 21.9% |
| 3 | 56 | 21.5% |
| 4 | 41 | 15.8% |
| 5 | 25 | 9.6% |
| 6 | 12 | 4.6% |
| 7 | 6 | 2.3% |
| 8 | 3 | 1.2% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 135 | 443 | 1.741 | 1.541 | 3.281 |
| 2026 | 125 | 321 | 1.328 | 1.24 | 2.568 |

## 3. Home vs away goal share
- Home goals: **401** (52.5%)
- Away goals: **363** (47.5%)
- Home/away ratio: **1.105**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 235 | 208 | 443 | 53.0% | 47.0% |
| 2026 | 166 | 155 | 321 | 51.7% | 48.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **150** of `260` (57.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 135 | 93 | 68.9% |
| 2026 | 125 | 57 | 45.6% |

## 5. Clean sheets
- Home clean sheets: **60** (23.1%)
- Away clean sheets: **64** (24.6%)
- Total clean sheets recorded: **124**
- Matches with at least one clean sheet: **110** (42.3%)
- Both teams kept clean sheets (0-0): **14**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 135 | 24 | 23 | 47 | 42 (31.1%) |
| 2026 | 125 | 36 | 41 | 77 | 68 (54.4%) |

## 6. Scoring intensity
- First-half goals: **335** (43.8%)
- Second-half goals: **429** (56.2%)
- Avg first-half goals per match: **1.288**
- Avg second-half goals per match: **1.65**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **60** (23.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 135 | 195 | 248 | 44.0% | 56.0% |
| 2026 | 125 | 140 | 181 | 43.6% | 56.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `246` of `260` (94.6%)
- Goalless matches: `14`
- Min `1` | Max `95` | Mean `29.53` | Median (p50) `20.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 93 | 35.8% | 37.8% |
| 16-30 | 59 | 22.7% | 24.0% |
| 31-45 | 32 | 12.3% | 13.0% |
| 46-60 | 32 | 12.3% | 13.0% |
| 61-75 | 19 | 7.3% | 7.7% |
| 76-90 | 7 | 2.7% | 2.8% |
| 91-120 | 4 | 1.5% | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\finland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\finland2\charts\goals_analysis_avg_per_season.png)

