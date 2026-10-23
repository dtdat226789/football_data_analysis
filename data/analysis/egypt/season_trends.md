# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:48:33+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Premier League (Egypt)
- Scope: league `egypt`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Zamalek | 56 | Pyramids | 2 pts |
| 2026-2027 | Pyramids | 15 | Zamalek | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Zamalek beat Pyramids by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 2 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 56 | 54 | 53 | 48 | 32 | 25 |
| 2026-2027 | 15 | 13 | 12 | 10 | 3 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 32 | 18 | 31 | 1 pts |
| 2026-2027 | 17 | 3 | 18 | 2 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 322 | 651 | 2.022 | 33.9% | 37.9% | 28.3% | 15.8% | 40.19 |
| 2026-2027 | 50 | 103 | 2.06 | 38.0% | 20.0% | 42.0% | 10.0% | 7.0 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 4.762)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.429 | 4.762 |
| 2026-2027 | 1.700 | 4.100 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\egypt\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\egypt\charts\season_trends_avg_goals.png)

