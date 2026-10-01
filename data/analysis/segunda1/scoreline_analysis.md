# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:06:52+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Scoreline frequency
- Matches analysed: **342** across **2** seasons.
- Distinct scorelines seen: **30**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 45 | 13.2% |
| 1-1 | 40 | 11.7% |
| 1-2 | 31 | 9.1% |
| 0-1 | 29 | 8.5% |
| 2-1 | 29 | 8.5% |
| 0-0 | 29 | 8.5% |
| 0-2 | 18 | 5.3% |
| 3-0 | 17 | 5.0% |
| 2-2 | 16 | 4.7% |
| 2-0 | 14 | 4.1% |
| 3-1 | 14 | 4.1% |
| 3-2 | 7 | 2.0% |
| 4-1 | 6 | 1.8% |
| 0-3 | 6 | 1.8% |
| 1-3 | 5 | 1.5% |
| 0-4 | 5 | 1.5% |
| 3-3 | 5 | 1.5% |
| 2-3 | 4 | 1.2% |
| 3-4 | 4 | 1.2% |
| 4-0 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 42 | 13.7% |
| 1-1 | 38 | 12.4% |
| 1-2 | 29 | 9.5% |
| 0-0 | 28 | 9.2% |
| 0-1 | 26 | 8.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 5 | 13.9% |
| 0-2 | 4 | 11.1% |
| 0-1 | 3 | 8.3% |
| 2-2 | 3 | 8.3% |
| 1-0 | 3 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 8.5% |
| 1 | 74 | 21.6% |
| 2 | 72 | 21.1% |
| 3 | 83 | 24.3% |
| 4 | 43 | 12.6% |
| 5 | 21 | 6.1% |
| 6 | 10 | 2.9% |
| 7 | 8 | 2.3% |
| 8 | 1 | 0.3% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **10**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-07 | 7-2 | 9 |
| 2025-2026 | 2026-03-21 | 4-4 | 8 |
| 2025-2026 | 2025-10-05 | 5-2 | 7 |
| 2025-2026 | 2026-02-08 | 7-0 | 7 |
| 2025-2026 | 2026-02-15 | 3-4 | 7 |
| 2025-2026 | 2026-03-01 | 5-2 | 7 |
| 2025-2026 | 2026-04-04 | 3-4 | 7 |
| 2025-2026 | 2026-04-05 | 3-4 | 7 |
| 2025-2026 | 2026-05-03 | 3-4 | 7 |
| 2026-2027 | 2026-09-27 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **251** (draws: **91**)
- Average winning margin: **1.68**

| margin | matches | pct |
|---|---|---|
| 1 | 149 | 59.4% |
| 2 | 54 | 21.5% |
| 3+ | 48 | 19.1% |

## 6. Margin by outcome

### Home wins
- Matches: **143** | avg margin: **1.73** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 81 | 56.6% |
| 2 | 30 | 21.0% |
| 3+ | 32 | 22.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **108** | avg margin: **1.6** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 68 | 63.0% |
| 2 | 24 | 22.2% |
| 3+ | 16 | 14.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 143 | 1-0 | 45 | 31.5% |
| draw | 91 | 1-1 | 40 | 44.0% |
| away | 108 | 1-2 | 31 | 28.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda1\charts\scoreline_analysis_total_goals.png)

