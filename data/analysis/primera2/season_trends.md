# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:42:53+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Primera RFEF - Group 2 (Spain)
- Scope: league `primera2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Eldense | 69 | Sabadell | 1 pts |
| 2026-2027 | Villarreal B | 10 | Jaen | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Villarreal B beat Jaen by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 69 | 68 | 63 | 57 | 45 | 28 |
| 2026-2027 | 10 | 10 | 9 | 7 | 1 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 45 | 18 | 34 | 11 pts |
| 2026-2027 | 17 | 1 | 18 | 1 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 856 | 2.253 | 45.5% | 29.7% | 24.7% | 12.1% | 51.35 |
| 2026-2027 | 39 | 100 | 2.564 | 48.7% | 28.2% | 23.1% | 10.3% | 5.3 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 5.100)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.800 | 5.100 |
| 2026-2027 | 1.800 | 5.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\primera2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\primera2\charts\season_trends_avg_goals.png)

