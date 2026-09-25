# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:01:08+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: NB II. (Hungary)
- Scope: league `hungary2`

## 1. Scoreline frequency
- Matches analysed: **301** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 39 | 13.0% |
| 1-0 | 35 | 11.6% |
| 2-1 | 32 | 10.6% |
| 0-1 | 27 | 9.0% |
| 2-0 | 24 | 8.0% |
| 0-2 | 19 | 6.3% |
| 1-2 | 18 | 6.0% |
| 0-0 | 17 | 5.6% |
| 2-2 | 16 | 5.3% |
| 0-3 | 11 | 3.7% |
| 3-1 | 11 | 3.7% |
| 3-0 | 8 | 2.7% |
| 3-2 | 7 | 2.3% |
| 4-0 | 5 | 1.7% |
| 1-4 | 5 | 1.7% |
| 0-4 | 3 | 1.0% |
| 1-3 | 3 | 1.0% |
| 4-1 | 3 | 1.0% |
| 4-3 | 2 | 0.7% |
| 1-5 | 2 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 33 | 13.8% |
| 1-0 | 27 | 11.2% |
| 2-1 | 26 | 10.8% |
| 0-1 | 22 | 9.2% |
| 2-0 | 18 | 7.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 8 | 13.1% |
| 1-1 | 6 | 9.8% |
| 2-1 | 6 | 9.8% |
| 2-0 | 6 | 9.8% |
| 0-1 | 5 | 8.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 17 | 5.6% |
| 1 | 62 | 20.6% |
| 2 | 82 | 27.2% |
| 3 | 69 | 22.9% |
| 4 | 38 | 12.6% |
| 5 | 17 | 5.6% |
| 6 | 9 | 3.0% |
| 7 | 6 | 2.0% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-01 | 5-3 | 8 |
| 2025-2026 | 2025-08-11 | 4-3 | 7 |
| 2025-2026 | 2025-09-22 | 4-3 | 7 |
| 2025-2026 | 2025-09-29 | 5-2 | 7 |
| 2025-2026 | 2025-10-05 | 3-4 | 7 |
| 2025-2026 | 2025-10-26 | 5-2 | 7 |
| 2025-2026 | 2026-03-22 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **227** (draws: **74**)
- Average winning margin: **1.74**

| margin | matches | pct |
|---|---|---|
| 1 | 123 | 54.2% |
| 2 | 60 | 26.4% |
| 3+ | 44 | 19.4% |

## 6. Margin by outcome

### Home wins
- Matches: **137** | avg margin: **1.73** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 76 | 55.5% |
| 2 | 38 | 27.7% |
| 3+ | 23 | 16.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **90** | avg margin: **1.77** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 47 | 52.2% |
| 2 | 22 | 24.4% |
| 3+ | 21 | 23.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 137 | 1-0 | 35 | 25.5% |
| draw | 74 | 1-1 | 39 | 52.7% |
| away | 90 | 0-1 | 27 | 30.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\hungary2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\hungary2\charts\scoreline_analysis_total_goals.png)

