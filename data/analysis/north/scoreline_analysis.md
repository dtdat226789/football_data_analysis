# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:02:26+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Scoreline frequency
- Matches analysed: **680** across **2** seasons.
- Distinct scorelines seen: **37**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 77 | 11.3% |
| 1-1 | 76 | 11.2% |
| 1-2 | 60 | 8.8% |
| 1-0 | 51 | 7.5% |
| 0-1 | 47 | 6.9% |
| 2-2 | 40 | 5.9% |
| 2-0 | 39 | 5.7% |
| 0-2 | 37 | 5.4% |
| 3-1 | 30 | 4.4% |
| 0-0 | 28 | 4.1% |
| 3-0 | 25 | 3.7% |
| 1-3 | 23 | 3.4% |
| 2-3 | 18 | 2.6% |
| 4-1 | 17 | 2.5% |
| 4-0 | 13 | 1.9% |
| 0-3 | 12 | 1.8% |
| 3-2 | 10 | 1.5% |
| 5-1 | 9 | 1.3% |
| 4-2 | 9 | 1.3% |
| 1-4 | 8 | 1.2% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 59 | 10.5% |
| 2-1 | 56 | 10.0% |
| 1-2 | 53 | 9.5% |
| 1-0 | 42 | 7.5% |
| 2-2 | 36 | 6.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 21 | 17.5% |
| 1-1 | 17 | 14.2% |
| 0-1 | 14 | 11.7% |
| 1-0 | 9 | 7.5% |
| 1-2 | 7 | 5.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 28 | 4.1% |
| 1 | 98 | 14.4% |
| 2 | 152 | 22.4% |
| 3 | 174 | 25.6% |
| 4 | 110 | 16.2% |
| 5 | 62 | 9.1% |
| 6 | 39 | 5.7% |
| 7 | 11 | 1.6% |
| 8 | 5 | 0.7% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 0.1% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **17**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-18 | 6-4 | 10 |
| 2025-2026 | 2025-11-22 | 6-2 | 8 |
| 2025-2026 | 2026-01-10 | 3-5 | 8 |
| 2025-2026 | 2026-01-17 | 0-8 | 8 |
| 2025-2026 | 2026-02-14 | 7-1 | 8 |
| 2025-2026 | 2026-04-18 | 8-0 | 8 |
| 2025-2026 | 2025-11-08 | 3-4 | 7 |
| 2025-2026 | 2025-11-18 | 5-2 | 7 |
| 2025-2026 | 2025-11-29 | 3-4 | 7 |
| 2025-2026 | 2026-01-27 | 4-3 | 7 |
| 2025-2026 | 2026-02-03 | 5-2 | 7 |
| 2025-2026 | 2026-02-24 | 5-2 | 7 |
| 2025-2026 | 2026-03-24 | 2-5 | 7 |
| 2025-2026 | 2026-04-06 | 4-3 | 7 |
| 2025-2026 | 2026-04-11 | 2-5 | 7 |
| 2026-2027 | 2026-08-15 | 3-4 | 7 |
| 2026-2027 | 2026-09-08 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **528** (draws: **152**)
- Average winning margin: **1.84**

| margin | matches | pct |
|---|---|---|
| 1 | 268 | 50.8% |
| 2 | 147 | 27.8% |
| 3+ | 113 | 21.4% |

## 6. Margin by outcome

### Home wins
- Matches: **297** | avg margin: **1.95** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 140 | 47.1% |
| 2 | 79 | 26.6% |
| 3+ | 78 | 26.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **231** | avg margin: **1.69** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 128 | 55.4% |
| 2 | 68 | 29.4% |
| 3+ | 35 | 15.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 297 | 2-1 | 77 | 25.9% |
| draw | 152 | 1-1 | 76 | 50.0% |
| away | 231 | 1-2 | 60 | 26.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\north\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\north\charts\scoreline_analysis_total_goals.png)

