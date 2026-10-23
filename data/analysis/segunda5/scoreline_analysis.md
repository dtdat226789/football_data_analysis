# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:07:53+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Scoreline frequency
- Matches analysed: **348** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 38 | 10.9% |
| 2-1 | 38 | 10.9% |
| 1-0 | 33 | 9.5% |
| 0-0 | 32 | 9.2% |
| 0-1 | 25 | 7.2% |
| 2-0 | 25 | 7.2% |
| 1-2 | 24 | 6.9% |
| 3-0 | 24 | 6.9% |
| 0-2 | 18 | 5.2% |
| 3-1 | 13 | 3.7% |
| 2-2 | 13 | 3.7% |
| 3-2 | 11 | 3.2% |
| 1-3 | 11 | 3.2% |
| 2-3 | 10 | 2.9% |
| 4-0 | 6 | 1.7% |
| 0-3 | 5 | 1.4% |
| 0-4 | 4 | 1.1% |
| 4-1 | 4 | 1.1% |
| 3-3 | 3 | 0.9% |
| 5-0 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 37 | 12.1% |
| 2-1 | 32 | 10.5% |
| 0-0 | 27 | 8.8% |
| 1-0 | 25 | 8.2% |
| 0-1 | 24 | 7.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 8 | 19.0% |
| 2-1 | 6 | 14.3% |
| 0-0 | 5 | 11.9% |
| 3-0 | 3 | 7.1% |
| 1-3 | 3 | 7.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.2% |
| 1 | 58 | 16.7% |
| 2 | 81 | 23.3% |
| 3 | 91 | 26.1% |
| 4 | 47 | 13.5% |
| 5 | 28 | 8.0% |
| 6 | 5 | 1.4% |
| 7 | 6 | 1.7% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-11-02 | 2-5 | 7 |
| 2025-2026 | 2026-01-03 | 5-2 | 7 |
| 2025-2026 | 2026-02-22 | 2-5 | 7 |
| 2026-2027 | 2026-09-12 | 4-3 | 7 |
| 2026-2027 | 2026-09-20 | 5-2 | 7 |
| 2026-2027 | 2026-09-20 | 6-1 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **262** (draws: **86**)
- Average winning margin: **1.72**

| margin | matches | pct |
|---|---|---|
| 1 | 142 | 54.2% |
| 2 | 68 | 26.0% |
| 3+ | 52 | 19.8% |

## 6. Margin by outcome

### Home wins
- Matches: **161** | avg margin: **1.8** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 83 | 51.6% |
| 2 | 39 | 24.2% |
| 3+ | 39 | 24.2% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **101** | avg margin: **1.59** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 58.4% |
| 2 | 29 | 28.7% |
| 3+ | 13 | 12.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 161 | 2-1 | 38 | 23.6% |
| draw | 86 | 1-1 | 38 | 44.2% |
| away | 101 | 0-1 | 25 | 24.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda5\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda5\charts\scoreline_analysis_total_goals.png)

