# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:04:19+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Primera RFEF - Group 1 (Spain)
- Scope: league `primera1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Tenerife | 79 | Celta Vigo B | 11 pts |
| 2026-2027 | UD Logrones | 13 | Lugo | 0 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - UD Logrones beat Lugo by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 0 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 79 | 68 | 61 | 59 | 43 | 28 |
| 2026-2027 | 13 | 13 | 11 | 8 | 3 | 1 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 43 | 18 | 41 | 2 pts |
| 2026-2027 | 17 | 3 | 18 | 3 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 398 | 974 | 2.447 | 45.7% | 28.4% | 25.9% | 9.8% | 51.48 |
| 2026-2027 | 50 | 133 | 2.66 | 46.0% | 26.0% | 28.0% | 6.0% | 6.85 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 7.200)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.857 | 6.857 |
| 2026-2027 | 1.100 | 7.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\primera1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\primera1\charts\season_trends_avg_goals.png)

