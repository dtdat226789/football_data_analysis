# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:45:04+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 28 | 7.3% |
| 1 | 61 | 15.9% |
| 2 | 96 | 25.0% |
| 3 | 91 | 23.7% |
| 4 | 54 | 14.1% |
| 5 | 33 | 8.6% |
| 6 | 13 | 3.4% |
| 7 | 4 | 1.0% |
| 8 | 2 | 0.5% |
| 9 | 0 | 0.0% |
| 10 | 2 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 864 | 1.449 | 1.243 | 2.692 |
| 2026-2027 | 63 | 185 | 1.698 | 1.238 | 2.937 |

## 3. Home vs away goal share
- Home goals: **572** (54.5%)
- Away goals: **477** (45.5%)
- Home/away ratio: **1.199**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 465 | 399 | 864 | 53.8% | 46.2% |
| 2026-2027 | 107 | 78 | 185 | 57.8% | 42.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **200** of `384` (52.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 321 | 175 | 54.5% |
| 2026-2027 | 63 | 25 | 39.7% |

## 5. Clean sheets
- Home clean sheets: **122** (31.8%)
- Away clean sheets: **90** (23.4%)
- Total clean sheets recorded: **212**
- Matches with at least one clean sheet: **184** (47.9%)
- Both teams kept clean sheets (0-0): **28**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 97 | 74 | 171 | 146 (45.5%) |
| 2026-2027 | 63 | 25 | 16 | 41 | 38 (60.3%) |

## 6. Scoring intensity
- First-half goals: **473** (45.1%)
- Second-half goals: **576** (54.9%)
- Avg first-half goals per match: **1.232**
- Avg second-half goals per match: **1.5**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **80** (20.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 391 | 473 | 45.3% | 54.7% |
| 2026-2027 | 63 | 82 | 103 | 44.3% | 55.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `356` of `384` (92.7%)
- Goalless matches: `28`
- Min `1` | Max `93` | Mean `30.46` | Median (p50) `24.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 123 | 32.0% | 34.6% |
| 16-30 | 84 | 21.9% | 23.6% |
| 31-45 | 64 | 16.7% | 18.0% |
| 46-60 | 37 | 9.6% | 10.4% |
| 61-75 | 27 | 7.0% | 7.6% |
| 76-90 | 17 | 4.4% | 4.8% |
| 91-120 | 4 | 1.0% | 1.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\belgium1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\belgium1\charts\goals_analysis_avg_per_season.png)

