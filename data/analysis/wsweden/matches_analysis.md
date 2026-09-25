# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:51:26+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Allsvenskan Women (Sweden)
- Scope: league `wsweden`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 315 |
| Home wins | 145 (46.0%) |
| Draws | 52 (16.5%) |
| Away wins | 118 (37.5%) |
| Total goals | 987 |
| Average goals per match | 3.133 |
| Goalless matches | 8 (2.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 182 | 85 (46.7%) | 25 (13.7%) | 72 (39.6%) | 606 | 3.33 | 4 (2.2%) |
| 2026 | 133 | 60 (45.1%) | 27 (20.3%) | 46 (34.6%) | 381 | 2.865 | 4 (3.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 104 (82.5%) | 10 (7.9%) | 12 (9.5%) | 126 |
| HT draw | 34 (34.7%) | 29 (29.6%) | 35 (35.7%) | 98 |
| HT away lead | 7 (7.7%) | 13 (14.3%) | 71 (78.0%) | 91 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.2%)
- Away comebacks (trailing at HT, won at FT): **12** (3.8%)

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
| Home lead | 126 | 104 (82.5%) | 10 (7.9%) | 12 (9.5%) |
| Away lead | 91 | 71 (78.0%) | 13 (14.3%) | 7 (7.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 34 | 34.7% |
| Draw | 29 | 29.6% |
| Away win | 35 | 35.7% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `307` of `315` (97.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 122 | 38.7% | 68 (55.7%) | 18 (14.8%) | 36 (29.5%) |
| 16-30 | 80 | 25.4% | 35 (43.8%) | 13 (16.2%) | 32 (40.0%) |
| 31-45 | 41 | 13.0% | 17 (41.5%) | 6 (14.6%) | 18 (43.9%) |
| 46-60 | 35 | 11.1% | 15 (42.9%) | 3 (8.6%) | 17 (48.6%) |
| 61-75 | 17 | 5.4% | 6 (35.3%) | 4 (23.5%) | 7 (41.2%) |
| 76-90 | 11 | 3.5% | 3 (27.3%) | 0 (0.0%) | 8 (72.7%) |
| 91-120 | 1 | 0.3% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **8** of `315` (2.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 182 | 4 | 2.2% |
| 2026 | 133 | 4 | 3.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wsweden\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wsweden\charts\matches_analysis_home_win_rate.png)

