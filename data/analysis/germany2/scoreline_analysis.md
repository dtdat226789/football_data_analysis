# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:59:39+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 2. Bundesliga (Germany)
- Scope: league `germany2`

## 1. Scoreline frequency
- Matches analysed: **364** across **2** seasons.
- Distinct scorelines seen: **34**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 41 | 11.3% |
| 1-1 | 36 | 9.9% |
| 1-0 | 35 | 9.6% |
| 1-2 | 29 | 8.0% |
| 2-2 | 26 | 7.1% |
| 2-0 | 23 | 6.3% |
| 0-1 | 21 | 5.8% |
| 0-0 | 19 | 5.2% |
| 0-2 | 17 | 4.7% |
| 3-1 | 16 | 4.4% |
| 3-0 | 15 | 4.1% |
| 2-3 | 12 | 3.3% |
| 0-3 | 11 | 3.0% |
| 3-2 | 10 | 2.7% |
| 4-1 | 9 | 2.5% |
| 3-3 | 8 | 2.2% |
| 1-3 | 7 | 1.9% |
| 5-1 | 4 | 1.1% |
| 4-3 | 3 | 0.8% |
| 4-5 | 2 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 36 | 11.6% |
| 1-0 | 31 | 10.0% |
| 1-1 | 31 | 10.0% |
| 1-2 | 26 | 8.4% |
| 2-0 | 22 | 7.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-1 | 7 | 13.0% |
| 2-2 | 7 | 13.0% |
| 2-1 | 5 | 9.3% |
| 1-1 | 5 | 9.3% |
| 3-0 | 4 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.2% |
| 1 | 56 | 15.4% |
| 2 | 76 | 20.9% |
| 3 | 96 | 26.4% |
| 4 | 53 | 14.6% |
| 5 | 33 | 9.1% |
| 6 | 16 | 4.4% |
| 7 | 9 | 2.5% |
| 8 | 4 | 1.1% |
| 9 | 2 | 0.5% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **15**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-31 | 4-5 | 9 |
| 2025-2026 | 2026-02-06 | 4-5 | 9 |
| 2025-2026 | 2026-02-21 | 5-3 | 8 |
| 2026-2027 | 2026-08-28 | 3-5 | 8 |
| 2026-2027 | 2026-08-29 | 5-3 | 8 |
| 2026-2027 | 2026-09-05 | 4-4 | 8 |
| 2025-2026 | 2025-10-18 | 4-3 | 7 |
| 2025-2026 | 2026-02-22 | 5-2 | 7 |
| 2025-2026 | 2026-03-22 | 2-5 | 7 |
| 2025-2026 | 2026-04-12 | 4-3 | 7 |
| 2025-2026 | 2026-05-17 | 6-1 | 7 |
| 2026-2027 | 2026-08-08 | 4-3 | 7 |
| 2026-2027 | 2026-08-08 | 1-6 | 7 |
| 2026-2027 | 2026-08-29 | 2-5 | 7 |
| 2026-2027 | 2026-08-29 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **274** (draws: **90**)
- Average winning margin: **1.69**

| margin | matches | pct |
|---|---|---|
| 1 | 154 | 56.2% |
| 2 | 68 | 24.8% |
| 3+ | 52 | 19.0% |

## 6. Margin by outcome

### Home wins
- Matches: **165** | avg margin: **1.75** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 89 | 53.9% |
| 2 | 42 | 25.5% |
| 3+ | 34 | 20.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **109** | avg margin: **1.61** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 65 | 59.6% |
| 2 | 26 | 23.9% |
| 3+ | 18 | 16.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 165 | 2-1 | 41 | 24.8% |
| draw | 90 | 1-1 | 36 | 40.0% |
| away | 109 | 1-2 | 29 | 26.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\germany2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\germany2\charts\scoreline_analysis_total_goals.png)

