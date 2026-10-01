# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:49:35+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Scoreline frequency
- Matches analysed: **273** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 32 | 11.7% |
| 1-0 | 26 | 9.5% |
| 2-1 | 23 | 8.4% |
| 0-1 | 22 | 8.1% |
| 0-0 | 18 | 6.6% |
| 3-2 | 17 | 6.2% |
| 2-2 | 16 | 5.9% |
| 3-0 | 14 | 5.1% |
| 1-2 | 13 | 4.8% |
| 0-2 | 12 | 4.4% |
| 2-0 | 12 | 4.4% |
| 3-1 | 10 | 3.7% |
| 2-3 | 10 | 3.7% |
| 1-3 | 9 | 3.3% |
| 0-4 | 7 | 2.6% |
| 4-1 | 4 | 1.5% |
| 0-3 | 4 | 1.5% |
| 5-0 | 4 | 1.5% |
| 1-4 | 3 | 1.1% |
| 4-3 | 2 | 0.7% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 3-2 | 12 | 9.1% |
| 0-1 | 11 | 8.3% |
| 2-2 | 11 | 8.3% |
| 2-1 | 11 | 8.3% |
| 1-1 | 10 | 7.6% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 22 | 15.6% |
| 1-0 | 19 | 13.5% |
| 2-1 | 12 | 8.5% |
| 0-1 | 11 | 7.8% |
| 0-0 | 10 | 7.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 18 | 6.6% |
| 1 | 48 | 17.6% |
| 2 | 56 | 20.5% |
| 3 | 54 | 19.8% |
| 4 | 43 | 15.8% |
| 5 | 39 | 14.3% |
| 6 | 9 | 3.3% |
| 7 | 4 | 1.5% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.4% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-08-24 | 8-2 | 10 |
| 2025 | 2025-07-01 | 6-2 | 8 |
| 2025 | 2025-04-05 | 4-3 | 7 |
| 2025 | 2025-08-09 | 2-5 | 7 |
| 2026 | 2026-06-13 | 2-5 | 7 |
| 2026 | 2026-06-23 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **206** (draws: **67**)
- Average winning margin: **1.8**

| margin | matches | pct |
|---|---|---|
| 1 | 113 | 54.9% |
| 2 | 47 | 22.8% |
| 3+ | 46 | 22.3% |

## 6. Margin by outcome

### Home wins
- Matches: **119** | avg margin: **1.78** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 68 | 57.1% |
| 2 | 24 | 20.2% |
| 3+ | 27 | 22.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **87** | avg margin: **1.83** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 45 | 51.7% |
| 2 | 23 | 26.4% |
| 3+ | 19 | 21.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 119 | 1-0 | 26 | 21.8% |
| draw | 67 | 1-1 | 32 | 47.8% |
| away | 87 | 0-1 | 22 | 25.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\finland1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\finland1\charts\scoreline_analysis_total_goals.png)

