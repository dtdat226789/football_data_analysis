# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:01:32+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.6% |
| 1 | 62 | 18.3% |
| 2 | 76 | 22.4% |
| 3 | 77 | 22.7% |
| 4 | 59 | 17.4% |
| 5 | 27 | 8.0% |
| 6 | 10 | 2.9% |
| 7 | 8 | 2.4% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 179 | 502 | 1.559 | 1.246 | 2.804 |
| 2026 | 160 | 439 | 1.637 | 1.106 | 2.744 |

## 3. Home vs away goal share
- Home goals: **541** (57.5%)
- Away goals: **400** (42.5%)
- Home/away ratio: **1.353**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 279 | 223 | 502 | 55.6% | 44.4% |
| 2026 | 262 | 177 | 439 | 59.7% | 40.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **180** of `339` (53.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 179 | 97 | 54.2% |
| 2026 | 160 | 83 | 51.9% |

## 5. Clean sheets
- Home clean sheets: **95** (28.0%)
- Away clean sheets: **83** (24.5%)
- Total clean sheets recorded: **178**
- Matches with at least one clean sheet: **159** (46.9%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 179 | 45 | 47 | 92 | 82 (45.8%) |
| 2026 | 160 | 50 | 36 | 86 | 77 (48.1%) |

## 6. Scoring intensity
- First-half goals: **401** (42.8%)
- Second-half goals: **537** (57.2%)
- Avg first-half goals per match: **1.186**
- Avg second-half goals per match: **1.589**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **83** (24.5%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 179 | 221 | 278 | 44.3% | 55.7% |
| 2026 | 160 | 180 | 259 | 41.0% | 59.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `319` of `339` (94.1%)
- Goalless matches: `20`
- Min `1` | Max `96` | Mean `30.94` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 112 | 33.0% | 35.1% |
| 16-30 | 75 | 22.1% | 23.5% |
| 31-45 | 45 | 13.3% | 14.1% |
| 46-60 | 42 | 12.4% | 13.2% |
| 61-75 | 28 | 8.3% | 8.8% |
| 76-90 | 12 | 3.5% | 3.8% |
| 91-120 | 5 | 1.5% | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\ireland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\ireland2\charts\goals_analysis_avg_per_season.png)

