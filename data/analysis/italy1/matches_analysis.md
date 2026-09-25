# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:01:40+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Serie A (Italy)
- Scope: league `italy1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 430 |
| Home wins | 170 (39.5%) |
| Draws | 108 (25.1%) |
| Away wins | 152 (35.3%) |
| Total goals | 1067 |
| Average goals per match | 2.481 |
| Goalless matches | 36 (8.4%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 148 (38.9%) | 99 (26.1%) | 133 (35.0%) | 922 | 2.426 | 36 (9.5%) |
| 2026-2027 | 50 | 22 (44.0%) | 9 (18.0%) | 19 (38.0%) | 145 | 2.9 | 0 (0.0%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 101 (80.8%) | 18 (14.4%) | 6 (4.8%) | 125 |
| HT draw | 62 (32.8%) | 65 (34.4%) | 62 (32.8%) | 189 |
| HT away lead | 7 (6.0%) | 25 (21.6%) | 84 (72.4%) | 116 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (1.6%)
- Away comebacks (trailing at HT, won at FT): **6** (1.4%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Napoli | Genoa | 0-1 | 2-1 |
| 2025-2026 | Torino | Genoa | 0-1 | 2-1 |
| 2025-2026 | Genoa | Bologna | 0-1 | 3-2 |
| 2025-2026 | Atalanta | Napoli | 0-1 | 2-1 |
| 2025-2026 | Napoli | Lecce | 0-1 | 2-1 |
| 2025-2026 | Como | AS Roma | 0-1 | 2-1 |
| 2025-2026 | Sassuolo | Cagliari | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Fiorentina | Como | 1-0 | 1-2 |
| 2025-2026 | Torino | AC Milan | 2-1 | 2-3 |
| 2025-2026 | Lecce | Parma | 1-0 | 1-2 |
| 2025-2026 | Udinese | Sassuolo | 1-0 | 1-2 |
| 2025-2026 | Como | Inter | 2-1 | 3-4 |
| 2025-2026 | Cremonese | Lazio | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 125 | 101 (80.8%) | 18 (14.4%) | 6 (4.8%) |
| Away lead | 116 | 84 (72.4%) | 25 (21.6%) | 7 (6.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 62 | 32.8% |
| Draw | 65 | 34.4% |
| Away win | 62 | 32.8% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `394` of `430` (91.6%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 128 | 29.8% | 58 (45.3%) | 26 (20.3%) | 44 (34.4%) |
| 16-30 | 88 | 20.5% | 34 (38.6%) | 19 (21.6%) | 35 (39.8%) |
| 31-45 | 58 | 13.5% | 27 (46.6%) | 9 (15.5%) | 22 (37.9%) |
| 46-60 | 55 | 12.8% | 24 (43.6%) | 9 (16.4%) | 22 (40.0%) |
| 61-75 | 39 | 9.1% | 17 (43.6%) | 5 (12.8%) | 17 (43.6%) |
| 76-90 | 21 | 4.9% | 7 (33.3%) | 4 (19.0%) | 10 (47.6%) |
| 91-120 | 5 | 1.2% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **36** of `430` (8.4%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 380 | 36 | 9.5% |
| 2026-2027 | 50 | 0 | 0.0% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\italy1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\italy1\charts\matches_analysis_home_win_rate.png)

