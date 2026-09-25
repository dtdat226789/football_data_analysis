# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T10:55:30+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Serie A Betano (Brazil)
- Scope: league `brazil1`

## 1. Scoreline frequency
- Matches analysed: **657** across **2** seasons.
- Distinct scorelines seen: **31**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 87 | 13.2% |
| 1-0 | 79 | 12.0% |
| 2-1 | 72 | 11.0% |
| 2-0 | 61 | 9.3% |
| 0-1 | 44 | 6.7% |
| 0-0 | 43 | 6.5% |
| 1-2 | 43 | 6.5% |
| 2-2 | 35 | 5.3% |
| 3-0 | 29 | 4.4% |
| 3-1 | 26 | 4.0% |
| 0-2 | 25 | 3.8% |
| 3-2 | 18 | 2.7% |
| 1-3 | 14 | 2.1% |
| 4-1 | 12 | 1.8% |
| 2-3 | 12 | 1.8% |
| 3-3 | 11 | 1.7% |
| 0-3 | 10 | 1.5% |
| 4-0 | 6 | 0.9% |
| 0-4 | 6 | 0.9% |
| 4-2 | 5 | 0.8% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 1-0 | 53 | 13.9% |
| 1-1 | 46 | 12.1% |
| 2-1 | 37 | 9.7% |
| 2-0 | 33 | 8.7% |
| 0-0 | 27 | 7.1% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 41 | 14.8% |
| 2-1 | 35 | 12.6% |
| 2-0 | 28 | 10.1% |
| 1-0 | 26 | 9.4% |
| 1-2 | 24 | 8.7% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 43 | 6.5% |
| 1 | 123 | 18.7% |
| 2 | 173 | 26.3% |
| 3 | 154 | 23.4% |
| 4 | 87 | 13.2% |
| 5 | 48 | 7.3% |
| 6 | 26 | 4.0% |
| 7 | 1 | 0.2% |
| 8 | 2 | 0.3% |
| 9 | 0 | 0.0% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **3**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-08-26 | 8-0 | 8 |
| 2026 | 2026-02-05 | 5-3 | 8 |
| 2025 | 2025-10-05 | 4-3 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **481** (draws: **176**)
- Average winning margin: **1.69**

| margin | matches | pct |
|---|---|---|
| 1 | 269 | 55.9% |
| 2 | 133 | 27.7% |
| 3+ | 79 | 16.4% |

## 6. Margin by outcome

### Home wins
- Matches: **321** | avg margin: **1.74** | max margin: **8**
| margin | matches | pct |
|---|---|---|
| 1 | 170 | 53.0% |
| 2 | 93 | 29.0% |
| 3+ | 58 | 18.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **160** | avg margin: **1.59** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 99 | 61.9% |
| 2 | 40 | 25.0% |
| 3+ | 21 | 13.1% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 321 | 1-0 | 79 | 24.6% |
| draw | 176 | 1-1 | 87 | 49.4% |
| away | 160 | 0-1 | 44 | 27.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\brazil1\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\brazil1\charts\scoreline_analysis_total_goals.png)

