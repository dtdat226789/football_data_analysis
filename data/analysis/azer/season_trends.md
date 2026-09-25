# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:55:07+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premier League (Azerbaijan)
- Scope: league `azer`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Sabah Baku | 78 | Qarabag | 9 pts |
| 2026-2027 | Neftci Baku | 15 | Sabah Baku | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Neftci Baku beat Sabah Baku by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 9 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025-2026 | 78 | 69 | 59 | 46 | 34 | 15 |
| 2026-2027 | 15 | 15 | 11 | 9 | 4 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 9 | 34 | 10 | 31 | 3 pts |
| 2026-2027 | 9 | 4 | 10 | 3 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 200 | 515 | 2.575 | 37.5% | 24.5% | 38.0% | 9.0% | 42.38 |
| 2026-2027 | 34 | 85 | 2.5 | 52.9% | 20.6% | 26.5% | 8.8% | 7.92 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 2.923)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.462 | 2.923 |
| 2026-2027 | 1.500 | 2.833 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\azer\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\azer\charts\season_trends_avg_goals.png)

