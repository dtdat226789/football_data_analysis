# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:58:41+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie C - Group B (Italy)
- Scope: league `italy3b`

## 1. Scoreline frequency
- Matches analysed: **426** across **2** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 65 | 15.3% |
| 1-0 | 52 | 12.2% |
| 2-1 | 44 | 10.3% |
| 0-0 | 41 | 9.6% |
| 0-1 | 41 | 9.6% |
| 2-0 | 32 | 7.5% |
| 1-2 | 28 | 6.6% |
| 2-2 | 24 | 5.6% |
| 0-2 | 22 | 5.2% |
| 3-1 | 11 | 2.6% |
| 3-0 | 11 | 2.6% |
| 0-3 | 10 | 2.3% |
| 3-2 | 8 | 1.9% |
| 1-3 | 8 | 1.9% |
| 2-3 | 7 | 1.6% |
| 2-4 | 4 | 0.9% |
| 4-2 | 4 | 0.9% |
| 1-4 | 3 | 0.7% |
| 0-4 | 3 | 0.7% |
| 3-3 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 55 | 15.4% |
| 1-0 | 45 | 12.6% |
| 0-1 | 38 | 10.6% |
| 2-1 | 36 | 10.1% |
| 0-0 | 35 | 9.8% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-1 | 10 | 14.5% |
| 2-0 | 8 | 11.6% |
| 2-1 | 8 | 11.6% |
| 1-0 | 7 | 10.1% |
| 0-0 | 6 | 8.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 41 | 9.6% |
| 1 | 93 | 21.8% |
| 2 | 119 | 27.9% |
| 3 | 93 | 21.8% |
| 4 | 47 | 11.0% |
| 5 | 20 | 4.7% |
| 6 | 12 | 2.8% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **1**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-08-29 | 6-3 | 9 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **293** (draws: **133**)
- Average winning margin: **1.52**

| margin | matches | pct |
|---|---|---|
| 1 | 180 | 61.4% |
| 2 | 81 | 27.6% |
| 3+ | 32 | 10.9% |

## 6. Margin by outcome

### Home wins
- Matches: **167** | avg margin: **1.5** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 104 | 62.3% |
| 2 | 47 | 28.1% |
| 3+ | 16 | 9.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **126** | avg margin: **1.55** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 76 | 60.3% |
| 2 | 34 | 27.0% |
| 3+ | 16 | 12.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 167 | 1-0 | 52 | 31.1% |
| draw | 133 | 1-1 | 65 | 48.9% |
| away | 126 | 0-1 | 41 | 32.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy3b\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy3b\charts\scoreline_analysis_total_goals.png)

