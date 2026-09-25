# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:41:31+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 25 | 6.8% |
| 1 | 68 | 18.4% |
| 2 | 78 | 21.1% |
| 3 | 83 | 22.4% |
| 4 | 79 | 21.4% |
| 5 | 22 | 5.9% |
| 6 | 12 | 3.2% |
| 7 | 2 | 0.5% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 823 | 1.494 | 1.179 | 2.672 |
| 2026-2027 | 62 | 170 | 1.323 | 1.419 | 2.742 |

## 3. Home vs away goal share
- Home goals: **542** (54.6%)
- Away goals: **451** (45.4%)
- Home/away ratio: **1.202**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 460 | 363 | 823 | 55.9% | 44.1% |
| 2026-2027 | 82 | 88 | 170 | 48.2% | 51.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **178** of `370` (48.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 308 | 147 | 47.7% |
| 2026-2027 | 62 | 31 | 50.0% |

## 5. Clean sheets
- Home clean sheets: **119** (32.2%)
- Away clean sheets: **98** (26.5%)
- Total clean sheets recorded: **217**
- Matches with at least one clean sheet: **192** (51.9%)
- Both teams kept clean sheets (0-0): **25**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 101 | 81 | 182 | 161 (52.3%) |
| 2026-2027 | 62 | 18 | 17 | 35 | 31 (50.0%) |

## 6. Scoring intensity
- First-half goals: **445** (44.8%)
- Second-half goals: **548** (55.2%)
- Avg first-half goals per match: **1.203**
- Avg second-half goals per match: **1.481**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **89** (24.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 368 | 455 | 44.7% | 55.3% |
| 2026-2027 | 62 | 77 | 93 | 45.3% | 54.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `345` of `370` (93.2%)
- Goalless matches: `25`
- Min `1` | Max `95` | Mean `31.21` | Median (p50) `26`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 120 | 32.4% | 34.8% |
| 16-30 | 67 | 18.1% | 19.4% |
| 31-45 | 64 | 17.3% | 18.6% |
| 46-60 | 44 | 11.9% | 12.8% |
| 61-75 | 30 | 8.1% | 8.7% |
| 76-90 | 16 | 4.3% | 4.6% |
| 91-120 | 4 | 1.1% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\portugal1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\portugal1\charts\goals_analysis_avg_per_season.png)

