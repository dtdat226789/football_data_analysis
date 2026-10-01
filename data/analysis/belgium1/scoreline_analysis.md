# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:45:09+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Jupiler Pro League (Belgium)
- Scope: league `belgium1`

## 1. Scoreline frequency
- Matches analysed: **384** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 42 | 10.9% |
| 2-1 | 35 | 9.1% |
| 1-0 | 34 | 8.9% |
| 1-2 | 32 | 8.3% |
| 2-0 | 31 | 8.1% |
| 0-0 | 28 | 7.3% |
| 0-1 | 27 | 7.0% |
| 0-2 | 23 | 6.0% |
| 2-2 | 17 | 4.4% |
| 3-0 | 17 | 4.4% |
| 3-1 | 14 | 3.6% |
| 1-3 | 11 | 2.9% |
| 2-3 | 10 | 2.6% |
| 3-2 | 9 | 2.3% |
| 4-0 | 8 | 2.1% |
| 0-3 | 7 | 1.8% |
| 1-4 | 5 | 1.3% |
| 5-0 | 4 | 1.0% |
| 4-1 | 4 | 1.0% |
| 0-4 | 4 | 1.0% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 39 | 12.1% |
| 2-1 | 30 | 9.3% |
| 1-2 | 30 | 9.3% |
| 1-0 | 28 | 8.7% |
| 2-0 | 26 | 8.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 3-0 | 6 | 9.5% |
| 1-0 | 6 | 9.5% |
| 2-0 | 5 | 7.9% |
| 2-1 | 5 | 7.9% |
| 0-1 | 5 | 7.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 28 | 7.3% |
| 1 | 61 | 15.9% |
| 2 | 96 | 25.0% |
| 3 | 91 | 23.7% |
| 4 | 54 | 14.1% |
| 5 | 33 | 8.6% |
| 6 | 13 | 3.4% |
| 7 | 4 | 1.0% |
| 8 | 2 | 0.5% |
| 9 | 0 | 0.0% |
| 10+ | 2 | 0.5% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-09-24 | 5-5 | 10 |
| 2025-2026 | 2026-03-22 | 5-5 | 10 |
| 2025-2026 | 2025-12-26 | 3-5 | 8 |
| 2026-2027 | 2026-08-22 | 4-4 | 8 |
| 2025-2026 | 2025-07-27 | 5-2 | 7 |
| 2025-2026 | 2026-01-24 | 4-3 | 7 |
| 2025-2026 | 2026-02-07 | 3-4 | 7 |
| 2025-2026 | 2026-04-22 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **291** (draws: **93**)
- Average winning margin: **1.78**

| margin | matches | pct |
|---|---|---|
| 1 | 149 | 51.2% |
| 2 | 86 | 29.6% |
| 3+ | 56 | 19.2% |

## 6. Margin by outcome

### Home wins
- Matches: **164** | avg margin: **1.87** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 79 | 48.2% |
| 2 | 48 | 29.3% |
| 3+ | 37 | 22.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **127** | avg margin: **1.66** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 70 | 55.1% |
| 2 | 38 | 29.9% |
| 3+ | 19 | 15.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 164 | 2-1 | 35 | 21.3% |
| draw | 93 | 1-1 | 42 | 45.2% |
| away | 127 | 1-2 | 32 | 25.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\belgium1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\belgium1\charts\scoreline_analysis_total_goals.png)

