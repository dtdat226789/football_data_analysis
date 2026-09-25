# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:43:32+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Scoreline frequency
- Matches analysed: **320** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 48 | 15.0% |
| 1-0 | 33 | 10.3% |
| 2-1 | 32 | 10.0% |
| 2-0 | 27 | 8.4% |
| 0-1 | 27 | 8.4% |
| 0-0 | 21 | 6.6% |
| 1-2 | 21 | 6.6% |
| 2-2 | 20 | 6.2% |
| 3-1 | 13 | 4.1% |
| 3-0 | 12 | 3.8% |
| 0-2 | 10 | 3.1% |
| 1-3 | 9 | 2.8% |
| 0-3 | 8 | 2.5% |
| 3-2 | 7 | 2.2% |
| 2-3 | 5 | 1.6% |
| 3-3 | 4 | 1.2% |
| 1-4 | 3 | 0.9% |
| 5-1 | 3 | 0.9% |
| 4-0 | 3 | 0.9% |
| 2-4 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 14.8% |
| 1-0 | 28 | 11.5% |
| 2-1 | 25 | 10.2% |
| 2-0 | 24 | 9.8% |
| 0-1 | 23 | 9.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 12 | 15.8% |
| 1-2 | 8 | 10.5% |
| 2-1 | 7 | 9.2% |
| 0-0 | 6 | 7.9% |
| 2-2 | 6 | 7.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 21 | 6.6% |
| 1 | 60 | 18.8% |
| 2 | 85 | 26.6% |
| 3 | 73 | 22.8% |
| 4 | 46 | 14.4% |
| 5 | 20 | 6.2% |
| 6 | 12 | 3.8% |
| 7 | 2 | 0.6% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-04 | 3-5 | 8 |
| 2025-2026 | 2025-09-27 | 5-2 | 7 |
| 2025-2026 | 2026-03-09 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **227** (draws: **93**)
- Average winning margin: **1.68**

| margin | matches | pct |
|---|---|---|
| 1 | 126 | 55.5% |
| 2 | 64 | 28.2% |
| 3+ | 37 | 16.3% |

## 6. Margin by outcome

### Home wins
- Matches: **137** | avg margin: **1.71** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 73 | 53.3% |
| 2 | 41 | 29.9% |
| 3+ | 23 | 16.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **90** | avg margin: **1.63** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 58.9% |
| 2 | 23 | 25.6% |
| 3+ | 14 | 15.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 137 | 1-0 | 33 | 24.1% |
| draw | 93 | 1-1 | 48 | 51.6% |
| away | 90 | 0-1 | 27 | 30.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\russia\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\russia\charts\scoreline_analysis_total_goals.png)

