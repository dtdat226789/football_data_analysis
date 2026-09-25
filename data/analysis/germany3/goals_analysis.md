# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:59:49+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 25 | 5.6% |
| 1 | 52 | 11.6% |
| 2 | 85 | 18.9% |
| 3 | 102 | 22.7% |
| 4 | 85 | 18.9% |
| 5 | 53 | 11.8% |
| 6 | 25 | 5.6% |
| 7 | 15 | 3.3% |
| 8 | 7 | 1.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 1219 | 1.758 | 1.45 | 3.208 |
| 2026-2027 | 69 | 225 | 1.696 | 1.565 | 3.261 |

## 3. Home vs away goal share
- Home goals: **785** (54.4%)
- Away goals: **659** (45.6%)
- Home/away ratio: **1.191**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 668 | 551 | 1219 | 54.8% | 45.2% |
| 2026-2027 | 117 | 108 | 225 | 52.0% | 48.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **288** of `449` (64.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 245 | 64.5% |
| 2026-2027 | 69 | 43 | 62.3% |

## 5. Clean sheets
- Home clean sheets: **105** (23.4%)
- Away clean sheets: **81** (18.0%)
- Total clean sheets recorded: **186**
- Matches with at least one clean sheet: **161** (35.9%)
- Both teams kept clean sheets (0-0): **25**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 88 | 70 | 158 | 135 (35.5%) |
| 2026-2027 | 69 | 17 | 11 | 28 | 26 (37.7%) |

## 6. Scoring intensity
- First-half goals: **635** (44.0%)
- Second-half goals: **809** (56.0%)
- Avg first-half goals per match: **1.414**
- Avg second-half goals per match: **1.802**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **76** (16.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 523 | 696 | 42.9% | 57.1% |
| 2026-2027 | 69 | 112 | 113 | 49.8% | 50.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `424` of `449` (94.4%)
- Goalless matches: `25`
- Min `1` | Max `95` | Mean `28.2` | Median (p50) `23.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 143 | 31.8% | 33.7% |
| 16-30 | 126 | 28.1% | 29.7% |
| 31-45 | 71 | 15.8% | 16.7% |
| 46-60 | 45 | 10.0% | 10.6% |
| 61-75 | 15 | 3.3% | 3.5% |
| 76-90 | 19 | 4.2% | 4.5% |
| 91-120 | 5 | 1.1% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\germany3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\germany3\charts\goals_analysis_avg_per_season.png)

