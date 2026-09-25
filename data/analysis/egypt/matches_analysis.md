# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:57:27+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 372 |
| Home wins | 128 (34.4%) |
| Draws | 132 (35.5%) |
| Away wins | 112 (30.1%) |
| Total goals | 754 |
| Average goals per match | 2.027 |
| Goalless matches | 56 (15.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 322 | 109 (33.9%) | 122 (37.9%) | 91 (28.3%) | 651 | 2.022 | 51 (15.8%) |
| 2026-2027 | 50 | 19 (38.0%) | 10 (20.0%) | 21 (42.0%) | 103 | 2.06 | 5 (10.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 65 (70.7%) | 22 (23.9%) | 5 (5.4%) | 92 |
| HT draw | 54 (28.6%) | 91 (48.1%) | 44 (23.3%) | 189 |
| HT away lead | 9 (9.9%) | 19 (20.9%) | 63 (69.2%) | 91 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.4%)
- Away comebacks (trailing at HT, won at FT): **5** (1.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Wadi Degla | Zamalek | 0-1 | 2-1 |
| 2025-2026 | Al Ahly | Zamalek | 0-1 | 2-1 |
| 2025-2026 | Ceramica Cleopatra | Petrojet | 0-1 | 2-1 |
| 2025-2026 | Enppi | Al Masry | 1-2 | 3-2 |
| 2025-2026 | Pharco | Haras El Hodood | 0-1 | 2-1 |
| 2025-2026 | National Bank Egypt | Arab Contractors | 0-1 | 2-1 |
| 2025-2026 | National Bank Egypt | Modern Sport | 0-1 | 2-1 |
| 2025-2026 | El Gouna | El Gaish | 0-1 | 2-1 |
| 2026-2027 | Al Ahly | Enppi | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Kahrabaa Ismailia | Wadi Degla | 1-0 | 1-4 |
| 2025-2026 | El Ismaily | El Gouna | 1-0 | 1-2 |
| 2025-2026 | Wadi Degla | Kahrabaa Ismailia | 1-0 | 1-2 |
| 2025-2026 | Petrojet | El Gouna | 1-0 | 1-2 |
| 2026-2027 | Ceramica Cleopatra | Al Qanah | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 92 | 65 (70.7%) | 22 (23.9%) | 5 (5.4%) |
| Away lead | 91 | 63 (69.2%) | 19 (20.9%) | 9 (9.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 54 | 28.6% |
| Draw | 91 | 48.1% |
| Away win | 44 | 23.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `316` of `372` (84.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 79 | 21.2% | 31 (39.2%) | 21 (26.6%) | 27 (34.2%) |
| 16-30 | 64 | 17.2% | 29 (45.3%) | 13 (20.3%) | 22 (34.4%) |
| 31-45 | 54 | 14.5% | 21 (38.9%) | 16 (29.6%) | 17 (31.5%) |
| 46-60 | 57 | 15.3% | 21 (36.8%) | 15 (26.3%) | 21 (36.8%) |
| 61-75 | 29 | 7.8% | 10 (34.5%) | 4 (13.8%) | 15 (51.7%) |
| 76-90 | 26 | 7.0% | 15 (57.7%) | 4 (15.4%) | 7 (26.9%) |
| 91-120 | 7 | 1.9% | 1 (14.3%) | 3 (42.9%) | 3 (42.9%) |

## 7. Goalless matches
- Overall: **56** of `372` (15.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 322 | 51 | 15.8% |
| 2026-2027 | 50 | 5 | 10.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\egypt\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\egypt\charts\matches_analysis_home_win_rate.png)

