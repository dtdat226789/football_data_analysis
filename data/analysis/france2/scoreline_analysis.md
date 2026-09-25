# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:58:52+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Scoreline frequency
- Matches analysed: **373** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 49 | 13.1% |
| 1-0 | 48 | 12.9% |
| 0-0 | 40 | 10.7% |
| 0-1 | 33 | 8.8% |
| 2-1 | 30 | 8.0% |
| 1-2 | 28 | 7.5% |
| 2-2 | 24 | 6.4% |
| 2-0 | 15 | 4.0% |
| 0-3 | 13 | 3.5% |
| 0-2 | 13 | 3.5% |
| 1-3 | 12 | 3.2% |
| 3-1 | 10 | 2.7% |
| 4-0 | 7 | 1.9% |
| 3-2 | 7 | 1.9% |
| 2-3 | 7 | 1.9% |
| 3-3 | 5 | 1.3% |
| 3-0 | 4 | 1.1% |
| 4-1 | 4 | 1.1% |
| 4-3 | 3 | 0.8% |
| 4-2 | 3 | 0.8% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 42 | 13.5% |
| 1-1 | 38 | 12.3% |
| 0-0 | 33 | 10.6% |
| 2-1 | 26 | 8.4% |
| 0-1 | 26 | 8.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 11 | 17.5% |
| 0-0 | 7 | 11.1% |
| 0-1 | 7 | 11.1% |
| 1-0 | 6 | 9.5% |
| 1-2 | 5 | 7.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 40 | 10.7% |
| 1 | 81 | 21.7% |
| 2 | 77 | 20.6% |
| 3 | 75 | 20.1% |
| 4 | 54 | 14.5% |
| 5 | 21 | 5.6% |
| 6 | 14 | 3.8% |
| 7 | 7 | 1.9% |
| 8 | 4 | 1.1% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-09-27 | 6-2 | 8 |
| 2025-2026 | 2025-10-28 | 2-6 | 8 |
| 2025-2026 | 2026-04-27 | 2-6 | 8 |
| 2025-2026 | 2026-05-09 | 5-3 | 8 |
| 2025-2026 | 2025-09-20 | 5-2 | 7 |
| 2025-2026 | 2026-02-09 | 4-3 | 7 |
| 2025-2026 | 2026-02-21 | 4-3 | 7 |
| 2025-2026 | 2026-03-20 | 3-4 | 7 |
| 2025-2026 | 2026-04-11 | 4-3 | 7 |
| 2026-2027 | 2026-08-22 | 2-5 | 7 |
| 2026-2027 | 2026-09-18 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **255** (draws: **118**)
- Average winning margin: **1.62**

| margin | matches | pct |
|---|---|---|
| 1 | 158 | 62.0% |
| 2 | 56 | 22.0% |
| 3+ | 41 | 16.1% |

## 6. Margin by outcome

### Home wins
- Matches: **138** | avg margin: **1.62** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 88 | 63.8% |
| 2 | 29 | 21.0% |
| 3+ | 21 | 15.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **117** | avg margin: **1.61** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 70 | 59.8% |
| 2 | 27 | 23.1% |
| 3+ | 20 | 17.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 138 | 1-0 | 48 | 34.8% |
| draw | 118 | 1-1 | 49 | 41.5% |
| away | 117 | 0-1 | 33 | 28.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\france2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\france2\charts\scoreline_analysis_total_goals.png)

