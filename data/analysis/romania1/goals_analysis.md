# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:43:07+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 32 | 7.5% |
| 1 | 93 | 21.7% |
| 2 | 104 | 24.2% |
| 3 | 79 | 18.4% |
| 4 | 68 | 15.9% |
| 5 | 37 | 8.6% |
| 6 | 12 | 2.8% |
| 7 | 4 | 0.9% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 350 | 887 | 1.44 | 1.094 | 2.534 |
| 2026-2027 | 79 | 208 | 1.785 | 0.848 | 2.633 |

## 3. Home vs away goal share
- Home goals: **645** (58.9%)
- Away goals: **450** (41.1%)
- Home/away ratio: **1.433**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 504 | 383 | 887 | 56.8% | 43.2% |
| 2026-2027 | 141 | 67 | 208 | 67.8% | 32.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **217** of `429` (50.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 350 | 180 | 51.4% |
| 2026-2027 | 79 | 37 | 46.8% |

## 5. Clean sheets
- Home clean sheets: **140** (32.6%)
- Away clean sheets: **104** (24.2%)
- Total clean sheets recorded: **244**
- Matches with at least one clean sheet: **212** (49.4%)
- Both teams kept clean sheets (0-0): **32**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 350 | 106 | 89 | 195 | 170 (48.6%) |
| 2026-2027 | 79 | 34 | 15 | 49 | 42 (53.2%) |

## 6. Scoring intensity
- First-half goals: **486** (44.4%)
- Second-half goals: **609** (55.6%)
- Avg first-half goals per match: **1.133**
- Avg second-half goals per match: **1.42**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **113** (26.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 350 | 397 | 490 | 44.8% | 55.2% |
| 2026-2027 | 79 | 89 | 119 | 42.8% | 57.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `397` of `429` (92.5%)
- Goalless matches: `32`
- Min `1` | Max `96` | Mean `33.53` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 112 | 26.1% | 28.2% |
| 16-30 | 97 | 22.6% | 24.4% |
| 31-45 | 70 | 16.3% | 17.6% |
| 46-60 | 50 | 11.7% | 12.6% |
| 61-75 | 46 | 10.7% | 11.6% |
| 76-90 | 15 | 3.5% | 3.8% |
| 91-120 | 7 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\romania1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\romania1\charts\goals_analysis_avg_per_season.png)

