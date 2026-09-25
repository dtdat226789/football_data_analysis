# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:44:57+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Scoreline frequency
- Matches analysed: **230** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 34 | 14.8% |
| 2-1 | 21 | 9.1% |
| 1-0 | 20 | 8.7% |
| 0-2 | 17 | 7.4% |
| 0-1 | 16 | 7.0% |
| 3-1 | 15 | 6.5% |
| 1-2 | 14 | 6.1% |
| 0-0 | 14 | 6.1% |
| 2-0 | 12 | 5.2% |
| 2-2 | 12 | 5.2% |
| 3-0 | 12 | 5.2% |
| 0-3 | 6 | 2.6% |
| 4-0 | 6 | 2.6% |
| 4-1 | 5 | 2.2% |
| 0-4 | 4 | 1.7% |
| 1-3 | 4 | 1.7% |
| 1-4 | 3 | 1.3% |
| 3-2 | 3 | 1.3% |
| 2-3 | 3 | 1.3% |
| 3-3 | 1 | 0.4% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 30 | 15.7% |
| 1-0 | 17 | 8.9% |
| 2-1 | 16 | 8.4% |
| 0-2 | 15 | 7.9% |
| 3-1 | 14 | 7.3% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 5 | 12.8% |
| 0-0 | 4 | 10.3% |
| 1-1 | 4 | 10.3% |
| 3-0 | 4 | 10.3% |
| 0-1 | 3 | 7.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.1% |
| 1 | 36 | 15.7% |
| 2 | 63 | 27.4% |
| 3 | 53 | 23.0% |
| 4 | 41 | 17.8% |
| 5 | 16 | 7.0% |
| 6 | 3 | 1.3% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.4% |
| 9 | 1 | 0.4% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-03-14 | 5-4 | 9 |
| 2026-2027 | 2026-09-15 | 8-0 | 8 |
| 2025-2026 | 2025-12-20 | 2-5 | 7 |
| 2025-2026 | 2026-05-15 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **169** (draws: **61**)
- Average winning margin: **1.91**

| margin | matches | pct |
|---|---|---|
| 1 | 79 | 46.7% |
| 2 | 48 | 28.4% |
| 3+ | 42 | 24.9% |

## 6. Margin by outcome

### Home wins
- Matches: **99** | avg margin: **1.94** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 46 | 46.5% |
| 2 | 27 | 27.3% |
| 3+ | 26 | 26.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **70** | avg margin: **1.86** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 33 | 47.1% |
| 2 | 21 | 30.0% |
| 3+ | 16 | 22.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 99 | 2-1 | 21 | 21.2% |
| draw | 61 | 1-1 | 34 | 55.7% |
| away | 70 | 0-2 | 17 | 24.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\scot1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\scot1\charts\scoreline_analysis_total_goals.png)

