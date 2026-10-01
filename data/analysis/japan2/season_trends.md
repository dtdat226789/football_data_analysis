# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:59:38+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: J2 League (Japan)
- Scope: league `japan2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2024 | Shimizu S-Pulse | 82 | Yokohama FC | 6 pts |
| 2025 | Mito | 70 | V-Varen Nagasaki | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2025** - Mito beat V-Varen Nagasaki by **0** pts

| season | margin | tight |
|---|---|---|
| 2024 | 6 pts |  |
| 2025 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2024 | 82 | 76 | 66 | 64 | 40 | 18 |
| 2025 | 70 | 70 | 65 | 63 | 37 | 22 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2024 | 17 | 40 | 18 | 34 | 6 pts |
| 2025 | 17 | 37 | 18 | 37 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2024 | 380 | 946 | 2.489 | 40.8% | 23.4% | 35.8% | 9.7% | 52.55 |
| 2025 | 380 | 934 | 2.458 | 37.6% | 28.4% | 33.9% | 10.0% | 51.6 |

## 6. View divergence
- Largest divergence: **2024** (goals view, avg abs position diff = 6.400)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2024 | 2.700 | 6.400 |
| 2025 | 1.400 | 6.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\japan2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\japan2\charts\season_trends_avg_goals.png)

