# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:08:39+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League South (England)
- Scope: league `south`

## 1. Scoreline frequency
- Matches analysed: **728** across **2** seasons.
- Distinct scorelines seen: **39**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 85 | 11.7% |
| 1-1 | 77 | 10.6% |
| 1-2 | 74 | 10.2% |
| 2-0 | 56 | 7.7% |
| 2-1 | 54 | 7.4% |
| 0-1 | 47 | 6.5% |
| 0-0 | 45 | 6.2% |
| 2-2 | 35 | 4.8% |
| 3-0 | 31 | 4.3% |
| 3-2 | 28 | 3.8% |
| 3-1 | 26 | 3.6% |
| 0-2 | 22 | 3.0% |
| 1-3 | 18 | 2.5% |
| 2-3 | 17 | 2.3% |
| 0-3 | 15 | 2.1% |
| 4-1 | 14 | 1.9% |
| 3-3 | 11 | 1.5% |
| 0-4 | 10 | 1.4% |
| 4-2 | 9 | 1.2% |
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
| 1-1 | 18 | 14.6% |
| 1-2 | 11 | 8.9% |
| 2-0 | 10 | 8.1% |
| 0-1 | 10 | 8.1% |
| 1-0 | 10 | 8.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 45 | 6.2% |
| 1 | 132 | 18.1% |
| 2 | 155 | 21.3% |
| 3 | 174 | 23.9% |
| 4 | 96 | 13.2% |
| 5 | 73 | 10.0% |
| 6 | 32 | 4.4% |
| 7 | 13 | 1.8% |
| 8 | 5 | 0.7% |
| 9 | 3 | 0.4% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **21**

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
| 2026-2027 | 2026-09-26 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **560** (draws: **168**)
- Average winning margin: **1.76**

| margin | matches | pct |
|---|---|---|
| 1 | 311 | 55.5% |
| 2 | 137 | 24.5% |
| 3+ | 112 | 20.0% |

## 6. Margin by outcome

### Home wins
- Matches: **333** | avg margin: **1.81** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 170 | 51.1% |
| 2 | 94 | 28.2% |
| 3+ | 69 | 20.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **227** | avg margin: **1.67** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 141 | 62.1% |
| 2 | 43 | 18.9% |
| 3+ | 43 | 18.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 333 | 1-0 | 85 | 25.5% |
| draw | 168 | 1-1 | 77 | 45.8% |
| away | 227 | 1-2 | 74 | 32.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\south\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\south\charts\scoreline_analysis_total_goals.png)

