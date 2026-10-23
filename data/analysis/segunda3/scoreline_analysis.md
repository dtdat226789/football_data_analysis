# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:07:23+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Scoreline frequency
- Matches analysed: **346** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 60 | 17.3% |
| 1-1 | 49 | 14.2% |
| 0-0 | 35 | 10.1% |
| 2-1 | 28 | 8.1% |
| 1-2 | 28 | 8.1% |
| 0-1 | 23 | 6.6% |
| 2-0 | 22 | 6.4% |
| 2-2 | 19 | 5.5% |
| 3-1 | 11 | 3.2% |
| 3-0 | 10 | 2.9% |
| 0-2 | 10 | 2.9% |
| 3-2 | 8 | 2.3% |
| 1-3 | 6 | 1.7% |
| 4-1 | 5 | 1.4% |
| 4-0 | 4 | 1.2% |
| 4-2 | 4 | 1.2% |
| 1-4 | 4 | 1.2% |
| 5-1 | 4 | 1.2% |
| 2-4 | 3 | 0.9% |
| 3-3 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 49 | 16.0% |
| 1-1 | 43 | 14.1% |
| 0-0 | 33 | 10.8% |
| 2-1 | 26 | 8.5% |
| 0-1 | 21 | 6.9% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 11 | 27.5% |
| 1-2 | 7 | 17.5% |
| 1-1 | 6 | 15.0% |
| 2-0 | 3 | 7.5% |
| 2-1 | 2 | 5.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 35 | 10.1% |
| 1 | 83 | 24.0% |
| 2 | 81 | 23.4% |
| 3 | 68 | 19.7% |
| 4 | 41 | 11.8% |
| 5 | 20 | 5.8% |
| 6 | 15 | 4.3% |
| 7 | 0 | 0.0% |
| 8 | 2 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-12-14 | 7-3 | 10 |
| 2025-2026 | 2025-12-21 | 4-4 | 8 |
| 2025-2026 | 2026-04-05 | 5-3 | 8 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **239** (draws: **107**)
- Average winning margin: **1.55**

| margin | matches | pct |
|---|---|---|
| 1 | 150 | 62.8% |
| 2 | 57 | 23.8% |
| 3+ | 32 | 13.4% |

## 6. Margin by outcome

### Home wins
- Matches: **158** | avg margin: **1.6** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 96 | 60.8% |
| 2 | 38 | 24.1% |
| 3+ | 24 | 15.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **81** | avg margin: **1.46** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 54 | 66.7% |
| 2 | 19 | 23.5% |
| 3+ | 8 | 9.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 158 | 1-0 | 60 | 38.0% |
| draw | 107 | 1-1 | 49 | 45.8% |
| away | 81 | 1-2 | 28 | 34.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda3\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda3\charts\scoreline_analysis_total_goals.png)

