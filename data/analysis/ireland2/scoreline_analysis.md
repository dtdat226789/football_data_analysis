# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:56:10+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Scoreline frequency
- Matches analysed: **344** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 41 | 11.9% |
| 1-1 | 36 | 10.5% |
| 0-1 | 34 | 9.9% |
| 1-0 | 29 | 8.4% |
| 2-0 | 25 | 7.3% |
| 2-2 | 23 | 6.7% |
| 1-2 | 20 | 5.8% |
| 0-0 | 19 | 5.5% |
| 3-1 | 18 | 5.2% |
| 0-2 | 15 | 4.4% |
| 3-2 | 12 | 3.5% |
| 3-0 | 9 | 2.6% |
| 4-0 | 9 | 2.6% |
| 0-3 | 9 | 2.6% |
| 1-3 | 7 | 2.0% |
| 2-3 | 4 | 1.2% |
| 5-0 | 4 | 1.2% |
| 4-2 | 4 | 1.2% |
| 5-1 | 4 | 1.2% |
| 4-1 | 4 | 1.2% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 21 | 11.7% |
| 0-1 | 19 | 10.6% |
| 2-1 | 16 | 8.9% |
| 1-0 | 13 | 7.3% |
| 3-1 | 12 | 6.7% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 25 | 15.2% |
| 1-0 | 16 | 9.7% |
| 1-1 | 15 | 9.1% |
| 0-1 | 15 | 9.1% |
| 2-0 | 15 | 9.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.5% |
| 1 | 63 | 18.3% |
| 2 | 76 | 22.1% |
| 3 | 79 | 23.0% |
| 4 | 60 | 17.4% |
| 5 | 27 | 7.8% |
| 6 | 11 | 3.2% |
| 7 | 8 | 2.3% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-08-28 | 5-4 | 9 |
| 2025 | 2025-06-27 | 4-3 | 7 |
| 2025 | 2025-08-08 | 6-1 | 7 |
| 2025 | 2025-08-22 | 0-7 | 7 |
| 2025 | 2025-10-17 | 3-4 | 7 |
| 2026 | 2026-05-15 | 3-4 | 7 |
| 2026 | 2026-06-19 | 5-2 | 7 |
| 2026 | 2026-07-10 | 3-4 | 7 |
| 2026 | 2026-07-24 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **264** (draws: **80**)
- Average winning margin: **1.78**

| margin | matches | pct |
|---|---|---|
| 1 | 145 | 54.9% |
| 2 | 69 | 26.1% |
| 3+ | 50 | 18.9% |

## 6. Margin by outcome

### Home wins
- Matches: **165** | avg margin: **1.85** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 84 | 50.9% |
| 2 | 47 | 28.5% |
| 3+ | 34 | 20.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **99** | avg margin: **1.66** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 61.6% |
| 2 | 22 | 22.2% |
| 3+ | 16 | 16.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 165 | 2-1 | 41 | 24.8% |
| draw | 80 | 1-1 | 36 | 45.0% |
| away | 99 | 0-1 | 34 | 34.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\ireland2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\ireland2\charts\scoreline_analysis_total_goals.png)

