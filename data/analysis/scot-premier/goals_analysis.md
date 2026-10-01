# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:06:01+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 6.9% |
| 1 | 46 | 16.7% |
| 2 | 67 | 24.3% |
| 3 | 63 | 22.8% |
| 4 | 48 | 17.4% |
| 5 | 17 | 6.2% |
| 6 | 11 | 4.0% |
| 7 | 3 | 1.1% |
| 8 | 1 | 0.4% |
| 9 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 234 | 643 | 1.573 | 1.175 | 2.748 |
| 2026-2027 | 42 | 107 | 1.19 | 1.357 | 2.548 |

## 3. Home vs away goal share
- Home goals: **418** (55.7%)
- Away goals: **332** (44.3%)
- Home/away ratio: **1.259**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 368 | 275 | 643 | 57.2% | 42.8% |
| 2026-2027 | 50 | 57 | 107 | 46.7% | 53.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **143** of `276` (51.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 234 | 121 | 51.7% |
| 2026-2027 | 42 | 22 | 52.4% |

## 5. Clean sheets
- Home clean sheets: **93** (33.7%)
- Away clean sheets: **59** (21.4%)
- Total clean sheets recorded: **152**
- Matches with at least one clean sheet: **133** (48.2%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 234 | 83 | 47 | 130 | 113 (48.3%) |
| 2026-2027 | 42 | 10 | 12 | 22 | 20 (47.6%) |

## 6. Scoring intensity
- First-half goals: **347** (46.3%)
- Second-half goals: **403** (53.7%)
- Avg first-half goals per match: **1.257**
- Avg second-half goals per match: **1.46**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **46** (16.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 234 | 291 | 352 | 45.3% | 54.7% |
| 2026-2027 | 42 | 56 | 51 | 52.3% | 47.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `257` of `276` (93.1%)
- Goalless matches: `19`
- Min `1` | Max `96` | Mean `29.15` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 80 | 29.0% | 31.1% |
| 16-30 | 79 | 28.6% | 30.7% |
| 31-45 | 50 | 18.1% | 19.5% |
| 46-60 | 22 | 8.0% | 8.6% |
| 61-75 | 14 | 5.1% | 5.4% |
| 76-90 | 7 | 2.5% | 2.7% |
| 91-120 | 5 | 1.8% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\scot-premier\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\scot-premier\charts\goals_analysis_avg_per_season.png)

