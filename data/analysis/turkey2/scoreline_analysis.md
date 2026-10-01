# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:10:50+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 1. Lig (Turkey)
- Scope: league `turkey2`

## 1. Scoreline frequency
- Matches analysed: **465** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 66 | 14.2% |
| 2-0 | 38 | 8.2% |
| 1-0 | 38 | 8.2% |
| 0-0 | 34 | 7.3% |
| 1-2 | 31 | 6.7% |
| 2-1 | 29 | 6.2% |
| 0-1 | 27 | 5.8% |
| 3-1 | 19 | 4.1% |
| 0-2 | 19 | 4.1% |
| 2-2 | 18 | 3.9% |
| 0-3 | 17 | 3.7% |
| 3-0 | 17 | 3.7% |
| 4-0 | 16 | 3.4% |
| 4-1 | 13 | 2.8% |
| 1-3 | 11 | 2.4% |
| 5-0 | 11 | 2.4% |
| 2-3 | 7 | 1.5% |
| 1-4 | 7 | 1.5% |
| 3-2 | 5 | 1.1% |
| 3-3 | 5 | 1.1% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 52 | 13.5% |
| 1-0 | 34 | 8.8% |
| 2-0 | 31 | 8.1% |
| 0-0 | 28 | 7.3% |
| 2-1 | 25 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 14 | 17.5% |
| 1-2 | 9 | 11.2% |
| 2-2 | 8 | 10.0% |
| 2-0 | 7 | 8.8% |
| 0-1 | 7 | 8.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 34 | 7.3% |
| 1 | 65 | 14.0% |
| 2 | 123 | 26.5% |
| 3 | 94 | 20.2% |
| 4 | 67 | 14.4% |
| 5 | 47 | 10.1% |
| 6 | 17 | 3.7% |
| 7 | 14 | 3.0% |
| 8 | 0 | 0.0% |
| 9 | 4 | 0.9% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **18**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-31 | 1-8 | 9 |
| 2025-2026 | 2025-11-09 | 2-7 | 9 |
| 2025-2026 | 2026-03-07 | 8-1 | 9 |
| 2025-2026 | 2026-05-01 | 8-1 | 9 |
| 2025-2026 | 2025-09-20 | 3-4 | 7 |
| 2025-2026 | 2025-12-06 | 3-4 | 7 |
| 2025-2026 | 2025-12-12 | 1-6 | 7 |
| 2025-2026 | 2026-02-01 | 7-0 | 7 |
| 2025-2026 | 2026-02-14 | 7-0 | 7 |
| 2025-2026 | 2026-02-14 | 4-3 | 7 |
| 2025-2026 | 2026-03-08 | 3-4 | 7 |
| 2025-2026 | 2026-03-10 | 3-4 | 7 |
| 2025-2026 | 2026-03-21 | 7-0 | 7 |
| 2025-2026 | 2026-04-05 | 6-1 | 7 |
| 2025-2026 | 2026-04-08 | 1-6 | 7 |
| 2025-2026 | 2026-04-12 | 1-6 | 7 |
| 2026-2027 | 2026-08-08 | 4-3 | 7 |
| 2026-2027 | 2026-09-06 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **342** (draws: **123**)
- Average winning margin: **2.16**

| margin | matches | pct |
|---|---|---|
| 1 | 144 | 42.1% |
| 2 | 94 | 27.5% |
| 3+ | 104 | 30.4% |

## 6. Margin by outcome

### Home wins
- Matches: **203** | avg margin: **2.29** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 75 | 36.9% |
| 2 | 62 | 30.5% |
| 3+ | 66 | 32.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **139** | avg margin: **1.97** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 69 | 49.6% |
| 2 | 32 | 23.0% |
| 3+ | 38 | 27.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 203 | 2-0 | 38 | 18.7% |
| draw | 123 | 1-1 | 66 | 53.7% |
| away | 139 | 1-2 | 31 | 22.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\turkey2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\turkey2\charts\scoreline_analysis_total_goals.png)

