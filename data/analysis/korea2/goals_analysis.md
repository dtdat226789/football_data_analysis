# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:57+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 42 | 8.5% |
| 1 | 97 | 19.7% |
| 2 | 117 | 23.7% |
| 3 | 95 | 19.3% |
| 4 | 79 | 16.0% |
| 5 | 43 | 8.7% |
| 6 | 14 | 2.8% |
| 7 | 5 | 1.0% |
| 8 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 273 | 686 | 1.319 | 1.194 | 2.513 |
| 2026 | 220 | 588 | 1.373 | 1.3 | 2.673 |

## 3. Home vs away goal share
- Home goals: **662** (52.0%)
- Away goals: **612** (48.0%)
- Home/away ratio: **1.082**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 360 | 326 | 686 | 52.5% | 47.5% |
| 2026 | 302 | 286 | 588 | 51.4% | 48.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **269** of `493` (54.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 273 | 135 | 49.5% |
| 2026 | 220 | 134 | 60.9% |

## 5. Clean sheets
- Home clean sheets: **134** (27.2%)
- Away clean sheets: **132** (26.8%)
- Total clean sheets recorded: **266**
- Matches with at least one clean sheet: **224** (45.4%)
- Both teams kept clean sheets (0-0): **42**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 273 | 78 | 86 | 164 | 138 (50.5%) |
| 2026 | 220 | 56 | 46 | 102 | 86 (39.1%) |

## 6. Scoring intensity
- First-half goals: **527** (41.4%)
- Second-half goals: **747** (58.6%)
- Avg first-half goals per match: **1.069**
- Avg second-half goals per match: **1.515**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **126** (25.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 273 | 283 | 403 | 41.3% | 58.7% |
| 2026 | 220 | 244 | 344 | 41.5% | 58.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `451` of `493` (91.5%)
- Goalless matches: `42`
- Min `1` | Max `97` | Mean `34.8` | Median (p50) `30`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 134 | 27.2% | 29.7% |
| 16-30 | 92 | 18.7% | 20.4% |
| 31-45 | 83 | 16.8% | 18.4% |
| 46-60 | 65 | 13.2% | 14.4% |
| 61-75 | 38 | 7.7% | 8.4% |
| 76-90 | 30 | 6.1% | 6.7% |
| 91-120 | 9 | 1.8% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\korea2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\korea2\charts\goals_analysis_avg_per_season.png)

