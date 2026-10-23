# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:47:10+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Scoreline frequency
- Matches analysed: **312** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 34 | 10.9% |
| 1-0 | 31 | 9.9% |
| 1-1 | 29 | 9.3% |
| 1-2 | 25 | 8.0% |
| 0-1 | 24 | 7.7% |
| 2-2 | 22 | 7.1% |
| 0-2 | 20 | 6.4% |
| 2-0 | 20 | 6.4% |
| 0-0 | 18 | 5.8% |
| 3-1 | 15 | 4.8% |
| 3-0 | 11 | 3.5% |
| 0-3 | 8 | 2.6% |
| 3-2 | 8 | 2.6% |
| 4-1 | 7 | 2.2% |
| 1-3 | 7 | 2.2% |
| 5-0 | 5 | 1.6% |
| 3-3 | 5 | 1.6% |
| 2-3 | 4 | 1.3% |
| 4-0 | 4 | 1.3% |
| 6-1 | 3 | 1.0% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 28 | 11.7% |
| 1-0 | 26 | 10.8% |
| 1-1 | 21 | 8.8% |
| 0-1 | 20 | 8.3% |
| 1-2 | 20 | 8.3% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 9 | 12.5% |
| 1-1 | 8 | 11.1% |
| 2-1 | 6 | 8.3% |
| 1-0 | 5 | 6.9% |
| 2-0 | 5 | 6.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 18 | 5.8% |
| 1 | 55 | 17.6% |
| 2 | 69 | 22.1% |
| 3 | 78 | 25.0% |
| 4 | 51 | 16.3% |
| 5 | 27 | 8.7% |
| 6 | 7 | 2.2% |
| 7 | 5 | 1.6% |
| 8 | 0 | 0.0% |
| 9 | 2 | 0.6% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-07-30 | 2-7 | 9 |
| 2025-2026 | 2025-11-09 | 7-2 | 9 |
| 2025-2026 | 2025-08-03 | 6-1 | 7 |
| 2025-2026 | 2025-10-04 | 6-1 | 7 |
| 2025-2026 | 2025-11-01 | 5-2 | 7 |
| 2025-2026 | 2026-04-10 | 6-1 | 7 |
| 2026-2027 | 2026-08-15 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **238** (draws: **74**)
- Average winning margin: **1.8**

| margin | matches | pct |
|---|---|---|
| 1 | 126 | 52.9% |
| 2 | 62 | 26.1% |
| 3+ | 50 | 21.0% |

## 6. Margin by outcome

### Home wins
- Matches: **142** | avg margin: **1.89** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 73 | 51.4% |
| 2 | 35 | 24.6% |
| 3+ | 34 | 23.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **96** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 55.2% |
| 2 | 27 | 28.1% |
| 3+ | 16 | 16.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 142 | 2-1 | 34 | 23.9% |
| draw | 74 | 1-1 | 29 | 39.2% |
| away | 96 | 1-2 | 25 | 26.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\czech2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\czech2\charts\scoreline_analysis_total_goals.png)

