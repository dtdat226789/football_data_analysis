# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:01:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 4.3% |
| 1 | 105 | 15.5% |
| 2 | 152 | 22.5% |
| 3 | 171 | 25.3% |
| 4 | 97 | 14.3% |
| 5 | 72 | 10.6% |
| 6 | 34 | 5.0% |
| 7 | 10 | 1.5% |
| 8 | 6 | 0.9% |
| 9 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1626 | 1.585 | 1.334 | 2.919 |
| 2026-2027 | 120 | 375 | 1.692 | 1.433 | 3.125 |

## 3. Home vs away goal share
- Home goals: **1086** (54.3%)
- Away goals: **915** (45.7%)
- Home/away ratio: **1.187**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 883 | 743 | 1626 | 54.3% | 45.7% |
| 2026-2027 | 203 | 172 | 375 | 54.1% | 45.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **392** of `677` (57.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 314 | 56.4% |
| 2026-2027 | 120 | 78 | 65.0% |

## 5. Clean sheets
- Home clean sheets: **177** (26.1%)
- Away clean sheets: **137** (20.2%)
- Total clean sheets recorded: **314**
- Matches with at least one clean sheet: **285** (42.1%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 150 | 121 | 271 | 243 (43.6%) |
| 2026-2027 | 120 | 27 | 16 | 43 | 42 (35.0%) |

## 6. Scoring intensity
- First-half goals: **855** (42.8%)
- Second-half goals: **1143** (57.2%)
- Avg first-half goals per match: **1.265**
- Avg second-half goals per match: **1.691**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **164** (24.2%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 707 | 916 | 43.6% | 56.4% |
| 2026-2027 | 120 | 148 | 227 | 39.5% | 60.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `647` of `677` (95.6%)
- Goalless matches: `30`
- Min `1` | Max `108` | Mean `31.58` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 210 | 31.0% | 32.5% |
| 16-30 | 164 | 24.2% | 25.3% |
| 31-45 | 93 | 13.7% | 14.4% |
| 46-60 | 90 | 13.3% | 13.9% |
| 61-75 | 47 | 6.9% | 7.3% |
| 76-90 | 27 | 4.0% | 4.2% |
| 91-120 | 16 | 2.4% | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\national\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\national\charts\goals_analysis_avg_per_season.png)

