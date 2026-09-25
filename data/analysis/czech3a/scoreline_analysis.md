# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:56:40+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: 3. CFL - Group A (Czech Republic)
- Scope: league `czech3a`

## 1. Scoreline frequency
- Matches analysed: **330** across **2** seasons.
- Distinct scorelines seen: **37**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 26 | 7.9% |
| 1-0 | 25 | 7.6% |
| 0-0 | 24 | 7.3% |
| 3-1 | 22 | 6.7% |
| 2-2 | 21 | 6.4% |
| 2-0 | 20 | 6.1% |
| 2-1 | 20 | 6.1% |
| 0-1 | 19 | 5.8% |
| 1-3 | 18 | 5.5% |
| 1-2 | 17 | 5.2% |
| 0-2 | 15 | 4.5% |
| 3-2 | 11 | 3.3% |
| 3-0 | 11 | 3.3% |
| 0-3 | 7 | 2.1% |
| 0-4 | 7 | 2.1% |
| 4-1 | 6 | 1.8% |
| 1-4 | 6 | 1.8% |
| 4-2 | 6 | 1.8% |
| 5-2 | 6 | 1.8% |
| 4-0 | 6 | 1.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 22 | 8.1% |
| 1-0 | 22 | 8.1% |
| 2-0 | 19 | 7.0% |
| 3-1 | 18 | 6.6% |
| 0-0 | 17 | 6.2% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-0 | 7 | 12.1% |
| 2-2 | 6 | 10.3% |
| 0-2 | 5 | 8.6% |
| 3-1 | 4 | 6.9% |
| 1-1 | 4 | 6.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 24 | 7.3% |
| 1 | 44 | 13.3% |
| 2 | 61 | 18.5% |
| 3 | 55 | 16.7% |
| 4 | 74 | 22.4% |
| 5 | 33 | 10.0% |
| 6 | 18 | 5.5% |
| 7 | 14 | 4.2% |
| 8 | 5 | 1.5% |
| 9 | 2 | 0.6% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **21**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-05-20 | 3-6 | 9 |
| 2026-2027 | 2026-09-05 | 7-2 | 9 |
| 2025-2026 | 2025-08-08 | 3-5 | 8 |
| 2025-2026 | 2025-10-04 | 5-3 | 8 |
| 2025-2026 | 2026-05-16 | 6-2 | 8 |
| 2025-2026 | 2026-05-20 | 3-5 | 8 |
| 2026-2027 | 2026-09-02 | 3-5 | 8 |
| 2025-2026 | 2025-08-08 | 3-4 | 7 |
| 2025-2026 | 2025-08-17 | 4-3 | 7 |
| 2025-2026 | 2025-09-10 | 5-2 | 7 |
| 2025-2026 | 2025-09-27 | 3-4 | 7 |
| 2025-2026 | 2025-09-28 | 5-2 | 7 |
| 2025-2026 | 2025-10-11 | 4-3 | 7 |
| 2025-2026 | 2025-11-08 | 5-2 | 7 |
| 2025-2026 | 2025-11-15 | 2-5 | 7 |
| 2025-2026 | 2026-05-01 | 4-3 | 7 |
| 2025-2026 | 2026-05-24 | 2-5 | 7 |
| 2025-2026 | 2026-05-30 | 5-2 | 7 |
| 2025-2026 | 2026-06-06 | 5-2 | 7 |
| 2026-2027 | 2026-09-12 | 5-2 | 7 |
| 2026-2027 | 2026-09-19 | 7-0 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **256** (draws: **74**)
- Average winning margin: **2.02**

| margin | matches | pct |
|---|---|---|
| 1 | 102 | 39.8% |
| 2 | 88 | 34.4% |
| 3+ | 66 | 25.8% |

## 6. Margin by outcome

### Home wins
- Matches: **147** | avg margin: **2.04** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 40.1% |
| 2 | 49 | 33.3% |
| 3+ | 39 | 26.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **109** | avg margin: **2.0** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 43 | 39.4% |
| 2 | 39 | 35.8% |
| 3+ | 27 | 24.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 147 | 1-0 | 25 | 17.0% |
| draw | 74 | 1-1 | 26 | 35.1% |
| away | 109 | 0-1 | 19 | 17.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\czech3a\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\czech3a\charts\scoreline_analysis_total_goals.png)

