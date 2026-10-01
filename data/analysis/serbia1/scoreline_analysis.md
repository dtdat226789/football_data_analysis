# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:08:08+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Mozzart Bet Super Liga (Serbia)
- Scope: league `serbia1`

## 1. Scoreline frequency
- Matches analysed: **365** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 0-0 | 42 | 11.5% |
| 1-1 | 40 | 11.0% |
| 1-0 | 39 | 10.7% |
| 2-0 | 31 | 8.5% |
| 2-1 | 29 | 7.9% |
| 1-2 | 25 | 6.8% |
| 0-1 | 19 | 5.2% |
| 2-2 | 19 | 5.2% |
| 1-3 | 16 | 4.4% |
| 3-1 | 12 | 3.3% |
| 0-2 | 12 | 3.3% |
| 3-0 | 11 | 3.0% |
| 4-0 | 10 | 2.7% |
| 2-3 | 9 | 2.5% |
| 3-2 | 8 | 2.2% |
| 1-4 | 6 | 1.6% |
| 5-0 | 6 | 1.6% |
| 0-3 | 5 | 1.4% |
| 4-1 | 5 | 1.4% |
| 2-4 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 0-0 | 36 | 12.1% |
| 1-1 | 33 | 11.1% |
| 1-0 | 32 | 10.8% |
| 2-0 | 24 | 8.1% |
| 2-1 | 22 | 7.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 7 | 10.3% |
| 1-0 | 7 | 10.3% |
| 1-1 | 7 | 10.3% |
| 2-0 | 7 | 10.3% |
| 0-0 | 6 | 8.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 42 | 11.5% |
| 1 | 58 | 15.9% |
| 2 | 83 | 22.7% |
| 3 | 70 | 19.2% |
| 4 | 57 | 15.6% |
| 5 | 35 | 9.6% |
| 6 | 11 | 3.0% |
| 7 | 4 | 1.1% |
| 8 | 4 | 1.1% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-10 | 2-7 | 9 |
| 2025-2026 | 2025-07-26 | 7-1 | 8 |
| 2025-2026 | 2025-09-14 | 7-1 | 8 |
| 2026-2027 | 2026-09-19 | 4-4 | 8 |
| 2026-2027 | 2026-09-19 | 3-5 | 8 |
| 2025-2026 | 2025-09-14 | 2-5 | 7 |
| 2025-2026 | 2025-10-19 | 6-1 | 7 |
| 2025-2026 | 2025-11-30 | 3-4 | 7 |
| 2025-2026 | 2026-05-10 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **261** (draws: **104**)
- Average winning margin: **1.86**

| margin | matches | pct |
|---|---|---|
| 1 | 130 | 49.8% |
| 2 | 77 | 29.5% |
| 3+ | 54 | 20.7% |

## 6. Margin by outcome

### Home wins
- Matches: **159** | avg margin: **1.97** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 76 | 47.8% |
| 2 | 45 | 28.3% |
| 3+ | 38 | 23.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **102** | avg margin: **1.69** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 54 | 52.9% |
| 2 | 32 | 31.4% |
| 3+ | 16 | 15.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 159 | 1-0 | 39 | 24.5% |
| draw | 104 | 0-0 | 42 | 40.4% |
| away | 102 | 1-2 | 25 | 24.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\serbia1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\serbia1\charts\scoreline_analysis_total_goals.png)

