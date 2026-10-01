# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:49:57+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ligue 1 (France)
- Scope: league `france1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 355 |
| Home wins | 161 (45.4%) |
| Draws | 89 (25.1%) |
| Away wins | 105 (29.6%) |
| Total goals | 1002 |
| Average goals per match | 2.823 |
| Goalless matches | 29 (8.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 310 | 143 (46.1%) | 76 (24.5%) | 91 (29.4%) | 874 | 2.819 | 25 (8.1%) |
| 2026-2027 | 45 | 18 (40.0%) | 13 (28.9%) | 14 (31.1%) | 128 | 2.844 | 4 (8.9%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 98 (83.8%) | 12 (10.3%) | 7 (6.0%) | 117 |
| HT draw | 55 (38.7%) | 53 (37.3%) | 34 (23.9%) | 142 |
| HT away lead | 8 (8.4%) | 23 (24.2%) | 64 (67.4%) | 95 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.3%)
- Away comebacks (trailing at HT, won at FT): **7** (2.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Lens | Brest | 0-1 | 3-1 |
| 2025-2026 | Rennes | Lyon | 0-1 | 3-1 |
| 2025-2026 | Metz | Nice | 0-1 | 2-1 |
| 2025-2026 | Marseille | Lyon | 0-1 | 3-2 |
| 2025-2026 | Lens | Toulouse | 0-2 | 3-2 |
| 2025-2026 | Strasbourg | Monaco | 1-3 | 5-4 |
| 2026-2027 | Strasbourg | Lens | 0-1 | 2-1 |
| 2026-2027 | Auxerre | Brest | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Lyon | Toulouse | 1-0 | 1-2 |
| 2025-2026 | Strasbourg | Brest | 1-0 | 1-2 |
| 2025-2026 | Lens | Monaco | 1-0 | 2-3 |
| 2025-2026 | Lyon | Monaco | 1-0 | 1-2 |
| 2025-2026 | Marseille | Lille | 1-0 | 1-2 |
| 2025-2026 | Lorient | Strasbourg | 1-0 | 2-3 |
| 2026-2027 | PSG | Monaco | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 117 | 98 (83.8%) | 12 (10.3%) | 7 (6.0%) |
| Away lead | 95 | 64 (67.4%) | 23 (24.2%) | 8 (8.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 55 | 38.7% |
| Draw | 53 | 37.3% |
| Away win | 34 | 23.9% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `326` of `355` (91.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 110 | 31.0% | 52 (47.3%) | 25 (22.7%) | 33 (30.0%) |
| 16-30 | 80 | 22.5% | 40 (50.0%) | 10 (12.5%) | 30 (37.5%) |
| 31-45 | 45 | 12.7% | 23 (51.1%) | 8 (17.8%) | 14 (31.1%) |
| 46-60 | 48 | 13.5% | 24 (50.0%) | 10 (20.8%) | 14 (29.2%) |
| 61-75 | 23 | 6.5% | 8 (34.8%) | 7 (30.4%) | 8 (34.8%) |
| 76-90 | 15 | 4.2% | 9 (60.0%) | 0 (0.0%) | 6 (40.0%) |
| 91-120 | 5 | 1.4% | 5 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **29** of `355` (8.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 310 | 25 | 8.1% |
| 2026-2027 | 45 | 4 | 8.9% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\france1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\france1\charts\matches_analysis_home_win_rate.png)

