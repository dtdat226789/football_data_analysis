# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:46:48+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Chance Liga (Czech Republic)
- Scope: league `czech1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 351 |
| Home wins | 150 (42.7%) |
| Draws | 82 (23.4%) |
| Away wins | 119 (33.9%) |
| Total goals | 941 |
| Average goals per match | 2.681 |
| Goalless matches | 27 (7.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 280 | 118 (42.1%) | 67 (23.9%) | 95 (33.9%) | 740 | 2.643 | 23 (8.2%) |
| 2026-2027 | 71 | 32 (45.1%) | 15 (21.1%) | 24 (33.8%) | 201 | 2.831 | 4 (5.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 98 (83.1%) | 15 (12.7%) | 5 (4.2%) | 118 |
| HT draw | 45 (34.4%) | 48 (36.6%) | 38 (29.0%) | 131 |
| HT away lead | 7 (6.9%) | 19 (18.8%) | 75 (74.3%) | 101 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.0%)
- Away comebacks (trailing at HT, won at FT): **5** (1.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Slovacko | Teplice | 0-1 | 2-1 |
| 2025-2026 | Sparta Prague | Dukla Prague | 1-2 | 3-2 |
| 2025-2026 | FK Pardubice | Karvina | 0-1 | 2-1 |
| 2025-2026 | Sparta Prague | Bohemians | 0-1 | 2-1 |
| 2025-2026 | Slavia Prague | Sparta Prague | 0-1 | 3-1 |
| 2025-2026 | Slavia Prague | Sigma Olomouc | 0-1 | 2-1 |
| 2026-2027 | Jablonec | Sigma Olomouc | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Teplice | Zlin | 1-0 | 1-3 |
| 2025-2026 | Hradec Kralove | Liberec | 2-1 | 2-3 |
| 2025-2026 | Teplice | Plzen | 1-0 | 1-2 |
| 2025-2026 | Zlin | Teplice | 2-1 | 2-4 |
| 2026-2027 | FK Pardubice | Artis Brno | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 118 | 98 (83.1%) | 15 (12.7%) | 5 (4.2%) |
| Away lead | 101 | 75 (74.3%) | 19 (18.8%) | 7 (6.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 45 | 34.4% |
| Draw | 48 | 36.6% |
| Away win | 38 | 29.0% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `323` of `351` (92.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 104 | 29.6% | 48 (46.2%) | 24 (23.1%) | 32 (30.8%) |
| 16-30 | 84 | 23.9% | 40 (47.6%) | 10 (11.9%) | 34 (40.5%) |
| 31-45 | 63 | 17.9% | 27 (42.9%) | 12 (19.0%) | 24 (38.1%) |
| 46-60 | 35 | 10.0% | 22 (62.9%) | 5 (14.3%) | 8 (22.9%) |
| 61-75 | 24 | 6.8% | 7 (29.2%) | 2 (8.3%) | 15 (62.5%) |
| 76-90 | 13 | 3.7% | 6 (46.2%) | 2 (15.4%) | 5 (38.5%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **27** of `351` (7.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 280 | 23 | 8.2% |
| 2026-2027 | 71 | 4 | 5.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech1\charts\matches_analysis_home_win_rate.png)

