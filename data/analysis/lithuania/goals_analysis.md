# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-26T01:40:54+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 100 | 9.0% |
| 1 | 201 | 18.1% |
| 2 | 275 | 24.8% |
| 3 | 235 | 21.2% |
| 4 | 162 | 14.6% |
| 5 | 87 | 7.8% |
| 6 | 38 | 3.4% |
| 7 | 8 | 0.7% |
| 8 | 4 | 0.4% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2020 | 60 | 156 | 1.4 | 1.2 | 2.6 |
| 2021 | 180 | 493 | 1.461 | 1.278 | 2.739 |
| 2022 | 180 | 471 | 1.406 | 1.211 | 2.617 |
| 2023 | 180 | 431 | 1.289 | 1.106 | 2.394 |
| 2024 | 180 | 423 | 1.189 | 1.161 | 2.35 |
| 2025 | 180 | 479 | 1.433 | 1.228 | 2.661 |
| 2026 | 150 | 402 | 1.473 | 1.207 | 2.68 |

## 3. Home vs away goal share
- Home goals: **1525** (53.4%)
- Away goals: **1330** (46.6%)
- Home/away ratio: **1.147**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2020 | 84 | 72 | 156 | 53.8% | 46.2% |
| 2021 | 263 | 230 | 493 | 53.3% | 46.7% |
| 2022 | 253 | 218 | 471 | 53.7% | 46.3% |
| 2023 | 232 | 199 | 431 | 53.8% | 46.2% |
| 2024 | 214 | 209 | 423 | 50.6% | 49.4% |
| 2025 | 258 | 221 | 479 | 53.9% | 46.1% |
| 2026 | 221 | 181 | 402 | 55.0% | 45.0% |

## 4. BTTS (Both Teams To Score)
- Overall: **516** of `1110` (46.5%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2020 | 60 | 28 | 46.7% |
| 2021 | 180 | 97 | 53.9% |
| 2022 | 180 | 81 | 45.0% |
| 2023 | 180 | 69 | 38.3% |
| 2024 | 180 | 78 | 43.3% |
| 2025 | 180 | 92 | 51.1% |
| 2026 | 150 | 71 | 47.3% |

## 5. Clean sheets
- Home clean sheets: **361** (32.5%)
- Away clean sheets: **333** (30.0%)
- Total clean sheets recorded: **694**
- Matches with at least one clean sheet: **594** (53.5%)
- Both teams kept clean sheets (0-0): **100**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2020 | 60 | 19 | 15 | 34 | 32 (53.3%) |
| 2021 | 180 | 50 | 43 | 93 | 83 (46.1%) |
| 2022 | 180 | 58 | 56 | 114 | 99 (55.0%) |
| 2023 | 180 | 73 | 59 | 132 | 111 (61.7%) |
| 2024 | 180 | 57 | 68 | 125 | 102 (56.7%) |
| 2025 | 180 | 51 | 50 | 101 | 88 (48.9%) |
| 2026 | 150 | 53 | 42 | 95 | 79 (52.7%) |

## 6. Scoring intensity
- First-half goals: **1231** (43.3%)
- Second-half goals: **1615** (56.7%)
- Avg first-half goals per match: **1.112**
- Avg second-half goals per match: **1.459**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **271** (24.4%)
- *3 match(es) excluded (no HT score recorded).*

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2020 | 60 | 69 | 87 | 44.2% | 55.8% |
| 2021 | 180 | 209 | 284 | 42.4% | 57.6% |
| 2022 | 180 | 217 | 254 | 46.1% | 53.9% |
| 2023 | 180 | 175 | 253 | 40.9% | 59.1% |
| 2024 | 180 | 175 | 245 | 41.7% | 58.3% |
| 2025 | 180 | 210 | 269 | 43.8% | 56.2% |
| 2026 | 150 | 176 | 223 | 44.1% | 55.9% |

## 7. First-goal timing
- Matches with first-goal time recorded: `1007` of `1110` (90.7%)
- Goalless matches: `103`
- Min `1` | Max `99` | Mean `33.13` | Median (p50) `28`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 307 | 27.7% | 30.5% |
| 16-30 | 238 | 21.4% | 23.6% |
| 31-45 | 170 | 15.3% | 16.9% |
| 46-60 | 142 | 12.8% | 14.1% |
| 61-75 | 75 | 6.8% | 7.4% |
| 76-90 | 57 | 5.1% | 5.7% |
| 91-120 | 18 | 1.6% | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

