# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:10:00+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 231 |
| Home wins | 103 (44.6%) |
| Draws | 52 (22.5%) |
| Away wins | 76 (32.9%) |
| Total goals | 702 |
| Average goals per match | 3.039 |
| Goalless matches | 14 (6.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 186 | 83 (44.6%) | 40 (21.5%) | 63 (33.9%) | 566 | 3.043 | 12 (6.5%) |
| 2026-2027 | 45 | 20 (44.4%) | 12 (26.7%) | 13 (28.9%) | 136 | 3.022 | 2 (4.4%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 60 (81.1%) | 12 (16.2%) | 2 (2.7%) | 74 |
| HT draw | 39 (39.8%) | 30 (30.6%) | 29 (29.6%) | 98 |
| HT away lead | 4 (6.8%) | 10 (16.9%) | 45 (76.3%) | 59 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.7%)
- Away comebacks (trailing at HT, won at FT): **2** (0.9%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Yverdon | Lausanne Ouchy | 1-2 | 3-2 |
| 2025-2026 | Xamax | Wil | 0-1 | 3-1 |
| 2025-2026 | Aarau | Rapperswil-Jona | 1-2 | 5-3 |
| 2026-2027 | Aarau | Rapperswil-Jona | 0-1 | 3-2 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Wil | Yverdon | 2-0 | 2-4 |
| 2025-2026 | Rapperswil-Jona | Xamax | 2-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 74 | 60 (81.1%) | 12 (16.2%) | 2 (2.7%) |
| Away lead | 59 | 45 (76.3%) | 10 (16.9%) | 4 (6.8%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 39 | 39.8% |
| Draw | 30 | 30.6% |
| Away win | 29 | 29.6% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `217` of `231` (93.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 100 | 43.3% | 49 (49.0%) | 18 (18.0%) | 33 (33.0%) |
| 16-30 | 38 | 16.5% | 18 (47.4%) | 7 (18.4%) | 13 (34.2%) |
| 31-45 | 30 | 13.0% | 9 (30.0%) | 7 (23.3%) | 14 (46.7%) |
| 46-60 | 22 | 9.5% | 12 (54.5%) | 3 (13.6%) | 7 (31.8%) |
| 61-75 | 16 | 6.9% | 8 (50.0%) | 2 (12.5%) | 6 (37.5%) |
| 76-90 | 6 | 2.6% | 3 (50.0%) | 1 (16.7%) | 2 (33.3%) |
| 91-120 | 5 | 2.2% | 4 (80.0%) | 0 (0.0%) | 1 (20.0%) |

## 7. Goalless matches
- Overall: **14** of `231` (6.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 186 | 12 | 6.5% |
| 2026-2027 | 45 | 2 | 4.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\swiss2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\swiss2\charts\matches_analysis_home_win_rate.png)

