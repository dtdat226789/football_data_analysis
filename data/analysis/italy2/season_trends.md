# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:57:37+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Serie B (Italy)
- Scope: league `italy2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Monza | 83 | Venezia | 1 pts |
| 2026-2027 | Palermo | 13 | Sudtirol | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Monza beat Venezia by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 83 | 82 | 75 | 55 | 41 | 35 |
| 2026-2027 | 13 | 11 | 10 | 7 | 5 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 41 | 18 | 37 | 4 pts |
| 2026-2027 | 17 | 5 | 18 | 4 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 390 | 993 | 2.546 | 44.9% | 31.0% | 24.1% | 7.7% | 52.45 |
| 2026-2027 | 50 | 132 | 2.64 | 42.0% | 26.0% | 32.0% | 2.0% | 6.85 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.300)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.200 | 6.300 |
| 2026-2027 | 2.000 | 6.100 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\italy2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\italy2\charts\season_trends_avg_goals.png)

