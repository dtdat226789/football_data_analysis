# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:00+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: K League 2 (South Korea)
- Scope: league `korea2`

## 1. Scoreline frequency
- Matches analysed: **493** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 64 | 13.0% |
| 0-1 | 56 | 11.4% |
| 0-0 | 42 | 8.5% |
| 2-2 | 42 | 8.5% |
| 1-0 | 41 | 8.3% |
| 2-1 | 36 | 7.3% |
| 1-2 | 35 | 7.1% |
| 2-0 | 29 | 5.9% |
| 0-2 | 24 | 4.9% |
| 1-3 | 17 | 3.4% |
| 3-1 | 16 | 3.2% |
| 3-0 | 15 | 3.0% |
| 3-2 | 13 | 2.6% |
| 2-3 | 12 | 2.4% |
| 0-3 | 9 | 1.8% |
| 1-4 | 8 | 1.6% |
| 4-1 | 7 | 1.4% |
| 4-2 | 5 | 1.0% |
| 3-3 | 5 | 1.0% |
| 4-0 | 3 | 0.6% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 0-1 | 35 | 12.8% |
| 1-1 | 33 | 12.1% |
| 0-0 | 26 | 9.5% |
| 1-0 | 22 | 8.1% |
| 2-1 | 20 | 7.3% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 14.1% |
| 2-2 | 24 | 10.9% |
| 0-1 | 21 | 9.5% |
| 1-0 | 19 | 8.6% |
| 1-2 | 18 | 8.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 42 | 8.5% |
| 1 | 97 | 19.7% |
| 2 | 117 | 23.7% |
| 3 | 95 | 19.3% |
| 4 | 79 | 16.0% |
| 5 | 43 | 8.7% |
| 6 | 14 | 2.8% |
| 7 | 5 | 1.0% |
| 8 | 1 | 0.2% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-07-20 | 5-3 | 8 |
| 2025 | 2025-07-19 | 3-4 | 7 |
| 2025 | 2025-08-10 | 3-4 | 7 |
| 2025 | 2025-08-31 | 2-5 | 7 |
| 2025 | 2025-09-13 | 3-4 | 7 |
| 2026 | 2026-07-24 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **340** (draws: **153**)
- Average winning margin: **1.62**

| margin | matches | pct |
|---|---|---|
| 1 | 197 | 57.9% |
| 2 | 92 | 27.1% |
| 3+ | 51 | 15.0% |

## 6. Margin by outcome

### Home wins
- Matches: **173** | avg margin: **1.73** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 91 | 52.6% |
| 2 | 51 | 29.5% |
| 3+ | 31 | 17.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **167** | avg margin: **1.5** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 106 | 63.5% |
| 2 | 41 | 24.6% |
| 3+ | 20 | 12.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 173 | 1-0 | 41 | 23.7% |
| draw | 153 | 1-1 | 64 | 41.8% |
| away | 167 | 0-1 | 56 | 33.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\korea2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\korea2\charts\scoreline_analysis_total_goals.png)

