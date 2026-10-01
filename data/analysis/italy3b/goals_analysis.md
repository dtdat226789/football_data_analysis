# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:58:30+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 41 | 9.6% |
| 1 | 93 | 21.8% |
| 2 | 119 | 27.9% |
| 3 | 93 | 21.8% |
| 4 | 47 | 11.0% |
| 5 | 20 | 4.7% |
| 6 | 12 | 2.8% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 802 | 1.165 | 1.081 | 2.246 |
| 2026-2027 | 69 | 177 | 1.464 | 1.101 | 2.565 |

## 3. Home vs away goal share
- Home goals: **517** (52.8%)
- Away goals: **462** (47.2%)
- Home/away ratio: **1.119**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 416 | 386 | 802 | 51.9% | 48.1% |
| 2026-2027 | 101 | 76 | 177 | 57.1% | 42.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **212** of `426` (49.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 357 | 173 | 48.5% |
| 2026-2027 | 69 | 39 | 56.5% |

## 5. Clean sheets
- Home clean sheets: **138** (32.4%)
- Away clean sheets: **117** (27.5%)
- Total clean sheets recorded: **255**
- Matches with at least one clean sheet: **214** (50.2%)
- Both teams kept clean sheets (0-0): **41**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 115 | 104 | 219 | 184 (51.5%) |
| 2026-2027 | 69 | 23 | 13 | 36 | 30 (43.5%) |

## 6. Scoring intensity
- First-half goals: **441** (45.0%)
- Second-half goals: **538** (55.0%)
- Avg first-half goals per match: **1.035**
- Avg second-half goals per match: **1.263**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **113** (26.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 358 | 444 | 44.6% | 55.4% |
| 2026-2027 | 69 | 83 | 94 | 46.9% | 53.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `385` of `426` (90.4%)
- Goalless matches: `41`
- Min `1` | Max `97` | Mean `34.35` | Median (p50) `31`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 98 | 23.0% | 25.5% |
| 16-30 | 89 | 20.9% | 23.1% |
| 31-45 | 76 | 17.8% | 19.7% |
| 46-60 | 59 | 13.8% | 15.3% |
| 61-75 | 40 | 9.4% | 10.4% |
| 76-90 | 16 | 3.8% | 4.2% |
| 91-120 | 7 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy3b\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy3b\charts\goals_analysis_avg_per_season.png)

