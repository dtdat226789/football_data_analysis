# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:50:42+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 9 | 2.2% |
| 1 | 37 | 8.9% |
| 2 | 85 | 20.5% |
| 3 | 61 | 14.7% |
| 4 | 98 | 23.6% |
| 5 | 62 | 14.9% |
| 6 | 28 | 6.7% |
| 7 | 15 | 3.6% |
| 8 | 13 | 3.1% |
| 9 | 4 | 1.0% |
| 10 | 3 | 0.7% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 1152 | 1.927 | 1.707 | 3.634 |
| 2026-2027 | 98 | 383 | 2.051 | 1.857 | 3.908 |

## 3. Home vs away goal share
- Home goals: **812** (52.9%)
- Away goals: **723** (47.1%)
- Home/away ratio: **1.123**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 611 | 541 | 1152 | 53.0% | 47.0% |
| 2026-2027 | 201 | 182 | 383 | 52.5% | 47.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **264** of `415` (63.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 317 | 204 | 64.4% |
| 2026-2027 | 98 | 60 | 61.2% |

## 5. Clean sheets
- Home clean sheets: **76** (18.3%)
- Away clean sheets: **84** (20.2%)
- Total clean sheets recorded: **160**
- Matches with at least one clean sheet: **151** (36.4%)
- Both teams kept clean sheets (0-0): **9**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 59 | 62 | 121 | 113 (35.6%) |
| 2026-2027 | 98 | 17 | 22 | 39 | 38 (38.8%) |

## 6. Scoring intensity
- First-half goals: **651** (42.4%)
- Second-half goals: **884** (57.6%)
- Avg first-half goals per match: **1.569**
- Avg second-half goals per match: **2.13**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **72** (17.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 317 | 504 | 648 | 43.8% | 56.2% |
| 2026-2027 | 98 | 147 | 236 | 38.4% | 61.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `406` of `415` (97.8%)
- Goalless matches: `9`
- Min `1` | Max `94` | Mean `26.52` | Median (p50) `19.5`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 171 | 41.2% | 42.1% |
| 16-30 | 95 | 22.9% | 23.4% |
| 31-45 | 63 | 15.2% | 15.5% |
| 46-60 | 40 | 9.6% | 9.9% |
| 61-75 | 18 | 4.3% | 4.4% |
| 76-90 | 16 | 3.9% | 3.9% |
| 91-120 | 3 | 0.7% | 0.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\germany-north\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\germany-north\charts\goals_analysis_avg_per_season.png)

