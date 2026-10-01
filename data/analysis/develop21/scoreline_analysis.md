# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:48:20+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Scoreline frequency
- Matches analysed: **40** across **1** seasons.
- Distinct scorelines seen: **23**.

| scoreline | count | pct |
|---|---|---|
| 2-2 | 5 | 12.5% |
| 3-1 | 5 | 12.5% |
| 0-2 | 3 | 7.5% |
| 4-1 | 3 | 7.5% |
| 2-0 | 2 | 5.0% |
| 1-2 | 2 | 5.0% |
| 1-1 | 2 | 5.0% |
| 3-3 | 2 | 5.0% |
| 2-1 | 2 | 5.0% |
| 0-4 | 1 | 2.5% |
| 0-1 | 1 | 2.5% |
| 2-3 | 1 | 2.5% |
| 2-5 | 1 | 2.5% |
| 2-4 | 1 | 2.5% |
| 7-0 | 1 | 2.5% |
| 1-0 | 1 | 2.5% |
| 3-4 | 1 | 2.5% |
| 0-0 | 1 | 2.5% |
| 5-3 | 1 | 2.5% |
| 6-4 | 1 | 2.5% |

## 2. Scoreline frequency per season

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 5 | 12.5% |
| 3-1 | 5 | 12.5% |
| 0-2 | 3 | 7.5% |
| 4-1 | 3 | 7.5% |
| 2-0 | 2 | 5.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 1 | 2.5% |
| 1 | 2 | 5.0% |
| 2 | 7 | 17.5% |
| 3 | 5 | 12.5% |
| 4 | 11 | 27.5% |
| 5 | 4 | 10.0% |
| 6 | 5 | 12.5% |
| 7 | 3 | 7.5% |
| 8 | 1 | 2.5% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 2.5% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **5**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-15 | 6-4 | 10 |
| 2026-2027 | 2026-09-15 | 5-3 | 8 |
| 2026-2027 | 2026-08-25 | 2-5 | 7 |
| 2026-2027 | 2026-08-25 | 7-0 | 7 |
| 2026-2027 | 2026-09-01 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **30** (draws: **10**)
- Average winning margin: **2.27**

| margin | matches | pct |
|---|---|---|
| 1 | 8 | 26.7% |
| 2 | 14 | 46.7% |
| 3+ | 8 | 26.7% |

## 6. Margin by outcome

### Home wins
- Matches: **18** | avg margin: **2.5** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 3 | 16.7% |
| 2 | 10 | 55.6% |
| 3+ | 5 | 27.8% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **12** | avg margin: **1.92** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 5 | 41.7% |
| 2 | 4 | 33.3% |
| 3+ | 3 | 25.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 18 | 3-1 | 5 | 27.8% |
| draw | 10 | 2-2 | 5 | 50.0% |
| away | 12 | 0-2 | 3 | 25.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\develop21\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\develop21\charts\scoreline_analysis_total_goals.png)

