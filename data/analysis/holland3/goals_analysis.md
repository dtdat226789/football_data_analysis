# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:53:32+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 10 | 2.6% |
| 1 | 43 | 11.2% |
| 2 | 77 | 20.0% |
| 3 | 92 | 23.9% |
| 4 | 73 | 19.0% |
| 5 | 46 | 11.9% |
| 6 | 24 | 6.2% |
| 7 | 14 | 3.6% |
| 8 | 4 | 1.0% |
| 9 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 1069 | 1.814 | 1.506 | 3.32 |
| 2026-2027 | 63 | 218 | 1.873 | 1.587 | 3.46 |

## 3. Home vs away goal share
- Home goals: **702** (54.5%)
- Away goals: **585** (45.5%)
- Home/away ratio: **1.2**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 584 | 485 | 1069 | 54.6% | 45.4% |
| 2026-2027 | 118 | 100 | 218 | 54.1% | 45.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **238** of `385` (61.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 322 | 196 | 60.9% |
| 2026-2027 | 63 | 42 | 66.7% |

## 5. Clean sheets
- Home clean sheets: **95** (24.7%)
- Away clean sheets: **62** (16.1%)
- Total clean sheets recorded: **157**
- Matches with at least one clean sheet: **147** (38.2%)
- Both teams kept clean sheets (0-0): **10**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 84 | 52 | 136 | 126 (39.1%) |
| 2026-2027 | 63 | 11 | 10 | 21 | 21 (33.3%) |

## 6. Scoring intensity
- First-half goals: **562** (43.7%)
- Second-half goals: **723** (56.3%)
- Avg first-half goals per match: **1.464**
- Avg second-half goals per match: **1.883**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **73** (19.0%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 473 | 596 | 44.2% | 55.8% |
| 2026-2027 | 63 | 89 | 127 | 41.2% | 58.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `374` of `385` (97.1%)
- Goalless matches: `11`
- Min `1` | Max `94` | Mean `28.36` | Median (p50) `23.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 125 | 32.5% | 33.4% |
| 16-30 | 104 | 27.0% | 27.8% |
| 31-45 | 63 | 16.4% | 16.8% |
| 46-60 | 46 | 11.9% | 12.3% |
| 61-75 | 23 | 6.0% | 6.1% |
| 76-90 | 9 | 2.3% | 2.4% |
| 91-120 | 4 | 1.0% | 1.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\holland3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\holland3\charts\goals_analysis_avg_per_season.png)

