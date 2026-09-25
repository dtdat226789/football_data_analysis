# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:41:12+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 4.7% |
| 1 | 49 | 12.0% |
| 2 | 102 | 25.0% |
| 3 | 104 | 25.5% |
| 4 | 67 | 16.4% |
| 5 | 39 | 9.6% |
| 6 | 16 | 3.9% |
| 7 | 10 | 2.5% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 328 | 991 | 1.619 | 1.402 | 3.021 |
| 2026-2027 | 80 | 220 | 1.55 | 1.2 | 2.75 |

## 3. Home vs away goal share
- Home goals: **655** (54.1%)
- Away goals: **556** (45.9%)
- Home/away ratio: **1.178**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 531 | 460 | 991 | 53.6% | 46.4% |
| 2026-2027 | 124 | 96 | 220 | 56.4% | 43.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **258** of `408` (63.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 328 | 213 | 64.9% |
| 2026-2027 | 80 | 45 | 56.2% |

## 5. Clean sheets
- Home clean sheets: **93** (22.8%)
- Away clean sheets: **76** (18.6%)
- Total clean sheets recorded: **169**
- Matches with at least one clean sheet: **150** (36.8%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 328 | 71 | 59 | 130 | 115 (35.1%) |
| 2026-2027 | 80 | 22 | 17 | 39 | 35 (43.8%) |

## 6. Scoring intensity
- First-half goals: **551** (45.6%)
- Second-half goals: **657** (54.4%)
- Avg first-half goals per match: **1.354**
- Avg second-half goals per match: **1.614**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **85** (20.8%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 328 | 452 | 536 | 45.7% | 54.3% |
| 2026-2027 | 80 | 99 | 121 | 45.0% | 55.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `388` of `408` (95.1%)
- Goalless matches: `20`
- Min `1` | Max `97` | Mean `29.77` | Median (p50) `24.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 131 | 32.1% | 33.8% |
| 16-30 | 93 | 22.8% | 24.0% |
| 31-45 | 68 | 16.7% | 17.5% |
| 46-60 | 53 | 13.0% | 13.7% |
| 61-75 | 26 | 6.4% | 6.7% |
| 76-90 | 15 | 3.7% | 3.9% |
| 91-120 | 2 | 0.5% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\poland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\poland2\charts\goals_analysis_avg_per_season.png)

