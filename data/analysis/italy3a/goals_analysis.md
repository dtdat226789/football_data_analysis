# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:10+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 48 | 10.9% |
| 1 | 99 | 22.5% |
| 2 | 102 | 23.2% |
| 3 | 90 | 20.5% |
| 4 | 65 | 14.8% |
| 5 | 27 | 6.1% |
| 6 | 6 | 1.4% |
| 7 | 2 | 0.5% |
| 8 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 889 | 1.247 | 1.092 | 2.339 |
| 2026-2027 | 60 | 137 | 1.217 | 1.067 | 2.283 |

## 3. Home vs away goal share
- Home goals: **547** (53.3%)
- Away goals: **479** (46.7%)
- Home/away ratio: **1.142**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 474 | 415 | 889 | 53.3% | 46.7% |
| 2026-2027 | 73 | 64 | 137 | 53.3% | 46.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **219** of `440` (49.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 189 | 49.7% |
| 2026-2027 | 60 | 30 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **143** (32.5%)
- Away clean sheets: **126** (28.6%)
- Total clean sheets recorded: **269**
- Matches with at least one clean sheet: **221** (50.2%)
- Both teams kept clean sheets (0-0): **48**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 119 | 109 | 228 | 191 (50.3%) |
| 2026-2027 | 60 | 24 | 17 | 41 | 30 (50.0%) |

## 6. Scoring intensity
- First-half goals: **438** (42.7%)
- Second-half goals: **588** (57.3%)
- Avg first-half goals per match: **0.995**
- Avg second-half goals per match: **1.336**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **105** (23.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 379 | 510 | 42.6% | 57.4% |
| 2026-2027 | 60 | 59 | 78 | 43.1% | 56.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `392` of `440` (89.1%)
- Goalless matches: `48`
- Min `1` | Max `97` | Mean `33.52` | Median (p50) `27.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 112 | 25.5% | 28.6% |
| 16-30 | 100 | 22.7% | 25.5% |
| 31-45 | 65 | 14.8% | 16.6% |
| 46-60 | 49 | 11.1% | 12.5% |
| 61-75 | 38 | 8.6% | 9.7% |
| 76-90 | 21 | 4.8% | 5.4% |
| 91-120 | 7 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy3a\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy3a\charts\goals_analysis_avg_per_season.png)

