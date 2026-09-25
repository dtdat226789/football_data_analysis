# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T10:56:57+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Superliga (Denmark)
- Scope: league `denmark1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 248 |
| Home wins | 104 (41.9%) |
| Draws | 61 (24.6%) |
| Away wins | 83 (33.5%) |
| Total goals | 763 |
| Average goals per match | 3.077 |
| Goalless matches | 12 (4.8%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 193 | 80 (41.5%) | 45 (23.3%) | 68 (35.2%) | 599 | 3.104 | 11 (5.7%) |
| 2026-2027 | 55 | 24 (43.6%) | 16 (29.1%) | 15 (27.3%) | 164 | 2.982 | 1 (1.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 64 (74.4%) | 15 (17.4%) | 7 (8.1%) | 86 |
| HT draw | 32 (35.2%) | 28 (30.8%) | 31 (34.1%) | 91 |
| HT away lead | 8 (11.3%) | 18 (25.4%) | 45 (63.4%) | 71 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **8** (3.2%)
- Away comebacks (trailing at HT, won at FT): **7** (2.8%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Aarhus | Odense | 0-1 | 2-1 |
| 2025-2026 | Sonderjyske | Silkeborg | 0-1 | 2-1 |
| 2025-2026 | Odense | FC Copenhagen | 0-1 | 2-1 |
| 2025-2026 | Nordsjaelland | Brondby | 0-1 | 2-1 |
| 2025-2026 | Silkeborg | Odense | 0-1 | 3-1 |
| 2025-2026 | Midtjylland | Aarhus | 0-1 | 2-1 |
| 2026-2027 | FC Copenhagen | Lyngby | 1-2 | 3-2 |
| 2026-2027 | Brondby | Silkeborg | 0-1 | 3-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Aarhus | Randers FC | 1-0 | 1-2 |
| 2025-2026 | Odense | Nordsjaelland | 1-0 | 1-2 |
| 2025-2026 | Viborg | Odense | 1-0 | 1-2 |
| 2025-2026 | Nordsjaelland | Odense | 1-0 | 2-4 |
| 2025-2026 | Aarhus | Sonderjyske | 2-1 | 2-3 |
| 2025-2026 | FC Copenhagen | Nordsjaelland | 1-0 | 1-2 |
| 2025-2026 | Midtjylland | Brondby | 2-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 86 | 64 (74.4%) | 15 (17.4%) | 7 (8.1%) |
| Away lead | 71 | 45 (63.4%) | 18 (25.4%) | 8 (11.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 32 | 35.2% |
| Draw | 28 | 30.8% |
| Away win | 31 | 34.1% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `236` of `248` (95.2%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 96 | 38.7% | 43 (44.8%) | 20 (20.8%) | 33 (34.4%) |
| 16-30 | 54 | 21.8% | 24 (44.4%) | 10 (18.5%) | 20 (37.0%) |
| 31-45 | 31 | 12.5% | 13 (41.9%) | 9 (29.0%) | 9 (29.0%) |
| 46-60 | 30 | 12.1% | 13 (43.3%) | 7 (23.3%) | 10 (33.3%) |
| 61-75 | 8 | 3.2% | 2 (25.0%) | 3 (37.5%) | 3 (37.5%) |
| 76-90 | 13 | 5.2% | 7 (53.8%) | 0 (0.0%) | 6 (46.2%) |
| 91-120 | 4 | 1.6% | 2 (50.0%) | 0 (0.0%) | 2 (50.0%) |

## 7. Goalless matches
- Overall: **12** of `248` (4.8%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 193 | 11 | 5.7% |
| 2026-2027 | 55 | 1 | 1.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\denmark1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\denmark1\charts\matches_analysis_home_win_rate.png)

