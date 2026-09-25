# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:42:33+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Scoreline frequency
- Matches analysed: **438** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 58 | 13.2% |
| 1-1 | 56 | 12.8% |
| 2-1 | 45 | 10.3% |
| 0-0 | 41 | 9.4% |
| 2-0 | 37 | 8.4% |
| 0-1 | 31 | 7.1% |
| 1-2 | 25 | 5.7% |
| 2-2 | 22 | 5.0% |
| 0-2 | 19 | 4.3% |
| 3-0 | 19 | 4.3% |
| 3-1 | 15 | 3.4% |
| 1-3 | 10 | 2.3% |
| 2-3 | 9 | 2.1% |
| 4-1 | 8 | 1.8% |
| 3-2 | 7 | 1.6% |
| 0-3 | 4 | 0.9% |
| 2-4 | 4 | 0.9% |
| 0-4 | 4 | 0.9% |
| 1-4 | 4 | 0.9% |
| 4-3 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 51 | 12.8% |
| 1-0 | 49 | 12.3% |
| 2-1 | 42 | 10.6% |
| 0-0 | 39 | 9.8% |
| 2-0 | 36 | 9.0% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 9 | 22.5% |
| 1-1 | 5 | 12.5% |
| 0-1 | 3 | 7.5% |
| 4-1 | 3 | 7.5% |
| 2-1 | 3 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 41 | 9.4% |
| 1 | 89 | 20.3% |
| 2 | 112 | 25.6% |
| 3 | 93 | 21.2% |
| 4 | 54 | 12.3% |
| 5 | 31 | 7.1% |
| 6 | 12 | 2.7% |
| 7 | 5 | 1.1% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-07 | 6-3 | 9 |
| 2025-2026 | 2025-10-05 | 3-4 | 7 |
| 2025-2026 | 2025-11-08 | 4-3 | 7 |
| 2025-2026 | 2025-11-29 | 4-3 | 7 |
| 2025-2026 | 2026-03-29 | 4-3 | 7 |
| 2026-2027 | 2026-09-12 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **316** (draws: **122**)
- Average winning margin: **1.63**

| margin | matches | pct |
|---|---|---|
| 1 | 180 | 57.0% |
| 2 | 88 | 27.8% |
| 3+ | 48 | 15.2% |

## 6. Margin by outcome

### Home wins
- Matches: **202** | avg margin: **1.64** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 113 | 55.9% |
| 2 | 55 | 27.2% |
| 3+ | 34 | 16.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **114** | avg margin: **1.61** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 58.8% |
| 2 | 33 | 28.9% |
| 3+ | 14 | 12.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 202 | 1-0 | 58 | 28.7% |
| draw | 122 | 1-1 | 56 | 45.9% |
| away | 114 | 0-1 | 31 | 27.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\primera1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\primera1\charts\scoreline_analysis_total_goals.png)

