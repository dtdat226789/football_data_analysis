# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:03:44+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 4.4% |
| 1 | 103 | 15.5% |
| 2 | 152 | 22.9% |
| 3 | 168 | 25.3% |
| 4 | 96 | 14.4% |
| 5 | 70 | 10.5% |
| 6 | 31 | 4.7% |
| 7 | 9 | 1.4% |
| 8 | 6 | 0.9% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1626 | 1.585 | 1.334 | 2.919 |
| 2026-2027 | 108 | 325 | 1.611 | 1.398 | 3.009 |

## 3. Home vs away goal share
- Home goals: **1057** (54.2%)
- Away goals: **894** (45.8%)
- Home/away ratio: **1.182**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 883 | 743 | 1626 | 54.3% | 45.7% |
| 2026-2027 | 174 | 151 | 325 | 53.5% | 46.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **385** of `665` (57.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 314 | 56.4% |
| 2026-2027 | 108 | 71 | 65.7% |

## 5. Clean sheets
- Home clean sheets: **175** (26.3%)
- Away clean sheets: **134** (20.2%)
- Total clean sheets recorded: **309**
- Matches with at least one clean sheet: **280** (42.1%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 150 | 121 | 271 | 243 (43.6%) |
| 2026-2027 | 108 | 25 | 13 | 38 | 37 (34.3%) |

## 6. Scoring intensity
- First-half goals: **835** (42.9%)
- Second-half goals: **1113** (57.1%)
- Avg first-half goals per match: **1.258**
- Avg second-half goals per match: **1.676**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **161** (24.2%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 707 | 916 | 43.6% | 56.4% |
| 2026-2027 | 108 | 128 | 197 | 39.4% | 60.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `635` of `665` (95.5%)
- Goalless matches: `30`
- Min `1` | Max `108` | Mean `31.63` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 205 | 30.8% | 32.3% |
| 16-30 | 162 | 24.4% | 25.5% |
| 31-45 | 92 | 13.8% | 14.5% |
| 46-60 | 87 | 13.1% | 13.7% |
| 61-75 | 46 | 6.9% | 7.2% |
| 76-90 | 27 | 4.1% | 4.3% |
| 91-120 | 16 | 2.4% | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\national\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\national\charts\goals_analysis_avg_per_season.png)

