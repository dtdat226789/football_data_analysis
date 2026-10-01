# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:07:18+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 35 | 10.1% |
| 1 | 83 | 24.0% |
| 2 | 81 | 23.4% |
| 3 | 68 | 19.7% |
| 4 | 41 | 11.8% |
| 5 | 20 | 5.8% |
| 6 | 15 | 4.3% |
| 7 | 0 | 0.0% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 742 | 1.418 | 1.007 | 2.425 |
| 2026-2027 | 40 | 87 | 1.2 | 0.975 | 2.175 |

## 3. Home vs away goal share
- Home goals: **482** (58.1%)
- Away goals: **347** (41.9%)
- Home/away ratio: **1.389**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 434 | 308 | 742 | 58.5% | 41.5% |
| 2026-2027 | 48 | 39 | 87 | 55.2% | 44.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **179** of `346` (51.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 159 | 52.0% |
| 2026-2027 | 40 | 20 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **131** (37.9%)
- Away clean sheets: **71** (20.5%)
- Total clean sheets recorded: **202**
- Matches with at least one clean sheet: **167** (48.3%)
- Both teams kept clean sheets (0-0): **35**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 114 | 66 | 180 | 147 (48.0%) |
| 2026-2027 | 40 | 17 | 5 | 22 | 20 (50.0%) |

## 6. Scoring intensity
- First-half goals: **357** (43.1%)
- Second-half goals: **472** (56.9%)
- Avg first-half goals per match: **1.032**
- Avg second-half goals per match: **1.364**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **100** (28.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 320 | 422 | 43.1% | 56.9% |
| 2026-2027 | 40 | 37 | 50 | 42.5% | 57.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `311` of `346` (89.9%)
- Goalless matches: `35`
- Min `1` | Max `99` | Mean `34.64` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 99 | 28.6% | 31.8% |
| 16-30 | 69 | 19.9% | 22.2% |
| 31-45 | 38 | 11.0% | 12.2% |
| 46-60 | 41 | 11.8% | 13.2% |
| 61-75 | 35 | 10.1% | 11.3% |
| 76-90 | 24 | 6.9% | 7.7% |
| 91-120 | 5 | 1.4% | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda3\charts\goals_analysis_avg_per_season.png)

