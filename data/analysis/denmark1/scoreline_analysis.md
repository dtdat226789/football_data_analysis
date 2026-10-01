# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:47:55+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

## 1. Scoreline frequency
- Matches analysed: **248** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 27 | 10.9% |
| 2-1 | 25 | 10.1% |
| 1-0 | 22 | 8.9% |
| 1-2 | 21 | 8.5% |
| 0-2 | 17 | 6.9% |
| 2-0 | 14 | 5.6% |
| 2-2 | 14 | 5.6% |
| 0-0 | 12 | 4.8% |
| 2-3 | 10 | 4.0% |
| 0-1 | 9 | 3.6% |
| 3-3 | 8 | 3.2% |
| 3-1 | 8 | 3.2% |
| 3-2 | 8 | 3.2% |
| 3-0 | 6 | 2.4% |
| 1-3 | 6 | 2.4% |
| 0-3 | 6 | 2.4% |
| 0-4 | 5 | 2.0% |
| 4-1 | 4 | 1.6% |
| 1-4 | 4 | 1.6% |
| 4-2 | 3 | 1.2% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 21 | 10.9% |
| 1-2 | 19 | 9.8% |
| 1-1 | 18 | 9.3% |
| 1-0 | 15 | 7.8% |
| 0-2 | 14 | 7.3% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 9 | 16.4% |
| 1-0 | 7 | 12.7% |
| 2-2 | 6 | 10.9% |
| 2-1 | 4 | 7.3% |
| 2-0 | 4 | 7.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 12 | 4.8% |
| 1 | 31 | 12.5% |
| 2 | 58 | 23.4% |
| 3 | 58 | 23.4% |
| 4 | 35 | 14.1% |
| 5 | 30 | 12.1% |
| 6 | 18 | 7.3% |
| 7 | 4 | 1.6% |
| 8 | 2 | 0.8% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-07-28 | 6-2 | 8 |
| 2025-2026 | 2026-05-17 | 6-2 | 8 |
| 2025-2026 | 2025-11-23 | 5-2 | 7 |
| 2025-2026 | 2026-02-22 | 5-2 | 7 |
| 2025-2026 | 2026-04-05 | 7-0 | 7 |
| 2026-2027 | 2026-09-06 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **187** (draws: **61**)
- Average winning margin: **1.89**

| margin | matches | pct |
|---|---|---|
| 1 | 95 | 50.8% |
| 2 | 49 | 26.2% |
| 3+ | 43 | 23.0% |

## 6. Margin by outcome

### Home wins
- Matches: **104** | avg margin: **1.91** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 55 | 52.9% |
| 2 | 25 | 24.0% |
| 3+ | 24 | 23.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **83** | avg margin: **1.86** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 40 | 48.2% |
| 2 | 24 | 28.9% |
| 3+ | 19 | 22.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 104 | 2-1 | 25 | 24.0% |
| draw | 61 | 1-1 | 27 | 44.3% |
| away | 83 | 1-2 | 21 | 25.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\denmark1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\denmark1\charts\scoreline_analysis_total_goals.png)

