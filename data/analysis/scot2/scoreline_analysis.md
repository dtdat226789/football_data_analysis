# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:45:12+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Scoreline frequency
- Matches analysed: **228** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 15.8% |
| 2-1 | 19 | 8.3% |
| 1-0 | 18 | 7.9% |
| 2-0 | 18 | 7.9% |
| 1-2 | 14 | 6.1% |
| 2-2 | 13 | 5.7% |
| 3-1 | 13 | 5.7% |
| 1-3 | 11 | 4.8% |
| 0-1 | 9 | 3.9% |
| 0-0 | 9 | 3.9% |
| 3-0 | 9 | 3.9% |
| 0-3 | 8 | 3.5% |
| 0-2 | 6 | 2.6% |
| 3-2 | 5 | 2.2% |
| 2-3 | 4 | 1.8% |
| 2-4 | 4 | 1.8% |
| 5-0 | 4 | 1.8% |
| 3-3 | 4 | 1.8% |
| 4-0 | 4 | 1.8% |
| 1-4 | 3 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 33 | 17.6% |
| 2-1 | 17 | 9.0% |
| 2-0 | 14 | 7.4% |
| 1-0 | 13 | 6.9% |
| 1-2 | 13 | 6.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 5 | 12.5% |
| 2-0 | 4 | 10.0% |
| 3-1 | 3 | 7.5% |
| 1-1 | 3 | 7.5% |
| 3-0 | 3 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 9 | 3.9% |
| 1 | 27 | 11.8% |
| 2 | 60 | 26.3% |
| 3 | 50 | 21.9% |
| 4 | 43 | 18.9% |
| 5 | 20 | 8.8% |
| 6 | 14 | 6.1% |
| 7 | 4 | 1.8% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.4% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-12 | 7-3 | 10 |
| 2025-2026 | 2025-08-23 | 3-4 | 7 |
| 2025-2026 | 2025-12-06 | 4-3 | 7 |
| 2025-2026 | 2026-02-17 | 1-6 | 7 |
| 2025-2026 | 2026-05-15 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **166** (draws: **62**)
- Average winning margin: **1.97**

| margin | matches | pct |
|---|---|---|
| 1 | 72 | 43.4% |
| 2 | 54 | 32.5% |
| 3+ | 40 | 24.1% |

## 6. Margin by outcome

### Home wins
- Matches: **99** | avg margin: **1.92** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 44 | 44.4% |
| 2 | 33 | 33.3% |
| 3+ | 22 | 22.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **67** | avg margin: **2.04** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 28 | 41.8% |
| 2 | 21 | 31.3% |
| 3+ | 18 | 26.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 99 | 2-1 | 19 | 19.2% |
| draw | 62 | 1-1 | 36 | 58.1% |
| away | 67 | 1-2 | 14 | 20.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\scot2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\scot2\charts\scoreline_analysis_total_goals.png)

