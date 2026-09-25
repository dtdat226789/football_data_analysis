# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:01:35+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Scoreline frequency
- Matches analysed: **339** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 39 | 11.5% |
| 1-1 | 36 | 10.6% |
| 0-1 | 34 | 10.0% |
| 1-0 | 28 | 8.3% |
| 2-0 | 25 | 7.4% |
| 2-2 | 23 | 6.8% |
| 1-2 | 20 | 5.9% |
| 0-0 | 19 | 5.6% |
| 3-1 | 18 | 5.3% |
| 0-2 | 15 | 4.4% |
| 3-2 | 12 | 3.5% |
| 3-0 | 9 | 2.7% |
| 4-0 | 9 | 2.7% |
| 0-3 | 9 | 2.7% |
| 1-3 | 6 | 1.8% |
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
| 2-1 | 23 | 14.4% |
| 1-1 | 15 | 9.4% |
| 1-0 | 15 | 9.4% |
| 0-1 | 15 | 9.4% |
| 2-0 | 15 | 9.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.6% |
| 1 | 62 | 18.3% |
| 2 | 76 | 22.4% |
| 3 | 77 | 22.7% |
| 4 | 59 | 17.4% |
| 5 | 27 | 8.0% |
| 6 | 10 | 2.9% |
| 7 | 8 | 2.4% |
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
- Decided matches: **260** (draws: **79**)
- Average winning margin: **1.79**

| margin | matches | pct |
|---|---|---|
| 1 | 142 | 54.6% |
| 2 | 68 | 26.2% |
| 3+ | 50 | 19.2% |

## 6. Margin by outcome

### Home wins
- Matches: **162** | avg margin: **1.87** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 81 | 50.0% |
| 2 | 47 | 29.0% |
| 3+ | 34 | 21.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **98** | avg margin: **1.65** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 61 | 62.2% |
| 2 | 21 | 21.4% |
| 3+ | 16 | 16.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 162 | 2-1 | 39 | 24.1% |
| draw | 79 | 1-1 | 36 | 45.6% |
| away | 98 | 0-1 | 34 | 34.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\ireland2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\ireland2\charts\scoreline_analysis_total_goals.png)

