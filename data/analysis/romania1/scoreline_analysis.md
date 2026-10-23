# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-29T16:04:51+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Scoreline frequency
- Matches analysed: **429** across **2** seasons.
- Distinct scorelines seen: **27**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 56 | 13.1% |
| 1-0 | 51 | 11.9% |
| 2-1 | 42 | 9.8% |
| 0-1 | 42 | 9.8% |
| 0-0 | 32 | 7.5% |
| 2-0 | 25 | 5.8% |
| 2-2 | 24 | 5.6% |
| 0-2 | 23 | 5.4% |
| 3-1 | 21 | 4.9% |
| 1-2 | 20 | 4.7% |
| 4-0 | 15 | 3.5% |
| 3-2 | 12 | 2.8% |
| 3-0 | 12 | 2.8% |
| 2-3 | 10 | 2.3% |
| 4-1 | 7 | 1.6% |
| 1-3 | 6 | 1.4% |
| 3-3 | 5 | 1.2% |
| 0-3 | 5 | 1.2% |
| 5-0 | 5 | 1.2% |
| 1-4 | 3 | 0.7% |

## 2. Scoreline frequency per season

### 2025-2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 47 | 13.4% |
| 1-0 | 39 | 11.1% |
| 0-1 | 37 | 10.6% |
| 2-1 | 35 | 10.0% |
| 0-0 | 25 | 7.1% |

### 2026-2027
| scoreline | count | pct |
|---|---|---|
| 1-0 | 12 | 15.2% |
| 1-1 | 9 | 11.4% |
| 2-1 | 7 | 8.9% |
| 0-0 | 7 | 8.9% |
| 2-2 | 5 | 6.3% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 32 | 7.5% |
| 1 | 93 | 21.7% |
| 2 | 104 | 24.2% |
| 3 | 79 | 18.4% |
| 4 | 68 | 15.9% |
| 5 | 37 | 8.6% |
| 6 | 12 | 2.8% |
| 7 | 4 | 0.9% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **4**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025-2026 | 2025-07-21 | 6-1 | 7 |
| 2025-2026 | 2025-08-02 | 4-3 | 7 |
| 2025-2026 | 2025-08-02 | 4-3 | 7 |
| 2025-2026 | 2026-05-24 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **312** (draws: **117**)
- Average winning margin: **1.7**

| margin | matches | pct |
|---|---|---|
| 1 | 180 | 57.7% |
| 2 | 78 | 25.0% |
| 3+ | 54 | 17.3% |

## 6. Margin by outcome

### Home wins
- Matches: **199** | avg margin: **1.82** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 108 | 54.3% |
| 2 | 48 | 24.1% |
| 3+ | 43 | 21.6% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **113** | avg margin: **1.49** | max margin: **4**
| margin | matches | pct |
|---|---|---|
| 1 | 72 | 63.7% |
| 2 | 30 | 26.5% |
| 3+ | 11 | 9.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 199 | 1-0 | 51 | 25.6% |
| draw | 117 | 1-1 | 56 | 47.9% |
| away | 113 | 0-1 | 42 | 37.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\romania1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\romania1\charts\scoreline_analysis_total_goals.png)

