# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:52:32+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 11 | 2.9% |
| 1 | 38 | 9.9% |
| 2 | 89 | 23.2% |
| 3 | 85 | 22.1% |
| 4 | 78 | 20.3% |
| 5 | 45 | 11.7% |
| 6 | 22 | 5.7% |
| 7 | 14 | 3.6% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 1016 | 1.794 | 1.371 | 3.165 |
| 2026-2027 | 63 | 240 | 1.714 | 2.095 | 3.81 |

## 3. Home vs away goal share
- Home goals: **684** (54.5%)
- Away goals: **572** (45.5%)
- Home/away ratio: **1.196**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 576 | 440 | 1016 | 56.7% | 43.3% |
| 2026-2027 | 108 | 132 | 240 | 45.0% | 55.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **246** of `384` (64.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 321 | 202 | 62.9% |
| 2026-2027 | 63 | 44 | 69.8% |

## 5. Clean sheets
- Home clean sheets: **86** (22.4%)
- Away clean sheets: **63** (16.4%)
- Total clean sheets recorded: **149**
- Matches with at least one clean sheet: **138** (35.9%)
- Both teams kept clean sheets (0-0): **11**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 77 | 52 | 129 | 119 (37.1%) |
| 2026-2027 | 63 | 9 | 11 | 20 | 19 (30.2%) |

## 6. Scoring intensity
- First-half goals: **558** (44.4%)
- Second-half goals: **698** (55.6%)
- Avg first-half goals per match: **1.453**
- Avg second-half goals per match: **1.818**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **67** (17.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 321 | 455 | 561 | 44.8% | 55.2% |
| 2026-2027 | 63 | 103 | 137 | 42.9% | 57.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `373` of `384` (97.1%)
- Goalless matches: `11`
- Min `1` | Max `93` | Mean `27.94` | Median (p50) `21`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 139 | 36.2% | 37.3% |
| 16-30 | 91 | 23.7% | 24.4% |
| 31-45 | 63 | 16.4% | 16.9% |
| 46-60 | 45 | 11.7% | 12.1% |
| 61-75 | 16 | 4.2% | 4.3% |
| 76-90 | 17 | 4.4% | 4.6% |
| 91-120 | 2 | 0.5% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\holland1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\holland1\charts\goals_analysis_avg_per_season.png)

