# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T13:50:50+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Premiere Ligue Women (France)
- Scope: league `wfrance1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 153 |
| Home wins | 62 (40.5%) |
| Draws | 28 (18.3%) |
| Away wins | 63 (41.2%) |
| Total goals | 471 |
| Average goals per match | 3.078 |
| Goalless matches | 8 (5.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 135 | 53 (39.3%) | 25 (18.5%) | 57 (42.2%) | 410 | 3.037 | 7 (5.2%) |
| 2026-2027 | 18 | 9 (50.0%) | 3 (16.7%) | 6 (33.3%) | 61 | 3.389 | 1 (5.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 39 (84.8%) | 5 (10.9%) | 2 (4.3%) | 46 |
| HT draw | 18 (37.5%) | 17 (35.4%) | 13 (27.1%) | 48 |
| HT away lead | 4 (7.3%) | 6 (10.9%) | 45 (81.8%) | 55 |
- *4 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (2.6%)
- Away comebacks (trailing at HT, won at FT): **2** (1.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Dijon W | Montpellier W | 0-1 | 2-1 |
| 2025-2026 | Le Havre W | Montpellier W | 0-1 | 3-2 |
| 2025-2026 | Nantes W | Le Havre W | 0-1 | 2-1 |
| 2025-2026 | Dijon W | Le Havre W | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Nantes W | Dijon W | 1-0 | 1-2 |
| 2025-2026 | Lens W | Paris FC W | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 46 | 39 (84.8%) | 5 (10.9%) | 2 (4.3%) |
| Away lead | 55 | 45 (81.8%) | 6 (10.9%) | 4 (7.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 18 | 37.5% |
| Draw | 17 | 35.4% |
| Away win | 13 | 27.1% |
- *4 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `141` of `153` (92.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 55 | 35.9% | 24 (43.6%) | 6 (10.9%) | 25 (45.5%) |
| 16-30 | 34 | 22.2% | 15 (44.1%) | 5 (14.7%) | 14 (41.2%) |
| 31-45 | 22 | 14.4% | 9 (40.9%) | 2 (9.1%) | 11 (50.0%) |
| 46-60 | 20 | 13.1% | 8 (40.0%) | 6 (30.0%) | 6 (30.0%) |
| 61-75 | 6 | 3.9% | 3 (50.0%) | 1 (16.7%) | 2 (33.3%) |
| 76-90 | 3 | 2.0% | 1 (33.3%) | 0 (0.0%) | 2 (66.7%) |
| 91-120 | 1 | 0.7% | 1 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **8** of `153` (5.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 135 | 7 | 5.2% |
| 2026-2027 | 18 | 1 | 5.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\wfrance1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\wfrance1\charts\matches_analysis_home_win_rate.png)

