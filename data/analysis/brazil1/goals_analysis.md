# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:45:19+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 43 | 6.5% |
| 1 | 123 | 18.7% |
| 2 | 173 | 26.3% |
| 3 | 154 | 23.4% |
| 4 | 87 | 13.2% |
| 5 | 48 | 7.3% |
| 6 | 26 | 4.0% |
| 7 | 1 | 0.2% |
| 8 | 2 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 380 | 959 | 1.526 | 0.997 | 2.524 |
| 2026 | 277 | 739 | 1.52 | 1.148 | 2.668 |

## 3. Home vs away goal share
- Home goals: **1001** (59.0%)
- Away goals: **697** (41.0%)
- Home/away ratio: **1.436**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 580 | 379 | 959 | 60.5% | 39.5% |
| 2026 | 421 | 318 | 739 | 57.0% | 43.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **345** of `657` (52.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 380 | 180 | 47.4% |
| 2026 | 277 | 165 | 59.6% |

## 5. Clean sheets
- Home clean sheets: **225** (34.2%)
- Away clean sheets: **130** (19.8%)
- Total clean sheets recorded: **355**
- Matches with at least one clean sheet: **312** (47.5%)
- Both teams kept clean sheets (0-0): **43**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 380 | 145 | 82 | 227 | 200 (52.6%) |
| 2026 | 277 | 80 | 48 | 128 | 112 (40.4%) |

## 6. Scoring intensity
- First-half goals: **754** (44.4%)
- Second-half goals: **944** (55.6%)
- Avg first-half goals per match: **1.148**
- Avg second-half goals per match: **1.437**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **141** (21.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 380 | 427 | 532 | 44.5% | 55.5% |
| 2026 | 277 | 327 | 412 | 44.2% | 55.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `614` of `657` (93.5%)
- Goalless matches: `43`
- Min `1` | Max `106` | Mean `31.82` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 184 | 28.0% | 30.0% |
| 16-30 | 158 | 24.0% | 25.7% |
| 31-45 | 107 | 16.3% | 17.4% |
| 46-60 | 85 | 12.9% | 13.8% |
| 61-75 | 48 | 7.3% | 7.8% |
| 76-90 | 18 | 2.7% | 2.9% |
| 91-120 | 14 | 2.1% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\brazil1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\brazil1\charts\goals_analysis_avg_per_season.png)

