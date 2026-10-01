# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:48:51+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: League One (England)
- Scope: league `eng1`

## 1. Scoreline frequency
- Matches analysed: **644** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 80 | 12.4% |
| 1-0 | 78 | 12.1% |
| 2-1 | 61 | 9.5% |
| 0-1 | 54 | 8.4% |
| 1-2 | 45 | 7.0% |
| 0-0 | 41 | 6.4% |
| 2-2 | 39 | 6.1% |
| 2-0 | 34 | 5.3% |
| 3-0 | 29 | 4.5% |
| 0-2 | 28 | 4.3% |
| 3-1 | 24 | 3.7% |
| 1-3 | 20 | 3.1% |
| 3-2 | 19 | 3.0% |
| 2-3 | 11 | 1.7% |
| 4-0 | 11 | 1.7% |
| 0-3 | 11 | 1.7% |
| 4-1 | 9 | 1.4% |
| 0-4 | 9 | 1.4% |
| 3-3 | 8 | 1.2% |
| 5-0 | 5 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 73 | 13.1% |
| 1-1 | 67 | 12.0% |
| 2-1 | 54 | 9.7% |
| 0-1 | 48 | 8.6% |
| 1-2 | 37 | 6.6% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 13 | 14.9% |
| 1-2 | 8 | 9.2% |
| 0-0 | 8 | 9.2% |
| 2-2 | 7 | 8.0% |
| 2-1 | 7 | 8.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 41 | 6.4% |
| 1 | 132 | 20.5% |
| 2 | 142 | 22.0% |
| 3 | 146 | 22.7% |
| 4 | 103 | 16.0% |
| 5 | 48 | 7.5% |
| 6 | 21 | 3.3% |
| 7 | 9 | 1.4% |
| 8 | 0 | 0.0% |
| 9 | 2 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-05-02 | 5-4 | 9 |
| 2026-2027 | 2026-08-29 | 7-2 | 9 |
| 2025-2026 | 2025-10-04 | 4-3 | 7 |
| 2025-2026 | 2025-12-13 | 4-3 | 7 |
| 2025-2026 | 2026-01-04 | 5-2 | 7 |
| 2025-2026 | 2026-02-07 | 6-1 | 7 |
| 2025-2026 | 2026-02-21 | 5-2 | 7 |
| 2025-2026 | 2026-04-25 | 4-3 | 7 |
| 2026-2027 | 2026-08-15 | 3-4 | 7 |
| 2026-2027 | 2026-08-30 | 5-2 | 7 |
| 2026-2027 | 2026-09-12 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **476** (draws: **168**)
- Average winning margin: **1.71**

| margin | matches | pct |
|---|---|---|
| 1 | 274 | 57.6% |
| 2 | 111 | 23.3% |
| 3+ | 91 | 19.1% |

## 6. Margin by outcome

### Home wins
- Matches: **287** | avg margin: **1.76** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 162 | 56.4% |
| 2 | 61 | 21.3% |
| 3+ | 64 | 22.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **189** | avg margin: **1.62** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 112 | 59.3% |
| 2 | 50 | 26.5% |
| 3+ | 27 | 14.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 287 | 1-0 | 78 | 27.2% |
| draw | 168 | 1-1 | 80 | 47.6% |
| away | 189 | 0-1 | 54 | 28.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\eng1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\eng1\charts\scoreline_analysis_total_goals.png)

