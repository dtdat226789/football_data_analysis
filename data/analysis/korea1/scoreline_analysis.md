# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:00:12+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Scoreline frequency
- Matches analysed: **378** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 54 | 14.3% |
| 0-1 | 38 | 10.1% |
| 0-0 | 37 | 9.8% |
| 1-0 | 33 | 8.7% |
| 2-1 | 32 | 8.5% |
| 1-2 | 32 | 8.5% |
| 2-0 | 22 | 5.8% |
| 2-2 | 21 | 5.6% |
| 3-2 | 16 | 4.2% |
| 3-1 | 14 | 3.7% |
| 0-2 | 14 | 3.7% |
| 2-3 | 12 | 3.2% |
| 1-3 | 12 | 3.2% |
| 3-0 | 10 | 2.6% |
| 0-3 | 8 | 2.1% |
| 4-0 | 3 | 0.8% |
| 0-4 | 2 | 0.5% |
| 4-1 | 2 | 0.5% |
| 4-2 | 2 | 0.5% |
| 1-4 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 25 | 12.6% |
| 0-1 | 20 | 10.1% |
| 2-1 | 19 | 9.6% |
| 1-0 | 19 | 9.6% |
| 0-0 | 16 | 8.1% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 29 | 16.1% |
| 0-0 | 21 | 11.7% |
| 0-1 | 18 | 10.0% |
| 1-2 | 16 | 8.9% |
| 1-0 | 14 | 7.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 37 | 9.8% |
| 1 | 71 | 18.8% |
| 2 | 90 | 23.8% |
| 3 | 82 | 21.7% |
| 4 | 52 | 13.8% |
| 5 | 35 | 9.3% |
| 6 | 6 | 1.6% |
| 7 | 4 | 1.1% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-08-17 | 6-2 | 8 |
| 2025 | 2025-09-28 | 3-4 | 7 |
| 2026 | 2026-04-26 | 2-5 | 7 |
| 2026 | 2026-08-22 | 0-7 | 7 |
| 2026 | 2026-08-30 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **265** (draws: **113**)
- Average winning margin: **1.58**

| margin | matches | pct |
|---|---|---|
| 1 | 164 | 61.9% |
| 2 | 65 | 24.5% |
| 3+ | 36 | 13.6% |

## 6. Margin by outcome

### Home wins
- Matches: **137** | avg margin: **1.59** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 81 | 59.1% |
| 2 | 38 | 27.7% |
| 3+ | 18 | 13.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **128** | avg margin: **1.58** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 83 | 64.8% |
| 2 | 27 | 21.1% |
| 3+ | 18 | 14.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 137 | 1-0 | 33 | 24.1% |
| draw | 113 | 1-1 | 54 | 47.8% |
| away | 128 | 0-1 | 38 | 29.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\korea1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\korea1\charts\scoreline_analysis_total_goals.png)

