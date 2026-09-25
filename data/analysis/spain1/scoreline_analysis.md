# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:47:58+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Scoreline frequency
- Matches analysed: **449** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 68 | 15.1% |
| 1-0 | 52 | 11.6% |
| 2-1 | 47 | 10.5% |
| 1-2 | 30 | 6.7% |
| 2-0 | 29 | 6.5% |
| 0-1 | 27 | 6.0% |
| 0-2 | 24 | 5.3% |
| 3-0 | 20 | 4.5% |
| 0-0 | 20 | 4.5% |
| 3-1 | 19 | 4.2% |
| 2-2 | 18 | 4.0% |
| 3-2 | 16 | 3.6% |
| 1-3 | 12 | 2.7% |
| 2-3 | 11 | 2.4% |
| 4-1 | 10 | 2.2% |
| 0-3 | 8 | 1.8% |
| 4-0 | 8 | 1.8% |
| 5-2 | 5 | 1.1% |
| 3-3 | 4 | 0.9% |
| 4-2 | 4 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 58 | 15.3% |
| 1-0 | 44 | 11.6% |
| 2-1 | 42 | 11.1% |
| 2-0 | 27 | 7.1% |
| 1-2 | 27 | 7.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 10 | 14.5% |
| 1-0 | 8 | 11.6% |
| 2-1 | 5 | 7.2% |
| 1-3 | 5 | 7.2% |
| 0-0 | 5 | 7.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 20 | 4.5% |
| 1 | 79 | 17.6% |
| 2 | 121 | 26.9% |
| 3 | 105 | 23.4% |
| 4 | 58 | 12.9% |
| 5 | 42 | 9.4% |
| 6 | 15 | 3.3% |
| 7 | 7 | 1.6% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-16 | 7-2 | 9 |
| 2025-2026 | 2025-12-06 | 3-5 | 8 |
| 2025-2026 | 2025-09-27 | 5-2 | 7 |
| 2025-2026 | 2026-03-15 | 5-2 | 7 |
| 2025-2026 | 2026-03-22 | 3-4 | 7 |
| 2025-2026 | 2026-05-17 | 3-4 | 7 |
| 2026-2027 | 2026-08-29 | 5-2 | 7 |
| 2026-2027 | 2026-08-31 | 5-2 | 7 |
| 2026-2027 | 2026-09-06 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **339** (draws: **110**)
- Average winning margin: **1.71**

| margin | matches | pct |
|---|---|---|
| 1 | 185 | 54.6% |
| 2 | 92 | 27.1% |
| 3+ | 62 | 18.3% |

## 6. Margin by outcome

### Home wins
- Matches: **217** | avg margin: **1.79** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 115 | 53.0% |
| 2 | 52 | 24.0% |
| 3+ | 50 | 23.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **122** | avg margin: **1.57** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 70 | 57.4% |
| 2 | 40 | 32.8% |
| 3+ | 12 | 9.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 217 | 1-0 | 52 | 24.0% |
| draw | 110 | 1-1 | 68 | 61.8% |
| away | 122 | 1-2 | 30 | 24.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\spain1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\spain1\charts\scoreline_analysis_total_goals.png)

