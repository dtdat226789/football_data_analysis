# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:55:38+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premier Division (Ireland)
- Scope: league `ireland1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Shamrock Rovers | 66 | Derry City | 3 pts |
| 2026 | St. Patricks | 59 | Shamrock Rovers | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2026** - St. Patricks beat Shamrock Rovers by **0** pts

| season | margin | tight |
|---|---|---|
| 2025 | 3 pts | yes |
| 2026 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025 | 66 | 63 | 54 | 51 | 41 | 24 |
| 2026 | 59 | 59 | 41 | 40 | 38 | 23 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 7 | 41 | 8 | 39 | 2 pts |
| 2026 | 7 | 38 | 8 | 34 | 4 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 180 | 437 | 2.428 | 42.8% | 28.9% | 28.3% | 8.3% | 48.8 |
| 2026 | 159 | 440 | 2.767 | 37.7% | 32.7% | 29.6% | 9.4% | 42.5 |

## 6. View divergence
- Largest divergence: **2025** (goals view, avg abs position diff = 4.000)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 2.600 | 4.000 |
| 2026 | 2.800 | 3.600 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\ireland1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\ireland1\charts\season_trends_avg_goals.png)

