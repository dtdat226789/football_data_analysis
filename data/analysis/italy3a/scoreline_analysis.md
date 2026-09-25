# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T11:02:13+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie C - Group A (Italy)
- Scope: league `italy3a`

## 1. Scoreline frequency
- Matches analysed: **440** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 57 | 13.0% |
| 1-0 | 51 | 11.6% |
| 0-1 | 48 | 10.9% |
| 0-0 | 48 | 10.9% |
| 2-1 | 37 | 8.4% |
| 1-2 | 35 | 8.0% |
| 2-2 | 29 | 6.6% |
| 2-0 | 26 | 5.9% |
| 0-2 | 19 | 4.3% |
| 3-1 | 19 | 4.3% |
| 3-0 | 11 | 2.5% |
| 1-3 | 11 | 2.5% |
| 2-3 | 9 | 2.0% |
| 0-3 | 7 | 1.6% |
| 4-1 | 6 | 1.4% |
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
| 0-0 | 11 | 18.3% |
| 1-0 | 8 | 13.3% |
| 1-2 | 8 | 13.3% |
| 2-2 | 7 | 11.7% |
| 0-1 | 5 | 8.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 48 | 10.9% |
| 1 | 99 | 22.5% |
| 2 | 102 | 23.2% |
| 3 | 90 | 20.5% |
| 4 | 65 | 14.8% |
| 5 | 27 | 6.1% |
| 6 | 6 | 1.4% |
| 7 | 2 | 0.5% |
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
- Decided matches: **302** (draws: **138**)
- Average winning margin: **1.58**

| margin | matches | pct |
|---|---|---|
| 1 | 185 | 61.3% |
| 2 | 77 | 25.5% |
| 3+ | 40 | 13.2% |

## 6. Margin by outcome

### Home wins
- Matches: **164** | avg margin: **1.66** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 93 | 56.7% |
| 2 | 45 | 27.4% |
| 3+ | 26 | 15.9% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **138** | avg margin: **1.49** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 92 | 66.7% |
| 2 | 32 | 23.2% |
| 3+ | 14 | 10.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 164 | 1-0 | 51 | 31.1% |
| draw | 138 | 1-1 | 57 | 41.3% |
| away | 138 | 0-1 | 48 | 34.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\italy3a\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\italy3a\charts\scoreline_analysis_total_goals.png)

