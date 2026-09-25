# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:45:28+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 1 (Spain)
- Scope: league `segunda1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Dep. Fabril | 69 | Oviedo B | 11 pts |
| 2026-2027 | Gernika | 7 | Bergantinos | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Gernika beat Bergantinos by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 69 | 58 | 55 | 51 | 40 | 15 |
| 2026-2027 | 7 | 7 | 6 | 6 | 3 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 40 | 16 | 36 | 4 pts |
| 2026-2027 | 15 | 3 | 16 | 2 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 776 | 2.536 | 41.5% | 27.5% | 31.0% | 9.2% | 46.33 |
| 2026-2027 | 27 | 71 | 2.63 | 44.4% | 18.5% | 37.0% | 3.7% | 4.22 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 7.667)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.222 | 7.667 |
| 2026-2027 | 0.778 | 6.000 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda1\charts\season_trends_avg_goals.png)

