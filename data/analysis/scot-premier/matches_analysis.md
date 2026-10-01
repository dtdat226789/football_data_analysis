# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:06:00+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premiership (Scotland)
- Scope: league `scot-premier`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 276 |
| Home wins | 121 (43.8%) |
| Draws | 73 (26.4%) |
| Away wins | 82 (29.7%) |
| Total goals | 750 |
| Average goals per match | 2.717 |
| Goalless matches | 19 (6.9%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 234 | 105 (44.9%) | 64 (27.4%) | 65 (27.8%) | 643 | 2.748 | 17 (7.3%) |
| 2026-2027 | 42 | 16 (38.1%) | 9 (21.4%) | 17 (40.5%) | 107 | 2.548 | 2 (4.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 78 (78.0%) | 13 (13.0%) | 9 (9.0%) | 100 |
| HT draw | 34 (35.8%) | 42 (44.2%) | 19 (20.0%) | 95 |
| HT away lead | 9 (11.1%) | 18 (22.2%) | 54 (66.7%) | 81 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **9** (3.3%)
- Away comebacks (trailing at HT, won at FT): **9** (3.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Falkirk | Dundee FC | 0-1 | 2-1 |
| 2025-2026 | Aberdeen | Kilmarnock | 0-1 | 2-1 |
| 2025-2026 | Dundee Utd | Celtic | 0-1 | 2-1 |
| 2025-2026 | Dundee FC | Kilmarnock | 0-1 | 2-1 |
| 2025-2026 | Hearts | Rangers | 0-1 | 2-1 |
| 2025-2026 | Partick Thistle | Dunfermline | 0-1 | 2-1 |
| 2025-2026 | Dundee FC | Aberdeen | 1-2 | 3-2 |
| 2026-2027 | Aberdeen | Hearts | 0-1 | 2-1 |
| 2026-2027 | Hearts | Dundee FC | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Dundee Utd | Hearts | 2-1 | 2-3 |
| 2025-2026 | Livingston | Hearts | 1-0 | 1-2 |
| 2025-2026 | Motherwell | Falkirk | 1-0 | 1-2 |
| 2025-2026 | Livingston | Motherwell | 1-0 | 1-2 |
| 2025-2026 | Celtic | Rangers | 1-0 | 1-3 |
| 2025-2026 | Kilmarnock | Celtic | 2-0 | 2-3 |
| 2025-2026 | Falkirk | Rangers | 2-1 | 3-6 |
| 2025-2026 | Hibernian | Hearts | 1-0 | 1-2 |
| 2026-2027 | St. Mirren | Celtic | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 100 | 78 (78.0%) | 13 (13.0%) | 9 (9.0%) |
| Away lead | 81 | 54 (66.7%) | 18 (22.2%) | 9 (11.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 34 | 35.8% |
| Draw | 42 | 44.2% |
| Away win | 19 | 20.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `257` of `276` (93.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 80 | 29.0% | 35 (43.8%) | 15 (18.8%) | 30 (37.5%) |
| 16-30 | 79 | 28.6% | 37 (46.8%) | 16 (20.3%) | 26 (32.9%) |
| 31-45 | 50 | 18.1% | 25 (50.0%) | 10 (20.0%) | 15 (30.0%) |
| 46-60 | 22 | 8.0% | 10 (45.5%) | 8 (36.4%) | 4 (18.2%) |
| 61-75 | 14 | 5.1% | 6 (42.9%) | 4 (28.6%) | 4 (28.6%) |
| 76-90 | 7 | 2.5% | 5 (71.4%) | 1 (14.3%) | 1 (14.3%) |
| 91-120 | 5 | 1.8% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **19** of `276` (6.9%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 234 | 17 | 7.3% |
| 2026-2027 | 42 | 2 | 4.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\scot-premier\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\scot-premier\charts\matches_analysis_home_win_rate.png)

