# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-23T11:02:27+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: J1 League (Japan)
- Scope: league `japan1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 241 |
| Home wins | 131 (54.4%) |
| Draws | 17 (7.1%) |
| Away wins | 93 (38.6%) |
| Total goals | 699 |
| Average goals per match | 2.900 |
| Goalless matches | 3 (1.2%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2026 | 161 | 94 (58.4%) | 0 (0.0%) | 67 (41.6%) | 462 | 2.87 | 0 (0.0%) |
| 2026-2027 | 80 | 37 (46.2%) | 17 (21.2%) | 26 (32.5%) | 237 | 2.962 | 3 (3.8%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 59 (80.8%) | 4 (5.5%) | 10 (13.7%) | 73 |
| HT draw | 61 (54.0%) | 12 (10.6%) | 40 (35.4%) | 113 |
| HT away lead | 11 (20.0%) | 1 (1.8%) | 43 (78.2%) | 55 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (4.6%)
- Away comebacks (trailing at HT, won at FT): **10** (4.1%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026 | Avispa Fukuoka | Okayama | 0-1 | 2-1 |
| 2026 | Kawasaki Frontale | Mito | 0-2 | 3-2 |
| 2026 | Gamba Osaka | V-Varen Nagasaki | 1-2 | 3-2 |
| 2026 | Avispa Fukuoka | Gamba Osaka | 1-2 | 3-2 |
| 2026 | Kyoto | Nagoya Grampus | 0-1 | 2-1 |
| 2026 | Nagoya Grampus | Avispa Fukuoka | 0-2 | 3-2 |
| 2026 | Sanfrecce Hiroshima | Cerezo Osaka | 0-1 | 2-1 |
| 2026 | Avispa Fukuoka | Sanfrecce Hiroshima | 1-2 | 3-2 |
| 2026 | Shimizu S-Pulse | Cerezo Osaka | 0-1 | 2-1 |
| 2026 | Avispa Fukuoka | Kyoto | 0-1 | 2-1 |
| 2026-2027 | Shimizu S-Pulse | Chiba | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2026 | Kashiwa Reysol | Verdy | 1-0 | 1-2 |
| 2026 | Sanfrecce Hiroshima | Kyoto | 1-0 | 1-2 |
| 2026 | Urawa Reds | Kashima Antlers | 2-1 | 2-3 |
| 2026 | Chiba | Yokohama F. Marinos | 1-0 | 2-3 |
| 2026 | Kyoto | Shimizu S-Pulse | 1-0 | 1-2 |
| 2026 | Sanfrecce Hiroshima | Vissel Kobe | 1-0 | 1-2 |
| 2026-2027 | Yokohama F. Marinos | Kashima Antlers | 2-1 | 3-4 |
| 2026-2027 | Avispa Fukuoka | Urawa Reds | 2-1 | 2-3 |
| 2026-2027 | Kyoto | Kashiwa Reysol | 2-0 | 2-3 |
| 2026-2027 | Machida | Kashiwa Reysol | 1-0 | 2-4 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 73 | 59 (80.8%) | 4 (5.5%) | 10 (13.7%) |
| Away lead | 55 | 43 (78.2%) | 1 (1.8%) | 11 (20.0%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 61 | 54.0% |
| Draw | 12 | 10.6% |
| Away win | 40 | 35.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `238` of `241` (98.8%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 66 | 27.4% | 42 (63.6%) | 1 (1.5%) | 23 (34.8%) |
| 16-30 | 51 | 21.2% | 25 (49.0%) | 3 (5.9%) | 23 (45.1%) |
| 31-45 | 46 | 19.1% | 20 (43.5%) | 4 (8.7%) | 22 (47.8%) |
| 46-60 | 41 | 17.0% | 20 (48.8%) | 4 (9.8%) | 17 (41.5%) |
| 61-75 | 19 | 7.9% | 14 (73.7%) | 1 (5.3%) | 4 (21.1%) |
| 76-90 | 14 | 5.8% | 10 (71.4%) | 1 (7.1%) | 3 (21.4%) |
| 91-120 | 1 | 0.4% | 0 (0.0%) | 0 (0.0%) | 1 (100.0%) |

## 7. Goalless matches
- Overall: **3** of `241` (1.2%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2026 | 161 | 0 | 0.0% |
| 2026-2027 | 80 | 3 | 3.8% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\japan1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\japan1\charts\matches_analysis_home_win_rate.png)

