# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:51:28+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 8 | 2.5% |
| 1 | 53 | 16.8% |
| 2 | 57 | 18.1% |
| 3 | 84 | 26.7% |
| 4 | 41 | 13.0% |
| 5 | 42 | 13.3% |
| 6 | 20 | 6.3% |
| 7 | 7 | 2.2% |
| 8 | 2 | 0.6% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 182 | 606 | 1.709 | 1.621 | 3.33 |
| 2026 | 133 | 381 | 1.609 | 1.256 | 2.865 |

## 3. Home vs away goal share
- Home goals: **525** (53.2%)
- Away goals: **462** (46.8%)
- Home/away ratio: **1.136**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 311 | 295 | 606 | 51.3% | 48.7% |
| 2026 | 214 | 167 | 381 | 56.2% | 43.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **159** of `315` (50.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 182 | 100 | 54.9% |
| 2026 | 133 | 59 | 44.4% |

## 5. Clean sheets
- Home clean sheets: **89** (28.3%)
- Away clean sheets: **75** (23.8%)
- Total clean sheets recorded: **164**
- Matches with at least one clean sheet: **156** (49.5%)
- Both teams kept clean sheets (0-0): **8**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 182 | 47 | 39 | 86 | 82 (45.1%) |
| 2026 | 133 | 42 | 36 | 78 | 74 (55.6%) |

## 6. Scoring intensity
- First-half goals: **459** (46.5%)
- Second-half goals: **528** (53.5%)
- Avg first-half goals per match: **1.457**
- Avg second-half goals per match: **1.676**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **59** (18.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 182 | 266 | 340 | 43.9% | 56.1% |
| 2026 | 133 | 193 | 188 | 50.7% | 49.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `307` of `315` (97.5%)
- Goalless matches: `8`
- Min `1` | Max `95` | Mean `26.99` | Median (p50) `20`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 122 | 38.7% | 39.7% |
| 16-30 | 80 | 25.4% | 26.1% |
| 31-45 | 41 | 13.0% | 13.4% |
| 46-60 | 35 | 11.1% | 11.4% |
| 61-75 | 17 | 5.4% | 5.5% |
| 76-90 | 11 | 3.5% | 3.6% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wsweden\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wsweden\charts\goals_analysis_avg_per_season.png)

