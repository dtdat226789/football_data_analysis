# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:03:25+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 370 |
| Home wins | 151 (40.8%) |
| Draws | 102 (27.6%) |
| Away wins | 117 (31.6%) |
| Total goals | 993 |
| Average goals per match | 2.684 |
| Goalless matches | 25 (6.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 308 | 127 (41.2%) | 84 (27.3%) | 97 (31.5%) | 823 | 2.672 | 21 (6.8%) |
| 2026-2027 | 62 | 24 (38.7%) | 18 (29.0%) | 20 (32.3%) | 170 | 2.742 | 4 (6.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 87 (76.3%) | 22 (19.3%) | 5 (4.4%) | 114 |
| HT draw | 56 (34.8%) | 61 (37.9%) | 44 (27.3%) | 161 |
| HT away lead | 8 (8.4%) | 19 (20.0%) | 68 (71.6%) | 95 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.2%)
- Away comebacks (trailing at HT, won at FT): **5** (1.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Vitoria Guimaraes | Santa Clara | 0-1 | 2-1 |
| 2025-2026 | Estoril | Vitoria Guimaraes | 1-2 | 4-2 |
| 2025-2026 | Arouca | Vitoria Guimaraes | 1-2 | 3-2 |
| 2025-2026 | Vitoria Guimaraes | Estrela | 0-1 | 2-1 |
| 2025-2026 | Gil Vicente | Braga | 0-1 | 2-1 |
| 2025-2026 | Alverca | Casa Pia | 0-1 | 3-1 |
| 2025-2026 | Santa Clara | Braga | 0-1 | 2-1 |
| 2025-2026 | Moreirense | Estrela | 1-2 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Nacional | Sporting CP | 1-0 | 1-4 |
| 2025-2026 | Estrela | Rio Ave | 1-0 | 1-2 |
| 2025-2026 | Arouca | Benfica | 1-0 | 1-2 |
| 2025-2026 | Estoril | Rio Ave | 1-0 | 1-2 |
| 2026-2027 | Alverca | Braga | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 114 | 87 (76.3%) | 22 (19.3%) | 5 (4.4%) |
| Away lead | 95 | 68 (71.6%) | 19 (20.0%) | 8 (8.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 56 | 34.8% |
| Draw | 61 | 37.9% |
| Away win | 44 | 27.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `345` of `370` (93.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 120 | 32.4% | 54 (45.0%) | 28 (23.3%) | 38 (31.7%) |
| 16-30 | 67 | 18.1% | 29 (43.3%) | 16 (23.9%) | 22 (32.8%) |
| 31-45 | 64 | 17.3% | 27 (42.2%) | 16 (25.0%) | 21 (32.8%) |
| 46-60 | 44 | 11.9% | 15 (34.1%) | 10 (22.7%) | 19 (43.2%) |
| 61-75 | 30 | 8.1% | 15 (50.0%) | 3 (10.0%) | 12 (40.0%) |
| 76-90 | 16 | 4.3% | 9 (56.2%) | 4 (25.0%) | 3 (18.8%) |
| 91-120 | 4 | 1.1% | 2 (50.0%) | 0 (0.0%) | 2 (50.0%) |

## 7. Goalless matches
- Overall: **25** of `370` (6.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 308 | 21 | 6.8% |
| 2026-2027 | 62 | 4 | 6.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\portugal1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\portugal1\charts\matches_analysis_home_win_rate.png)

