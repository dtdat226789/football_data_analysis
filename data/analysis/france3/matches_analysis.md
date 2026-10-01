# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:50:26+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Ligue 3 (France)
- Scope: league `france3`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 388 |
| Home wins | 140 (36.1%) |
| Draws | 126 (32.5%) |
| Away wins | 122 (31.4%) |
| Total goals | 943 |
| Average goals per match | 2.430 |
| Goalless matches | 42 (10.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 303 | 109 (36.0%) | 100 (33.0%) | 94 (31.0%) | 738 | 2.436 | 32 (10.6%) |
| 2026-2027 | 85 | 31 (36.5%) | 26 (30.6%) | 28 (32.9%) | 205 | 2.412 | 10 (11.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 89 (79.5%) | 18 (16.1%) | 5 (4.5%) | 112 |
| HT draw | 43 (26.1%) | 80 (48.5%) | 42 (25.5%) | 165 |
| HT away lead | 8 (7.3%) | 28 (25.5%) | 74 (67.3%) | 110 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (2.1%)
- Away comebacks (trailing at HT, won at FT): **5** (1.3%)

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
| 2026-2027 | Valenciennes | Fleury 91 | 1-0 | 1-2 |
| 2026-2027 | Valenciennes | Fleury-Merogis | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 112 | 89 (79.5%) | 18 (16.1%) | 5 (4.5%) |
| Away lead | 110 | 74 (67.3%) | 28 (25.5%) | 8 (7.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 43 | 26.1% |
| Draw | 80 | 48.5% |
| Away win | 42 | 25.5% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `345` of `388` (88.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 121 | 31.2% | 47 (38.8%) | 36 (29.8%) | 38 (31.4%) |
| 16-30 | 88 | 22.7% | 34 (38.6%) | 20 (22.7%) | 34 (38.6%) |
| 31-45 | 53 | 13.7% | 25 (47.2%) | 10 (18.9%) | 18 (34.0%) |
| 46-60 | 42 | 10.8% | 14 (33.3%) | 11 (26.2%) | 17 (40.5%) |
| 61-75 | 27 | 7.0% | 13 (48.1%) | 6 (22.2%) | 8 (29.6%) |
| 76-90 | 9 | 2.3% | 4 (44.4%) | 1 (11.1%) | 4 (44.4%) |
| 91-120 | 5 | 1.3% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **42** of `388` (10.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 303 | 32 | 10.6% |
| 2026-2027 | 85 | 10 | 11.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\france3\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\france3\charts\matches_analysis_home_win_rate.png)

