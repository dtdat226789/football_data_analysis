# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:55:59+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.5% |
| 1 | 63 | 18.3% |
| 2 | 76 | 22.1% |
| 3 | 79 | 23.0% |
| 4 | 60 | 17.4% |
| 5 | 27 | 7.8% |
| 6 | 11 | 3.2% |
| 7 | 8 | 2.3% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 179 | 502 | 1.559 | 1.246 | 2.804 |
| 2026 | 165 | 456 | 1.642 | 1.121 | 2.764 |

## 3. Home vs away goal share
- Home goals: **550** (57.4%)
- Away goals: **408** (42.6%)
- Home/away ratio: **1.348**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 279 | 223 | 502 | 55.6% | 44.4% |
| 2026 | 271 | 185 | 456 | 59.4% | 40.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **184** of `344` (53.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 179 | 97 | 54.2% |
| 2026 | 165 | 87 | 52.7% |

## 5. Clean sheets
- Home clean sheets: **96** (27.9%)
- Away clean sheets: **83** (24.1%)
- Total clean sheets recorded: **179**
- Matches with at least one clean sheet: **160** (46.5%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 179 | 45 | 47 | 92 | 82 (45.8%) |
| 2026 | 165 | 51 | 36 | 87 | 78 (47.3%) |

## 6. Scoring intensity
- First-half goals: **407** (42.6%)
- Second-half goals: **548** (57.4%)
- Avg first-half goals per match: **1.187**
- Avg second-half goals per match: **1.598**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **84** (24.4%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 179 | 221 | 278 | 44.3% | 55.7% |
| 2026 | 165 | 186 | 270 | 40.8% | 59.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `324` of `344` (94.2%)
- Goalless matches: `20`
- Min `1` | Max `96` | Mean `31.07` | Median (p50) `25.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 113 | 32.8% | 34.9% |
| 16-30 | 76 | 22.1% | 23.5% |
| 31-45 | 46 | 13.4% | 14.2% |
| 46-60 | 43 | 12.5% | 13.3% |
| 61-75 | 29 | 8.4% | 9.0% |
| 76-90 | 12 | 3.5% | 3.7% |
| 91-120 | 5 | 1.5% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\ireland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\ireland2\charts\goals_analysis_avg_per_season.png)

