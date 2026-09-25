# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:48+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League (England)
- Scope: league `national`

## 1. Scoreline frequency
- Matches analysed: **665** across **2** seasons.
- Distinct scorelines seen: **38**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 77 | 11.6% |
| 1-0 | 65 | 9.8% |
| 2-1 | 64 | 9.6% |
| 1-2 | 56 | 8.4% |
| 0-2 | 40 | 6.0% |
| 0-1 | 38 | 5.7% |
| 2-0 | 35 | 5.3% |
| 2-2 | 32 | 4.8% |
| 0-0 | 29 | 4.4% |
| 3-2 | 25 | 3.8% |
| 3-0 | 24 | 3.6% |
| 0-3 | 24 | 3.6% |
| 1-3 | 24 | 3.6% |
| 3-1 | 23 | 3.5% |
| 2-3 | 19 | 2.9% |
| 4-0 | 15 | 2.3% |
| 4-1 | 12 | 1.8% |
| 3-3 | 9 | 1.4% |
| 4-2 | 9 | 1.4% |
| 5-1 | 8 | 1.2% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 64 | 11.5% |
| 2-1 | 54 | 9.7% |
| 1-0 | 50 | 9.0% |
| 1-2 | 47 | 8.4% |
| 0-2 | 36 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 15 | 13.9% |
| 1-1 | 13 | 12.0% |
| 2-1 | 10 | 9.3% |
| 1-3 | 9 | 8.3% |
| 1-2 | 9 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 29 | 4.4% |
| 1 | 103 | 15.5% |
| 2 | 152 | 22.9% |
| 3 | 168 | 25.3% |
| 4 | 96 | 14.4% |
| 5 | 70 | 10.5% |
| 6 | 31 | 4.7% |
| 7 | 9 | 1.4% |
| 8 | 6 | 0.9% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **16**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-14 | 3-6 | 9 |
| 2025-2026 | 2025-09-13 | 4-4 | 8 |
| 2025-2026 | 2025-12-26 | 7-1 | 8 |
| 2025-2026 | 2026-02-25 | 4-4 | 8 |
| 2025-2026 | 2026-03-07 | 5-3 | 8 |
| 2025-2026 | 2026-03-21 | 6-2 | 8 |
| 2025-2026 | 2026-04-18 | 2-6 | 8 |
| 2025-2026 | 2025-08-25 | 3-4 | 7 |
| 2025-2026 | 2025-09-03 | 3-4 | 7 |
| 2025-2026 | 2025-09-20 | 4-3 | 7 |
| 2025-2026 | 2025-09-30 | 2-5 | 7 |
| 2025-2026 | 2026-02-21 | 3-4 | 7 |
| 2025-2026 | 2026-03-31 | 7-0 | 7 |
| 2025-2026 | 2026-04-21 | 4-3 | 7 |
| 2026-2027 | 2026-08-08 | 5-2 | 7 |
| 2026-2027 | 2026-09-19 | 1-6 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **516** (draws: **149**)
- Average winning margin: **1.78**

| margin | matches | pct |
|---|---|---|
| 1 | 272 | 52.7% |
| 2 | 135 | 26.2% |
| 3+ | 109 | 21.1% |

## 6. Margin by outcome

### Home wins
- Matches: **293** | avg margin: **1.85** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 156 | 53.2% |
| 2 | 68 | 23.2% |
| 3+ | 69 | 23.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **223** | avg margin: **1.7** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 116 | 52.0% |
| 2 | 67 | 30.0% |
| 3+ | 40 | 17.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 293 | 1-0 | 65 | 22.2% |
| draw | 149 | 1-1 | 77 | 51.7% |
| away | 223 | 1-2 | 56 | 25.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\national\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\national\charts\scoreline_analysis_total_goals.png)

