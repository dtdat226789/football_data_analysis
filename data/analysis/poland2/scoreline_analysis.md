# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:41:19+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Division 1 (Poland)
- Scope: league `poland2`

## 1. Scoreline frequency
- Matches analysed: **408** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 59 | 14.5% |
| 2-1 | 46 | 11.3% |
| 1-2 | 38 | 9.3% |
| 0-1 | 28 | 6.9% |
| 2-0 | 28 | 6.9% |
| 2-2 | 26 | 6.4% |
| 1-0 | 21 | 5.1% |
| 3-1 | 19 | 4.7% |
| 0-0 | 19 | 4.7% |
| 3-2 | 16 | 3.9% |
| 0-2 | 15 | 3.7% |
| 3-0 | 12 | 2.9% |
| 2-3 | 12 | 2.9% |
| 4-0 | 10 | 2.5% |
| 0-3 | 8 | 2.0% |
| 3-3 | 8 | 2.0% |
| 1-3 | 7 | 1.7% |
| 0-4 | 5 | 1.2% |
| 1-4 | 4 | 1.0% |
| 4-1 | 4 | 1.0% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 14.3% |
| 2-1 | 39 | 11.9% |
| 1-2 | 32 | 9.8% |
| 2-2 | 21 | 6.4% |
| 2-0 | 20 | 6.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 12 | 15.0% |
| 0-1 | 9 | 11.2% |
| 2-0 | 8 | 10.0% |
| 2-1 | 7 | 8.8% |
| 1-2 | 6 | 7.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 4.7% |
| 1 | 49 | 12.0% |
| 2 | 102 | 25.0% |
| 3 | 104 | 25.5% |
| 4 | 67 | 16.4% |
| 5 | 39 | 9.6% |
| 6 | 16 | 3.9% |
| 7 | 10 | 2.5% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **12**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-07-25 | 4-5 | 9 |
| 2026-2027 | 2026-09-19 | 7-1 | 8 |
| 2025-2026 | 2025-07-19 | 4-3 | 7 |
| 2025-2026 | 2025-08-04 | 3-4 | 7 |
| 2025-2026 | 2025-08-19 | 1-6 | 7 |
| 2025-2026 | 2025-08-19 | 1-6 | 7 |
| 2025-2026 | 2025-08-19 | 0-7 | 7 |
| 2025-2026 | 2025-11-28 | 6-1 | 7 |
| 2025-2026 | 2026-02-08 | 5-2 | 7 |
| 2025-2026 | 2026-04-23 | 4-3 | 7 |
| 2026-2027 | 2026-07-24 | 4-3 | 7 |
| 2026-2027 | 2026-08-16 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **296** (draws: **112**)
- Average winning margin: **1.75**

| margin | matches | pct |
|---|---|---|
| 1 | 166 | 56.1% |
| 2 | 75 | 25.3% |
| 3+ | 55 | 18.6% |

## 6. Margin by outcome

### Home wins
- Matches: **170** | avg margin: **1.81** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 86 | 50.6% |
| 2 | 51 | 30.0% |
| 3+ | 33 | 19.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **126** | avg margin: **1.66** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 80 | 63.5% |
| 2 | 24 | 19.0% |
| 3+ | 22 | 17.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 170 | 2-1 | 46 | 27.1% |
| draw | 112 | 1-1 | 59 | 52.7% |
| away | 126 | 1-2 | 38 | 30.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\poland2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\poland2\charts\scoreline_analysis_total_goals.png)

