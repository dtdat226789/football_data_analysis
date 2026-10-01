# Match Analysis
- Report: `matches_analysis`
- Generated: 2026-09-29T15:45:53+00:00
- Script: `backend/scripts/analyze_matches.py` v1.0.0
- League: efbet League (Bulgaria)
- Scope: league `bulgaria1`

## 1. Overall summary
| metric | value |
|---|---|
| Matches | 363 |
| Home wins | 156 (43.0%) |
| Draws | 99 (27.3%) |
| Away wins | 108 (29.8%) |
| Total goals | 861 |
| Average goals per match | 2.372 |
| Goalless matches | 39 (10.7%) |

## 2. Per-season breakdown
| season | matches | home wins | draws | away wins | total goals | avg goals | goalless |
|---|---|---|---|---|---|---|---|
| 2025-2026 | 294 | 125 (42.5%) | 82 (27.9%) | 87 (29.6%) | 677 | 2.303 | 36 (12.2%) |
| 2026-2027 | 69 | 31 (44.9%) | 17 (24.6%) | 21 (30.4%) | 184 | 2.667 | 3 (4.3%) |

## 3. HT/FT outcome matrix
| HT result \ FT result | Home | Draw | Away | total |
|---|---|---|---|---|
| HT home lead | 89 (76.1%) | 19 (16.2%) | 9 (7.7%) | 117 |
| HT draw | 61 (36.7%) | 66 (39.8%) | 39 (23.5%) | 166 |
| HT away lead | 6 (7.6%) | 14 (17.7%) | 59 (74.7%) | 79 |
- *1 match(es) excluded (no HT score recorded).*

## 4. Comeback matches
- Home comebacks (trailing at HT, won at FT): **6** (1.7%)
- Away comebacks (trailing at HT, won at FT): **9** (2.5%)

### Home comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Dobrudzha | CSKA 1948 Sofia | 0-1 | 2-1 |
| 2025-2026 | Botev Plovdiv | Dobrudzha | 0-1 | 2-1 |
| 2025-2026 | CSKA Sofia | Botev Plovdiv | 0-1 | 2-1 |
| 2025-2026 | Lok. Sofia | Beroe | 0-1 | 2-1 |
| 2025-2026 | Botev Vratsa | Lok. Sofia | 1-2 | 3-2 |
| 2025-2026 | Septemvri Sofia | Yantra Gabrovo | 0-1 | 2-1 |

### Away comebacks
| season | home | away | HT | FT |
|---|---|---|---|---|
| 2025-2026 | Septemvri Sofia | Levski Sofia | 1-0 | 1-2 |
| 2025-2026 | Cherno More | Levski Sofia | 1-0 | 1-3 |
| 2025-2026 | Beroe | Cherno More | 1-0 | 1-2 |
| 2025-2026 | Lok. Sofia | Ludogorets | 1-0 | 1-3 |
| 2025-2026 | Spartak Varna | Beroe | 1-0 | 1-2 |
| 2025-2026 | Cherno More | Arda | 1-0 | 2-3 |
| 2026-2027 | Cherno More | Ludogorets | 1-0 | 2-3 |
| 2026-2027 | Lok. Plovdiv | Dunav Ruse | 1-0 | 1-2 |
| 2026-2027 | Slavia Sofia | CSKA 1948 Sofia | 1-0 | 1-2 |

## 5. HT lead conversion
| HT state | matches | converted to win | held as draw | collapsed to loss |
|---|---|---|---|---|
| Home lead | 117 | 89 (76.1%) | 19 (16.2%) | 9 (7.7%) |
| Away lead | 79 | 59 (74.7%) | 14 (17.7%) | 6 (7.6%) |

### Matches level at half-time
| FT result | count | pct |
|---|---|---|
| Home win | 61 | 36.7% |
| Draw | 66 | 39.8% |
| Away win | 39 | 23.5% |
- *1 match(es) excluded (no HT score recorded).*

## 6. First-goal timing
- Matches with a first-goal time recorded: `323` of `363` (89.0%)

Outcome distribution by first-goal timing bucket:
| bucket | matches | % of matches | home | draw | away |
|---|---|---|---|---|---|
| 1-15 | 97 | 26.7% | 50 (51.5%) | 18 (18.6%) | 29 (29.9%) |
| 16-30 | 71 | 19.6% | 31 (43.7%) | 13 (18.3%) | 27 (38.0%) |
| 31-45 | 56 | 15.4% | 30 (53.6%) | 11 (19.6%) | 15 (26.8%) |
| 46-60 | 48 | 13.2% | 21 (43.8%) | 10 (20.8%) | 17 (35.4%) |
| 61-75 | 32 | 8.8% | 12 (37.5%) | 7 (21.9%) | 13 (40.6%) |
| 76-90 | 14 | 3.9% | 9 (64.3%) | 1 (7.1%) | 4 (28.6%) |
| 91-120 | 5 | 1.4% | 3 (60.0%) | 0 (0.0%) | 2 (40.0%) |

## 7. Goalless matches
- Overall: **39** of `363` (10.7%)

| season | matches | goalless | pct |
|---|---|---|---|
| 2025-2026 | 294 | 36 | 12.2% |
| 2026-2027 | 69 | 3 | 4.3% |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_matches.py` to regenerate.*

## Charts

![matches_analysis_ht_ft_matrix](E:\football_data_analysis\data\analysis\bulgaria1\charts\matches_analysis_ht_ft_matrix.png)
![matches_analysis_home_win_rate](E:\football_data_analysis\data\analysis\bulgaria1\charts\matches_analysis_home_win_rate.png)

