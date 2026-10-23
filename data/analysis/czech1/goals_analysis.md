# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:46:50+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 27 | 7.7% |
| 1 | 52 | 14.8% |
| 2 | 92 | 26.2% |
| 3 | 86 | 24.5% |
| 4 | 54 | 15.4% |
| 5 | 21 | 6.0% |
| 6 | 12 | 3.4% |
| 7 | 4 | 1.1% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 280 | 740 | 1.404 | 1.239 | 2.643 |
| 2026-2027 | 71 | 201 | 1.521 | 1.31 | 2.831 |

## 3. Home vs away goal share
- Home goals: **501** (53.2%)
- Away goals: **440** (46.8%)
- Home/away ratio: **1.139**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 393 | 347 | 740 | 53.1% | 46.9% |
| 2026-2027 | 108 | 93 | 201 | 53.7% | 46.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **177** of `351` (50.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 280 | 139 | 49.6% |
| 2026-2027 | 71 | 38 | 53.5% |

## 5. Clean sheets
- Home clean sheets: **111** (31.6%)
- Away clean sheets: **90** (25.6%)
- Total clean sheets recorded: **201**
- Matches with at least one clean sheet: **174** (49.6%)
- Both teams kept clean sheets (0-0): **27**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 280 | 92 | 72 | 164 | 141 (50.4%) |
| 2026-2027 | 71 | 19 | 18 | 37 | 33 (46.5%) |

## 6. Scoring intensity
- First-half goals: **437** (46.6%)
- Second-half goals: **501** (53.4%)
- Avg first-half goals per match: **1.249**
- Avg second-half goals per match: **1.431**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **65** (18.5%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 280 | 347 | 390 | 47.1% | 52.9% |
| 2026-2027 | 71 | 90 | 111 | 44.8% | 55.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `323` of `351` (92.0%)
- Goalless matches: `28`
- Min `1` | Max `88` | Mean `29.83` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 104 | 29.6% | 32.2% |
| 16-30 | 84 | 23.9% | 26.0% |
| 31-45 | 63 | 17.9% | 19.5% |
| 46-60 | 35 | 10.0% | 10.8% |
| 61-75 | 24 | 6.8% | 7.4% |
| 76-90 | 13 | 3.7% | 4.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech1\charts\goals_analysis_avg_per_season.png)

