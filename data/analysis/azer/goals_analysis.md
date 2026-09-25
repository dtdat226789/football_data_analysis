# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:55:05+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 21 | 9.0% |
| 1 | 47 | 20.1% |
| 2 | 54 | 23.1% |
| 3 | 52 | 22.2% |
| 4 | 26 | 11.1% |
| 5 | 23 | 9.8% |
| 6 | 8 | 3.4% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 200 | 515 | 1.305 | 1.27 | 2.575 |
| 2026-2027 | 34 | 85 | 1.5 | 1.0 | 2.5 |

## 3. Home vs away goal share
- Home goals: **312** (52.0%)
- Away goals: **288** (48.0%)
- Home/away ratio: **1.083**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 261 | 254 | 515 | 50.7% | 49.3% |
| 2026-2027 | 51 | 34 | 85 | 60.0% | 40.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **106** of `234` (45.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 200 | 91 | 45.5% |
| 2026-2027 | 34 | 15 | 44.1% |

## 5. Clean sheets
- Home clean sheets: **76** (32.5%)
- Away clean sheets: **73** (31.2%)
- Total clean sheets recorded: **149**
- Matches with at least one clean sheet: **128** (54.7%)
- Both teams kept clean sheets (0-0): **21**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 200 | 63 | 64 | 127 | 109 (54.5%) |
| 2026-2027 | 34 | 13 | 9 | 22 | 19 (55.9%) |

## 6. Scoring intensity
- First-half goals: **261** (43.7%)
- Second-half goals: **336** (56.3%)
- Avg first-half goals per match: **1.125**
- Avg second-half goals per match: **1.448**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **60** (25.6%)
- *2 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 200 | 222 | 290 | 43.4% | 56.6% |
| 2026-2027 | 34 | 39 | 46 | 45.9% | 54.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `212` of `234` (90.6%)
- Goalless matches: `22`
- Min `1` | Max `99` | Mean `34.83` | Median (p50) `32.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 58 | 24.8% | 27.4% |
| 16-30 | 42 | 17.9% | 19.8% |
| 31-45 | 43 | 18.4% | 20.3% |
| 46-60 | 38 | 16.2% | 17.9% |
| 61-75 | 20 | 8.5% | 9.4% |
| 76-90 | 9 | 3.8% | 4.2% |
| 91-120 | 2 | 0.9% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\azer\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\azer\charts\goals_analysis_avg_per_season.png)

