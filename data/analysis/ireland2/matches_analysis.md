# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:01:31+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Division 1 (Ireland)
- Scope: league `ireland2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 339 |
| Home wins | 162 (47.8%) |
| Draws | 79 (23.3%) |
| Away wins | 98 (28.9%) |
| Total goals | 941 |
| Average goals per match | 2.776 |
| Goalless matches | 19 (5.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 179 | 81 (45.3%) | 42 (23.5%) | 56 (31.3%) | 502 | 2.804 | 10 (5.6%) |
| 2026 | 160 | 81 (50.6%) | 37 (23.1%) | 42 (26.2%) | 439 | 2.744 | 9 (5.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 97 (85.1%) | 12 (10.5%) | 5 (4.4%) | 114 |
| HT draw | 48 (36.4%) | 48 (36.4%) | 36 (27.3%) | 132 |
| HT away lead | 16 (17.4%) | 19 (20.7%) | 57 (62.0%) | 92 |
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
| Home lead | 114 | 97 (85.1%) | 12 (10.5%) | 5 (4.4%) |
| Away lead | 92 | 57 (62.0%) | 19 (20.7%) | 16 (17.4%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 48 | 36.4% |
| Draw | 48 | 36.4% |
| Away win | 36 | 27.3% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `319` of `339` (94.1%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 112 | 33.0% | 59 (52.7%) | 15 (13.4%) | 38 (33.9%) |
| 16-30 | 75 | 22.1% | 40 (53.3%) | 20 (26.7%) | 15 (20.0%) |
| 31-45 | 45 | 13.3% | 25 (55.6%) | 6 (13.3%) | 14 (31.1%) |
| 46-60 | 42 | 12.4% | 19 (45.2%) | 8 (19.0%) | 15 (35.7%) |
| 61-75 | 28 | 8.3% | 11 (39.3%) | 7 (25.0%) | 10 (35.7%) |
| 76-90 | 12 | 3.5% | 3 (25.0%) | 4 (33.3%) | 5 (41.7%) |
| 91-120 | 5 | 1.5% | 4 (80.0%) | 0 (0.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **19** of `339` (5.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 179 | 10 | 5.6% |
| 2026 | 160 | 9 | 5.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\ireland2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\ireland2\charts\matches_analysis_home_win_rate.png)

