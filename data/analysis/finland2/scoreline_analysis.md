# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:58:30+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ykkosliiga (Finland)
- Scope: league `finland2`

## 1. Scoreline frequency
- Matches analysed: **255** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 28 | 11.0% |
| 1-0 | 23 | 9.0% |
| 2-1 | 22 | 8.6% |
| 0-1 | 22 | 8.6% |
| 3-1 | 18 | 7.1% |
| 1-2 | 16 | 6.3% |
| 0-2 | 16 | 6.3% |
| 2-2 | 16 | 6.3% |
| 0-0 | 13 | 5.1% |
| 2-0 | 11 | 4.3% |
| 0-3 | 9 | 3.5% |
| 3-0 | 8 | 3.1% |
| 2-3 | 7 | 2.7% |
| 4-2 | 6 | 2.4% |
| 3-2 | 5 | 2.0% |
| 1-4 | 5 | 2.0% |
| 1-3 | 4 | 1.6% |
| 4-1 | 4 | 1.6% |
| 3-3 | 4 | 1.6% |
| 4-0 | 3 | 1.2% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 19 | 14.1% |
| 2-1 | 12 | 8.9% |
| 1-2 | 11 | 8.1% |
| 3-1 | 11 | 8.1% |
| 2-2 | 9 | 6.7% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 15 | 12.5% |
| 0-1 | 15 | 12.5% |
| 0-2 | 12 | 10.0% |
| 2-1 | 10 | 8.3% |
| 1-1 | 9 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 13 | 5.1% |
| 1 | 45 | 17.6% |
| 2 | 55 | 21.6% |
| 3 | 55 | 21.6% |
| 4 | 41 | 16.1% |
| 5 | 24 | 9.4% |
| 6 | 12 | 4.7% |
| 7 | 6 | 2.4% |
| 8 | 3 | 1.2% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.4% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **10**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-04-23 | 4-6 | 10 |
| 2025 | 2025-05-25 | 5-3 | 8 |
| 2025 | 2025-06-18 | 5-3 | 8 |
| 2026 | 2026-08-30 | 2-6 | 8 |
| 2025 | 2025-04-22 | 3-4 | 7 |
| 2025 | 2025-05-10 | 3-4 | 7 |
| 2025 | 2025-07-04 | 4-3 | 7 |
| 2026 | 2026-05-03 | 5-2 | 7 |
| 2026 | 2026-05-08 | 4-3 | 7 |
| 2026 | 2026-08-22 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **194** (draws: **61**)
- Average winning margin: **1.74**

| margin | matches | pct |
|---|---|---|
| 1 | 100 | 51.5% |
| 2 | 58 | 29.9% |
| 3+ | 36 | 18.6% |

## 6. Margin by outcome

### Home wins
- Matches: **108** | avg margin: **1.73** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 49.1% |
| 2 | 37 | 34.3% |
| 3+ | 18 | 16.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **86** | avg margin: **1.76** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 47 | 54.7% |
| 2 | 21 | 24.4% |
| 3+ | 18 | 20.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 108 | 1-0 | 23 | 21.3% |
| draw | 61 | 1-1 | 28 | 45.9% |
| away | 86 | 0-1 | 22 | 25.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\finland2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\finland2\charts\scoreline_analysis_total_goals.png)

