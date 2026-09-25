# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:00:53+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: NB I. (Hungary)
- Scope: league `hungary1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 245 |
| Home wins | 98 (40.0%) |
| Draws | 62 (25.3%) |
| Away wins | 85 (34.7%) |
| Total goals | 747 |
| Average goals per match | 3.049 |
| Goalless matches | 10 (4.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 198 | 78 (39.4%) | 49 (24.7%) | 71 (35.9%) | 594 | 3.0 | 8 (4.0%) |
| 2026-2027 | 47 | 20 (42.6%) | 13 (27.7%) | 14 (29.8%) | 153 | 3.255 | 2 (4.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 55 (75.3%) | 13 (17.8%) | 5 (6.8%) | 73 |
| HT draw | 33 (32.7%) | 33 (32.7%) | 35 (34.7%) | 101 |
| HT away lead | 10 (14.1%) | 16 (22.5%) | 45 (63.4%) | 71 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **10** (4.1%)
- Away comebacks (trailing at HT, won at FT): **5** (2.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Puskas Academy | Nyiregyhaza | 1-2 | 3-2 |
| 2025-2026 | Nyiregyhaza | Zalaegerszegi | 0-1 | 3-1 |
| 2025-2026 | Kisvarda | Gyor | 1-2 | 3-2 |
| 2025-2026 | Debrecen | DVTK | 1-2 | 3-2 |
| 2025-2026 | Nyiregyhaza | MTK Budapest | 1-2 | 4-2 |
| 2025-2026 | Zalaegerszegi | Ferencvaros | 0-1 | 3-1 |
| 2025-2026 | Kisvarda | Paks | 0-1 | 2-1 |
| 2025-2026 | Ferencvaros | DVTK | 0-1 | 3-1 |
| 2026-2027 | Nyiregyhaza | Ujpest | 0-1 | 2-1 |
| 2026-2027 | Ujpest | Zalaegerszegi | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Debrecen | Nyiregyhaza | 1-0 | 1-2 |
| 2025-2026 | Ujpest | MTK Budapest | 1-0 | 1-2 |
| 2025-2026 | DVTK | Puskas Academy | 1-0 | 1-2 |
| 2026-2027 | Honved | Vasas | 1-0 | 1-2 |
| 2026-2027 | Debrecen | Vasas | 2-1 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 73 | 55 (75.3%) | 13 (17.8%) | 5 (6.8%) |
| Away lead | 71 | 45 (63.4%) | 16 (22.5%) | 10 (14.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 33 | 32.7% |
| Draw | 33 | 32.7% |
| Away win | 35 | 34.7% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `235` of `245` (95.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 74 | 30.2% | 39 (52.7%) | 11 (14.9%) | 24 (32.4%) |
| 16-30 | 63 | 25.7% | 24 (38.1%) | 16 (25.4%) | 23 (36.5%) |
| 31-45 | 31 | 12.7% | 9 (29.0%) | 10 (32.3%) | 12 (38.7%) |
| 46-60 | 45 | 18.4% | 18 (40.0%) | 14 (31.1%) | 13 (28.9%) |
| 61-75 | 11 | 4.5% | 4 (36.4%) | 0 (0.0%) | 7 (63.6%) |
| 76-90 | 10 | 4.1% | 3 (30.0%) | 1 (10.0%) | 6 (60.0%) |
| 91-120 | 1 | 0.4% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **10** of `245` (4.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 198 | 8 | 4.0% |
| 2026-2027 | 47 | 2 | 4.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\hungary1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\hungary1\charts\matches_analysis_home_win_rate.png)

