# Goal Analysis
- Report: `goals_analysis`
- Generated: 2026-10-29T01:57:39+00:00
- Script: `backend/scripts/analyze_goals.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Goals per match distribution
| goals | matches | pct |
|---|---|---|
| 0 | 1 | 1.5% |
| 1 | 6 | 8.8% |
| 2 | 11 | 16.2% |
| 3 | 8 | 11.8% |
| 4 | 20 | 29.4% |
| 5 | 6 | 8.8% |
| 6 | 7 | 10.3% |
| 7 | 5 | 7.4% |
| 8 | 2 | 2.9% |
| 9 | 1 | 1.5% |
| 10 | 1 | 1.5% |

## 2. Goals per match per season
| season | matches | total goals | avg home | avg away | avg total |
|---|---|---|---|---|---|
| 2026-2027 | 68 | 274 | 2.103 | 1.926 | 4.029 |

## 3. Home vs away goal share
- Home goals: **143** (52.2%)
- Away goals: **131** (47.8%)
- Home/away ratio: **1.092**

| season | home goals | away goals | total | home pct | away pct |
|---|---|---|---|---|---|
| 2026-2027 | 143 | 131 | 274 | 52.2% | 47.8% |

## 4. BTTS (Both Teams To Score)
- Overall: **48** of `68` (70.6%)

| season | matches | BTTS | pct |
|---|---|---|---|
| 2026-2027 | 68 | 48 | 70.6% |

## 5. Clean sheets
- Home clean sheets: **10** (14.7%)
- Away clean sheets: **11** (16.2%)
- Total clean sheets recorded: **21**
- Matches with at least one clean sheet: **20** (29.4%)
- Both teams kept clean sheets (0-0): **1**

| season | matches | home CS | away CS | total CS | matches w/ CS |
|---|---|---|---|---|---|
| 2026-2027 | 68 | 10 | 11 | 21 | 20 (29.4%) |

## 6. Scoring intensity
- First-half goals: **138** (50.4%)
- Second-half goals: **136** (49.6%)
- Avg first-half goals per match: **2.029**
- Avg second-half goals per match: **2.0**
- Second-half-only scoring (HT 0-0, FT goals >= 1): **6** (8.8%)

| season | matches | 1st half | 2nd half | 1st half pct | 2nd half pct |
|---|---|---|---|---|---|
| 2026-2027 | 68 | 138 | 136 | 50.4% | 49.6% |

## 7. First-goal timing
- Matches with first-goal time recorded: `67` of `68` (98.5%)
- Goalless matches: `1`
- Min `1` | Max `70` | Mean `23.69` | Median (p50) `20`

| bucket | count | % of matches | % of scoring matches |
|---|---|---|---|
| 1-15 | 23 | 33.8% | 34.3% |
| 16-30 | 24 | 35.3% | 35.8% |
| 31-45 | 14 | 20.6% | 20.9% |
| 46-60 | 3 | 4.4% | 4.5% |
| 61-75 | 3 | 4.4% | 4.5% |
| 76-90 | 0 | 0.0% | 0.0% |
| 91-120 | 0 | 0.0% | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_goals.py` to regenerate.*

## Charts

![goals_analysis_distribution](charts/goals_analysis_distribution.png)
![goals_analysis_avg_per_season](charts/goals_analysis_avg_per_season.png)

