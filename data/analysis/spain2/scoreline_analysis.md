# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:09:09+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Scoreline frequency
- Matches analysed: **586** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 74 | 12.6% |
| 1-0 | 63 | 10.8% |
| 2-1 | 59 | 10.1% |
| 0-1 | 54 | 9.2% |
| 0-0 | 47 | 8.0% |
| 1-2 | 45 | 7.7% |
| 2-0 | 35 | 6.0% |
| 1-3 | 26 | 4.4% |
| 3-1 | 24 | 4.1% |
| 0-2 | 24 | 4.1% |
| 3-0 | 21 | 3.6% |
| 2-2 | 19 | 3.2% |
| 3-2 | 19 | 3.2% |
| 2-3 | 11 | 1.9% |
| 4-1 | 8 | 1.4% |
| 0-3 | 8 | 1.4% |
| 4-2 | 7 | 1.2% |
| 5-1 | 6 | 1.0% |
| 4-0 | 6 | 1.0% |
| 0-4 | 5 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 67 | 13.2% |
| 2-1 | 57 | 11.2% |
| 1-0 | 56 | 11.0% |
| 0-1 | 45 | 8.8% |
| 0-0 | 40 | 7.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 9 | 11.7% |
| 2-0 | 8 | 10.4% |
| 0-0 | 7 | 9.1% |
| 1-1 | 7 | 9.1% |
| 1-2 | 7 | 9.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 47 | 8.0% |
| 1 | 117 | 20.0% |
| 2 | 133 | 22.7% |
| 3 | 133 | 22.7% |
| 4 | 80 | 13.7% |
| 5 | 44 | 7.5% |
| 6 | 23 | 3.9% |
| 7 | 5 | 0.9% |
| 8 | 3 | 0.5% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-15 | 5-4 | 9 |
| 2025-2026 | 2025-08-18 | 4-4 | 8 |
| 2025-2026 | 2026-03-15 | 5-3 | 8 |
| 2025-2026 | 2026-04-05 | 6-2 | 8 |
| 2025-2026 | 2025-09-28 | 3-4 | 7 |
| 2025-2026 | 2025-10-04 | 5-2 | 7 |
| 2025-2026 | 2026-03-08 | 4-3 | 7 |
| 2025-2026 | 2026-03-21 | 5-2 | 7 |
| 2026-2027 | 2026-08-29 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **441** (draws: **145**)
- Average winning margin: **1.63**

| margin | matches | pct |
|---|---|---|
| 1 | 254 | 57.6% |
| 2 | 121 | 27.4% |
| 3+ | 66 | 15.0% |

## 6. Margin by outcome

### Home wins
- Matches: **256** | avg margin: **1.68** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 143 | 55.9% |
| 2 | 67 | 26.2% |
| 3+ | 46 | 18.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **185** | avg margin: **1.56** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 111 | 60.0% |
| 2 | 54 | 29.2% |
| 3+ | 20 | 10.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 256 | 1-0 | 63 | 24.6% |
| draw | 145 | 1-1 | 74 | 51.0% |
| away | 185 | 0-1 | 54 | 29.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\spain2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\spain2\charts\scoreline_analysis_total_goals.png)

