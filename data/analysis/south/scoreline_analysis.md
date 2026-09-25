# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:47:40+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Scoreline frequency
- Matches analysed: **716** across **2** seasons.
- Distinct scorelines seen: **38**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 84 | 11.7% |
| 1-1 | 77 | 10.8% |
| 1-2 | 72 | 10.1% |
| 2-0 | 54 | 7.5% |
| 2-1 | 54 | 7.5% |
| 0-1 | 47 | 6.6% |
| 0-0 | 44 | 6.1% |
| 2-2 | 34 | 4.7% |
| 3-0 | 30 | 4.2% |
| 3-2 | 27 | 3.8% |
| 3-1 | 26 | 3.6% |
| 0-2 | 21 | 2.9% |
| 1-3 | 18 | 2.5% |
| 2-3 | 17 | 2.4% |
| 0-3 | 15 | 2.1% |
| 4-1 | 14 | 2.0% |
| 3-3 | 11 | 1.5% |
| 0-4 | 9 | 1.3% |
| 4-2 | 9 | 1.3% |
| 1-4 | 7 | 1.0% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 75 | 12.4% |
| 1-2 | 63 | 10.4% |
| 1-1 | 59 | 9.8% |
| 2-1 | 51 | 8.4% |
| 2-0 | 46 | 7.6% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 18 | 16.2% |
| 0-1 | 10 | 9.0% |
| 1-2 | 9 | 8.1% |
| 1-0 | 9 | 8.1% |
| 2-0 | 8 | 7.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 44 | 6.1% |
| 1 | 131 | 18.3% |
| 2 | 152 | 21.2% |
| 3 | 171 | 23.9% |
| 4 | 94 | 13.1% |
| 5 | 72 | 10.1% |
| 6 | 32 | 4.5% |
| 7 | 12 | 1.7% |
| 8 | 5 | 0.7% |
| 9 | 3 | 0.4% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **20**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-10 | 5-4 | 9 |
| 2025-2026 | 2026-04-06 | 5-4 | 9 |
| 2025-2026 | 2026-04-11 | 7-2 | 9 |
| 2025-2026 | 2026-02-14 | 5-3 | 8 |
| 2025-2026 | 2026-02-24 | 8-0 | 8 |
| 2025-2026 | 2026-03-07 | 7-1 | 8 |
| 2026-2027 | 2026-08-15 | 5-3 | 8 |
| 2026-2027 | 2026-08-22 | 5-3 | 8 |
| 2025-2026 | 2025-08-16 | 3-4 | 7 |
| 2025-2026 | 2025-09-01 | 2-5 | 7 |
| 2025-2026 | 2025-09-06 | 2-5 | 7 |
| 2025-2026 | 2025-09-20 | 2-5 | 7 |
| 2025-2026 | 2025-11-22 | 7-0 | 7 |
| 2025-2026 | 2025-12-20 | 2-5 | 7 |
| 2025-2026 | 2025-12-30 | 3-4 | 7 |
| 2025-2026 | 2026-03-21 | 5-2 | 7 |
| 2025-2026 | 2026-03-31 | 3-4 | 7 |
| 2025-2026 | 2026-04-18 | 1-6 | 7 |
| 2025-2026 | 2026-04-18 | 5-2 | 7 |
| 2025-2026 | 2026-04-25 | 1-6 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **550** (draws: **166**)
- Average winning margin: **1.75**

| margin | matches | pct |
|---|---|---|
| 1 | 306 | 55.6% |
| 2 | 134 | 24.4% |
| 3+ | 110 | 20.0% |

## 6. Margin by outcome

### Home wins
- Matches: **327** | avg margin: **1.81** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 167 | 51.1% |
| 2 | 92 | 28.1% |
| 3+ | 68 | 20.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **223** | avg margin: **1.67** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 139 | 62.3% |
| 2 | 42 | 18.8% |
| 3+ | 42 | 18.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 327 | 1-0 | 84 | 25.7% |
| draw | 166 | 1-1 | 77 | 46.4% |
| away | 223 | 1-2 | 72 | 32.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\south\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\south\charts\scoreline_analysis_total_goals.png)

