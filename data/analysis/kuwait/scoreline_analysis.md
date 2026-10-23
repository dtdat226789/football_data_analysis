# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:00:59+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premier League (Kuwait)
- Scope: league `kuwait`

## 1. Scoreline frequency
- Matches analysed: **116** across **2** seasons.
- Distinct scorelines seen: **24**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 17 | 14.7% |
| 1-0 | 12 | 10.3% |
| 0-1 | 10 | 8.6% |
| 0-2 | 10 | 8.6% |
| 1-2 | 9 | 7.8% |
| 0-0 | 8 | 6.9% |
| 2-1 | 7 | 6.0% |
| 3-0 | 6 | 5.2% |
| 4-1 | 5 | 4.3% |
| 1-3 | 4 | 3.4% |
| 2-0 | 4 | 3.4% |
| 4-0 | 3 | 2.6% |
| 3-2 | 3 | 2.6% |
| 3-3 | 3 | 2.6% |
| 5-1 | 2 | 1.7% |
| 0-4 | 2 | 1.7% |
| 3-1 | 2 | 1.7% |
| 4-2 | 2 | 1.7% |
| 2-3 | 2 | 1.7% |
| 0-3 | 1 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 16 | 16.3% |
| 0-1 | 9 | 9.2% |
| 0-2 | 9 | 9.2% |
| 1-0 | 9 | 9.2% |
| 0-0 | 7 | 7.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 3 | 16.7% |
| 3-3 | 2 | 11.1% |
| 1-2 | 2 | 11.1% |
| 2-1 | 2 | 11.1% |
| 3-2 | 1 | 5.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 8 | 6.9% |
| 1 | 22 | 19.0% |
| 2 | 31 | 26.7% |
| 3 | 23 | 19.8% |
| 4 | 12 | 10.3% |
| 5 | 12 | 10.3% |
| 6 | 7 | 6.0% |
| 7 | 0 | 0.0% |
| 8 | 1 | 0.9% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-01-02 | 7-1 | 8 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **87** (draws: **29**)
- Average winning margin: **1.92**

| margin | matches | pct |
|---|---|---|
| 1 | 43 | 49.4% |
| 2 | 22 | 25.3% |
| 3+ | 22 | 25.3% |

## 6. Margin by outcome

### Home wins
- Matches: **48** | avg margin: **2.12** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 22 | 45.8% |
| 2 | 8 | 16.7% |
| 3+ | 18 | 37.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **39** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 21 | 53.8% |
| 2 | 14 | 35.9% |
| 3+ | 4 | 10.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 48 | 1-0 | 12 | 25.0% |
| draw | 29 | 1-1 | 17 | 58.6% |
| away | 39 | 0-1 | 10 | 25.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\kuwait\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\kuwait\charts\scoreline_analysis_total_goals.png)

