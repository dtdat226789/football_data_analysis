# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:04:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 448 |
| Home wins | 205 (45.8%) |
| Draws | 126 (28.1%) |
| Away wins | 117 (26.1%) |
| Total goals | 1107 |
| Average goals per match | 2.471 |
| Goalless matches | 42 (9.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 398 | 182 (45.7%) | 113 (28.4%) | 103 (25.9%) | 974 | 2.447 | 39 (9.8%) |
| 2026-2027 | 50 | 23 (46.0%) | 13 (26.0%) | 14 (28.0%) | 133 | 2.66 | 3 (6.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 121 (81.2%) | 21 (14.1%) | 7 (4.7%) | 149 |
| HT draw | 77 (36.3%) | 86 (40.6%) | 49 (23.1%) | 212 |
| HT away lead | 7 (8.0%) | 19 (21.8%) | 61 (70.1%) | 87 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (1.6%)
- Away comebacks (trailing at HT, won at FT): **7** (1.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Lugo | Racing Club Ferrol | 0-1 | 2-1 |
| 2025-2026 | Real Aviles | Ath Bilbao B | 0-1 | 3-2 |
| 2025-2026 | Celta Vigo B | CF Talavera | 0-3 | 4-3 |
| 2025-2026 | Ourense CF | Real Aviles | 0-1 | 2-1 |
| 2025-2026 | CF Talavera | Arenas Getxo | 0-1 | 2-1 |
| 2025-2026 | Ourense CF | Tenerife | 0-1 | 2-1 |
| 2026-2027 | Dep. Fabril | Ponferradina | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Osasuna B | Racing Club Ferrol | 1-0 | 1-2 |
| 2025-2026 | Ath Bilbao B | Celta Vigo B | 1-0 | 1-2 |
| 2025-2026 | Ath Bilbao B | CF Talavera | 1-0 | 1-2 |
| 2025-2026 | Zamora | Unionistas | 1-0 | 2-3 |
| 2025-2026 | CF Talavera | Real Madrid B | 1-0 | 1-2 |
| 2025-2026 | Zamora | Cacereno | 1-0 | 1-2 |
| 2025-2026 | Cacereno | CF Talavera | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 149 | 121 (81.2%) | 21 (14.1%) | 7 (4.7%) |
| Away lead | 87 | 61 (70.1%) | 19 (21.8%) | 7 (8.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 77 | 36.3% |
| Draw | 86 | 40.6% |
| Away win | 49 | 23.1% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `406` of `448` (90.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 110 | 24.6% | 49 (44.5%) | 21 (19.1%) | 40 (36.4%) |
| 16-30 | 101 | 22.5% | 49 (48.5%) | 27 (26.7%) | 25 (24.8%) |
| 31-45 | 73 | 16.3% | 42 (57.5%) | 11 (15.1%) | 20 (27.4%) |
| 46-60 | 52 | 11.6% | 29 (55.8%) | 12 (23.1%) | 11 (21.2%) |
| 61-75 | 40 | 8.9% | 25 (62.5%) | 6 (15.0%) | 9 (22.5%) |
| 76-90 | 21 | 4.7% | 7 (33.3%) | 7 (33.3%) | 7 (33.3%) |
| 91-120 | 9 | 2.0% | 4 (44.4%) | 0 (0.0%) | 5 (55.6%) |

## 7. Goalless matches
- Overall: **42** of `448` (9.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 398 | 39 | 9.8% |
| 2026-2027 | 50 | 3 | 6.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\primera1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\primera1\charts\matches_analysis_home_win_rate.png)

