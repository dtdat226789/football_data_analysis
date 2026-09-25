# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:57:28+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 56 | 15.1% |
| 1 | 86 | 23.1% |
| 2 | 103 | 27.7% |
| 3 | 71 | 19.1% |
| 4 | 36 | 9.7% |
| 5 | 16 | 4.3% |
| 6 | 3 | 0.8% |
| 7 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 651 | 1.043 | 0.978 | 2.022 |
| 2026-2027 | 50 | 103 | 0.96 | 1.1 | 2.06 |

## 3. Home vs away goal share
- Home goals: **384** (50.9%)
- Away goals: **370** (49.1%)
- Home/away ratio: **1.038**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 336 | 315 | 651 | 51.6% | 48.4% |
| 2026-2027 | 48 | 55 | 103 | 46.6% | 53.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **169** of `372` (45.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 322 | 150 | 46.6% |
| 2026-2027 | 50 | 19 | 38.0% |

## 5. Clean sheets
- Home clean sheets: **138** (37.1%)
- Away clean sheets: **121** (32.5%)
- Total clean sheets recorded: **259**
- Matches with at least one clean sheet: **203** (54.6%)
- Both teams kept clean sheets (0-0): **56**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 121 | 102 | 223 | 172 (53.4%) |
| 2026-2027 | 50 | 17 | 19 | 36 | 31 (62.0%) |

## 6. Scoring intensity
- First-half goals: **312** (41.4%)
- Second-half goals: **442** (58.6%)
- Avg first-half goals per match: **0.839**
- Avg second-half goals per match: **1.188**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **106** (28.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 322 | 279 | 372 | 42.9% | 57.1% |
| 2026-2027 | 50 | 33 | 70 | 32.0% | 68.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `316` of `372` (84.9%)
- Goalless matches: `56`
- Min `1` | Max `96` | Mean `37.3` | Median (p50) `35.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 79 | 21.2% | 25.0% |
| 16-30 | 64 | 17.2% | 20.3% |
| 31-45 | 54 | 14.5% | 17.1% |
| 46-60 | 57 | 15.3% | 18.0% |
| 61-75 | 29 | 7.8% | 9.2% |
| 76-90 | 26 | 7.0% | 8.2% |
| 91-120 | 7 | 1.9% | 2.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\egypt\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\egypt\charts\goals_analysis_avg_per_season.png)

