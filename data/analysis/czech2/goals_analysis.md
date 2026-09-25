# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:56:27+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 18 | 5.8% |
| 1 | 55 | 17.6% |
| 2 | 69 | 22.1% |
| 3 | 78 | 25.0% |
| 4 | 51 | 16.3% |
| 5 | 27 | 8.7% |
| 6 | 7 | 2.2% |
| 7 | 5 | 1.6% |
| 8 | 0 | 0.0% |
| 9 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 643 | 1.517 | 1.163 | 2.679 |
| 2026-2027 | 72 | 218 | 1.681 | 1.347 | 3.028 |

## 3. Home vs away goal share
- Home goals: **485** (56.3%)
- Away goals: **376** (43.7%)
- Home/away ratio: **1.29**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 364 | 279 | 643 | 56.6% | 43.4% |
| 2026-2027 | 121 | 97 | 218 | 55.5% | 44.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **168** of `312` (53.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 240 | 121 | 50.4% |
| 2026-2027 | 72 | 47 | 65.3% |

## 5. Clean sheets
- Home clean sheets: **89** (28.5%)
- Away clean sheets: **73** (23.4%)
- Total clean sheets recorded: **162**
- Matches with at least one clean sheet: **144** (46.2%)
- Both teams kept clean sheets (0-0): **18**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 71 | 62 | 133 | 119 (49.6%) |
| 2026-2027 | 72 | 18 | 11 | 29 | 25 (34.7%) |

## 6. Scoring intensity
- First-half goals: **416** (48.3%)
- Second-half goals: **445** (51.7%)
- Avg first-half goals per match: **1.333**
- Avg second-half goals per match: **1.426**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **63** (20.2%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 240 | 303 | 340 | 47.1% | 52.9% |
| 2026-2027 | 72 | 113 | 105 | 51.8% | 48.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `294` of `312` (94.2%)
- Goalless matches: `18`
- Min `1` | Max `90` | Mean `29.5` | Median (p50) `23.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 98 | 31.4% | 33.3% |
| 16-30 | 82 | 26.3% | 27.9% |
| 31-45 | 48 | 15.4% | 16.3% |
| 46-60 | 26 | 8.3% | 8.8% |
| 61-75 | 21 | 6.7% | 7.1% |
| 76-90 | 19 | 6.1% | 6.5% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech2\charts\goals_analysis_avg_per_season.png)

