# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:45:22+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 333 |
| Home wins | 139 (41.7%) |
| Draws | 89 (26.7%) |
| Away wins | 105 (31.5%) |
| Total goals | 847 |
| Average goals per match | 2.544 |
| Goalless matches | 29 (8.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 127 (41.5%) | 84 (27.5%) | 95 (31.0%) | 776 | 2.536 | 28 (9.2%) |
| 2026-2027 | 27 | 12 (44.4%) | 5 (18.5%) | 10 (37.0%) | 71 | 2.63 | 1 (3.7%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 74 (74.0%) | 20 (20.0%) | 6 (6.0%) | 100 |
| HT draw | 59 (38.8%) | 55 (36.2%) | 38 (25.0%) | 152 |
| HT away lead | 5 (6.2%) | 14 (17.5%) | 61 (76.2%) | 80 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **5** (1.5%)
- Away comebacks (trailing at HT, won at FT): **6** (1.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Oviedo B | Valladolid Promesas | 0-1 | 2-1 |
| 2025-2026 | Salamanca | Sarriana | 0-1 | 2-1 |
| 2025-2026 | UD Ourense | Dep. Fabril | 0-1 | 2-1 |
| 2025-2026 | Numancia | Valladolid Promesas | 0-1 | 3-1 |
| 2025-2026 | Langreo | Burgos CF B | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | UD Samano | Sarriana | 1-0 | 1-2 |
| 2025-2026 | Bergantinos | Oviedo B | 1-0 | 1-2 |
| 2025-2026 | Sarriana | Gimnastica Segoviana | 1-0 | 1-2 |
| 2025-2026 | Real Avila | Salamanca | 1-0 | 1-2 |
| 2025-2026 | Burgos CF B | Real Avila | 1-0 | 1-2 |
| 2025-2026 | Valladolid Promesas | Bergantinos | 2-1 | 3-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 100 | 74 (74.0%) | 20 (20.0%) | 6 (6.0%) |
| Away lead | 80 | 61 (76.2%) | 14 (17.5%) | 5 (6.2%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 59 | 38.8% |
| Draw | 55 | 36.2% |
| Away win | 38 | 25.0% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `303` of `333` (91.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 106 | 31.8% | 43 (40.6%) | 20 (18.9%) | 43 (40.6%) |
| 16-30 | 58 | 17.4% | 23 (39.7%) | 15 (25.9%) | 20 (34.5%) |
| 31-45 | 57 | 17.1% | 28 (49.1%) | 10 (17.5%) | 19 (33.3%) |
| 46-60 | 37 | 11.1% | 18 (48.6%) | 8 (21.6%) | 11 (29.7%) |
| 61-75 | 23 | 6.9% | 11 (47.8%) | 6 (26.1%) | 6 (26.1%) |
| 76-90 | 13 | 3.9% | 10 (76.9%) | 0 (0.0%) | 3 (23.1%) |
| 91-120 | 9 | 2.7% | 5 (55.6%) | 1 (11.1%) | 3 (33.3%) |

## 7. Goalless matches
- Overall: **29** of `333` (8.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 28 | 9.2% |
| 2026-2027 | 27 | 1 | 3.7% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda1\charts\matches_analysis_home_win_rate.png)

