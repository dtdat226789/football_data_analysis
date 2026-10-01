# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:11:04+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Scoreline frequency
- Matches analysed: **124** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 2-0 | 17 | 13.7% |
| 2-1 | 14 | 11.3% |
| 1-1 | 13 | 10.5% |
| 0-2 | 8 | 6.5% |
| 1-2 | 8 | 6.5% |
| 0-0 | 7 | 5.6% |
| 1-0 | 7 | 5.6% |
| 1-3 | 6 | 4.8% |
| 2-2 | 5 | 4.0% |
| 4-1 | 4 | 3.2% |
| 0-3 | 4 | 3.2% |
| 0-1 | 4 | 3.2% |
| 1-5 | 3 | 2.4% |
| 2-3 | 3 | 2.4% |
| 4-2 | 3 | 2.4% |
| 3-0 | 3 | 2.4% |
| 0-5 | 2 | 1.6% |
| 3-4 | 2 | 1.6% |
| 3-3 | 2 | 1.6% |
| 3-2 | 2 | 1.6% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 2-0 | 14 | 13.0% |
| 2-1 | 14 | 13.0% |
| 1-1 | 12 | 11.1% |
| 0-2 | 7 | 6.5% |
| 1-2 | 7 | 6.5% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 3 | 18.8% |
| 2-0 | 3 | 18.8% |
| 3-1 | 1 | 6.2% |
| 4-0 | 1 | 6.2% |
| 6-1 | 1 | 6.2% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 7 | 5.6% |
| 1 | 11 | 8.9% |
| 2 | 38 | 30.6% |
| 3 | 29 | 23.4% |
| 4 | 14 | 11.3% |
| 5 | 12 | 9.7% |
| 6 | 9 | 7.3% |
| 7 | 4 | 3.2% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-12-20 | 1-6 | 7 |
| 2025-2026 | 2026-01-31 | 3-4 | 7 |
| 2026-2027 | 2026-09-06 | 6-1 | 7 |
| 2026-2027 | 2026-09-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **97** (draws: **27**)
- Average winning margin: **1.98**

| margin | matches | pct |
|---|---|---|
| 1 | 40 | 41.2% |
| 2 | 35 | 36.1% |
| 3+ | 22 | 22.7% |

## 6. Margin by outcome

### Home wins
- Matches: **54** | avg margin: **1.87** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 23 | 42.6% |
| 2 | 21 | 38.9% |
| 3+ | 10 | 18.5% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **43** | avg margin: **2.12** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 17 | 39.5% |
| 2 | 14 | 32.6% |
| 3+ | 12 | 27.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 54 | 2-0 | 17 | 31.5% |
| draw | 27 | 1-1 | 13 | 48.1% |
| away | 43 | 0-2 | 8 | 18.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\wbelgium1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\wbelgium1\charts\scoreline_analysis_total_goals.png)

