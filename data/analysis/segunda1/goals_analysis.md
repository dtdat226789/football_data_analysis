# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:45:24+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.7% |
| 1 | 72 | 21.6% |
| 2 | 70 | 21.0% |
| 3 | 81 | 24.3% |
| 4 | 43 | 12.9% |
| 5 | 20 | 6.0% |
| 6 | 9 | 2.7% |
| 7 | 7 | 2.1% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 776 | 1.392 | 1.144 | 2.536 |
| 2026-2027 | 27 | 71 | 1.296 | 1.333 | 2.63 |

## 3. Home vs away goal share
- Home goals: **461** (54.4%)
- Away goals: **386** (45.6%)
- Home/away ratio: **1.194**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 426 | 350 | 776 | 54.9% | 45.1% |
| 2026-2027 | 35 | 36 | 71 | 49.3% | 50.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **167** of `333` (50.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 156 | 51.0% |
| 2026-2027 | 27 | 11 | 40.7% |

## 5. Clean sheets
- Home clean sheets: **107** (32.1%)
- Away clean sheets: **88** (26.4%)
- Total clean sheets recorded: **195**
- Matches with at least one clean sheet: **166** (49.8%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 100 | 78 | 178 | 150 (49.0%) |
| 2026-2027 | 27 | 7 | 10 | 17 | 16 (59.3%) |

## 6. Scoring intensity
- First-half goals: **370** (43.8%)
- Second-half goals: **474** (56.2%)
- Avg first-half goals per match: **1.114**
- Avg second-half goals per match: **1.428**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **82** (24.6%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 340 | 433 | 44.0% | 56.0% |
| 2026-2027 | 27 | 30 | 41 | 42.3% | 57.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `303` of `333` (91.0%)
- Goalless matches: `30`
- Min `1` | Max `96` | Mean `32.49` | Median (p50) `28`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 106 | 31.8% | 35.0% |
| 16-30 | 58 | 17.4% | 19.1% |
| 31-45 | 57 | 17.1% | 18.8% |
| 46-60 | 37 | 11.1% | 12.2% |
| 61-75 | 23 | 6.9% | 7.6% |
| 76-90 | 13 | 3.9% | 4.3% |
| 91-120 | 9 | 2.7% | 3.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\segunda1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\segunda1\charts\goals_analysis_avg_per_season.png)

