# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T15:50:27+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 42 | 10.8% |
| 1 | 60 | 15.5% |
| 2 | 103 | 26.5% |
| 3 | 102 | 26.3% |
| 4 | 49 | 12.6% |
| 5 | 23 | 5.9% |
| 6 | 4 | 1.0% |
| 7 | 4 | 1.0% |
| 8 | 1 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 738 | 1.267 | 1.168 | 2.436 |
| 2026-2027 | 85 | 205 | 1.259 | 1.153 | 2.412 |

## 3. Home vs away goal share
- Home goals: **491** (52.1%)
- Away goals: **452** (47.9%)
- Home/away ratio: **1.086**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025-2026 | 384 | 354 | 738 | 52.0% | 48.0% |
| 2026-2027 | 107 | 98 | 205 | 52.2% | 47.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **201** of `388` (51.8%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025-2026 | 303 | 162 | 53.5% |
| 2026-2027 | 85 | 39 | 45.9% |

## 5. Clean sheets
- Home clean sheets: **121** (31.2%)
- Away clean sheets: **108** (27.8%)
- Total clean sheets recorded: **229**
- Matches with at least one clean sheet: **187** (48.2%)
- Both teams kept clean sheets (0-0): **42**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 94 | 79 | 173 | 141 (46.5%) |
| 2026-2027 | 85 | 27 | 29 | 56 | 46 (54.1%) |

## 6. Scoring intensity
- First-half goals: **437** (46.5%)
- Second-half goals: **503** (53.5%)
- Avg first-half goals per match: **1.129**
- Avg second-half goals per match: **1.3**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **73** (18.8%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025-2026 | 303 | 337 | 398 | 45.9% | 54.1% |
| 2026-2027 | 85 | 100 | 105 | 48.8% | 51.2% |

## 7. First-goal timing
- Matches with first-goal time recorded: `345` of `388` (88.9%)
- Goalless matches: `43`
- Min `1` | Max `96` | Mean `29.41` | Median (p50) `24`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 121 | 31.2% | 35.1% |
| 16-30 | 88 | 22.7% | 25.5% |
| 31-45 | 53 | 13.7% | 15.4% |
| 46-60 | 42 | 10.8% | 12.2% |
| 61-75 | 27 | 7.0% | 7.8% |
| 76-90 | 9 | 2.3% | 2.6% |
| 91-120 | 5 | 1.3% | 1.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\france3\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\france3\charts\goals_analysis_avg_per_season.png)

