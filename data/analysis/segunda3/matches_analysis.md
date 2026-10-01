# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:07:17+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 346 |
| Home wins | 158 (45.7%) |
| Draws | 107 (30.9%) |
| Away wins | 81 (23.4%) |
| Total goals | 829 |
| Average goals per match | 2.396 |
| Goalless matches | 35 (10.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 140 (45.8%) | 97 (31.7%) | 69 (22.5%) | 742 | 2.425 | 33 (10.8%) |
| 2026-2027 | 40 | 18 (45.0%) | 10 (25.0%) | 12 (30.0%) | 87 | 2.175 | 2 (5.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 83 (74.8%) | 19 (17.1%) | 9 (8.1%) | 111 |
| HT draw | 69 (41.3%) | 64 (38.3%) | 34 (20.4%) | 167 |
| HT away lead | 6 (8.8%) | 24 (35.3%) | 38 (55.9%) | 68 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (1.7%)
- Away comebacks (trailing at HT, won at FT): **9** (2.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Barbastro | Torrent | 0-1 | 2-1 |
| 2025-2026 | Sant Andreu | SD Ibiza | 0-1 | 2-1 |
| 2025-2026 | Atletic Lleida | Andratx | 1-2 | 3-2 |
| 2025-2026 | Sant Andreu | Espanyol B | 0-1 | 2-1 |
| 2025-2026 | Girona B | Olot | 0-1 | 4-1 |
| 2025-2026 | Barcelona B | Atletic Lleida | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | SD Ibiza | Valencia B | 1-0 | 1-2 |
| 2025-2026 | Barbastro | SD Ibiza | 1-0 | 1-2 |
| 2025-2026 | Torrent | Sant Andreu | 1-0 | 1-2 |
| 2025-2026 | SD Ibiza | Barbastro | 1-0 | 1-2 |
| 2025-2026 | Espanyol B | Sant Andreu | 1-0 | 1-2 |
| 2025-2026 | Terrassa | Poblense | 2-1 | 2-3 |
| 2026-2027 | Castellon B | CF Intercity | 1-0 | 1-2 |
| 2026-2027 | Castellon B | CF Intercity | 1-0 | 1-2 |
| 2026-2027 | Valencia B | Castellon B | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 111 | 83 (74.8%) | 19 (17.1%) | 9 (8.1%) |
| Away lead | 68 | 38 (55.9%) | 24 (35.3%) | 6 (8.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 69 | 41.3% |
| Draw | 64 | 38.3% |
| Away win | 34 | 20.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `311` of `346` (89.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 99 | 28.6% | 50 (50.5%) | 20 (20.2%) | 29 (29.3%) |
| 16-30 | 69 | 19.9% | 37 (53.6%) | 21 (30.4%) | 11 (15.9%) |
| 31-45 | 38 | 11.0% | 15 (39.5%) | 11 (28.9%) | 12 (31.6%) |
| 46-60 | 41 | 11.8% | 20 (48.8%) | 11 (26.8%) | 10 (24.4%) |
| 61-75 | 35 | 10.1% | 17 (48.6%) | 6 (17.1%) | 12 (34.3%) |
| 76-90 | 24 | 6.9% | 14 (58.3%) | 3 (12.5%) | 7 (29.2%) |
| 91-120 | 5 | 1.4% | 5 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **35** of `346` (10.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 33 | 10.8% |
| 2026-2027 | 40 | 2 | 5.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda3\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda3\charts\matches_analysis_home_win_rate.png)

