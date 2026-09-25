# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:02:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

## 1. Scoreline frequency
- Matches analysed: **760** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 89 | 11.7% |
| 1-1 | 79 | 10.4% |
| 0-1 | 77 | 10.1% |
| 1-2 | 76 | 10.0% |
| 0-0 | 75 | 9.9% |
| 2-1 | 58 | 7.6% |
| 2-0 | 50 | 6.6% |
| 2-2 | 38 | 5.0% |
| 0-2 | 36 | 4.7% |
| 3-0 | 22 | 2.9% |
| 1-3 | 22 | 2.9% |
| 3-1 | 22 | 2.9% |
| 2-3 | 20 | 2.6% |
| 3-2 | 15 | 2.0% |
| 4-1 | 13 | 1.7% |
| 4-0 | 11 | 1.4% |
| 0-3 | 10 | 1.3% |
| 0-4 | 7 | 0.9% |
| 4-2 | 5 | 0.7% |
| 3-4 | 5 | 0.7% |

## 2. Scoreline frequency per season

### 2024
| scoreline | count | pct |
|---|---|---|
| 1-2 | 44 | 11.6% |
| 1-0 | 41 | 10.8% |
| 0-0 | 37 | 9.7% |
| 1-1 | 36 | 9.5% |
| 0-1 | 35 | 9.2% |

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-0 | 48 | 12.6% |
| 1-1 | 43 | 11.3% |
| 0-1 | 42 | 11.1% |
| 0-0 | 38 | 10.0% |
| 1-2 | 32 | 8.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 75 | 9.9% |
| 1 | 166 | 21.8% |
| 2 | 165 | 21.7% |
| 3 | 166 | 21.8% |
| 4 | 100 | 13.2% |
| 5 | 55 | 7.2% |
| 6 | 22 | 2.9% |
| 7 | 9 | 1.2% |
| 8 | 2 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2024 | 2024-04-03 | 8-0 | 8 |
| 2024 | 2024-05-18 | 7-1 | 8 |
| 2024 | 2024-04-07 | 3-4 | 7 |
| 2024 | 2024-04-13 | 6-1 | 7 |
| 2024 | 2024-08-10 | 4-3 | 7 |
| 2024 | 2024-08-25 | 3-4 | 7 |
| 2024 | 2024-11-10 | 5-2 | 7 |
| 2025 | 2025-04-25 | 3-4 | 7 |
| 2025 | 2025-06-15 | 3-4 | 7 |
| 2025 | 2025-09-27 | 3-4 | 7 |
| 2025 | 2025-11-02 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **563** (draws: **197**)
- Average winning margin: **1.62**

| margin | matches | pct |
|---|---|---|
| 1 | 341 | 60.6% |
| 2 | 140 | 24.9% |
| 3+ | 82 | 14.6% |

## 6. Margin by outcome

### Home wins
- Matches: **298** | avg margin: **1.75** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 163 | 54.7% |
| 2 | 77 | 25.8% |
| 3+ | 58 | 19.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **265** | avg margin: **1.46** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 178 | 67.2% |
| 2 | 63 | 23.8% |
| 3+ | 24 | 9.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 298 | 1-0 | 89 | 29.9% |
| draw | 197 | 1-1 | 79 | 40.1% |
| away | 265 | 0-1 | 77 | 29.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\japan2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\japan2\charts\scoreline_analysis_total_goals.png)

