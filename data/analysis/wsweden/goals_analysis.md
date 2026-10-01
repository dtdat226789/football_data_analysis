# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:24:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 8 | 2.5% |
| 1 | 54 | 16.8% |
| 2 | 57 | 17.7% |
| 3 | 86 | 26.7% |
| 4 | 43 | 13.4% |
| 5 | 43 | 13.4% |
| 6 | 21 | 6.5% |
| 7 | 7 | 2.2% |
| 8 | 2 | 0.6% |
| 9 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 182 | 606 | 1.709 | 1.621 | 3.33 |
| 2026 | 140 | 407 | 1.614 | 1.293 | 2.907 |

## 3. Home vs away goal share
- Home goals: **537** (53.0%)
- Away goals: **476** (47.0%)
- Home/away ratio: **1.128**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 311 | 295 | 606 | 51.3% | 48.7% |
| 2026 | 226 | 181 | 407 | 55.5% | 44.5% |

## 4. BTTS (Both Teams To Score)
- Overall: **162** of `322` (50.3%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 182 | 100 | 54.9% |
| 2026 | 140 | 62 | 44.3% |

## 5. Clean sheets
- Home clean sheets: **92** (28.6%)
- Away clean sheets: **76** (23.6%)
- Total clean sheets recorded: **168**
- Matches with at least one clean sheet: **160** (49.7%)
- Both teams kept clean sheets (0-0): **8**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 182 | 47 | 39 | 86 | 82 (45.1%) |
| 2026 | 140 | 45 | 37 | 82 | 78 (55.7%) |

## 6. Scoring intensity
- First-half goals: **470** (46.4%)
- Second-half goals: **543** (53.6%)
- Avg first-half goals per match: **1.46**
- Avg second-half goals per match: **1.686**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **60** (18.6%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 182 | 266 | 340 | 43.9% | 56.1% |
| 2026 | 140 | 204 | 203 | 50.1% | 49.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `314` of `322` (97.5%)
- Goalless matches: `8`
- Min `1` | Max `95` | Mean `26.9` | Median (p50) `20.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 125 | 38.8% | 39.8% |
| 16-30 | 83 | 25.8% | 26.4% |
| 31-45 | 41 | 12.7% | 13.1% |
| 46-60 | 35 | 10.9% | 11.1% |
| 61-75 | 17 | 5.3% | 5.4% |
| 76-90 | 12 | 3.7% | 3.8% |
| 91-120 | 1 | 0.3% | 0.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\wsweden\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\wsweden\charts\goals_analysis_avg_per_season.png)

