# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T13:47:13+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.5% |
| 1 | 25 | 11.6% |
| 2 | 46 | 21.3% |
| 3 | 62 | 28.7% |
| 4 | 32 | 14.8% |
| 5 | 22 | 10.2% |
| 6 | 12 | 5.6% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 164 | 501 | 1.665 | 1.39 | 3.055 |
| 2026-2027 | 52 | 134 | 1.288 | 1.288 | 2.577 |

## 3. Home vs away goal share
- Home goals: **340** (53.5%)
- Away goals: **295** (46.5%)
- Home/away ratio: **1.153**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 273 | 228 | 501 | 54.5% | 45.5% |
| 2026-2027 | 67 | 67 | 134 | 50.0% | 50.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **122** of `216` (56.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 164 | 95 | 57.9% |
| 2026-2027 | 52 | 27 | 51.9% |

## 5. Clean sheets
- Home clean sheets: **61** (28.2%)
- Away clean sheets: **47** (21.8%)
- Total clean sheets recorded: **108**
- Matches with at least one clean sheet: **94** (43.5%)
- Both teams kept clean sheets (0-0): **14**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 164 | 45 | 32 | 77 | 69 (42.1%) |
| 2026-2027 | 52 | 16 | 15 | 31 | 25 (48.1%) |

## 6. Scoring intensity
- First-half goals: **284** (44.9%)
- Second-half goals: **348** (55.1%)
- Avg first-half goals per match: **1.321**
- Avg second-half goals per match: **1.619**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **25** (11.6%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 164 | 228 | 270 | 45.8% | 54.2% |
| 2026-2027 | 52 | 56 | 78 | 41.8% | 58.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `201` of `216` (93.1%)
- Goalless matches: `15`
- Min `1` | Max `94` | Mean `25.33` | Median (p50) `21`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 77 | 35.6% | 38.3% |
| 16-30 | 63 | 29.2% | 31.3% |
| 31-45 | 32 | 14.8% | 15.9% |
| 46-60 | 15 | 6.9% | 7.5% |
| 61-75 | 8 | 3.7% | 4.0% |
| 76-90 | 2 | 0.9% | 1.0% |
| 91-120 | 4 | 1.9% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\slovenia1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\slovenia1\charts\goals_analysis_avg_per_season.png)

