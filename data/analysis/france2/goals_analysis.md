# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:58:48+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 40 | 10.7% |
| 1 | 81 | 21.7% |
| 2 | 77 | 20.6% |
| 3 | 75 | 20.1% |
| 4 | 54 | 14.5% |
| 5 | 21 | 5.6% |
| 6 | 14 | 3.8% |
| 7 | 7 | 1.9% |
| 8 | 4 | 1.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 784 | 1.313 | 1.216 | 2.529 |
| 2026-2027 | 63 | 162 | 1.333 | 1.238 | 2.571 |

## 3. Home vs away goal share
- Home goals: **491** (51.9%)
- Away goals: **455** (48.1%)
- Home/away ratio: **1.079**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 407 | 377 | 784 | 51.9% | 48.1% |
| 2026-2027 | 84 | 78 | 162 | 51.9% | 48.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **197** of `373` (52.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 310 | 160 | 51.6% |
| 2026-2027 | 63 | 37 | 58.7% |

## 5. Clean sheets
- Home clean sheets: **116** (31.1%)
- Away clean sheets: **100** (26.8%)
- Total clean sheets recorded: **216**
- Matches with at least one clean sheet: **176** (47.2%)
- Both teams kept clean sheets (0-0): **40**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 99 | 84 | 183 | 150 (48.4%) |
| 2026-2027 | 63 | 17 | 16 | 33 | 26 (41.3%) |

## 6. Scoring intensity
- First-half goals: **431** (45.6%)
- Second-half goals: **515** (54.4%)
- Avg first-half goals per match: **1.159**
- Avg second-half goals per match: **1.384**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **90** (24.1%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 310 | 365 | 419 | 46.6% | 53.4% |
| 2026-2027 | 63 | 66 | 96 | 40.7% | 59.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `333` of `373` (89.3%)
- Goalless matches: `40`
- Min `1` | Max `94` | Mean `31.13` | Median (p50) `25`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 106 | 28.4% | 31.8% |
| 16-30 | 88 | 23.6% | 26.4% |
| 31-45 | 46 | 12.3% | 13.8% |
| 46-60 | 47 | 12.6% | 14.1% |
| 61-75 | 26 | 7.0% | 7.8% |
| 76-90 | 17 | 4.6% | 5.1% |
| 91-120 | 3 | 0.8% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\france2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\france2\charts\goals_analysis_avg_per_season.png)

