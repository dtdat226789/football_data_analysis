# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:47:36+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 12 | 3.6% |
| 1 | 38 | 11.4% |
| 2 | 76 | 22.8% |
| 3 | 70 | 21.0% |
| 4 | 54 | 16.2% |
| 5 | 43 | 12.9% |
| 6 | 21 | 6.3% |
| 7 | 10 | 3.0% |
| 8 | 6 | 1.8% |
| 9 | 2 | 0.6% |
| 10 | 0 | 0.0% |
| 11 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 912 | 1.82 | 1.533 | 3.353 |
| 2026-2027 | 61 | 192 | 1.721 | 1.426 | 3.148 |

## 3. Home vs away goal share
- Home goals: **600** (54.3%)
- Away goals: **504** (45.7%)
- Home/away ratio: **1.19**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 495 | 417 | 912 | 54.3% | 45.7% |
| 2026-2027 | 105 | 87 | 192 | 54.7% | 45.3% |

## 4. BTTS (Both Teams To Score)
- Overall: **190** of `333` (57.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 272 | 158 | 58.1% |
| 2026-2027 | 61 | 32 | 52.5% |

## 5. Clean sheets
- Home clean sheets: **89** (26.7%)
- Away clean sheets: **66** (19.8%)
- Total clean sheets recorded: **155**
- Matches with at least one clean sheet: **143** (42.9%)
- Both teams kept clean sheets (0-0): **12**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 73 | 48 | 121 | 114 (41.9%) |
| 2026-2027 | 61 | 16 | 18 | 34 | 29 (47.5%) |

## 6. Scoring intensity
- First-half goals: **522** (47.3%)
- Second-half goals: **582** (52.7%)
- Avg first-half goals per match: **1.568**
- Avg second-half goals per match: **1.748**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **51** (15.3%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 272 | 434 | 478 | 47.6% | 52.4% |
| 2026-2027 | 61 | 88 | 104 | 45.8% | 54.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `321` of `333` (96.4%)
- Goalless matches: `12`
- Min `1` | Max `91` | Mean `25.95` | Median (p50) `21`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 123 | 36.9% | 38.3% |
| 16-30 | 88 | 26.4% | 27.4% |
| 31-45 | 57 | 17.1% | 17.8% |
| 46-60 | 33 | 9.9% | 10.3% |
| 61-75 | 8 | 2.4% | 2.5% |
| 76-90 | 11 | 3.3% | 3.4% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\czech3b\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\czech3b\charts\goals_analysis_avg_per_season.png)

