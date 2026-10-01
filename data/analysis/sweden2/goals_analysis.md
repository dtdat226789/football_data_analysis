# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-09-29T16:09:33+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.0% |
| 1 | 67 | 15.2% |
| 2 | 96 | 21.8% |
| 3 | 91 | 20.7% |
| 4 | 81 | 18.4% |
| 5 | 43 | 9.8% |
| 6 | 25 | 5.7% |
| 7 | 4 | 0.9% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2025 | 240 | 686 | 1.6 | 1.258 | 2.858 |
| 2026 | 200 | 580 | 1.495 | 1.405 | 2.9 |

## 3. Home vs away goal share
- Home goals: **683** (53.9%)
- Away goals: **583** (46.1%)
- Home/away ratio: **1.172**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2025 | 384 | 302 | 686 | 56.0% | 44.0% |
| 2026 | 299 | 281 | 580 | 51.6% | 48.4% |

## 4. BTTS (Both Teams To Score)
- Overall: **253** of `440` (57.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2025 | 240 | 132 | 55.0% |
| 2026 | 200 | 121 | 60.5% |

## 5. Clean sheets
- Home clean sheets: **117** (26.6%)
- Away clean sheets: **101** (23.0%)
- Total clean sheets recorded: **218**
- Matches with at least one clean sheet: **187** (42.5%)
- Both teams kept clean sheets (0-0): **31**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2025 | 240 | 70 | 56 | 126 | 108 (45.0%) |
| 2026 | 200 | 47 | 45 | 92 | 79 (39.5%) |

## 6. Scoring intensity
- First-half goals: **547** (43.3%)
- Second-half goals: **716** (56.7%)
- Avg first-half goals per match: **1.246**
- Avg second-half goals per match: **1.631**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **92** (20.9%)
- *1 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2025 | 240 | 296 | 390 | 43.1% | 56.9% |
| 2026 | 200 | 251 | 326 | 43.5% | 56.5% |

## 7. First-goal timing
- Matches with first-goal time recorded: `408` of `440` (92.7%)
- Goalless matches: `32`
- Min `1` | Max `95` | Mean `29.18` | Median (p50) `23.0`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 154 | 35.0% | 37.7% |
| 16-30 | 85 | 19.3% | 20.8% |
| 31-45 | 72 | 16.4% | 17.6% |
| 46-60 | 48 | 10.9% | 11.8% |
| 61-75 | 26 | 5.9% | 6.4% |
| 76-90 | 17 | 3.9% | 4.2% |
| 91-120 | 6 | 1.4% | 1.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](E:\football_data_analysis\data\analysis\sweden2\charts\goals_analysis_distribution.png)
![goals_analysis_avg_per_season](E:\football_data_analysis\data\analysis\sweden2\charts\goals_analysis_avg_per_season.png)

