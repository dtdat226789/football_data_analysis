# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:46:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Scoreline frequency
- Matches analysed: **339** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 38 | 11.2% |
| 2-1 | 37 | 10.9% |
| 0-0 | 32 | 9.4% |
| 1-0 | 30 | 8.8% |
| 0-1 | 25 | 7.4% |
| 1-2 | 24 | 7.1% |
| 2-0 | 23 | 6.8% |
| 3-0 | 23 | 6.8% |
| 0-2 | 18 | 5.3% |
| 3-1 | 13 | 3.8% |
| 2-2 | 12 | 3.5% |
| 3-2 | 11 | 3.2% |
| 2-3 | 10 | 2.9% |
| 1-3 | 10 | 2.9% |
| 4-0 | 6 | 1.8% |
| 0-3 | 5 | 1.5% |
| 0-4 | 4 | 1.2% |
| 4-1 | 4 | 1.2% |
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
| 2-1 | 5 | 15.2% |
| 0-0 | 5 | 15.2% |
| 1-0 | 5 | 15.2% |
| 3-0 | 2 | 6.1% |
| 1-3 | 2 | 6.1% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 32 | 9.4% |
| 1 | 55 | 16.2% |
| 2 | 79 | 23.3% |
| 3 | 89 | 26.3% |
| 4 | 45 | 13.3% |
| 5 | 28 | 8.3% |
| 6 | 5 | 1.5% |
| 7 | 6 | 1.8% |
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
- Decided matches: **254** (draws: **85**)
- Average winning margin: **1.72**

| margin | matches | pct |
|---|---|---|
| 1 | 138 | 54.3% |
| 2 | 65 | 25.6% |
| 3+ | 51 | 20.1% |

## 6. Margin by outcome

### Home wins
- Matches: **154** | avg margin: **1.81** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 79 | 51.3% |
| 2 | 37 | 24.0% |
| 3+ | 38 | 24.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **100** | avg margin: **1.59** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 59 | 59.0% |
| 2 | 28 | 28.0% |
| 3+ | 13 | 13.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 154 | 2-1 | 37 | 24.0% |
| draw | 85 | 1-1 | 38 | 44.7% |
| away | 100 | 0-1 | 25 | 25.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda5\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda5\charts\scoreline_analysis_total_goals.png)

