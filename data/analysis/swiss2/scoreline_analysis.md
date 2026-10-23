# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:10:06+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Scoreline frequency
- Matches analysed: **231** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 27 | 11.7% |
| 1-1 | 20 | 8.7% |
| 1-0 | 18 | 7.8% |
| 1-2 | 17 | 7.4% |
| 2-0 | 15 | 6.5% |
| 2-2 | 15 | 6.5% |
| 0-2 | 15 | 6.5% |
| 1-3 | 14 | 6.1% |
| 0-0 | 14 | 6.1% |
| 3-0 | 9 | 3.9% |
| 0-1 | 9 | 3.9% |
| 3-2 | 8 | 3.5% |
| 0-3 | 7 | 3.0% |
| 3-1 | 6 | 2.6% |
| 4-0 | 5 | 2.2% |
| 5-0 | 4 | 1.7% |
| 4-5 | 3 | 1.3% |
| 3-3 | 3 | 1.3% |
| 2-4 | 3 | 1.3% |
| 5-2 | 3 | 1.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-1 | 22 | 11.8% |
| 1-0 | 18 | 9.7% |
| 1-1 | 14 | 7.5% |
| 1-3 | 13 | 7.0% |
| 1-2 | 13 | 7.0% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 6 | 13.3% |
| 2-1 | 5 | 11.1% |
| 2-0 | 4 | 8.9% |
| 2-2 | 4 | 8.9% |
| 1-2 | 4 | 8.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 14 | 6.1% |
| 1 | 27 | 11.7% |
| 2 | 50 | 21.6% |
| 3 | 60 | 26.0% |
| 4 | 42 | 18.2% |
| 5 | 18 | 7.8% |
| 6 | 11 | 4.8% |
| 7 | 4 | 1.7% |
| 8 | 2 | 0.9% |
| 9 | 3 | 1.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **9**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-22 | 4-5 | 9 |
| 2025-2026 | 2026-04-04 | 4-5 | 9 |
| 2026-2027 | 2026-07-24 | 4-5 | 9 |
| 2025-2026 | 2026-02-27 | 5-3 | 8 |
| 2025-2026 | 2026-05-03 | 3-5 | 8 |
| 2025-2026 | 2025-10-31 | 3-4 | 7 |
| 2025-2026 | 2026-01-30 | 5-2 | 7 |
| 2025-2026 | 2026-04-03 | 5-2 | 7 |
| 2025-2026 | 2026-04-07 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **179** (draws: **52**)
- Average winning margin: **1.87**

| margin | matches | pct |
|---|---|---|
| 1 | 84 | 46.9% |
| 2 | 56 | 31.3% |
| 3+ | 39 | 21.8% |

## 6. Margin by outcome

### Home wins
- Matches: **103** | avg margin: **1.92** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 53 | 51.5% |
| 2 | 23 | 22.3% |
| 3+ | 27 | 26.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **76** | avg margin: **1.79** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 31 | 40.8% |
| 2 | 33 | 43.4% |
| 3+ | 12 | 15.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 103 | 2-1 | 27 | 26.2% |
| draw | 52 | 1-1 | 20 | 38.5% |
| away | 76 | 1-2 | 17 | 22.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\swiss2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\swiss2\charts\scoreline_analysis_total_goals.png)

