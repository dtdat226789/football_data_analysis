# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:50:59+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Scoreline frequency
- Matches analysed: **153** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-2 | 12 | 7.8% |
| 2-1 | 12 | 7.8% |
| 0-2 | 12 | 7.8% |
| 2-0 | 11 | 7.2% |
| 0-3 | 11 | 7.2% |
| 1-0 | 11 | 7.2% |
| 1-1 | 11 | 7.2% |
| 0-1 | 11 | 7.2% |
| 2-2 | 8 | 5.2% |
| 0-0 | 8 | 5.2% |
| 3-0 | 7 | 4.6% |
| 3-1 | 5 | 3.3% |
| 0-4 | 5 | 3.3% |
| 6-1 | 3 | 2.0% |
| 4-0 | 3 | 2.0% |
| 3-2 | 2 | 1.3% |
| 1-8 | 2 | 1.3% |
| 1-5 | 2 | 1.3% |
| 5-0 | 2 | 1.3% |
| 2-3 | 2 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-2 | 11 | 8.1% |
| 2-1 | 11 | 8.1% |
| 0-3 | 11 | 8.1% |
| 0-1 | 11 | 8.1% |
| 1-1 | 10 | 7.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-2 | 3 | 16.7% |
| 1-0 | 3 | 16.7% |
| 2-0 | 2 | 11.1% |
| 1-7 | 1 | 5.6% |
| 5-1 | 1 | 5.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 8 | 5.2% |
| 1 | 22 | 14.4% |
| 2 | 34 | 22.2% |
| 3 | 42 | 27.5% |
| 4 | 21 | 13.7% |
| 5 | 7 | 4.6% |
| 6 | 6 | 3.9% |
| 7 | 6 | 3.9% |
| 8 | 5 | 3.3% |
| 9 | 2 | 1.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **13**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-03 | 1-8 | 9 |
| 2026-2027 | 2026-09-18 | 1-8 | 9 |
| 2025-2026 | 2026-02-21 | 2-6 | 8 |
| 2025-2026 | 2026-05-06 | 6-2 | 8 |
| 2025-2026 | 2026-05-16 | 8-0 | 8 |
| 2026-2027 | 2026-09-04 | 1-7 | 8 |
| 2026-2027 | 2026-09-12 | 7-1 | 8 |
| 2025-2026 | 2025-09-20 | 5-2 | 7 |
| 2025-2026 | 2025-09-27 | 3-4 | 7 |
| 2025-2026 | 2025-09-27 | 6-1 | 7 |
| 2025-2026 | 2025-10-18 | 6-1 | 7 |
| 2025-2026 | 2025-10-18 | 6-1 | 7 |
| 2025-2026 | 2025-12-13 | 0-7 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **125** (draws: **28**)
- Average winning margin: **2.31**

| margin | matches | pct |
|---|---|---|
| 1 | 51 | 40.8% |
| 2 | 30 | 24.0% |
| 3+ | 44 | 35.2% |

## 6. Margin by outcome

### Home wins
- Matches: **62** | avg margin: **2.29** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 25 | 40.3% |
| 2 | 17 | 27.4% |
| 3+ | 20 | 32.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **63** | avg margin: **2.33** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 26 | 41.3% |
| 2 | 13 | 20.6% |
| 3+ | 24 | 38.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 62 | 2-1 | 12 | 19.4% |
| draw | 28 | 1-1 | 11 | 39.3% |
| away | 63 | 1-2 | 12 | 19.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\wfrance1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\wfrance1\charts\scoreline_analysis_total_goals.png)

