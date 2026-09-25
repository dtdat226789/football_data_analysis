# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:49:48+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Thai League 1 (Thailand)
- Scope: league `thai1`

## 1. Scoreline frequency
- Matches analysed: **264** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 46 | 17.4% |
| 1-0 | 26 | 9.8% |
| 2-1 | 23 | 8.7% |
| 0-1 | 21 | 8.0% |
| 2-0 | 20 | 7.6% |
| 0-0 | 18 | 6.8% |
| 1-2 | 17 | 6.4% |
| 2-2 | 13 | 4.9% |
| 3-1 | 10 | 3.8% |
| 3-0 | 10 | 3.8% |
| 0-2 | 8 | 3.0% |
| 1-3 | 8 | 3.0% |
| 1-4 | 7 | 2.7% |
| 3-2 | 6 | 2.3% |
| 2-3 | 5 | 1.9% |
| 4-1 | 4 | 1.5% |
| 4-0 | 3 | 1.1% |
| 5-0 | 3 | 1.1% |
| 0-3 | 2 | 0.8% |
| 3-3 | 1 | 0.4% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 43 | 17.9% |
| 1-0 | 22 | 9.2% |
| 2-1 | 20 | 8.3% |
| 2-0 | 20 | 8.3% |
| 0-1 | 18 | 7.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 4 | 16.7% |
| 1-2 | 3 | 12.5% |
| 2-1 | 3 | 12.5% |
| 1-1 | 3 | 12.5% |
| 0-1 | 3 | 12.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 18 | 6.8% |
| 1 | 47 | 17.8% |
| 2 | 74 | 28.0% |
| 3 | 52 | 19.7% |
| 4 | 35 | 13.3% |
| 5 | 26 | 9.8% |
| 6 | 5 | 1.9% |
| 7 | 4 | 1.5% |
| 8 | 2 | 0.8% |
| 9 | 1 | 0.4% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-18 | 8-1 | 9 |
| 2025-2026 | 2025-10-04 | 8-0 | 8 |
| 2025-2026 | 2025-12-06 | 4-4 | 8 |
| 2025-2026 | 2025-10-26 | 4-3 | 7 |
| 2025-2026 | 2025-11-29 | 7-0 | 7 |
| 2025-2026 | 2026-01-18 | 5-2 | 7 |
| 2025-2026 | 2026-05-03 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **185** (draws: **79**)
- Average winning margin: **1.84**

| margin | matches | pct |
|---|---|---|
| 1 | 99 | 53.5% |
| 2 | 48 | 25.9% |
| 3+ | 38 | 20.5% |

## 6. Margin by outcome

### Home wins
- Matches: **114** | avg margin: **1.99** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 49.1% |
| 2 | 31 | 27.2% |
| 3+ | 27 | 23.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **71** | avg margin: **1.59** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 43 | 60.6% |
| 2 | 17 | 23.9% |
| 3+ | 11 | 15.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 114 | 1-0 | 26 | 22.8% |
| draw | 79 | 1-1 | 46 | 58.2% |
| away | 71 | 0-1 | 21 | 29.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\thai1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\thai1\charts\scoreline_analysis_total_goals.png)

