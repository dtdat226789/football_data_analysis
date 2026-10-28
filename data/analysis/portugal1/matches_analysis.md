# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-10-27T02:24:58+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Liga Portugal (Portugal)
- Scope: league `portugal1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 388 |
| Home wins | 157 (40.5%) |
| Draws | 102 (26.3%) |
| Away wins | 129 (33.2%) |
| Total goals | 1042 |
| Average goals per match | 2.686 |
| Goalless matches | 25 (6.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 308 | 127 (41.2%) | 84 (27.3%) | 97 (31.5%) | 823 | 2.672 | 21 (6.8%) |
| 2026-2027 | 80 | 30 (37.5%) | 18 (22.5%) | 32 (40.0%) | 219 | 2.737 | 4 (5.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 92 (76.0%) | 22 (18.2%) | 7 (5.8%) | 121 |
| HT draw | 57 (33.9%) | 61 (36.3%) | 50 (29.8%) | 168 |
| HT away lead | 8 (8.1%) | 19 (19.2%) | 72 (72.7%) | 99 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.1%)
- Away comebacks (trailing at HT, won at FT): **7** (1.8%)

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
| 2026-2027 | Braga | Sporting CP | 1-0 | 1-3 |
| 2026-2027 | Braga | Gil Vicente | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 121 | 92 (76.0%) | 22 (18.2%) | 7 (5.8%) |
| Away lead | 99 | 72 (72.7%) | 19 (19.2%) | 8 (8.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 57 | 33.9% |
| Draw | 61 | 36.3% |
| Away win | 50 | 29.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `363` of `388` (93.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 123 | 31.7% | 55 (44.7%) | 28 (22.8%) | 40 (32.5%) |
| 16-30 | 73 | 18.8% | 32 (43.8%) | 16 (21.9%) | 25 (34.2%) |
| 31-45 | 69 | 17.8% | 29 (42.0%) | 16 (23.2%) | 24 (34.8%) |
| 46-60 | 45 | 11.6% | 15 (33.3%) | 10 (22.2%) | 20 (44.4%) |
| 61-75 | 31 | 8.0% | 15 (48.4%) | 3 (9.7%) | 13 (41.9%) |
| 76-90 | 17 | 4.4% | 9 (52.9%) | 4 (23.5%) | 4 (23.5%) |
| 91-120 | 5 | 1.3% | 2 (40.0%) | 0 (0.0%) | 3 (60.0%) |

## 7. Goalless matches
- Overall: **25** of `388` (6.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 308 | 21 | 6.8% |
| 2026-2027 | 80 | 4 | 5.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](charts/matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](charts/matches_analysis_home_win_rate.png)

