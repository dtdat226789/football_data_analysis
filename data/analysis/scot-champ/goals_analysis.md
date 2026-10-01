# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:05:46+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 12.6% |
| 1 | 42 | 18.2% |
| 2 | 65 | 28.1% |
| 3 | 44 | 19.0% |
| 4 | 28 | 12.1% |
| 5 | 15 | 6.5% |
| 6 | 7 | 3.0% |
| 7 | 1 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 460 | 1.326 | 1.095 | 2.421 |
| 2026-2027 | 41 | 80 | 1.122 | 0.829 | 1.951 |

## 3. Home vs away goal share
- Home goals: **298** (55.2%)
- Away goals: **242** (44.8%)
- Home/away ratio: **1.231**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 252 | 208 | 460 | 54.8% | 45.2% |
| 2026-2027 | 46 | 34 | 80 | 57.5% | 42.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **107** of `231` (46.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 190 | 93 | 48.9% |
| 2026-2027 | 41 | 14 | 34.1% |

## 5. Clean sheets
- Home clean sheets: **82** (35.5%)
- Away clean sheets: **71** (30.7%)
- Total clean sheets recorded: **153**
- Matches with at least one clean sheet: **124** (53.7%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 63 | 59 | 122 | 97 (51.1%) |
| 2026-2027 | 41 | 19 | 12 | 31 | 27 (65.9%) |

## 6. Scoring intensity
- First-half goals: **255** (47.2%)
- Second-half goals: **285** (52.8%)
- Avg first-half goals per match: **1.104**
- Avg second-half goals per match: **1.234**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **41** (17.7%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 190 | 215 | 245 | 46.7% | 53.3% |
| 2026-2027 | 41 | 40 | 40 | 50.0% | 50.0% |

## 7. First-goal timing
- Matches with first-goal time recorded: `202` of `231` (87.4%)
- Goalless matches: `29`
- Min `1` | Max `88` | Mean `29.51` | Median (p50) `25.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 60 | 26.0% | 29.7% |
| 16-30 | 56 | 24.2% | 27.7% |
| 31-45 | 41 | 17.7% | 20.3% |
| 46-60 | 27 | 11.7% | 13.4% |
| 61-75 | 10 | 4.3% | 5.0% |
| 76-90 | 8 | 3.5% | 4.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\scot-champ\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\scot-champ\charts\goals_analysis_avg_per_season.png)

