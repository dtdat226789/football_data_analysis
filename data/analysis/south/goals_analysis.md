# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:08:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 45 | 6.2% |
| 1 | 132 | 18.1% |
| 2 | 155 | 21.3% |
| 3 | 174 | 23.9% |
| 4 | 96 | 13.2% |
| 5 | 73 | 10.0% |
| 6 | 32 | 4.4% |
| 7 | 13 | 1.8% |
| 8 | 5 | 0.7% |
| 9 | 3 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 1709 | 1.6 | 1.225 | 2.825 |
| 2026-2027 | 123 | 354 | 1.423 | 1.455 | 2.878 |

## 3. Home vs away goal share
- Home goals: **1143** (55.4%)
- Away goals: **920** (44.6%)
- Home/away ratio: **1.242**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 968 | 741 | 1709 | 56.6% | 43.4% |
| 2026-2027 | 175 | 179 | 354 | 49.4% | 50.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **399** of `728` (54.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 605 | 335 | 55.4% |
| 2026-2027 | 123 | 64 | 52.0% |

## 5. Clean sheets
- Home clean sheets: **231** (31.7%)
- Away clean sheets: **143** (19.6%)
- Total clean sheets recorded: **374**
- Matches with at least one clean sheet: **329** (45.2%)
- Both teams kept clean sheets (0-0): **45**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 200 | 109 | 309 | 270 (44.6%) |
| 2026-2027 | 123 | 31 | 34 | 65 | 59 (48.0%) |

## 6. Scoring intensity
- First-half goals: **924** (44.8%)
- Second-half goals: **1139** (55.2%)
- Avg first-half goals per match: **1.269**
- Avg second-half goals per match: **1.565**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **162** (22.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 605 | 750 | 959 | 43.9% | 56.1% |
| 2026-2027 | 123 | 174 | 180 | 49.2% | 50.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `683` of `728` (93.8%)
- Goalless matches: `45`
- Min `1` | Max `99` | Mean `30.58` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 244 | 33.5% | 35.7% |
| 16-30 | 171 | 23.5% | 25.0% |
| 31-45 | 96 | 13.2% | 14.1% |
| 46-60 | 87 | 12.0% | 12.7% |
| 61-75 | 36 | 4.9% | 5.3% |
| 76-90 | 32 | 4.4% | 4.7% |
| 91-120 | 17 | 2.3% | 2.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\south\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\south\charts\goals_analysis_avg_per_season.png)

