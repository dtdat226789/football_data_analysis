# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:56:51+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 3. CFL - Group B (Czech Republic)
- Scope: league `czech3b`

## 1. Scoreline frequency
- Matches analysed: **326** across **2** seasons.
- Distinct scorelines seen: **42**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 11.0% |
| 1-2 | 23 | 7.1% |
| 2-0 | 22 | 6.7% |
| 1-0 | 21 | 6.4% |
| 2-1 | 20 | 6.1% |
| 2-2 | 20 | 6.1% |
| 0-2 | 17 | 5.2% |
| 3-0 | 17 | 5.2% |
| 0-1 | 16 | 4.9% |
| 2-3 | 13 | 4.0% |
| 3-1 | 12 | 3.7% |
| 0-0 | 12 | 3.7% |
| 4-1 | 9 | 2.8% |
| 0-3 | 9 | 2.8% |
| 4-0 | 7 | 2.1% |
| 1-3 | 7 | 2.1% |
| 3-2 | 7 | 2.1% |
| 3-3 | 6 | 1.8% |
| 5-0 | 6 | 1.8% |
| 0-4 | 6 | 1.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 11.4% |
| 2-0 | 20 | 7.4% |
| 1-2 | 18 | 6.6% |
| 1-0 | 17 | 6.2% |
| 2-1 | 16 | 5.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-2 | 5 | 9.3% |
| 0-0 | 5 | 9.3% |
| 1-1 | 5 | 9.3% |
| 2-2 | 5 | 9.3% |
| 2-1 | 4 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 12 | 3.7% |
| 1 | 37 | 11.3% |
| 2 | 75 | 23.0% |
| 3 | 69 | 21.2% |
| 4 | 52 | 16.0% |
| 5 | 42 | 12.9% |
| 6 | 20 | 6.1% |
| 7 | 10 | 3.1% |
| 8 | 6 | 1.8% |
| 9 | 2 | 0.6% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **19**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-05-06 | 2-9 | 11 |
| 2025-2026 | 2025-11-08 | 3-6 | 9 |
| 2025-2026 | 2026-05-03 | 8-1 | 9 |
| 2025-2026 | 2025-10-04 | 3-5 | 8 |
| 2025-2026 | 2025-11-16 | 2-6 | 8 |
| 2025-2026 | 2025-11-22 | 1-7 | 8 |
| 2025-2026 | 2026-04-11 | 5-3 | 8 |
| 2025-2026 | 2026-04-18 | 4-4 | 8 |
| 2026-2027 | 2026-09-12 | 4-4 | 8 |
| 2025-2026 | 2025-09-06 | 5-2 | 7 |
| 2025-2026 | 2025-09-13 | 4-3 | 7 |
| 2025-2026 | 2026-03-08 | 1-6 | 7 |
| 2025-2026 | 2026-05-06 | 4-3 | 7 |
| 2025-2026 | 2026-05-06 | 2-5 | 7 |
| 2025-2026 | 2026-05-31 | 7-0 | 7 |
| 2025-2026 | 2026-05-31 | 5-2 | 7 |
| 2026-2027 | 2026-08-08 | 6-1 | 7 |
| 2026-2027 | 2026-08-16 | 5-2 | 7 |
| 2026-2027 | 2026-08-30 | 7-0 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **250** (draws: **76**)
- Average winning margin: **2.2**

| margin | matches | pct |
|---|---|---|
| 1 | 102 | 40.8% |
| 2 | 65 | 26.0% |
| 3+ | 83 | 33.2% |

## 6. Margin by outcome

### Home wins
- Matches: **140** | avg margin: **2.31** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 50 | 35.7% |
| 2 | 39 | 27.9% |
| 3+ | 51 | 36.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **110** | avg margin: **2.05** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 52 | 47.3% |
| 2 | 26 | 23.6% |
| 3+ | 32 | 29.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 140 | 2-0 | 22 | 15.7% |
| draw | 76 | 1-1 | 36 | 47.4% |
| away | 110 | 1-2 | 23 | 20.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\czech3b\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\czech3b\charts\scoreline_analysis_total_goals.png)

