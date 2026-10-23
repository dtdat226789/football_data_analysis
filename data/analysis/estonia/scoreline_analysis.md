# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:49:20+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Scoreline frequency
- Matches analysed: **325** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-2 | 43 | 13.2% |
| 1-0 | 29 | 8.9% |
| 2-1 | 25 | 7.7% |
| 0-1 | 19 | 5.8% |
| 1-3 | 19 | 5.8% |
| 1-1 | 18 | 5.5% |
| 2-0 | 17 | 5.2% |
| 3-1 | 17 | 5.2% |
| 2-2 | 15 | 4.6% |
| 0-2 | 15 | 4.6% |
| 2-3 | 13 | 4.0% |
| 0-3 | 12 | 3.7% |
| 3-0 | 12 | 3.7% |
| 4-0 | 11 | 3.4% |
| 3-2 | 10 | 3.1% |
| 0-0 | 9 | 2.8% |
| 5-0 | 7 | 2.2% |
| 4-1 | 6 | 1.8% |
| 0-4 | 4 | 1.2% |
| 5-1 | 4 | 1.2% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-2 | 21 | 11.7% |
| 2-1 | 17 | 9.4% |
| 1-0 | 15 | 8.3% |
| 2-2 | 11 | 6.1% |
| 0-1 | 11 | 6.1% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-2 | 22 | 15.2% |
| 1-0 | 14 | 9.7% |
| 1-3 | 9 | 6.2% |
| 3-1 | 9 | 6.2% |
| 1-1 | 9 | 6.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 9 | 2.8% |
| 1 | 48 | 14.8% |
| 2 | 50 | 15.4% |
| 3 | 92 | 28.3% |
| 4 | 66 | 20.3% |
| 5 | 39 | 12.0% |
| 6 | 9 | 2.8% |
| 7 | 7 | 2.2% |
| 8 | 3 | 0.9% |
| 9 | 2 | 0.6% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **12**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-04-19 | 0-9 | 9 |
| 2025 | 2025-08-15 | 8-1 | 9 |
| 2025 | 2025-07-20 | 6-2 | 8 |
| 2026 | 2026-03-14 | 7-1 | 8 |
| 2026 | 2026-04-22 | 7-1 | 8 |
| 2025 | 2025-04-22 | 6-1 | 7 |
| 2025 | 2025-05-19 | 2-5 | 7 |
| 2025 | 2025-08-17 | 1-6 | 7 |
| 2025 | 2025-10-25 | 5-2 | 7 |
| 2026 | 2026-04-26 | 7-0 | 7 |
| 2026 | 2026-05-24 | 1-6 | 7 |
| 2026 | 2026-07-19 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **283** (draws: **42**)
- Average winning margin: **2.02**

| margin | matches | pct |
|---|---|---|
| 1 | 139 | 49.1% |
| 2 | 70 | 24.7% |
| 3+ | 74 | 26.1% |

## 6. Margin by outcome

### Home wins
- Matches: **151** | avg margin: **2.28** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 64 | 42.4% |
| 2 | 36 | 23.8% |
| 3+ | 51 | 33.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **132** | avg margin: **1.73** | max margin: **9**
| margin | matches | pct |
|---|---|---|
| 1 | 75 | 56.8% |
| 2 | 34 | 25.8% |
| 3+ | 23 | 17.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 151 | 1-0 | 29 | 19.2% |
| draw | 42 | 1-1 | 18 | 42.9% |
| away | 132 | 1-2 | 43 | 32.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\estonia\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\estonia\charts\scoreline_analysis_total_goals.png)

