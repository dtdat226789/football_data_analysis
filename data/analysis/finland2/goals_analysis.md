# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:58:26+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 13 | 5.1% |
| 1 | 45 | 17.6% |
| 2 | 55 | 21.6% |
| 3 | 55 | 21.6% |
| 4 | 41 | 16.1% |
| 5 | 24 | 9.4% |
| 6 | 12 | 4.7% |
| 7 | 6 | 2.4% |
| 8 | 3 | 1.2% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 135 | 443 | 1.741 | 1.541 | 3.281 |
| 2026 | 120 | 309 | 1.325 | 1.25 | 2.575 |

## 3. Home vs away goal share
- Home goals: **394** (52.4%)
- Away goals: **358** (47.6%)
- Home/away ratio: **1.101**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 235 | 208 | 443 | 53.0% | 47.0% |
| 2026 | 159 | 150 | 309 | 51.5% | 48.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **146** of `255` (57.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 135 | 93 | 68.9% |
| 2026 | 120 | 53 | 44.2% |

## 5. Clean sheets
- Home clean sheets: **59** (23.1%)
- Away clean sheets: **63** (24.7%)
- Total clean sheets recorded: **122**
- Matches with at least one clean sheet: **109** (42.7%)
- Both teams kept clean sheets (0-0): **13**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 135 | 24 | 23 | 47 | 42 (31.1%) |
| 2026 | 120 | 35 | 40 | 75 | 67 (55.8%) |

## 6. Scoring intensity
- First-half goals: **330** (43.9%)
- Second-half goals: **422** (56.1%)
- Avg first-half goals per match: **1.294**
- Avg second-half goals per match: **1.655**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **60** (23.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 135 | 195 | 248 | 44.0% | 56.0% |
| 2026 | 120 | 135 | 174 | 43.7% | 56.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `242` of `255` (94.9%)
- Goalless matches: `13`
- Min `1` | Max `95` | Mean `29.74` | Median (p50) `21.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 92 | 36.1% | 38.0% |
| 16-30 | 56 | 22.0% | 23.1% |
| 31-45 | 32 | 12.5% | 13.2% |
| 46-60 | 32 | 12.5% | 13.2% |
| 61-75 | 19 | 7.5% | 7.9% |
| 76-90 | 7 | 2.7% | 2.9% |
| 91-120 | 4 | 1.6% | 1.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\finland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\finland2\charts\goals_analysis_avg_per_season.png)

