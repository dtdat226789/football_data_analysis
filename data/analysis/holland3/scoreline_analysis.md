# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:00:48+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Tweede Divisie (Netherlands)
- Scope: league `holland3`

## 1. Scoreline frequency
- Matches analysed: **376** across **2** seasons.
- Distinct scorelines seen: **39**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 37 | 9.8% |
| 2-1 | 31 | 8.2% |
| 1-2 | 31 | 8.2% |
| 1-0 | 27 | 7.2% |
| 2-2 | 22 | 5.9% |
| 1-3 | 21 | 5.6% |
| 0-2 | 19 | 5.1% |
| 3-0 | 19 | 5.1% |
| 2-0 | 19 | 5.1% |
| 3-2 | 18 | 4.8% |
| 0-1 | 15 | 4.0% |
| 3-1 | 15 | 4.0% |
| 4-0 | 10 | 2.7% |
| 0-0 | 10 | 2.7% |
| 0-3 | 9 | 2.4% |
| 4-1 | 8 | 2.1% |
| 2-3 | 7 | 1.9% |
| 3-3 | 6 | 1.6% |
| 1-4 | 6 | 1.6% |
| 0-4 | 5 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 29 | 9.0% |
| 2-1 | 28 | 8.7% |
| 1-0 | 26 | 8.1% |
| 1-2 | 25 | 7.8% |
| 2-0 | 18 | 5.6% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 8 | 14.8% |
| 1-2 | 6 | 11.1% |
| 1-3 | 5 | 9.3% |
| 2-2 | 5 | 9.3% |
| 0-2 | 4 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 10 | 2.7% |
| 1 | 42 | 11.2% |
| 2 | 75 | 19.9% |
| 3 | 90 | 23.9% |
| 4 | 73 | 19.4% |
| 5 | 43 | 11.4% |
| 6 | 23 | 6.1% |
| 7 | 14 | 3.7% |
| 8 | 4 | 1.1% |
| 9 | 2 | 0.5% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **20**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-05-23 | 5-4 | 9 |
| 2026-2027 | 2026-08-22 | 3-6 | 9 |
| 2025-2026 | 2025-08-23 | 4-4 | 8 |
| 2025-2026 | 2025-10-11 | 4-4 | 8 |
| 2025-2026 | 2025-11-15 | 8-0 | 8 |
| 2025-2026 | 2026-04-11 | 6-2 | 8 |
| 2025-2026 | 2025-08-16 | 4-3 | 7 |
| 2025-2026 | 2025-09-27 | 4-3 | 7 |
| 2025-2026 | 2025-09-27 | 5-2 | 7 |
| 2025-2026 | 2025-10-04 | 5-2 | 7 |
| 2025-2026 | 2025-10-25 | 4-3 | 7 |
| 2025-2026 | 2025-12-13 | 3-4 | 7 |
| 2025-2026 | 2026-01-31 | 3-4 | 7 |
| 2025-2026 | 2026-03-07 | 4-3 | 7 |
| 2025-2026 | 2026-03-21 | 3-4 | 7 |
| 2025-2026 | 2026-05-16 | 5-2 | 7 |
| 2025-2026 | 2026-05-23 | 7-0 | 7 |
| 2025-2026 | 2026-06-03 | 0-7 | 7 |
| 2026-2027 | 2026-08-15 | 6-1 | 7 |
| 2026-2027 | 2026-09-12 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **299** (draws: **77**)
- Average winning margin: **1.99**

| margin | matches | pct |
|---|---|---|
| 1 | 137 | 45.8% |
| 2 | 82 | 27.4% |
| 3+ | 80 | 26.8% |

## 6. Margin by outcome

### Home wins
- Matches: **171** | avg margin: **2.05** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 81 | 47.4% |
| 2 | 37 | 21.6% |
| 3+ | 53 | 31.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **128** | avg margin: **1.91** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 43.8% |
| 2 | 45 | 35.2% |
| 3+ | 27 | 21.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 171 | 2-1 | 31 | 18.1% |
| draw | 77 | 1-1 | 37 | 48.1% |
| away | 128 | 1-2 | 31 | 24.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\holland3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\holland3\charts\scoreline_analysis_total_goals.png)

