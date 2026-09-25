# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:50:32+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 120 |
| Home wins | 52 (43.3%) |
| Draws | 26 (21.7%) |
| Away wins | 42 (35.0%) |
| Total goals | 359 |
| Average goals per match | 2.992 |
| Goalless matches | 7 (5.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 108 | 44 (40.7%) | 25 (23.1%) | 39 (36.1%) | 324 | 3.0 | 6 (5.6%) |
| 2026-2027 | 12 | 8 (66.7%) | 1 (8.3%) | 3 (25.0%) | 35 | 2.917 | 1 (8.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 30 (88.2%) | 4 (11.8%) | 0 (0.0%) | 34 |
| HT draw | 18 (36.7%) | 16 (32.7%) | 15 (30.6%) | 49 |
| HT away lead | 4 (10.8%) | 6 (16.2%) | 27 (73.0%) | 37 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (3.3%)
- Away comebacks (trailing at HT, won at FT): **0** (0.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Westerlo W | Gent W | 0-1 | 2-1 |
| 2025-2026 | RSC Anderlecht W | Club Brugge W | 0-1 | 2-1 |
| 2025-2026 | Club Brugge W | St. Liege W | 0-1 | 4-2 |
| 2025-2026 | Leuven W | St. Liege W | 0-1 | 2-1 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 34 | 30 (88.2%) | 4 (11.8%) | 0 (0.0%) |
| Away lead | 37 | 27 (73.0%) | 6 (16.2%) | 4 (10.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 18 | 36.7% |
| Draw | 16 | 32.7% |
| Away win | 15 | 30.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `113` of `120` (94.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 41 | 34.2% | 17 (41.5%) | 5 (12.2%) | 19 (46.3%) |
| 16-30 | 31 | 25.8% | 11 (35.5%) | 8 (25.8%) | 12 (38.7%) |
| 31-45 | 19 | 15.8% | 12 (63.2%) | 2 (10.5%) | 5 (26.3%) |
| 46-60 | 12 | 10.0% | 7 (58.3%) | 2 (16.7%) | 3 (25.0%) |
| 61-75 | 4 | 3.3% | 2 (50.0%) | 2 (50.0%) | 0 (0.0%) |
| 76-90 | 6 | 5.0% | 3 (50.0%) | 0 (0.0%) | 3 (50.0%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **7** of `120` (5.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 108 | 6 | 5.6% |
| 2026-2027 | 12 | 1 | 8.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wbelgium1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wbelgium1\charts\matches_analysis_home_win_rate.png)

