# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:46:17+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

## 1. Scoreline frequency
- Matches analysed: **654** across **2** seasons.
- Distinct scorelines seen: **33**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 94 | 14.4% |
| 2-1 | 73 | 11.2% |
| 1-0 | 64 | 9.8% |
| 1-2 | 59 | 9.0% |
| 0-1 | 46 | 7.0% |
| 0-0 | 44 | 6.7% |
| 2-2 | 38 | 5.8% |
| 3-1 | 35 | 5.4% |
| 2-0 | 32 | 4.9% |
| 0-2 | 32 | 4.9% |
| 1-3 | 25 | 3.8% |
| 3-0 | 24 | 3.7% |
| 0-3 | 13 | 2.0% |
| 3-2 | 13 | 2.0% |
| 2-3 | 12 | 1.8% |
| 4-0 | 9 | 1.4% |
| 4-1 | 6 | 0.9% |
| 1-4 | 4 | 0.6% |
| 5-1 | 4 | 0.6% |
| 4-2 | 3 | 0.5% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 83 | 14.8% |
| 2-1 | 61 | 10.9% |
| 1-0 | 58 | 10.4% |
| 1-2 | 49 | 8.8% |
| 0-1 | 40 | 7.2% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-1 | 12 | 12.6% |
| 2-2 | 11 | 11.6% |
| 1-1 | 11 | 11.6% |
| 1-2 | 10 | 10.5% |
| 0-0 | 7 | 7.4% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 44 | 6.7% |
| 1 | 110 | 16.8% |
| 2 | 158 | 24.2% |
| 3 | 169 | 25.8% |
| 4 | 110 | 16.8% |
| 5 | 41 | 6.3% |
| 6 | 14 | 2.1% |
| 7 | 4 | 0.6% |
| 8 | 4 | 0.6% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **8**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-08-16 | 3-5 | 8 |
| 2025-2026 | 2025-08-23 | 7-1 | 8 |
| 2025-2026 | 2025-12-26 | 5-3 | 8 |
| 2025-2026 | 2026-02-21 | 5-3 | 8 |
| 2025-2026 | 2026-02-10 | 3-4 | 7 |
| 2025-2026 | 2026-03-21 | 6-1 | 7 |
| 2026-2027 | 2026-09-12 | 4-3 | 7 |
| 2026-2027 | 2026-09-20 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **476** (draws: **178**)
- Average winning margin: **1.67**

| margin | matches | pct |
|---|---|---|
| 1 | 270 | 56.7% |
| 2 | 132 | 27.7% |
| 3+ | 74 | 15.5% |

## 6. Margin by outcome

### Home wins
- Matches: **272** | avg margin: **1.72** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 151 | 55.5% |
| 2 | 72 | 26.5% |
| 3+ | 49 | 18.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **204** | avg margin: **1.59** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 119 | 58.3% |
| 2 | 60 | 29.4% |
| 3+ | 25 | 12.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 272 | 2-1 | 73 | 26.8% |
| draw | 178 | 1-1 | 94 | 52.8% |
| away | 204 | 1-2 | 59 | 28.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\cha\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\cha\charts\scoreline_analysis_total_goals.png)

