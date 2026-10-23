# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:46:38+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League (China)
- Scope: league `china`

## 1. Scoreline frequency
- Matches analysed: **448** across **2** seasons.
- Distinct scorelines seen: **35**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 55 | 12.3% |
| 1-0 | 43 | 9.6% |
| 2-1 | 34 | 7.6% |
| 2-2 | 33 | 7.4% |
| 1-2 | 32 | 7.1% |
| 2-0 | 31 | 6.9% |
| 3-1 | 26 | 5.8% |
| 0-0 | 19 | 4.2% |
| 0-1 | 19 | 4.2% |
| 3-2 | 16 | 3.6% |
| 1-3 | 14 | 3.1% |
| 3-0 | 14 | 3.1% |
| 2-3 | 13 | 2.9% |
| 0-2 | 12 | 2.7% |
| 4-1 | 11 | 2.5% |
| 4-0 | 11 | 2.5% |
| 3-3 | 8 | 1.8% |
| 3-4 | 6 | 1.3% |
| 0-3 | 6 | 1.3% |
| 4-2 | 6 | 1.3% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-0 | 24 | 10.0% |
| 1-1 | 24 | 10.0% |
| 2-2 | 23 | 9.6% |
| 2-0 | 20 | 8.3% |
| 2-1 | 17 | 7.1% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 31 | 14.9% |
| 1-0 | 19 | 9.1% |
| 2-1 | 17 | 8.2% |
| 1-2 | 15 | 7.2% |
| 0-1 | 13 | 6.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 4.2% |
| 1 | 62 | 13.8% |
| 2 | 98 | 21.9% |
| 3 | 86 | 19.2% |
| 4 | 88 | 19.6% |
| 5 | 47 | 10.5% |
| 6 | 31 | 6.9% |
| 7 | 12 | 2.7% |
| 8 | 4 | 0.9% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **17**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-08-22 | 4-5 | 9 |
| 2025 | 2025-04-15 | 4-4 | 8 |
| 2025 | 2025-08-02 | 4-4 | 8 |
| 2026 | 2026-03-07 | 5-3 | 8 |
| 2026 | 2026-08-23 | 4-4 | 8 |
| 2025 | 2025-03-28 | 3-4 | 7 |
| 2025 | 2025-03-29 | 3-4 | 7 |
| 2025 | 2025-04-19 | 6-1 | 7 |
| 2025 | 2025-05-05 | 3-4 | 7 |
| 2025 | 2025-08-10 | 3-4 | 7 |
| 2025 | 2025-09-19 | 2-5 | 7 |
| 2025 | 2025-09-26 | 6-1 | 7 |
| 2025 | 2025-10-17 | 3-4 | 7 |
| 2026 | 2026-04-05 | 5-2 | 7 |
| 2026 | 2026-04-12 | 3-4 | 7 |
| 2026 | 2026-07-10 | 4-3 | 7 |
| 2026 | 2026-07-26 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **330** (draws: **118**)
- Average winning margin: **1.83**

| margin | matches | pct |
|---|---|---|
| 1 | 166 | 50.3% |
| 2 | 95 | 28.8% |
| 3+ | 69 | 20.9% |

## 6. Margin by outcome

### Home wins
- Matches: **207** | avg margin: **1.92** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 95 | 45.9% |
| 2 | 64 | 30.9% |
| 3+ | 48 | 23.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **123** | avg margin: **1.68** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 71 | 57.7% |
| 2 | 31 | 25.2% |
| 3+ | 21 | 17.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 207 | 1-0 | 43 | 20.8% |
| draw | 118 | 1-1 | 55 | 46.6% |
| away | 123 | 1-2 | 32 | 26.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\china\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\china\charts\scoreline_analysis_total_goals.png)

