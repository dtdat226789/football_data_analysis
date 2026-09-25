# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:54:58+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 2. Liga (Austria)
- Scope: league `austria2`

## 1. Scoreline frequency
- Matches analysed: **279** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 28 | 10.0% |
| 2-1 | 25 | 9.0% |
| 0-2 | 23 | 8.2% |
| 1-0 | 23 | 8.2% |
| 0-1 | 20 | 7.2% |
| 0-0 | 19 | 6.8% |
| 2-0 | 17 | 6.1% |
| 1-2 | 16 | 5.7% |
| 2-2 | 14 | 5.0% |
| 3-1 | 13 | 4.7% |
| 3-0 | 12 | 4.3% |
| 0-3 | 8 | 2.9% |
| 2-3 | 7 | 2.5% |
| 4-0 | 7 | 2.5% |
| 1-3 | 7 | 2.5% |
| 3-2 | 6 | 2.2% |
| 4-2 | 5 | 1.8% |
| 4-1 | 5 | 1.8% |
| 0-4 | 4 | 1.4% |
| 1-4 | 4 | 1.4% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 25 | 11.2% |
| 2-1 | 20 | 9.0% |
| 0-2 | 19 | 8.5% |
| 1-0 | 18 | 8.1% |
| 0-0 | 18 | 8.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 5 | 8.9% |
| 1-0 | 5 | 8.9% |
| 2-1 | 5 | 8.9% |
| 0-2 | 4 | 7.1% |
| 1-3 | 4 | 7.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 6.8% |
| 1 | 43 | 15.4% |
| 2 | 68 | 24.4% |
| 3 | 61 | 21.9% |
| 4 | 45 | 16.1% |
| 5 | 25 | 9.0% |
| 6 | 10 | 3.6% |
| 7 | 7 | 2.5% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-09 | 4-4 | 8 |
| 2025-2026 | 2025-10-24 | 4-3 | 7 |
| 2025-2026 | 2025-11-07 | 5-2 | 7 |
| 2025-2026 | 2025-12-05 | 6-1 | 7 |
| 2025-2026 | 2026-03-06 | 4-3 | 7 |
| 2025-2026 | 2026-03-20 | 2-5 | 7 |
| 2026-2027 | 2026-08-30 | 5-2 | 7 |
| 2026-2027 | 2026-09-18 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **213** (draws: **66**)
- Average winning margin: **1.85**

| margin | matches | pct |
|---|---|---|
| 1 | 100 | 46.9% |
| 2 | 65 | 30.5% |
| 3+ | 48 | 22.5% |

## 6. Margin by outcome

### Home wins
- Matches: **121** | avg margin: **1.9** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 46.3% |
| 2 | 35 | 28.9% |
| 3+ | 30 | 24.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **92** | avg margin: **1.78** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 44 | 47.8% |
| 2 | 30 | 32.6% |
| 3+ | 18 | 19.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 121 | 2-1 | 25 | 20.7% |
| draw | 66 | 1-1 | 28 | 42.4% |
| away | 92 | 0-2 | 23 | 25.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\austria2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\austria2\charts\scoreline_analysis_total_goals.png)

