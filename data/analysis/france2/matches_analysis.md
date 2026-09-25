# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:58:47+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ligue 2 (France)
- Scope: league `france2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 373 |
| Home wins | 138 (37.0%) |
| Draws | 118 (31.6%) |
| Away wins | 117 (31.4%) |
| Total goals | 946 |
| Average goals per match | 2.536 |
| Goalless matches | 40 (10.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 117 (37.7%) | 95 (30.6%) | 98 (31.6%) | 784 | 2.529 | 33 (10.6%) |
| 2026-2027 | 63 | 21 (33.3%) | 23 (36.5%) | 19 (30.2%) | 162 | 2.571 | 7 (11.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 72 (64.9%) | 31 (27.9%) | 8 (7.2%) | 111 |
| HT draw | 54 (32.1%) | 71 (42.3%) | 43 (25.6%) | 168 |
| HT away lead | 12 (12.9%) | 15 (16.1%) | 66 (71.0%) | 93 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.2%)
- Away comebacks (trailing at HT, won at FT): **8** (2.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Amiens | Rodez | 0-1 | 2-1 |
| 2025-2026 | Troyes | Amiens | 0-1 | 3-1 |
| 2025-2026 | Boulogne | Grenoble | 0-1 | 3-1 |
| 2025-2026 | Clermont | Dunkerque | 0-1 | 2-1 |
| 2025-2026 | Laval | Grenoble | 0-1 | 3-2 |
| 2025-2026 | Red Star | Bastia | 1-3 | 4-3 |
| 2025-2026 | Rodez | Troyes | 0-1 | 2-1 |
| 2025-2026 | Rodez | Amiens | 1-2 | 3-2 |
| 2025-2026 | Pau FC | Guingamp | 0-1 | 2-1 |
| 2026-2027 | Reims | Annecy | 0-1 | 3-1 |
| 2026-2027 | Guingamp | Annecy | 0-1 | 2-1 |
| 2026-2027 | Dunkerque | St Etienne | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Clermont | St Etienne | 1-0 | 1-2 |
| 2025-2026 | Bastia | Rodez | 1-0 | 2-3 |
| 2025-2026 | Reims | Rodez | 1-0 | 1-2 |
| 2025-2026 | Annecy | Troyes | 1-0 | 1-2 |
| 2025-2026 | Pau FC | Nancy | 1-0 | 1-3 |
| 2026-2027 | Nantes | Rodez | 2-1 | 2-5 |
| 2026-2027 | Rodez | Nancy | 2-1 | 3-4 |
| 2026-2027 | Annecy | Dijon | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 111 | 72 (64.9%) | 31 (27.9%) | 8 (7.2%) |
| Away lead | 93 | 66 (71.0%) | 15 (16.1%) | 12 (12.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 54 | 32.1% |
| Draw | 71 | 42.3% |
| Away win | 43 | 25.6% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `333` of `373` (89.3%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 106 | 28.4% | 44 (41.5%) | 20 (18.9%) | 42 (39.6%) |
| 16-30 | 88 | 23.6% | 30 (34.1%) | 28 (31.8%) | 30 (34.1%) |
| 31-45 | 46 | 12.3% | 20 (43.5%) | 14 (30.4%) | 12 (26.1%) |
| 46-60 | 47 | 12.6% | 22 (46.8%) | 8 (17.0%) | 17 (36.2%) |
| 61-75 | 26 | 7.0% | 13 (50.0%) | 4 (15.4%) | 9 (34.6%) |
| 76-90 | 17 | 4.6% | 7 (41.2%) | 4 (23.5%) | 6 (35.3%) |
| 91-120 | 3 | 0.8% | 2 (66.7%) | 0 (0.0%) | 1 (33.3%) |

## 7. Goalless matches
- Overall: **40** of `373` (10.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 310 | 33 | 10.6% |
| 2026-2027 | 63 | 7 | 11.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\france2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\france2\charts\matches_analysis_home_win_rate.png)

