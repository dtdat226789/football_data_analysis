# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:08:47+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 449 |
| Home wins | 217 (48.3%) |
| Draws | 110 (24.5%) |
| Away wins | 122 (27.2%) |
| Total goals | 1234 |
| Average goals per match | 2.748 |
| Goalless matches | 20 (4.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 186 (48.9%) | 93 (24.5%) | 101 (26.6%) | 1024 | 2.695 | 15 (3.9%) |
| 2026-2027 | 69 | 31 (44.9%) | 17 (24.6%) | 21 (30.4%) | 210 | 3.043 | 5 (7.2%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 122 (77.7%) | 20 (12.7%) | 15 (9.6%) | 157 |
| HT draw | 86 (44.6%) | 61 (31.6%) | 46 (23.8%) | 193 |
| HT away lead | 9 (9.1%) | 29 (29.3%) | 61 (61.6%) | 99 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (2.0%)
- Away comebacks (trailing at HT, won at FT): **15** (3.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Espanyol | Atl. Madrid | 0-1 | 2-1 |
| 2025-2026 | Villarreal | Osasuna | 0-1 | 2-1 |
| 2025-2026 | Levante | Elche | 0-1 | 3-2 |
| 2025-2026 | Valencia | Alaves | 0-1 | 3-2 |
| 2025-2026 | Mallorca | Espanyol | 0-1 | 2-1 |
| 2025-2026 | Real Madrid | Atl. Madrid | 0-1 | 3-2 |
| 2025-2026 | Alaves | Mallorca | 0-1 | 2-1 |
| 2025-2026 | Atl. Madrid | Ath Bilbao | 0-1 | 3-2 |
| 2026-2027 | Sevilla | Rayo Vallecano | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Levante | Barcelona | 2-0 | 2-3 |
| 2025-2026 | Oviedo | Barcelona | 1-0 | 1-3 |
| 2025-2026 | Valencia | Oviedo | 1-0 | 1-2 |
| 2025-2026 | Espanyol | Betis | 1-0 | 1-2 |
| 2025-2026 | Sevilla | Mallorca | 1-0 | 1-3 |
| 2025-2026 | Osasuna | Celta Vigo | 2-1 | 2-3 |
| 2025-2026 | Osasuna | Real Sociedad | 1-0 | 1-3 |
| 2025-2026 | Real Sociedad | Girona | 1-0 | 1-2 |
| 2025-2026 | Oviedo | Ath Bilbao | 1-0 | 1-2 |
| 2025-2026 | Girona | Celta Vigo | 1-0 | 1-2 |
| 2025-2026 | Celta Vigo | Alaves | 3-1 | 3-4 |
| 2025-2026 | Valencia | Celta Vigo | 1-0 | 2-3 |
| 2025-2026 | Alaves | Ath Bilbao | 1-0 | 2-4 |
| 2025-2026 | Alaves | Rayo Vallecano | 1-0 | 1-2 |
| 2026-2027 | Celta Vigo | Osasuna | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 157 | 122 (77.7%) | 20 (12.7%) | 15 (9.6%) |
| Away lead | 99 | 61 (61.6%) | 29 (29.3%) | 9 (9.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 86 | 44.6% |
| Draw | 61 | 31.6% |
| Away win | 46 | 23.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `429` of `449` (95.5%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 123 | 27.4% | 62 (50.4%) | 21 (17.1%) | 40 (32.5%) |
| 16-30 | 97 | 21.6% | 52 (53.6%) | 20 (20.6%) | 25 (25.8%) |
| 31-45 | 80 | 17.8% | 40 (50.0%) | 20 (25.0%) | 20 (25.0%) |
| 46-60 | 66 | 14.7% | 31 (47.0%) | 20 (30.3%) | 15 (22.7%) |
| 61-75 | 33 | 7.3% | 18 (54.5%) | 6 (18.2%) | 9 (27.3%) |
| 76-90 | 28 | 6.2% | 13 (46.4%) | 3 (10.7%) | 12 (42.9%) |
| 91-120 | 2 | 0.4% | 1 (50.0%) | 0 (0.0%) | 1 (50.0%) |

## 7. Goalless matches
- Overall: **20** of `449` (4.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 15 | 3.9% |
| 2026-2027 | 69 | 5 | 7.2% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\spain1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\spain1\charts\matches_analysis_home_win_rate.png)

