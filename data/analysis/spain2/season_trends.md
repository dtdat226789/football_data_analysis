# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:48:15+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: LaLiga2 (Spain)
- Scope: league `spain2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Racing Santander | 88 | Malaga | 3 pts |
| 2026-2027 | Castellon | 16 | Eibar | 1 pts |

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
| 2026-2027 | 16 | 15 | 12 | 11 | 3 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 19 | 44 | 20 | 40 | 4 pts |
| 2026-2027 | 19 | 3 | 20 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 509 | 1335 | 2.623 | 43.8% | 25.3% | 30.8% | 7.9% | 60.78 |
| 2026-2027 | 66 | 163 | 2.47 | 40.9% | 21.2% | 37.9% | 10.6% | 8.36 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 7.909)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.696 | 5.130 |
| 2026-2027 | 2.182 | 7.909 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\spain2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\spain2\charts\season_trends_avg_goals.png)

