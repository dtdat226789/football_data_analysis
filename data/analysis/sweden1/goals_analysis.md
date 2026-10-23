# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:09:18+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 21 | 5.0% |
| 1 | 64 | 15.4% |
| 2 | 112 | 26.9% |
| 3 | 93 | 22.4% |
| 4 | 58 | 13.9% |
| 5 | 37 | 8.9% |
| 6 | 13 | 3.1% |
| 7 | 12 | 2.9% |
| 8 | 2 | 0.5% |
| 9 | 2 | 0.5% |
| 10 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 240 | 683 | 1.475 | 1.371 | 2.846 |
| 2026 | 176 | 517 | 1.619 | 1.318 | 2.938 |

## 3. Home vs away goal share
- Home goals: **639** (53.2%)
- Away goals: **561** (46.8%)
- Home/away ratio: **1.139**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 354 | 329 | 683 | 51.8% | 48.2% |
| 2026 | 285 | 232 | 517 | 55.1% | 44.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **219** of `416` (52.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 240 | 126 | 52.5% |
| 2026 | 176 | 93 | 52.8% |

## 5. Clean sheets
- Home clean sheets: **118** (28.4%)
- Away clean sheets: **100** (24.0%)
- Total clean sheets recorded: **218**
- Matches with at least one clean sheet: **197** (47.4%)
- Both teams kept clean sheets (0-0): **21**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 240 | 67 | 61 | 128 | 114 (47.5%) |
| 2026 | 176 | 51 | 39 | 90 | 83 (47.2%) |

## 6. Scoring intensity
- First-half goals: **526** (43.8%)
- Second-half goals: **674** (56.2%)
- Avg first-half goals per match: **1.264**
- Avg second-half goals per match: **1.62**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **108** (26.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 240 | 294 | 389 | 43.0% | 57.0% |
| 2026 | 176 | 232 | 285 | 44.9% | 55.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `395` of `416` (95.0%)
- Goalless matches: `21`
- Min `1` | Max `94` | Mean `31.45` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 131 | 31.5% | 33.2% |
| 16-30 | 92 | 22.1% | 23.3% |
| 31-45 | 56 | 13.5% | 14.2% |
| 46-60 | 69 | 16.6% | 17.5% |
| 61-75 | 27 | 6.5% | 6.8% |
| 76-90 | 14 | 3.4% | 3.5% |
| 91-120 | 6 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\sweden1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\sweden1\charts\goals_analysis_avg_per_season.png)

