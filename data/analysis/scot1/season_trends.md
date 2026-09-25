# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:44:55+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: League One (Scotland)
- Scope: league `scot1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Inverness | 74 | Stenhousemuir | 3 pts |
| 2026-2027 | Ross County | 19 | Hamilton | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Ross County beat Hamilton by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025-2026 | 74 | 71 | 59 | 43 | 42 | 29 |
| 2026-2027 | 19 | 19 | 13 | 9 | 8 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 7 | 42 | 8 | 38 | 4 pts |
| 2026-2027 | 7 | 8 | 8 | 7 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 191 | 511 | 2.675 | 41.9% | 27.2% | 30.9% | 5.2% | 37.0 |
| 2026-2027 | 39 | 103 | 2.641 | 48.7% | 23.1% | 28.2% | 10.3% | 10.8 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.571)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.286 | 4.571 |
| 2026-2027 | 1.000 | 2.600 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\scot1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\scot1\charts\season_trends_avg_goals.png)

