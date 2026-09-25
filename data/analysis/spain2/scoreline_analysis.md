# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:48:17+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Scoreline frequency
- Matches analysed: **575** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 72 | 12.5% |
| 1-0 | 62 | 10.8% |
| 2-1 | 59 | 10.3% |
| 0-1 | 53 | 9.2% |
| 0-0 | 47 | 8.2% |
| 1-2 | 45 | 7.8% |
| 2-0 | 33 | 5.7% |
| 1-3 | 26 | 4.5% |
| 0-2 | 23 | 4.0% |
| 3-1 | 22 | 3.8% |
| 3-0 | 21 | 3.7% |
| 2-2 | 19 | 3.3% |
| 3-2 | 18 | 3.1% |
| 2-3 | 10 | 1.7% |
| 4-1 | 8 | 1.4% |
| 0-3 | 8 | 1.4% |
| 4-2 | 7 | 1.2% |
| 5-1 | 6 | 1.0% |
| 4-0 | 6 | 1.0% |
| 0-4 | 5 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 67 | 13.2% |
| 2-1 | 57 | 11.2% |
| 1-0 | 56 | 11.0% |
| 0-1 | 45 | 8.8% |
| 0-0 | 40 | 7.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 8 | 12.1% |
| 0-0 | 7 | 10.6% |
| 1-2 | 7 | 10.6% |
| 2-0 | 6 | 9.1% |
| 1-0 | 6 | 9.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 47 | 8.2% |
| 1 | 115 | 20.0% |
| 2 | 128 | 22.3% |
| 3 | 133 | 23.1% |
| 4 | 78 | 13.6% |
| 5 | 42 | 7.3% |
| 6 | 23 | 4.0% |
| 7 | 5 | 0.9% |
| 8 | 3 | 0.5% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-15 | 5-4 | 9 |
| 2025-2026 | 2025-08-18 | 4-4 | 8 |
| 2025-2026 | 2026-03-15 | 5-3 | 8 |
| 2025-2026 | 2026-04-05 | 6-2 | 8 |
| 2025-2026 | 2025-09-28 | 3-4 | 7 |
| 2025-2026 | 2025-10-04 | 5-2 | 7 |
| 2025-2026 | 2026-03-08 | 4-3 | 7 |
| 2025-2026 | 2026-03-21 | 5-2 | 7 |
| 2026-2027 | 2026-08-29 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **432** (draws: **143**)
- Average winning margin: **1.63**

| margin | matches | pct |
|---|---|---|
| 1 | 250 | 57.9% |
| 2 | 116 | 26.9% |
| 3+ | 66 | 15.3% |

## 6. Margin by outcome

### Home wins
- Matches: **250** | avg margin: **1.68** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 141 | 56.4% |
| 2 | 63 | 25.2% |
| 3+ | 46 | 18.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **182** | avg margin: **1.56** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 109 | 59.9% |
| 2 | 53 | 29.1% |
| 3+ | 20 | 11.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 250 | 1-0 | 62 | 24.8% |
| draw | 143 | 1-1 | 72 | 50.3% |
| away | 182 | 0-1 | 53 | 29.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\spain2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\spain2\charts\scoreline_analysis_total_goals.png)

