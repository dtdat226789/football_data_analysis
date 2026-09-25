# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-23T13:49:27+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Challenge League (Switzerland)
- Scope: league `swiss2`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Vaduz | 81 | Aarau | 1 pts |
| 2026-2027 | Lausanne Ouchy | 21 | Winterthur | 3 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **2** of 2 seasons
- Tightest race: **2025-2026** - Vaduz beat Aarau by **1** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 1 pts | yes |
| 2026-2027 | 3 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 7 = last safe, 10 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 7 | pos 10 |
|---|---|---|---|---|---|---|
| 2025-2026 | 81 | 80 | 50 | 48 | 44 | 23 |
| 2026-2027 | 21 | 18 | 14 | 12 | 10 | 2 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 7 | 44 | 8 | 40 | 4 pts |
| 2026-2027 | 7 | 10 | 8 | 9 | 1 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 186 | 566 | 3.043 | 44.6% | 21.5% | 33.9% | 6.5% | 47.09 |
| 2026-2027 | 45 | 136 | 3.022 | 44.4% | 26.7% | 28.9% | 4.4% | 12.3 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 4.400)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 1.455 | 2.000 |
| 2026-2027 | 1.000 | 4.400 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\swiss2\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\swiss2\charts\season_trends_avg_goals.png)

