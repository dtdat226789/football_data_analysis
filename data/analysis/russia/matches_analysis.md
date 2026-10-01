# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:04:59+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premier League (Russia)
- Scope: league `russia`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 320 |
| Home wins | 137 (42.8%) |
| Draws | 93 (29.1%) |
| Away wins | 90 (28.1%) |
| Total goals | 827 |
| Average goals per match | 2.584 |
| Goalless matches | 21 (6.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 244 | 110 (45.1%) | 67 (27.5%) | 67 (27.5%) | 615 | 2.52 | 15 (6.1%) |
| 2026-2027 | 76 | 27 (35.5%) | 26 (34.2%) | 23 (30.3%) | 212 | 2.789 | 6 (7.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 77 (72.0%) | 26 (24.3%) | 4 (3.7%) | 107 |
| HT draw | 48 (38.1%) | 45 (35.7%) | 33 (26.2%) | 126 |
| HT away lead | 12 (13.8%) | 22 (25.3%) | 53 (60.9%) | 87 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.8%)
- Away comebacks (trailing at HT, won at FT): **4** (1.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Zenit | FK Rostov | 0-1 | 2-1 |
| 2025-2026 | Spartak Moscow | Krylya Sovetov | 0-1 | 2-1 |
| 2025-2026 | Akron Togliatti | Sochi | 0-1 | 3-2 |
| 2025-2026 | Akhmat Grozny | Dynamo Moscow | 0-1 | 2-1 |
| 2025-2026 | Orenburg | Zenit | 0-1 | 2-1 |
| 2025-2026 | Spartak Moscow | Lokomotiv Moscow | 0-1 | 2-1 |
| 2025-2026 | Sochi | Krylya Sovetov | 0-1 | 2-1 |
| 2025-2026 | Orenburg | Pari NN | 0-1 | 2-1 |
| 2025-2026 | Zenit | Sochi | 0-1 | 2-1 |
| 2025-2026 | Dynamo Moscow | Krasnodar | 0-1 | 2-1 |
| 2026-2027 | Dynamo Makhachkala | Lokomotiv Moscow | 0-1 | 2-1 |
| 2026-2027 | Zenit | Lokomotiv Moscow | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Akron Togliatti | Orenburg | 1-0 | 1-2 |
| 2025-2026 | Sochi | CSKA Moscow | 1-0 | 1-3 |
| 2025-2026 | Pari NN | CSKA Moscow | 1-0 | 1-2 |
| 2026-2027 | Zenit | Rodina Moscow | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 107 | 77 (72.0%) | 26 (24.3%) | 4 (3.7%) |
| Away lead | 87 | 53 (60.9%) | 22 (25.3%) | 12 (13.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 48 | 38.1% |
| Draw | 45 | 35.7% |
| Away win | 33 | 26.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `299` of `320` (93.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 102 | 31.9% | 44 (43.1%) | 27 (26.5%) | 31 (30.4%) |
| 16-30 | 68 | 21.2% | 35 (51.5%) | 13 (19.1%) | 20 (29.4%) |
| 31-45 | 49 | 15.3% | 22 (44.9%) | 15 (30.6%) | 12 (24.5%) |
| 46-60 | 38 | 11.9% | 16 (42.1%) | 11 (28.9%) | 11 (28.9%) |
| 61-75 | 21 | 6.6% | 11 (52.4%) | 3 (14.3%) | 7 (33.3%) |
| 76-90 | 16 | 5.0% | 6 (37.5%) | 2 (12.5%) | 8 (50.0%) |
| 91-120 | 5 | 1.6% | 3 (60.0%) | 1 (20.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **21** of `320` (6.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 244 | 15 | 6.1% |
| 2026-2027 | 76 | 6 | 7.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\russia\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\russia\charts\matches_analysis_home_win_rate.png)

