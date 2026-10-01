# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:47:21+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 24 | 7.1% |
| 1 | 44 | 13.1% |
| 2 | 64 | 19.0% |
| 3 | 55 | 16.3% |
| 4 | 75 | 22.3% |
| 5 | 35 | 10.4% |
| 6 | 18 | 5.3% |
| 7 | 14 | 4.2% |
| 8 | 5 | 1.5% |
| 9 | 3 | 0.9% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 869 | 1.706 | 1.489 | 3.195 |
| 2026-2027 | 65 | 216 | 1.831 | 1.492 | 3.323 |

## 3. Home vs away goal share
- Home goals: **583** (53.7%)
- Away goals: **502** (46.3%)
- Home/away ratio: **1.161**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 464 | 405 | 869 | 53.4% | 46.6% |
| 2026-2027 | 119 | 97 | 216 | 55.1% | 44.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **192** of `337` (57.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 272 | 156 | 57.4% |
| 2026-2027 | 65 | 36 | 55.4% |

## 5. Clean sheets
- Home clean sheets: **91** (27.0%)
- Away clean sheets: **78** (23.1%)
- Total clean sheets recorded: **169**
- Matches with at least one clean sheet: **145** (43.0%)
- Both teams kept clean sheets (0-0): **24**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 73 | 60 | 133 | 116 (42.6%) |
| 2026-2027 | 65 | 18 | 18 | 36 | 29 (44.6%) |

## 6. Scoring intensity
- First-half goals: **508** (46.8%)
- Second-half goals: **577** (53.2%)
- Avg first-half goals per match: **1.512**
- Avg second-half goals per match: **1.717**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **58** (17.2%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 408 | 461 | 47.0% | 53.0% |
| 2026-2027 | 65 | 100 | 116 | 46.3% | 53.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `313` of `337` (92.9%)
- Goalless matches: `24`
- Min `1` | Max `94` | Mean `26.37` | Median (p50) `19`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 130 | 38.6% | 41.5% |
| 16-30 | 77 | 22.8% | 24.6% |
| 31-45 | 44 | 13.1% | 14.1% |
| 46-60 | 36 | 10.7% | 11.5% |
| 61-75 | 12 | 3.6% | 3.8% |
| 76-90 | 13 | 3.9% | 4.2% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech3a\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech3a\charts\goals_analysis_avg_per_season.png)

