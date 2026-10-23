# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:45:44+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie B (Brazil)
- Scope: league `brazil2`

## 1. Scoreline frequency
- Matches analysed: **679** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 98 | 14.4% |
| 1-1 | 97 | 14.3% |
| 2-1 | 81 | 11.9% |
| 0-1 | 61 | 9.0% |
| 2-0 | 60 | 8.8% |
| 0-0 | 59 | 8.7% |
| 1-2 | 49 | 7.2% |
| 2-2 | 37 | 5.4% |
| 3-0 | 25 | 3.7% |
| 0-2 | 23 | 3.4% |
| 3-1 | 16 | 2.4% |
| 1-3 | 16 | 2.4% |
| 4-0 | 8 | 1.2% |
| 0-3 | 7 | 1.0% |
| 3-2 | 7 | 1.0% |
| 4-2 | 6 | 0.9% |
| 2-3 | 6 | 0.9% |
| 1-4 | 5 | 0.7% |
| 3-3 | 5 | 0.7% |
| 5-0 | 3 | 0.4% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-0 | 60 | 15.8% |
| 1-1 | 57 | 15.0% |
| 2-1 | 44 | 11.6% |
| 2-0 | 37 | 9.7% |
| 0-0 | 33 | 8.7% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 40 | 13.4% |
| 1-0 | 38 | 12.7% |
| 2-1 | 37 | 12.4% |
| 0-1 | 29 | 9.7% |
| 0-0 | 26 | 8.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 59 | 8.7% |
| 1 | 159 | 23.4% |
| 2 | 180 | 26.5% |
| 3 | 162 | 23.9% |
| 4 | 79 | 11.6% |
| 5 | 22 | 3.2% |
| 6 | 14 | 2.1% |
| 7 | 3 | 0.4% |
| 8 | 1 | 0.1% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-05-16 | 2-6 | 8 |
| 2025 | 2025-07-19 | 2-5 | 7 |
| 2026 | 2026-06-20 | 4-3 | 7 |
| 2026 | 2026-07-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **481** (draws: **198**)
- Average winning margin: **1.53**

| margin | matches | pct |
|---|---|---|
| 1 | 304 | 63.2% |
| 2 | 122 | 25.4% |
| 3+ | 55 | 11.4% |

## 6. Margin by outcome

### Home wins
- Matches: **308** | avg margin: **1.58** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 187 | 60.7% |
| 2 | 82 | 26.6% |
| 3+ | 39 | 12.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **173** | avg margin: **1.43** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 117 | 67.6% |
| 2 | 40 | 23.1% |
| 3+ | 16 | 9.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 308 | 1-0 | 98 | 31.8% |
| draw | 198 | 1-1 | 97 | 49.0% |
| away | 173 | 0-1 | 61 | 35.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\brazil2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\brazil2\charts\scoreline_analysis_total_goals.png)

