# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:49:01+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 45 | 6.9% |
| 1 | 130 | 20.0% |
| 2 | 164 | 25.2% |
| 3 | 136 | 20.9% |
| 4 | 106 | 16.3% |
| 5 | 48 | 7.4% |
| 6 | 14 | 2.2% |
| 7 | 4 | 0.6% |
| 8 | 4 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 1434 | 1.372 | 1.203 | 2.575 |
| 2026-2027 | 94 | 240 | 1.574 | 0.979 | 2.553 |

## 3. Home vs away goal share
- Home goals: **912** (54.5%)
- Away goals: **762** (45.5%)
- Home/away ratio: **1.197**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 764 | 670 | 1434 | 53.3% | 46.7% |
| 2026-2027 | 148 | 92 | 240 | 61.7% | 38.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **343** of `651` (52.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 557 | 292 | 52.4% |
| 2026-2027 | 94 | 51 | 54.3% |

## 5. Clean sheets
- Home clean sheets: **202** (31.0%)
- Away clean sheets: **151** (23.2%)
- Total clean sheets recorded: **353**
- Matches with at least one clean sheet: **308** (47.3%)
- Both teams kept clean sheets (0-0): **45**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 165 | 137 | 302 | 265 (47.6%) |
| 2026-2027 | 94 | 37 | 14 | 51 | 43 (45.7%) |

## 6. Scoring intensity
- First-half goals: **743** (44.4%)
- Second-half goals: **931** (55.6%)
- Avg first-half goals per match: **1.141**
- Avg second-half goals per match: **1.43**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **167** (25.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 557 | 635 | 799 | 44.3% | 55.7% |
| 2026-2027 | 94 | 108 | 132 | 45.0% | 55.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `606` of `651` (93.1%)
- Goalless matches: `45`
- Min `1` | Max `103` | Mean `33.25` | Median (p50) `28.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 193 | 29.6% | 31.8% |
| 16-30 | 128 | 19.7% | 21.1% |
| 31-45 | 99 | 15.2% | 16.3% |
| 46-60 | 83 | 12.7% | 13.7% |
| 61-75 | 62 | 9.5% | 10.2% |
| 76-90 | 27 | 4.1% | 4.5% |
| 91-120 | 14 | 2.2% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\eng2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\eng2\charts\goals_analysis_avg_per_season.png)

