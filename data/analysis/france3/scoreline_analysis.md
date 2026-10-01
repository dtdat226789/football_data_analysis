# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:50:33+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Scoreline frequency
- Matches analysed: **388** across **2** seasons.
- Distinct scorelines seen: **26**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 61 | 15.7% |
| 0-0 | 42 | 10.8% |
| 1-2 | 35 | 9.0% |
| 1-0 | 34 | 8.8% |
| 2-1 | 32 | 8.2% |
| 0-1 | 26 | 6.7% |
| 2-0 | 24 | 6.2% |
| 2-2 | 21 | 5.4% |
| 0-3 | 19 | 4.9% |
| 0-2 | 18 | 4.6% |
| 3-0 | 16 | 4.1% |
| 3-1 | 12 | 3.1% |
| 1-3 | 9 | 2.3% |
| 3-2 | 8 | 2.1% |
| 2-3 | 6 | 1.5% |
| 4-1 | 4 | 1.0% |
| 4-0 | 4 | 1.0% |
| 1-4 | 4 | 1.0% |
| 0-4 | 3 | 0.8% |
| 6-1 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 46 | 15.2% |
| 0-0 | 32 | 10.6% |
| 1-0 | 28 | 9.2% |
| 1-2 | 27 | 8.9% |
| 2-1 | 27 | 8.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 15 | 17.6% |
| 0-0 | 10 | 11.8% |
| 2-0 | 8 | 9.4% |
| 1-2 | 8 | 9.4% |
| 0-2 | 7 | 8.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 42 | 10.8% |
| 1 | 60 | 15.5% |
| 2 | 103 | 26.5% |
| 3 | 102 | 26.3% |
| 4 | 49 | 12.6% |
| 5 | 23 | 5.9% |
| 6 | 4 | 1.0% |
| 7 | 4 | 1.0% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-10 | 3-5 | 8 |
| 2026-2027 | 2026-08-14 | 4-3 | 7 |
| 2026-2027 | 2026-09-05 | 6-1 | 7 |
| 2026-2027 | 2026-09-05 | 6-1 | 7 |
| 2026-2027 | 2026-09-05 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **262** (draws: **126**)
- Average winning margin: **1.72**

| margin | matches | pct |
|---|---|---|
| 1 | 142 | 54.2% |
| 2 | 66 | 25.2% |
| 3+ | 54 | 20.6% |

## 6. Margin by outcome

### Home wins
- Matches: **140** | avg margin: **1.75** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 75 | 53.6% |
| 2 | 37 | 26.4% |
| 3+ | 28 | 20.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **122** | avg margin: **1.69** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 54.9% |
| 2 | 29 | 23.8% |
| 3+ | 26 | 21.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 140 | 1-0 | 34 | 24.3% |
| draw | 126 | 1-1 | 61 | 48.4% |
| away | 122 | 1-2 | 35 | 28.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\france3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\france3\charts\scoreline_analysis_total_goals.png)

