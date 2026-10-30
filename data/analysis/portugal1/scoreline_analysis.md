# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-10-30T04:05:05+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Scoreline frequency
- Matches analysed: **389** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 0-1 | 38 | 9.8% |
| 1-1 | 36 | 9.3% |
| 1-0 | 36 | 9.3% |
| 2-2 | 35 | 9.0% |
| 1-2 | 34 | 8.7% |
| 2-1 | 25 | 6.4% |
| 2-0 | 25 | 6.4% |
| 0-0 | 25 | 6.4% |
| 0-2 | 19 | 4.9% |
| 3-1 | 19 | 4.9% |
| 3-0 | 19 | 4.9% |
| 4-0 | 11 | 2.8% |
| 0-3 | 10 | 2.6% |
| 0-4 | 10 | 2.6% |
| 3-2 | 9 | 2.3% |
| 1-3 | 7 | 1.8% |
| 1-4 | 6 | 1.5% |
| 3-3 | 6 | 1.5% |
| 5-0 | 5 | 1.3% |
| 6-0 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 10.1% |
| 0-1 | 30 | 9.7% |
| 2-2 | 27 | 8.8% |
| 1-0 | 27 | 8.8% |
| 1-2 | 26 | 8.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 9 | 11.1% |
| 0-1 | 8 | 9.9% |
| 2-2 | 8 | 9.9% |
| 1-2 | 8 | 9.9% |
| 2-0 | 6 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 25 | 6.4% |
| 1 | 74 | 19.0% |
| 2 | 80 | 20.6% |
| 3 | 88 | 22.6% |
| 4 | 82 | 21.1% |
| 5 | 25 | 6.4% |
| 6 | 12 | 3.1% |
| 7 | 2 | 0.5% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-01 | 3-5 | 8 |
| 2025-2026 | 2025-11-07 | 4-3 | 7 |
| 2026-2027 | 2026-08-17 | 0-7 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **287** (draws: **102**)
- Average winning margin: **1.89**

| margin | matches | pct |
|---|---|---|
| 1 | 145 | 50.5% |
| 2 | 74 | 25.8% |
| 3+ | 68 | 23.7% |

## 6. Margin by outcome

### Home wins
- Matches: **157** | avg margin: **1.98** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 71 | 45.2% |
| 2 | 46 | 29.3% |
| 3+ | 40 | 25.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **130** | avg margin: **1.77** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 74 | 56.9% |
| 2 | 28 | 21.5% |
| 3+ | 28 | 21.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 157 | 1-0 | 36 | 22.9% |
| draw | 102 | 1-1 | 36 | 35.3% |
| away | 130 | 0-1 | 38 | 29.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](charts/scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](charts/scoreline_analysis_total_goals.png)

