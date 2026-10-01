# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:24:31+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 322 |
| Home wins | 149 (46.3%) |
| Draws | 52 (16.1%) |
| Away wins | 121 (37.6%) |
| Total goals | 1013 |
| Average goals per match | 3.146 |
| Goalless matches | 8 (2.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 182 | 85 (46.7%) | 25 (13.7%) | 72 (39.6%) | 606 | 3.33 | 4 (2.2%) |
| 2026 | 140 | 64 (45.7%) | 27 (19.3%) | 49 (35.0%) | 407 | 2.907 | 4 (2.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 106 (82.8%) | 10 (7.8%) | 12 (9.4%) | 128 |
| HT draw | 36 (36.0%) | 29 (29.0%) | 35 (35.0%) | 100 |
| HT away lead | 7 (7.4%) | 13 (13.8%) | 74 (78.7%) | 94 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.2%)
- Away comebacks (trailing at HT, won at FT): **12** (3.7%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Djurgarden W | Kristianstad W | 0-1 | 2-1 |
| 2025 | Pitea W | Alingsas W | 0-1 | 2-1 |
| 2025 | Hammarby W | Vittsjo W | 0-1 | 3-2 |
| 2025 | Kristianstad W | Linkoping W | 0-1 | 3-1 |
| 2025 | Alingsas W | IF Brommapojkarna W | 1-2 | 3-2 |
| 2025 | Djurgarden W | Alingsas W | 0-1 | 5-1 |
| 2026 | Vaxjo DFF W | IF Brommapojkarna W | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Vaxjo DFF W | Kristianstad W | 2-1 | 2-3 |
| 2025 | Hacken W | Norrkoping W | 1-0 | 1-3 |
| 2025 | IF Brommapojkarna W | Djurgarden W | 1-0 | 1-2 |
| 2025 | Rosengard W | AIK W | 1-0 | 1-2 |
| 2025 | Pitea W | IF Brommapojkarna W | 1-0 | 1-2 |
| 2025 | Vittsjo W | Kristianstad W | 1-0 | 1-2 |
| 2025 | AIK W | Vittsjo W | 1-0 | 1-2 |
| 2025 | AIK W | Norrkoping W | 1-0 | 1-2 |
| 2026 | Rosengard W | AIK W | 1-0 | 1-2 |
| 2026 | Pitea W | IF Brommapojkarna W | 1-0 | 1-2 |
| 2026 | IF Brommapojkarna W | Vittsjo W | 1-0 | 1-2 |
| 2026 | AIK W | Vittsjo W | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 128 | 106 (82.8%) | 10 (7.8%) | 12 (9.4%) |
| Away lead | 94 | 74 (78.7%) | 13 (13.8%) | 7 (7.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 36 | 36.0% |
| Draw | 29 | 29.0% |
| Away win | 35 | 35.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `314` of `322` (97.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 125 | 38.8% | 70 (56.0%) | 18 (14.4%) | 37 (29.6%) |
| 16-30 | 83 | 25.8% | 36 (43.4%) | 13 (15.7%) | 34 (41.0%) |
| 31-45 | 41 | 12.7% | 17 (41.5%) | 6 (14.6%) | 18 (43.9%) |
| 46-60 | 35 | 10.9% | 15 (42.9%) | 3 (8.6%) | 17 (48.6%) |
| 61-75 | 17 | 5.3% | 6 (35.3%) | 4 (23.5%) | 7 (41.2%) |
| 76-90 | 12 | 3.7% | 4 (33.3%) | 0 (0.0%) | 8 (66.7%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **8** of `322` (2.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 182 | 4 | 2.2% |
| 2026 | 140 | 4 | 2.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wsweden\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wsweden\charts\matches_analysis_home_win_rate.png)

