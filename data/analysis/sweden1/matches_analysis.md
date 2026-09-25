# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:48:26+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Allsvenskan (Sweden)
- Scope: league `sweden1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 416 |
| Home wins | 169 (40.6%) |
| Draws | 94 (22.6%) |
| Away wins | 153 (36.8%) |
| Total goals | 1200 |
| Average goals per match | 2.885 |
| Goalless matches | 21 (5.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 240 | 96 (40.0%) | 53 (22.1%) | 91 (37.9%) | 683 | 2.846 | 14 (5.8%) |
| 2026 | 176 | 73 (41.5%) | 41 (23.3%) | 62 (35.2%) | 517 | 2.938 | 7 (4.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 103 (80.5%) | 18 (14.1%) | 7 (5.5%) | 128 |
| HT draw | 53 (30.6%) | 56 (32.4%) | 64 (37.0%) | 173 |
| HT away lead | 13 (11.3%) | 20 (17.4%) | 82 (71.3%) | 115 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **13** (3.1%)
- Away comebacks (trailing at HT, won at FT): **7** (1.7%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | AIK | Norrkoping | 0-1 | 4-3 |
| 2025 | Hammarby | Brommapojkarna | 0-2 | 3-2 |
| 2025 | Mjallby | Sirius | 0-1 | 2-1 |
| 2025 | Elfsborg | Goteborg | 1-3 | 4-3 |
| 2025 | Brommapojkarna | Norrkoping | 3-4 | 6-4 |
| 2025 | AIK | Sirius | 0-1 | 2-1 |
| 2025 | Mjallby | Norrkoping | 0-1 | 2-1 |
| 2025 | Malmo FF | GAIS | 0-1 | 2-1 |
| 2026 | Sirius | Kalmar | 0-2 | 3-2 |
| 2026 | Hacken | Hammarby | 0-2 | 3-2 |
| 2026 | Orgryte | Hacken | 1-2 | 4-3 |
| 2026 | Mjallby | Sirius | 0-3 | 4-3 |
| 2026 | AIK | Hammarby | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Norrkoping | Goteborg | 2-0 | 2-3 |
| 2025 | Varnamo | Hammarby | 2-1 | 2-3 |
| 2025 | Sirius | Degerfors | 1-0 | 1-3 |
| 2025 | Varnamo | Halmstad | 1-0 | 1-2 |
| 2025 | Oster | Djurgarden | 1-0 | 1-3 |
| 2026 | Orgryte | AIK | 2-1 | 3-4 |
| 2026 | AIK | Vasteras SK | 1-0 | 1-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 128 | 103 (80.5%) | 18 (14.1%) | 7 (5.5%) |
| Away lead | 115 | 82 (71.3%) | 20 (17.4%) | 13 (11.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 53 | 30.6% |
| Draw | 56 | 32.4% |
| Away win | 64 | 37.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `395` of `416` (95.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 131 | 31.5% | 61 (46.6%) | 26 (19.8%) | 44 (33.6%) |
| 16-30 | 92 | 22.1% | 37 (40.2%) | 21 (22.8%) | 34 (37.0%) |
| 31-45 | 56 | 13.5% | 31 (55.4%) | 7 (12.5%) | 18 (32.1%) |
| 46-60 | 69 | 16.6% | 20 (29.0%) | 11 (15.9%) | 38 (55.1%) |
| 61-75 | 27 | 6.5% | 11 (40.7%) | 4 (14.8%) | 12 (44.4%) |
| 76-90 | 14 | 3.4% | 5 (35.7%) | 4 (28.6%) | 5 (35.7%) |
| 91-120 | 6 | 1.4% | 4 (66.7%) | 0 (0.0%) | 2 (33.3%) |

## 7. Goalless matches
- Overall: **21** of `416` (5.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 240 | 14 | 5.8% |
| 2026 | 176 | 7 | 4.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\sweden1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\sweden1\charts\matches_analysis_home_win_rate.png)

