# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:00:44+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 10 | 2.7% |
| 1 | 42 | 11.2% |
| 2 | 75 | 19.9% |
| 3 | 90 | 23.9% |
| 4 | 73 | 19.4% |
| 5 | 43 | 11.4% |
| 6 | 23 | 6.1% |
| 7 | 14 | 3.7% |
| 8 | 4 | 1.1% |
| 9 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 1069 | 1.814 | 1.506 | 3.32 |
| 2026-2027 | 54 | 186 | 1.796 | 1.648 | 3.444 |

## 3. Home vs away goal share
- Home goals: **681** (54.3%)
- Away goals: **574** (45.7%)
- Home/away ratio: **1.186**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 584 | 485 | 1069 | 54.6% | 45.4% |
| 2026-2027 | 97 | 89 | 186 | 52.2% | 47.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **234** of `376` (62.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 322 | 196 | 60.9% |
| 2026-2027 | 54 | 38 | 70.4% |

## 5. Clean sheets
- Home clean sheets: **91** (24.2%)
- Away clean sheets: **61** (16.2%)
- Total clean sheets recorded: **152**
- Matches with at least one clean sheet: **142** (37.8%)
- Both teams kept clean sheets (0-0): **10**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 84 | 52 | 136 | 126 (39.1%) |
| 2026-2027 | 54 | 7 | 9 | 16 | 16 (29.6%) |

## 6. Scoring intensity
- First-half goals: **553** (44.1%)
- Second-half goals: **700** (55.9%)
- Avg first-half goals per match: **1.475**
- Avg second-half goals per match: **1.867**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **69** (18.4%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 473 | 596 | 44.2% | 55.8% |
| 2026-2027 | 54 | 80 | 104 | 43.5% | 56.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `365` of `376` (97.1%)
- Goalless matches: `11`
- Min `1` | Max `94` | Mean `28.11` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 122 | 32.4% | 33.4% |
| 16-30 | 102 | 27.1% | 27.9% |
| 31-45 | 63 | 16.8% | 17.3% |
| 46-60 | 45 | 12.0% | 12.3% |
| 61-75 | 23 | 6.1% | 6.3% |
| 76-90 | 6 | 1.6% | 1.6% |
| 91-120 | 4 | 1.1% | 1.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\holland3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\holland3\charts\goals_analysis_avg_per_season.png)

