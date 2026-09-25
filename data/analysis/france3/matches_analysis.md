# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:59:00+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 371 |
| Home wins | 135 (36.4%) |
| Draws | 120 (32.3%) |
| Away wins | 116 (31.3%) |
| Total goals | 899 |
| Average goals per match | 2.423 |
| Goalless matches | 40 (10.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 303 | 109 (36.0%) | 100 (33.0%) | 94 (31.0%) | 738 | 2.436 | 32 (10.6%) |
| 2026-2027 | 68 | 26 (38.2%) | 20 (29.4%) | 22 (32.4%) | 161 | 2.368 | 8 (11.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 85 (80.2%) | 17 (16.0%) | 4 (3.8%) | 106 |
| HT draw | 42 (26.8%) | 77 (49.0%) | 38 (24.2%) | 157 |
| HT away lead | 8 (7.5%) | 26 (24.3%) | 73 (68.2%) | 107 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.2%)
- Away comebacks (trailing at HT, won at FT): **4** (1.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Chateauroux | Caen | 0-1 | 2-1 |
| 2025-2026 | Villefranche | Chateauroux | 0-1 | 2-1 |
| 2025-2026 | Versailles | Villefranche | 0-1 | 2-1 |
| 2025-2026 | Quevilly Rouen | Concarneau | 0-1 | 2-1 |
| 2025-2026 | Bourg en Bresse | Rouen | 0-1 | 3-1 |
| 2025-2026 | Orleans | Paris 13 Atl. | 0-1 | 2-1 |
| 2025-2026 | Dijon | Versailles | 0-1 | 3-1 |
| 2026-2027 | Thionville | Caen | 1-2 | 4-3 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Rouen | Chateauroux | 1-0 | 1-2 |
| 2025-2026 | Paris 13 Atl. | Versailles | 1-0 | 1-3 |
| 2025-2026 | Villefranche | Valenciennes | 2-1 | 2-3 |
| 2026-2027 | Valenciennes | Fleury-Merogis | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 106 | 85 (80.2%) | 17 (16.0%) | 4 (3.8%) |
| Away lead | 107 | 73 (68.2%) | 26 (24.3%) | 8 (7.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 42 | 26.8% |
| Draw | 77 | 49.0% |
| Away win | 38 | 24.2% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `330` of `371` (88.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 115 | 31.0% | 45 (39.1%) | 35 (30.4%) | 35 (30.4%) |
| 16-30 | 85 | 22.9% | 32 (37.6%) | 20 (23.5%) | 33 (38.8%) |
| 31-45 | 51 | 13.7% | 24 (47.1%) | 10 (19.6%) | 17 (33.3%) |
| 46-60 | 39 | 10.5% | 14 (35.9%) | 9 (23.1%) | 16 (41.0%) |
| 61-75 | 26 | 7.0% | 13 (50.0%) | 5 (19.2%) | 8 (30.8%) |
| 76-90 | 9 | 2.4% | 4 (44.4%) | 1 (11.1%) | 4 (44.4%) |
| 91-120 | 5 | 1.3% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **40** of `371` (10.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 303 | 32 | 10.6% |
| 2026-2027 | 68 | 8 | 11.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\france3\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\france3\charts\matches_analysis_home_win_rate.png)

