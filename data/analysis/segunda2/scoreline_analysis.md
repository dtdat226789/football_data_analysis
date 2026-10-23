# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:07:07+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 2 (Spain)
- Scope: league `segunda2`

## 1. Scoreline frequency
- Matches analysed: **342** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 49 | 14.3% |
| 0-1 | 33 | 9.6% |
| 1-0 | 33 | 9.6% |
| 0-0 | 32 | 9.4% |
| 2-0 | 26 | 7.6% |
| 1-2 | 26 | 7.6% |
| 2-1 | 21 | 6.1% |
| 3-1 | 17 | 5.0% |
| 2-2 | 14 | 4.1% |
| 0-2 | 12 | 3.5% |
| 3-2 | 12 | 3.5% |
| 1-3 | 11 | 3.2% |
| 4-0 | 10 | 2.9% |
| 3-0 | 9 | 2.6% |
| 4-1 | 7 | 2.0% |
| 0-3 | 5 | 1.5% |
| 2-3 | 4 | 1.2% |
| 0-4 | 4 | 1.2% |
| 5-0 | 4 | 1.2% |
| 5-1 | 3 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 15.4% |
| 1-0 | 30 | 9.8% |
| 0-0 | 28 | 9.2% |
| 0-1 | 27 | 8.8% |
| 2-0 | 24 | 7.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 6 | 16.7% |
| 0-0 | 4 | 11.1% |
| 1-2 | 3 | 8.3% |
| 5-0 | 3 | 8.3% |
| 1-0 | 3 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.4% |
| 1 | 66 | 19.3% |
| 2 | 87 | 25.4% |
| 3 | 61 | 17.8% |
| 4 | 56 | 16.4% |
| 5 | 29 | 8.5% |
| 6 | 8 | 2.3% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.3% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-03-29 | 6-4 | 10 |
| 2025-2026 | 2025-09-14 | 4-3 | 7 |
| 2026-2027 | 2026-09-06 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **245** (draws: **97**)
- Average winning margin: **1.77**

| margin | matches | pct |
|---|---|---|
| 1 | 131 | 53.5% |
| 2 | 68 | 27.8% |
| 3+ | 46 | 18.8% |

## 6. Margin by outcome

### Home wins
- Matches: **146** | avg margin: **1.93** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 68 | 46.6% |
| 2 | 44 | 30.1% |
| 3+ | 34 | 23.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **99** | avg margin: **1.54** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 63 | 63.6% |
| 2 | 24 | 24.2% |
| 3+ | 12 | 12.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 146 | 1-0 | 33 | 22.6% |
| draw | 97 | 1-1 | 49 | 50.5% |
| away | 99 | 0-1 | 33 | 33.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda2\charts\scoreline_analysis_total_goals.png)

