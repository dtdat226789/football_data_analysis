# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:03:58+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: National League North (England)
- Scope: league `north`

## 1. Scoreline frequency
- Matches analysed: **668** across **2** seasons.
- Distinct scorelines seen: **37**.

| scoreline | count | pct |
|---|---|---|
| 2-1 | 76 | 11.4% |
| 1-1 | 72 | 10.8% |
| 1-2 | 59 | 8.8% |
| 1-0 | 50 | 7.5% |
| 0-1 | 47 | 7.0% |
| 2-0 | 39 | 5.8% |
| 2-2 | 39 | 5.8% |
| 0-2 | 37 | 5.5% |
| 3-1 | 30 | 4.5% |
| 0-0 | 28 | 4.2% |
| 3-0 | 25 | 3.7% |
| 1-3 | 23 | 3.4% |
| 2-3 | 18 | 2.7% |
| 4-1 | 15 | 2.2% |
| 0-3 | 12 | 1.8% |
| 4-0 | 12 | 1.8% |
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
| 2-1 | 20 | 18.5% |
| 0-1 | 14 | 13.0% |
| 1-1 | 13 | 12.0% |
| 1-0 | 8 | 7.4% |
| 1-2 | 6 | 5.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 28 | 4.2% |
| 1 | 97 | 14.5% |
| 2 | 148 | 22.2% |
| 3 | 172 | 25.7% |
| 4 | 108 | 16.2% |
| 5 | 59 | 8.8% |
| 6 | 39 | 5.8% |
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
- Decided matches: **521** (draws: **147**)
- Average winning margin: **1.83**

| margin | matches | pct |
|---|---|---|
| 1 | 265 | 50.9% |
| 2 | 147 | 28.2% |
| 3+ | 109 | 20.9% |

## 6. Margin by outcome

### Home wins
- Matches: **292** | avg margin: **1.95** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 138 | 47.3% |
| 2 | 79 | 27.1% |
| 3+ | 75 | 25.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **229** | avg margin: **1.68** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 127 | 55.5% |
| 2 | 68 | 29.7% |
| 3+ | 34 | 14.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 292 | 2-1 | 76 | 26.0% |
| draw | 147 | 1-1 | 72 | 49.0% |
| away | 229 | 1-2 | 59 | 25.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\north\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\north\charts\scoreline_analysis_total_goals.png)

