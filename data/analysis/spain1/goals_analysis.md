# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:47:52+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 20 | 4.5% |
| 1 | 79 | 17.6% |
| 2 | 121 | 26.9% |
| 3 | 105 | 23.4% |
| 4 | 58 | 12.9% |
| 5 | 42 | 9.4% |
| 6 | 15 | 3.3% |
| 7 | 7 | 1.6% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 1024 | 1.574 | 1.121 | 2.695 |
| 2026-2027 | 69 | 210 | 1.71 | 1.333 | 3.043 |

## 3. Home vs away goal share
- Home goals: **716** (58.0%)
- Away goals: **518** (42.0%)
- Home/away ratio: **1.382**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 598 | 426 | 1024 | 58.4% | 41.6% |
| 2026-2027 | 118 | 92 | 210 | 56.2% | 43.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **255** of `449` (56.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 215 | 56.6% |
| 2026-2027 | 69 | 40 | 58.0% |

## 5. Clean sheets
- Home clean sheets: **132** (29.4%)
- Away clean sheets: **82** (18.3%)
- Total clean sheets recorded: **214**
- Matches with at least one clean sheet: **194** (43.2%)
- Both teams kept clean sheets (0-0): **20**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 111 | 69 | 180 | 165 (43.4%) |
| 2026-2027 | 69 | 21 | 13 | 34 | 29 (42.0%) |

## 6. Scoring intensity
- First-half goals: **532** (43.1%)
- Second-half goals: **702** (56.9%)
- Avg first-half goals per match: **1.185**
- Avg second-half goals per match: **1.563**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **117** (26.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 437 | 587 | 42.7% | 57.3% |
| 2026-2027 | 69 | 95 | 115 | 45.2% | 54.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `429` of `449` (95.5%)
- Goalless matches: `20`
- Min `1` | Max `94` | Mean `33.82` | Median (p50) `30`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 123 | 27.4% | 28.7% |
| 16-30 | 97 | 21.6% | 22.6% |
| 31-45 | 80 | 17.8% | 18.6% |
| 46-60 | 66 | 14.7% | 15.4% |
| 61-75 | 33 | 7.3% | 7.7% |
| 76-90 | 28 | 6.2% | 6.5% |
| 91-120 | 2 | 0.4% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\spain1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\spain1\charts\goals_analysis_avg_per_season.png)

