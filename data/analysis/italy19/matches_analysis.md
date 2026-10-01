# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:56:55+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Primavera 1 (Italy)
- Scope: league `italy19`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 432 |
| Home wins | 166 (38.4%) |
| Draws | 133 (30.8%) |
| Away wins | 133 (30.8%) |
| Total goals | 1212 |
| Average goals per match | 2.806 |
| Goalless matches | 31 (7.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 382 | 152 (39.8%) | 117 (30.6%) | 113 (29.6%) | 1051 | 2.751 | 29 (7.6%) |
| 2026-2027 | 50 | 14 (28.0%) | 16 (32.0%) | 20 (40.0%) | 161 | 3.22 | 2 (4.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 90 (67.2%) | 32 (23.9%) | 12 (9.0%) | 134 |
| HT draw | 68 (35.8%) | 76 (40.0%) | 46 (24.2%) | 190 |
| HT away lead | 7 (6.7%) | 24 (22.9%) | 74 (70.5%) | 105 |
- *3 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (1.6%)
- Away comebacks (trailing at HT, won at FT): **12** (2.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Cesena U20 | AS Roma U20 | 0-1 | 3-1 |
| 2025-2026 | Inter U20 | Cagliari U20 | 1-2 | 4-3 |
| 2025-2026 | Inter U20 | Genoa U20 | 0-1 | 3-1 |
| 2025-2026 | Napoli U20 | Cesena U20 | 0-1 | 2-1 |
| 2025-2026 | Atalanta U20 | Cesena U20 | 0-1 | 2-1 |
| 2025-2026 | Inter U20 | Lazio U20 | 0-2 | 3-2 |
| 2025-2026 | Parma U20 | AC Milan U20 | 1-2 | 4-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Bologna U20 | Atalanta U20 | 1-0 | 1-2 |
| 2025-2026 | Inter U20 | Juventus U20 | 1-0 | 1-3 |
| 2025-2026 | Lazio U20 | Verona U20 | 2-0 | 2-4 |
| 2025-2026 | Frosinone U20 | Monza U20 | 1-0 | 1-2 |
| 2025-2026 | AS Roma U20 | Lazio U20 | 1-0 | 1-2 |
| 2025-2026 | Sassuolo U20 | Cesena U20 | 2-1 | 2-4 |
| 2025-2026 | Atalanta U20 | Lecce U20 | 2-0 | 2-3 |
| 2025-2026 | Frosinone U20 | Parma U20 | 2-0 | 2-3 |
| 2025-2026 | Sassuolo U20 | Inter U20 | 1-0 | 1-2 |
| 2025-2026 | Genoa U20 | Cesena U20 | 3-0 | 3-5 |
| 2025-2026 | Atalanta U20 | Fiorentina U20 | 1-0 | 1-2 |
| 2025-2026 | AS Roma U20 | Bologna U20 | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 134 | 90 (67.2%) | 32 (23.9%) | 12 (9.0%) |
| Away lead | 105 | 74 (70.5%) | 24 (22.9%) | 7 (6.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 68 | 35.8% |
| Draw | 76 | 40.0% |
| Away win | 46 | 24.2% |
- *3 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `392` of `432` (90.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 158 | 36.6% | 63 (39.9%) | 49 (31.0%) | 46 (29.1%) |
| 16-30 | 81 | 18.8% | 29 (35.8%) | 23 (28.4%) | 29 (35.8%) |
| 31-45 | 65 | 15.0% | 29 (44.6%) | 11 (16.9%) | 25 (38.5%) |
| 46-60 | 40 | 9.3% | 19 (47.5%) | 10 (25.0%) | 11 (27.5%) |
| 61-75 | 23 | 5.3% | 11 (47.8%) | 3 (13.0%) | 9 (39.1%) |
| 76-90 | 21 | 4.9% | 10 (47.6%) | 3 (14.3%) | 8 (38.1%) |
| 91-120 | 4 | 0.9% | 3 (75.0%) | 0 (0.0%) | 1 (25.0%) |

## 7. Goalless matches
- Overall: **31** of `432` (7.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 382 | 29 | 7.6% |
| 2026-2027 | 50 | 2 | 4.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy19\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy19\charts\matches_analysis_home_win_rate.png)

