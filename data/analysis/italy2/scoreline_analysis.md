# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:57:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Scoreline frequency
- Matches analysed: **440** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 69 | 15.7% |
| 1-0 | 49 | 11.1% |
| 2-1 | 39 | 8.9% |
| 2-0 | 32 | 7.3% |
| 1-2 | 32 | 7.3% |
| 0-0 | 31 | 7.0% |
| 2-2 | 30 | 6.8% |
| 0-1 | 28 | 6.4% |
| 3-1 | 24 | 5.5% |
| 3-0 | 23 | 5.2% |
| 0-2 | 16 | 3.6% |
| 1-3 | 12 | 2.7% |
| 3-2 | 11 | 2.5% |
| 0-3 | 9 | 2.0% |
| 5-0 | 5 | 1.1% |
| 4-0 | 4 | 0.9% |
| 4-1 | 4 | 0.9% |
| 3-3 | 4 | 0.9% |
| 2-3 | 4 | 0.9% |
| 0-4 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 60 | 15.4% |
| 1-0 | 43 | 11.0% |
| 2-1 | 34 | 8.7% |
| 2-0 | 30 | 7.7% |
| 0-0 | 30 | 7.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 9 | 18.0% |
| 1-0 | 6 | 12.0% |
| 1-2 | 6 | 12.0% |
| 0-1 | 5 | 10.0% |
| 3-1 | 5 | 10.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.0% |
| 1 | 77 | 17.5% |
| 2 | 117 | 26.6% |
| 3 | 103 | 23.4% |
| 4 | 73 | 16.6% |
| 5 | 26 | 5.9% |
| 6 | 8 | 1.8% |
| 7 | 5 | 1.1% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-09-21 | 3-4 | 7 |
| 2025-2026 | 2025-11-01 | 4-3 | 7 |
| 2025-2026 | 2026-01-24 | 2-5 | 7 |
| 2025-2026 | 2026-04-18 | 6-1 | 7 |
| 2025-2026 | 2026-05-08 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **306** (draws: **134**)
- Average winning margin: **1.7**

| margin | matches | pct |
|---|---|---|
| 1 | 166 | 54.2% |
| 2 | 87 | 28.4% |
| 3+ | 53 | 17.3% |

## 6. Margin by outcome

### Home wins
- Matches: **196** | avg margin: **1.76** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 100 | 51.0% |
| 2 | 59 | 30.1% |
| 3+ | 37 | 18.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **110** | avg margin: **1.58** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 66 | 60.0% |
| 2 | 28 | 25.5% |
| 3+ | 16 | 14.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 196 | 1-0 | 49 | 25.0% |
| draw | 134 | 1-1 | 69 | 51.5% |
| away | 110 | 1-2 | 32 | 29.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy2\charts\scoreline_analysis_total_goals.png)

