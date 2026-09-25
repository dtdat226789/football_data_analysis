# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:19+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Virsliga (Latvia)
- Scope: league `latvia`

## 1. Scoreline frequency
- Matches analysed: **336** across **2** seasons.
- Distinct scorelines seen: **34**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 40 | 11.9% |
| 0-1 | 36 | 10.7% |
| 1-0 | 28 | 8.3% |
| 2-0 | 27 | 8.0% |
| 2-1 | 23 | 6.8% |
| 1-2 | 22 | 6.5% |
| 0-0 | 19 | 5.7% |
| 2-2 | 17 | 5.1% |
| 4-1 | 12 | 3.6% |
| 3-1 | 12 | 3.6% |
| 3-0 | 11 | 3.3% |
| 3-2 | 11 | 3.3% |
| 1-3 | 9 | 2.7% |
| 0-2 | 9 | 2.7% |
| 4-0 | 7 | 2.1% |
| 0-3 | 7 | 2.1% |
| 2-3 | 6 | 1.8% |
| 1-4 | 5 | 1.5% |
| 2-4 | 4 | 1.2% |
| 3-3 | 4 | 1.2% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 20 | 11.0% |
| 2-0 | 19 | 10.4% |
| 0-1 | 18 | 9.9% |
| 1-0 | 16 | 8.8% |
| 2-2 | 12 | 6.6% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 20 | 13.0% |
| 0-1 | 18 | 11.7% |
| 2-1 | 12 | 7.8% |
| 1-2 | 12 | 7.8% |
| 1-0 | 12 | 7.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 19 | 5.7% |
| 1 | 64 | 19.0% |
| 2 | 76 | 22.6% |
| 3 | 63 | 18.8% |
| 4 | 47 | 14.0% |
| 5 | 37 | 11.0% |
| 6 | 19 | 5.7% |
| 7 | 7 | 2.1% |
| 8 | 4 | 1.2% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **11**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-06-30 | 1-7 | 8 |
| 2025 | 2025-07-26 | 6-2 | 8 |
| 2025 | 2025-08-30 | 2-6 | 8 |
| 2026 | 2026-04-04 | 0-8 | 8 |
| 2025 | 2025-04-03 | 2-5 | 7 |
| 2025 | 2025-05-25 | 2-5 | 7 |
| 2025 | 2025-11-07 | 3-4 | 7 |
| 2026 | 2026-05-02 | 3-4 | 7 |
| 2026 | 2026-05-07 | 6-1 | 7 |
| 2026 | 2026-05-07 | 7-0 | 7 |
| 2026 | 2026-08-10 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **256** (draws: **80**)
- Average winning margin: **1.93**

| margin | matches | pct |
|---|---|---|
| 1 | 128 | 50.0% |
| 2 | 64 | 25.0% |
| 3+ | 64 | 25.0% |

## 6. Margin by outcome

### Home wins
- Matches: **147** | avg margin: **2.1** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 62 | 42.2% |
| 2 | 42 | 28.6% |
| 3+ | 43 | 29.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **109** | avg margin: **1.71** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 66 | 60.6% |
| 2 | 22 | 20.2% |
| 3+ | 21 | 19.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 147 | 1-0 | 28 | 19.0% |
| draw | 80 | 1-1 | 40 | 50.0% |
| away | 109 | 0-1 | 36 | 33.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\latvia\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\latvia\charts\scoreline_analysis_total_goals.png)

