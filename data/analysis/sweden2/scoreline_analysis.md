# Scoreline Analysis
- Report: `scoreline_analysis`
- Generated: 2026-09-23T13:48:52+00:00
- Script: `backend/scripts/analyze_scorelines.py` v1.0.0
- League: Superettan (Sweden)
- Scope: league `sweden2`

## 1. Scoreline frequency
- Matches analysed: **440** across **2** seasons.
- Distinct scorelines seen: **32**.

| scoreline | count | pct |
|---|---|---|
| 1-1 | 45 | 10.2% |
| 2-1 | 37 | 8.4% |
| 2-2 | 35 | 8.0% |
| 1-0 | 34 | 7.7% |
| 0-1 | 33 | 7.5% |
| 1-2 | 33 | 7.5% |
| 0-0 | 31 | 7.0% |
| 0-2 | 27 | 6.1% |
| 2-0 | 24 | 5.5% |
| 1-3 | 18 | 4.1% |
| 3-1 | 16 | 3.6% |
| 3-2 | 16 | 3.6% |
| 3-0 | 13 | 3.0% |
| 4-1 | 12 | 2.7% |
| 4-0 | 10 | 2.3% |
| 0-3 | 8 | 1.8% |
| 3-3 | 7 | 1.6% |
| 4-2 | 7 | 1.6% |
| 2-3 | 6 | 1.4% |
| 1-4 | 6 | 1.4% |

## 2. Scoreline frequency per season

### 2025
| scoreline | count | pct |
|---|---|---|
| 2-1 | 21 | 8.8% |
| 2-2 | 21 | 8.8% |
| 1-1 | 21 | 8.8% |
| 1-2 | 20 | 8.3% |
| 0-0 | 18 | 7.5% |

### 2026
| scoreline | count | pct |
|---|---|---|
| 1-1 | 24 | 12.0% |
| 1-0 | 17 | 8.5% |
| 0-1 | 16 | 8.0% |
| 2-1 | 16 | 8.0% |
| 2-2 | 14 | 7.0% |

## 3. Total-goal histogram
_10+ groups all matches with 10 or more total goals._

| total goals | matches | pct |
|---|---|---|
| 0 | 31 | 7.0% |
| 1 | 67 | 15.2% |
| 2 | 96 | 21.8% |
| 3 | 91 | 20.7% |
| 4 | 81 | 18.4% |
| 5 | 43 | 9.8% |
| 6 | 25 | 5.7% |
| 7 | 4 | 0.9% |
| 8 | 1 | 0.2% |
| 9 | 1 | 0.2% |
| 10+ | 0 | 0.0% |

## 4. Extreme scorelines
- Matches with 7+ total goals: **6**

| season | date | scoreline | total goals |
|---|---|---|---|
| 2025 | 2025-09-20 | 4-5 | 9 |
| 2025 | 2025-05-21 | 4-4 | 8 |
| 2025 | 2025-08-02 | 2-5 | 7 |
| 2025 | 2025-10-04 | 1-6 | 7 |
| 2026 | 2026-04-12 | 3-4 | 7 |
| 2026 | 2026-06-21 | 5-2 | 7 |

## 5. Margin-of-victory distribution (decided matches)
- Decided matches: **321** (draws: **119**)
- Average winning margin: **1.79**

| margin | matches | pct |
|---|---|---|
| 1 | 161 | 50.2% |
| 2 | 96 | 29.9% |
| 3+ | 64 | 19.9% |

## 6. Margin by outcome

### Home wins
- Matches: **178** | avg margin: **1.9** | max margin: **6**
| margin | matches | pct |
|---|---|---|
| 1 | 87 | 48.9% |
| 2 | 47 | 26.4% |
| 3+ | 44 | 24.7% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

### Away wins
- Matches: **143** | avg margin: **1.66** | max margin: **5**
| margin | matches | pct |
|---|---|---|
| 1 | 74 | 51.7% |
| 2 | 49 | 34.3% |
| 3+ | 20 | 14.0% |
- *Full match-by-match list available in `scoreline_analysis.json`.*

## 7. Most common exact score by outcome type
| outcome | matches | most common score | count | pct |
|---|---|---|---|---|
| home | 178 | 2-1 | 37 | 20.8% |
| draw | 119 | 1-1 | 45 | 37.8% |
| away | 143 | 0-1 | 33 | 23.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_scorelines.py` to regenerate.*

## Charts

![scoreline_analysis_top_scorelines](E:\football_data_analysis\data\analysis\sweden2\charts\scoreline_analysis_top_scorelines.png)
![scoreline_analysis_total_goals](E:\football_data_analysis\data\analysis\sweden2\charts\scoreline_analysis_total_goals.png)

