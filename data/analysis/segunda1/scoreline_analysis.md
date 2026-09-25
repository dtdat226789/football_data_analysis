# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:45:30+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Scoreline frequency
- Matches analysed: **333** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 44 | 13.2% |
| 1-1 | 39 | 11.7% |
| 1-2 | 30 | 9.0% |
| 0-0 | 29 | 8.7% |
| 0-1 | 28 | 8.4% |
| 2-1 | 28 | 8.4% |
| 0-2 | 18 | 5.4% |
| 3-0 | 17 | 5.1% |
| 2-2 | 16 | 4.8% |
| 3-1 | 14 | 4.2% |
| 2-0 | 13 | 3.9% |
| 3-2 | 6 | 1.8% |
| 4-1 | 6 | 1.8% |
| 0-3 | 6 | 1.8% |
| 1-3 | 5 | 1.5% |
| 0-4 | 5 | 1.5% |
| 2-3 | 4 | 1.2% |
| 3-3 | 4 | 1.2% |
| 3-4 | 4 | 1.2% |
| 4-0 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 42 | 13.7% |
| 1-1 | 38 | 12.4% |
| 1-2 | 29 | 9.5% |
| 0-0 | 28 | 9.2% |
| 0-1 | 26 | 8.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 4 | 14.8% |
| 0-2 | 4 | 14.8% |
| 2-2 | 3 | 11.1% |
| 0-1 | 2 | 7.4% |
| 0-3 | 2 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.7% |
| 1 | 72 | 21.6% |
| 2 | 70 | 21.0% |
| 3 | 81 | 24.3% |
| 4 | 43 | 12.9% |
| 5 | 20 | 6.0% |
| 6 | 9 | 2.7% |
| 7 | 7 | 2.1% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-07 | 7-2 | 9 |
| 2025-2026 | 2026-03-21 | 4-4 | 8 |
| 2025-2026 | 2025-10-05 | 5-2 | 7 |
| 2025-2026 | 2026-02-08 | 7-0 | 7 |
| 2025-2026 | 2026-02-15 | 3-4 | 7 |
| 2025-2026 | 2026-03-01 | 5-2 | 7 |
| 2025-2026 | 2026-04-04 | 3-4 | 7 |
| 2025-2026 | 2026-04-05 | 3-4 | 7 |
| 2025-2026 | 2026-05-03 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **244** (draws: **89**)
- Average winning margin: **1.68**

| margin | matches | pct |
|---|---|---|
| 1 | 144 | 59.0% |
| 2 | 53 | 21.7% |
| 3+ | 47 | 19.3% |

## 6. Margin by outcome

### Home wins
- Matches: **139** | avg margin: **1.75** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 78 | 56.1% |
| 2 | 29 | 20.9% |
| 3+ | 32 | 23.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **105** | avg margin: **1.6** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 66 | 62.9% |
| 2 | 24 | 22.9% |
| 3+ | 15 | 14.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 139 | 1-0 | 44 | 31.7% |
| draw | 89 | 1-1 | 39 | 43.8% |
| away | 105 | 1-2 | 30 | 28.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda1\charts\scoreline_analysis_total_goals.png)

