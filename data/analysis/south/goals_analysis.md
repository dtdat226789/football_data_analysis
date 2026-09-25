# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:47:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 44 | 6.1% |
| 1 | 131 | 18.3% |
| 2 | 152 | 21.2% |
| 3 | 171 | 23.9% |
| 4 | 94 | 13.1% |
| 5 | 72 | 10.1% |
| 6 | 32 | 4.5% |
| 7 | 12 | 1.7% |
| 8 | 5 | 0.7% |
| 9 | 3 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 1709 | 1.6 | 1.225 | 2.825 |
| 2026-2027 | 111 | 318 | 1.405 | 1.459 | 2.865 |

## 3. Home vs away goal share
- Home goals: **1124** (55.5%)
- Away goals: **903** (44.5%)
- Home/away ratio: **1.245**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 968 | 741 | 1709 | 56.6% | 43.4% |
| 2026-2027 | 156 | 162 | 318 | 49.1% | 50.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **394** of `716` (55.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 605 | 335 | 55.4% |
| 2026-2027 | 111 | 59 | 53.2% |

## 5. Clean sheets
- Home clean sheets: **226** (31.6%)
- Away clean sheets: **140** (19.6%)
- Total clean sheets recorded: **366**
- Matches with at least one clean sheet: **322** (45.0%)
- Both teams kept clean sheets (0-0): **44**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 200 | 109 | 309 | 270 (44.6%) |
| 2026-2027 | 111 | 26 | 31 | 57 | 52 (46.8%) |

## 6. Scoring intensity
- First-half goals: **902** (44.5%)
- Second-half goals: **1125** (55.5%)
- Avg first-half goals per match: **1.26**
- Avg second-half goals per match: **1.571**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **161** (22.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 750 | 959 | 43.9% | 56.1% |
| 2026-2027 | 111 | 152 | 166 | 47.8% | 52.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `672` of `716` (93.9%)
- Goalless matches: `44`
- Min `1` | Max `99` | Mean `30.67` | Median (p50) `24.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 240 | 33.5% | 35.7% |
| 16-30 | 167 | 23.3% | 24.9% |
| 31-45 | 95 | 13.3% | 14.1% |
| 46-60 | 86 | 12.0% | 12.8% |
| 61-75 | 35 | 4.9% | 5.2% |
| 76-90 | 32 | 4.5% | 4.8% |
| 91-120 | 17 | 2.4% | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\south\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\south\charts\goals_analysis_avg_per_season.png)

