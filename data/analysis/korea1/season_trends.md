# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T11:02:49+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: K League 1 (South Korea)
- Scope: league `korea1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025 | Jeonbuk | 71 | Gimcheon Sangmu | 16 pts |
| 2026 | Seoul | 62 | Ulsan HD | 15 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026** - Seoul beat Ulsan HD by **15** pts

| season | margin | tight |
|---|---|---|
| 2025 | 16 pts |  |
| 2026 | 15 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 9 = last safe, 12 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 9 | pos 12 |
|---|---|---|---|---|---|---|
| 2025 | 71 | 55 | 51 | 44 | 40 | 27 |
| 2026 | 62 | 47 | 44 | 40 | 38 | 15 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025 | 9 | 40 | 10 | 38 | 2 pts |
| 2026 | 9 | 38 | 10 | 33 | 5 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025 | 198 | 512 | 2.586 | 41.9% | 26.3% | 31.8% | 8.1% | 45.17 |
| 2026 | 179 | 440 | 2.458 | 30.2% | 33.5% | 36.3% | 11.2% | 39.75 |

## 6. View divergence
- Largest divergence: **2026** (goals view, avg abs position diff = 4.167)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025 | 1.667 | 3.333 |
| 2026 | 2.333 | 4.167 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\korea1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\korea1\charts\season_trends_avg_goals.png)

