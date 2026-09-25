# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:50:05+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super Lig (Turkey)
- Scope: league `turkey1`

## 1. Scoreline frequency
- Matches analysed: **360** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 13.1% |
| 1-0 | 37 | 10.3% |
| 2-1 | 33 | 9.2% |
| 0-0 | 30 | 8.3% |
| 1-2 | 28 | 7.8% |
| 3-0 | 19 | 5.3% |
| 0-1 | 19 | 5.3% |
| 2-0 | 19 | 5.3% |
| 2-2 | 19 | 5.3% |
| 0-2 | 16 | 4.4% |
| 3-1 | 13 | 3.6% |
| 3-2 | 11 | 3.1% |
| 0-3 | 10 | 2.8% |
| 1-3 | 9 | 2.5% |
| 2-3 | 8 | 2.2% |
| 4-0 | 8 | 2.2% |
| 0-4 | 6 | 1.7% |
| 4-2 | 4 | 1.1% |
| 3-3 | 4 | 1.1% |
| 1-4 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 43 | 14.1% |
| 1-0 | 30 | 9.8% |
| 2-1 | 29 | 9.5% |
| 0-0 | 28 | 9.2% |
| 1-2 | 23 | 7.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 7 | 13.0% |
| 0-1 | 5 | 9.3% |
| 1-2 | 5 | 9.3% |
| 2-2 | 4 | 7.4% |
| 1-1 | 4 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 30 | 8.3% |
| 1 | 56 | 15.6% |
| 2 | 82 | 22.8% |
| 3 | 90 | 25.0% |
| 4 | 55 | 15.3% |
| 5 | 28 | 7.8% |
| 6 | 12 | 3.3% |
| 7 | 5 | 1.4% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-31 | 6-2 | 8 |
| 2026-2027 | 2026-09-20 | 8-0 | 8 |
| 2025-2026 | 2025-09-27 | 3-4 | 7 |
| 2025-2026 | 2025-10-03 | 2-5 | 7 |
| 2025-2026 | 2025-11-23 | 2-5 | 7 |
| 2025-2026 | 2025-11-24 | 3-4 | 7 |
| 2025-2026 | 2025-12-22 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **260** (draws: **100**)
- Average winning margin: **1.8**

| margin | matches | pct |
|---|---|---|
| 1 | 139 | 53.5% |
| 2 | 62 | 23.8% |
| 3+ | 59 | 22.7% |

## 6. Margin by outcome

### Home wins
- Matches: **155** | avg margin: **1.85** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 82 | 52.9% |
| 2 | 36 | 23.2% |
| 3+ | 37 | 23.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **105** | avg margin: **1.73** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 57 | 54.3% |
| 2 | 26 | 24.8% |
| 3+ | 22 | 21.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 155 | 1-0 | 37 | 23.9% |
| draw | 100 | 1-1 | 47 | 47.0% |
| away | 105 | 1-2 | 28 | 26.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\turkey1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\turkey1\charts\scoreline_analysis_total_goals.png)

