# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:54:12+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Scoreline frequency
- Matches analysed: **245** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 12.7% |
| 2-1 | 24 | 9.8% |
| 0-1 | 21 | 8.6% |
| 2-2 | 17 | 6.9% |
| 1-2 | 17 | 6.9% |
| 1-0 | 15 | 6.1% |
| 1-3 | 14 | 5.7% |
| 3-1 | 11 | 4.5% |
| 3-0 | 11 | 4.5% |
| 2-0 | 11 | 4.5% |
| 0-0 | 10 | 4.1% |
| 0-2 | 9 | 3.7% |
| 3-2 | 7 | 2.9% |
| 0-3 | 6 | 2.4% |
| 4-0 | 5 | 2.0% |
| 3-3 | 4 | 1.6% |
| 1-4 | 4 | 1.6% |
| 5-0 | 3 | 1.2% |
| 2-3 | 3 | 1.2% |
| 5-2 | 3 | 1.2% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 25 | 12.6% |
| 2-1 | 20 | 10.1% |
| 0-1 | 18 | 9.1% |
| 1-3 | 14 | 7.1% |
| 2-2 | 13 | 6.6% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 6 | 12.8% |
| 2-1 | 4 | 8.5% |
| 2-2 | 4 | 8.5% |
| 1-2 | 4 | 8.5% |
| 2-4 | 3 | 6.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 10 | 4.1% |
| 1 | 36 | 14.7% |
| 2 | 51 | 20.8% |
| 3 | 58 | 23.7% |
| 4 | 49 | 20.0% |
| 5 | 20 | 8.2% |
| 6 | 13 | 5.3% |
| 7 | 5 | 2.0% |
| 8 | 1 | 0.4% |
| 9 | 2 | 0.8% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-17 | 2-7 | 9 |
| 2025-2026 | 2026-04-17 | 7-2 | 9 |
| 2025-2026 | 2025-11-08 | 5-3 | 8 |
| 2025-2026 | 2025-10-26 | 5-2 | 7 |
| 2025-2026 | 2025-12-13 | 3-4 | 7 |
| 2025-2026 | 2026-02-22 | 3-4 | 7 |
| 2025-2026 | 2026-05-03 | 5-2 | 7 |
| 2026-2027 | 2026-08-03 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **183** (draws: **62**)
- Average winning margin: **1.87**

| margin | matches | pct |
|---|---|---|
| 1 | 89 | 48.6% |
| 2 | 52 | 28.4% |
| 3+ | 42 | 23.0% |

## 6. Margin by outcome

### Home wins
- Matches: **98** | avg margin: **1.95** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 46 | 46.9% |
| 2 | 26 | 26.5% |
| 3+ | 26 | 26.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **85** | avg margin: **1.79** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 43 | 50.6% |
| 2 | 26 | 30.6% |
| 3+ | 16 | 18.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 98 | 2-1 | 24 | 24.5% |
| draw | 62 | 1-1 | 31 | 50.0% |
| away | 85 | 0-1 | 21 | 24.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\hungary1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\hungary1\charts\scoreline_analysis_total_goals.png)

