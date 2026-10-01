# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:07:38+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Segunda RFEF - Group 4 (Spain)
- Scope: league `segunda4`

## 1. Scoreline frequency
- Matches analysed: **359** across **2** seasons.
- Distinct scorelines seen: **25**.

| scoreline | count | pct |
|---|---|---|
| 1-0 | 62 | 17.3% |
| 1-1 | 50 | 13.9% |
| 2-1 | 41 | 11.4% |
| 0-0 | 33 | 9.2% |
| 1-2 | 27 | 7.5% |
| 0-1 | 27 | 7.5% |
| 2-0 | 23 | 6.4% |
| 3-2 | 13 | 3.6% |
| 3-1 | 13 | 3.6% |
| 0-2 | 11 | 3.1% |
| 3-0 | 11 | 3.1% |
| 1-3 | 10 | 2.8% |
| 2-2 | 10 | 2.8% |
| 0-3 | 6 | 1.7% |
| 4-0 | 5 | 1.4% |
| 2-3 | 3 | 0.8% |
| 4-2 | 3 | 0.8% |
| 2-4 | 2 | 0.6% |
| 5-0 | 2 | 0.6% |
| 4-1 | 2 | 0.6% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-0 | 59 | 18.3% |
| 1-1 | 47 | 14.6% |
| 2-1 | 38 | 11.8% |
| 0-0 | 28 | 8.7% |
| 1-2 | 24 | 7.4% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 0-0 | 5 | 13.9% |
| 0-1 | 4 | 11.1% |
| 2-1 | 3 | 8.3% |
| 1-1 | 3 | 8.3% |
| 1-2 | 3 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 33 | 9.2% |
| 1 | 89 | 24.8% |
| 2 | 84 | 23.4% |
| 3 | 85 | 23.7% |
| 4 | 38 | 10.6% |
| 5 | 21 | 5.8% |
| 6 | 7 | 1.9% |
| 7 | 1 | 0.3% |
| 8 | 1 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **2**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2026-2027 | 2026-09-27 | 6-2 | 8 |
| 2025-2026 | 2026-04-26 | 3-4 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **265** (draws: **94**)
- Average winning margin: **1.49**

| margin | matches | pct |
|---|---|---|
| 1 | 174 | 65.7% |
| 2 | 62 | 23.4% |
| 3+ | 29 | 10.9% |

## 6. Margin by outcome

### Home wins
- Matches: **177** | avg margin: **1.53** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 116 | 65.5% |
| 2 | 39 | 22.0% |
| 3+ | 22 | 12.4% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **88** | avg margin: **1.42** | max margin: **3**
| margin | matches | pct |
|---|---|---|
| 1 | 58 | 65.9% |
| 2 | 23 | 26.1% |
| 3+ | 7 | 8.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 177 | 1-0 | 62 | 35.0% |
| draw | 94 | 1-1 | 50 | 53.2% |
| away | 88 | 1-2 | 27 | 30.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\segunda4\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\segunda4\charts\scoreline_analysis_total_goals.png)

