# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:24:17+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Bundesliga Women (Germany)
- Scope: league `wgermany1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 7 | 3.2% |
| 1 | 22 | 10.1% |
| 2 | 43 | 19.8% |
| 3 | 53 | 24.4% |
| 4 | 27 | 12.4% |
| 5 | 34 | 15.7% |
| 6 | 21 | 9.7% |
| 7 | 5 | 2.3% |
| 8 | 4 | 1.8% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 182 | 627 | 1.786 | 1.659 | 3.445 |
| 2026-2027 | 35 | 121 | 1.829 | 1.629 | 3.457 |

## 3. Home vs away goal share
- Home goals: **389** (52.0%)
- Away goals: **359** (48.0%)
- Home/away ratio: **1.084**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 325 | 302 | 627 | 51.8% | 48.2% |
| 2026-2027 | 64 | 57 | 121 | 52.9% | 47.1% |

## 4. BTTS (Both Teams To Score)
- Overall: **131** of `217` (60.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 182 | 108 | 59.3% |
| 2026-2027 | 35 | 23 | 65.7% |

## 5. Clean sheets
- Home clean sheets: **50** (23.0%)
- Away clean sheets: **43** (19.8%)
- Total clean sheets recorded: **93**
- Matches with at least one clean sheet: **86** (39.6%)
- Both teams kept clean sheets (0-0): **7**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 182 | 42 | 39 | 81 | 74 (40.7%) |
| 2026-2027 | 35 | 8 | 4 | 12 | 12 (34.3%) |

## 6. Scoring intensity
- First-half goals: **325** (43.4%)
- Second-half goals: **423** (56.6%)
- Avg first-half goals per match: **1.498**
- Avg second-half goals per match: **1.949**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **35** (16.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 182 | 277 | 350 | 44.2% | 55.8% |
| 2026-2027 | 35 | 48 | 73 | 39.7% | 60.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `210` of `217` (96.8%)
- Goalless matches: `7`
- Min `1` | Max `93` | Mean `24.43` | Median (p50) `19.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 90 | 41.5% | 42.9% |
| 16-30 | 60 | 27.6% | 28.6% |
| 31-45 | 24 | 11.1% | 11.4% |
| 46-60 | 20 | 9.2% | 9.5% |
| 61-75 | 9 | 4.1% | 4.3% |
| 76-90 | 6 | 2.8% | 2.9% |
| 91-120 | 1 | 0.5% | 0.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wgermany1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wgermany1\charts\goals_analysis_avg_per_season.png)

