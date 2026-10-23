# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:56:40+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Scoreline frequency
- Matches analysed: **430** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 45 | 10.5% |
| 1-1 | 43 | 10.0% |
| 0-1 | 42 | 9.8% |
| 2-1 | 39 | 9.1% |
| 0-0 | 36 | 8.4% |
| 1-2 | 36 | 8.4% |
| 0-2 | 34 | 7.9% |
| 2-0 | 29 | 6.7% |
| 2-2 | 24 | 5.6% |
| 0-3 | 16 | 3.7% |
| 3-2 | 12 | 2.8% |
| 3-0 | 12 | 2.8% |
| 3-1 | 11 | 2.6% |
| 4-0 | 9 | 2.1% |
| 2-3 | 8 | 1.9% |
| 1-3 | 7 | 1.6% |
| 3-3 | 5 | 1.2% |
| 4-1 | 4 | 0.9% |
| 1-4 | 4 | 0.9% |
| 5-0 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 41 | 10.8% |
| 1-1 | 37 | 9.7% |
| 0-1 | 37 | 9.7% |
| 0-0 | 36 | 9.5% |
| 2-1 | 33 | 8.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 6 | 12.0% |
| 2-1 | 6 | 12.0% |
| 0-1 | 5 | 10.0% |
| 1-2 | 5 | 10.0% |
| 0-2 | 4 | 8.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 36 | 8.4% |
| 1 | 87 | 20.2% |
| 2 | 106 | 24.7% |
| 3 | 103 | 24.0% |
| 4 | 52 | 12.1% |
| 5 | 32 | 7.4% |
| 6 | 9 | 2.1% |
| 7 | 3 | 0.7% |
| 8 | 2 | 0.5% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-23 | 6-2 | 8 |
| 2026-2027 | 2026-09-14 | 5-3 | 8 |
| 2025-2026 | 2025-09-13 | 4-3 | 7 |
| 2025-2026 | 2026-04-05 | 5-2 | 7 |
| 2025-2026 | 2026-04-12 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **322** (draws: **108**)
- Average winning margin: **1.67**

| margin | matches | pct |
|---|---|---|
| 1 | 184 | 57.1% |
| 2 | 83 | 25.8% |
| 3+ | 55 | 17.1% |

## 6. Margin by outcome

### Home wins
- Matches: **170** | avg margin: **1.74** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 97 | 57.1% |
| 2 | 41 | 24.1% |
| 3+ | 32 | 18.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **152** | avg margin: **1.61** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 87 | 57.2% |
| 2 | 42 | 27.6% |
| 3+ | 23 | 15.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 170 | 1-0 | 45 | 26.5% |
| draw | 108 | 1-1 | 43 | 39.8% |
| away | 152 | 0-1 | 42 | 27.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy1\charts\scoreline_analysis_total_goals.png)

