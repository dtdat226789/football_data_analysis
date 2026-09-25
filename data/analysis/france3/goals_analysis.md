# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T10:59:01+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 40 | 10.8% |
| 1 | 59 | 15.9% |
| 2 | 98 | 26.4% |
| 3 | 95 | 25.6% |
| 4 | 49 | 13.2% |
| 5 | 22 | 5.9% |
| 6 | 4 | 1.1% |
| 7 | 3 | 0.8% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 738 | 1.267 | 1.168 | 2.436 |
| 2026-2027 | 68 | 161 | 1.235 | 1.132 | 2.368 |

## 3. Home vs away goal share
- Home goals: **468** (52.1%)
- Away goals: **431** (47.9%)
- Home/away ratio: **1.086**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 384 | 354 | 738 | 52.0% | 48.0% |
| 2026-2027 | 84 | 77 | 161 | 52.2% | 47.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **188** of `371` (50.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 303 | 162 | 53.5% |
| 2026-2027 | 68 | 26 | 38.2% |

## 5. Clean sheets
- Home clean sheets: **118** (31.8%)
- Away clean sheets: **105** (28.3%)
- Total clean sheets recorded: **223**
- Matches with at least one clean sheet: **183** (49.3%)
- Both teams kept clean sheets (0-0): **40**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 94 | 79 | 173 | 141 (46.5%) |
| 2026-2027 | 68 | 24 | 26 | 50 | 42 (61.8%) |

## 6. Scoring intensity
- First-half goals: **415** (46.3%)
- Second-half goals: **481** (53.7%)
- Avg first-half goals per match: **1.122**
- Avg second-half goals per match: **1.3**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **71** (19.1%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 337 | 398 | 45.9% | 54.1% |
| 2026-2027 | 68 | 78 | 83 | 48.4% | 51.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `330` of `371` (88.9%)
- Goalless matches: `41`
- Min `1` | Max `96` | Mean `29.5` | Median (p50) `24.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 115 | 31.0% | 34.8% |
| 16-30 | 85 | 22.9% | 25.8% |
| 31-45 | 51 | 13.7% | 15.5% |
| 46-60 | 39 | 10.5% | 11.8% |
| 61-75 | 26 | 7.0% | 7.9% |
| 76-90 | 9 | 2.4% | 2.7% |
| 91-120 | 5 | 1.3% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\france3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\france3\charts\goals_analysis_avg_per_season.png)

