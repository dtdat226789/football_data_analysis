# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:49:22+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.1% |
| 1 | 27 | 11.7% |
| 2 | 50 | 21.6% |
| 3 | 60 | 26.0% |
| 4 | 42 | 18.2% |
| 5 | 18 | 7.8% |
| 6 | 11 | 4.8% |
| 7 | 4 | 1.7% |
| 8 | 2 | 0.9% |
| 9 | 3 | 1.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 186 | 566 | 1.613 | 1.43 | 3.043 |
| 2026-2027 | 45 | 136 | 1.822 | 1.2 | 3.022 |

## 3. Home vs away goal share
- Home goals: **382** (54.4%)
- Away goals: **320** (45.6%)
- Home/away ratio: **1.194**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 300 | 266 | 566 | 53.0% | 47.0% |
| 2026-2027 | 82 | 54 | 136 | 60.3% | 39.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **132** of `231` (57.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 186 | 107 | 57.5% |
| 2026-2027 | 45 | 25 | 55.6% |

## 5. Clean sheets
- Home clean sheets: **66** (28.6%)
- Away clean sheets: **47** (20.3%)
- Total clean sheets recorded: **113**
- Matches with at least one clean sheet: **99** (42.9%)
- Both teams kept clean sheets (0-0): **14**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 186 | 53 | 38 | 91 | 79 (42.5%) |
| 2026-2027 | 45 | 13 | 9 | 22 | 20 (44.4%) |

## 6. Scoring intensity
- First-half goals: **336** (47.9%)
- Second-half goals: **366** (52.1%)
- Avg first-half goals per match: **1.455**
- Avg second-half goals per match: **1.584**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **46** (19.9%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 186 | 269 | 297 | 47.5% | 52.5% |
| 2026-2027 | 45 | 67 | 69 | 49.3% | 50.7% |

## 7. First-goal timing
- Matches with first-goal time recorded: `217` of `231` (93.9%)
- Goalless matches: `14`
- Min `1` | Max `95` | Mean `27.17` | Median (p50) `19`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 100 | 43.3% | 46.1% |
| 16-30 | 38 | 16.5% | 17.5% |
| 31-45 | 30 | 13.0% | 13.8% |
| 46-60 | 22 | 9.5% | 10.1% |
| 61-75 | 16 | 6.9% | 7.4% |
| 76-90 | 6 | 2.6% | 2.8% |
| 91-120 | 5 | 2.2% | 2.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\swiss2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\swiss2\charts\goals_analysis_avg_per_season.png)

