# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:03:16+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.7% |
| 1 | 64 | 19.0% |
| 2 | 76 | 22.6% |
| 3 | 63 | 18.8% |
| 4 | 47 | 14.0% |
| 5 | 37 | 11.0% |
| 6 | 19 | 5.7% |
| 7 | 7 | 2.1% |
| 8 | 4 | 1.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 182 | 535 | 1.659 | 1.28 | 2.94 |
| 2026 | 154 | 438 | 1.597 | 1.247 | 2.844 |

## 3. Home vs away goal share
- Home goals: **548** (56.3%)
- Away goals: **425** (43.7%)
- Home/away ratio: **1.289**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 302 | 233 | 535 | 56.4% | 43.6% |
| 2026 | 246 | 192 | 438 | 56.2% | 43.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **182** of `336` (54.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 182 | 99 | 54.4% |
| 2026 | 154 | 83 | 53.9% |

## 5. Clean sheets
- Home clean sheets: **99** (29.5%)
- Away clean sheets: **74** (22.0%)
- Total clean sheets recorded: **173**
- Matches with at least one clean sheet: **154** (45.8%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 182 | 58 | 36 | 94 | 83 (45.6%) |
| 2026 | 154 | 41 | 38 | 79 | 71 (46.1%) |

## 6. Scoring intensity
- First-half goals: **449** (46.1%)
- Second-half goals: **524** (53.9%)
- Avg first-half goals per match: **1.336**
- Avg second-half goals per match: **1.56**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **73** (21.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 182 | 245 | 290 | 45.8% | 54.2% |
| 2026 | 154 | 204 | 234 | 46.6% | 53.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `317` of `336` (94.3%)
- Goalless matches: `19`
- Min `1` | Max `97` | Mean `30.7` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 104 | 31.0% | 32.8% |
| 16-30 | 85 | 25.3% | 26.8% |
| 31-45 | 45 | 13.4% | 14.2% |
| 46-60 | 43 | 12.8% | 13.6% |
| 61-75 | 17 | 5.1% | 5.4% |
| 76-90 | 19 | 5.7% | 6.0% |
| 91-120 | 4 | 1.2% | 1.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\latvia\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\latvia\charts\goals_analysis_avg_per_season.png)

