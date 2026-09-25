# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:41:50+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Liga Portugal 2 (Portugal)
- Scope: league `portugal2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 37 | 10.2% |
| 1 | 84 | 23.1% |
| 2 | 81 | 22.3% |
| 3 | 79 | 21.8% |
| 4 | 40 | 11.0% |
| 5 | 27 | 7.4% |
| 6 | 9 | 2.5% |
| 7 | 6 | 1.7% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 751 | 1.274 | 1.148 | 2.423 |
| 2026-2027 | 53 | 123 | 1.132 | 1.189 | 2.321 |

## 3. Home vs away goal share
- Home goals: **455** (52.1%)
- Away goals: **419** (47.9%)
- Home/away ratio: **1.086**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 395 | 356 | 751 | 52.6% | 47.4% |
| 2026-2027 | 60 | 63 | 123 | 48.8% | 51.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **164** of `363` (45.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 310 | 142 | 45.8% |
| 2026-2027 | 53 | 22 | 41.5% |

## 5. Clean sheets
- Home clean sheets: **132** (36.4%)
- Away clean sheets: **104** (28.7%)
- Total clean sheets recorded: **236**
- Matches with at least one clean sheet: **199** (54.8%)
- Both teams kept clean sheets (0-0): **37**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 113 | 88 | 201 | 168 (54.2%) |
| 2026-2027 | 53 | 19 | 16 | 35 | 31 (58.5%) |

## 6. Scoring intensity
- First-half goals: **377** (43.1%)
- Second-half goals: **497** (56.9%)
- Avg first-half goals per match: **1.039**
- Avg second-half goals per match: **1.369**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **87** (24.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 321 | 430 | 42.7% | 57.3% |
| 2026-2027 | 53 | 56 | 67 | 45.5% | 54.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `326` of `363` (89.8%)
- Goalless matches: `37`
- Min `1` | Max `101` | Mean `34.61` | Median (p50) `30.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 86 | 23.7% | 26.4% |
| 16-30 | 77 | 21.2% | 23.6% |
| 31-45 | 65 | 17.9% | 19.9% |
| 46-60 | 48 | 13.2% | 14.7% |
| 61-75 | 27 | 7.4% | 8.3% |
| 76-90 | 13 | 3.6% | 4.0% |
| 91-120 | 10 | 2.8% | 3.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\portugal2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\portugal2\charts\goals_analysis_avg_per_season.png)

