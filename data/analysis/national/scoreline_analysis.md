# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:02:05+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Scoreline frequency
- Matches analysed: **677** across **2** seasons.
- Distinct scorelines seen: **38**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 77 | 11.4% |
| 1-0 | 65 | 9.6% |
| 2-1 | 65 | 9.6% |
| 1-2 | 56 | 8.3% |
| 0-2 | 40 | 5.9% |
| 0-1 | 40 | 5.9% |
| 2-0 | 35 | 5.2% |
| 2-2 | 32 | 4.7% |
| 0-0 | 29 | 4.3% |
| 3-2 | 25 | 3.7% |
| 3-0 | 25 | 3.7% |
| 0-3 | 25 | 3.7% |
| 1-3 | 24 | 3.5% |
| 3-1 | 23 | 3.4% |
| 2-3 | 19 | 2.8% |
| 4-0 | 16 | 2.4% |
| 4-1 | 14 | 2.1% |
| 3-3 | 10 | 1.5% |
| 4-2 | 9 | 1.3% |
| 5-1 | 9 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 64 | 11.5% |
| 2-1 | 54 | 9.7% |
| 1-0 | 50 | 9.0% |
| 1-2 | 47 | 8.4% |
| 0-2 | 36 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 15 | 12.5% |
| 1-1 | 13 | 10.8% |
| 2-1 | 11 | 9.2% |
| 1-3 | 9 | 7.5% |
| 1-2 | 9 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 4.3% |
| 1 | 105 | 15.5% |
| 2 | 152 | 22.5% |
| 3 | 171 | 25.3% |
| 4 | 97 | 14.3% |
| 5 | 72 | 10.6% |
| 6 | 34 | 5.0% |
| 7 | 10 | 1.5% |
| 8 | 6 | 0.9% |
| 9 | 1 | 0.1% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **17**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-14 | 3-6 | 9 |
| 2025-2026 | 2025-09-13 | 4-4 | 8 |
| 2025-2026 | 2025-12-26 | 7-1 | 8 |
| 2025-2026 | 2026-02-25 | 4-4 | 8 |
| 2025-2026 | 2026-03-07 | 5-3 | 8 |
| 2025-2026 | 2026-03-21 | 6-2 | 8 |
| 2025-2026 | 2026-04-18 | 2-6 | 8 |
| 2025-2026 | 2025-08-25 | 3-4 | 7 |
| 2025-2026 | 2025-09-03 | 3-4 | 7 |
| 2025-2026 | 2025-09-20 | 4-3 | 7 |
| 2025-2026 | 2025-09-30 | 2-5 | 7 |
| 2025-2026 | 2026-02-21 | 3-4 | 7 |
| 2025-2026 | 2026-03-31 | 7-0 | 7 |
| 2025-2026 | 2026-04-21 | 4-3 | 7 |
| 2026-2027 | 2026-08-08 | 5-2 | 7 |
| 2026-2027 | 2026-09-19 | 1-6 | 7 |
| 2026-2027 | 2026-09-26 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **527** (draws: **150**)
- Average winning margin: **1.8**

| margin | matches | pct |
|---|---|---|
| 1 | 275 | 52.2% |
| 2 | 136 | 25.8% |
| 3+ | 116 | 22.0% |

## 6. Margin by outcome

### Home wins
- Matches: **299** | avg margin: **1.87** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 157 | 52.5% |
| 2 | 68 | 22.7% |
| 3+ | 74 | 24.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **228** | avg margin: **1.71** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 118 | 51.8% |
| 2 | 68 | 29.8% |
| 3+ | 42 | 18.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 299 | 1-0 | 65 | 21.7% |
| draw | 150 | 1-1 | 77 | 51.3% |
| away | 228 | 1-2 | 56 | 24.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\national\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\national\charts\scoreline_analysis_total_goals.png)

