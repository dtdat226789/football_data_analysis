# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:51:44+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League (Greece)
- Scope: league `greece1`

## 1. Scoreline frequency
- Matches analysed: **281** across **2** seasons.
- Distinct scorelines seen: **26**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 41 | 14.6% |
| 0-1 | 24 | 8.5% |
| 0-0 | 24 | 8.5% |
| 1-0 | 23 | 8.2% |
| 1-2 | 20 | 7.1% |
| 3-0 | 19 | 6.8% |
| 2-0 | 18 | 6.4% |
| 0-2 | 18 | 6.4% |
| 2-1 | 18 | 6.4% |
| 3-1 | 13 | 4.6% |
| 2-2 | 11 | 3.9% |
| 3-2 | 8 | 2.8% |
| 0-3 | 7 | 2.5% |
| 4-0 | 6 | 2.1% |
| 2-3 | 6 | 2.1% |
| 1-3 | 5 | 1.8% |
| 4-1 | 3 | 1.1% |
| 1-4 | 3 | 1.1% |
| 5-0 | 2 | 0.7% |
| 6-0 | 2 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 35 | 14.2% |
| 1-0 | 22 | 8.9% |
| 0-0 | 22 | 8.9% |
| 0-1 | 20 | 8.1% |
| 3-0 | 18 | 7.3% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 6 | 17.1% |
| 2-0 | 4 | 11.4% |
| 3-1 | 4 | 11.4% |
| 0-1 | 4 | 11.4% |
| 1-2 | 3 | 8.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 24 | 8.5% |
| 1 | 47 | 16.7% |
| 2 | 77 | 27.4% |
| 3 | 64 | 22.8% |
| 4 | 37 | 13.2% |
| 5 | 24 | 8.5% |
| 6 | 5 | 1.8% |
| 7 | 3 | 1.1% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-10-04 | 2-5 | 7 |
| 2025-2026 | 2025-11-09 | 5-2 | 7 |
| 2025-2026 | 2026-05-03 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **204** (draws: **77**)
- Average winning margin: **1.86**

| margin | matches | pct |
|---|---|---|
| 1 | 99 | 48.5% |
| 2 | 56 | 27.5% |
| 3+ | 49 | 24.0% |

## 6. Margin by outcome

### Home wins
- Matches: **116** | avg margin: **2.01** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 49 | 42.2% |
| 2 | 33 | 28.4% |
| 3+ | 34 | 29.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **88** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 50 | 56.8% |
| 2 | 23 | 26.1% |
| 3+ | 15 | 17.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 116 | 1-0 | 23 | 19.8% |
| draw | 77 | 1-1 | 41 | 53.2% |
| away | 88 | 0-1 | 24 | 27.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\greece1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\greece1\charts\scoreline_analysis_total_goals.png)

