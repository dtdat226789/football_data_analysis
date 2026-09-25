# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:56:26+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: ChNL (Czech Republic)
- Scope: league `czech2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 312 |
| Home wins | 142 (45.5%) |
| Draws | 74 (23.7%) |
| Away wins | 96 (30.8%) |
| Total goals | 861 |
| Average goals per match | 2.760 |
| Goalless matches | 18 (5.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 240 | 111 (46.2%) | 50 (20.8%) | 79 (32.9%) | 643 | 2.679 | 14 (5.8%) |
| 2026-2027 | 72 | 31 (43.1%) | 24 (33.3%) | 17 (23.6%) | 218 | 3.028 | 4 (5.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 88 (85.4%) | 10 (9.7%) | 5 (4.9%) | 103 |
| HT draw | 45 (39.1%) | 41 (35.7%) | 29 (25.2%) | 115 |
| HT away lead | 9 (9.6%) | 23 (24.5%) | 62 (66.0%) | 94 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.9%)
- Away comebacks (trailing at HT, won at FT): **5** (1.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Chrudim | Zizkov | 0-1 | 3-2 |
| 2025-2026 | Zizkov | Chrudim | 0-1 | 2-1 |
| 2025-2026 | Kromeriz | Sparta Prague B | 0-1 | 2-1 |
| 2025-2026 | Prostejov | Usti nad Labem | 0-1 | 2-1 |
| 2025-2026 | Vlasim | Zizkov | 0-1 | 3-1 |
| 2025-2026 | Prostejov | Taborsko | 0-1 | 2-1 |
| 2026-2027 | Vlasim | Zizkov | 0-1 | 4-1 |
| 2026-2027 | Kromeriz | Prostejov | 0-1 | 2-1 |
| 2026-2027 | Trinec | Karvina | 0-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Slavia Prague B | Artis Brno | 1-0 | 1-2 |
| 2025-2026 | Ostrava B | Usti nad Labem | 1-0 | 1-2 |
| 2026-2027 | Jihlava | Pribram | 1-0 | 1-2 |
| 2026-2027 | Dukla Prague | Slavia Prague B | 1-0 | 1-3 |
| 2026-2027 | Opava | Dukla Prague | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 103 | 88 (85.4%) | 10 (9.7%) | 5 (4.9%) |
| Away lead | 94 | 62 (66.0%) | 23 (24.5%) | 9 (9.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 45 | 39.1% |
| Draw | 41 | 35.7% |
| Away win | 29 | 25.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `294` of `312` (94.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 98 | 31.4% | 45 (45.9%) | 24 (24.5%) | 29 (29.6%) |
| 16-30 | 82 | 26.3% | 40 (48.8%) | 15 (18.3%) | 27 (32.9%) |
| 31-45 | 48 | 15.4% | 24 (50.0%) | 6 (12.5%) | 18 (37.5%) |
| 46-60 | 26 | 8.3% | 13 (50.0%) | 5 (19.2%) | 8 (30.8%) |
| 61-75 | 21 | 6.7% | 11 (52.4%) | 1 (4.8%) | 9 (42.9%) |
| 76-90 | 19 | 6.1% | 9 (47.4%) | 5 (26.3%) | 5 (26.3%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **18** of `312` (5.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 240 | 14 | 5.8% |
| 2026-2027 | 72 | 4 | 5.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\czech2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\czech2\charts\matches_analysis_home_win_rate.png)

