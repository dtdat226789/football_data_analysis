# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:04:05+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 17 | 4.2% |
| 1 | 49 | 12.0% |
| 2 | 88 | 21.6% |
| 3 | 96 | 23.5% |
| 4 | 70 | 17.2% |
| 5 | 56 | 13.7% |
| 6 | 18 | 4.4% |
| 7 | 5 | 1.2% |
| 8 | 5 | 1.2% |
| 9 | 3 | 0.7% |
| 10 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 240 | 762 | 1.808 | 1.367 | 3.175 |
| 2026 | 168 | 531 | 1.845 | 1.315 | 3.161 |

## 3. Home vs away goal share
- Home goals: **744** (57.5%)
- Away goals: **549** (42.5%)
- Home/away ratio: **1.355**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 434 | 328 | 762 | 57.0% | 43.0% |
| 2026 | 310 | 221 | 531 | 58.4% | 41.6% |

## 4. BTTS (Both Teams To Score)
- Overall: **234** of `408` (57.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 240 | 136 | 56.7% |
| 2026 | 168 | 98 | 58.3% |

## 5. Clean sheets
- Home clean sheets: **118** (28.9%)
- Away clean sheets: **73** (17.9%)
- Total clean sheets recorded: **191**
- Matches with at least one clean sheet: **174** (42.6%)
- Both teams kept clean sheets (0-0): **17**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 240 | 69 | 46 | 115 | 104 (43.3%) |
| 2026 | 168 | 49 | 27 | 76 | 70 (41.7%) |

## 6. Scoring intensity
- First-half goals: **601** (46.6%)
- Second-half goals: **689** (53.4%)
- Avg first-half goals per match: **1.477**
- Avg second-half goals per match: **1.693**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **65** (15.9%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 240 | 344 | 415 | 45.3% | 54.7% |
| 2026 | 168 | 257 | 274 | 48.4% | 51.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `390` of `408` (95.6%)
- Goalless matches: `18`
- Min `1` | Max `91` | Mean `26.31` | Median (p50) `22.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 160 | 39.2% | 41.0% |
| 16-30 | 89 | 21.8% | 22.8% |
| 31-45 | 64 | 15.7% | 16.4% |
| 46-60 | 43 | 10.5% | 11.0% |
| 61-75 | 20 | 4.9% | 5.1% |
| 76-90 | 13 | 3.2% | 3.3% |
| 91-120 | 1 | 0.2% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\norway\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\norway\charts\goals_analysis_avg_per_season.png)

