# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:06:44+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 342 |
| Home wins | 143 (41.8%) |
| Draws | 91 (26.6%) |
| Away wins | 108 (31.6%) |
| Total goals | 877 |
| Average goals per match | 2.564 |
| Goalless matches | 29 (8.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 127 (41.5%) | 84 (27.5%) | 95 (31.0%) | 776 | 2.536 | 28 (9.2%) |
| 2026-2027 | 36 | 16 (44.4%) | 7 (19.4%) | 13 (36.1%) | 101 | 2.806 | 1 (2.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 75 (73.5%) | 21 (20.6%) | 6 (5.9%) | 102 |
| HT draw | 62 (40.0%) | 55 (35.5%) | 38 (24.5%) | 155 |
| HT away lead | 5 (6.0%) | 15 (17.9%) | 64 (76.2%) | 84 |
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
| Home lead | 102 | 75 (73.5%) | 21 (20.6%) | 6 (5.9%) |
| Away lead | 84 | 64 (76.2%) | 15 (17.9%) | 5 (6.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 62 | 40.0% |
| Draw | 55 | 35.5% |
| Away win | 38 | 24.5% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `312` of `342` (91.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 111 | 32.5% | 45 (40.5%) | 22 (19.8%) | 44 (39.6%) |
| 16-30 | 60 | 17.5% | 24 (40.0%) | 15 (25.0%) | 21 (35.0%) |
| 31-45 | 57 | 16.7% | 27 (47.4%) | 10 (17.5%) | 20 (35.1%) |
| 46-60 | 38 | 11.1% | 19 (50.0%) | 8 (21.1%) | 11 (28.9%) |
| 61-75 | 24 | 7.0% | 12 (50.0%) | 6 (25.0%) | 6 (25.0%) |
| 76-90 | 13 | 3.8% | 10 (76.9%) | 0 (0.0%) | 3 (23.1%) |
| 91-120 | 9 | 2.6% | 5 (55.6%) | 1 (11.1%) | 3 (33.3%) |

## 7. Goalless matches
- Overall: **29** of `342` (8.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 28 | 9.2% |
| 2026-2027 | 36 | 1 | 2.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda1\charts\matches_analysis_home_win_rate.png)

