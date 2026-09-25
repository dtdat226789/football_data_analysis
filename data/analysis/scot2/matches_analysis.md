# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:45:05+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 228 |
| Home wins | 99 (43.4%) |
| Draws | 62 (27.2%) |
| Away wins | 67 (29.4%) |
| Total goals | 691 |
| Average goals per match | 3.031 |
| Goalless matches | 9 (3.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 188 | 75 (39.9%) | 55 (29.3%) | 58 (30.9%) | 552 | 2.936 | 9 (4.8%) |
| 2026-2027 | 40 | 24 (60.0%) | 7 (17.5%) | 9 (22.5%) | 139 | 3.475 | 0 (0.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 67 (77.9%) | 14 (16.3%) | 5 (5.8%) | 86 |
| HT draw | 27 (35.1%) | 32 (41.6%) | 18 (23.4%) | 77 |
| HT away lead | 5 (7.7%) | 16 (24.6%) | 44 (67.7%) | 65 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **5** (2.2%)
- Away comebacks (trailing at HT, won at FT): **5** (2.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Annan | Elgin City | 0-1 | 3-2 |
| 2025-2026 | Elgin City | Forfar Athletic | 0-1 | 2-1 |
| 2025-2026 | Annan | Forfar Athletic | 0-1 | 3-1 |
| 2026-2027 | Clyde | Edinburgh City | 0-1 | 3-2 |
| 2026-2027 | Stranraer | Dumbarton | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Forfar Athletic | Dumbarton | 2-1 | 2-3 |
| 2025-2026 | Edinburgh City | Elgin City | 1-0 | 1-3 |
| 2025-2026 | Edinburgh City | Stirling | 1-0 | 1-4 |
| 2025-2026 | Clyde | East Kilbride | 1-0 | 1-3 |
| 2026-2027 | Annan | Spartans | 1-0 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 86 | 67 (77.9%) | 14 (16.3%) | 5 (5.8%) |
| Away lead | 65 | 44 (67.7%) | 16 (24.6%) | 5 (7.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 27 | 35.1% |
| Draw | 32 | 41.6% |
| Away win | 18 | 23.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `219` of `228` (96.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 70 | 30.7% | 33 (47.1%) | 15 (21.4%) | 22 (31.4%) |
| 16-30 | 60 | 26.3% | 24 (40.0%) | 16 (26.7%) | 20 (33.3%) |
| 31-45 | 41 | 18.0% | 19 (46.3%) | 9 (22.0%) | 13 (31.7%) |
| 46-60 | 24 | 10.5% | 14 (58.3%) | 6 (25.0%) | 4 (16.7%) |
| 61-75 | 17 | 7.5% | 5 (29.4%) | 7 (41.2%) | 5 (29.4%) |
| 76-90 | 7 | 3.1% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **9** of `228` (3.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 188 | 9 | 4.8% |
| 2026-2027 | 40 | 0 | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\scot2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\scot2\charts\matches_analysis_home_win_rate.png)

