# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:07:46+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 348 |
| Home wins | 161 (46.3%) |
| Draws | 86 (24.7%) |
| Away wins | 101 (29.0%) |
| Total goals | 893 |
| Average goals per match | 2.566 |
| Goalless matches | 32 (9.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 138 (45.1%) | 77 (25.2%) | 91 (29.7%) | 783 | 2.559 | 27 (8.8%) |
| 2026-2027 | 42 | 23 (54.8%) | 9 (21.4%) | 10 (23.8%) | 110 | 2.619 | 5 (11.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 97 (82.2%) | 14 (11.9%) | 7 (5.9%) | 118 |
| HT draw | 55 (34.8%) | 58 (36.7%) | 45 (28.5%) | 158 |
| HT away lead | 9 (12.5%) | 14 (19.4%) | 49 (68.1%) | 72 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.6%)
- Away comebacks (trailing at HT, won at FT): **7** (2.0%)

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
| Home lead | 118 | 97 (82.2%) | 14 (11.9%) | 7 (5.9%) |
| Away lead | 72 | 49 (68.1%) | 14 (19.4%) | 9 (12.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 55 | 34.8% |
| Draw | 58 | 36.7% |
| Away win | 45 | 28.5% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `316` of `348` (90.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 99 | 28.4% | 50 (50.5%) | 14 (14.1%) | 35 (35.4%) |
| 16-30 | 79 | 22.7% | 47 (59.5%) | 14 (17.7%) | 18 (22.8%) |
| 31-45 | 54 | 15.5% | 29 (53.7%) | 13 (24.1%) | 12 (22.2%) |
| 46-60 | 35 | 10.1% | 14 (40.0%) | 7 (20.0%) | 14 (40.0%) |
| 61-75 | 29 | 8.3% | 15 (51.7%) | 3 (10.3%) | 11 (37.9%) |
| 76-90 | 17 | 4.9% | 5 (29.4%) | 3 (17.6%) | 9 (52.9%) |
| 91-120 | 3 | 0.9% | 1 (33.3%) | 0 (0.0%) | 2 (66.7%) |

## 7. Goalless matches
- Overall: **32** of `348` (9.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 27 | 8.8% |
| 2026-2027 | 42 | 5 | 11.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda5\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda5\charts\matches_analysis_home_win_rate.png)

