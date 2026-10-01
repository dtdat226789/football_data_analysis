# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:04:21+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Scoreline frequency
- Matches analysed: **448** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 60 | 13.4% |
| 1-1 | 57 | 12.7% |
| 2-1 | 45 | 10.0% |
| 0-0 | 42 | 9.4% |
| 2-0 | 38 | 8.5% |
| 0-1 | 32 | 7.1% |
| 1-2 | 25 | 5.6% |
| 2-2 | 23 | 5.1% |
| 0-2 | 19 | 4.2% |
| 3-0 | 19 | 4.2% |
| 3-1 | 15 | 3.3% |
| 1-3 | 10 | 2.2% |
| 2-3 | 9 | 2.0% |
| 4-1 | 8 | 1.8% |
| 3-2 | 7 | 1.6% |
| 0-3 | 5 | 1.1% |
| 2-4 | 4 | 0.9% |
| 0-4 | 4 | 0.9% |
| 1-4 | 4 | 0.9% |
| 3-3 | 4 | 0.9% |

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
| 1-0 | 11 | 22.0% |
| 1-1 | 6 | 12.0% |
| 0-1 | 4 | 8.0% |
| 0-0 | 3 | 6.0% |
| 4-1 | 3 | 6.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 42 | 9.4% |
| 1 | 92 | 20.5% |
| 2 | 114 | 25.4% |
| 3 | 94 | 21.0% |
| 4 | 55 | 12.3% |
| 5 | 31 | 6.9% |
| 6 | 13 | 2.9% |
| 7 | 5 | 1.1% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-07 | 6-3 | 9 |
| 2026-2027 | 2026-09-27 | 3-5 | 8 |
| 2025-2026 | 2025-10-05 | 3-4 | 7 |
| 2025-2026 | 2025-11-08 | 4-3 | 7 |
| 2025-2026 | 2025-11-29 | 4-3 | 7 |
| 2025-2026 | 2026-03-29 | 4-3 | 7 |
| 2026-2027 | 2026-09-12 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **322** (draws: **126**)
- Average winning margin: **1.63**

| margin | matches | pct |
|---|---|---|
| 1 | 183 | 56.8% |
| 2 | 90 | 28.0% |
| 3+ | 49 | 15.2% |

## 6. Margin by outcome

### Home wins
- Matches: **205** | avg margin: **1.64** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 115 | 56.1% |
| 2 | 56 | 27.3% |
| 3+ | 34 | 16.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **117** | avg margin: **1.62** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 68 | 58.1% |
| 2 | 34 | 29.1% |
| 3+ | 15 | 12.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 205 | 1-0 | 60 | 29.3% |
| draw | 126 | 1-1 | 57 | 45.2% |
| away | 117 | 0-1 | 32 | 27.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\primera1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\primera1\charts\scoreline_analysis_total_goals.png)

