# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:58:37+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.2% |
| 1 | 67 | 18.9% |
| 2 | 69 | 19.4% |
| 3 | 73 | 20.6% |
| 4 | 59 | 16.6% |
| 5 | 31 | 8.7% |
| 6 | 11 | 3.1% |
| 7 | 9 | 2.5% |
| 8 | 5 | 1.4% |
| 9 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 874 | 1.584 | 1.235 | 2.819 |
| 2026-2027 | 45 | 128 | 1.556 | 1.289 | 2.844 |

## 3. Home vs away goal share
- Home goals: **561** (56.0%)
- Away goals: **441** (44.0%)
- Home/away ratio: **1.272**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 491 | 383 | 874 | 56.2% | 43.8% |
| 2026-2027 | 70 | 58 | 128 | 54.7% | 45.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **184** of `355` (51.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 310 | 157 | 50.6% |
| 2026-2027 | 45 | 27 | 60.0% |

## 5. Clean sheets
- Home clean sheets: **118** (33.2%)
- Away clean sheets: **82** (23.1%)
- Total clean sheets recorded: **200**
- Matches with at least one clean sheet: **171** (48.2%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 106 | 72 | 178 | 153 (49.4%) |
| 2026-2027 | 45 | 12 | 10 | 22 | 18 (40.0%) |

## 6. Scoring intensity
- First-half goals: **427** (42.6%)
- Second-half goals: **575** (57.4%)
- Avg first-half goals per match: **1.206**
- Avg second-half goals per match: **1.624**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **80** (22.5%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 375 | 499 | 42.9% | 57.1% |
| 2026-2027 | 45 | 52 | 76 | 40.6% | 59.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `326` of `355` (91.8%)
- Goalless matches: `29`
- Min `1` | Max `94` | Mean `31.32` | Median (p50) `26.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 110 | 31.0% | 33.7% |
| 16-30 | 80 | 22.5% | 24.5% |
| 31-45 | 45 | 12.7% | 13.8% |
| 46-60 | 48 | 13.5% | 14.7% |
| 61-75 | 23 | 6.5% | 7.1% |
| 76-90 | 15 | 4.2% | 4.6% |
| 91-120 | 5 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\france1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\france1\charts\goals_analysis_avg_per_season.png)

