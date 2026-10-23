# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:59:00+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 3 | 1.2% |
| 1 | 47 | 19.5% |
| 2 | 44 | 18.3% |
| 3 | 86 | 35.7% |
| 4 | 18 | 7.5% |
| 5 | 30 | 12.4% |
| 6 | 8 | 3.3% |
| 7 | 4 | 1.7% |
| 8 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2026 | 161 | 462 | 1.54 | 1.329 | 2.87 |
| 2026-2027 | 80 | 237 | 1.587 | 1.375 | 2.962 |

## 3. Home vs away goal share
- Home goals: **375** (53.6%)
- Away goals: **324** (46.4%)
- Home/away ratio: **1.157**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2026 | 248 | 214 | 462 | 53.7% | 46.3% |
| 2026-2027 | 127 | 110 | 237 | 53.6% | 46.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **137** of `241` (56.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2026 | 161 | 89 | 55.3% |
| 2026-2027 | 80 | 48 | 60.0% |

## 5. Clean sheets
- Home clean sheets: **63** (26.1%)
- Away clean sheets: **44** (18.3%)
- Total clean sheets recorded: **107**
- Matches with at least one clean sheet: **104** (43.2%)
- Both teams kept clean sheets (0-0): **3**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2026 | 161 | 45 | 27 | 72 | 72 (44.7%) |
| 2026-2027 | 80 | 18 | 17 | 35 | 32 (40.0%) |

## 6. Scoring intensity
- First-half goals: **275** (39.3%)
- Second-half goals: **424** (60.7%)
- Avg first-half goals per match: **1.141**
- Avg second-half goals per match: **1.759**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **79** (32.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2026 | 161 | 175 | 287 | 37.9% | 62.1% |
| 2026-2027 | 80 | 100 | 137 | 42.2% | 57.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `238` of `241` (98.8%)
- Goalless matches: `3`
- Min `1` | Max `93` | Mean `34.22` | Median (p50) `31.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 66 | 27.4% | 27.7% |
| 16-30 | 51 | 21.2% | 21.4% |
| 31-45 | 46 | 19.1% | 19.3% |
| 46-60 | 41 | 17.0% | 17.2% |
| 61-75 | 19 | 7.9% | 8.0% |
| 76-90 | 14 | 5.8% | 5.9% |
| 91-120 | 1 | 0.4% | 0.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\japan1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\japan1\charts\goals_analysis_avg_per_season.png)

