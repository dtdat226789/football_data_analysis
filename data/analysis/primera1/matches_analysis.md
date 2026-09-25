# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:42:24+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 438 |
| Home wins | 202 (46.1%) |
| Draws | 122 (27.9%) |
| Away wins | 114 (26.0%) |
| Total goals | 1079 |
| Average goals per match | 2.463 |
| Goalless matches | 41 (9.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 398 | 182 (45.7%) | 113 (28.4%) | 103 (25.9%) | 974 | 2.447 | 39 (9.8%) |
| 2026-2027 | 40 | 20 (50.0%) | 9 (22.5%) | 11 (27.5%) | 105 | 2.625 | 2 (5.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 119 (82.1%) | 19 (13.1%) | 7 (4.8%) | 145 |
| HT draw | 76 (36.4%) | 85 (40.7%) | 48 (23.0%) | 209 |
| HT away lead | 7 (8.3%) | 18 (21.4%) | 59 (70.2%) | 84 |

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
| Home lead | 145 | 119 (82.1%) | 19 (13.1%) | 7 (4.8%) |
| Away lead | 84 | 59 (70.2%) | 18 (21.4%) | 7 (8.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 76 | 36.4% |
| Draw | 85 | 40.7% |
| Away win | 48 | 23.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `397` of `438` (90.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 109 | 24.9% | 49 (45.0%) | 21 (19.3%) | 39 (35.8%) |
| 16-30 | 97 | 22.1% | 48 (49.5%) | 24 (24.7%) | 25 (25.8%) |
| 31-45 | 71 | 16.2% | 41 (57.7%) | 11 (15.5%) | 19 (26.8%) |
| 46-60 | 52 | 11.9% | 29 (55.8%) | 12 (23.1%) | 11 (21.2%) |
| 61-75 | 39 | 8.9% | 25 (64.1%) | 6 (15.4%) | 8 (20.5%) |
| 76-90 | 20 | 4.6% | 6 (30.0%) | 7 (35.0%) | 7 (35.0%) |
| 91-120 | 9 | 2.1% | 4 (44.4%) | 0 (0.0%) | 5 (55.6%) |

## 7. Goalless matches
- Overall: **41** of `438` (9.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 398 | 39 | 9.8% |
| 2026-2027 | 40 | 2 | 5.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\primera1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\primera1\charts\matches_analysis_home_win_rate.png)

