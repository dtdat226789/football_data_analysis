# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:51:58+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 297 |
| Home wins | 138 (46.5%) |
| Draws | 68 (22.9%) |
| Away wins | 91 (30.6%) |
| Total goals | 676 |
| Average goals per match | 2.276 |
| Goalless matches | 24 (8.1%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 265 | 117 (44.2%) | 61 (23.0%) | 87 (32.8%) | 607 | 2.291 | 21 (7.9%) |
| 2026-2027 | 32 | 21 (65.6%) | 7 (21.9%) | 4 (12.5%) | 69 | 2.156 | 3 (9.4%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 82 (89.1%) | 7 (7.6%) | 3 (3.3%) | 92 |
| HT draw | 52 (37.4%) | 49 (35.3%) | 38 (27.3%) | 139 |
| HT away lead | 4 (6.1%) | 12 (18.2%) | 50 (75.8%) | 66 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.3%)
- Away comebacks (trailing at HT, won at FT): **3** (1.0%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Panionios | Olympiacos Piraeus B | 0-1 | 4-1 |
| 2025-2026 | Olympiacos Piraeus B | PAE Egaleo | 0-1 | 2-1 |
| 2025-2026 | Kavala | PAOK B | 0-1 | 2-1 |
| 2025-2026 | PAOK B | Giannina | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Chrisoupolis | Iraklis 1908 | 1-0 | 1-2 |
| 2025-2026 | Kampaniakos | Makedonikos | 1-0 | 1-2 |
| 2026-2027 | Niki Volos | Olympiacos Piraeus B | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 92 | 82 (89.1%) | 7 (7.6%) | 3 (3.3%) |
| Away lead | 66 | 50 (75.8%) | 12 (18.2%) | 4 (6.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 52 | 37.4% |
| Draw | 49 | 35.3% |
| Away win | 38 | 27.3% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `273` of `297` (91.9%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 84 | 28.3% | 44 (52.4%) | 10 (11.9%) | 30 (35.7%) |
| 16-30 | 52 | 17.5% | 30 (57.7%) | 7 (13.5%) | 15 (28.8%) |
| 31-45 | 46 | 15.5% | 18 (39.1%) | 13 (28.3%) | 15 (32.6%) |
| 46-60 | 41 | 13.8% | 20 (48.8%) | 4 (9.8%) | 17 (41.5%) |
| 61-75 | 32 | 10.8% | 15 (46.9%) | 9 (28.1%) | 8 (25.0%) |
| 76-90 | 13 | 4.4% | 8 (61.5%) | 1 (7.7%) | 4 (30.8%) |
| 91-120 | 5 | 1.7% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **24** of `297` (8.1%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 265 | 21 | 7.9% |
| 2026-2027 | 32 | 3 | 9.4% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\greece2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\greece2\charts\matches_analysis_home_win_rate.png)

