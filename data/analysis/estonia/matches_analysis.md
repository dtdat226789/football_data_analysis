# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:58:02+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Meistriliiga (Estonia)
- Scope: league `estonia`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 325 |
| Home wins | 151 (46.5%) |
| Draws | 42 (12.9%) |
| Away wins | 132 (40.6%) |
| Total goals | 1028 |
| Average goals per match | 3.163 |
| Goalless matches | 9 (2.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 180 | 84 (46.7%) | 24 (13.3%) | 72 (40.0%) | 572 | 3.178 | 4 (2.2%) |
| 2026 | 145 | 67 (46.2%) | 18 (12.4%) | 60 (41.4%) | 456 | 3.145 | 5 (3.4%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 95 (84.1%) | 9 (8.0%) | 9 (8.0%) | 113 |
| HT draw | 35 (36.5%) | 24 (25.0%) | 37 (38.5%) | 96 |
| HT away lead | 12 (12.9%) | 6 (6.5%) | 75 (80.6%) | 93 |
- *23 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **12** (3.7%)
- Away comebacks (trailing at HT, won at FT): **9** (2.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Levadia | Kuressaare | 0-1 | 2-1 |
| 2025 | Harju JK Laagri | Tammeka | 0-1 | 4-1 |
| 2025 | Paide | Levadia | 0-1 | 2-1 |
| 2025 | Flora | Tammeka | 0-1 | 3-1 |
| 2025 | Tallinna Kalev | Tammeka | 1-2 | 3-2 |
| 2025 | Kuressaare | Parnu JK Vaprus | 0-1 | 2-1 |
| 2025 | Kuressaare | Tallinna Kalev | 0-1 | 2-1 |
| 2025 | Tammeka | Tallinna Kalev | 0-1 | 5-2 |
| 2025 | Kalju | Tammeka | 0-1 | 2-1 |
| 2026 | Kuressaare | Tammeka | 1-2 | 3-2 |
| 2026 | Kalju | Narva | 0-1 | 2-1 |
| 2026 | Nomme Utd | Kuressaare | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Narva | Flora | 1-0 | 1-2 |
| 2025 | Flora | Levadia | 2-0 | 2-3 |
| 2025 | Harju JK Laagri | Kalju | 1-0 | 1-3 |
| 2026 | Paide | Flora | 1-0 | 1-2 |
| 2026 | Kuressaare | Levadia | 1-0 | 1-2 |
| 2026 | Harju JK Laagri | Nomme Utd | 1-0 | 1-3 |
| 2026 | Levadia | Flora | 1-0 | 1-2 |
| 2026 | Kalju | Levadia | 2-0 | 2-3 |
| 2026 | Nomme Utd | Flora | 1-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 113 | 95 (84.1%) | 9 (8.0%) | 9 (8.0%) |
| Away lead | 93 | 75 (80.6%) | 6 (6.5%) | 12 (12.9%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 35 | 36.5% |
| Draw | 24 | 25.0% |
| Away win | 37 | 38.5% |
- *23 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `316` of `325` (97.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 111 | 34.2% | 52 (46.8%) | 13 (11.7%) | 46 (41.4%) |
| 16-30 | 93 | 28.6% | 40 (43.0%) | 9 (9.7%) | 44 (47.3%) |
| 31-45 | 55 | 16.9% | 29 (52.7%) | 5 (9.1%) | 21 (38.2%) |
| 46-60 | 30 | 9.2% | 14 (46.7%) | 4 (13.3%) | 12 (40.0%) |
| 61-75 | 14 | 4.3% | 9 (64.3%) | 1 (7.1%) | 4 (28.6%) |
| 76-90 | 6 | 1.8% | 2 (33.3%) | 0 (0.0%) | 4 (66.7%) |
| 91-120 | 7 | 2.2% | 5 (71.4%) | 1 (14.3%) | 1 (14.3%) |

## 7. Goalless matches
- Overall: **9** of `325` (2.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 180 | 4 | 2.2% |
| 2026 | 145 | 5 | 3.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\estonia\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\estonia\charts\matches_analysis_home_win_rate.png)

