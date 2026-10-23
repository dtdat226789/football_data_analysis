# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T16:01:26+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: TOPLYGA (Lithuania)
- Scope: league `lithuania`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 324 |
| Home wins | 130 (40.1%) |
| Draws | 84 (25.9%) |
| Away wins | 110 (34.0%) |
| Total goals | 860 |
| Average goals per match | 2.654 |
| Goalless matches | 29 (9.0%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 180 | 73 (40.6%) | 44 (24.4%) | 63 (35.0%) | 479 | 2.661 | 13 (7.2%) |
| 2026 | 144 | 57 (39.6%) | 40 (27.8%) | 47 (32.6%) | 381 | 2.646 | 16 (11.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 84 (78.5%) | 16 (15.0%) | 7 (6.5%) | 107 |
| HT draw | 39 (29.8%) | 50 (38.2%) | 42 (32.1%) | 131 |
| HT away lead | 7 (8.2%) | 18 (21.2%) | 60 (70.6%) | 85 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **7** (2.2%)
- Away comebacks (trailing at HT, won at FT): **7** (2.2%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Hegelmann | Dainava Alytus | 0-2 | 3-2 |
| 2025 | Dainava Alytus | Banga | 0-1 | 2-1 |
| 2025 | Dziugas Telsiai | Riteriai | 0-1 | 2-1 |
| 2025 | Suduva | Banga | 0-1 | 2-1 |
| 2026 | FA Siauliai | FK Panevezys | 0-1 | 3-1 |
| 2026 | FA Siauliai | Suduva | 0-1 | 2-1 |
| 2026 | FK Panevezys | Zalgiris | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Kauno Zalgiris | Dziugas Telsiai | 1-0 | 1-2 |
| 2025 | Siauliai FA | Kauno Zalgiris | 2-1 | 2-3 |
| 2025 | Banga | Siauliai FA | 1-0 | 1-2 |
| 2025 | Zalgiris | FK Panevezys | 2-1 | 2-3 |
| 2026 | Riteriai | Kauno Zalgiris | 1-0 | 1-2 |
| 2026 | Transinvest | Kauno Zalgiris | 1-0 | 1-2 |
| 2026 | FK Panevezys | Suduva | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 107 | 84 (78.5%) | 16 (15.0%) | 7 (6.5%) |
| Away lead | 85 | 60 (70.6%) | 18 (21.2%) | 7 (8.2%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 39 | 29.8% |
| Draw | 50 | 38.2% |
| Away win | 42 | 32.1% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `294` of `324` (90.7%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 87 | 26.9% | 43 (49.4%) | 18 (20.7%) | 26 (29.9%) |
| 16-30 | 67 | 20.7% | 26 (38.8%) | 15 (22.4%) | 26 (38.8%) |
| 31-45 | 60 | 18.5% | 28 (46.7%) | 8 (13.3%) | 24 (40.0%) |
| 46-60 | 39 | 12.0% | 19 (48.7%) | 6 (15.4%) | 14 (35.9%) |
| 61-75 | 23 | 7.1% | 6 (26.1%) | 6 (26.1%) | 11 (47.8%) |
| 76-90 | 12 | 3.7% | 4 (33.3%) | 2 (16.7%) | 6 (50.0%) |
| 91-120 | 6 | 1.9% | 4 (66.7%) | 0 (0.0%) | 2 (33.3%) |

## 7. Goalless matches
- Overall: **29** of `324` (9.0%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 180 | 13 | 7.2% |
| 2026 | 144 | 16 | 11.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\lithuania\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\lithuania\charts\matches_analysis_home_win_rate.png)

