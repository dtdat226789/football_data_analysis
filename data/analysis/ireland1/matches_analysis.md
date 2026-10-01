# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:55:27+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 339 |
| Home wins | 137 (40.4%) |
| Draws | 104 (30.7%) |
| Away wins | 98 (28.9%) |
| Total goals | 877 |
| Average goals per match | 2.587 |
| Goalless matches | 30 (8.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 180 | 77 (42.8%) | 52 (28.9%) | 51 (28.3%) | 437 | 2.428 | 15 (8.3%) |
| 2026 | 159 | 60 (37.7%) | 52 (32.7%) | 47 (29.6%) | 440 | 2.767 | 15 (9.4%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 85 (69.1%) | 21 (17.1%) | 17 (13.8%) | 123 |
| HT draw | 42 (32.1%) | 60 (45.8%) | 29 (22.1%) | 131 |
| HT away lead | 10 (11.8%) | 23 (27.1%) | 52 (61.2%) | 85 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (2.9%)
- Away comebacks (trailing at HT, won at FT): **17** (5.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Waterford | Cork City | 0-1 | 2-1 |
| 2025 | Derry City | Cork City | 0-1 | 2-1 |
| 2025 | Bohemians | St. Patricks | 0-1 | 2-1 |
| 2025 | Galway | Drogheda | 0-1 | 2-1 |
| 2025 | Shelbourne | St. Patricks | 0-1 | 2-1 |
| 2026 | Derry City | Sligo Rovers | 0-1 | 2-1 |
| 2026 | Derry City | Waterford | 0-1 | 4-2 |
| 2026 | St. Patricks | Drogheda | 0-1 | 4-1 |
| 2026 | Bohemians | Derry City | 0-1 | 5-3 |
| 2026 | Shamrock Rovers | Waterford | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Waterford | St. Patricks | 1-0 | 1-2 |
| 2025 | Shamrock Rovers | Bohemians | 2-0 | 2-3 |
| 2025 | Galway | Bohemians | 1-0 | 1-2 |
| 2025 | Cork City | Sligo Rovers | 1-0 | 2-3 |
| 2025 | Waterford | Sligo Rovers | 1-0 | 1-2 |
| 2025 | Bohemians | Shelbourne | 2-1 | 2-3 |
| 2026 | Drogheda | Shelbourne | 1-0 | 1-2 |
| 2026 | Drogheda | Galway | 2-1 | 2-3 |
| 2026 | Shelbourne | Drogheda | 2-0 | 3-4 |
| 2026 | Dundalk | Bohemians | 1-0 | 1-3 |
| 2026 | Shamrock Rovers | Sligo Rovers | 1-0 | 1-2 |
| 2026 | Bohemians | Shamrock Rovers | 1-0 | 1-2 |
| 2026 | Dundalk | Waterford | 2-1 | 2-3 |
| 2026 | Sligo Rovers | Shamrock Rovers | 1-0 | 1-2 |
| 2026 | Dundalk | Drogheda | 1-0 | 1-2 |
| 2026 | Drogheda | Dundalk | 2-1 | 2-3 |
| 2026 | Galway | Bohemians | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 123 | 85 (69.1%) | 21 (17.1%) | 17 (13.8%) |
| Away lead | 85 | 52 (61.2%) | 23 (27.1%) | 10 (11.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 42 | 32.1% |
| Draw | 60 | 45.8% |
| Away win | 29 | 22.1% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `309` of `339` (91.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 99 | 29.2% | 38 (38.4%) | 22 (22.2%) | 39 (39.4%) |
| 16-30 | 82 | 24.2% | 37 (45.1%) | 19 (23.2%) | 26 (31.7%) |
| 31-45 | 57 | 16.8% | 28 (49.1%) | 16 (28.1%) | 13 (22.8%) |
| 46-60 | 36 | 10.6% | 18 (50.0%) | 11 (30.6%) | 7 (19.4%) |
| 61-75 | 14 | 4.1% | 4 (28.6%) | 4 (28.6%) | 6 (42.9%) |
| 76-90 | 15 | 4.4% | 10 (66.7%) | 2 (13.3%) | 3 (20.0%) |
| 91-120 | 6 | 1.8% | 2 (33.3%) | 0 (0.0%) | 4 (66.7%) |

## 7. Goalless matches
- Overall: **30** of `339` (8.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 180 | 15 | 8.3% |
| 2026 | 159 | 15 | 9.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\ireland1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\ireland1\charts\matches_analysis_home_win_rate.png)

