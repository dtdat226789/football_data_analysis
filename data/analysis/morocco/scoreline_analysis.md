# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:38+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Botola Pro (Morocco)
- Scope: league `morocco`

## 1. Scoreline frequency
- Matches analysed: **488** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 81 | 16.6% |
| 1-0 | 62 | 12.7% |
| 0-0 | 51 | 10.5% |
| 2-1 | 50 | 10.2% |
| 2-0 | 42 | 8.6% |
| 1-2 | 38 | 7.8% |
| 0-1 | 36 | 7.4% |
| 0-2 | 22 | 4.5% |
| 2-2 | 19 | 3.9% |
| 3-0 | 16 | 3.3% |
| 1-3 | 13 | 2.7% |
| 0-3 | 10 | 2.0% |
| 3-1 | 9 | 1.8% |
| 3-2 | 8 | 1.6% |
| 0-4 | 5 | 1.0% |
| 4-0 | 4 | 0.8% |
| 2-3 | 4 | 0.8% |
| 0-5 | 3 | 0.6% |
| 4-2 | 3 | 0.6% |
| 4-1 | 2 | 0.4% |

## 2. Scoreline frequency per season

### 2024-2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 35 | 14.6% |
| 1-0 | 30 | 12.5% |
| 2-0 | 23 | 9.6% |
| 2-1 | 23 | 9.6% |
| 0-0 | 22 | 9.2% |

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 46 | 18.5% |
| 1-0 | 32 | 12.9% |
| 0-0 | 29 | 11.7% |
| 2-1 | 27 | 10.9% |
| 1-2 | 26 | 10.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 51 | 10.5% |
| 1 | 98 | 20.1% |
| 2 | 145 | 29.7% |
| 3 | 114 | 23.4% |
| 4 | 50 | 10.2% |
| 5 | 19 | 3.9% |
| 6 | 8 | 1.6% |
| 7 | 3 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-03-08 | 3-4 | 7 |
| 2025-2026 | 2026-05-07 | 4-3 | 7 |
| 2025-2026 | 2026-06-17 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **335** (draws: **153**)
- Average winning margin: **1.59**

| margin | matches | pct |
|---|---|---|
| 1 | 201 | 60.0% |
| 2 | 89 | 26.6% |
| 3+ | 45 | 13.4% |

## 6. Margin by outcome

### Home wins
- Matches: **198** | avg margin: **1.53** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 121 | 61.1% |
| 2 | 54 | 27.3% |
| 3+ | 23 | 11.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **137** | avg margin: **1.69** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 80 | 58.4% |
| 2 | 35 | 25.5% |
| 3+ | 22 | 16.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 198 | 1-0 | 62 | 31.3% |
| draw | 153 | 1-1 | 81 | 52.9% |
| away | 137 | 1-2 | 38 | 27.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\morocco\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\morocco\charts\scoreline_analysis_total_goals.png)

