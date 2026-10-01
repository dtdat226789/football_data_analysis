# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:58:00+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.1% |
| 1 | 100 | 22.2% |
| 2 | 106 | 23.6% |
| 3 | 93 | 20.7% |
| 4 | 65 | 14.4% |
| 5 | 27 | 6.0% |
| 6 | 6 | 1.3% |
| 7 | 2 | 0.4% |
| 8 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 889 | 1.247 | 1.092 | 2.339 |
| 2026-2027 | 70 | 155 | 1.143 | 1.071 | 2.214 |

## 3. Home vs away goal share
- Home goals: **554** (53.1%)
- Away goals: **490** (46.9%)
- Home/away ratio: **1.131**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 474 | 415 | 889 | 53.3% | 46.7% |
| 2026-2027 | 80 | 75 | 155 | 51.6% | 48.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **223** of `450` (49.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 380 | 189 | 49.7% |
| 2026-2027 | 70 | 34 | 48.6% |

## 5. Clean sheets
- Home clean sheets: **146** (32.4%)
- Away clean sheets: **131** (29.1%)
- Total clean sheets recorded: **277**
- Matches with at least one clean sheet: **227** (50.4%)
- Both teams kept clean sheets (0-0): **50**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 119 | 109 | 228 | 191 (50.3%) |
| 2026-2027 | 70 | 27 | 22 | 49 | 36 (51.4%) |

## 6. Scoring intensity
- First-half goals: **444** (42.5%)
- Second-half goals: **600** (57.5%)
- Avg first-half goals per match: **0.987**
- Avg second-half goals per match: **1.333**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **110** (24.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 380 | 379 | 510 | 42.6% | 57.4% |
| 2026-2027 | 70 | 65 | 90 | 41.9% | 58.1% |

## 7. First-goal timing
- Matches with first-goal time recorded: `400` of `450` (88.9%)
- Goalless matches: `50`
- Min `1` | Max `97` | Mean `33.83` | Median (p50) `27.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 113 | 25.1% | 28.2% |
| 16-30 | 100 | 22.2% | 25.0% |
| 31-45 | 67 | 14.9% | 16.8% |
| 46-60 | 51 | 11.3% | 12.8% |
| 61-75 | 40 | 8.9% | 10.0% |
| 76-90 | 22 | 4.9% | 5.5% |
| 91-120 | 7 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\italy3a\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\italy3a\charts\goals_analysis_avg_per_season.png)

