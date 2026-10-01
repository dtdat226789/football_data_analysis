# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:46:11+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 44 | 6.7% |
| 1 | 110 | 16.8% |
| 2 | 158 | 24.2% |
| 3 | 169 | 25.8% |
| 4 | 110 | 16.8% |
| 5 | 41 | 6.3% |
| 6 | 14 | 2.1% |
| 7 | 4 | 0.6% |
| 8 | 4 | 0.6% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 559 | 1445 | 1.39 | 1.195 | 2.585 |
| 2026-2027 | 95 | 277 | 1.642 | 1.274 | 2.916 |

## 3. Home vs away goal share
- Home goals: **933** (54.2%)
- Away goals: **789** (45.8%)
- Home/away ratio: **1.183**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 777 | 668 | 1445 | 53.8% | 46.2% |
| 2026-2027 | 156 | 121 | 277 | 56.3% | 43.7% |

## 4. BTTS (Both Teams To Score)
- Overall: **380** of `654` (58.1%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 559 | 315 | 56.4% |
| 2026-2027 | 95 | 65 | 68.4% |

## 5. Clean sheets
- Home clean sheets: **177** (27.1%)
- Away clean sheets: **141** (21.6%)
- Total clean sheets recorded: **318**
- Matches with at least one clean sheet: **274** (41.9%)
- Both teams kept clean sheets (0-0): **44**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 559 | 157 | 124 | 281 | 244 (43.6%) |
| 2026-2027 | 95 | 20 | 17 | 37 | 30 (31.6%) |

## 6. Scoring intensity
- First-half goals: **807** (46.9%)
- Second-half goals: **914** (53.1%)
- Avg first-half goals per match: **1.238**
- Avg second-half goals per match: **1.402**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **138** (21.1%)
- *2 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 559 | 669 | 775 | 46.3% | 53.7% |
| 2026-2027 | 95 | 138 | 139 | 49.8% | 50.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `609` of `654` (93.1%)
- Goalless matches: `45`
- Min `1` | Max `97` | Mean `29.57` | Median (p50) `23`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 215 | 32.9% | 35.3% |
| 16-30 | 147 | 22.5% | 24.1% |
| 31-45 | 99 | 15.1% | 16.3% |
| 46-60 | 78 | 11.9% | 12.8% |
| 61-75 | 40 | 6.1% | 6.6% |
| 76-90 | 24 | 3.7% | 3.9% |
| 91-120 | 6 | 0.9% | 1.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\cha\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\cha\charts\goals_analysis_avg_per_season.png)

