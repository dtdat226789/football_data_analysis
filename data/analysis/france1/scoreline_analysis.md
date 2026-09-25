# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:58:42+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

## 1. Scoreline frequency
- Matches analysed: **355** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 40 | 11.3% |
| 1-1 | 32 | 9.0% |
| 0-0 | 29 | 8.2% |
| 0-1 | 27 | 7.6% |
| 2-1 | 26 | 7.3% |
| 1-2 | 25 | 7.0% |
| 2-0 | 24 | 6.8% |
| 2-2 | 21 | 5.9% |
| 3-1 | 20 | 5.6% |
| 3-0 | 15 | 4.2% |
| 0-2 | 13 | 3.7% |
| 3-2 | 10 | 2.8% |
| 2-3 | 8 | 2.3% |
| 4-0 | 7 | 2.0% |
| 0-3 | 7 | 2.0% |
| 3-3 | 6 | 1.7% |
| 4-1 | 6 | 1.7% |
| 1-3 | 6 | 1.7% |
| 0-4 | 5 | 1.4% |
| 5-2 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 38 | 12.3% |
| 1-1 | 29 | 9.4% |
| 0-0 | 25 | 8.1% |
| 0-1 | 23 | 7.4% |
| 2-0 | 21 | 6.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 6 | 13.3% |
| 2-1 | 6 | 13.3% |
| 1-2 | 5 | 11.1% |
| 0-0 | 4 | 8.9% |
| 0-1 | 4 | 8.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.2% |
| 1 | 67 | 18.9% |
| 2 | 69 | 19.4% |
| 3 | 73 | 20.6% |
| 4 | 59 | 16.6% |
| 5 | 31 | 8.7% |
| 6 | 11 | 3.1% |
| 7 | 9 | 2.5% |
| 8 | 5 | 1.4% |
| 9 | 2 | 0.6% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **16**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-30 | 3-6 | 9 |
| 2025-2026 | 2026-05-17 | 5-4 | 9 |
| 2025-2026 | 2025-08-30 | 1-7 | 8 |
| 2025-2026 | 2025-10-18 | 6-2 | 8 |
| 2025-2026 | 2025-10-29 | 3-5 | 8 |
| 2025-2026 | 2026-04-26 | 4-4 | 8 |
| 2026-2027 | 2026-09-06 | 2-6 | 8 |
| 2025-2026 | 2025-08-23 | 5-2 | 7 |
| 2025-2026 | 2025-09-21 | 5-2 | 7 |
| 2025-2026 | 2025-10-26 | 6-1 | 7 |
| 2025-2026 | 2025-12-14 | 3-4 | 7 |
| 2025-2026 | 2026-01-17 | 2-5 | 7 |
| 2025-2026 | 2026-01-25 | 2-5 | 7 |
| 2025-2026 | 2026-03-15 | 3-4 | 7 |
| 2025-2026 | 2026-04-04 | 3-4 | 7 |
| 2026-2027 | 2026-08-22 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **266** (draws: **89**)
- Average winning margin: **1.81**

| margin | matches | pct |
|---|---|---|
| 1 | 140 | 52.6% |
| 2 | 66 | 24.8% |
| 3+ | 60 | 22.6% |

## 6. Margin by outcome

### Home wins
- Matches: **161** | avg margin: **1.87** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 77 | 47.8% |
| 2 | 46 | 28.6% |
| 3+ | 38 | 23.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **105** | avg margin: **1.72** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 63 | 60.0% |
| 2 | 20 | 19.0% |
| 3+ | 22 | 21.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 161 | 1-0 | 40 | 24.8% |
| draw | 89 | 1-1 | 32 | 36.0% |
| away | 105 | 0-1 | 27 | 25.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\france1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\france1\charts\scoreline_analysis_total_goals.png)

