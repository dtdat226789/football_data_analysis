# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-10-26T01:30:20+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Professional Development League (England)
- Scope: league `develop21`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 61 |
| Home wins | 26 (42.6%) |
| Draws | 14 (23.0%) |
| Away wins | 21 (34.4%) |
| Total goals | 237 |
| Average goals per match | 3.885 |
| Goalless matches | 1 (1.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2026-2027 | 61 | 26 (42.6%) | 14 (23.0%) | 21 (34.4%) | 237 | 3.885 | 1 (1.6%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 19 (76.0%) | 5 (20.0%) | 1 (4.0%) | 25 |
| HT draw | 5 (33.3%) | 4 (26.7%) | 6 (40.0%) | 15 |
| HT away lead | 2 (9.5%) | 5 (23.8%) | 14 (66.7%) | 21 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **2** (3.3%)
- Away comebacks (trailing at HT, won at FT): **1** (1.6%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026-2027 | Bristol City U21 | Sheffield Utd U21 | 0-1 | 3-1 |
| 2026-2027 | Wigan U21 | Colchester U21 | 1-2 | 6-4 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026-2027 | Millwall U21 | Huddersfield U21 | 2-0 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 25 | 19 (76.0%) | 5 (20.0%) | 1 (4.0%) |
| Away lead | 21 | 14 (66.7%) | 5 (23.8%) | 2 (9.5%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 5 | 33.3% |
| Draw | 4 | 26.7% |
| Away win | 6 | 40.0% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `60` of `61` (98.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 19 | 31.1% | 7 (36.8%) | 5 (26.3%) | 7 (36.8%) |
| 16-30 | 21 | 34.4% | 12 (57.1%) | 3 (14.3%) | 6 (28.6%) |
| 31-45 | 15 | 24.6% | 5 (33.3%) | 4 (26.7%) | 6 (40.0%) |
| 46-60 | 2 | 3.3% | 0 (0.0%) | 1 (50.0%) | 1 (50.0%) |
| 61-75 | 3 | 4.9% | 2 (66.7%) | 0 (0.0%) | 1 (33.3%) |
| 76-90 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |
| 91-120 | 0 | 0.0% | 0 (-) | 0 (-) | 0 (-) |

## 7. Goalless matches
- Overall: **1** of `61` (1.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2026-2027 | 61 | 1 | 1.6% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](charts/matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](charts/matches_analysis_home_win_rate.png)

