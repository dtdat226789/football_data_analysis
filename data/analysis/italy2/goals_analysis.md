# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:00+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.0% |
| 1 | 77 | 17.5% |
| 2 | 117 | 26.6% |
| 3 | 103 | 23.4% |
| 4 | 73 | 16.6% |
| 5 | 26 | 5.9% |
| 6 | 8 | 1.8% |
| 7 | 5 | 1.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 390 | 993 | 1.479 | 1.067 | 2.546 |
| 2026-2027 | 50 | 132 | 1.42 | 1.22 | 2.64 |

## 3. Home vs away goal share
- Home goals: **648** (57.6%)
- Away goals: **477** (42.4%)
- Home/away ratio: **1.358**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 577 | 416 | 993 | 58.1% | 41.9% |
| 2026-2027 | 71 | 61 | 132 | 53.8% | 46.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **240** of `440` (54.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 390 | 208 | 53.3% |
| 2026-2027 | 50 | 32 | 64.0% |

## 5. Clean sheets
- Home clean sheets: **144** (32.7%)
- Away clean sheets: **87** (19.8%)
- Total clean sheets recorded: **231**
- Matches with at least one clean sheet: **200** (45.5%)
- Both teams kept clean sheets (0-0): **31**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 390 | 133 | 79 | 212 | 182 (46.7%) |
| 2026-2027 | 50 | 11 | 8 | 19 | 18 (36.0%) |

## 6. Scoring intensity
- First-half goals: **488** (43.4%)
- Second-half goals: **637** (56.6%)
- Avg first-half goals per match: **1.109**
- Avg second-half goals per match: **1.448**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **105** (23.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 390 | 440 | 553 | 44.3% | 55.7% |
| 2026-2027 | 50 | 48 | 84 | 36.4% | 63.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `409` of `440` (93.0%)
- Goalless matches: `31`
- Min `1` | Max `94` | Mean `32.59` | Median (p50) `29`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 113 | 25.7% | 27.6% |
| 16-30 | 101 | 23.0% | 24.7% |
| 31-45 | 79 | 18.0% | 19.3% |
| 46-60 | 65 | 14.8% | 15.9% |
| 61-75 | 23 | 5.2% | 5.6% |
| 76-90 | 25 | 5.7% | 6.1% |
| 91-120 | 3 | 0.7% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy2\charts\goals_analysis_avg_per_season.png)

