# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:00:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Eerste Divisie (Netherlands)
- Scope: league `holland2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 16 | 3.4% |
| 1 | 64 | 13.7% |
| 2 | 84 | 18.0% |
| 3 | 102 | 21.9% |
| 4 | 92 | 19.7% |
| 5 | 57 | 12.2% |
| 6 | 29 | 6.2% |
| 7 | 17 | 3.6% |
| 8 | 3 | 0.6% |
| 9 | 1 | 0.2% |
| 10 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 1248 | 1.73 | 1.454 | 3.184 |
| 2026-2027 | 74 | 279 | 2.095 | 1.676 | 3.77 |

## 3. Home vs away goal share
- Home goals: **833** (54.6%)
- Away goals: **694** (45.4%)
- Home/away ratio: **1.2**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 678 | 570 | 1248 | 54.3% | 45.7% |
| 2026-2027 | 155 | 124 | 279 | 55.6% | 44.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **296** of `466` (63.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 392 | 241 | 61.5% |
| 2026-2027 | 74 | 55 | 74.3% |

## 5. Clean sheets
- Home clean sheets: **109** (23.4%)
- Away clean sheets: **77** (16.5%)
- Total clean sheets recorded: **186**
- Matches with at least one clean sheet: **170** (36.5%)
- Both teams kept clean sheets (0-0): **16**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 97 | 68 | 165 | 151 (38.5%) |
| 2026-2027 | 74 | 12 | 9 | 21 | 19 (25.7%) |

## 6. Scoring intensity
- First-half goals: **665** (43.5%)
- Second-half goals: **862** (56.5%)
- Avg first-half goals per match: **1.427**
- Avg second-half goals per match: **1.85**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **92** (19.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 392 | 540 | 708 | 43.3% | 56.7% |
| 2026-2027 | 74 | 125 | 154 | 44.8% | 55.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `450` of `466` (96.6%)
- Goalless matches: `16`
- Min `1` | Max `95` | Mean `27.66` | Median (p50) `22.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 165 | 35.4% | 36.7% |
| 16-30 | 124 | 26.6% | 27.6% |
| 31-45 | 63 | 13.5% | 14.0% |
| 46-60 | 54 | 11.6% | 12.0% |
| 61-75 | 24 | 5.2% | 5.3% |
| 76-90 | 17 | 3.6% | 3.8% |
| 91-120 | 3 | 0.6% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\holland2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\holland2\charts\goals_analysis_avg_per_season.png)

