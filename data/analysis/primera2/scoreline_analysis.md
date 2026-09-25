# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:42:55+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Scoreline frequency
- Matches analysed: **419** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 57 | 13.6% |
| 0-0 | 50 | 11.9% |
| 1-1 | 46 | 11.0% |
| 2-0 | 42 | 10.0% |
| 0-1 | 38 | 9.1% |
| 2-1 | 37 | 8.8% |
| 2-2 | 25 | 6.0% |
| 1-2 | 21 | 5.0% |
| 3-0 | 17 | 4.1% |
| 0-2 | 16 | 3.8% |
| 3-1 | 14 | 3.3% |
| 3-2 | 9 | 2.1% |
| 1-3 | 8 | 1.9% |
| 0-3 | 7 | 1.7% |
| 4-0 | 6 | 1.4% |
| 2-3 | 5 | 1.2% |
| 1-4 | 5 | 1.2% |
| 3-3 | 3 | 0.7% |
| 4-1 | 3 | 0.7% |
| 4-2 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 52 | 13.7% |
| 0-0 | 46 | 12.1% |
| 1-1 | 43 | 11.3% |
| 0-1 | 37 | 9.7% |
| 2-0 | 37 | 9.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 5 | 12.8% |
| 2-0 | 5 | 12.8% |
| 2-2 | 4 | 10.3% |
| 0-0 | 4 | 10.3% |
| 2-1 | 4 | 10.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.9% |
| 1 | 95 | 22.7% |
| 2 | 104 | 24.8% |
| 3 | 82 | 19.6% |
| 4 | 53 | 12.6% |
| 5 | 23 | 5.5% |
| 6 | 7 | 1.7% |
| 7 | 3 | 0.7% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-04-10 | 5-4 | 9 |
| 2025-2026 | 2026-05-16 | 6-2 | 8 |
| 2025-2026 | 2026-03-14 | 5-2 | 7 |
| 2025-2026 | 2026-05-08 | 4-3 | 7 |
| 2026-2027 | 2026-09-13 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **295** (draws: **124**)
- Average winning margin: **1.6**

| margin | matches | pct |
|---|---|---|
| 1 | 170 | 57.6% |
| 2 | 83 | 28.1% |
| 3+ | 42 | 14.2% |

## 6. Margin by outcome

### Home wins
- Matches: **192** | avg margin: **1.65** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 105 | 54.7% |
| 2 | 58 | 30.2% |
| 3+ | 29 | 15.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **103** | avg margin: **1.5** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 65 | 63.1% |
| 2 | 25 | 24.3% |
| 3+ | 13 | 12.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 192 | 1-0 | 57 | 29.7% |
| draw | 124 | 0-0 | 50 | 40.3% |
| away | 103 | 0-1 | 38 | 36.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\primera2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\primera2\charts\scoreline_analysis_total_goals.png)

