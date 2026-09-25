# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:00:26+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Eredivisie (Netherlands)
- Scope: league `holland1`

## 1. Scoreline frequency
- Matches analysed: **384** across **2** seasons.
- Distinct scorelines seen: **35**.

| scoreline | count | pct |
|---|---|---|
| 2-2 | 41 | 10.7% |
| 1-1 | 40 | 10.4% |
| 2-1 | 35 | 9.1% |
| 1-2 | 29 | 7.6% |
| 2-0 | 26 | 6.8% |
| 0-2 | 23 | 6.0% |
| 1-0 | 21 | 5.5% |
| 0-1 | 17 | 4.4% |
| 3-0 | 16 | 4.2% |
| 3-1 | 15 | 3.9% |
| 2-3 | 13 | 3.4% |
| 4-1 | 11 | 2.9% |
| 1-3 | 11 | 2.9% |
| 0-0 | 11 | 2.9% |
| 1-4 | 8 | 2.1% |
| 3-2 | 8 | 2.1% |
| 3-3 | 8 | 2.1% |
| 4-0 | 6 | 1.6% |
| 5-0 | 5 | 1.3% |
| 0-3 | 5 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 11.2% |
| 2-1 | 33 | 10.3% |
| 2-2 | 31 | 9.7% |
| 1-2 | 26 | 8.1% |
| 2-0 | 24 | 7.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 10 | 15.9% |
| 1-3 | 4 | 6.3% |
| 1-4 | 4 | 6.3% |
| 1-1 | 4 | 6.3% |
| 0-4 | 3 | 4.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 11 | 2.9% |
| 1 | 38 | 9.9% |
| 2 | 89 | 23.2% |
| 3 | 85 | 22.1% |
| 4 | 78 | 20.3% |
| 5 | 45 | 11.7% |
| 6 | 22 | 5.7% |
| 7 | 14 | 3.6% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **16**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-02 | 8-2 | 10 |
| 2025-2026 | 2025-09-13 | 3-5 | 8 |
| 2025-2026 | 2025-08-09 | 6-1 | 7 |
| 2025-2026 | 2025-10-19 | 0-7 | 7 |
| 2025-2026 | 2025-10-31 | 5-2 | 7 |
| 2025-2026 | 2025-12-06 | 6-1 | 7 |
| 2025-2026 | 2025-12-13 | 4-3 | 7 |
| 2025-2026 | 2025-12-21 | 4-3 | 7 |
| 2025-2026 | 2026-01-17 | 3-4 | 7 |
| 2025-2026 | 2026-01-18 | 3-4 | 7 |
| 2025-2026 | 2026-04-04 | 4-3 | 7 |
| 2025-2026 | 2026-04-23 | 6-1 | 7 |
| 2026-2027 | 2026-08-23 | 2-5 | 7 |
| 2026-2027 | 2026-08-29 | 5-2 | 7 |
| 2026-2027 | 2026-08-30 | 1-6 | 7 |
| 2026-2027 | 2026-09-13 | 0-7 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **284** (draws: **100**)
- Average winning margin: **1.99**

| margin | matches | pct |
|---|---|---|
| 1 | 128 | 45.1% |
| 2 | 82 | 28.9% |
| 3+ | 74 | 26.1% |

## 6. Margin by outcome

### Home wins
- Matches: **162** | avg margin: **2.09** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 41.4% |
| 2 | 46 | 28.4% |
| 3+ | 49 | 30.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **122** | avg margin: **1.85** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 50.0% |
| 2 | 36 | 29.5% |
| 3+ | 25 | 20.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 162 | 2-1 | 35 | 21.6% |
| draw | 100 | 2-2 | 41 | 41.0% |
| away | 122 | 1-2 | 29 | 23.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\holland1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\holland1\charts\scoreline_analysis_total_goals.png)

