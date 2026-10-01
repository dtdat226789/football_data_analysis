# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:09:07+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Racing Santander | 88 | Malaga | 3 pts |
| 2026-2027 | Castellon | 19 | Eibar | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026-2027** - Castellon beat Eibar by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 3 pts | yes |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 19 = last safe, 22 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 19 | pos 22 |
|---|---|---|---|---|---|---|
| 2025-2026 | 88 | 85 | 79 | 77 | 44 | 37 |
| 2026-2027 | 19 | 18 | 14 | 13 | 5 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 19 | 44 | 20 | 40 | 4 pts |
| 2026-2027 | 19 | 5 | 20 | 4 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 509 | 1335 | 2.623 | 43.8% | 25.3% | 30.8% | 7.9% | 60.78 |
| 2026-2027 | 77 | 193 | 2.506 | 42.9% | 20.8% | 36.4% | 9.1% | 9.77 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 8.182)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.696 | 5.130 |
| 2026-2027 | 2.091 | 8.182 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\spain2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\spain2\charts\season_trends_avg_goals.png)

