# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:46:02+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Segunda RFEF - Group 3 (Spain)
- Scope: league `segunda3`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Baleares | 66 | Sant Andreu | 0 pts |
| 2026-2027 | Castellonense | 12 | Orihuela | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Baleares beat Sant Andreu by **0** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 0 pts | yes |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 15 = last safe, 18 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 15 | pos 18 |
|---|---|---|---|---|---|---|
| 2025-2026 | 66 | 66 | 55 | 52 | 33 | 27 |
| 2026-2027 | 12 | 10 | 8 | 6 | 1 | 0 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 15 | 33 | 16 | 30 | 3 pts |
| 2026-2027 | 15 | 1 | 16 | 1 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 306 | 742 | 2.425 | 45.8% | 31.7% | 22.5% | 10.8% | 45.61 |
| 2026-2027 | 31 | 68 | 2.194 | 41.9% | 29.0% | 29.0% | 6.5% | 4.67 |

## 6. View divergence
- Largest divergence: **2025-2026** (goals view, avg abs position diff = 6.556)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 2.111 | 6.556 |
| 2026-2027 | 1.333 | 5.111 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\segunda3\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\segunda3\charts\season_trends_avg_goals.png)

