# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:09:52+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League (Switzerland)
- Scope: league `swiss1`

## 1. Scoreline frequency
- Matches analysed: **284** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 29 | 10.2% |
| 2-1 | 28 | 9.9% |
| 1-2 | 28 | 9.9% |
| 2-2 | 17 | 6.0% |
| 0-1 | 17 | 6.0% |
| 1-3 | 15 | 5.3% |
| 1-0 | 13 | 4.6% |
| 3-0 | 13 | 4.6% |
| 3-1 | 12 | 4.2% |
| 0-0 | 11 | 3.9% |
| 0-2 | 9 | 3.2% |
| 3-3 | 9 | 3.2% |
| 2-0 | 9 | 3.2% |
| 4-2 | 8 | 2.8% |
| 2-3 | 7 | 2.5% |
| 3-2 | 7 | 2.5% |
| 5-0 | 6 | 2.1% |
| 1-4 | 5 | 1.8% |
| 4-1 | 5 | 1.8% |
| 2-4 | 5 | 1.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 26 | 11.3% |
| 1-2 | 24 | 10.4% |
| 2-1 | 22 | 9.6% |
| 2-2 | 13 | 5.7% |
| 0-1 | 13 | 5.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 6 | 11.1% |
| 0-1 | 4 | 7.4% |
| 2-2 | 4 | 7.4% |
| 1-2 | 4 | 7.4% |
| 1-1 | 3 | 5.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 11 | 3.9% |
| 1 | 30 | 10.6% |
| 2 | 47 | 16.5% |
| 3 | 74 | 26.1% |
| 4 | 52 | 18.3% |
| 5 | 30 | 10.6% |
| 6 | 29 | 10.2% |
| 7 | 7 | 2.5% |
| 8 | 3 | 1.1% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.4% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-05-14 | 3-8 | 11 |
| 2025-2026 | 2025-11-30 | 4-4 | 8 |
| 2025-2026 | 2025-12-17 | 2-6 | 8 |
| 2025-2026 | 2026-04-26 | 5-3 | 8 |
| 2025-2026 | 2026-01-17 | 2-5 | 7 |
| 2025-2026 | 2026-01-25 | 3-4 | 7 |
| 2025-2026 | 2026-02-10 | 4-3 | 7 |
| 2025-2026 | 2026-02-14 | 6-1 | 7 |
| 2026-2027 | 2026-08-30 | 5-2 | 7 |
| 2026-2027 | 2026-08-30 | 3-4 | 7 |
| 2026-2027 | 2026-09-15 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **217** (draws: **67**)
- Average winning margin: **1.94**

| margin | matches | pct |
|---|---|---|
| 1 | 103 | 47.5% |
| 2 | 59 | 27.2% |
| 3+ | 55 | 25.3% |

## 6. Margin by outcome

### Home wins
- Matches: **114** | avg margin: **2.1** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 49 | 43.0% |
| 2 | 30 | 26.3% |
| 3+ | 35 | 30.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **103** | avg margin: **1.78** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 54 | 52.4% |
| 2 | 29 | 28.2% |
| 3+ | 20 | 19.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 114 | 2-1 | 28 | 24.6% |
| draw | 67 | 1-1 | 29 | 43.3% |
| away | 103 | 1-2 | 28 | 27.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\swiss1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\swiss1\charts\scoreline_analysis_total_goals.png)

