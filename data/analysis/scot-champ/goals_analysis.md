# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:44:16+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 12.8% |
| 1 | 41 | 18.1% |
| 2 | 63 | 27.8% |
| 3 | 43 | 18.9% |
| 4 | 28 | 12.3% |
| 5 | 15 | 6.6% |
| 6 | 7 | 3.1% |
| 7 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 460 | 1.326 | 1.095 | 2.421 |
| 2026-2027 | 37 | 72 | 1.135 | 0.811 | 1.946 |

## 3. Home vs away goal share
- Home goals: **294** (55.3%)
- Away goals: **238** (44.7%)
- Home/away ratio: **1.235**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 252 | 208 | 460 | 54.8% | 45.2% |
| 2026-2027 | 42 | 30 | 72 | 58.3% | 41.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **106** of `227` (46.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 190 | 93 | 48.9% |
| 2026-2027 | 37 | 13 | 35.1% |

## 5. Clean sheets
- Home clean sheets: **81** (35.7%)
- Away clean sheets: **69** (30.4%)
- Total clean sheets recorded: **150**
- Matches with at least one clean sheet: **121** (53.3%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 63 | 59 | 122 | 97 (51.1%) |
| 2026-2027 | 37 | 18 | 10 | 28 | 24 (64.9%) |

## 6. Scoring intensity
- First-half goals: **251** (47.2%)
- Second-half goals: **281** (52.8%)
- Avg first-half goals per match: **1.106**
- Avg second-half goals per match: **1.238**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **40** (17.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 215 | 245 | 46.7% | 53.3% |
| 2026-2027 | 37 | 36 | 36 | 50.0% | 50.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `198` of `227` (87.2%)
- Goalless matches: `29`
- Min `1` | Max `88` | Mean `29.58` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 59 | 26.0% | 29.8% |
| 16-30 | 54 | 23.8% | 27.3% |
| 31-45 | 41 | 18.1% | 20.7% |
| 46-60 | 26 | 11.5% | 13.1% |
| 61-75 | 10 | 4.4% | 5.1% |
| 76-90 | 8 | 3.5% | 4.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\scot-champ\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\scot-champ\charts\goals_analysis_avg_per_season.png)

