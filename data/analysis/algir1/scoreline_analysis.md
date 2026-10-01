# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:43:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ligue 1 (Algeria)
- Scope: league `algir1`

## 1. Scoreline frequency
- Matches analysed: **263** across **2** seasons.
- Distinct scorelines seen: **26**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 49 | 18.6% |
| 1-1 | 38 | 14.4% |
| 2-1 | 25 | 9.5% |
| 2-0 | 23 | 8.7% |
| 0-0 | 22 | 8.4% |
| 0-1 | 22 | 8.4% |
| 2-2 | 16 | 6.1% |
| 1-2 | 15 | 5.7% |
| 3-1 | 9 | 3.4% |
| 0-2 | 8 | 3.0% |
| 3-0 | 8 | 3.0% |
| 3-2 | 7 | 2.7% |
| 2-3 | 3 | 1.1% |
| 1-3 | 2 | 0.8% |
| 4-1 | 2 | 0.8% |
| 0-3 | 2 | 0.8% |
| 5-1 | 2 | 0.8% |
| 3-3 | 2 | 0.8% |
| 3-5 | 1 | 0.4% |
| 4-3 | 1 | 0.4% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 46 | 19.2% |
| 1-1 | 35 | 14.6% |
| 2-1 | 25 | 10.4% |
| 0-0 | 20 | 8.3% |
| 2-0 | 19 | 7.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-0 | 4 | 17.4% |
| 0-1 | 3 | 13.0% |
| 1-0 | 3 | 13.0% |
| 1-1 | 3 | 13.0% |
| 0-0 | 2 | 8.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 22 | 8.4% |
| 1 | 71 | 27.0% |
| 2 | 69 | 26.2% |
| 3 | 50 | 19.0% |
| 4 | 29 | 11.0% |
| 5 | 13 | 4.9% |
| 6 | 5 | 1.9% |
| 7 | 2 | 0.8% |
| 8 | 2 | 0.8% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-14 | 3-5 | 8 |
| 2025-2026 | 2026-05-07 | 5-3 | 8 |
| 2025-2026 | 2026-02-21 | 4-3 | 7 |
| 2025-2026 | 2026-04-05 | 7-0 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **185** (draws: **78**)
- Average winning margin: **1.49**

| margin | matches | pct |
|---|---|---|
| 1 | 122 | 65.9% |
| 2 | 45 | 24.3% |
| 3+ | 18 | 9.7% |

## 6. Margin by outcome

### Home wins
- Matches: **130** | avg margin: **1.53** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 82 | 63.1% |
| 2 | 34 | 26.2% |
| 3+ | 14 | 10.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **55** | avg margin: **1.4** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 40 | 72.7% |
| 2 | 11 | 20.0% |
| 3+ | 4 | 7.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 130 | 1-0 | 49 | 37.7% |
| draw | 78 | 1-1 | 38 | 48.7% |
| away | 55 | 0-1 | 22 | 40.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\algir1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\algir1\charts\scoreline_analysis_total_goals.png)

