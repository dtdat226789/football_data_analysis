# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:59:14+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 9 | 2.2% |
| 1 | 37 | 9.1% |
| 2 | 84 | 20.6% |
| 3 | 58 | 14.2% |
| 4 | 97 | 23.8% |
| 5 | 61 | 15.0% |
| 6 | 27 | 6.6% |
| 7 | 15 | 3.7% |
| 8 | 13 | 3.2% |
| 9 | 4 | 1.0% |
| 10 | 3 | 0.7% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 1152 | 1.927 | 1.707 | 3.634 |
| 2026-2027 | 91 | 357 | 2.121 | 1.802 | 3.923 |

## 3. Home vs away goal share
- Home goals: **804** (53.3%)
- Away goals: **705** (46.7%)
- Home/away ratio: **1.14**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 611 | 541 | 1152 | 53.0% | 47.0% |
| 2026-2027 | 193 | 164 | 357 | 54.1% | 45.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **261** of `408` (64.0%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 317 | 204 | 64.4% |
| 2026-2027 | 91 | 57 | 62.6% |

## 5. Clean sheets
- Home clean sheets: **76** (18.6%)
- Away clean sheets: **80** (19.6%)
- Total clean sheets recorded: **156**
- Matches with at least one clean sheet: **147** (36.0%)
- Both teams kept clean sheets (0-0): **9**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 59 | 62 | 121 | 113 (35.6%) |
| 2026-2027 | 91 | 17 | 18 | 35 | 34 (37.4%) |

## 6. Scoring intensity
- First-half goals: **644** (42.7%)
- Second-half goals: **865** (57.3%)
- Avg first-half goals per match: **1.578**
- Avg second-half goals per match: **2.12**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **71** (17.4%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 504 | 648 | 43.8% | 56.2% |
| 2026-2027 | 91 | 140 | 217 | 39.2% | 60.8% |

## 7. First-goal timing
- Matches with first-goal time recorded: `399` of `408` (97.8%)
- Goalless matches: `9`
- Min `1` | Max `94` | Mean `26.51` | Median (p50) `19`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 169 | 41.4% | 42.4% |
| 16-30 | 93 | 22.8% | 23.3% |
| 31-45 | 61 | 15.0% | 15.3% |
| 46-60 | 39 | 9.6% | 9.8% |
| 61-75 | 18 | 4.4% | 4.5% |
| 76-90 | 16 | 3.9% | 4.0% |
| 91-120 | 3 | 0.7% | 0.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\germany-north\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\germany-north\charts\goals_analysis_avg_per_season.png)

