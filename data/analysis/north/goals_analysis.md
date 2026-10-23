# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:02:17+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 28 | 4.1% |
| 1 | 98 | 14.4% |
| 2 | 152 | 22.4% |
| 3 | 174 | 25.6% |
| 4 | 110 | 16.2% |
| 5 | 62 | 9.1% |
| 6 | 39 | 5.7% |
| 7 | 11 | 1.6% |
| 8 | 5 | 0.7% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 1707 | 1.643 | 1.405 | 3.048 |
| 2026-2027 | 120 | 328 | 1.6 | 1.133 | 2.733 |

## 3. Home vs away goal share
- Home goals: **1112** (54.6%)
- Away goals: **923** (45.4%)
- Home/away ratio: **1.205**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 920 | 787 | 1707 | 53.9% | 46.1% |
| 2026-2027 | 192 | 136 | 328 | 58.5% | 41.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **410** of `680` (60.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 560 | 341 | 60.9% |
| 2026-2027 | 120 | 69 | 57.5% |

## 5. Clean sheets
- Home clean sheets: **164** (24.1%)
- Away clean sheets: **134** (19.7%)
- Total clean sheets recorded: **298**
- Matches with at least one clean sheet: **270** (39.7%)
- Both teams kept clean sheets (0-0): **28**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 135 | 107 | 242 | 219 (39.1%) |
| 2026-2027 | 120 | 29 | 27 | 56 | 51 (42.5%) |

## 6. Scoring intensity
- First-half goals: **882** (43.4%)
- Second-half goals: **1148** (56.6%)
- Avg first-half goals per match: **1.305**
- Avg second-half goals per match: **1.698**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **148** (21.8%)
- *4 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 746 | 956 | 43.8% | 56.2% |
| 2026-2027 | 120 | 136 | 192 | 41.5% | 58.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `649` of `680` (95.4%)
- Goalless matches: `31`
- Min `1` | Max `95` | Mean `29.14` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 225 | 33.1% | 34.7% |
| 16-30 | 161 | 23.7% | 24.8% |
| 31-45 | 104 | 15.3% | 16.0% |
| 46-60 | 91 | 13.4% | 14.0% |
| 61-75 | 36 | 5.3% | 5.5% |
| 76-90 | 28 | 4.1% | 4.3% |
| 91-120 | 4 | 0.6% | 0.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\north\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\north\charts\goals_analysis_avg_per_season.png)

