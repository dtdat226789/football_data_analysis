# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:10:58+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super League Women (Belgium)
- Scope: league `wbelgium1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 124 |
| Home wins | 54 (43.5%) |
| Draws | 27 (21.8%) |
| Away wins | 43 (34.7%) |
| Total goals | 372 |
| Average goals per match | 3.000 |
| Goalless matches | 7 (5.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 108 | 44 (40.7%) | 25 (23.1%) | 39 (36.1%) | 324 | 3.0 | 6 (5.6%) |
| 2026-2027 | 16 | 10 (62.5%) | 2 (12.5%) | 4 (25.0%) | 48 | 3.0 | 1 (6.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 30 (85.7%) | 4 (11.4%) | 1 (2.9%) | 35 |
| HT draw | 20 (38.5%) | 17 (32.7%) | 15 (28.8%) | 52 |
| HT away lead | 4 (10.8%) | 6 (16.2%) | 27 (73.0%) | 37 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (3.2%)
- Away comebacks (trailing at HT, won at FT): **1** (0.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Westerlo W | Gent W | 0-1 | 2-1 |
| 2025-2026 | RSC Anderlecht W | Club Brugge W | 0-1 | 2-1 |
| 2025-2026 | Club Brugge W | St. Liege W | 0-1 | 4-2 |
| 2025-2026 | Leuven W | St. Liege W | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026-2027 | Waregem W | St. Liege W | 3-0 | 3-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 35 | 30 (85.7%) | 4 (11.4%) | 1 (2.9%) |
| Away lead | 37 | 27 (73.0%) | 6 (16.2%) | 4 (10.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 20 | 38.5% |
| Draw | 17 | 32.7% |
| Away win | 15 | 28.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `117` of `124` (94.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 41 | 33.1% | 17 (41.5%) | 5 (12.2%) | 19 (46.3%) |
| 16-30 | 32 | 25.8% | 11 (34.4%) | 8 (25.0%) | 13 (40.6%) |
| 31-45 | 19 | 15.3% | 12 (63.2%) | 2 (10.5%) | 5 (26.3%) |
| 46-60 | 12 | 9.7% | 7 (58.3%) | 2 (16.7%) | 3 (25.0%) |
| 61-75 | 6 | 4.8% | 3 (50.0%) | 3 (50.0%) | 0 (0.0%) |
| 76-90 | 7 | 5.6% | 4 (57.1%) | 0 (0.0%) | 3 (42.9%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **7** of `124` (5.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 108 | 6 | 5.6% |
| 2026-2027 | 16 | 1 | 6.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wbelgium1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wbelgium1\charts\matches_analysis_home_win_rate.png)

