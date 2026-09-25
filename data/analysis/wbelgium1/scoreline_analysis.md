# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:50:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Scoreline frequency
- Matches analysed: **120** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 2-0 | 15 | 12.5% |
| 2-1 | 14 | 11.7% |
| 1-1 | 12 | 10.0% |
| 0-2 | 8 | 6.7% |
| 1-2 | 8 | 6.7% |
| 0-0 | 7 | 5.8% |
| 1-0 | 7 | 5.8% |
| 1-3 | 6 | 5.0% |
| 2-2 | 5 | 4.2% |
| 4-1 | 4 | 3.3% |
| 0-3 | 4 | 3.3% |
| 0-1 | 4 | 3.3% |
| 1-5 | 3 | 2.5% |
| 2-3 | 3 | 2.5% |
| 4-2 | 3 | 2.5% |
| 3-0 | 3 | 2.5% |
| 0-5 | 2 | 1.7% |
| 3-3 | 2 | 1.7% |
| 3-2 | 2 | 1.7% |
| 1-4 | 1 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-0 | 14 | 13.0% |
| 2-1 | 14 | 13.0% |
| 1-1 | 12 | 11.1% |
| 0-2 | 7 | 6.5% |
| 1-2 | 7 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 3 | 25.0% |
| 3-1 | 1 | 8.3% |
| 4-0 | 1 | 8.3% |
| 6-1 | 1 | 8.3% |
| 0-0 | 1 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 7 | 5.8% |
| 1 | 11 | 9.2% |
| 2 | 35 | 29.2% |
| 3 | 29 | 24.2% |
| 4 | 14 | 11.7% |
| 5 | 12 | 10.0% |
| 6 | 9 | 7.5% |
| 7 | 3 | 2.5% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-12-20 | 1-6 | 7 |
| 2025-2026 | 2026-01-31 | 3-4 | 7 |
| 2026-2027 | 2026-09-06 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **94** (draws: **26**)
- Average winning margin: **1.99**

| margin | matches | pct |
|---|---|---|
| 1 | 39 | 41.5% |
| 2 | 33 | 35.1% |
| 3+ | 22 | 23.4% |

## 6. Margin by outcome

### Home wins
- Matches: **52** | avg margin: **1.87** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 23 | 44.2% |
| 2 | 19 | 36.5% |
| 3+ | 10 | 19.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **42** | avg margin: **2.14** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 16 | 38.1% |
| 2 | 14 | 33.3% |
| 3+ | 12 | 28.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 52 | 2-0 | 15 | 28.8% |
| draw | 26 | 1-1 | 12 | 46.2% |
| away | 42 | 0-2 | 8 | 19.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\wbelgium1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\wbelgium1\charts\scoreline_analysis_total_goals.png)

