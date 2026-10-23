# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:49:15+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 9 | 2.8% |
| 1 | 48 | 14.8% |
| 2 | 50 | 15.4% |
| 3 | 92 | 28.3% |
| 4 | 66 | 20.3% |
| 5 | 39 | 12.0% |
| 6 | 9 | 2.8% |
| 7 | 7 | 2.2% |
| 8 | 3 | 0.9% |
| 9 | 2 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 180 | 572 | 1.739 | 1.439 | 3.178 |
| 2026 | 145 | 456 | 1.786 | 1.359 | 3.145 |

## 3. Home vs away goal share
- Home goals: **572** (55.6%)
- Away goals: **456** (44.4%)
- Home/away ratio: **1.254**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 313 | 259 | 572 | 54.7% | 45.3% |
| 2026 | 259 | 197 | 456 | 56.8% | 43.2% |

## 4. BTTS (Both Teams To Score)
- Overall: **184** of `325` (56.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 180 | 99 | 55.0% |
| 2026 | 145 | 85 | 58.6% |

## 5. Clean sheets
- Home clean sheets: **89** (27.4%)
- Away clean sheets: **61** (18.8%)
- Total clean sheets recorded: **150**
- Matches with at least one clean sheet: **141** (43.4%)
- Both teams kept clean sheets (0-0): **9**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 180 | 49 | 36 | 85 | 81 (45.0%) |
| 2026 | 145 | 40 | 25 | 65 | 60 (41.4%) |

## 6. Scoring intensity
- First-half goals: **460** (48.3%)
- Second-half goals: **492** (51.7%)
- Avg first-half goals per match: **1.523**
- Avg second-half goals per match: **1.629**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **51** (15.7%)
- *23 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 180 | 243 | 253 | 49.0% | 51.0% |
| 2026 | 145 | 217 | 239 | 47.6% | 52.4% |

## 7. First-goal timing
- Matches with first-goal time recorded: `316` of `325` (97.2%)
- Goalless matches: `9`
- Min `1` | Max `97` | Mean `27.47` | Median (p50) `22.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 111 | 34.2% | 35.1% |
| 16-30 | 93 | 28.6% | 29.4% |
| 31-45 | 55 | 16.9% | 17.4% |
| 46-60 | 30 | 9.2% | 9.5% |
| 61-75 | 14 | 4.3% | 4.4% |
| 76-90 | 6 | 1.8% | 1.9% |
| 91-120 | 7 | 2.2% | 2.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\estonia\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\estonia\charts\goals_analysis_avg_per_season.png)

