# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:46:33+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 339 |
| Home wins | 154 (45.4%) |
| Draws | 85 (25.1%) |
| Away wins | 100 (29.5%) |
| Total goals | 872 |
| Average goals per match | 2.572 |
| Goalless matches | 32 (9.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 138 (45.1%) | 77 (25.2%) | 91 (29.7%) | 783 | 2.559 | 27 (8.8%) |
| 2026-2027 | 33 | 16 (48.5%) | 8 (24.2%) | 9 (27.3%) | 89 | 2.697 | 5 (15.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 93 (81.6%) | 14 (12.3%) | 7 (6.1%) | 114 |
| HT draw | 52 (34.0%) | 57 (37.3%) | 44 (28.8%) | 153 |
| HT away lead | 9 (12.5%) | 14 (19.4%) | 49 (68.1%) | 72 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.7%)
- Away comebacks (trailing at HT, won at FT): **7** (2.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Rayo Majadahonda | San Sebastian Reyes | 0-1 | 2-1 |
| 2025-2026 | Orihuela | Quintanar del Rey | 0-1 | 3-1 |
| 2025-2026 | CD Coria | Real Madrid C | 0-1 | 2-1 |
| 2025-2026 | Tenerife B | Colonia M. | 0-1 | 3-1 |
| 2025-2026 | Quintanar del Rey | Getafe B | 0-1 | 3-1 |
| 2025-2026 | Fuenlabrada | Quintanar del Rey | 0-1 | 2-1 |
| 2025-2026 | San Sebastian Reyes | Quintanar del Rey | 0-1 | 3-2 |
| 2025-2026 | CD Coria | Navalcarnero | 0-1 | 2-1 |
| 2026-2027 | Guadalajara | RSD Alcala | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Tenerife B | Getafe B | 1-0 | 1-2 |
| 2025-2026 | Real Madrid C | San Sebastian Reyes | 1-0 | 1-2 |
| 2025-2026 | CF Intercity | Real Madrid C | 1-0 | 1-2 |
| 2025-2026 | Las Palmas B | Quintanar del Rey | 1-0 | 1-2 |
| 2025-2026 | CF Intercity | Quintanar del Rey | 1-0 | 1-2 |
| 2026-2027 | Guadalajara | Salamanca | 1-0 | 2-3 |
| 2026-2027 | Guadalajara | Salamanca | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 114 | 93 (81.6%) | 14 (12.3%) | 7 (6.1%) |
| Away lead | 72 | 49 (68.1%) | 14 (19.4%) | 9 (12.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 52 | 34.0% |
| Draw | 57 | 37.3% |
| Away win | 44 | 28.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `307` of `339` (90.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 98 | 28.9% | 50 (51.0%) | 13 (13.3%) | 35 (35.7%) |
| 16-30 | 78 | 23.0% | 46 (59.0%) | 14 (17.9%) | 18 (23.1%) |
| 31-45 | 51 | 15.0% | 25 (49.0%) | 13 (25.5%) | 13 (25.5%) |
| 46-60 | 34 | 10.0% | 14 (41.2%) | 7 (20.6%) | 13 (38.2%) |
| 61-75 | 26 | 7.7% | 13 (50.0%) | 3 (11.5%) | 10 (38.5%) |
| 76-90 | 17 | 5.0% | 5 (29.4%) | 3 (17.6%) | 9 (52.9%) |
| 91-120 | 3 | 0.9% | 1 (33.3%) | 0 (0.0%) | 2 (66.7%) |

## 7. Goalless matches
- Overall: **32** of `339` (9.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 27 | 8.8% |
| 2026-2027 | 33 | 5 | 15.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda5\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda5\charts\matches_analysis_home_win_rate.png)

