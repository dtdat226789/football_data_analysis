# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:51:29+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 3. Liga (Germany)
- Scope: league `germany3`

## 1. Scoreline frequency
- Matches analysed: **450** across **2** seasons.
- Distinct scorelines seen: **36**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 47 | 10.4% |
| 1-1 | 46 | 10.2% |
| 1-0 | 29 | 6.4% |
| 1-2 | 27 | 6.0% |
| 2-2 | 26 | 5.8% |
| 2-0 | 26 | 5.8% |
| 3-1 | 26 | 5.8% |
| 0-0 | 25 | 5.6% |
| 0-1 | 23 | 5.1% |
| 1-3 | 21 | 4.7% |
| 3-2 | 19 | 4.2% |
| 3-0 | 14 | 3.1% |
| 2-3 | 14 | 3.1% |
| 0-3 | 14 | 3.1% |
| 0-2 | 13 | 2.9% |
| 4-1 | 12 | 2.7% |
| 4-0 | 9 | 2.0% |
| 2-4 | 8 | 1.8% |
| 3-3 | 6 | 1.3% |
| 5-1 | 5 | 1.1% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 41 | 10.8% |
| 2-1 | 40 | 10.5% |
| 3-1 | 26 | 6.8% |
| 2-0 | 24 | 6.3% |
| 0-0 | 23 | 6.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 8 | 11.4% |
| 2-1 | 7 | 10.0% |
| 1-2 | 7 | 10.0% |
| 1-1 | 5 | 7.1% |
| 1-3 | 4 | 5.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 25 | 5.6% |
| 1 | 52 | 11.6% |
| 2 | 85 | 18.9% |
| 3 | 102 | 22.7% |
| 4 | 86 | 19.1% |
| 5 | 53 | 11.8% |
| 6 | 25 | 5.6% |
| 7 | 15 | 3.3% |
| 8 | 7 | 1.6% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **22**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-09-17 | 2-6 | 8 |
| 2025-2026 | 2025-12-12 | 3-5 | 8 |
| 2025-2026 | 2026-04-04 | 3-5 | 8 |
| 2025-2026 | 2026-04-19 | 5-3 | 8 |
| 2025-2026 | 2026-05-03 | 3-5 | 8 |
| 2025-2026 | 2026-05-09 | 5-3 | 8 |
| 2026-2027 | 2026-09-12 | 6-2 | 8 |
| 2025-2026 | 2025-08-22 | 3-4 | 7 |
| 2025-2026 | 2025-09-27 | 6-1 | 7 |
| 2025-2026 | 2025-10-25 | 4-3 | 7 |
| 2025-2026 | 2025-11-01 | 4-3 | 7 |
| 2025-2026 | 2026-01-17 | 5-2 | 7 |
| 2025-2026 | 2026-02-14 | 6-1 | 7 |
| 2025-2026 | 2026-03-21 | 5-2 | 7 |
| 2025-2026 | 2026-04-25 | 2-5 | 7 |
| 2025-2026 | 2026-05-02 | 6-1 | 7 |
| 2025-2026 | 2026-05-16 | 6-1 | 7 |
| 2025-2026 | 2026-05-16 | 3-4 | 7 |
| 2025-2026 | 2026-05-16 | 3-4 | 7 |
| 2026-2027 | 2026-08-08 | 2-5 | 7 |
| 2026-2027 | 2026-08-09 | 5-2 | 7 |
| 2026-2027 | 2026-09-05 | 1-6 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **347** (draws: **103**)
- Average winning margin: **1.88**

| margin | matches | pct |
|---|---|---|
| 1 | 164 | 47.3% |
| 2 | 102 | 29.4% |
| 3+ | 81 | 23.3% |

## 6. Margin by outcome

### Home wins
- Matches: **204** | avg margin: **1.9** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 97 | 47.5% |
| 2 | 57 | 27.9% |
| 3+ | 50 | 24.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **143** | avg margin: **1.85** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 46.9% |
| 2 | 45 | 31.5% |
| 3+ | 31 | 21.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 204 | 2-1 | 47 | 23.0% |
| draw | 103 | 1-1 | 46 | 44.7% |
| away | 143 | 1-2 | 27 | 18.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\germany3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\germany3\charts\scoreline_analysis_total_goals.png)

