# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:57:11+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Scoreline frequency
- Matches analysed: **432** across **2** seasons.
- Distinct scorelines seen: **34**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 58 | 13.4% |
| 1-2 | 37 | 8.6% |
| 1-0 | 37 | 8.6% |
| 2-1 | 37 | 8.6% |
| 0-1 | 36 | 8.3% |
| 0-0 | 31 | 7.2% |
| 2-2 | 30 | 6.9% |
| 0-2 | 23 | 5.3% |
| 2-0 | 22 | 5.1% |
| 3-1 | 18 | 4.2% |
| 3-3 | 14 | 3.2% |
| 3-0 | 14 | 3.2% |
| 1-3 | 12 | 2.8% |
| 3-2 | 11 | 2.5% |
| 2-3 | 8 | 1.9% |
| 4-1 | 7 | 1.6% |
| 0-3 | 6 | 1.4% |
| 4-2 | 4 | 0.9% |
| 1-4 | 3 | 0.7% |
| 4-0 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 52 | 13.6% |
| 1-0 | 36 | 9.4% |
| 2-1 | 34 | 8.9% |
| 1-2 | 33 | 8.6% |
| 0-0 | 29 | 7.6% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 8 | 16.0% |
| 1-1 | 6 | 12.0% |
| 2-2 | 5 | 10.0% |
| 1-2 | 4 | 8.0% |
| 1-3 | 3 | 6.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.2% |
| 1 | 73 | 16.9% |
| 2 | 103 | 23.8% |
| 3 | 94 | 21.8% |
| 4 | 64 | 14.8% |
| 5 | 30 | 6.9% |
| 6 | 23 | 5.3% |
| 7 | 7 | 1.6% |
| 8 | 5 | 1.2% |
| 9 | 2 | 0.5% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **14**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-25 | 7-2 | 9 |
| 2025-2026 | 2026-02-20 | 5-4 | 9 |
| 2025-2026 | 2026-02-15 | 2-6 | 8 |
| 2025-2026 | 2026-05-02 | 3-5 | 8 |
| 2025-2026 | 2026-05-02 | 3-5 | 8 |
| 2026-2027 | 2026-08-29 | 6-2 | 8 |
| 2026-2027 | 2026-09-12 | 5-3 | 8 |
| 2025-2026 | 2025-12-13 | 4-3 | 7 |
| 2025-2026 | 2026-03-07 | 5-2 | 7 |
| 2025-2026 | 2026-03-14 | 5-2 | 7 |
| 2025-2026 | 2026-03-14 | 7-0 | 7 |
| 2025-2026 | 2026-05-02 | 5-2 | 7 |
| 2025-2026 | 2026-05-10 | 6-1 | 7 |
| 2026-2027 | 2026-09-13 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **299** (draws: **133**)
- Average winning margin: **1.66**

| margin | matches | pct |
|---|---|---|
| 1 | 168 | 56.2% |
| 2 | 85 | 28.4% |
| 3+ | 46 | 15.4% |

## 6. Margin by outcome

### Home wins
- Matches: **166** | avg margin: **1.78** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 87 | 52.4% |
| 2 | 45 | 27.1% |
| 3+ | 34 | 20.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **133** | avg margin: **1.51** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 81 | 60.9% |
| 2 | 40 | 30.1% |
| 3+ | 12 | 9.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 166 | 1-0 | 37 | 22.3% |
| draw | 133 | 1-1 | 58 | 43.6% |
| away | 133 | 1-2 | 37 | 27.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy19\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy19\charts\scoreline_analysis_total_goals.png)

