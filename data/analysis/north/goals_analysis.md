# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:03:55+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 28 | 4.2% |
| 1 | 97 | 14.5% |
| 2 | 148 | 22.2% |
| 3 | 172 | 25.7% |
| 4 | 108 | 16.2% |
| 5 | 59 | 8.8% |
| 6 | 39 | 5.8% |
| 7 | 11 | 1.6% |
| 8 | 5 | 0.7% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 1707 | 1.643 | 1.405 | 3.048 |
| 2026-2027 | 108 | 290 | 1.574 | 1.111 | 2.685 |

## 3. Home vs away goal share
- Home goals: **1090** (54.6%)
- Away goals: **907** (45.4%)
- Home/away ratio: **1.202**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 920 | 787 | 1707 | 53.9% | 46.1% |
| 2026-2027 | 170 | 120 | 290 | 58.6% | 41.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **401** of `668` (60.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 560 | 341 | 60.9% |
| 2026-2027 | 108 | 60 | 55.6% |

## 5. Clean sheets
- Home clean sheets: **162** (24.3%)
- Away clean sheets: **133** (19.9%)
- Total clean sheets recorded: **295**
- Matches with at least one clean sheet: **267** (40.0%)
- Both teams kept clean sheets (0-0): **28**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 135 | 107 | 242 | 219 (39.1%) |
| 2026-2027 | 108 | 27 | 26 | 53 | 48 (44.4%) |

## 6. Scoring intensity
- First-half goals: **868** (43.6%)
- Second-half goals: **1124** (56.4%)
- Avg first-half goals per match: **1.307**
- Avg second-half goals per match: **1.693**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **145** (21.7%)
- *4 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 560 | 746 | 956 | 43.8% | 56.2% |
| 2026-2027 | 108 | 122 | 168 | 42.1% | 57.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `637` of `668` (95.4%)
- Goalless matches: `31`
- Min `1` | Max `95` | Mean `29.15` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 223 | 33.4% | 35.0% |
| 16-30 | 155 | 23.2% | 24.3% |
| 31-45 | 103 | 15.4% | 16.2% |
| 46-60 | 88 | 13.2% | 13.8% |
| 61-75 | 36 | 5.4% | 5.7% |
| 76-90 | 28 | 4.2% | 4.4% |
| 91-120 | 4 | 0.6% | 0.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\north\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\north\charts\goals_analysis_avg_per_season.png)

