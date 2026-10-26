# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-26T01:42:57+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 25 | 6.5% |
| 1 | 73 | 19.0% |
| 2 | 80 | 20.8% |
| 3 | 86 | 22.4% |
| 4 | 80 | 20.8% |
| 5 | 25 | 6.5% |
| 6 | 12 | 3.1% |
| 7 | 2 | 0.5% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 823 | 1.494 | 1.179 | 2.672 |
| 2026-2027 | 76 | 207 | 1.303 | 1.421 | 2.724 |

## 3. Home vs away goal share
- Home goals: **559** (54.3%)
- Away goals: **471** (45.7%)
- Home/away ratio: **1.187**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 460 | 363 | 823 | 55.9% | 44.1% |
| 2026-2027 | 99 | 108 | 207 | 47.8% | 52.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **184** of `384` (47.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 308 | 147 | 47.7% |
| 2026-2027 | 76 | 37 | 48.7% |

## 5. Clean sheets
- Home clean sheets: **122** (31.8%)
- Away clean sheets: **103** (26.8%)
- Total clean sheets recorded: **225**
- Matches with at least one clean sheet: **200** (52.1%)
- Both teams kept clean sheets (0-0): **25**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 101 | 81 | 182 | 161 (52.3%) |
| 2026-2027 | 76 | 21 | 22 | 43 | 39 (51.3%) |

## 6. Scoring intensity
- First-half goals: **459** (44.6%)
- Second-half goals: **571** (55.4%)
- Avg first-half goals per match: **1.195**
- Avg second-half goals per match: **1.487**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **92** (24.0%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 368 | 455 | 44.7% | 55.3% |
| 2026-2027 | 76 | 91 | 116 | 44.0% | 56.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `359` of `384` (93.5%)
- Goalless matches: `25`
- Min `1` | Max `95` | Mean `31.48` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 122 | 31.8% | 34.0% |
| 16-30 | 71 | 18.5% | 19.8% |
| 31-45 | 69 | 18.0% | 19.2% |
| 46-60 | 44 | 11.5% | 12.3% |
| 61-75 | 31 | 8.1% | 8.6% |
| 76-90 | 17 | 4.4% | 4.7% |
| 91-120 | 5 | 1.3% | 1.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

