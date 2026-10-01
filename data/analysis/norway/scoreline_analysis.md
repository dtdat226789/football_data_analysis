# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:02:46+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Eliteserien (Norway)
- Scope: league `norway`

## 1. Scoreline frequency
- Matches analysed: **408** across **2** seasons.
- Distinct scorelines seen: **39**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 39 | 9.6% |
| 1-1 | 39 | 9.6% |
| 1-0 | 30 | 7.4% |
| 2-0 | 30 | 7.4% |
| 1-2 | 26 | 6.4% |
| 3-1 | 24 | 5.9% |
| 0-2 | 19 | 4.7% |
| 0-1 | 19 | 4.7% |
| 3-0 | 18 | 4.4% |
| 2-2 | 18 | 4.4% |
| 0-0 | 17 | 4.2% |
| 3-2 | 15 | 3.7% |
| 4-0 | 14 | 3.4% |
| 2-3 | 13 | 3.2% |
| 1-3 | 13 | 3.2% |
| 0-3 | 13 | 3.2% |
| 4-1 | 10 | 2.5% |
| 1-4 | 7 | 1.7% |
| 5-0 | 7 | 1.7% |
| 0-5 | 4 | 1.0% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-1 | 22 | 9.2% |
| 1-0 | 20 | 8.3% |
| 2-1 | 19 | 7.9% |
| 3-1 | 17 | 7.1% |
| 2-0 | 14 | 5.8% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 20 | 11.9% |
| 1-1 | 17 | 10.1% |
| 2-0 | 16 | 9.5% |
| 1-2 | 14 | 8.3% |
| 1-0 | 10 | 6.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 17 | 4.2% |
| 1 | 49 | 12.0% |
| 2 | 88 | 21.6% |
| 3 | 96 | 23.5% |
| 4 | 70 | 17.2% |
| 5 | 56 | 13.7% |
| 6 | 18 | 4.4% |
| 7 | 5 | 1.2% |
| 8 | 5 | 1.2% |
| 9 | 3 | 0.7% |
| 10+ | 1 | 0.2% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **14**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026 | 2026-08-16 | 5-5 | 10 |
| 2025 | 2025-07-26 | 7-2 | 9 |
| 2026 | 2026-05-16 | 6-3 | 9 |
| 2026 | 2026-09-13 | 8-1 | 9 |
| 2025 | 2025-04-27 | 4-4 | 8 |
| 2025 | 2025-09-12 | 7-1 | 8 |
| 2025 | 2025-11-22 | 2-6 | 8 |
| 2026 | 2026-08-02 | 2-6 | 8 |
| 2026 | 2026-09-12 | 5-3 | 8 |
| 2025 | 2025-04-21 | 2-5 | 7 |
| 2025 | 2025-05-24 | 4-3 | 7 |
| 2025 | 2025-10-18 | 2-5 | 7 |
| 2026 | 2026-07-16 | 6-1 | 7 |
| 2026 | 2026-08-30 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **330** (draws: **78**)
- Average winning margin: **2.03**

| margin | matches | pct |
|---|---|---|
| 1 | 144 | 43.6% |
| 2 | 95 | 28.8% |
| 3+ | 91 | 27.6% |

## 6. Margin by outcome

### Home wins
- Matches: **204** | avg margin: **2.12** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 85 | 41.7% |
| 2 | 59 | 28.9% |
| 3+ | 60 | 29.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **126** | avg margin: **1.88** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 46.8% |
| 2 | 36 | 28.6% |
| 3+ | 31 | 24.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 204 | 2-1 | 39 | 19.1% |
| draw | 78 | 1-1 | 39 | 50.0% |
| away | 126 | 1-2 | 26 | 20.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\norway\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\norway\charts\scoreline_analysis_total_goals.png)

