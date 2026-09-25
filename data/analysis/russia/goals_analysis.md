# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:43:25+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 21 | 6.6% |
| 1 | 60 | 18.8% |
| 2 | 85 | 26.6% |
| 3 | 73 | 22.8% |
| 4 | 46 | 14.4% |
| 5 | 20 | 6.2% |
| 6 | 12 | 3.8% |
| 7 | 2 | 0.6% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 244 | 615 | 1.434 | 1.086 | 2.52 |
| 2026-2027 | 76 | 212 | 1.408 | 1.382 | 2.789 |

## 3. Home vs away goal share
- Home goals: **457** (55.3%)
- Away goals: **370** (44.7%)
- Home/away ratio: **1.235**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 350 | 265 | 615 | 56.9% | 43.1% |
| 2026-2027 | 107 | 105 | 212 | 50.5% | 49.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **174** of `320` (54.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 244 | 125 | 51.2% |
| 2026-2027 | 76 | 49 | 64.5% |

## 5. Clean sheets
- Home clean sheets: **98** (30.6%)
- Away clean sheets: **69** (21.6%)
- Total clean sheets recorded: **167**
- Matches with at least one clean sheet: **146** (45.6%)
- Both teams kept clean sheets (0-0): **21**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 244 | 81 | 53 | 134 | 119 (48.8%) |
| 2026-2027 | 76 | 17 | 16 | 33 | 27 (35.5%) |

## 6. Scoring intensity
- First-half goals: **368** (44.5%)
- Second-half goals: **459** (55.5%)
- Avg first-half goals per match: **1.15**
- Avg second-half goals per match: **1.434**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **74** (23.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 244 | 285 | 330 | 46.3% | 53.7% |
| 2026-2027 | 76 | 83 | 129 | 39.2% | 60.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `299` of `320` (93.4%)
- Goalless matches: `21`
- Min `1` | Max `95` | Mean `31.51` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 102 | 31.9% | 34.1% |
| 16-30 | 68 | 21.2% | 22.7% |
| 31-45 | 49 | 15.3% | 16.4% |
| 46-60 | 38 | 11.9% | 12.7% |
| 61-75 | 21 | 6.6% | 7.0% |
| 76-90 | 16 | 5.0% | 5.4% |
| 91-120 | 5 | 1.6% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\russia\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\russia\charts\goals_analysis_avg_per_season.png)

