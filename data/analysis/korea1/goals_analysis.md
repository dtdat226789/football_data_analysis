# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:47+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 36 | 9.5% |
| 1 | 71 | 18.8% |
| 2 | 90 | 23.9% |
| 3 | 82 | 21.8% |
| 4 | 52 | 13.8% |
| 5 | 35 | 9.3% |
| 6 | 6 | 1.6% |
| 7 | 4 | 1.1% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 198 | 512 | 1.389 | 1.197 | 2.586 |
| 2026 | 179 | 440 | 1.168 | 1.291 | 2.458 |

## 3. Home vs away goal share
- Home goals: **484** (50.8%)
- Away goals: **468** (49.2%)
- Home/away ratio: **1.034**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 275 | 237 | 512 | 53.7% | 46.3% |
| 2026 | 209 | 231 | 440 | 47.5% | 52.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **207** of `377` (54.9%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 198 | 112 | 56.6% |
| 2026 | 179 | 95 | 53.1% |

## 5. Clean sheets
- Home clean sheets: **105** (27.9%)
- Away clean sheets: **101** (26.8%)
- Total clean sheets recorded: **206**
- Matches with at least one clean sheet: **170** (45.1%)
- Both teams kept clean sheets (0-0): **36**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 198 | 56 | 46 | 102 | 86 (43.4%) |
| 2026 | 179 | 49 | 55 | 104 | 84 (46.9%) |

## 6. Scoring intensity
- First-half goals: **392** (41.2%)
- Second-half goals: **560** (58.8%)
- Avg first-half goals per match: **1.04**
- Avg second-half goals per match: **1.485**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **102** (27.1%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 198 | 211 | 301 | 41.2% | 58.8% |
| 2026 | 179 | 181 | 259 | 41.1% | 58.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `341` of `377` (90.5%)
- Goalless matches: `36`
- Min `1` | Max `97` | Mean `35.26` | Median (p50) `32`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 92 | 24.4% | 27.0% |
| 16-30 | 75 | 19.9% | 22.0% |
| 31-45 | 67 | 17.8% | 19.6% |
| 46-60 | 46 | 12.2% | 13.5% |
| 61-75 | 33 | 8.8% | 9.7% |
| 76-90 | 21 | 5.6% | 6.2% |
| 91-120 | 7 | 1.9% | 2.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\korea1\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\korea1\charts\goals_analysis_avg_per_season.png)

