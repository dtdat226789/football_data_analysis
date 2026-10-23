# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:08:03+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 42 | 11.5% |
| 1 | 58 | 15.9% |
| 2 | 83 | 22.7% |
| 3 | 70 | 19.2% |
| 4 | 57 | 15.6% |
| 5 | 35 | 9.6% |
| 6 | 11 | 3.0% |
| 7 | 4 | 1.1% |
| 8 | 4 | 1.1% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 297 | 790 | 1.488 | 1.172 | 2.66 |
| 2026-2027 | 68 | 182 | 1.691 | 0.985 | 2.676 |

## 3. Home vs away goal share
- Home goals: **557** (57.3%)
- Away goals: **415** (42.7%)
- Home/away ratio: **1.342**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 442 | 348 | 790 | 55.9% | 44.1% |
| 2026-2027 | 115 | 67 | 182 | 63.2% | 36.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **189** of `365` (51.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 297 | 157 | 52.9% |
| 2026-2027 | 68 | 32 | 47.1% |

## 5. Clean sheets
- Home clean sheets: **139** (38.1%)
- Away clean sheets: **79** (21.6%)
- Total clean sheets recorded: **218**
- Matches with at least one clean sheet: **176** (48.2%)
- Both teams kept clean sheets (0-0): **42**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 297 | 111 | 65 | 176 | 140 (47.1%) |
| 2026-2027 | 68 | 28 | 14 | 42 | 36 (52.9%) |

## 6. Scoring intensity
- First-half goals: **440** (45.4%)
- Second-half goals: **530** (54.6%)
- Avg first-half goals per match: **1.209**
- Avg second-half goals per match: **1.456**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **65** (17.8%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 297 | 358 | 430 | 45.4% | 54.6% |
| 2026-2027 | 68 | 82 | 100 | 45.1% | 54.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `322` of `365` (88.2%)
- Goalless matches: `43`
- Min `1` | Max `97` | Mean `30.28` | Median (p50) `25.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 95 | 26.0% | 29.5% |
| 16-30 | 90 | 24.7% | 28.0% |
| 31-45 | 63 | 17.3% | 19.6% |
| 46-60 | 41 | 11.2% | 12.7% |
| 61-75 | 20 | 5.5% | 6.2% |
| 76-90 | 6 | 1.6% | 1.9% |
| 91-120 | 7 | 1.9% | 2.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\serbia1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\serbia1\charts\goals_analysis_avg_per_season.png)

