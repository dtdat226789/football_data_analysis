# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:43:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Division 1 (Saudi Arabia)
- Scope: league `saudi2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 27 | 7.5% |
| 1 | 51 | 14.1% |
| 2 | 77 | 21.3% |
| 3 | 90 | 24.9% |
| 4 | 64 | 17.7% |
| 5 | 32 | 8.8% |
| 6 | 13 | 3.6% |
| 7 | 5 | 1.4% |
| 8 | 2 | 0.6% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 309 | 917 | 1.576 | 1.392 | 2.968 |
| 2026-2027 | 53 | 112 | 1.17 | 0.943 | 2.113 |

## 3. Home vs away goal share
- Home goals: **549** (53.4%)
- Away goals: **480** (46.6%)
- Home/away ratio: **1.144**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 487 | 430 | 917 | 53.1% | 46.9% |
| 2026-2027 | 62 | 50 | 112 | 55.4% | 44.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **215** of `362` (59.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 309 | 192 | 62.1% |
| 2026-2027 | 53 | 23 | 43.4% |

## 5. Clean sheets
- Home clean sheets: **90** (24.9%)
- Away clean sheets: **84** (23.2%)
- Total clean sheets recorded: **174**
- Matches with at least one clean sheet: **147** (40.6%)
- Both teams kept clean sheets (0-0): **27**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 309 | 70 | 63 | 133 | 117 (37.9%) |
| 2026-2027 | 53 | 20 | 21 | 41 | 30 (56.6%) |

## 6. Scoring intensity
- First-half goals: **451** (44.1%)
- Second-half goals: **572** (55.9%)
- Avg first-half goals per match: **1.253**
- Avg second-half goals per match: **1.589**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **68** (18.8%)
- *2 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 309 | 402 | 509 | 44.1% | 55.9% |
| 2026-2027 | 53 | 49 | 63 | 43.8% | 56.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `333` of `362` (92.0%)
- Goalless matches: `29`
- Min `1` | Max `98` | Mean `31.97` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 101 | 27.9% | 30.3% |
| 16-30 | 80 | 22.1% | 24.0% |
| 31-45 | 65 | 18.0% | 19.5% |
| 46-60 | 48 | 13.3% | 14.4% |
| 61-75 | 18 | 5.0% | 5.4% |
| 76-90 | 16 | 4.4% | 4.8% |
| 91-120 | 5 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\saudi2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\saudi2\charts\goals_analysis_avg_per_season.png)

