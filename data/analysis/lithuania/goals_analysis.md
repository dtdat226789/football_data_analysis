# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:03:25+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 29 | 9.0% |
| 1 | 52 | 16.0% |
| 2 | 73 | 22.5% |
| 3 | 76 | 23.5% |
| 4 | 54 | 16.7% |
| 5 | 27 | 8.3% |
| 6 | 8 | 2.5% |
| 7 | 5 | 1.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 180 | 479 | 1.433 | 1.228 | 2.661 |
| 2026 | 144 | 381 | 1.431 | 1.215 | 2.646 |

## 3. Home vs away goal share
- Home goals: **464** (54.0%)
- Away goals: **396** (46.0%)
- Home/away ratio: **1.172**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 258 | 221 | 479 | 53.9% | 46.1% |
| 2026 | 206 | 175 | 381 | 54.1% | 45.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **160** of `324` (49.4%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 180 | 92 | 51.1% |
| 2026 | 144 | 68 | 47.2% |

## 5. Clean sheets
- Home clean sheets: **102** (31.5%)
- Away clean sheets: **91** (28.1%)
- Total clean sheets recorded: **193**
- Matches with at least one clean sheet: **164** (50.6%)
- Both teams kept clean sheets (0-0): **29**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 180 | 51 | 50 | 101 | 88 (48.9%) |
| 2026 | 144 | 51 | 41 | 92 | 76 (52.8%) |

## 6. Scoring intensity
- First-half goals: **379** (44.2%)
- Second-half goals: **478** (55.8%)
- Avg first-half goals per match: **1.173**
- Avg second-half goals per match: **1.48**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **71** (21.9%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 180 | 210 | 269 | 43.8% | 56.2% |
| 2026 | 144 | 169 | 209 | 44.7% | 55.3% |

## 7. First-goal timing
- Matches with first-goal time recorded: `294` of `324` (90.7%)
- Goalless matches: `30`
- Min `1` | Max `99` | Mean `32.58` | Median (p50) `28.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 87 | 26.9% | 29.6% |
| 16-30 | 67 | 20.7% | 22.8% |
| 31-45 | 60 | 18.5% | 20.4% |
| 46-60 | 39 | 12.0% | 13.3% |
| 61-75 | 23 | 7.1% | 7.8% |
| 76-90 | 12 | 3.7% | 4.1% |
| 91-120 | 6 | 1.9% | 2.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\lithuania\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\lithuania\charts\goals_analysis_avg_per_season.png)

