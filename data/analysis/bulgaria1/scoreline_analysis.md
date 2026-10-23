# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:46:00+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Scoreline frequency
- Matches analysed: **363** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 45 | 12.4% |
| 1-0 | 43 | 11.8% |
| 0-0 | 39 | 10.7% |
| 2-1 | 38 | 10.5% |
| 0-1 | 29 | 8.0% |
| 2-0 | 27 | 7.4% |
| 1-2 | 21 | 5.8% |
| 0-2 | 16 | 4.4% |
| 2-2 | 15 | 4.1% |
| 3-0 | 15 | 4.1% |
| 1-3 | 13 | 3.6% |
| 0-3 | 12 | 3.3% |
| 3-1 | 11 | 3.0% |
| 2-3 | 6 | 1.7% |
| 3-2 | 6 | 1.7% |
| 5-0 | 5 | 1.4% |
| 4-0 | 4 | 1.1% |
| 0-4 | 4 | 1.1% |
| 1-4 | 3 | 0.8% |
| 0-5 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 0-0 | 36 | 12.2% |
| 1-0 | 35 | 11.9% |
| 1-1 | 35 | 11.9% |
| 2-1 | 30 | 10.2% |
| 0-1 | 25 | 8.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 10 | 14.5% |
| 2-1 | 8 | 11.6% |
| 1-0 | 8 | 11.6% |
| 1-2 | 5 | 7.2% |
| 2-0 | 5 | 7.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 39 | 10.7% |
| 1 | 72 | 19.8% |
| 2 | 88 | 24.2% |
| 3 | 86 | 23.7% |
| 4 | 47 | 12.9% |
| 5 | 24 | 6.6% |
| 6 | 4 | 1.1% |
| 7 | 2 | 0.6% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.3% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-27 | 5-4 | 9 |
| 2025-2026 | 2025-11-30 | 7-0 | 7 |
| 2025-2026 | 2026-03-01 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **264** (draws: **99**)
- Average winning margin: **1.77**

| margin | matches | pct |
|---|---|---|
| 1 | 145 | 54.9% |
| 2 | 67 | 25.4% |
| 3+ | 52 | 19.7% |

## 6. Margin by outcome

### Home wins
- Matches: **156** | avg margin: **1.76** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 89 | 57.1% |
| 2 | 38 | 24.4% |
| 3+ | 29 | 18.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **108** | avg margin: **1.79** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 56 | 51.9% |
| 2 | 29 | 26.9% |
| 3+ | 23 | 21.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 156 | 1-0 | 43 | 27.6% |
| draw | 99 | 1-1 | 45 | 45.5% |
| away | 108 | 0-1 | 29 | 26.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\bulgaria1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\bulgaria1\charts\scoreline_analysis_total_goals.png)

