# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:44:21+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 19 | 6.8% |
| 1 | 43 | 15.4% |
| 2 | 68 | 24.4% |
| 3 | 61 | 21.9% |
| 4 | 45 | 16.1% |
| 5 | 25 | 9.0% |
| 6 | 10 | 3.6% |
| 7 | 7 | 2.5% |
| 8 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 223 | 599 | 1.422 | 1.265 | 2.686 |
| 2026-2027 | 56 | 185 | 1.929 | 1.375 | 3.304 |

## 3. Home vs away goal share
- Home goals: **425** (54.2%)
- Away goals: **359** (45.8%)
- Home/away ratio: **1.184**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 282 | 599 | 52.9% | 47.1% |
| 2026-2027 | 108 | 77 | 185 | 58.4% | 41.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **143** of `279` (51.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 223 | 112 | 50.2% |
| 2026-2027 | 56 | 31 | 55.4% |

## 5. Clean sheets
- Home clean sheets: **80** (28.7%)
- Away clean sheets: **75** (26.9%)
- Total clean sheets recorded: **155**
- Matches with at least one clean sheet: **136** (48.7%)
- Both teams kept clean sheets (0-0): **19**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 223 | 66 | 63 | 129 | 111 (49.8%) |
| 2026-2027 | 56 | 14 | 12 | 26 | 25 (44.6%) |

## 6. Scoring intensity
- First-half goals: **365** (46.7%)
- Second-half goals: **416** (53.3%)
- Avg first-half goals per match: **1.313**
- Avg second-half goals per match: **1.496**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **54** (19.4%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 223 | 284 | 312 | 47.7% | 52.3% |
| 2026-2027 | 56 | 81 | 104 | 43.8% | 56.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `259` of `279` (92.8%)
- Goalless matches: `20`
- Min `1` | Max `96` | Mean `28.59` | Median (p50) `22`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 95 | 34.1% | 36.7% |
| 16-30 | 68 | 24.4% | 26.3% |
| 31-45 | 41 | 14.7% | 15.8% |
| 46-60 | 26 | 9.3% | 10.0% |
| 61-75 | 13 | 4.7% | 5.0% |
| 76-90 | 11 | 3.9% | 4.2% |
| 91-120 | 5 | 1.8% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\austria2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\austria2\charts\goals_analysis_avg_per_season.png)

