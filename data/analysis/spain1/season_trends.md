# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T16:08:52+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: LaLiga (Spain)
- Scope: league `spain1`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Barcelona | 94 | Real Madrid | 8 pts |
| 2026-2027 | Barcelona | 21 | Atl. Madrid | 5 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **0** of 2 seasons
- Tightest race: **2026-2027** - Barcelona beat Atl. Madrid by **5** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 8 pts |  |
| 2026-2027 | 5 pts |  |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 17 = last safe, 20 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 17 | pos 20 |
|---|---|---|---|---|---|---|
| 2025-2026 | 94 | 86 | 69 | 54 | 42 | 29 |
| 2026-2027 | 21 | 16 | 15 | 11 | 5 | 3 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 17 | 42 | 18 | 42 | 0 pts |
| 2026-2027 | 17 | 5 | 18 | 5 | 0 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 380 | 1024 | 2.695 | 48.9% | 24.5% | 26.6% | 3.9% | 52.35 |
| 2026-2027 | 69 | 210 | 3.043 | 44.9% | 24.6% | 30.4% | 7.2% | 9.5 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.200)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 3.400 | 4.300 |
| 2026-2027 | 3.600 | 6.200 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\spain1\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\spain1\charts\season_trends_avg_goals.png)

