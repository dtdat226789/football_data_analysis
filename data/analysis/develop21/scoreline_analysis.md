# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-10-26T01:30:26+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Scoreline frequency
- Matches analysed: **61** across **1** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 2-2 | 8 | 13.1% |
| 3-1 | 7 | 11.5% |
| 0-2 | 4 | 6.6% |
| 2-0 | 4 | 6.6% |
| 1-2 | 4 | 6.6% |
| 4-1 | 4 | 6.6% |
| 1-1 | 3 | 4.9% |
| 1-0 | 3 | 4.9% |
| 2-1 | 3 | 4.9% |
| 0-4 | 2 | 3.3% |
| 0-1 | 2 | 3.3% |
| 2-5 | 2 | 3.3% |
| 3-3 | 2 | 3.3% |
| 3-4 | 2 | 3.3% |
| 2-3 | 1 | 1.6% |
| 2-4 | 1 | 1.6% |
| 7-0 | 1 | 1.6% |
| 0-0 | 1 | 1.6% |
| 5-3 | 1 | 1.6% |
| 0-3 | 1 | 1.6% |

## 2. Scoreline frequency per season

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 2-2 | 8 | 13.1% |
| 3-1 | 7 | 11.5% |
| 0-2 | 4 | 6.6% |
| 2-0 | 4 | 6.6% |
| 1-2 | 4 | 6.6% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 1 | 1.6% |
| 1 | 5 | 8.2% |
| 2 | 11 | 18.0% |
| 3 | 8 | 13.1% |
| 4 | 18 | 29.5% |
| 5 | 5 | 8.2% |
| 6 | 6 | 9.8% |
| 7 | 5 | 8.2% |
| 8 | 1 | 1.6% |
| 9 | 0 | 0.0% |
| 10+ | 1 | 1.6% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **7**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-15 | 6-4 | 10 |
| 2026-2027 | 2026-09-15 | 5-3 | 8 |
| 2026-2027 | 2026-08-25 | 2-5 | 7 |
| 2026-2027 | 2026-08-25 | 7-0 | 7 |
| 2026-2027 | 2026-09-01 | 3-4 | 7 |
| 2026-2027 | 2026-10-13 | 2-5 | 7 |
| 2026-2027 | 2026-10-23 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **47** (draws: **14**)
- Average winning margin: **2.15**

| margin | matches | pct |
|---|---|---|
| 1 | 15 | 31.9% |
| 2 | 20 | 42.6% |
| 3+ | 12 | 25.5% |

## 6. Margin by outcome

### Home wins
- Matches: **26** | avg margin: **2.27** | max margin: **7**
| margin | matches | pct |
|---|---|---|
| 1 | 6 | 23.1% |
| 2 | 14 | 53.8% |
| 3+ | 6 | 23.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **21** | avg margin: **2.0** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 9 | 42.9% |
| 2 | 6 | 28.6% |
| 3+ | 6 | 28.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 26 | 3-1 | 7 | 26.9% |
| draw | 14 | 2-2 | 8 | 57.1% |
| away | 21 | 0-2 | 4 | 19.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](charts/scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](charts/scoreline_analysis_total_goals.png)

