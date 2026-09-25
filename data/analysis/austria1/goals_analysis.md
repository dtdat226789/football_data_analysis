# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:54:45+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 13 | 5.5% |
| 1 | 36 | 15.2% |
| 2 | 61 | 25.7% |
| 3 | 56 | 23.6% |
| 4 | 41 | 17.3% |
| 5 | 18 | 7.6% |
| 6 | 9 | 3.8% |
| 7 | 2 | 0.8% |
| 8 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 195 | 527 | 1.436 | 1.267 | 2.703 |
| 2026-2027 | 42 | 129 | 1.881 | 1.19 | 3.071 |

## 3. Home vs away goal share
- Home goals: **359** (54.7%)
- Away goals: **297** (45.3%)
- Home/away ratio: **1.209**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 280 | 247 | 527 | 53.1% | 46.9% |
| 2026-2027 | 79 | 50 | 129 | 61.2% | 38.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **131** of `237` (55.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 195 | 108 | 55.4% |
| 2026-2027 | 42 | 23 | 54.8% |

## 5. Clean sheets
- Home clean sheets: **70** (29.5%)
- Away clean sheets: **49** (20.7%)
- Total clean sheets recorded: **119**
- Matches with at least one clean sheet: **106** (44.7%)
- Both teams kept clean sheets (0-0): **13**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 195 | 58 | 41 | 99 | 87 (44.6%) |
| 2026-2027 | 42 | 12 | 8 | 20 | 19 (45.2%) |

## 6. Scoring intensity
- First-half goals: **312** (47.6%)
- Second-half goals: **344** (52.4%)
- Avg first-half goals per match: **1.316**
- Avg second-half goals per match: **1.451**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **48** (20.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 195 | 247 | 280 | 46.9% | 53.1% |
| 2026-2027 | 42 | 65 | 64 | 50.4% | 49.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `224` of `237` (94.5%)
- Goalless matches: `13`
- Min `1` | Max `95` | Mean `30.96` | Median (p50) `24.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 80 | 33.8% | 35.7% |
| 16-30 | 47 | 19.8% | 21.0% |
| 31-45 | 40 | 16.9% | 17.9% |
| 46-60 | 27 | 11.4% | 12.1% |
| 61-75 | 12 | 5.1% | 5.4% |
| 76-90 | 16 | 6.8% | 7.1% |
| 91-120 | 2 | 0.8% | 0.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\austria1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\austria1\charts\goals_analysis_avg_per_season.png)

