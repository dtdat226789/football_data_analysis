# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T10:59:17+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Regionalliga North (Germany)
- Scope: league `germany-north`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Meppen | 83 | VfB Oldenburg | 11 pts |
| 2026-2027 | Phonix Lubeck | 23 | SC Weiche-08 | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Phonix Lubeck beat SC Weiche-08 by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 16 = last safe, 19 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 16 | pos 19 |
|---|---|---|---|---|---|---|
| 2025-2026 | 83 | 72 | 67 | 53 | 26 | 16 |
| 2026-2027 | 23 | 23 | 22 | 18 | 8 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 16 | 26 | 17 | 25 | 1 pts |
| 2026-2027 | 16 | 8 | 17 | 8 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 317 | 1152 | 3.634 | 42.6% | 21.8% | 35.6% | 2.5% | 46.42 |
| 2026-2027 | 91 | 357 | 3.923 | 40.7% | 22.0% | 37.4% | 1.1% | 13.32 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.421)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.053 | 6.421 |
| 2026-2027 | 2.947 | 5.474 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\germany-north\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\germany-north\charts\season_trends_avg_goals.png)

