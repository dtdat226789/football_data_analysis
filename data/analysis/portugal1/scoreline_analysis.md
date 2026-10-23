# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:03:32+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Scoreline frequency
- Matches analysed: **370** across **2** seasons.
- Distinct scorelines seen: **29**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 36 | 9.7% |
| 2-2 | 35 | 9.5% |
| 0-1 | 34 | 9.2% |
| 1-0 | 34 | 9.2% |
| 1-2 | 30 | 8.1% |
| 0-0 | 25 | 6.8% |
| 2-1 | 24 | 6.5% |
| 2-0 | 24 | 6.5% |
| 3-1 | 19 | 5.1% |
| 3-0 | 19 | 5.1% |
| 0-2 | 18 | 4.9% |
| 4-0 | 11 | 3.0% |
| 0-3 | 10 | 2.7% |
| 0-4 | 9 | 2.4% |
| 3-2 | 8 | 2.2% |
| 3-3 | 6 | 1.6% |
| 1-4 | 5 | 1.4% |
| 1-3 | 5 | 1.4% |
| 5-0 | 4 | 1.1% |
| 6-0 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 10.1% |
| 0-1 | 30 | 9.7% |
| 2-2 | 27 | 8.8% |
| 1-0 | 27 | 8.8% |
| 1-2 | 26 | 8.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 8 | 12.9% |
| 1-0 | 7 | 11.3% |
| 1-1 | 5 | 8.1% |
| 2-0 | 5 | 8.1% |
| 2-1 | 5 | 8.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 25 | 6.8% |
| 1 | 68 | 18.4% |
| 2 | 78 | 21.1% |
| 3 | 83 | 22.4% |
| 4 | 79 | 21.4% |
| 5 | 22 | 5.9% |
| 6 | 12 | 3.2% |
| 7 | 2 | 0.5% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-01 | 3-5 | 8 |
| 2025-2026 | 2025-11-07 | 4-3 | 7 |
| 2026-2027 | 2026-08-17 | 0-7 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **268** (draws: **102**)
- Average winning margin: **1.9**

| margin | matches | pct |
|---|---|---|
| 1 | 133 | 49.6% |
| 2 | 70 | 26.1% |
| 3+ | 65 | 24.3% |

## 6. Margin by outcome

### Home wins
- Matches: **151** | avg margin: **1.99** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 67 | 44.4% |
| 2 | 45 | 29.8% |
| 3+ | 39 | 25.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **117** | avg margin: **1.79** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 66 | 56.4% |
| 2 | 25 | 21.4% |
| 3+ | 26 | 22.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 151 | 1-0 | 34 | 22.5% |
| draw | 102 | 1-1 | 36 | 35.3% |
| away | 117 | 0-1 | 34 | 29.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\portugal1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\portugal1\charts\scoreline_analysis_total_goals.png)

