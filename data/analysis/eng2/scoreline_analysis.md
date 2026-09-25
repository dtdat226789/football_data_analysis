# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:57:55+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: League Two (England)
- Scope: league `eng2`

## 1. Scoreline frequency
- Matches analysed: **641** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 78 | 12.2% |
| 1-0 | 77 | 12.0% |
| 2-1 | 53 | 8.3% |
| 0-1 | 52 | 8.1% |
| 1-2 | 48 | 7.5% |
| 2-0 | 48 | 7.5% |
| 0-0 | 45 | 7.0% |
| 2-2 | 38 | 5.9% |
| 0-2 | 35 | 5.5% |
| 3-1 | 31 | 4.8% |
| 1-3 | 22 | 3.4% |
| 3-2 | 19 | 3.0% |
| 3-0 | 17 | 2.7% |
| 0-3 | 14 | 2.2% |
| 4-0 | 9 | 1.4% |
| 2-3 | 9 | 1.4% |
| 3-3 | 8 | 1.2% |
| 1-4 | 8 | 1.2% |
| 4-1 | 7 | 1.1% |
| 0-4 | 5 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 68 | 12.2% |
| 1-1 | 66 | 11.8% |
| 0-1 | 48 | 8.6% |
| 2-1 | 46 | 8.3% |
| 1-2 | 46 | 8.3% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-0 | 13 | 15.5% |
| 1-1 | 12 | 14.3% |
| 1-0 | 9 | 10.7% |
| 2-2 | 8 | 9.5% |
| 0-0 | 8 | 9.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 45 | 7.0% |
| 1 | 129 | 20.1% |
| 2 | 161 | 25.1% |
| 3 | 132 | 20.6% |
| 4 | 105 | 16.4% |
| 5 | 47 | 7.3% |
| 6 | 14 | 2.2% |
| 7 | 4 | 0.6% |
| 8 | 4 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-09-27 | 7-1 | 8 |
| 2025-2026 | 2025-10-04 | 6-2 | 8 |
| 2025-2026 | 2026-04-25 | 6-2 | 8 |
| 2026-2027 | 2026-08-22 | 5-3 | 8 |
| 2025-2026 | 2025-11-29 | 4-3 | 7 |
| 2025-2026 | 2025-12-13 | 4-3 | 7 |
| 2025-2026 | 2026-03-21 | 5-2 | 7 |
| 2025-2026 | 2026-04-06 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **472** (draws: **169**)
- Average winning margin: **1.66**

| margin | matches | pct |
|---|---|---|
| 1 | 260 | 55.1% |
| 2 | 141 | 29.9% |
| 3+ | 71 | 15.0% |

## 6. Margin by outcome

### Home wins
- Matches: **276** | avg margin: **1.69** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 151 | 54.7% |
| 2 | 83 | 30.1% |
| 3+ | 42 | 15.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **196** | avg margin: **1.62** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 109 | 55.6% |
| 2 | 58 | 29.6% |
| 3+ | 29 | 14.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 276 | 1-0 | 77 | 27.9% |
| draw | 169 | 1-1 | 78 | 46.2% |
| away | 196 | 0-1 | 52 | 26.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\eng2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\eng2\charts\scoreline_analysis_total_goals.png)

