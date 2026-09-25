# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:44:20+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Championship (Scotland)
- Scope: league `scot-champ`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | St Johnstone | 77 | Partick Thistle | 7 pts |
| 2026-2027 | Stenhousemuir | 19 | Partick Thistle | 4 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - Stenhousemuir beat Partick Thistle by **4** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 7 pts |  |
| 2026-2027 | 4 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025-2026 | 77 | 70 | 53 | 41 | 39 | 34 |
| 2026-2027 | 19 | 15 | 12 | 8 | 8 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 7 | 39 | 8 | 38 | 1 pts |
| 2026-2027 | 7 | 8 | 8 | 7 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 190 | 460 | 2.421 | 38.9% | 33.7% | 27.4% | 13.2% | 38.69 |
| 2026-2027 | 37 | 72 | 1.946 | 45.9% | 27.0% | 27.0% | 10.8% | 10.1 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.400)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.385 | 2.462 |
| 2026-2027 | 1.400 | 4.400 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\scot-champ\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\scot-champ\charts\season_trends_avg_goals.png)

