# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:51:39+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 24 | 8.5% |
| 1 | 47 | 16.7% |
| 2 | 77 | 27.4% |
| 3 | 64 | 22.8% |
| 4 | 37 | 13.2% |
| 5 | 24 | 8.5% |
| 6 | 5 | 1.8% |
| 7 | 3 | 1.1% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 246 | 624 | 1.407 | 1.13 | 2.537 |
| 2026-2027 | 35 | 88 | 1.514 | 1.0 | 2.514 |

## 3. Home vs away goal share
- Home goals: **399** (56.0%)
- Away goals: **313** (44.0%)
- Home/away ratio: **1.275**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 346 | 278 | 624 | 55.4% | 44.6% |
| 2026-2027 | 53 | 35 | 88 | 60.2% | 39.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **134** of `281` (47.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 246 | 117 | 47.6% |
| 2026-2027 | 35 | 17 | 48.6% |

## 5. Clean sheets
- Home clean sheets: **94** (33.5%)
- Away clean sheets: **77** (27.4%)
- Total clean sheets recorded: **171**
- Matches with at least one clean sheet: **147** (52.3%)
- Both teams kept clean sheets (0-0): **24**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 246 | 83 | 68 | 151 | 129 (52.4%) |
| 2026-2027 | 35 | 11 | 9 | 20 | 18 (51.4%) |

## 6. Scoring intensity
- First-half goals: **327** (45.9%)
- Second-half goals: **385** (54.1%)
- Avg first-half goals per match: **1.164**
- Avg second-half goals per match: **1.37**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **60** (21.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 246 | 290 | 334 | 46.5% | 53.5% |
| 2026-2027 | 35 | 37 | 51 | 42.0% | 58.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `257` of `281` (91.5%)
- Goalless matches: `24`
- Min `1` | Max `93` | Mean `31.09` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 75 | 26.7% | 29.2% |
| 16-30 | 66 | 23.5% | 25.7% |
| 31-45 | 51 | 18.1% | 19.8% |
| 46-60 | 31 | 11.0% | 12.1% |
| 61-75 | 23 | 8.2% | 8.9% |
| 76-90 | 7 | 2.5% | 2.7% |
| 91-120 | 4 | 1.4% | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\greece1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\greece1\charts\goals_analysis_avg_per_season.png)

