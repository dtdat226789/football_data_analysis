# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:57:22+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Scoreline frequency
- Matches analysed: **34** across **1** seasons.
- Distinct scorelines seen: **22**.

| scoreline | count | pct |
|---|---|---|
| 2-2 | 4 | 11.8% |
| 3-1 | 4 | 11.8% |
| 0-2 | 2 | 5.9% |
| 2-0 | 2 | 5.9% |
| 1-2 | 2 | 5.9% |
| 1-1 | 2 | 5.9% |
| 3-3 | 2 | 5.9% |
| 4-1 | 2 | 5.9% |
| 0-4 | 1 | 2.9% |
| 0-1 | 1 | 2.9% |
| 2-3 | 1 | 2.9% |
| 2-5 | 1 | 2.9% |
| 2-4 | 1 | 2.9% |
| 7-0 | 1 | 2.9% |
| 1-0 | 1 | 2.9% |
| 0-0 | 1 | 2.9% |
| 3-4 | 1 | 2.9% |
| 5-3 | 1 | 2.9% |
| 0-3 | 1 | 2.9% |
| 6-4 | 1 | 2.9% |

## 2. Scoreline frequency per season

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 4 | 11.8% |
| 3-1 | 4 | 11.8% |
| 0-2 | 2 | 5.9% |
| 2-0 | 2 | 5.9% |
| 1-2 | 2 | 5.9% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 1 | 2.9% |
| 1 | 2 | 5.9% |
| 2 | 6 | 17.6% |
| 3 | 4 | 11.8% |
| 4 | 9 | 26.5% |
| 5 | 3 | 8.8% |
| 6 | 4 | 11.8% |
| 7 | 3 | 8.8% |
| 8 | 1 | 2.9% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 2.9% |

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
- Decided matches: **25** (draws: **9**)
- Average winning margin: **2.32**

| margin | matches | pct |
|---|---|---|
| 1 | 7 | 28.0% |
| 2 | 11 | 44.0% |
| 3+ | 7 | 28.0% |

## 6. Margin by outcome

### Home wins
- Matches: **14** | avg margin: **2.64** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 2 | 14.3% |
| 2 | 8 | 57.1% |
| 3+ | 4 | 28.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **11** | avg margin: **1.91** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 5 | 45.5% |
| 2 | 3 | 27.3% |
| 3+ | 3 | 27.3% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 14 | 3-1 | 4 | 28.6% |
| draw | 9 | 2-2 | 4 | 44.4% |
| away | 11 | 0-2 | 2 | 18.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\develop21\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\develop21\charts\scoreline_analysis_total_goals.png)

