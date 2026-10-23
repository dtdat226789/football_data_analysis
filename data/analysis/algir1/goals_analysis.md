# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:43:36+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 22 | 8.4% |
| 1 | 71 | 27.0% |
| 2 | 69 | 26.2% |
| 3 | 50 | 19.0% |
| 4 | 29 | 11.0% |
| 5 | 13 | 4.9% |
| 6 | 5 | 1.9% |
| 7 | 2 | 0.8% |
| 8 | 2 | 0.8% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 544 | 1.354 | 0.912 | 2.267 |
| 2026-2027 | 23 | 56 | 1.565 | 0.87 | 2.435 |

## 3. Home vs away goal share
- Home goals: **361** (60.2%)
- Away goals: **239** (39.8%)
- Home/away ratio: **1.51**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 325 | 219 | 544 | 59.7% | 40.3% |
| 2026-2027 | 36 | 20 | 56 | 64.3% | 35.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **125** of `263` (47.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 240 | 117 | 48.8% |
| 2026-2027 | 23 | 8 | 34.8% |

## 5. Clean sheets
- Home clean sheets: **104** (39.5%)
- Away clean sheets: **56** (21.3%)
- Total clean sheets recorded: **160**
- Matches with at least one clean sheet: **138** (52.5%)
- Both teams kept clean sheets (0-0): **22**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 93 | 50 | 143 | 123 (51.2%) |
| 2026-2027 | 23 | 11 | 6 | 17 | 15 (65.2%) |

## 6. Scoring intensity
- First-half goals: **272** (45.3%)
- Second-half goals: **328** (54.7%)
- Avg first-half goals per match: **1.034**
- Avg second-half goals per match: **1.247**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **75** (28.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 249 | 295 | 45.8% | 54.2% |
| 2026-2027 | 23 | 23 | 33 | 41.1% | 58.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `241` of `263` (91.6%)
- Goalless matches: `22`
- Min `1` | Max `108` | Mean `35.51` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 65 | 24.7% | 27.0% |
| 16-30 | 64 | 24.3% | 26.6% |
| 31-45 | 31 | 11.8% | 12.9% |
| 46-60 | 33 | 12.5% | 13.7% |
| 61-75 | 23 | 8.7% | 9.5% |
| 76-90 | 20 | 7.6% | 8.3% |
| 91-120 | 5 | 1.9% | 2.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\algir1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\algir1\charts\goals_analysis_avg_per_season.png)

