# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:44:14+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 227 |
| Home wins | 91 (40.1%) |
| Draws | 74 (32.6%) |
| Away wins | 62 (27.3%) |
| Total goals | 532 |
| Average goals per match | 2.344 |
| Goalless matches | 29 (12.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 190 | 74 (38.9%) | 64 (33.7%) | 52 (27.4%) | 460 | 2.421 | 25 (13.2%) |
| 2026-2027 | 37 | 17 (45.9%) | 10 (27.0%) | 10 (27.0%) | 72 | 1.946 | 4 (10.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 58 (80.6%) | 13 (18.1%) | 1 (1.4%) | 72 |
| HT draw | 23 (25.6%) | 46 (51.1%) | 21 (23.3%) | 90 |
| HT away lead | 10 (15.4%) | 15 (23.1%) | 40 (61.5%) | 65 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (4.4%)
- Away comebacks (trailing at HT, won at FT): **1** (0.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Partick Thistle | Airdrieonians | 0-1 | 2-1 |
| 2025-2026 | St Johnstone | Dunfermline | 0-1 | 2-1 |
| 2025-2026 | Arbroath | St Johnstone | 0-1 | 3-1 |
| 2025-2026 | Partick Thistle | Ayr | 0-1 | 2-1 |
| 2025-2026 | Partick Thistle | Morton | 0-2 | 3-2 |
| 2025-2026 | Dunfermline | Morton | 0-1 | 3-1 |
| 2025-2026 | Raith | Morton | 0-1 | 3-2 |
| 2025-2026 | Airdrieonians | Ayr | 0-1 | 2-1 |
| 2025-2026 | Raith | Ross County | 0-1 | 3-2 |
| 2025-2026 | Partick Thistle | Dunfermline | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Ayr | St Johnstone | 2-0 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 72 | 58 (80.6%) | 13 (18.1%) | 1 (1.4%) |
| Away lead | 65 | 40 (61.5%) | 15 (23.1%) | 10 (15.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 23 | 25.6% |
| Draw | 46 | 51.1% |
| Away win | 21 | 23.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `198` of `227` (87.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 59 | 26.0% | 31 (52.5%) | 11 (18.6%) | 17 (28.8%) |
| 16-30 | 54 | 23.8% | 29 (53.7%) | 15 (27.8%) | 10 (18.5%) |
| 31-45 | 41 | 18.1% | 16 (39.0%) | 9 (22.0%) | 16 (39.0%) |
| 46-60 | 26 | 11.5% | 10 (38.5%) | 6 (23.1%) | 10 (38.5%) |
| 61-75 | 10 | 4.4% | 2 (20.0%) | 4 (40.0%) | 4 (40.0%) |
| 76-90 | 8 | 3.5% | 3 (37.5%) | 0 (0.0%) | 5 (62.5%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **29** of `227` (12.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 190 | 25 | 13.2% |
| 2026-2027 | 37 | 4 | 10.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\scot-champ\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\scot-champ\charts\matches_analysis_home_win_rate.png)

