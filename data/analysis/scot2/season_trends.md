# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:45:10+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: League Two (Scotland)
- Scope: league `scot2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | East Kilbride | 69 | Spartans | 4 pts |
| 2026-2027 | Clyde | 17 | Stranraer | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Clyde beat Stranraer by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 4 pts |  |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025-2026 | 69 | 65 | 50 | 44 | 43 | 38 |
| 2026-2027 | 17 | 16 | 12 | 11 | 9 | 5 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 7 | 43 | 8 | 41 | 2 pts |
| 2026-2027 | 7 | 9 | 8 | 9 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 188 | 552 | 2.936 | 39.9% | 29.3% | 30.9% | 4.8% | 42.42 |
| 2026-2027 | 40 | 139 | 3.475 | 60.0% | 17.5% | 22.5% | 0.0% | 11.3 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.167)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.500 | 4.167 |
| 2026-2027 | 1.200 | 3.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\scot2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\scot2\charts\season_trends_avg_goals.png)

