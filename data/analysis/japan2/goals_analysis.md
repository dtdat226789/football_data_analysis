# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-23T11:02:38+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 75 | 9.9% |
| 1 | 166 | 21.8% |
| 2 | 165 | 21.7% |
| 3 | 166 | 21.8% |
| 4 | 100 | 13.2% |
| 5 | 55 | 7.2% |
| 6 | 22 | 2.9% |
| 7 | 9 | 1.2% |
| 8 | 2 | 0.3% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2024 | 380 | 946 | 1.368 | 1.121 | 2.489 |
| 2025 | 380 | 934 | 1.282 | 1.176 | 2.458 |

## 3. Home vs away goal share
- Home goals: **1007** (53.6%)
- Away goals: **873** (46.4%)
- Home/away ratio: **1.153**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2024 | 520 | 426 | 946 | 55.0% | 45.0% |
| 2025 | 487 | 447 | 934 | 52.1% | 47.9% |

## 4. BTTS (Both Teams To Score)
- Overall: **378** of `760` (49.7%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2024 | 380 | 183 | 48.2% |
| 2025 | 380 | 195 | 51.3% |

## 5. Clean sheets
- Home clean sheets: **251** (33.0%)
- Away clean sheets: **206** (27.1%)
- Total clean sheets recorded: **457**
- Matches with at least one clean sheet: **382** (50.3%)
- Both teams kept clean sheets (0-0): **75**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2024 | 380 | 135 | 99 | 234 | 197 (51.8%) |
| 2025 | 380 | 116 | 107 | 223 | 185 (48.7%) |

## 6. Scoring intensity
- First-half goals: **815** (43.4%)
- Second-half goals: **1065** (56.6%)
- Avg first-half goals per match: **1.072**
- Avg second-half goals per match: **1.401**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **171** (22.5%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2024 | 380 | 403 | 543 | 42.6% | 57.4% |
| 2025 | 380 | 412 | 522 | 44.1% | 55.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `685` of `760` (90.1%)
- Goalless matches: `75`
- Min `1` | Max `96` | Mean `32.32` | Median (p50) `27`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 206 | 27.1% | 30.1% |
| 16-30 | 167 | 22.0% | 24.4% |
| 31-45 | 132 | 17.4% | 19.3% |
| 46-60 | 85 | 11.2% | 12.4% |
| 61-75 | 48 | 6.3% | 7.0% |
| 76-90 | 34 | 4.5% | 5.0% |
| 91-120 | 13 | 1.7% | 1.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\japan2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\japan2\charts\goals_analysis_avg_per_season.png)

