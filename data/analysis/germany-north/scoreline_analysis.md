# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:59:19+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Scoreline frequency
- Matches analysed: **408** across **2** seasons.
- Distinct scorelines seen: **47**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 41 | 10.0% |
| 2-2 | 30 | 7.4% |
| 2-0 | 22 | 5.4% |
| 0-1 | 21 | 5.1% |
| 2-1 | 21 | 5.1% |
| 1-3 | 21 | 5.1% |
| 3-2 | 21 | 5.1% |
| 0-2 | 21 | 5.1% |
| 3-1 | 18 | 4.4% |
| 1-2 | 17 | 4.2% |
| 1-0 | 16 | 3.9% |
| 4-0 | 15 | 3.7% |
| 4-1 | 14 | 3.4% |
| 2-3 | 13 | 3.2% |
| 0-4 | 13 | 3.2% |
| 0-3 | 12 | 2.9% |
| 0-0 | 9 | 2.2% |
| 3-0 | 8 | 2.0% |
| 5-1 | 8 | 2.0% |
| 3-3 | 6 | 1.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 32 | 10.1% |
| 2-2 | 24 | 7.6% |
| 3-2 | 18 | 5.7% |
| 2-1 | 17 | 5.4% |
| 1-3 | 17 | 5.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 9 | 9.9% |
| 2-2 | 6 | 6.6% |
| 2-0 | 6 | 6.6% |
| 0-3 | 5 | 5.5% |
| 0-2 | 5 | 5.5% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 9 | 2.2% |
| 1 | 37 | 9.1% |
| 2 | 84 | 20.6% |
| 3 | 58 | 14.2% |
| 4 | 97 | 23.8% |
| 5 | 61 | 15.0% |
| 6 | 27 | 6.6% |
| 7 | 15 | 3.7% |
| 8 | 13 | 3.2% |
| 9 | 4 | 1.0% |
| 10+ | 3 | 0.7% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **35**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-02 | 6-4 | 10 |
| 2026-2027 | 2026-08-29 | 7-3 | 10 |
| 2026-2027 | 2026-09-15 | 8-2 | 10 |
| 2025-2026 | 2025-10-17 | 7-2 | 9 |
| 2025-2026 | 2026-04-02 | 2-7 | 9 |
| 2025-2026 | 2026-05-16 | 3-6 | 9 |
| 2026-2027 | 2026-09-16 | 9-0 | 9 |
| 2025-2026 | 2025-08-09 | 4-4 | 8 |
| 2025-2026 | 2025-08-22 | 7-1 | 8 |
| 2025-2026 | 2025-08-27 | 6-2 | 8 |
| 2025-2026 | 2025-09-06 | 6-2 | 8 |
| 2025-2026 | 2025-10-04 | 5-3 | 8 |
| 2025-2026 | 2025-10-04 | 5-3 | 8 |
| 2025-2026 | 2025-10-11 | 6-2 | 8 |
| 2025-2026 | 2025-11-29 | 2-6 | 8 |
| 2025-2026 | 2026-05-09 | 4-4 | 8 |
| 2025-2026 | 2026-05-16 | 3-5 | 8 |
| 2026-2027 | 2026-08-01 | 4-4 | 8 |
| 2026-2027 | 2026-08-12 | 6-2 | 8 |
| 2026-2027 | 2026-09-04 | 7-1 | 8 |
| 2025-2026 | 2025-07-26 | 2-5 | 7 |
| 2025-2026 | 2025-07-26 | 2-5 | 7 |
| 2025-2026 | 2025-08-23 | 3-4 | 7 |
| 2025-2026 | 2025-08-30 | 5-2 | 7 |
| 2025-2026 | 2025-09-06 | 6-1 | 7 |
| 2025-2026 | 2025-10-01 | 3-4 | 7 |
| 2025-2026 | 2025-10-04 | 3-4 | 7 |
| 2025-2026 | 2025-11-22 | 6-1 | 7 |
| 2025-2026 | 2026-05-02 | 3-4 | 7 |
| 2026-2027 | 2026-08-08 | 5-2 | 7 |
| 2026-2027 | 2026-08-15 | 5-2 | 7 |
| 2026-2027 | 2026-09-06 | 5-2 | 7 |
| 2026-2027 | 2026-09-06 | 1-6 | 7 |
| 2026-2027 | 2026-09-11 | 4-3 | 7 |
| 2026-2027 | 2026-09-20 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **319** (draws: **89**)
- Average winning margin: **2.27**

| margin | matches | pct |
|---|---|---|
| 1 | 114 | 35.7% |
| 2 | 95 | 29.8% |
| 3+ | 110 | 34.5% |

## 6. Margin by outcome

### Home wins
- Matches: **172** | avg margin: **2.39** | max margin: **9**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 34.3% |
| 2 | 47 | 27.3% |
| 3+ | 66 | 38.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **147** | avg margin: **2.12** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 55 | 37.4% |
| 2 | 48 | 32.7% |
| 3+ | 44 | 29.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 172 | 2-0 | 22 | 12.8% |
| draw | 89 | 1-1 | 41 | 46.1% |
| away | 147 | 0-1 | 21 | 14.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\germany-north\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\germany-north\charts\scoreline_analysis_total_goals.png)

