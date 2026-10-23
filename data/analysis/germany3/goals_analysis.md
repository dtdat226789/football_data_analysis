# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:51:24+00:00
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
| 4 | 86 | 19.1% |
| 5 | 53 | 11.8% |
| 6 | 25 | 5.6% |
| 7 | 15 | 3.3% |
| 8 | 7 | 1.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 1219 | 1.758 | 1.45 | 3.208 |
| 2026-2027 | 70 | 229 | 1.686 | 1.586 | 3.271 |

## 3. Home vs away goal share
- Home goals: **786** (54.3%)
- Away goals: **662** (45.7%)
- Home/away ratio: **1.187**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 668 | 551 | 1219 | 54.8% | 45.2% |
| 2026-2027 | 118 | 111 | 229 | 51.5% | 48.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **289** of `450` (64.2%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 245 | 64.5% |
| 2026-2027 | 70 | 44 | 62.9% |

## 5. Clean sheets
- Home clean sheets: **105** (23.3%)
- Away clean sheets: **81** (18.0%)
- Total clean sheets recorded: **186**
- Matches with at least one clean sheet: **161** (35.8%)
- Both teams kept clean sheets (0-0): **25**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 88 | 70 | 158 | 135 (35.5%) |
| 2026-2027 | 70 | 17 | 11 | 28 | 26 (37.1%) |

## 6. Scoring intensity
- First-half goals: **636** (43.9%)
- Second-half goals: **812** (56.1%)
- Avg first-half goals per match: **1.413**
- Avg second-half goals per match: **1.804**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **76** (16.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 523 | 696 | 42.9% | 57.1% |
| 2026-2027 | 70 | 113 | 116 | 49.3% | 50.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `425` of `450` (94.4%)
- Goalless matches: `25`
- Min `1` | Max `95` | Mean `28.22` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 143 | 31.8% | 33.6% |
| 16-30 | 126 | 28.0% | 29.6% |
| 31-45 | 72 | 16.0% | 16.9% |
| 46-60 | 45 | 10.0% | 10.6% |
| 61-75 | 15 | 3.3% | 3.5% |
| 76-90 | 19 | 4.2% | 4.5% |
| 91-120 | 5 | 1.1% | 1.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\germany3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\germany3\charts\goals_analysis_avg_per_season.png)

