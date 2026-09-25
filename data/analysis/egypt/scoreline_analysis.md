# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:57:32+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Scoreline frequency
- Matches analysed: **372** across **2** seasons.
- Distinct scorelines seen: **21**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 59 | 15.9% |
| 0-0 | 56 | 15.1% |
| 1-0 | 51 | 13.7% |
| 0-1 | 35 | 9.4% |
| 1-2 | 29 | 7.8% |
| 2-1 | 27 | 7.3% |
| 2-0 | 24 | 6.5% |
| 0-2 | 20 | 5.4% |
| 2-2 | 17 | 4.6% |
| 0-3 | 10 | 2.7% |
| 1-3 | 9 | 2.4% |
| 3-1 | 8 | 2.2% |
| 3-2 | 7 | 1.9% |
| 3-0 | 5 | 1.3% |
| 2-3 | 5 | 1.3% |
| 4-1 | 2 | 0.5% |
| 4-0 | 2 | 0.5% |
| 1-4 | 2 | 0.5% |
| 4-2 | 2 | 0.5% |
| 2-4 | 1 | 0.3% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 54 | 16.8% |
| 0-0 | 51 | 15.8% |
| 1-0 | 45 | 14.0% |
| 0-1 | 29 | 9.0% |
| 1-2 | 26 | 8.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 6 | 12.0% |
| 2-0 | 6 | 12.0% |
| 0-2 | 6 | 12.0% |
| 0-1 | 6 | 12.0% |
| 0-0 | 5 | 10.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 56 | 15.1% |
| 1 | 86 | 23.1% |
| 2 | 103 | 27.7% |
| 3 | 71 | 19.1% |
| 4 | 36 | 9.7% |
| 5 | 16 | 4.3% |
| 6 | 3 | 0.8% |
| 7 | 1 | 0.3% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-02-04 | 2-5 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **240** (draws: **132**)
- Average winning margin: **1.46**

| margin | matches | pct |
|---|---|---|
| 1 | 154 | 64.2% |
| 2 | 64 | 26.7% |
| 3+ | 22 | 9.2% |

## 6. Margin by outcome

### Home wins
- Matches: **128** | avg margin: **1.42** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 85 | 66.4% |
| 2 | 34 | 26.6% |
| 3+ | 9 | 7.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **112** | avg margin: **1.5** | max margin: **3**
| margin | matches | pct |
|---|---|---|
| 1 | 69 | 61.6% |
| 2 | 30 | 26.8% |
| 3+ | 13 | 11.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 128 | 1-0 | 51 | 39.8% |
| draw | 132 | 1-1 | 59 | 44.7% |
| away | 112 | 0-1 | 35 | 31.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\egypt\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\egypt\charts\scoreline_analysis_total_goals.png)

