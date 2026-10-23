# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:09:47+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 11 | 3.9% |
| 1 | 30 | 10.6% |
| 2 | 47 | 16.5% |
| 3 | 74 | 26.1% |
| 4 | 52 | 18.3% |
| 5 | 30 | 10.6% |
| 6 | 29 | 10.2% |
| 7 | 7 | 2.5% |
| 8 | 3 | 1.1% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 230 | 753 | 1.77 | 1.504 | 3.274 |
| 2026-2027 | 54 | 209 | 1.889 | 1.981 | 3.87 |

## 3. Home vs away goal share
- Home goals: **509** (52.9%)
- Away goals: **453** (47.1%)
- Home/away ratio: **1.124**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 407 | 346 | 753 | 54.1% | 45.9% |
| 2026-2027 | 102 | 107 | 209 | 48.8% | 51.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **191** of `284` (67.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 230 | 151 | 65.7% |
| 2026-2027 | 54 | 40 | 74.1% |

## 5. Clean sheets
- Home clean sheets: **57** (20.1%)
- Away clean sheets: **47** (16.5%)
- Total clean sheets recorded: **104**
- Matches with at least one clean sheet: **93** (32.7%)
- Both teams kept clean sheets (0-0): **11**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 230 | 51 | 38 | 89 | 79 (34.3%) |
| 2026-2027 | 54 | 6 | 9 | 15 | 14 (25.9%) |

## 6. Scoring intensity
- First-half goals: **416** (43.2%)
- Second-half goals: **546** (56.8%)
- Avg first-half goals per match: **1.465**
- Avg second-half goals per match: **1.923**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **55** (19.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 230 | 329 | 424 | 43.7% | 56.3% |
| 2026-2027 | 54 | 87 | 122 | 41.6% | 58.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `273` of `284` (96.1%)
- Goalless matches: `11`
- Min `1` | Max `97` | Mean `26.79` | Median (p50) `20`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 120 | 42.3% | 44.0% |
| 16-30 | 55 | 19.4% | 20.1% |
| 31-45 | 42 | 14.8% | 15.4% |
| 46-60 | 30 | 10.6% | 11.0% |
| 61-75 | 16 | 5.6% | 5.9% |
| 76-90 | 5 | 1.8% | 1.8% |
| 91-120 | 5 | 1.8% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\swiss1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\swiss1\charts\goals_analysis_avg_per_season.png)

