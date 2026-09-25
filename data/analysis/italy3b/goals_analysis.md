# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:19+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 40 | 9.6% |
| 1 | 92 | 22.1% |
| 2 | 117 | 28.1% |
| 3 | 90 | 21.6% |
| 4 | 46 | 11.0% |
| 5 | 19 | 4.6% |
| 6 | 12 | 2.9% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 802 | 1.165 | 1.081 | 2.246 |
| 2026-2027 | 60 | 154 | 1.5 | 1.067 | 2.567 |

## 3. Home vs away goal share
- Home goals: **506** (52.9%)
- Away goals: **450** (47.1%)
- Home/away ratio: **1.124**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 416 | 386 | 802 | 51.9% | 48.1% |
| 2026-2027 | 90 | 64 | 154 | 58.4% | 41.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **207** of `417` (49.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 357 | 173 | 48.5% |
| 2026-2027 | 60 | 34 | 56.7% |

## 5. Clean sheets
- Home clean sheets: **135** (32.4%)
- Away clean sheets: **115** (27.6%)
- Total clean sheets recorded: **250**
- Matches with at least one clean sheet: **210** (50.4%)
- Both teams kept clean sheets (0-0): **40**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 115 | 104 | 219 | 184 (51.5%) |
| 2026-2027 | 60 | 20 | 11 | 31 | 26 (43.3%) |

## 6. Scoring intensity
- First-half goals: **429** (44.9%)
- Second-half goals: **527** (55.1%)
- Avg first-half goals per match: **1.029**
- Avg second-half goals per match: **1.264**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **111** (26.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 357 | 358 | 444 | 44.6% | 55.4% |
| 2026-2027 | 60 | 71 | 83 | 46.1% | 53.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `377` of `417` (90.4%)
- Goalless matches: `40`
- Min `1` | Max `97` | Mean `34.51` | Median (p50) `31`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 94 | 22.5% | 24.9% |
| 16-30 | 88 | 21.1% | 23.3% |
| 31-45 | 76 | 18.2% | 20.2% |
| 46-60 | 57 | 13.7% | 15.1% |
| 61-75 | 39 | 9.4% | 10.3% |
| 76-90 | 16 | 3.8% | 4.2% |
| 91-120 | 7 | 1.7% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy3b\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy3b\charts\goals_analysis_avg_per_season.png)

