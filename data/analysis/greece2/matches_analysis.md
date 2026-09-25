# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:00:10+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Super League 2 (Greece)
- Scope: league `greece2`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 289 |
| Home wins | 131 (45.3%) |
| Draws | 67 (23.2%) |
| Away wins | 91 (31.5%) |
| Total goals | 661 |
| Average goals per match | 2.287 |
| Goalless matches | 23 (8.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 265 | 117 (44.2%) | 61 (23.0%) | 87 (32.8%) | 607 | 2.291 | 21 (7.9%) |
| 2026-2027 | 24 | 14 (58.3%) | 6 (25.0%) | 4 (16.7%) | 54 | 2.25 | 2 (8.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 79 (88.8%) | 7 (7.9%) | 3 (3.4%) | 89 |
| HT draw | 48 (35.8%) | 48 (35.8%) | 38 (28.4%) | 134 |
| HT away lead | 4 (6.1%) | 12 (18.2%) | 50 (75.8%) | 66 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **4** (1.4%)
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
| Home lead | 89 | 79 (88.8%) | 7 (7.9%) | 3 (3.4%) |
| Away lead | 66 | 50 (75.8%) | 12 (18.2%) | 4 (6.1%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 48 | 35.8% |
| Draw | 48 | 35.8% |
| Away win | 38 | 28.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `266` of `289` (92.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 81 | 28.0% | 41 (50.6%) | 10 (12.3%) | 30 (37.0%) |
| 16-30 | 51 | 17.6% | 29 (56.9%) | 7 (13.7%) | 15 (29.4%) |
| 31-45 | 46 | 15.9% | 18 (39.1%) | 13 (28.3%) | 15 (32.6%) |
| 46-60 | 40 | 13.8% | 19 (47.5%) | 4 (10.0%) | 17 (42.5%) |
| 61-75 | 31 | 10.7% | 14 (45.2%) | 9 (29.0%) | 8 (25.8%) |
| 76-90 | 12 | 4.2% | 7 (58.3%) | 1 (8.3%) | 4 (33.3%) |
| 91-120 | 5 | 1.7% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **23** of `289` (8.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 265 | 21 | 7.9% |
| 2026-2027 | 24 | 2 | 8.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\greece2\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\greece2\charts\matches_analysis_home_win_rate.png)

