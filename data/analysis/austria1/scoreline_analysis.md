# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:44:12+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Bundesliga (Austria)
- Scope: league `austria1`

## 1. Scoreline frequency
- Matches analysed: **237** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 29 | 12.2% |
| 1-0 | 26 | 11.0% |
| 2-1 | 23 | 9.7% |
| 0-2 | 18 | 7.6% |
| 2-2 | 15 | 6.3% |
| 2-0 | 14 | 5.9% |
| 1-2 | 13 | 5.5% |
| 3-1 | 13 | 5.5% |
| 0-0 | 13 | 5.5% |
| 3-0 | 13 | 5.5% |
| 1-3 | 11 | 4.6% |
| 0-1 | 10 | 4.2% |
| 0-3 | 7 | 3.0% |
| 4-1 | 6 | 2.5% |
| 2-3 | 5 | 2.1% |
| 3-2 | 4 | 1.7% |
| 1-5 | 3 | 1.3% |
| 4-2 | 2 | 0.8% |
| 5-0 | 2 | 0.8% |
| 3-3 | 2 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 24 | 12.3% |
| 1-0 | 22 | 11.3% |
| 2-1 | 19 | 9.7% |
| 0-2 | 15 | 7.7% |
| 2-2 | 13 | 6.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 3-0 | 5 | 11.9% |
| 1-1 | 5 | 11.9% |
| 1-0 | 4 | 9.5% |
| 2-1 | 4 | 9.5% |
| 0-2 | 3 | 7.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 13 | 5.5% |
| 1 | 36 | 15.2% |
| 2 | 61 | 25.7% |
| 3 | 56 | 23.6% |
| 4 | 41 | 17.3% |
| 5 | 18 | 7.6% |
| 6 | 9 | 3.8% |
| 7 | 2 | 0.8% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-16 | 8-0 | 8 |
| 2025-2026 | 2025-10-19 | 3-4 | 7 |
| 2025-2026 | 2026-03-15 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **178** (draws: **59**)
- Average winning margin: **1.83**

| margin | matches | pct |
|---|---|---|
| 1 | 82 | 46.1% |
| 2 | 59 | 33.1% |
| 3+ | 37 | 20.8% |

## 6. Margin by outcome

### Home wins
- Matches: **106** | avg margin: **1.83** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 50.0% |
| 2 | 29 | 27.4% |
| 3+ | 24 | 22.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **72** | avg margin: **1.83** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 29 | 40.3% |
| 2 | 30 | 41.7% |
| 3+ | 13 | 18.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 106 | 1-0 | 26 | 24.5% |
| draw | 59 | 1-1 | 29 | 49.2% |
| away | 72 | 0-2 | 18 | 25.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\austria1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\austria1\charts\scoreline_analysis_total_goals.png)

