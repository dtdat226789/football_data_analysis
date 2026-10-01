# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:48:15+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 1 | 2.5% |
| 1 | 2 | 5.0% |
| 2 | 7 | 17.5% |
| 3 | 5 | 12.5% |
| 4 | 11 | 27.5% |
| 5 | 4 | 10.0% |
| 6 | 5 | 12.5% |
| 7 | 3 | 7.5% |
| 8 | 1 | 2.5% |
| 9 | 0 | 0.0% |
| 10 | 1 | 2.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2026-2027 | 40 | 164 | 2.325 | 1.775 | 4.1 |

## 3. Home vs away goal share
- Home goals: **93** (56.7%)
- Away goals: **71** (43.3%)
- Home/away ratio: **1.31**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2026-2027 | 93 | 71 | 164 | 56.7% | 43.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **28** of `40` (70.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2026-2027 | 40 | 28 | 70.0% |

## 5. Clean sheets
- Home clean sheets: **6** (15.0%)
- Away clean sheets: **7** (17.5%)
- Total clean sheets recorded: **13**
- Matches with at least one clean sheet: **12** (30.0%)
- Both teams kept clean sheets (0-0): **1**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2026-2027 | 40 | 6 | 7 | 13 | 12 (30.0%) |

## 6. Scoring intensity
- First-half goals: **84** (51.2%)
- Second-half goals: **80** (48.8%)
- Avg first-half goals per match: **2.1**
- Avg second-half goals per match: **2.0**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **3** (7.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2026-2027 | 40 | 84 | 80 | 51.2% | 48.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `39` of `40` (97.5%)
- Goalless matches: `1`
- Min `1` | Max `67` | Mean `23.56` | Median (p50) `20`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 12 | 30.0% | 30.8% |
| 16-30 | 16 | 40.0% | 41.0% |
| 31-45 | 8 | 20.0% | 20.5% |
| 46-60 | 1 | 2.5% | 2.6% |
| 61-75 | 2 | 5.0% | 5.1% |
| 76-90 | 0 | 0.0% | 0.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\develop21\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\develop21\charts\goals_analysis_avg_per_season.png)

