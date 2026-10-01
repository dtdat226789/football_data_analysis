# Season Trends Analysis
- Report: `season_trends`
- Generated: 2026-09-29T15:46:15+00:00
- Script: `backend/scripts/analyze_seasons.py` v1.0.0
- League: Championship (England)
- Scope: league `cha`

## 1. Champions per season
| season | champion | pts | runner-up | margin |
|---|---|---|---|---|
| 2025-2026 | Coventry | 95 | Ipswich | 11 pts |
| 2026-2027 | Swansea | 17 | West Ham | 2 pts |

## 2. Title-race tightness
- Tight races (margin <= 3 pts): **1** of 2 seasons
- Tightest race: **2026-2027** - Swansea beat West Ham by **2** pts

| season | margin | tight |
|---|---|---|
| 2025-2026 | 11 pts |  |
| 2026-2027 | 2 pts | yes |

## 3. Points thresholds
_Position-specific points per season. Key: 1 = champion, 2 = runner-up, 4 = CL line, 6 = Europa, 21 = last safe, 24 = bottom._

| season | pos 1 | pos 2 | pos 4 | pos 6 | pos 21 | pos 24 |
|---|---|---|---|---|---|---|
| 2025-2026 | 95 | 84 | 81 | 80 | 53 | 18 |
| 2026-2027 | 17 | 15 | 14 | 14 | 7 | 4 |

## 4. Relegation battle
| season | safe pos | safe pts | drop pos | drop pts | gap |
|---|---|---|---|---|---|
| 2025-2026 | 21 | 53 | 22 | 52 | 1 pts |
| 2026-2027 | 21 | 7 | 22 | 5 | 2 pts |

## 5. League-level trends
| season | matches | total goals | avg goals | home win | draw | away win | goalless | avg pts/team |
|---|---|---|---|---|---|---|---|---|
| 2025-2026 | 559 | 1445 | 2.585 | 41.7% | 26.7% | 31.7% | 6.6% | 63.54 |
| 2026-2027 | 95 | 277 | 2.916 | 41.1% | 30.5% | 28.4% | 7.4% | 10.67 |

## 6. View divergence
- Largest divergence: **2026-2027** (goals view, avg abs position diff = 6.750)

_Avg absolute position difference between classic view and alternative view per season._

| season | classic vs luck | classic vs goals |
|---|---|---|
| 2025-2026 | 4.083 | 4.583 |
| 2026-2027 | 3.417 | 6.750 |

---
*All statistics are computed from PostgreSQL tables (read-only). Run with `python backend/scripts/analyze_seasons.py` to regenerate.*

## Charts

![season_trends_champion_points](E:\football_data_analysis\data\analysis\cha\charts\season_trends_champion_points.png)
![season_trends_avg_goals](E:\football_data_analysis\data\analysis\cha\charts\season_trends_avg_goals.png)

