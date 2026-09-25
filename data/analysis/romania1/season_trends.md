# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:43:12+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Superliga (Romania)
- Scope: league `romania1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Univ. Craiova | 82 | U. Cluj | 9 pts |
| 2026-2027 | Dinamo Bucuresti | 23 | FC Rapid Bucuresti | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Dinamo Bucuresti beat FC Rapid Bucuresti by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 9 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 13 = last safe, 16 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 13 | pos 16 |
|---|---|---|---|---|---|---|
| 2025-2026 | 82 | 73 | 68 | 64 | 45 | 34 |
| 2026-2027 | 23 | 21 | 19 | 14 | 11 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 13 | 45 | 14 | 42 | 3 pts |
| 2026-2027 | 13 | 11 | 14 | 10 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 350 | 887 | 2.534 | 44.3% | 27.4% | 28.3% | 7.1% | 49.74 |
| 2026-2027 | 79 | 208 | 2.633 | 55.7% | 26.6% | 17.7% | 8.9% | 13.5 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.684)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.316 | 7.684 |
| 2026-2027 | 1.500 | 5.125 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\romania1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\romania1\charts\season_trends_avg_goals.png)

