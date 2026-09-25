# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:55:08+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Scoreline frequency
- Matches analysed: **234** across **2** seasons.
- Distinct scorelines seen: **28**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 25 | 10.7% |
| 1-1 | 24 | 10.3% |
| 0-1 | 22 | 9.4% |
| 0-0 | 21 | 9.0% |
| 2-1 | 19 | 8.1% |
| 2-0 | 16 | 6.8% |
| 0-2 | 14 | 6.0% |
| 1-2 | 13 | 5.6% |
| 0-3 | 12 | 5.1% |
| 2-2 | 10 | 4.3% |
| 1-3 | 9 | 3.8% |
| 3-0 | 8 | 3.4% |
| 3-2 | 6 | 2.6% |
| 2-3 | 5 | 2.1% |
| 4-1 | 5 | 2.1% |
| 3-1 | 5 | 2.1% |
| 5-0 | 3 | 1.3% |
| 0-5 | 2 | 0.9% |
| 1-4 | 2 | 0.9% |
| 5-1 | 2 | 0.9% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 21 | 10.5% |
| 1-0 | 19 | 9.5% |
| 0-1 | 18 | 9.0% |
| 0-0 | 18 | 9.0% |
| 2-1 | 16 | 8.0% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 6 | 17.6% |
| 0-1 | 4 | 11.8% |
| 0-0 | 3 | 8.8% |
| 3-1 | 3 | 8.8% |
| 2-1 | 3 | 8.8% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 21 | 9.0% |
| 1 | 47 | 20.1% |
| 2 | 54 | 23.1% |
| 3 | 52 | 22.2% |
| 4 | 26 | 11.1% |
| 5 | 23 | 9.8% |
| 6 | 8 | 3.4% |
| 7 | 2 | 0.9% |
| 8 | 1 | 0.4% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2026-03-10 | 7-1 | 8 |
| 2025-2026 | 2026-04-06 | 7-0 | 7 |
| 2025-2026 | 2026-05-22 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **178** (draws: **56**)
- Average winning margin: **1.88**

| margin | matches | pct |
|---|---|---|
| 1 | 91 | 51.1% |
| 2 | 46 | 25.8% |
| 3+ | 41 | 23.0% |

## 6. Margin by outcome

### Home wins
- Matches: **93** | avg margin: **1.92** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 50 | 53.8% |
| 2 | 21 | 22.6% |
| 3+ | 22 | 23.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **85** | avg margin: **1.82** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 41 | 48.2% |
| 2 | 25 | 29.4% |
| 3+ | 19 | 22.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 93 | 1-0 | 25 | 26.9% |
| draw | 56 | 1-1 | 24 | 42.9% |
| away | 85 | 0-1 | 22 | 25.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\azer\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\azer\charts\scoreline_analysis_total_goals.png)

