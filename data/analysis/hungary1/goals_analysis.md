# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:54:01+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 10 | 4.1% |
| 1 | 36 | 14.7% |
| 2 | 51 | 20.8% |
| 3 | 58 | 23.7% |
| 4 | 49 | 20.0% |
| 5 | 20 | 8.2% |
| 6 | 13 | 5.3% |
| 7 | 5 | 2.0% |
| 8 | 1 | 0.4% |
| 9 | 2 | 0.8% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 198 | 594 | 1.556 | 1.444 | 3.0 |
| 2026-2027 | 47 | 153 | 1.809 | 1.447 | 3.255 |

## 3. Home vs away goal share
- Home goals: **393** (52.6%)
- Away goals: **354** (47.4%)
- Home/away ratio: **1.11**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 308 | 286 | 594 | 51.9% | 48.1% |
| 2026-2027 | 85 | 68 | 153 | 55.6% | 44.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **150** of `245` (61.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 198 | 119 | 60.1% |
| 2026-2027 | 47 | 31 | 66.0% |

## 5. Clean sheets
- Home clean sheets: **55** (22.4%)
- Away clean sheets: **50** (20.4%)
- Total clean sheets recorded: **105**
- Matches with at least one clean sheet: **95** (38.8%)
- Both teams kept clean sheets (0-0): **10**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 198 | 45 | 42 | 87 | 79 (39.9%) |
| 2026-2027 | 47 | 10 | 8 | 18 | 16 (34.0%) |

## 6. Scoring intensity
- First-half goals: **327** (43.8%)
- Second-half goals: **420** (56.2%)
- Avg first-half goals per match: **1.335**
- Avg second-half goals per match: **1.714**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **64** (26.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 198 | 259 | 335 | 43.6% | 56.4% |
| 2026-2027 | 47 | 68 | 85 | 44.4% | 55.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `235` of `245` (95.9%)
- Goalless matches: `10`
- Min `1` | Max `93` | Mean `30.78` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 74 | 30.2% | 31.5% |
| 16-30 | 63 | 25.7% | 26.8% |
| 31-45 | 31 | 12.7% | 13.2% |
| 46-60 | 45 | 18.4% | 19.1% |
| 61-75 | 11 | 4.5% | 4.7% |
| 76-90 | 10 | 4.1% | 4.3% |
| 91-120 | 1 | 0.4% | 0.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\hungary1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\hungary1\charts\goals_analysis_avg_per_season.png)

