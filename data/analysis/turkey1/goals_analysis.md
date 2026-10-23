# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:10:30+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 30 | 8.3% |
| 1 | 56 | 15.6% |
| 2 | 82 | 22.8% |
| 3 | 90 | 25.0% |
| 4 | 55 | 15.3% |
| 5 | 28 | 7.8% |
| 6 | 12 | 3.3% |
| 7 | 5 | 1.4% |
| 8 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 812 | 1.444 | 1.209 | 2.654 |
| 2026-2027 | 54 | 161 | 1.796 | 1.185 | 2.981 |

## 3. Home vs away goal share
- Home goals: **539** (55.4%)
- Away goals: **434** (44.6%)
- Home/away ratio: **1.242**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 442 | 370 | 812 | 54.4% | 45.6% |
| 2026-2027 | 97 | 64 | 161 | 60.2% | 39.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **192** of `360` (53.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 306 | 167 | 54.6% |
| 2026-2027 | 54 | 25 | 46.3% |

## 5. Clean sheets
- Home clean sheets: **117** (32.5%)
- Away clean sheets: **81** (22.5%)
- Total clean sheets recorded: **198**
- Matches with at least one clean sheet: **168** (46.7%)
- Both teams kept clean sheets (0-0): **30**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 97 | 70 | 167 | 139 (45.4%) |
| 2026-2027 | 54 | 20 | 11 | 31 | 29 (53.7%) |

## 6. Scoring intensity
- First-half goals: **424** (43.6%)
- Second-half goals: **549** (56.4%)
- Avg first-half goals per match: **1.178**
- Avg second-half goals per match: **1.525**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **82** (22.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 306 | 350 | 462 | 43.1% | 56.9% |
| 2026-2027 | 54 | 74 | 87 | 46.0% | 54.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `330` of `360` (91.7%)
- Goalless matches: `30`
- Min `1` | Max `101` | Mean `31.82` | Median (p50) `24.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 108 | 30.0% | 32.7% |
| 16-30 | 76 | 21.1% | 23.0% |
| 31-45 | 49 | 13.6% | 14.8% |
| 46-60 | 49 | 13.6% | 14.8% |
| 61-75 | 28 | 7.8% | 8.5% |
| 76-90 | 12 | 3.3% | 3.6% |
| 91-120 | 8 | 2.2% | 2.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\turkey1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\turkey1\charts\goals_analysis_avg_per_season.png)

