# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T15:58:11+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Scoreline frequency
- Matches analysed: **450** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 60 | 13.3% |
| 1-0 | 51 | 11.3% |
| 0-0 | 50 | 11.1% |
| 0-1 | 49 | 10.9% |
| 2-1 | 37 | 8.2% |
| 1-2 | 36 | 8.0% |
| 2-2 | 29 | 6.4% |
| 2-0 | 26 | 5.8% |
| 0-2 | 20 | 4.4% |
| 3-1 | 19 | 4.2% |
| 3-0 | 12 | 2.7% |
| 1-3 | 11 | 2.4% |
| 2-3 | 9 | 2.0% |
| 0-3 | 8 | 1.8% |
| 4-1 | 6 | 1.3% |
| 3-2 | 5 | 1.1% |
| 5-0 | 4 | 0.9% |
| 3-3 | 4 | 0.9% |
| 4-0 | 3 | 0.7% |
| 0-4 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 53 | 13.9% |
| 1-0 | 43 | 11.3% |
| 0-1 | 43 | 11.3% |
| 0-0 | 37 | 9.7% |
| 2-1 | 33 | 8.7% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-0 | 13 | 18.6% |
| 1-2 | 9 | 12.9% |
| 1-0 | 8 | 11.4% |
| 1-1 | 7 | 10.0% |
| 2-2 | 7 | 10.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 50 | 11.1% |
| 1 | 100 | 22.2% |
| 2 | 106 | 23.6% |
| 3 | 93 | 20.7% |
| 4 | 65 | 14.4% |
| 5 | 27 | 6.0% |
| 6 | 6 | 1.3% |
| 7 | 2 | 0.4% |
| 8 | 1 | 0.2% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-20 | 3-5 | 8 |
| 2025-2026 | 2025-12-14 | 5-2 | 7 |
| 2025-2026 | 2026-04-25 | 1-6 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **307** (draws: **143**)
- Average winning margin: **1.59**

| margin | matches | pct |
|---|---|---|
| 1 | 187 | 60.9% |
| 2 | 78 | 25.4% |
| 3+ | 42 | 13.7% |

## 6. Margin by outcome

### Home wins
- Matches: **165** | avg margin: **1.67** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 93 | 56.4% |
| 2 | 45 | 27.3% |
| 3+ | 27 | 16.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **142** | avg margin: **1.49** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 94 | 66.2% |
| 2 | 33 | 23.2% |
| 3+ | 15 | 10.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 165 | 1-0 | 51 | 30.9% |
| draw | 143 | 1-1 | 60 | 42.0% |
| away | 142 | 0-1 | 49 | 34.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy3a\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy3a\charts\scoreline_analysis_total_goals.png)

