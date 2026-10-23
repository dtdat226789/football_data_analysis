# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:53:02+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 16 | 3.4% |
| 1 | 66 | 13.9% |
| 2 | 87 | 18.4% |
| 3 | 102 | 21.5% |
| 4 | 92 | 19.4% |
| 5 | 59 | 12.4% |
| 6 | 30 | 6.3% |
| 7 | 17 | 3.6% |
| 8 | 3 | 0.6% |
| 9 | 1 | 0.2% |
| 10 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 1248 | 1.73 | 1.454 | 3.184 |
| 2026-2027 | 82 | 303 | 2.11 | 1.585 | 3.695 |

## 3. Home vs away goal share
- Home goals: **851** (54.9%)
- Away goals: **700** (45.1%)
- Home/away ratio: **1.216**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 678 | 570 | 1248 | 54.3% | 45.7% |
| 2026-2027 | 173 | 130 | 303 | 57.1% | 42.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **299** of `474` (63.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 392 | 241 | 61.5% |
| 2026-2027 | 82 | 58 | 70.7% |

## 5. Clean sheets
- Home clean sheets: **114** (24.1%)
- Away clean sheets: **77** (16.2%)
- Total clean sheets recorded: **191**
- Matches with at least one clean sheet: **175** (36.9%)
- Both teams kept clean sheets (0-0): **16**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 97 | 68 | 165 | 151 (38.5%) |
| 2026-2027 | 82 | 17 | 9 | 26 | 24 (29.3%) |

## 6. Scoring intensity
- First-half goals: **677** (43.6%)
- Second-half goals: **874** (56.4%)
- Avg first-half goals per match: **1.428**
- Avg second-half goals per match: **1.844**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **93** (19.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 540 | 708 | 43.3% | 56.7% |
| 2026-2027 | 82 | 137 | 166 | 45.2% | 54.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `458` of `474` (96.6%)
- Goalless matches: `16`
- Min `1` | Max `95` | Mean `27.48` | Median (p50) `22.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 170 | 35.9% | 37.1% |
| 16-30 | 125 | 26.4% | 27.3% |
| 31-45 | 64 | 13.5% | 14.0% |
| 46-60 | 55 | 11.6% | 12.0% |
| 61-75 | 24 | 5.1% | 5.2% |
| 76-90 | 17 | 3.6% | 3.7% |
| 91-120 | 3 | 0.6% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\holland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\holland2\charts\goals_analysis_avg_per_season.png)

