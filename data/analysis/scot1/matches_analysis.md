# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:06:15+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 230 |
| Home wins | 99 (43.0%) |
| Draws | 61 (26.5%) |
| Away wins | 70 (30.4%) |
| Total goals | 614 |
| Average goals per match | 2.670 |
| Goalless matches | 14 (6.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 191 | 80 (41.9%) | 52 (27.2%) | 59 (30.9%) | 511 | 2.675 | 10 (5.2%) |
| 2026-2027 | 39 | 19 (48.7%) | 9 (23.1%) | 11 (28.2%) | 103 | 2.641 | 4 (10.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 62 (80.5%) | 12 (15.6%) | 3 (3.9%) | 77 |
| HT draw | 31 (36.9%) | 31 (36.9%) | 22 (26.2%) | 84 |
| HT away lead | 6 (8.7%) | 18 (26.1%) | 45 (65.2%) | 69 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (2.6%)
- Away comebacks (trailing at HT, won at FT): **3** (1.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Montrose | Inverness | 0-1 | 2-1 |
| 2025-2026 | Queen of South | Kelty Hearts | 0-1 | 3-1 |
| 2025-2026 | Inverness | Alloa | 0-1 | 3-1 |
| 2025-2026 | East Fife | Cove Rangers | 0-1 | 2-1 |
| 2025-2026 | Alloa | Kelty Hearts | 0-1 | 2-1 |
| 2026-2027 | Queen of South | Airdrieonians | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Hamilton | East Fife | 1-0 | 1-2 |
| 2025-2026 | Kelty Hearts | Cove Rangers | 2-1 | 2-5 |
| 2025-2026 | Alloa | Peterhead | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 77 | 62 (80.5%) | 12 (15.6%) | 3 (3.9%) |
| Away lead | 69 | 45 (65.2%) | 18 (26.1%) | 6 (8.7%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 31 | 36.9% |
| Draw | 31 | 36.9% |
| Away win | 22 | 26.2% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `216` of `230` (93.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 74 | 32.2% | 39 (52.7%) | 12 (16.2%) | 23 (31.1%) |
| 16-30 | 51 | 22.2% | 27 (52.9%) | 9 (17.6%) | 15 (29.4%) |
| 31-45 | 41 | 17.8% | 10 (24.4%) | 13 (31.7%) | 18 (43.9%) |
| 46-60 | 24 | 10.4% | 11 (45.8%) | 8 (33.3%) | 5 (20.8%) |
| 61-75 | 17 | 7.4% | 9 (52.9%) | 3 (17.6%) | 5 (29.4%) |
| 76-90 | 8 | 3.5% | 2 (25.0%) | 2 (25.0%) | 4 (50.0%) |
| 91-120 | 1 | 0.4% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **14** of `230` (6.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 191 | 10 | 5.2% |
| 2026-2027 | 39 | 4 | 10.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\scot1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\scot1\charts\matches_analysis_home_win_rate.png)

