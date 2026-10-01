# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:11:21+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 8 | 5.2% |
| 1 | 22 | 14.4% |
| 2 | 34 | 22.2% |
| 3 | 42 | 27.5% |
| 4 | 21 | 13.7% |
| 5 | 7 | 4.6% |
| 6 | 6 | 3.9% |
| 7 | 6 | 3.9% |
| 8 | 5 | 3.3% |
| 9 | 2 | 1.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 135 | 410 | 1.504 | 1.533 | 3.037 |
| 2026-2027 | 18 | 61 | 1.667 | 1.722 | 3.389 |

## 3. Home vs away goal share
- Home goals: **233** (49.5%)
- Away goals: **238** (50.5%)
- Home/away ratio: **0.979**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 203 | 207 | 410 | 49.5% | 50.5% |
| 2026-2027 | 30 | 31 | 61 | 49.2% | 50.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **70** of `153` (45.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 135 | 61 | 45.2% |
| 2026-2027 | 18 | 9 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **43** (28.1%)
- Away clean sheets: **48** (31.4%)
- Total clean sheets recorded: **91**
- Matches with at least one clean sheet: **83** (54.2%)
- Both teams kept clean sheets (0-0): **8**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 135 | 37 | 44 | 81 | 74 (54.8%) |
| 2026-2027 | 18 | 6 | 4 | 10 | 9 (50.0%) |

## 6. Scoring intensity
- First-half goals: **212** (46.2%)
- Second-half goals: **247** (53.8%)
- Avg first-half goals per match: **1.423**
- Avg second-half goals per match: **1.658**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **26** (17.0%)
- *4 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 135 | 178 | 220 | 44.7% | 55.3% |
| 2026-2027 | 18 | 34 | 27 | 55.7% | 44.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `141` of `153` (92.2%)
- Goalless matches: `12`
- Min `1` | Max `97` | Mean `27.11` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 55 | 35.9% | 39.0% |
| 16-30 | 34 | 22.2% | 24.1% |
| 31-45 | 22 | 14.4% | 15.6% |
| 46-60 | 20 | 13.1% | 14.2% |
| 61-75 | 6 | 3.9% | 4.3% |
| 76-90 | 3 | 2.0% | 2.1% |
| 91-120 | 1 | 0.7% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wfrance1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wfrance1\charts\goals_analysis_avg_per_season.png)

