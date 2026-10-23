# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:46:55+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

## 1. Scoreline frequency
- Matches analysed: **351** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 37 | 10.5% |
| 2-0 | 35 | 10.0% |
| 2-1 | 31 | 8.8% |
| 1-0 | 28 | 8.0% |
| 1-2 | 28 | 8.0% |
| 0-0 | 27 | 7.7% |
| 0-1 | 24 | 6.8% |
| 0-2 | 20 | 5.7% |
| 3-1 | 17 | 4.8% |
| 1-3 | 15 | 4.3% |
| 2-2 | 14 | 4.0% |
| 0-3 | 14 | 4.0% |
| 3-0 | 13 | 3.7% |
| 3-2 | 8 | 2.3% |
| 2-4 | 5 | 1.4% |
| 4-0 | 5 | 1.4% |
| 3-3 | 3 | 0.9% |
| 4-1 | 3 | 0.9% |
| 2-3 | 3 | 0.9% |
| 1-4 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 30 | 10.7% |
| 2-0 | 29 | 10.4% |
| 1-0 | 24 | 8.6% |
| 0-0 | 23 | 8.2% |
| 1-2 | 22 | 7.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 9 | 12.7% |
| 1-1 | 7 | 9.9% |
| 2-0 | 6 | 8.5% |
| 1-2 | 6 | 8.5% |
| 0-2 | 5 | 7.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 27 | 7.7% |
| 1 | 52 | 14.8% |
| 2 | 92 | 26.2% |
| 3 | 86 | 24.5% |
| 4 | 54 | 15.4% |
| 5 | 21 | 6.0% |
| 6 | 12 | 3.4% |
| 7 | 4 | 1.1% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-08 | 5-5 | 10 |
| 2025-2026 | 2025-11-09 | 3-5 | 8 |
| 2025-2026 | 2026-03-08 | 6-2 | 8 |
| 2025-2026 | 2025-11-23 | 4-3 | 7 |
| 2025-2026 | 2025-12-13 | 4-3 | 7 |
| 2025-2026 | 2026-02-28 | 5-2 | 7 |
| 2025-2026 | 2026-03-15 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **269** (draws: **82**)
- Average winning margin: **1.82**

| margin | matches | pct |
|---|---|---|
| 1 | 124 | 46.1% |
| 2 | 93 | 34.6% |
| 3+ | 52 | 19.3% |

## 6. Margin by outcome

### Home wins
- Matches: **150** | avg margin: **1.83** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 69 | 46.0% |
| 2 | 52 | 34.7% |
| 3+ | 29 | 19.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **119** | avg margin: **1.8** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 55 | 46.2% |
| 2 | 41 | 34.5% |
| 3+ | 23 | 19.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 150 | 2-0 | 35 | 23.3% |
| draw | 82 | 1-1 | 37 | 45.1% |
| away | 119 | 1-2 | 28 | 23.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\czech1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\czech1\charts\scoreline_analysis_total_goals.png)

