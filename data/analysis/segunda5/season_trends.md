# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:46:39+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 5 (Spain)
- Scope: league `segunda5`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Rayo Majadahonda | 70 | San Sebastian Reyes | 0 pts |
| 2026-2027 | San Sebastian Reyes | 10 | RSD Alcala | 1 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Rayo Majadahonda beat San Sebastian Reyes by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 1 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 70 | 70 | 57 | 51 | 37 | 30 |
| 2026-2027 | 10 | 9 | 9 | 7 | 2 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 37 | 16 | 34 | 3 pts |
| 2026-2027 | 15 | 2 | 16 | 1 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 783 | 2.559 | 45.1% | 25.2% | 29.7% | 8.8% | 46.72 |
| 2026-2027 | 33 | 89 | 2.697 | 48.5% | 24.2% | 27.3% | 15.2% | 5.06 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.444)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.111 | 6.444 |
| 2026-2027 | 1.333 | 5.333 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda5\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda5\charts\season_trends_avg_goals.png)

