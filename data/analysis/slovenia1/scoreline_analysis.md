# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:47:20+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Prva liga (Slovenia)
- Scope: league `slovenia1`

## 1. Scoreline frequency
- Matches analysed: **216** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 25 | 11.6% |
| 1-1 | 19 | 8.8% |
| 1-0 | 18 | 8.3% |
| 1-2 | 17 | 7.9% |
| 2-0 | 14 | 6.5% |
| 0-0 | 14 | 6.5% |
| 3-0 | 13 | 6.0% |
| 0-2 | 13 | 6.0% |
| 1-3 | 11 | 5.1% |
| 3-1 | 9 | 4.2% |
| 2-2 | 8 | 3.7% |
| 2-3 | 8 | 3.7% |
| 0-3 | 7 | 3.2% |
| 0-1 | 7 | 3.2% |
| 3-2 | 6 | 2.8% |
| 3-3 | 5 | 2.3% |
| 4-1 | 5 | 2.3% |
| 5-1 | 3 | 1.4% |
| 0-4 | 3 | 1.4% |
| 0-5 | 2 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 22 | 13.4% |
| 1-2 | 14 | 8.5% |
| 1-0 | 14 | 8.5% |
| 1-1 | 12 | 7.3% |
| 2-0 | 11 | 6.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 7 | 13.5% |
| 0-0 | 6 | 11.5% |
| 0-2 | 4 | 7.7% |
| 1-0 | 4 | 7.7% |
| 1-3 | 4 | 7.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.5% |
| 1 | 25 | 11.6% |
| 2 | 46 | 21.3% |
| 3 | 62 | 28.7% |
| 4 | 32 | 14.8% |
| 5 | 22 | 10.2% |
| 6 | 12 | 5.6% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.5% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-31 | 6-2 | 8 |
| 2026-2027 | 2026-08-01 | 5-2 | 7 |
| 2026-2027 | 2026-09-13 | 1-6 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **170** (draws: **46**)
- Average winning margin: **1.86**

| margin | matches | pct |
|---|---|---|
| 1 | 81 | 47.6% |
| 2 | 50 | 29.4% |
| 3+ | 39 | 22.9% |

## 6. Margin by outcome

### Home wins
- Matches: **99** | avg margin: **1.83** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 49 | 49.5% |
| 2 | 25 | 25.3% |
| 3+ | 25 | 25.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **71** | avg margin: **1.92** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 32 | 45.1% |
| 2 | 25 | 35.2% |
| 3+ | 14 | 19.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 99 | 2-1 | 25 | 25.3% |
| draw | 46 | 1-1 | 19 | 41.3% |
| away | 71 | 1-2 | 17 | 23.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\slovenia1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\slovenia1\charts\scoreline_analysis_total_goals.png)

