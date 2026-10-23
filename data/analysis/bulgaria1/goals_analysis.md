# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:45:55+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 39 | 10.7% |
| 1 | 72 | 19.8% |
| 2 | 88 | 24.2% |
| 3 | 86 | 23.7% |
| 4 | 47 | 12.9% |
| 5 | 24 | 6.6% |
| 6 | 4 | 1.1% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 294 | 677 | 1.255 | 1.048 | 2.303 |
| 2026-2027 | 69 | 184 | 1.478 | 1.188 | 2.667 |

## 3. Home vs away goal share
- Home goals: **471** (54.7%)
- Away goals: **390** (45.3%)
- Home/away ratio: **1.208**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 369 | 308 | 677 | 54.5% | 45.5% |
| 2026-2027 | 102 | 82 | 184 | 55.4% | 44.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **165** of `363` (45.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 294 | 126 | 42.9% |
| 2026-2027 | 69 | 39 | 56.5% |

## 5. Clean sheets
- Home clean sheets: **135** (37.2%)
- Away clean sheets: **102** (28.1%)
- Total clean sheets recorded: **237**
- Matches with at least one clean sheet: **198** (54.5%)
- Both teams kept clean sheets (0-0): **39**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 294 | 116 | 88 | 204 | 168 (57.1%) |
| 2026-2027 | 69 | 19 | 14 | 33 | 30 (43.5%) |

## 6. Scoring intensity
- First-half goals: **364** (42.5%)
- Second-half goals: **493** (57.5%)
- Avg first-half goals per match: **1.006**
- Avg second-half goals per match: **1.362**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **90** (24.8%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 294 | 291 | 382 | 43.2% | 56.8% |
| 2026-2027 | 69 | 73 | 111 | 39.7% | 60.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `323` of `363` (89.0%)
- Goalless matches: `40`
- Min `1` | Max `96` | Mean `33.35` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 97 | 26.7% | 30.0% |
| 16-30 | 71 | 19.6% | 22.0% |
| 31-45 | 56 | 15.4% | 17.3% |
| 46-60 | 48 | 13.2% | 14.9% |
| 61-75 | 32 | 8.8% | 9.9% |
| 76-90 | 14 | 3.9% | 4.3% |
| 91-120 | 5 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\bulgaria1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\bulgaria1\charts\goals_analysis_avg_per_season.png)

