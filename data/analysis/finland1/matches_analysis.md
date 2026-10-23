# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:49:29+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: Veikkausliiga (Finland)
- Scope: league `finland1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 273 |
| Home wins | 119 (43.6%) |
| Draws | 67 (24.5%) |
| Away wins | 87 (31.9%) |
| Total goals | 789 |
| Average goals per match | 2.890 |
| Goalless matches | 18 (6.6%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025 | 132 | 56 (42.4%) | 29 (22.0%) | 47 (35.6%) | 433 | 3.28 | 8 (6.1%) |
| 2026 | 141 | 63 (44.7%) | 38 (27.0%) | 40 (28.4%) | 356 | 2.525 | 10 (7.1%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 69 (74.2%) | 15 (16.1%) | 9 (9.7%) | 93 |
| HT draw | 39 (37.9%) | 42 (40.8%) | 22 (21.4%) | 103 |
| HT away lead | 11 (14.3%) | 10 (13.0%) | 56 (72.7%) | 77 |

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **11** (4.0%)
- Away comebacks (trailing at HT, won at FT): **9** (3.3%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Ilves | HJK | 1-2 | 3-2 |
| 2025 | VPS | AC Oulu | 0-2 | 4-3 |
| 2025 | Haka | AC Oulu | 0-1 | 2-1 |
| 2025 | Gnistan | KTP | 0-1 | 2-1 |
| 2025 | AC Oulu | KTP | 0-1 | 3-2 |
| 2025 | SJK | Gnistan | 0-1 | 3-1 |
| 2025 | VPS | KTP | 1-2 | 3-2 |
| 2026 | Inter Turku | Ilves | 0-1 | 2-1 |
| 2026 | VPS | HJK | 0-1 | 2-1 |
| 2026 | TPS | Jaro | 1-2 | 3-2 |
| 2026 | HJK | Inter Turku | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025 | Mariehamn | SJK | 1-0 | 1-2 |
| 2025 | Gnistan | KuPS | 1-0 | 1-2 |
| 2025 | HJK | Jaro | 1-0 | 2-3 |
| 2025 | VPS | SJK | 1-0 | 1-2 |
| 2025 | Haka | HJK | 1-0 | 1-2 |
| 2026 | Jaro | HJK | 2-1 | 2-5 |
| 2026 | SJK | VPS | 1-0 | 1-2 |
| 2026 | AC Oulu | Inter Turku | 2-0 | 2-3 |
| 2026 | HJK | Gnistan | 2-0 | 2-3 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 93 | 69 (74.2%) | 15 (16.1%) | 9 (9.7%) |
| Away lead | 77 | 56 (72.7%) | 10 (13.0%) | 11 (14.3%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 39 | 37.9% |
| Draw | 42 | 40.8% |
| Away win | 22 | 21.4% |

## 6. First-goal timing
- Matches with a first-goal time recorded: `255` of `273` (93.4%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 85 | 31.1% | 41 (48.2%) | 20 (23.5%) | 24 (28.2%) |
| 16-30 | 62 | 22.7% | 27 (43.5%) | 9 (14.5%) | 26 (41.9%) |
| 31-45 | 43 | 15.8% | 16 (37.2%) | 10 (23.3%) | 17 (39.5%) |
| 46-60 | 37 | 13.6% | 21 (56.8%) | 4 (10.8%) | 12 (32.4%) |
| 61-75 | 15 | 5.5% | 6 (40.0%) | 4 (26.7%) | 5 (33.3%) |
| 76-90 | 11 | 4.0% | 6 (54.5%) | 2 (18.2%) | 3 (27.3%) |
| 91-120 | 2 | 0.7% | 2 (100.0%) | 0 (0.0%) | 0 (0.0%) |

## 7. Goalless matches
- Overall: **18** of `273` (6.6%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025 | 132 | 8 | 6.1% |
| 2026 | 141 | 10 | 7.1% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\finland1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\finland1\charts\matches_analysis_home_win_rate.png)

