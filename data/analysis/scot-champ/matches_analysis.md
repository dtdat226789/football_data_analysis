# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:05:45+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 231 |
| Home wins | 93 (40.3%) |
| Draws | 74 (32.0%) |
| Away wins | 64 (27.7%) |
| Total goals | 540 |
| Average goals per match | 2.338 |
| Goalless matches | 29 (12.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 190 | 74 (38.9%) | 64 (33.7%) | 52 (27.4%) | 460 | 2.421 | 25 (13.2%) |
| 2026-2027 | 41 | 19 (46.3%) | 10 (24.4%) | 12 (29.3%) | 80 | 1.951 | 4 (9.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 60 (81.1%) | 13 (17.6%) | 1 (1.4%) | 74 |
| HT draw | 23 (25.3%) | 46 (50.5%) | 22 (24.2%) | 91 |
| HT away lead | 10 (15.2%) | 15 (22.7%) | 41 (62.1%) | 66 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (4.3%)
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
| Home lead | 74 | 60 (81.1%) | 13 (17.6%) | 1 (1.4%) |
| Away lead | 66 | 41 (62.1%) | 15 (22.7%) | 10 (15.2%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 23 | 25.3% |
| Draw | 46 | 50.5% |
| Away win | 22 | 24.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `202` of `231` (87.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 60 | 26.0% | 32 (53.3%) | 11 (18.3%) | 17 (28.3%) |
| 16-30 | 56 | 24.2% | 30 (53.6%) | 15 (26.8%) | 11 (19.6%) |
| 31-45 | 41 | 17.7% | 16 (39.0%) | 9 (22.0%) | 16 (39.0%) |
| 46-60 | 27 | 11.7% | 10 (37.0%) | 6 (22.2%) | 11 (40.7%) |
| 61-75 | 10 | 4.3% | 2 (20.0%) | 4 (40.0%) | 4 (40.0%) |
| 76-90 | 8 | 3.5% | 3 (37.5%) | 0 (0.0%) | 5 (62.5%) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **29** of `231` (12.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 190 | 25 | 13.2% |
| 2026-2027 | 41 | 4 | 9.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\scot-champ\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\scot-champ\charts\matches_analysis_home_win_rate.png)

