# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:45:57+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 337 |
| Home wins | 153 (45.4%) |
| Draws | 106 (31.5%) |
| Away wins | 78 (23.1%) |
| Total goals | 810 |
| Average goals per match | 2.404 |
| Goalless matches | 35 (10.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 140 (45.8%) | 97 (31.7%) | 69 (22.5%) | 742 | 2.425 | 33 (10.8%) |
| 2026-2027 | 31 | 13 (41.9%) | 9 (29.0%) | 9 (29.0%) | 68 | 2.194 | 2 (6.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 81 (74.3%) | 19 (17.4%) | 9 (8.3%) | 109 |
| HT draw | 66 (40.7%) | 63 (38.9%) | 33 (20.4%) | 162 |
| HT away lead | 6 (9.1%) | 24 (36.4%) | 36 (54.5%) | 66 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (1.8%)
- Away comebacks (trailing at HT, won at FT): **9** (2.7%)

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
| Home lead | 109 | 81 (74.3%) | 19 (17.4%) | 9 (8.3%) |
| Away lead | 66 | 36 (54.5%) | 24 (36.4%) | 6 (9.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 66 | 40.7% |
| Draw | 63 | 38.9% |
| Away win | 33 | 20.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `302` of `337` (89.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 96 | 28.5% | 48 (50.0%) | 20 (20.8%) | 28 (29.2%) |
| 16-30 | 68 | 20.2% | 37 (54.4%) | 20 (29.4%) | 11 (16.2%) |
| 31-45 | 36 | 10.7% | 15 (41.7%) | 11 (30.6%) | 10 (27.8%) |
| 46-60 | 40 | 11.9% | 19 (47.5%) | 11 (27.5%) | 10 (25.0%) |
| 61-75 | 34 | 10.1% | 16 (47.1%) | 6 (17.6%) | 12 (35.3%) |
| 76-90 | 23 | 6.8% | 13 (56.5%) | 3 (13.0%) | 7 (30.4%) |
| 91-120 | 5 | 1.5% | 5 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **35** of `337` (10.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 306 | 33 | 10.8% |
| 2026-2027 | 31 | 2 | 6.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\segunda3\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\segunda3\charts\matches_analysis_home_win_rate.png)

