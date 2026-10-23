# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:01:43+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 51 | 10.5% |
| 1 | 98 | 20.1% |
| 2 | 145 | 29.7% |
| 3 | 114 | 23.4% |
| 4 | 50 | 10.2% |
| 5 | 19 | 3.9% |
| 6 | 8 | 1.6% |
| 7 | 3 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2024-2025 | 240 | 555 | 1.242 | 1.071 | 2.312 |
| 2025-2026 | 248 | 539 | 1.149 | 1.024 | 2.173 |

## 3. Home vs away goal share
- Home goals: **583** (53.3%)
- Away goals: **511** (46.7%)
- Home/away ratio: **1.141**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2024-2025 | 298 | 257 | 555 | 53.7% | 46.3% |
| 2025-2026 | 285 | 254 | 539 | 52.9% | 47.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **236** of `488` (48.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2024-2025 | 240 | 107 | 44.6% |
| 2025-2026 | 248 | 129 | 52.0% |

## 5. Clean sheets
- Home clean sheets: **175** (35.9%)
- Away clean sheets: **128** (26.2%)
- Total clean sheets recorded: **303**
- Matches with at least one clean sheet: **252** (51.6%)
- Both teams kept clean sheets (0-0): **51**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2024-2025 | 240 | 89 | 66 | 155 | 133 (55.4%) |
| 2025-2026 | 248 | 86 | 62 | 148 | 119 (48.0%) |

## 6. Scoring intensity
- First-half goals: **478** (43.7%)
- Second-half goals: **616** (56.3%)
- Avg first-half goals per match: **0.98**
- Avg second-half goals per match: **1.262**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **129** (26.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2024-2025 | 240 | 228 | 327 | 41.1% | 58.9% |
| 2025-2026 | 248 | 250 | 289 | 46.4% | 53.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `437` of `488` (89.5%)
- Goalless matches: `51`
- Min `1` | Max `99` | Mean `36.07` | Median (p50) `33`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 106 | 21.7% | 24.3% |
| 16-30 | 100 | 20.5% | 22.9% |
| 31-45 | 76 | 15.6% | 17.4% |
| 46-60 | 82 | 16.8% | 18.8% |
| 61-75 | 36 | 7.4% | 8.2% |
| 76-90 | 25 | 5.1% | 5.7% |
| 91-120 | 12 | 2.5% | 2.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\morocco\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\morocco\charts\goals_analysis_avg_per_season.png)

