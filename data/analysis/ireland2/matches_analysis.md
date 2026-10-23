# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:55:56+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 344 |
| Home wins | 165 (48.0%) |
| Draws | 80 (23.3%) |
| Away wins | 99 (28.8%) |
| Total goals | 958 |
| Average goals per match | 2.785 |
| Goalless matches | 19 (5.5%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 179 | 81 (45.3%) | 42 (23.5%) | 56 (31.3%) | 502 | 2.804 | 10 (5.6%) |
| 2026 | 165 | 84 (50.9%) | 38 (23.0%) | 43 (26.1%) | 456 | 2.764 | 9 (5.5%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 98 (85.2%) | 12 (10.4%) | 5 (4.3%) | 115 |
| HT draw | 50 (37.0%) | 49 (36.3%) | 36 (26.7%) | 135 |
| HT away lead | 16 (17.2%) | 19 (20.4%) | 58 (62.4%) | 93 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **16** (4.7%)
- Away comebacks (trailing at HT, won at FT): **5** (1.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Longford | Kerry | 1-2 | 3-2 |
| 2025 | Finn Harps | Kerry | 1-2 | 4-2 |
| 2025 | Longford | Athlone | 1-2 | 3-2 |
| 2025 | Wexford | Kerry | 1-3 | 4-3 |
| 2025 | Wexford | Finn Harps | 0-1 | 2-1 |
| 2025 | Bray | Treaty United | 0-1 | 3-2 |
| 2025 | Bray | Finn Harps | 1-2 | 3-2 |
| 2026 | UC Dublin | Kerry | 0-1 | 2-1 |
| 2026 | Bray | Kerry | 0-1 | 2-1 |
| 2026 | Wexford | Bray | 0-1 | 2-1 |
| 2026 | Cork City | Kerry | 0-2 | 4-2 |
| 2026 | Cobh Ramblers | Finn Harps | 0-1 | 3-1 |
| 2026 | Treaty United | Kerry | 0-1 | 2-1 |
| 2026 | Longford | UC Dublin | 0-1 | 2-1 |
| 2026 | Cork City | Kerry | 0-1 | 3-1 |
| 2026 | UC Dublin | Finn Harps | 1-2 | 5-4 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Treaty United | Cobh Ramblers | 1-0 | 2-3 |
| 2025 | Wexford | Dundalk | 2-1 | 2-3 |
| 2025 | Athlone | Longford | 1-0 | 1-2 |
| 2026 | Cobh Ramblers | UC Dublin | 1-0 | 1-2 |
| 2026 | Cork City | Cobh Ramblers | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 115 | 98 (85.2%) | 12 (10.4%) | 5 (4.3%) |
| Away lead | 93 | 58 (62.4%) | 19 (20.4%) | 16 (17.2%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 50 | 37.0% |
| Draw | 49 | 36.3% |
| Away win | 36 | 26.7% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `324` of `344` (94.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 113 | 32.8% | 59 (52.2%) | 16 (14.2%) | 38 (33.6%) |
| 16-30 | 76 | 22.1% | 40 (52.6%) | 20 (26.3%) | 16 (21.1%) |
| 31-45 | 46 | 13.4% | 26 (56.5%) | 6 (13.0%) | 14 (30.4%) |
| 46-60 | 43 | 12.5% | 20 (46.5%) | 8 (18.6%) | 15 (34.9%) |
| 61-75 | 29 | 8.4% | 12 (41.4%) | 7 (24.1%) | 10 (34.5%) |
| 76-90 | 12 | 3.5% | 3 (25.0%) | 4 (33.3%) | 5 (41.7%) |
| 91-120 | 5 | 1.5% | 4 (80.0%) | 0 (0.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **19** of `344` (5.5%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 179 | 10 | 5.6% |
| 2026 | 165 | 9 | 5.5% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\ireland2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\ireland2\charts\matches_analysis_home_win_rate.png)

