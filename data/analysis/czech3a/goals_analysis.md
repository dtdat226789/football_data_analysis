# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:56:37+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 24 | 7.3% |
| 1 | 44 | 13.3% |
| 2 | 61 | 18.5% |
| 3 | 55 | 16.7% |
| 4 | 74 | 22.4% |
| 5 | 33 | 10.0% |
| 6 | 18 | 5.5% |
| 7 | 14 | 4.2% |
| 8 | 5 | 1.5% |
| 9 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 869 | 1.706 | 1.489 | 3.195 |
| 2026-2027 | 58 | 187 | 1.81 | 1.414 | 3.224 |

## 3. Home vs away goal share
- Home goals: **569** (53.9%)
- Away goals: **487** (46.1%)
- Home/away ratio: **1.168**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 464 | 405 | 869 | 53.4% | 46.6% |
| 2026-2027 | 105 | 82 | 187 | 56.1% | 43.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **187** of `330` (56.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 272 | 156 | 57.4% |
| 2026-2027 | 58 | 31 | 53.4% |

## 5. Clean sheets
- Home clean sheets: **91** (27.6%)
- Away clean sheets: **76** (23.0%)
- Total clean sheets recorded: **167**
- Matches with at least one clean sheet: **143** (43.3%)
- Both teams kept clean sheets (0-0): **24**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 73 | 60 | 133 | 116 (42.6%) |
| 2026-2027 | 58 | 18 | 16 | 34 | 27 (46.6%) |

## 6. Scoring intensity
- First-half goals: **496** (47.0%)
- Second-half goals: **560** (53.0%)
- Avg first-half goals per match: **1.508**
- Avg second-half goals per match: **1.702**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **58** (17.6%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 408 | 461 | 47.0% | 53.0% |
| 2026-2027 | 58 | 88 | 99 | 47.1% | 52.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `306` of `330` (92.7%)
- Goalless matches: `24`
- Min `1` | Max `94` | Mean `26.65` | Median (p50) `19.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 127 | 38.5% | 41.5% |
| 16-30 | 73 | 22.1% | 23.9% |
| 31-45 | 44 | 13.3% | 14.4% |
| 46-60 | 36 | 10.9% | 11.8% |
| 61-75 | 12 | 3.6% | 3.9% |
| 76-90 | 13 | 3.9% | 4.2% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech3a\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech3a\charts\goals_analysis_avg_per_season.png)

