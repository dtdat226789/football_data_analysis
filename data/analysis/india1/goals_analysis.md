# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:01:14+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: ISL (India)
- Scope: league `india1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 21 | 8.5% |
| 1 | 36 | 14.6% |
| 2 | 63 | 25.5% |
| 3 | 57 | 23.1% |
| 4 | 32 | 13.0% |
| 5 | 23 | 9.3% |
| 6 | 12 | 4.9% |
| 7 | 3 | 1.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2024-2025 | 156 | 448 | 1.487 | 1.385 | 2.872 |
| 2025-2026 | 91 | 221 | 1.363 | 1.066 | 2.429 |

## 3. Home vs away goal share
- Home goals: **356** (53.2%)
- Away goals: **313** (46.8%)
- Home/away ratio: **1.137**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2024-2025 | 232 | 216 | 448 | 51.8% | 48.2% |
| 2025-2026 | 124 | 97 | 221 | 56.1% | 43.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **131** of `247` (53.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2024-2025 | 156 | 83 | 53.2% |
| 2025-2026 | 91 | 48 | 52.7% |

## 5. Clean sheets
- Home clean sheets: **78** (31.6%)
- Away clean sheets: **59** (23.9%)
- Total clean sheets recorded: **137**
- Matches with at least one clean sheet: **116** (47.0%)
- Both teams kept clean sheets (0-0): **21**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2024-2025 | 156 | 47 | 37 | 84 | 73 (46.8%) |
| 2025-2026 | 91 | 31 | 22 | 53 | 43 (47.3%) |

## 6. Scoring intensity
- First-half goals: **283** (42.3%)
- Second-half goals: **386** (57.7%)
- Avg first-half goals per match: **1.146**
- Avg second-half goals per match: **1.563**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **56** (22.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2024-2025 | 156 | 185 | 263 | 41.3% | 58.7% |
| 2025-2026 | 91 | 98 | 123 | 44.3% | 55.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `226` of `247` (91.5%)
- Goalless matches: `21`
- Min `1` | Max `94` | Mean `31.38` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 82 | 33.2% | 36.3% |
| 16-30 | 43 | 17.4% | 19.0% |
| 31-45 | 34 | 13.8% | 15.0% |
| 46-60 | 38 | 15.4% | 16.8% |
| 61-75 | 18 | 7.3% | 8.0% |
| 76-90 | 9 | 3.6% | 4.0% |
| 91-120 | 2 | 0.8% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\india1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\india1\charts\goals_analysis_avg_per_season.png)

